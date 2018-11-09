# Mystique_SexMenu //////////////////////////////////////////////////////////////////////
label Mystique_SexAct(Act = 0):    
    call Shift_Focus("Mystique")
    if Act == "masturbate":         
        call MystiqueM_Prep
        if not Situation:
            return        
    elif Act == "morningwood":
        # This action is called for by the label Mystique_Morning and returns to there
        $ newgirl["Mystique"].RecentActions.append("blow")           
        $ newgirl["Mystique"].DailyActions.append("blow")                          
        $ newgirl["Mystique"].DailyActions.append("morningwood")         
        call Mystique_MorningWood
        if Situation == "blow": 
            #If you selected to continue the BJ, then it calls the BJ actions
            $ Situation = 0
            call MystiqueBJ_Prep
        if not Situation:
            return
    elif Act == "kissing":        
        call Mystique_KissPrep
        if not Situation:
            return   
    elif Act == "breasts":        
        call Mystique_Fondle_Breasts
        if not Situation:
            return  
    elif Act == "blow":        
        call Mystique_BJ_Prep
        if not Situation:
            return  
    elif Act == "hand":        
        call MystiqueHJ_Prep
        if not Situation:
            return   
    elif Act == "sex":        
        call Mystique_SexPrep
        if not Situation:
            return   

label Mystique_SexMenu: 
    call CleartheRoom("Mystique",Check=1)
    # if _return >= 1:
    #         # if there are other girls in the room. . .
    #         ch_m "I don't really feel comfortable with these other girls around just yet."
    #         return  
    # elif Taboo:
    #         ch_m "I think this is a bit too exposed. . ."
    #         return          
    call Shift_Focus("Mystique")
    $ Trigger = 0    
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    $ Situation = 0
    call Mystique_Hide    
    $ newgirl["Mystique"].Girl_Arms = 1
    if "detention" in newgirl["Mystique"].RecentActions:
        $ Tempmod = 20 if Tempmod <= 20 else Tempmod
    call Set_The_Scene(Dress = 0)
#    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc):
#        alpha 1
#        zoom 1
#        offset (0,0)
#        anchor (0.5, 0.0)
    if not P_Semen:
        "You're a little out of juice at the moment, you might want to wait a bit." 
    if P_Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not newgirl["Mystique"].Action:
        "Mystique's looking a bit tired out, maybe let her rest a bit."
    
    if "caught" in newgirl["Mystique"].RecentActions or "angry" in newgirl["Mystique"].RecentActions:  
        ch_m "I'd rather not deal with you at the moment."
        call MystiqueOutfit        
        call DrainWord("Mystique","caught",1,0)
        return
        
    if Round < 5:
        ch_m "I think we could both do with a short break."   
        return
    menu Mystique_SMenu:  
        ch_m "So, what was it you hoped to do with?"
        "Do you want to make out?":
            if newgirl["Mystique"].Action:
                call Mystique_Makeout
            else:
                ch_m "I'm sorry, [newgirl[Mystique].Petname], but I need a break." 
        
        "Could I touch you?":
                if newgirl["Mystique"].Action:
                    call MystiqueFace("sly")                    
                    menu:
                        ch_m "Um, where do you want to touch, [newgirl[Mystique].Petname]?"                      
                        "Could I give you a massage?":
                                call Mystique_Massage                        
                        "Your breasts?":
                                call Mystique_Fondle_Breasts
                        "Your thighs?":
                                call Mystique_Fondle_Thighs
                        "Your pussy?":
                                call Mystique_Fondle_Pussy
                        "Your Ass?":
                                call Mystique_Fondle_Ass
                        "Never mind [[something else]":
                                jump Mystique_SMenu
                else:
                    ch_m "I'm sorry, [newgirl[Mystique].Petname], but I need a break."
                    
        "Could you take care of something for me? [[Your dick, you mean your dick]":        
                if P_Semen and newgirl["Mystique"].Action:                
                    menu:
                        ch_m "What do you want me to do?"
                        "Could you give me a handjob?":
                            call Mystique_Handjob
                        # "Could you give me a titjob?":
                        #     call Mystique_Titjob         
                        "Could you suck my cock?":
                            call Mystique_Blowjob 
                        "Could you use your feet?":
                            call Mystique_Footjob 
                        "Never mind [[something else]":
                            jump Mystique_SMenu
                elif not newgirl["Mystique"].Action:
                        "I'm sorry, [newgirl[Mystique].Petname], but I need a break."
                else:
                        "You really don't have it in you, maybe take a break." 
                # ch_m "Not if you mean \"your dick\".[[Not available yet]"
                
        "Could you put on a show for me?":
                    menu:
                        ch_m "What d0 you want to see?"
                        "Dance for me?":
                                if newgirl["Mystique"].Action:
                                    $ Count = 1
                                    call Mystique_Strip            
                                else:
                                    "I'm sorry, [newgirl[Mystique].Petname], but I need a break."
                                
                        "Could you undress for me?": 
                                    call Mystique_Undress  
                                            
                        "You've got a little something. . . [[clean-up]" if newgirl["Mystique"].Spunk:
                                    ch_m "Huh?"
                                    call Mystique_Cleanup
                                    
                        "Could I watch you get yourself off? [[masturbate]":
                                if newgirl["Mystique"].Action:
                                    call Mystique_Masturbate           
                                else:
                                    "I'm sorry, [newgirl[Mystique].Petname], but I need a break."
                        
                        "Never mind [[something else]":
                                jump Mystique_SMenu
                          
                
        "Could we maybe?. . . [[fuck]":
                if P_Semen and newgirl["Mystique"].Action:
                    menu:
                        "What do you want to do?"
                        "Lean back, I've got something in mind (Missionary). . .":
                                call Mystique_Sex_H           
                        "Fuck your pussy. (Missionary)":                        
                                call Mystique_Sex_P           
                        "Fuck your ass. (Missionary)":                        
                                call Mystique_Sex_A    
                        "Turn around, I've got something in mind (DoggyStyle). . .":
                                call Mystique_Doggy_H  
                        "Fuck your pussy. (DoggyStyle)":                        
                                call Mystique_Doggy_P           
                        "Fuck your ass. (DoggyStyle)":                        
                                call Mystique_Doggy_A 
                        "How about some toys? [[Pussy]":                        
                                call Mystique_Dildo_Pussy     
                        "How about some toys? [[Anal]":                        
                                call Mystique_Dildo_Ass   
                        "Never mind [[something else]":
                                jump Mystique_SMenu
                elif not newgirl["Mystique"].Action:
                        "I'm sorry, [newgirl[Mystique].Petname], but I need a break."
                else:
                        "The spirit is apparently willing, but the flesh is spongy and bruised." 
            #ch_m "Doubtful.[[Not available yet]"

        "Cheat Menu" if config.developer:                                                   #Remove
            call Mystique_Cheat_Menu
        "Never mind. [[exit]":         
                if newgirl["Mystique"].Lust >= 50 or newgirl["Mystique"].Addict >= 50:
                        call MystiqueFace("sad")
                        if newgirl["Mystique"].Action and newgirl["Mystique"].SEXP >= 15 and Round > 20:
                                if "round2" not in newgirl["Mystique"].RecentActions:  
                                    ch_m "Are you certain, [newgirl[Mystique].Petname]? Are you perhaps forgetting something?"                
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                                elif newgirl["Mystique"].Addict >= 50:                        
                                    ch_m "I need more of it." 
                                else:
                                    ch_m "I'm afraid that still wasn't enough."                          
                                menu:
                                    extend ""
                                    "Yeah, I'm done for now." if P_Semen and "round2" not in newgirl["Mystique"].RecentActions:                 
                                        if "unsatisfied" in newgirl["Mystique"].RecentActions and not newgirl["Mystique"].OCount:                                
                                            call MystiqueFace("angry")
                                            $ newgirl["Mystique"].Eyes = "side" 
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2)
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -4)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 1)
                                            ch_m "Well! This might count against you next time."
                                        else:                               
                                            call MystiqueFace("bemused", 1)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)   
                                            ch_m "I suppose I'll have to blame myself as an educator."  
                                    "I gave it a shot." if "round2" in newgirl["Mystique"].RecentActions:                 
                                        if "unsatisfied" in newgirl["Mystique"].RecentActions and not newgirl["Mystique"].OCount:                                
                                            call MystiqueFace("angry")
                                            $ newgirl["Mystique"].Eyes = "side"                                 
                                            ch_m "Yes, disappointingly so. . ."
                                        else:                               
                                            call MystiqueFace("bemused", 1) 
                                            ch_m "I suppose you did. . .shame you couldn't do better. . ."  
                                    "Hey, I did my part." if newgirl["Mystique"].OCount > 2:      
                                        call MystiqueFace("sly", 1) 
                                        ch_m "Take it as a compliment that I expected more."  
                                    "I'm tapped out for the moment, let's try again later." if not P_Semen:
                                        call MystiqueFace("normal")                        
                                        ch_m "I suppose that can't be helped. . ."
                                    "Ok, we can try something else." if MultiAction and "round2" not in newgirl["Mystique"].RecentActions:
                                        call MystiqueFace("smile")
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1) 
                                        ch_m "Excellent. . ."                            
                                        $ newgirl["Mystique"].RecentActions.append("round2")                      
                                        $ newgirl["Mystique"].DailyActions.append("round2") 
                                        jump Mystique_SexMenu
                                    "Again? Ok, fine." if MultiAction and "round2" in newgirl["Mystique"].RecentActions:
                                        call MystiqueFace("sly")
                                        ch_m "Always. . ."           
                                        jump Mystique_SexMenu  
                                #End "if Mystique is still up for more"
                        else:  
                                call MystiqueFace("bemused", 1)
                                ch_m "I suppose I'm tired as well, [newgirl[Mystique].Petname]. We can take a breather. . ."  
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)    
                        call MystiqueFace
                else:
                    ch_m "Fine."
                    
                $ newgirl["Mystique"].OCount = 0    
                call Mystique_Cleanup
                if newgirl["Mystique"].LooksLike != "Raven":
                    $ newgirl["Mystique"].LooksLike = "Raven"
                    "Mystique turns back into her human form"
                call MystiqueOutfit
                return
    if newgirl["Mystique"].Loc != bg_current:
        call Set_The_Scene
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    if not MultiAction:    
        call Set_The_Scene
        ch_m "That's all you get. . . for now."
        $ newgirl["Mystique"].OCount = 0
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    jump Mystique_SexMenu
# end Mystique_SexMenu //////////////////////////////////////////////////////////////////////            

label Mystique_Cheat_Menu:
    menu:
        "Level-Up":
            $ newgirl["Mystique"].Hand += 5
            $ newgirl["Mystique"].Blow += 5
            $ newgirl["Mystique"].Swallow += 5
            $ newgirl["Mystique"].Hand += 5
            $ newgirl["Mystique"].Slap += 5
            $ newgirl["Mystique"].Tit += 5
            $ newgirl["Mystique"].Sex += 5
            $ newgirl["Mystique"].Anal += 5
            $ newgirl["Mystique"].Hotdog += 5
            $ newgirl["Mystique"].Mast += 5
            $ newgirl["Mystique"].Org += 5
            $ newgirl["Mystique"].FondleB += 5
            $ newgirl["Mystique"].FondleT += 5
            $ newgirl["Mystique"].FondleP += 5
            $ newgirl["Mystique"].FondleA += 5
            $ newgirl["Mystique"].DildoP += 5
            $ newgirl["Mystique"].DildoA += 5
            $ newgirl["Mystique"].Plug += 5
            $ newgirl["Mystique"].SuckB += 5
            $ newgirl["Mystique"].InsertP += 5
            $ newgirl["Mystique"].InsertA += 5
            $ newgirl["Mystique"].LickP += 5    
            $ newgirl["Mystique"].LickA += 5
            $ newgirl["Mystique"].Blow += 5
            $ newgirl["Mystique"].Swallow += 5
            $ newgirl["Mystique"].CreamP += 5
            $ newgirl["Mystique"].CreamA += 5
            $ newgirl["Mystique"].SeenChest = 1
            $ newgirl["Mystique"].SeenPanties = 1
            $ newgirl["Mystique"].SeenPussy = 1
            "Hand [newgirl[Mystique].Hand], Blow [newgirl[Mystique].Blow], Swallow [newgirl[Mystique].Swallow]"
        "Level Reset":
            $ newgirl["Mystique"].Hand = 0
            $ newgirl["Mystique"].Blow = 0
            $ newgirl["Mystique"].Swallow = 0
            "Hand [newgirl[Mystique].Hand], Blow [newgirl[Mystique].Blow], Swallow [newgirl[Mystique].Swallow]"
        "Toggle Taboo":
            if not Taboo:
                $ Taboo = 40
            else:
                $ Taboo = 0
        "Maxed":
                $ newgirl["Mystique"].Love = 1000
                $ newgirl["Mystique"].Inbt = 1000
                $ newgirl["Mystique"].Obed = 1000
                $ newgirl["Mystique"].Lust = 50
                $ newgirl["Mystique"].Addict = 0 #how addicted she is
                $ newgirl["Mystique"].Addictionrate = 0 #How faster her addiciton rises
                $ newgirl["Mystique"].Kissed = 1 #How many times they've kissed
                $ newgirl["Mystique"].Swallow = 0
        "50\%":
                $ newgirl["Mystique"].Love = 500
                $ newgirl["Mystique"].Inbt = 500
                $ newgirl["Mystique"].Obed = 500
                $ newgirl["Mystique"].Lust = 65
                $ newgirl["Mystique"].Addict = 0 #how addicted she is
                $ newgirl["Mystique"].Addictionrate = 10 #How faster her addiciton rises
                $ newgirl["Mystique"].Kissed = 10 #How many times they've kissed
                $ newgirl["Mystique"].Swallow = 0
        "25\%":
                $ newgirl["Mystique"].Love = 250
                $ newgirl["Mystique"].Inbt = 250
                $ newgirl["Mystique"].Obed = 250
                $ newgirl["Mystique"].Lust = 85
                $ newgirl["Mystique"].Addict = 10 #how addicted she is
                $ newgirl["Mystique"].Addictionrate = 50 #How faster her addiciton rises
                $ newgirl["Mystique"].Kissed = 10 #How many times they've kissed
                $ newgirl["Mystique"].Swallow = 0
        "Juice up":
            $ P_Semen += 5
            $ newgirl["Mystique"].Action = 10
        "Cold Shower":
            $ P_Focus = 0
        "Exit":
            return
    jump Mystique_Cheat_Menu
    return
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
label Mystique_Jackin(Cnt = 0, TempVar = 0):
    if "unseen" in newgirl["Mystique"].RecentActions:        
            $ P_RecentActions.append("cockout") 
            $ Trigger2 = "jackin"
            if not renpy.showing("Chibi_UI"):
                        show Chibi_UI
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
                    call Mystique_First_Peen
            
            if not renpy.showing("Chibi_UI"):
                        show Chibi_UI
            $ Trigger2 = "jackin"
            if "jackin" in newgirl["Mystique"].RecentActions:
                return            
            $ newgirl["Mystique"].RecentActions.append("jackin")
            $ newgirl["Mystique"].DailyActions.append("jackin") 
            
            if newgirl["Mystique"].SEXP < 10 and "classcaught" not in newgirl["Mystique"].History:
                    call MystiqueFace("surprised", 1) 
                    $ newgirl["Mystique"].Eyes = "down"
                    "Wait,"
                    call MystiqueFace("angry", 1)                     
                    ch_m "That really isn't appropriate."  
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 7) 
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")  
                    $ renpy.pop_call()
                    return
            elif newgirl["Mystique"].SEXP <= 15:            
                    call MystiqueFace("surprised", 1) 
                    $ newgirl["Mystique"].Eyes = "down"
                    "Mystique looks down at your cock with some surprise."
                    call MystiqueFace("perplexed", 0) 
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 10)
            elif ApprovalCheck("Mystique", 1200, TabM = 3):
                    call MystiqueFace("surprised", 1) 
                    $ newgirl["Mystique"].Eyes = "down"
                    "Mystique looks down at your cock and smiles."            
                    call MystiqueFace("sly", 0) 
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 12)
            elif ApprovalCheck("Mystique", 500, "I", TabM=2):
                    call MystiqueFace("surprised", 1) 
                    $ newgirl["Mystique"].Eyes = "down"
                    "Mystique glances at it, but just smiles in amusement."        
                    call MystiqueFace("sly", 0) 
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 15)
            else:
                    call MystiqueFace("angry", 1) 
                    $ newgirl["Mystique"].Eyes = "down"
                    "Mystique glances down at your cock with a scowl."    
                    call MystiqueFace("angry", 0)
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")  
                    return
            
            if newgirl["Mystique"].Action:
                $ Options = ["none"]
                
                if newgirl["Mystique"].Hand >= 5 and ApprovalCheck("Mystique", 1200, TabM = 3):
                        $ Cnt = newgirl["Mystique"].Hand - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("hand") 
                            $ Cnt -= 1
                if newgirl["Mystique"].Blow >= 5 and ApprovalCheck("Mystique", 1400, TabM = 3):
                        $ Cnt = newgirl["Mystique"].Blow - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if "hungry" in newgirl["Mystique"].Traits else 0
                        while Cnt:
                            $ Options.append("blow") 
                            $ Cnt -= 1
                if newgirl["Mystique"].Tit >= 5 and ApprovalCheck("Mystique", 1300, TabM = 5):
                        $ Cnt = newgirl["Mystique"].Tit - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("Tit") 
                            $ Cnt -= 1
                if newgirl["Mystique"].Sex >= 5 and ApprovalCheck("Mystique", 1500, TabM = 5):
                        $ Cnt = newgirl["Mystique"].Sex - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if newgirl["Mystique"].Lust >= 70 else 0
                        while Cnt:
                            $ Options.append("sex") 
                            $ Cnt -= 1
                if newgirl["Mystique"].Anal >= 5 and ApprovalCheck("Mystique", 1700, TabM = 5):
                        $ Cnt = newgirl["Mystique"].Anal - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].Loose else 0
                        while Cnt:
                            $ Options.append("anal") 
                            $ Cnt -= 1
                    
                $ renpy.random.shuffle(Options) 
                                
                $ TempVar = Options[0]  
                $ del Options[:]  
                
                if TempVar == "hand":
                        ch_m "Would you like a hand with that?"
                elif TempVar == "blow":
                        ch_m "I wouldn't mind a taste of that. . ."
                elif TempVar == "tit":
                        ch_m "If you like, I could use my chest. . ."
                elif TempVar == "sex":
                        ch_m "I'm positively dripping here. . ."
                elif TempVar == "anal":
                        ch_m "I wouldn't mind you using the back door. . ."
                else:
                        ch_m "Mmmmm. . ."
                        return
                    
                menu:
                    extend ""
                    "No thanks, I've got this in hand.":
                        call MystiqueFace("perplexed", 1)  
                        ch_m "Oh. . ."      
                        ch_m "Carry on then, [newgirl[Mystique].Petname]."
                        call MystiqueFace("sly", 0, Eyes="down") 
                        return
                    "Hmm, sounds like a plan.": 
                        $ Situation = "shift"
                
                $ Trigger2 = 0
                    
                #Close out what you were doing 
                if Trigger == "strip":
                        $ Count = 0
                        $ newgirl["Mystique"].Action -= 1    
                        $ newgirl["Mystique"].SpriteLoc = StageRight 
                elif Trigger == "masturbation":
                        $ newgirl["Mystique"].Action -= 1
                        $ newgirl["Mystique"].Mast += 1    
                        call Checkout
                else:
                        call CloseOut("Mystique")
                                
                show blackscreen onlayer black
                hide blackscreen onlayer black
                if TempVar == "hand":                
                        jump MystiqueHJ_Prep
                elif TempVar == "blow":
                        jump MystiqueBJ_Prep
                elif TempVar == "tit":
                        jump MystiqueTJ_Prep
                elif TempVar == "sex":
                        jump Mystique_Doggy_SexPrep
                elif TempVar == "anal":
                        jump Mystique_Doggy_AnalPrep
    return
# End Mystique "jackin it" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
 
label Mystique_TouchCheek:  
    call Shift_Focus("Mystique")
    call MystiqueFace("surprised", 1) 
    if "no cheek" in newgirl["Mystique"].DailyActions:
            "You reach out to brush Mystique's face with your hand, but she slaps it away."
            if P_Lvl < 4:
                $ newgirl["Mystique"].LooksLike = "Mystique"
                call NewGirl_RemoveClothes("Mystique")
                "As soon as your hands touch she turns back into her original form and her clothes vanish"
            call MystiqueFace("angry")
            ch_m "What are you doing, [newgirl[Mystique].Petname]?"
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -2)
            if P_Lvl < 4:
                $ newgirl["Mystique"].LooksLike = "Raven"
                call MystiqueOutfit
            return
    else:
            "You reach out and brush Mystique's face with your hand."
            if P_Lvl < 4:
                $ newgirl["Mystique"].LooksLike = "Mystique"
                call NewGirl_RemoveClothes("Mystique")
                "As soon as your hand touchs her, she turns back into her original form and her clothes vanish"
    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)    
    if "addict Mystique" in P_Traits:
        $ newgirl["Mystique"].Addict -= 2            
        $ newgirl["Mystique"].Addictionrate += 1 if newgirl["Mystique"].Addictionrate < 5 else newgirl["Mystique"].Addictionrate 
        $ newgirl["Mystique"].Addictionrate = 3 if newgirl["Mystique"].Addictionrate < 3 else newgirl["Mystique"].Addictionrate 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)
    else:
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 40, 5)
        
    if ApprovalCheck("Mystique", 1000):
        call MystiqueFace("sexy", 1)
        ch_m "That's sweet, what was it for, [newgirl[Mystique].Petname]?"
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
    elif ApprovalCheck("Mystique", 800) or ApprovalCheck("Mystique", 700, "L"):
        call MystiqueFace("smile", 1)
        ch_m "Mmmmm. . ."      
    elif "cheek" in newgirl["Mystique"].DailyActions:        
        call MystiqueFace("angry", 1)
        ch_m "I won't warn you again, [newgirl[Mystique].Petname]."
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -2)
        $ newgirl["Mystique"].DailyActions.append("no cheek")
    elif ApprovalCheck("Mystique", 400):
        $ newgirl["Mystique"].Mouth = "smile"
        $ newgirl["Mystique"].Brows = "normal"
        ch_m "Hmm, maybe we need to discuss \"boundaries.\""
    else:
        call MystiqueFace("angry", 1)
        ch_m "That's inappropriate behavior, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)

    if P_Lvl < 4:
        $ newgirl["Mystique"].LooksLike = "Raven"
        call MystiqueOutfit
    
    if "no cheek" in newgirl["Mystique"].DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Mystique", 300):
                    call MystiqueFace("sexy", 1)
                    ch_m "See that it doesn't."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                else:
                    call MystiqueFace("angry", 1)
                    $ newgirl["Mystique"].Eyes = "side"
                    ch_m "I'm sure."                 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck("Mystique", 400, "OI") or ApprovalCheck("Mystique", 800):
                    call MystiqueFace("normal", 1)
                    $ newgirl["Mystique"].Eyes = "squint"
                    ch_m "Don't presume. . . so much."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -1) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)                        
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                else:
                    call MystiqueFace("angry", 2)
                    $ newgirl["Mystique"].Eyes = "squint"
                    ch_m "You {i}must{/i} be daydreaming."  
                    $ newgirl["Mystique"].Blush = 1
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -3) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 3)                        
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
    else:
        menu:
            "Sorry, you looked so lovely.":
                if ApprovalCheck("Mystique", 850, "LI"):
                    call MystiqueFace("sexy", 1)
                    ch_m "Don't make promises you can't keep."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                elif ApprovalCheck("Mystique", 500, "LI"):
                    call MystiqueFace("smile", 1)
                    ch_m "You don't look so bad yourself, [newgirl[Mystique].Petname]."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                else:
                    call MystiqueFace("angry", 1)
                    $ newgirl["Mystique"].Eyes = "side"
                    ch_m "Obviously."                 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)   
                    
            "You had a fly on you.":
                if ApprovalCheck("Mystique", 700, "LI"):
                    call MystiqueFace("sexy", 1)
                    ch_m "Oh? I'm {i}sure{/i} that was it. . ."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, 1)                        
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 1)
                elif ApprovalCheck("Mystique", 700):
                    call MystiqueFace("normal")
                    ch_m "A fly, right. . ."
                else:
                    call MystiqueFace("angry", 1)
                    ch_m "That's no excuse." 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)    
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Mystique", 850):
                    call MystiqueFace("sexy", 1)
                    $ newgirl["Mystique"].Eyes = "side"
                    ch_m "I'd need to try again to be sure. . ."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 1)                        
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 1)
                elif ApprovalCheck("Mystique", 500, "OI"):
                    call MystiqueFace("normal", 1)
                    ch_m "Don't push it. . . too far."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)                        
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                else:
                    call MystiqueFace("angry", 1)
                    $ newgirl["Mystique"].Eyes = "side"
                    ch_m "Certain."   
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -3)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 3)                        
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)   
            
    $ newgirl["Mystique"].RecentActions.append("cheek")
    $ newgirl["Mystique"].DailyActions.append("cheek")
    return
# End Mystique "touch cheek" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    
# Slap Ass

label Mystique_Slap_Ass:
    call Shift_Focus("Mystique")
    $ renpy.play('sounds/slap.mp3')
    # fix add sound here?
    if renpy.showing("Mystique_SexSprite"):
            show Mystique_SexSprite #fix, test this
            with vpunch
    if renpy.showing("Mystique_Doggy"):
            show Mystique_Doggy #fix, test this
            with vpunch
    elif renpy.showing("Mystique_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Mystique_BJ_Animation
            with vpunch
    elif renpy.showing("Mystique_TJ_Animation"):
            show Mystique_TJ_Animation  
            with vpunch
    elif renpy.showing("Mystique_HJ_Animation"):
            show Mystique_HJ_Animation  
            with vpunch
    else:
            show Mystique_Sprite
            with vpunch
    $ newgirl["Mystique"].Slap += 1                               #add in slap-base obedience        
    $ newgirl["Mystique"].Spank += 1    
    if ApprovalCheck("Mystique", 300, "O", TabM=1):   
        call MystiqueFace("sexy", 1)  
        $ newgirl["Mystique"].Mouth = "surprised"
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 51, 3, 1)
        if Action_Check("Mystique", "recent", "slap") < 4:
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2) if newgirl["Mystique"].Slap <= 5 else newgirl["Mystique"].Obed
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1) if newgirl["Mystique"].Slap <= 10 else newgirl["Mystique"].Obed
        $ Line = "You slap her ass and she jumps with pleasure"
        if renpy.showing("Mystique_Doggy"):
            #$ Line2 = "This feels good"
            if newgirl["Mystique"].Spank == 1:
                $ Line2 = "This feels good" 
            elif newgirl["Mystique"].Spank < 4:
                $ Line2 = "Keep hitting me"
            elif newgirl["Mystique"].Spank < 10:
                $ Line2 = "Harder!"  
            else:
                $ Line2 = "Don't stop, " + newgirl["Mystique"].Petname
    else:                
        call MystiqueFace("surprised", 1)        
        if Action_Check("Mystique", "recent", "slap") < 4:
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)        
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1)
        $ Line = "You slap her ass and she looks back at you a bit startled" 
        if renpy.showing("Mystique_Doggy"):
            if newgirl["Mystique"].Spank == 1:
                $ Line2 = newgirl["Mystique"].Petname + "?" 
            elif newgirl["Mystique"].Spank < 4:
                $ Line2 = "Ouch"
            elif newgirl["Mystique"].Spank < 10:
                $ Line2 = "This hurts, " + newgirl["Mystique"].Petname
            else:
                $ Line2 = "Please stop, " + newgirl["Mystique"].Petname 
    
    if Taboo:    
        "[Line]."
        if renpy.showing("Mystique_Doggy"):
            ch_m "[Line2]"
            $ Line2 = 0
        if not ApprovalCheck("Mystique", 900, TabM=3) and "public" not in newgirl["Mystique"].History:
            call MystiqueFace("angry",1)
            if newgirl["Mystique"].Slap <= 5:
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)  
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)      
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2)    
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1)
            $ Line = "She looks pretty mad though"  
        elif not ApprovalCheck("Mystique", 1500, TabM=3) and "public" not in newgirl["Mystique"].History:
            call MystiqueFace("bemused",2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2) if newgirl["Mystique"].Slap <= 5 else newgirl["Mystique"].Obed
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -1)
            $ Line = "She looks a bit embarrassed"  
            $ newgirl["Mystique"].Blush = 1
        else:                         #Over 1500
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Mouth = "smile"
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1) if newgirl["Mystique"].Slap <= 5 else newgirl["Mystique"].Obed
            $ Line = "She gives you a naughty grin" 
        
    #if not Trigger:
    "[Line]."
    if P_Lvl < 4:
            $ newgirl["Mystique"].LooksLike = "Mystique"
            call NewGirl_RemoveClothes("Mystique")
            "As soon as your hand touchs her butt she turns back into her original form and her clothes vanish"
    $ Line = 0
    if renpy.showing("Mystique_Doggy") and Line2:
        ch_m "[Line2]"
        $ Line2 = 0
        
    $ newgirl["Mystique"].RecentActions.append("slap") if Action_Check("Mystique", "recent", "slap") < 4 else newgirl["Mystique"].RecentActions
    $ newgirl["Mystique"].DailyActions.append("slap") if Action_Check("Mystique", "daily", "slap") < 10 else newgirl["Mystique"].DailyActions
        
    return
    
# Tag end ////////////////////////////////////////////////////////////////////////


# Mystique_Makeout //////////////////////////////////////////////////////////////////////
label Mystique_Makeout:
    call Shift_Focus("Mystique")
    
    $ Approval = ApprovalCheck("Mystique", 700, TabM=1) # 50, 65, 80, Taboo -40(90)
    
    if Approval > 1 and not newgirl["Mystique"].Kissed and not newgirl["Mystique"].Forced:        
        call MystiqueFace("sexy")
        $ newgirl["Mystique"].Eyes = "side"
        ch_m "Well, I suppose it couldn't hurt. . ."
    elif Approval and not newgirl["Mystique"].Kissed:        
        call MystiqueFace("sexy")
        $ newgirl["Mystique"].Eyes = "side"
        ch_m "We could. . ."   
    elif Approval and "kissing" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy", 1)
            ch_m "Mmmm. . ."
            jump Mystique_KissPrep
    elif Approval and "kissing" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["Mmmm. . .",       
            "Didn't get enough earlier?",
            "Come and get it."]) 
        ch_m "[Line]"            
    elif Approval > 1 and newgirl["Mystique"].Love > newgirl["Mystique"].Obed:       
        call MystiqueFace("sexy")
        ch_m "Mwa."            
    elif ApprovalCheck("Mystique", 500, "O") and newgirl["Mystique"].Obed > newgirl["Mystique"].Love:
        call MystiqueFace("normal")
        ch_m "Of course."
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
    elif ApprovalCheck("Mystique", 300, "O") and ApprovalCheck("Mystique", 200, "L"):
        call MystiqueFace("sexy")
        ch_m "Ok, fine."
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
    elif newgirl["Mystique"].Addict >= 50:
        call MystiqueFace("sexy")
        $ newgirl["Mystique"].Eyes = "manic"
        ch_m ". . . yes."    
    elif Approval:       
        call MystiqueFace("bemused")
        ch_m "Very well." 
    else:        
        call MystiqueFace("normal") # Else
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "Hmmm, no."
        $ newgirl["Mystique"].RecentActions.append("no kissing")                      
        $ newgirl["Mystique"].DailyActions.append("no kissing") 
        return    
        
label Mystique_KissPrep:    
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 10, 1)
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 1)
    call Mystique_Kissing_Launch("kissing")
    if newgirl["Mystique"].Kissed >= 10 and newgirl["Mystique"].Inbt >= 300:
        call MystiqueFace("sucking")
    elif newgirl["Mystique"].Kissed > 1 and newgirl["Mystique"].Addict >= 50:
        call MystiqueFace("sucking")
    else:
        call MystiqueFace("kiss")
    if newgirl["Mystique"].Kissed >= 10:
        "She's all over you, running her hands along your body."  
    elif newgirl["Mystique"].Kissed > 7:
        "She's really sucking face."
    elif newgirl["Mystique"].Kissed > 3:
        "She's really getting into it."
    else:
        "You and Mystique make out for a while."    
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no kissing")
    $ newgirl["Mystique"].RecentActions.append("kissing")                      
    $ newgirl["Mystique"].DailyActions.append("kissing") 
    if not newgirl["Mystique"].Kissed: 
        $ newgirl["Mystique"].Addict -= 5       
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, 25)            
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 20)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 20)
        jump Mystique_Kiss_After
    $ Trigger = "kissing"
    $ Line = 0
    $ Cnt = 0
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
     
label Mystique_KissCycle:
    while Round >=0:
        call Shift_Focus("Mystique")
        call Mystique_Kissing_Launch("kissing")       
        call MystiqueLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                  
        if Line:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                pass                
                        "Move a hand to her breasts. . ." if newgirl["Mystique"].Kissed >= 5 and MultiAction:
                                if newgirl["Mystique"].Action and MultiAction:
                                    $ Situation = "auto"
                                    call Mystique_Kiss_After
                                    call Mystique_Fondle_Breasts                          
                                    if Trigger == "fondle breasts": 
                                        $ Trigger2 = "kissing"                                   
                                        call Mystique_FB_Prep        
                                    else: 
                                        $ Trigger = "kissing"
                                else:
                                    "As your hands creep upwards, she grabs your wrists."
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        "Move a hand to her thighs. . ." if newgirl["Mystique"].Kissed >= 5 and MultiAction:
                                if newgirl["Mystique"].Action and MultiAction:
                                    $ Situation = "auto"
                                    call Mystique_Kiss_After
                                    call Mystique_Fondle_Thighs   
                                    if Trigger == "fondle thighs": 
                                        $ Trigger2 = "kissing"      
                                        call Mystique_FT_Prep  
                                    else: 
                                        $ Trigger = "kissing"    
                                else:
                                    "As your hands creep downwards, she grabs your wrists."
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?" 
                        
                        "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                call Mystique_Jackin
                        
                        "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                "You stop jack'in it."
                                $ Trigger2 = 0
                          
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                
                        "Maybe lose some clothes. . .":
                                    call Mystique_Undress  
                                    
                        "Let's try something else." if MultiAction and newgirl["Mystique"].Kissed >= 5:   
                                $ Situation = "shift"
                                jump Mystique_Kiss_After
                        "Let's stop for now.": 
                                jump Mystique_Kiss_After
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                                           
                    "[Line]"    
                    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Pos_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_Kiss_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                                                
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Kiss_After            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump Mystique_Kiss_After   
                
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
label Mystique_Kiss_After:
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].Kissed += 1
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    
    call LikeUpdater("Mystique",1)
    
    if "kissing" not in newgirl["Mystique"].RecentActions:
        if newgirl["Mystique"].Love > 300:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, 4)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)
        $ newgirl["Mystique"].RecentActions.append("kissing")                      
        $ newgirl["Mystique"].DailyActions.append("kissing") 
     
    if newgirl["Mystique"].Kissed > 10: 
            pass        
    elif newgirl["Mystique"].Kissed == 10:
            call MystiqueFace("smile", 1)        
            ch_m "This has been a pleasant surprise."
    elif newgirl["Mystique"].Kissed == 5:
            ch_m "You're surprisingly talented. . ." 
    elif newgirl["Mystique"].Kissed == 1:    
            $ newgirl["Mystique"].SEXP += 1 
        
    if not Situation and newgirl["Mystique"].Kissed > 5 and newgirl["Mystique"].Lust > 50 and ApprovalCheck("Mystique", 950):
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "sad"
            ch_m "Does that satisfy you, [newgirl[Mystique].Petname]?"  
     
    $ Tempmod = 0  
    if Situation:
        ch_m "What were you considering?"
    else:
        call Mystique_Pos_Reset  
    call Checkout
    return


# end Makeout //////////////////////////////////////////////////////////////////////

            

##  newgirl["Mystique"].Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label Mystique_Masturbate: #(Situation = Situation):
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Mast:
        $ Tempmod += 10
    if newgirl["Mystique"].SEXP >= 50:
        $ Tempmod += 25
    elif newgirl["Mystique"].SEXP >= 30:
        $ Tempmod += 15
    elif newgirl["Mystique"].SEXP >= 15:
        $ Tempmod += 5
    if newgirl["Mystique"].Lust >= 90:
        $ Tempmod += 20
    elif newgirl["Mystique"].Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in newgirl["Mystique"].Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:        
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount   
        
    $ Approval = ApprovalCheck("Mystique", 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    call DrainWord("Mystique","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and newgirl["Mystique"].Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if P_Semen and newgirl["Mystique"].Action:
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                                call MystiqueFace("sexy")
                                ch_m "Hm, well I do have my hands full with these. . ."                  
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ newgirl["Mystique"].Mast += 1
                                jump MystiqueM_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if P_Semen and newgirl["Mystique"].Action:
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                                call MystiqueFace("sexy")
                                ch_m "I suppose I could use some added attention. . ."                
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ newgirl["Mystique"].Mast += 1
                                jump MystiqueM_Cycle
                        "Why don't we take care of each other?" if P_Semen and newgirl["Mystique"].Action:
                                call MystiqueFace("sexy")
                                ch_m "I suppose I could spare some attention. . ."                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if newgirl["Mystique"].Lust >= 50:
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)      
                                    call MystiqueFace("sexy")
                                    ch_m "So you prefer to watch. . ."                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5)  
                                    jump MystiqueM_Cycle
                                elif ApprovalCheck("Mystique", 1200):
                                    call MystiqueFace("sly")                        
                                    ch_m "I did, but I wasn't intending perfomance art."
                                else:
                                    call MystiqueFace("angry")
                                    ch_m "I did, but now the mood is ruined. . ."
                                    
                #else: You've failed all checks so she kicks you out.
                $ newgirl["Mystique"].Girl_Arms = 1  
                call MystiqueOutfit  
                $ newgirl["Mystique"].Action -= 1
                $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        call MystiqueFace("bemused", 1)
                        if bg_current == "bg Mystique":
                            ch_m "Why are you even in my room?"   
                        else:
                            ch_m "I wasn't expecting visitors. . ." 
                        $ newgirl["Mystique"].Blush = 0
                else:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                        call MystiqueFace("angry")
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")  
                        if bg_current == "bg Mystique":
                            ch_m "You may have noticed, I had soem work to take care of, so if you'll leave me to it. . ."
                            "Mystique kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_m "I think I'll be leaving, if you don't mind."                            
                            hide Mystique with easeoutright
                            call Remove_Girl("Mystique")
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
                if Approval > 2:                                                      # fix, add Mystique auto stuff here
                        if newgirl["Mystique"].Legs == "skirt":
                            "Mystique's hand snakes down her body, and hikes up her skirt."
                            $ newgirl["Mystique"].Upskirt = 1
                        elif newgirl["Mystique"].Legs == "pants":
                            "Mystique slides her hand down her body and into her pants."  
                        elif HoseNum("Mystique") >= 5:
                            "Mystique's hand slides down her body and under her [newgirl[Mystique].Hose]."
                        elif newgirl["Mystique"].Panties:                
                            "Mystique's hand slides down her body and under her [newgirl[Mystique].Panties]."
                        else:
                            "Mystique's hand slides down her body and begins to caress her pussy."
                        $ newgirl["Mystique"].SeenPanties = 1
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
                                    "Mystique begins to masturbate."
                            "Go for it.":       
                                    call MystiqueFace("sexy, 1")                    
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                                    ch_p "That is so sexy, [newgirl[Mystique].Pet]."
                                    call Mystique_Namecheck
                                    "You lean back and enjoy the show."
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                            "Ask her to stop.":
                                    call MystiqueFace("surprised")       
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                                    ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                                    call Mystique_Namecheck
                                    "Mystique pulls her hands away from herself."
                                    call MystiqueOutfit
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                                    return            
                        jump MystiqueM_Prep
                else:                
                        $ Tempmod = 0                               # fix, add Mystique auto stuff here
                        $ Trigger2 = 0
                return            
    #End if Mystique intitiates this action
    
    #first time
    if not newgirl["Mystique"].Mast:                                                                
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So you enjoy a good show then. . ."
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m "but. . . {i}only{/i} a show?"
            
            
    #First time dialog             
    if not newgirl["Mystique"].Mast and Approval:                                                      
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            elif newgirl["Mystique"].Love >= newgirl["Mystique"].Obed and newgirl["Mystique"].Love >= newgirl["Mystique"].Inbt:
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Mouth = "smile" 
                ch_m "I don't usually show this side . . ."          
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                call MystiqueFace("normal")
                ch_m "If that's what you're into, [newgirl[Mystique].Petname]. . ."            
            else: # Uninhibited 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Mouth = "smile"             
                ch_m "I do enjoy a good performance . . ."     
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                ch_m "Again? Just you only want to watch?"  
            elif Approval and "masturbation" in newgirl["Mystique"].RecentActions:
                call MystiqueFace("sexy", 1)
                ch_m "I still have some. . . work I could be doing. . ."    
                jump MystiqueM_Prep
            elif Approval and "masturbation" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy", 1)
                $ Line = renpy.random.choice(["I was that good?",       
                    "Didn't get enough earlier?",
                    "I did enjoy the audience participation. . ."]) 
                ch_m "[Line]"            
            elif newgirl["Mystique"].Mast < 3:        
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Brows = "confused"
                ch_m "You enjoyed the show?"       
            else:       
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Girl_Arms = 2
                $ Line = renpy.random.choice(["You really do like to watch.",                 
                    "Once more?",                 
                    "You enjoy watching me.",
                    "You want me to take care of myself?"]) 
                ch_m "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                ch_m "Fine. . ." 
            else:
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Ok.",                 
                    "It couldn't hurt having you around. . .",
                    "Very well.", 
                    "Sure, why not?",
                    "[[chuckles]. . . ok."]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump MystiqueM_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_m "I don't know that I want to perform."
            "Maybe later?":
                    call MystiqueFace("sexy", 1)  
                    if newgirl["Mystique"].Lust > 70:                        
                        ch_m "I have plans for. . . later, but perhaps you could take part."
                    else:
                        ch_m "I couldn't say."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)               
                    return
            "You look like you could use it. . .":             
                    if Approval:
                        call MystiqueFace("sexy")     
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Ok.",                 
                            "It couldn't hurt having you around. . .",
                            "Very well.", 
                            "Sure, why not?",
                            "[[chuckles]. . . ok."]) 
                        ch_m "[Line]"
                        $ Line = 0                   
                        jump MystiqueM_Prep
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Mystique", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                        call MystiqueFace("sad")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                        ch_m "Oh, if it will shut you up."  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                        $ newgirl["Mystique"].Forced = 1  
                        jump MystiqueM_Prep
                    else:                              
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)     
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1                
    if newgirl["Mystique"].Forced:
            call MystiqueFace("angry", 1)
            ch_m "That's something I won't do."
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)         
            if newgirl["Mystique"].Love > 300:
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
            $ newgirl["Mystique"].RecentActions.append("no masturbation")                      
            $ newgirl["Mystique"].DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            call MystiqueFace("angry", 1)          
            $ newgirl["Mystique"].DailyActions.append("tabno") 
            ch_m "Obviously not in someplace so exposed."     
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)  
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)    
            return                
    elif newgirl["Mystique"].Mast:
            call MystiqueFace("sad") 
            ch_m "I'm sure you can find something else to watch."     
    else:
            call MystiqueFace("normal", 1)
            ch_m "I don't think so, [newgirl[Mystique].Petname]."  
    $ newgirl["Mystique"].RecentActions.append("no masturbation")                      
    $ newgirl["Mystique"].DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label MystiqueM_Prep: 
    $ newgirl["Mystique"].Upskirt = 1    
    $ newgirl["Mystique"].PantiesDown = 1 
    call Set_The_Scene  
    
    #if she hasn't seen you yet. . .
    if "unseen" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Eyes = "closed"
            $ newgirl["Mystique"].Girl_Arms = 2
            "You see Mystique leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Girl_Arms = 2
            "Mystique lays back and starts to play with herself."
            if not newgirl["Mystique"].Mast:#First time        
                    if newgirl["Mystique"].Forced:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 45)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35) 
                    else:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 35)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no masturbation")
    $ newgirl["Mystique"].RecentActions.append("masturbation")                      
    $ newgirl["Mystique"].DailyActions.append("masturbation") 
            
label MystiqueM_Cycle:  
    if Situation == "join":
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call MystiqueLust  
        if "unseen" in newgirl["Mystique"].RecentActions:  
                $ newgirl["Mystique"].Eyes = "closed"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Line:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                                        
                    menu:
                        "[Line]"
                        
                        "Keep Watching.":
                                pass
                                
                        "Mystique. . .[[jump in]" if "unseen" not in newgirl["Mystique"].RecentActions and MultiAction:                 
                                "Mystique slows what she's doing with a sly grin."
                                ch_m "Enjoy the show?"
                                $ Situation = "join"
                                call Mystique_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in newgirl["Mystique"].RecentActions:  
                                jump MystiqueM_Interupted      
                        "Slap her ass":    
                                if "unseen" in newgirl["Mystique"].RecentActions:
                                        "You smack Mystique firmly on the ass!"
                                        $ renpy.play('sounds/slap.mp3')
                                        jump MystiqueM_Interupted                                          
                                else:
                                        call Mystique_Slap_Ass
                                        jump MystiqueM_Cycle  
                                
                        "Change what I'm doing":
                                menu:
                                    "Start jack'in it." if Trigger2 != "jackin":
                                            call Mystique_Jackin                   
                                    "Stop jack'in it." if Trigger2 == "jackin":
                                            $ Trigger2 = 0
                                
#                                    "Fondle her breasts" if "unseen" not in newgirl["Mystique"].RecentActions and Trigger2 != "fondle breasts":
#                                            $ Trigger2 = "fondle breasts"
#                                    "Suck on her breasts" if "unseen" not in newgirl["Mystique"].RecentActions and Trigger2 != "suck breasts":
#                                            $ Trigger2 = "suck breasts" 
                                    "Nevermind":
                                            pass
                             
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                        
                        "Maybe lose some clothes. . ." if "unseen" not in newgirl["Mystique"].RecentActions:
                                    call Mystique_Undress  
                                    
                        "Let's try something else." if MultiAction and "unseen" not in newgirl["Mystique"].RecentActions: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump MystiqueM_Interupted
                        "Let's stop for now." if not MultiAction and "unseen" not in newgirl["Mystique"].RecentActions: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump MystiqueM_Interupted
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:
                        if "unseen" not in newgirl["Mystique"].RecentActions: #if she knows you're there
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Pos_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            $ P_Focus = 95
                            jump MystiqueM_Interupted
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        jump MystiqueM_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,  
                            "Mystique still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump MystiqueM_Cycle 
                                "No, I'm done.":
                                    "You pull back."
                                    return
        #End orgasm
        
        if "unseen" in newgirl["Mystique"].RecentActions:
                if Round == 10:
                    "It's getting a bit late, Mystique will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if Round == 10:
                    ch_m "We might want to wrap this up, it's getting late."  
                    $ newgirl["Mystique"].Lust += 10
                elif Round == 5:
                    ch_m "Seriously, it'll be time to stop soon."     
                    $ newgirl["Mystique"].Lust += 25   
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    if "unseen" not in newgirl["Mystique"].RecentActions:
        ch_m "Ok, I'm kinda done for now, I need a break."
    
label MystiqueM_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in newgirl["Mystique"].RecentActions:                         
                call MystiqueFace("surprised", 2)
                "Mystique stops what she's doing with a start, eyes wide."
                if not newgirl["Mystique"].Legs or newgirl["Mystique"].Upskirt:                    
                    if not newgirl["Mystique"].Panties or newgirl["Mystique"].PantiesDown:
                        call Mystique_First_Bottomless(1) 
                call MystiqueFace("confused", 1, Eyes="surprised")
                if newgirl["Mystique"].Loc == "bg desk":
                    $ newgirl["Mystique"].Loc = bg_current
                    call Display_Mystique
                    "She approaches you."
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_m "!"
                        ch_m "How long have you been there?!"
                        $ newgirl["Mystique"].Eyes = "down"
                        menu:
                            ch_m "And I see you've been busy. . . "
                            "A little while, it was an excellent show.":   
                                    call MystiqueFace("sexy",1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
                                    ch_m "Well, obviously. . ."
                                    if newgirl["Mystique"].Love >= 800 or newgirl["Mystique"].Obed >= 500 or newgirl["Mystique"].Inbt >= 500:
                                        $ Tempmod += 10
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)
                                    ch_m "and I suppose you bring a lot ot the table as well, don't you. . ."  
                                    
                            "I. . . just got here?":
                                    call MystiqueFace("angry",1, Eyes="down")                   
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
                                    "She looks pointedly at your cock,"
                                    $ newgirl["Mystique"].Eyes = "squint"
                                    ch_m "Long enough to raise your sails?"   
                                    if newgirl["Mystique"].Love >= 800 or newgirl["Mystique"].Obed >= 500 or newgirl["Mystique"].Inbt >= 500:
                                            $ Tempmod += 10
                                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)
                                            call MystiqueFace("bemused", 1)
                                            ch_m "I suppose you couldn't help yourself under the circumstances. . ."   
                                    else:
                                            $ Tempmod -= 10
                                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, -5)
                        call Mystique_First_Peen
                                    
                #you haven't been jacking it                    
                else:         
                        ch_m "!"
                        ch_m "How long have you been there?!" 
                        menu:
                            extend ""
                            "A little while.":   
                                    call MystiqueFace("sexy", 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
                                    ch_m "Enjoying the show?"
                            "I just got here.":
                                    call MystiqueFace("bemused", 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)                    
                                    ch_m "Yes, I'm sure. . ."   
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)    
                                
                call DrainWord("Mystique","unseen",1,0) #She sees you, so remove unseens
                $ newgirl["Mystique"].Mast += 1
                if "classcaught" not in newgirl["Mystique"].History:
                    # this activates if it's the first time in class
                    return
                if Round <= 10:
                    ch_m "Unfortunately it's getting rather late."
                    return
                $ Situation = "join"        
                call Mystique_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ newgirl["Mystique"].Action -= 1
    $ newgirl["Mystique"].Mast += 1    
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
    if Round <= 10:
            ch_m "Allow me to collect myself. . ."
            return
    call MystiqueFace("sexy", 1)
    if newgirl["Mystique"].Lust < 20:
        ch_m "I suppose that took care of my needs, at least."
    else:
        ch_m "Yes?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if P_Semen and newgirl["Mystique"].Action and MultiAction:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if P_Semen:
                call MystiqueFace("sly")
                if newgirl["Mystique"].Action and Round >= 10:
                    ch_m "I suppose. . ."
                    jump MystiqueM_Cycle
                else:
                    ch_m "Give me a minute, I need to collect myself here. . ."
        "I'm good here. [[Stop]":  
                if newgirl["Mystique"].Love < 800 and newgirl["Mystique"].Inbt < 500 and newgirl["Mystique"].Obed < 500:
                    call MystiqueOutfit
                call MystiqueFace("normal")
                $ newgirl["Mystique"].Brows = "confused"
                ch_m "Well. . . yes. . ."
                $ newgirl["Mystique"].Brows = "normal" 
        "You should probably stop for now." if newgirl["Mystique"].Lust > 30:
                call MystiqueFace("angry")
                ch_m "I . . . yes . ."
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    return
    
## end newgirl["Mystique"].Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Mystique_Offhand function //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label Mystique_Offhand(TempLine=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    
    $ D20 = renpy.random.randint(1, 20)                                                                 # Taboo caught check
                    
    if not Trigger2: #If there are no offhand options set, return
        return    
    
    if Trigger2 == "kissing":
                $ Line = renpy.random.choice([". Your lips gently slide across hers.", 
                        ". Her lips part as you hold her close.",    
                        ". You nibble her neck as she groans in pleasure.",
                        ". You squeeze her tightly as your tongues jostle.",
                        ". Her tongue dances around yours.",
                        ". She nibbles your ear as her hands slide across your back.",
                        ". Your hands slide down her body as your lips press hers.",
                        ". You kiss her passionately.", 
                        ". Your tongues swirl around each other's."])
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 75, 1) if newgirl["Mystique"].Love >= 300 else newgirl["Mystique"].Love
                $ PrimaryLust += 2 if newgirl["Mystique"].Lust < 50 else 1
        
    elif Trigger2 == "fondle breasts":
                $ Line = renpy.random.choice([". You reach out and massage her pert breasts.", 
                        ". You pass your hands gently over her warm breasts.", 
                        ". Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                        ". She gasps as you lightly thumb her tight nipples."])
                $ PrimaryLust += 3           
                $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "suck breasts":
            if newgirl["Mystique"].Chest:
                $ Line = renpy.random.choice([". You bend down and motor-boat her breasts.",
                    ". You tease her nipples with your tongue through her top.",
                    ". You slowly lick her nipples through her moist top.", 
                    ". you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    ". She gasps as you lightly lick her rigid nipples, poking through her top."])            
            else:
                $ Line = renpy.random.choice([". You bend down and motor-boat her breasts.",
                    ". You gently nibble at her nipples as you suck on them.",
                    ". You tease her nipples with your tongue.",
                    ". You slowly lick around, and then blow across her nipples.", 
                    ". You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    ". She gasps as you lightly lick her rigid nipples."])
            $ PrimaryLust += 4 if 60 < newgirl["Mystique"].Lust < 80 else 2  
            $ TempFocus += 3 if P_Focus < 90 else 0 
        
    elif Trigger2 == "fondle pussy":
            
            $ Line = renpy.random.choice([". You put your hand against her mound and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her lips.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < newgirl["Mystique"].Lust < 90 else 2        
            $ TempFocus += 4 if P_Focus < 90 else 0 
        
    elif Trigger2 == "lick pussy":
            if newgirl["Mystique"].Legs != "pants" and not newgirl["Mystique"].Panties:  
                $ Line = renpy.random.choice([". You slide your tongue into her pussy and flick the roof with deft strokes.", 
                    ". You spread the lips back and she gasps as you slide your tongue between them.", 
                    ". You can feel her twitching as you grind your tongue against her clit.",
                    ". She gasps as you suck on her clit.",
                    ". You rub her clit with your thumb as you dive into her pussy with your tongue.",
                    ". With a little nibble, you tug on her lower lips.",
                    ". You slowly lick into her gap and she gasps as you press the walls aside."])
            else:
                $ Line = renpy.random.choice([". You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.", 
                    ". She gasps as you suck on her clit through the fabric.",
                    ". You rub her clit with your thumb as you press against her pussy with your tongue.",
                    ". You put your hand against her mound and lick the juice that's collected.", 
                    ". With a little nibble, you tug back the fabric.",
                    ". You slowly lick into her gap and she gasps as you press the walls aside."])
            $ PrimaryLust += 5 if newgirl["Mystique"].Lust > 50 else 2       
            $ TempFocus += 4 if P_Focus < 90 else 0 
            
    elif Trigger2 == "fondle ass":
            if newgirl["Mystique"].Legs != "pants" and not newgirl["Mystique"].Panties: 
                $ Line = renpy.random.choice([". You reach out and brush your hands across her bare ass.", 
                        ". You put your hand against her firm rear and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". She gasps as you reach under her and lightly stroke her ass.",
                        ". You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            else:
                $ Line = renpy.random.choice([". You reach out and brush your hands across her ass.", 
                        ". You put your hand against her firm rear and grind against it.", 
                        ". You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        ". Her legs twitch a bit as you press your thumb against her.",
                        ". She gasps as you reach under her and lightly stroke her ass.",
                        ". You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if newgirl["Mystique"].Lust < 50 else 1
            $ TempFocus += 1 if P_Focus < 50 else 0  
            $ TempFocus += 1 if P_Focus < 80 else 0   
        
    elif Trigger2 == "insert ass":
            $ Line = renpy.random.choice([". You reach out and slide a finger into her ass.", 
                    ". You slide a finger into her asshole and stroke the roof of it.", 
                    ". You can feel her twitching as you press your thumb against her clit.",
                    ". She gasps as you rub her asshole with your fingers.",
                    ". You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    ". You reach into her gap and she gasps as you slide your hand across and press against her hole.", 
                    ". She gasps as you reach under her warm lips and lightly stroke her ass."])       
            $ PrimaryLust += 3 if newgirl["Mystique"].Lust > 70 and newgirl["Mystique"].Loose else 1
            $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "jackin":
            if Trigger == "masturbation":
                    $ Line = ". You stroke your cock as you watch her go."
            elif Trigger == "hand":
                    $ Line = renpy.random.choice([". You also give it a little rub.", 
                            ". As she does so, you polish the knob a bit.", 
                            ", and you help.",
                            ", your hand bumps into hers occasionally."])     
            elif Trigger == "blow":
                    if Speed >= 3:
                        $ Line = "."
                    else:
                        $ Line = renpy.random.choice([". You also give it a little rub.", 
                            ". As she does so, you work the shaft a bit.", 
                            ", and you help.",
                            ", her lips brush your hand occasionally."])    
            else:
                    $ Line = renpy.random.choice([", and with your other hand, you stroke your shaft.", 
                            ". You stroke your cock with your other hand.", 
                            ", and as you do, you stoke yourself."])               
            if "unseen" not in newgirl["Mystique"].RecentActions:
                $ PrimaryLust += 3 if 20 < newgirl["Mystique"].Lust < 70 else 2
                $ TempFocus += 1 if P_Focus < 70 else 0            
            $ TempFocus += 5
               
    return                      #End Mystique_Offhand check
    


label Mystique_Offhand_Set(Situation = Situation, TempTrigger = Trigger2):
    
    if Situation == "shift focus":        
            if TempTrigger:      
                $ Trigger2 = 0  
#                $ Situation = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump Mystique_FB_Prep
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump Mystique_SB_Prep
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump Mystique_FP_Prep
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump Mystique_LP_Prep
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump Mystique_FA_Prep
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump Mystique_IA_Prep
                else: #If Trigger2 is "kissing"
                        "You go back to kissing her deeply."
                        jump Mystique_KissPrep                
            else: #if there's no Trigger2
                "You aren't doing anything else to shift to."     
            return
    # End "shift" situation    
        
    if Trigger:
        $ Situation = "auto"                 
        menu:  
            "Also kiss her." if Trigger in ("fondle breasts", "fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    "You lean in and start kissing her."
                    $ Trigger2 = "kissing"
                    
            "Also fondle her breasts." if Trigger in ("fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle breasts"
                    call Mystique_Fondle_Breasts
                    
            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "suck breasts"
                    call Mystique_Suck_Breasts
                    
            "Also fondle her pussy." if Trigger in ("fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle pussy"
                    call Mystique_Fondle_Pussy
                    
            "Also fondle her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call Mystique_Fondle_Ass
                    
            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "dildo pussy", "foot"):
                    $ Trigger2 = "insert ass"
                    call Mystique_Insert_Ass
                    
            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call Mystique_Jackin
                    
            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know." 
        
    $ Situation = 0
    return

    
# end Mystique_Offhand function ////////////////////////////////////////////////////////////////////////


label Mystique_ShameIndex:   
    $ newgirl["Mystique"].ShameLevel = 0
    
    if Trigger == "kissing":
        $ newgirl["Mystique"].ShameLevel += 2
        
    elif Trigger in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ newgirl["Mystique"].ShameLevel += 6
        
    elif Trigger in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ newgirl["Mystique"].ShameLevel += 10
        
    elif Trigger in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand", "blow", "titjob", "masturbation"):
        $ newgirl["Mystique"].ShameLevel += 15
    
    elif Trigger in ("sex",  "anal"):
        $ newgirl["Mystique"].ShameLevel += 20
    
    
    if not Trigger2:
        pass
    if Trigger2 == "kissing":
        $ newgirl["Mystique"].ShameLevel += 2
        
    elif Trigger2 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ newgirl["Mystique"].ShameLevel += 6
        
    elif Trigger2 in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ newgirl["Mystique"].ShameLevel += 10
        
    elif Trigger2 in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand"):
        $ newgirl["Mystique"].ShameLevel += 15    
        
        
    if not Trigger3:
        pass
    elif Trigger3 == "kissing":
        $ newgirl["Mystique"].ShameLevel += 2
        
    elif Trigger3 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ newgirl["Mystique"].ShameLevel += 6
        
    elif Trigger3 in ("fondle pussy"):
        $ newgirl["Mystique"].ShameLevel += 10
        
    elif Trigger3 in ("dildo pussy", "dildo anal", "hand"):
        $ newgirl["Mystique"].ShameLevel += 15
    
    
    $ newgirl["Mystique"].ShameLevel += newgirl["Mystique"].Shame #adds clothing based shame
    
    return
            
label Mystique_Taboo(Cnt= 1, Public=0):    
    if Trigger == "kissing" and not Trigger2 and not Trigger3:        
            if R_Loc == bg_current:
                call Rogue_Noticed("Mystique")
            if K_Loc == bg_current:
                call Kitty_Noticed("Mystique")
            if E_Loc == bg_current:
                call Emma_Noticed("Mystique")
            $ i = 0
            while i < len(ModdedGirls):
                if ModdedGirls[i] != "Mystique":
                    if newgirl[ModdedGirls[i]].Loc == bg_current:
                        call NewGirl_Noticed("Mystique", ModdedGirls[i])
                $ i += 1
            return
    call MystiqueFace("surprised", 1) 
    
    if newgirl["Mystique"].Rep <= 200:
            $ Public = 2
    elif newgirl["Mystique"].Rep <= 400:
            $ Public = 1     
    #This is a trait for if she's open to being sexy in public
    
    $ Cnt = Action_Check("Mystique", "recent", "spotted") if "spotted" in newgirl["Mystique"].RecentActions else 1
    $ Cnt = 4 if Cnt > 4 else Cnt   
    
    $ D20 = renpy.random.randint(1, 20)  
    if newgirl["Mystique"].Rules and D20 < 10:                                              
        # If Xavier notices you can calls you in   
        if R_Loc == bg_current:
                call Rogue_Noticed("Mystique")
        if K_Loc == bg_current:
                call Kitty_Noticed("Mystique")
        if E_Loc == bg_current:
                call Emma_Noticed("Mystique")
        $ i = 0
        while i < len(ModdedGirls):
                if ModdedGirls[i] != "Mystique":
                    if newgirl[ModdedGirls[i]].Loc == bg_current:
                        call NewGirl_Noticed("Mystique", ModdedGirls[i])
                $ i += 1
        if Trigger != "kissing" and Taboo > 20:
                call MystiqueFace("confused", 1)
                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                    "Mystique stops what she's doing with an annoyed look."                
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!" 
                call AllReset("Mystique")
                $ renpy.pop_call()        
                $ renpy.pop_call()
                call Mystique_Caught
                return
    elif D20 < 10:                                                      
        #If Xavier notices you, but doesn't care because you brainwashed him
        if R_Loc == bg_current:
                call Rogue_Noticed("Mystique")
        if K_Loc == bg_current:
                call Kitty_Noticed("Mystique")
        if E_Loc == bg_current:
                call Emma_Noticed("Mystique")
        $ i = 0
        while i < len(ModdedGirls):
                if ModdedGirls[i] != "Mystique":
                    if newgirl[ModdedGirls[i]].Loc == bg_current:
                        call NewGirl_Noticed("Mystique", ModdedGirls[i])
                $ i += 1
        if Taboo > 20:
            ch_x "Hmmm. . ."
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 2) 
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3) 
    if Taboo <= 20:
            #This is a private space with others around.
            return        
    elif Cnt < 4:                                                      
            #if this has happened less than 4 times within the current cycle of events
            if "spotted" not in newgirl["Mystique"].RecentActions:
                "Some of the other students notice you and Mystique."
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 2)               
                $ newgirl["Mystique"].Rep -= 4                         
                $ P_Rep -= 2             
            elif Cnt < 3:
                "A few more students notice you and Mystique."   
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 2)               
                $ newgirl["Mystique"].Rep -= 2                    
                $ P_Rep -= 1  
            elif Cnt == 3:
                "You've got quite an audience."               
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 3)               
                $ newgirl["Mystique"].Rep -= 1                    
                $ P_Rep -= 1  
                
            if "exhibitionist" in newgirl["Mystique"].Traits:                
                    call MystiqueFace("sexy", 0)                     
                    if "spotted" not in newgirl["Mystique"].RecentActions:
                        ch_m "Hmm, maybe they can learn a few things, [newgirl[Mystique].Petname]."                          
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                    $ Line = "A"
            elif ApprovalCheck("Mystique", 750, "I", TabM=Cnt-Public):
                    #not an exhibitionist but very uninhibited       
                    call MystiqueFace("sexy", 1)                    
                    $ newgirl["Mystique"].Brows = "sad"                           
                    if "spotted" not in newgirl["Mystique"].RecentActions:                        
                        ch_m "Well, this is something of a situation." 
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4)   
                    $ Line = "B"
            elif ApprovalCheck("Mystique", 1000, "OI", TabM=Cnt-Public):     
                    #not an exhibitionist but obedient/uninhibited          
                    call MystiqueFace("confused", 2)
                    "Mystique looks a bit concerned."
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4)
                    $ Line = "C"
            else:  
                    # She fails her inhibition checks
                    call MystiqueFace("angry", 2)
                    if "spotted" not in newgirl["Mystique"].RecentActions:    
                        "Mystique bolts up with an embarassed look. She grabs her clothes and stalks off."  
                        $ newgirl["Mystique"].Rep -= 3 if newgirl["Mystique"].Rep >= 30 else newgirl["Mystique"].Rep            
                    else:
                        "With a sudden embarrassed start, Mystique panics. She grabs her clothes and stalks off."  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -15) 
                    "You head back to your room."                    
                    $ Line = "stop"
                
            if Line != "stop":
                menu:
                    "What would you like to do?"
                    "Let them watch. . ." if "spotted" not in newgirl["Mystique"].RecentActions:   
                            if Line == "A":                
                                    call MystiqueFace("sexy", 0) 
                                    ch_m "It's only fair."             
                            elif Line == "B":            
                                    #not an exhibitionist but very uninhibited       
                                    call MystiqueFace("sexy", 1)            
                                    ch_m "I do suppose we can show them how it's done."    
                            elif Line == "C":     
                                    call MystiqueFace("sexy",2)
                                    if newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
                                        $ newgirl["Mystique"].Eyes = "side"
                                        ch_m "I won't back down if you won't, [newgirl[Mystique].Petname]."
                                    else:          
                                        $ newgirl["Mystique"].Mouth = "smile"
                                        $ newgirl["Mystique"].Brows = "sad"
                                        ch_m "Not that I mind, of course."                     
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)                       
                            "You get back to it." 
                            $ newgirl["Mystique"].Blush = 1
                    "Continue" if "spotted" in newgirl["Mystique"].RecentActions:
                            if Line == "C":          
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5) 
                    "Ok, let's stop.":                
                            call MystiqueFace("sad")
                            if Line == "A":               
                                    ch_m "Spoilsport."                                         
                            elif Line == "B":            
                                    ch_m "I suppose." 
                            elif Line == "C":     
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)          
                                    call MystiqueFace("confused")
                                    $ newgirl["Mystique"].Eyes = "side"
                                    ch_m "That probably would be for the best. . ." 
                            "You both run back to your rooms."
                            $ Line = "stop"
                        
            if Line == "stop":            
                    $ newgirl["Mystique"].RecentActions.append("caught")
                    $ newgirl["Mystique"].DailyActions.append("caught")          
                    show blackscreen onlayer black 
                    call Remove_Girl("Mystique")
                    call MystiqueOutfit
                    hide blackscreen onlayer black 
                    $ renpy.pop_call()          
                    $ renpy.pop_call()       
                    $ renpy.pop_call()                    
                    jump Player_Room             
    elif "exhibitionist" not in newgirl["Mystique"].Traits:     
            call MystiqueFace("sly")   
            $ newgirl["Mystique"].Traits.append("exhibitionist") 
            "Mystique seems to have become something of an exhibitionist."
    elif D20 > 15:
            call MystiqueFace("sexy")
            "The crowd cheers."
        
    $ newgirl["Mystique"].RecentActions.append("spotted") if Cnt < 4 else newgirl["Mystique"].RecentActions
    $ newgirl["Mystique"].DailyActions.append("spotted")  if "spotted" not in newgirl["Mystique"].DailyActions else newgirl["Mystique"].DailyActions
    return

