# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label Mystique_P_Cumming:
    call Shift_Focus("Mystique")
    if Trigger == "blow":
            $ Tempmod += 5
        
    if newgirl["Mystique"].Addict > 75:
            $ Tempmod += 20
    elif newgirl["Mystique"].Addict > 50:
            $ Tempmod += 5
    
    if newgirl["Mystique"].Swallow >= 10:
            $ Tempmod += 15  
    elif newgirl["Mystique"].Swallow >= 3:
            $ Tempmod += 5
        
    if (newgirl["Mystique"].CreamP + newgirl["Mystique"].CreamA) >= 10:
            $ Tempmod += 15 
    elif (newgirl["Mystique"].CreamP + newgirl["Mystique"].CreamA) >= 3:
            $ Tempmod += 5        
       
    $ D20 = renpy.random.randint(1, 20) 
    
# intro lines    
    if Trigger == "hand":
            $ Line = "As she strokes, you're about ready to come. . ."
    elif Trigger == "blow":
            $ Line = "As she sucks you, you start to feel about to come. . ."
    elif Trigger == "titjob":
            $ Line = "As you rub into her cleavage, you start to feel about to come. . ."
    elif Trigger == "sex" or Trigger == "anal":
            $ Line = "As you thrust into her, you feel about to blow. . ."
    elif Trigger == "hotdog":
            $ Line = "As you grind into her, you feel about to blow. . ."
    else:        
            $ Line = "You start to feel about to come. . ."    
    
    call MystiqueFace("sexy") 
    
    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
#                jump Mystique_No_Cum
                jump Mystique_Warn_Her
            
        "Ask to cum in her mouth": 
                $ Situation = "asked"
#                jump Mystique_No_Cum
                jump Mystique_In_Mouth                            
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                $ Situation = "auto"
#                jump Mystique_No_Cum
                jump Mystique_In_Mouth
        
        "Ask to cum inside her" if Trigger == "sex":
                $ Situation = "asked"
                jump Mystique_Creampie_P        
        "Ask to cum inside her" if Trigger == "anal":
                $ Situation = "asked"
                jump Mystique_Creampie_A
                
        "Cum inside her" if Trigger == "sex":
                $ Situation = "auto"
                jump Mystique_Creampie_P        
        "Cum inside her" if Trigger == "anal":
                $ Situation = "auto"
                jump Mystique_Creampie_A
            
        "Cum on her face":
                #jump Mystique_No_Cum
                jump Mystique_Facial            

        "Cum on her ass" if Trigger in ("sex","anal","hotdog") and renpy.showing("Mystique_Doggy"):
                jump Mystique_SpunkBack

        "Cum on her belly" if Trigger in ("sex","anal","hotdog","foot") and renpy.showing("Mystique_SexSprite"):
                jump Mystique_SpunkBelly
            
        "Pull back":
#            if renpy.showing("Mystique_BJ_Animation"):
#                    if newgirl["Mystique"].Addict >= 60 and ApprovalCheck("Mystique", 1000, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) and newgirl["Mystique"].Swallow:
#                            $ newgirl["Mystique"].Eyes = "manic"
#                            $ Speed = 0
#                            "You pull out of her mouth with a pop, and her eyes widen in surprise."
#                            $ newgirl["Mystique"].Mouth = "sucking"
#                            $ newgirl["Mystique"].Spunk.append("mouth")
#                            $ Speed = 4
#                            "She leaps at your cock and sucks it deep, draining your fluids hungrily." 
#                            $ Speed = 0
#                            $ newgirl["Mystique"].Mouth = "lipbite"
#                            "When she finishes, she draws her hand across her lips."
#                            call MystiqueFace("bemused")
#                            ch_m "I'm sorry, [newgirl[Mystique].Petname], but that would have been a waste."
#                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -5)
#                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)
#                            jump Mystique_Swallowed                            
#                    call Mystique_BJ_Reset                
#            elif renpy.showing("Mystique_HJ_Animation"):
#                    call Mystique_HJ_Reset                
#            elif renpy.showing("Mystique_SexSprite"):
#                    call Mystique_Sex_Reset                    
#            if ApprovalCheck("Mystique", 500, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) and newgirl["Mystique"].Addict > 50 and newgirl["Mystique"].Swallow: #If addict + Inbt is > obedience + 50. . .
#                    $ newgirl["Mystique"].Eyes = "manic"
#                    $ newgirl["Mystique"].Mouth = "kiss"
#                    $ Speed = 0
#                    "Her eyes widen in panic."
#                    ch_m "Won't you reconsider, [newgirl[Mystique].Petname]?" 
#                    $ newgirl["Mystique"].Blush = 2
#                    menu:
#                        extend ""
#                        "Ok, if you'll swallow it.":
#                                if Trigger != "blow": 
#                                    call Mystique_BJ_Launch("cum")
#                                call MystiqueFace("sucking") 
#                                $ Speed = 2
#                                "She nods and puts the tip into her mouth. as you release she gulps it down hungrily."
#                                call MystiqueFace("sexy")                      
#                                $ newgirl["Mystique"].Mouth = "sucking"
#                                $ newgirl["Mystique"].Spunk.append("mouth")
#                                ". . ."
#                                $ Speed = 0
#                                call MystiqueFace("sad")                       
#                                $ newgirl["Mystique"].Mouth = "lipbite"
#                                ch_m "Waste not, want not."  
#                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
#                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 1)
#                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
#                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
#                                jump Mystique_Swallowed                                
#                        "No, we're done for now.": #If addict is > obedience + 50. . .
#                                if ApprovalCheck("Mystique", 250, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) or newgirl["Mystique"].Addict > 75:                            
#                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1)
#                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, -2)
#                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
#                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3)
#                                        if Trigger != "blow":
#                                            call Mystique_BJ_Launch("cum")
#                                            $ Speed = 4
#                                        "She dives down on you and you can't resist filling her throat."
#                                        $ Speed = 0
#                                        ch_m "Well, I'm afraid I wasn't."
#                                        jump Mystique_Swallowed                                
#                                else:                         
#                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 3)
#                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 5)
#                                        call MystiqueFace("sad")
#                                        $ newgirl["Mystique"].Brows = "confused"
#                                        ch_m "If you insist."
#                                        $ Line = 0
#                                        $ P_Focus -= 5
#                                        return  
#                    #manic, wanted to swallow
                    
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips." 
            ch_m "Well [newgirl[Mystique].Petname], what next then?"
            $ Line = 0
            $ P_Focus = 95
            return
            #end "pull back"
#End Main orgasm menu

label Mystique_No_Cum:
    #this is a temporary thing until this system is complete
    call MystiqueFace("confused", Mouth="smirk") 
    if Situation == "warn":
        ch_p "I'm about to. . . blow. . ."
        ch_m "Oh? How thoughtful."
    elif Situation == "asked":        
        ch_p "I'm about to. . . blow. . ."
        ch_p "Could I. . . come in your mouth?"
        ch_m "Hmmm, I don't think so."
    else:
        ch_m "Oh, I know that look, [newgirl[Mystique].Petname]. You're about to make a mess, aren't you."         
    $ newgirl["Mystique"].Girl_Arms = 2
    call MystiqueFace("sly",1) 
    ch_m "For now why don't you just come in my hand here. . ."
    $ newgirl["Mystique"].Spunk.append("hand") 
    "She grabs the head of your cock and you gush into it."
    ch_m "See? That wasn't so hard."         
    jump Mystique_Orgasm_After

label Mystique_Warn_Her:                                                                                                                       #Warn her start
        "You let her know that you're going to come."
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5) if newgirl["Mystique"].Obed >= 500 else newgirl["Mystique"].Obed   
        if "hungry" in newgirl["Mystique"].Traits and D20 >= 5:
                if renpy.showing("Mystique_SexSprite"):
                    call Mystique_HJ_Launch("cum")   
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                call MystiqueFace("sucking")       
                ". . ."
                $ Speed = 0
                $ newgirl["Mystique"].Spunk.append("mouth")
                if not renpy.showing("Mystique_BJ_Animation"):
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:                    
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."        
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Mouth = "smile"
                ch_m "Delectable, [newgirl[Mystique].Petname], I appreciate the warning."        
                jump Mystique_Swallowed
        #End Hungy take-over
            
        if Trigger == "sex" and newgirl["Mystique"].CreamP >= 5: 
                # She's Creampied a few times
                call MystiqueFace("sexy")
                $ P_Cock = "in"
                $ newgirl["Mystique"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."   
                if newgirl["Mystique"].Lust >= 85: 
                    call Mystique_Cumming  
                jump Mystique_Creampied
        
        elif Trigger == "sex" and newgirl["Mystique"].CreamP and D20 >= 10:  
                # She's Creampied at least once
                call MystiqueFace("sly")
                $ P_Cock = "in"
                $ newgirl["Mystique"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."          
                if newgirl["Mystique"].Lust >= 85: 
                    call Mystique_Cumming  
                jump Mystique_Creampied
            
        elif Trigger == "anal" and newgirl["Mystique"].CreamA >= 5: 
                # She's Anal Creampied a few times
                call MystiqueFace("sexy")
                $ P_Cock = "anal"
                $ newgirl["Mystique"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."         
                if newgirl["Mystique"].Lust >= 85: 
                    call Mystique_Cumming  
                jump Mystique_Creampied
        
        elif Trigger == "anal" and newgirl["Mystique"].CreamA and D20 >= 10: 
                # She's Anal Creampied at least once
                call MystiqueFace("sexy")
                $ P_Cock = "anal"
                $ newgirl["Mystique"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."    
                if newgirl["Mystique"].Lust >= 85: 
                    call Mystique_Cumming          
                jump Mystique_Creampied
            
        elif Trigger != "anal" and newgirl["Mystique"].Swallow >= 5: 
                #If she's swallowed a lot                
                if renpy.showing("Mystique_BJ_Animation"):            
                        call MystiqueFace("sucking")
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        "She makes a little humming sound, but keeps sucking."
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:
                        if renpy.showing("Mystique_SexSprite"):
                            call Mystique_BJ_Launch("cum")
                            $ Speed = 2
                        call MystiqueFace("sucking")
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        "She smiles and then puts your tip in her mouth."
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."                
                $ Speed = 0
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Mouth = "smile"
                ch_m "Delectable, [newgirl[Mystique].Petname], I appreciate the warning."  
                jump Mystique_Swallowed
            
        elif newgirl["Mystique"].Swallow and D20 >= 10:  
                #She's swallowed before, but not a lot  
                if renpy.showing("Mystique_SexSprite"):
                    call Mystique_HJ_Launch("cum") 
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                if renpy.showing("Mystique_BJ_Animation"): 
                        #if she's blowing
                        call MystiqueFace("sucking")
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        "She makes a little humming sound, but keeps sucking."
                        "When you finish filling her mouth, she gags a little, but manages to swallow it."
                        $ Speed = 0
                        call MystiqueFace("sexy")
                        $ newgirl["Mystique"].Mouth = "smile"
                        if newgirl["Mystique"].Addict > 50:
                                $ newgirl["Mystique"].Eyes = "manic"
                                "She gulps it down hungrily and licks her lips."
                        call MystiqueFace("bemused")
                        ch_m "Hmm. . . an acquired taste, I appreciate the warning."
                        jump Mystique_Swallowed                    
                        #fix, add titjob option here.   
                else:
                        #If she's handying
                        jump Mystique_Handy_Finish    
        #end if she's swallowed        
            
        elif ApprovalCheck("Mystique", 1000):                    
                #warned but likes you and experienced
                if newgirl["Mystique"].SEXP > 20 and renpy.showing("Mystique_SexSprite"):
                        "She gently pushes you back off of her."
                        jump Mystique_SpunkBelly
                elif newgirl["Mystique"].SEXP > 20:
                        jump Mystique_Facial            
        
                if renpy.showing("Mystique_HJ_Animation") and newgirl["Mystique"].Hand:
                        jump Mystique_Handy_Finish
                elif renpy.showing("Mystique_BJ_Animation") and newgirl["Mystique"].Blow:
                        jump Mystique_Handy_Finish
                elif renpy.showing("Mystique_TJ_Animation") and newgirl["Mystique"].Tit:
                        jump Mystique_Facial
                elif renpy.showing("Mystique_SexSprite"):
                        "She gently pushes you back off of her."
                        jump Mystique_SpunkBelly
                elif renpy.showing("Mystique_Doggy"):
                        "She gently pushes you back off of her."
                        jump Mystique_SpunkBack
        
        
        # Else. . . not experienced or she's not a huge fan, 
        if renpy.showing("Mystique_BJ_Animation"):
                $ Situation = "auto"
                jump Mystique_In_Mouth
        elif Trigger == "sex" or Trigger == "anal":
                call Mystique_Sex_Reset
                "She pulls off of you and grabs your cock in her hand."
                jump Mystique_Handy_Finish
        elif renpy.showing("Mystique_SexSprite"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump Mystique_SpunkBack
        else:
                jump Mystique_Facial
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
                      
                      
#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_In_Mouth:      
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in newgirl["Mystique"].Traits and newgirl["Mystique"].Addict <= 50 and "full" in newgirl["Mystique"].RecentActions:
            $ Tempmod -= 15                  
                
    if Situation == "auto":
                $ Situation = 0
                if not renpy.showing("Mystique_BJ_Animation"):
                        call Mystique_BJ_Launch("cum")
                $ Speed = 3
                "You grab her head and cum in her mouth"  
                $ newgirl["Mystique"].Eyes = "closed"        
                show Mystique_BJ_Animation
                with vpunch
                if "full" in newgirl["Mystique"].RecentActions:
                        #if she's had enough
                        call MystiqueFace("bemused")
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ newgirl["Mystique"].Spunk.remove("mouth")
                        ch_m "Hmm. . . that, may be a bit much for right now. . ."
                        ch_m "Perhaps we could find someplace else for you to. . . release. . ."
                elif newgirl["Mystique"].Swallow >= 5 or "hungry" in newgirl["Mystique"].Traits:
                        #if she likes to swallow
                        call MystiqueFace("sexy")
                        $ newgirl["Mystique"].Mouth = "smile"
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        "She quickly gulps it down and wipes her mouth."
                        $ newgirl["Mystique"].Spunk.remove("mouth")
                        $ Speed = 0
                        ch_m "Delectable, [newgirl[Mystique].Petname]."
                        call MystiqueFace
                elif newgirl["Mystique"].Swallow:
                        call MystiqueFace("bemused")
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ newgirl["Mystique"].Spunk.remove("mouth")
                        ch_m "Your. . . flavor is growing on me, but perhaps some warning?"
                        call MystiqueFace
                elif not newgirl["Mystique"].Swallow and newgirl["Mystique"].Addict >= 50 and newgirl["Mystique"].Inbt < 400 and newgirl["Mystique"].Blow < 10:
                        call MystiqueFace("bemused", 1)
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        ". . ."            
                        $ newgirl["Mystique"].Spunk.remove("mouth")
                        $ newgirl["Mystique"].Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ newgirl["Mystique"].Spunk.remove("hand")
                        ch_m "That certainly is. . . rich. . ."
                        $ newgirl["Mystique"].Addictionrate += 1
                        if "addictive" in P_Traits:
                            $ newgirl["Mystique"].Addictionrate += 1
                        call MystiqueFace
                        jump Mystique_Orgasm_After
                elif not newgirl["Mystique"].Swallow and newgirl["Mystique"].Addict >= 50:
                        call MystiqueFace("sexy")
                        $ newgirl["Mystique"].Mouth = "tongue"
                        $ newgirl["Mystique"].Spunk.append("mouth")
                        ". . ."
                        $ newgirl["Mystique"].Spunk.remove("mouth")
                        $ newgirl["Mystique"].Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ newgirl["Mystique"].Spunk.remove("hand")
                        ch_m "I shouldn't reward such rude behavior. . . but it was nourishing."
                        call MystiqueFace
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                elif not newgirl["Mystique"].Swallow:
                        if ApprovalCheck("Mystique", 800, "LI") and ApprovalCheck("Mystique", 400, "OI"):
                            call MystiqueFace("angry")
                            $ newgirl["Mystique"].Spunk.append("mouth")
                        else:
                            call MystiqueFace("bemused")
                            $ newgirl["Mystique"].Mouth = "tongue"
                            $ newgirl["Mystique"].Spunk.append("mouth")
                        ". . ."
                        $ newgirl["Mystique"].Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm."   
                        menu:
                            ch_m "Did I say you could come in my mouth, [newgirl[Mystique].Petname]?"
                            "Sorry about that.":
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                                    $ newgirl["Mystique"].Addictionrate += 1
                                    if "addictive" in P_Traits:
                                        $ newgirl["Mystique"].Addictionrate += 1
                                    call MystiqueFace("smile", 1)
                                    ch_m "Very well. . ."
                                    ch_m "Just warn me next time. . ."
                                    jump Mystique_Orgasm_After
                                
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck("Mystique", 1200):
                                        "She tentatively licks her hand, and then gulps it down."
                                        $ newgirl["Mystique"].Spunk.remove("hand")
                                        call MystiqueFace("sexy", 1)
                                        $ newgirl["Mystique"].Spunk.append("mouth")
                                        ch_m "Well, that was a bit of an acquired taste. . ."
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                        $ newgirl["Mystique"].Spunk.remove("mouth")
                                    elif ApprovalCheck("Mystique", 1200, "OI", Bonus = (newgirl["Mystique"].Addict*10)):
                                        call MystiqueFace("bemused", 1)
                                        $ newgirl["Mystique"].Brows = "normal" 
                                        $ newgirl["Mystique"].Mouth = "sad"
                                        $ newgirl["Mystique"].Spunk.remove("hand")
                                        $ newgirl["Mystique"].Spunk.append("mouth")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ newgirl["Mystique"].Spunk.remove("mouth")
                                        ch_m "I can't say that it would be my favorite flavor. . ."
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                    else:
                                        $ newgirl["Mystique"].Spunk.remove("hand")
                                        "She scowls at you and wipes her hand off. Then she licks her lips."
                                        jump Mystique_Orgasm_After
                                    
                            "Swallow it, now.":
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 30, -1, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -1, 1)                    
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -1, 1)
                                    if ApprovalCheck("Mystique", 1200, "OI") or newgirl["Mystique"].Addict >= 50:                            
                                        call MystiqueFace("sad", 1)
                                        $ newgirl["Mystique"].Spunk.append("mouth")
                                        $ newgirl["Mystique"].Spunk.remove("hand")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ newgirl["Mystique"].Spunk.remove("mouth")
                                        ch_m "I can't say that it would be my favorite flavor. . ."
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                    else:         
                                        $ newgirl["Mystique"].Spunk.remove("hand")               
                                        "She scowls at you and wipes her hand off. Then she licks her lips."                        
                                        jump Mystique_Orgasm_After
                else:                
                            jump Mystique_Orgasm_After
                                
                jump Mystique_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    
    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing("Mystique_SexSprite"):
            call Mystique_HJ_Launch("cum")
        
    if "full" in newgirl["Mystique"].RecentActions:
            pass
        
    elif newgirl["Mystique"].Swallow >= 5 or "hungry" in newgirl["Mystique"].Traits:  
            # If she's swallowed 5 times, 
            call MystiqueFace("sucking")
            if not renpy.showing("Mystique_BJ_Animation"):
                call Mystique_BJ_Launch("cum")            
                $ Speed = 3
                "She nods and bends down to put the tip between her lips. After you cum, she quickly gulps it down and wipes her mouth."
            else:            
                $ Speed = 3
                "She nods and hums a \"yes\" sound."
            $ newgirl["Mystique"].Spunk.append("mouth")
            ". . ."
            call MystiqueFace("sexy")            
            $ Speed = 0
            ch_m "Delectable, [newgirl[Mystique].Petname]."
            $ newgirl["Mystique"].Spunk.remove("mouth")
            jump Mystique_Swallowed
        
    elif newgirl["Mystique"].Addict >= 80 and newgirl["Mystique"].Swallow: 
            #addicted
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Eyes = "manic"
            if not renpy.showing("Mystique_BJ_Animation"):
                call Mystique_BJ_Launch("cum")            
                $ Speed = 3    
                "She gently puts the tip to her lips, just as you blow. She gags a little, but quickly swallows it."
            else:            
                $ Speed = 3
                "She nods and hums a \"yes\" sound."
            $ newgirl["Mystique"].Mouth = "sucking"
            $ newgirl["Mystique"].Spunk.append("mouth")
            ". . ."
            $ Speed = 0
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Mouth = "smile"
            ch_m "I should be upset, but I can't say I didn't enjoy that. . ."
            $ newgirl["Mystique"].Spunk.remove("mouth")
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5)
            jump Mystique_Swallowed
            
    elif newgirl["Mystique"].Swallow:                
            if ApprovalCheck("Mystique", 900):
                $ newgirl["Mystique"].Brows = "confused"
                if not renpy.showing("Mystique_BJ_Animation"):
                    call Mystique_BJ_Launch("cum")            
                    $ Speed = 3    
                    "She gently puts the tip to her lips, just as you blow. She gags a little, but quickly swallows it."
                else:            
                    $ Speed = 3
                    "She tilts her head and hums a \"hmm?\" sound."
                $ newgirl["Mystique"].Mouth = "sucking"
                $ newgirl["Mystique"].Spunk.append("mouth")
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "sexy"
                ". . ."
                $ Speed = 0
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Spunk.append("mouth")
                ch_m "It does grow on you. . ."
                $ newgirl["Mystique"].Spunk.remove("mouth")
                jump Mystique_Swallowed
     
    #If she hasn't swallowed or doesn't automatically want to. . .  
    
    if  ApprovalCheck("Mystique", 300, "LI") or ApprovalCheck("Mystique", 300, "OI"): 
        call MystiqueFace("bemused")
        $ newgirl["Mystique"].Eyes = "sexy"
    else:
        call MystiqueFace("angry")
        
    $ Speed = 0    
    
    if "full" in newgirl["Mystique"].RecentActions:
            ch_m "I couldn't finish another drop, [newgirl[Mystique].Petname]. . ." 
    else:
            ch_m "I can't imagine why I would. . ."
    
    menu:
        extend ""
        "Sorry about that.":
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 3)
                $ newgirl["Mystique"].Addictionrate += 1
                if "addictive" in P_Traits:
                    $ newgirl["Mystique"].Addictionrate += 1
                call MystiqueFace("smile", 1)
                ch_m "It is a tempting offer. . ."
                if ApprovalCheck("Mystique", 1200, TabM=1) and "full" not in newgirl["Mystique"].RecentActions:
                    $ Approval = 2 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)  
                    call MystiqueFace("sexy", 1)
                    ch_m "Perhaps a little bit. . ."
                else:
                    jump Mystique_Handy_Finish                
            
        "Give it a try, you might like it." if "full" not in newgirl["Mystique"].RecentActions:
                if ApprovalCheck("Mystique", 1200, TabM=1):  
                    $ Approval = 2
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                    $ newgirl["Mystique"].Brows = "confused"  
                    $ newgirl["Mystique"].Eyes = "sexy"
                    ch_m "If you insist. . ."
                else:     
                    $ newgirl["Mystique"].Addictionrate += 1
                    if "addictive" in P_Traits:
                        $ newgirl["Mystique"].Addictionrate += 1
                    $ newgirl["Mystique"].Blush = 1
                    ch_m "I highly doubt that, [newgirl[Mystique].Petname]."
                    jump Mystique_Handy_Finish
                            
        "Seriously, put it in your mouth.":
                if ApprovalCheck("Mystique", 1500, "LI", TabM=1) or ApprovalCheck("Mystique", 1200, "OI", TabM=1):
                        call MystiqueFace("sucking", 1)
                elif ApprovalCheck("Mystique", 1000, "OI", Bonus = (newgirl["Mystique"].Addict*10)): #Mild addiction included                
                        call MystiqueFace("angry", 1)
                else: 
                        #You insisted, she refused. 
                        call MystiqueFace("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call Mystique_HJ_Launch("cum")
                        call Mystique_HJ_Reset                
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                        ch_m "I think you overestimate your charms."
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")   
                        $ Line = 0
                        return                    
                $ newgirl["Mystique"].Mouth = "sucking"
                call Mystique_BJ_Launch("cum")            
                $ Speed = 3     
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 5)
        
    if not renpy.showing("Mystique_BJ_Animation"):
        call Mystique_BJ_Launch("cum")            
    $ Speed = 3    
    if ApprovalCheck("Mystique", 1200):            
            "She gently puts the tip to her lips, just as you blow."
            "She coughs a little, but quickly swallows it." 
    else:
            "She tentatively places the tip in her mouth, and you blast inside it. She quickly gulps it down."                    
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)        
    $ newgirl["Mystique"].Mouth = "sucking"
    $ newgirl["Mystique"].Spunk.append("mouth")
    ". . ."   
    $ Speed = 0            
    call MystiqueFace("sexy") 
    
    if ApprovalCheck("Mystique", 1000) and newgirl["Mystique"].Swallow >= 3:
            ch_m "It does grow on you. . ."    
    elif ApprovalCheck("Mystique", 800):                
            ch_m "Well, that was a bit of an acquired taste. . ."
    else:
            call MystiqueFace("sad")
            ch_m "I can't say that it would be my favorite flavor. . ."   
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 3)
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)            
    $ newgirl["Mystique"].Blow += 1
    jump Mystique_Swallowed     
    #end Mystique in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_Creampie_P:
        if Trigger == "sex" and Situation == "auto":
                $ P_Cock = "in"
                $ newgirl["Mystique"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if ApprovalCheck("Mystique", 1300) or newgirl["Mystique"].CreamP:              
                        call MystiqueFace("surprised")
                        "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."  
                        call MystiqueFace("sexy")
                        if newgirl["Mystique"].Lust >= 85: 
                            call Mystique_Cumming
                else:
                    if newgirl["Mystique"].Lust >= 85: 
                            "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                            call Mystique_Cumming                
                    else:
                            "You come in her pussy. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call MystiqueFace("angry")
                    ch_m "Perhaps some warning next time?"
                    call MystiqueFace("bemused")
                    ch_m "Not that it didn't feel good at the time. . ."
                    
                jump Mystique_Creampied
        
        #else (You ask her if it's ok):
        if ApprovalCheck("Mystique", 1200) or newgirl["Mystique"].CreamP:        
                call MystiqueFace("sexy")
                if newgirl["Mystique"].CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif newgirl["Mystique"].CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "in"
                $ newgirl["Mystique"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if newgirl["Mystique"].Lust >= 85: 
                    call Mystique_Cumming  
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1) 
                ch_m "How very. . . filling."
                jump Mystique_Creampied
        else:
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2) 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2) 
                ch_m "Thanks for warning me *grunt* [newgirl[Mystique].Petname], but perhaps not."
        jump Mystique_SpunkBack

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_Creampie_A:                             
        # These need conditionals added    
        if Trigger == "anal" and Situation == "auto":
                $ P_Cock = "anal"
                $ newgirl["Mystique"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if ApprovalCheck("Mystique", 1200) or newgirl["Mystique"].CreamP:              
                    call MystiqueFace("surprised", 1)
                    "You come in her ass. Her eyes widen in surprise, but she takes it in stride."  
                    call MystiqueFace("sexy")
                    if newgirl["Mystique"].Lust >= 85: 
                        call Mystique_Cumming
                else:
                    if newgirl["Mystique"].Lust >= 85: 
                        "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                        call Mystique_Cumming                
                    else:
                        "You come in her ass. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call MystiqueFace("angry")
                    ch_m "No advanced warning, [newgirl[Mystique].Petname]?"
                    call MystiqueFace("bemused")
                    ch_m "I suppose it was rather. . . filling though."
                jump Mystique_Creampied
            
        #else (You ask her if it's ok):
        if ApprovalCheck("Mystique", 1200) or newgirl["Mystique"].CreamP:        
                call MystiqueFace("sexy")
                if newgirl["Mystique"].CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif newgirl["Mystique"].CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "anal"
                $ newgirl["Mystique"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if newgirl["Mystique"].Lust >= 85: 
                    call Mystique_Cumming  
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1) 
                ch_m "Mmmm, I feel so full. . ."
                jump Mystique_Creampied
        else:
                call MystiqueFace("sexy")     
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2) 
                ch_m "Thanks for warning me *grunt* [newgirl[Mystique].Petname], but perhaps not."
        jump Mystique_SpunkBack
            
#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label Mystique_Facial: 
    if renpy.showing("Mystique_BJ_Animation"):       
            if newgirl["Mystique"].Addict >= 60 and ApprovalCheck("Mystique", 1000, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) and newgirl["Mystique"].Swallow:
                    $ newgirl["Mystique"].Eyes = "manic"
                    $ newgirl["Mystique"].Blush = 1
                    $ Speed = 0
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    $ Speed = 4
                    $ newgirl["Mystique"].Spunk.append("mouth")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ newgirl["Mystique"].Mouth = "lipbite"
                    $ Speed = 0
                    "When she finishes, she draws her hand across her lips."
                    call MystiqueFace("bemused")
                    $ newgirl["Mystique"].Spunk.remove("mouth")
                    ch_m "I'm sorry, [newgirl[Mystique].Petname], but waste not want not."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -5)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)
                    jump Mystique_Swallowed
            call Mystique_HJ_Launch("cum")
            $ Speed = 2
            $ newgirl["Mystique"].Spunk.append("facial")
            "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
            $ Speed = 0
    
    elif renpy.showing("Mystique_TJ_Animation"):   
            $ newgirl["Mystique"].Spunk.append("facial")
            "As you're about to finish, you aim squarely at her face, and spray all over it."  
            $ Speed = 0
            
    elif renpy.showing("Mystique_HJ_Animation"):       
            $ newgirl["Mystique"].Spunk.append("facial")
            "As you're about to finish, you aim squarely at her face, and spray all over it."  
            $ Speed = 0
    else:        
            call Mystique_BJ_Launch("cum")
            $ Speed = 0
            $ newgirl["Mystique"].Spunk.append("facial")
            "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
            $ Speed = 0
    
            if Situation == "warn":
                ch_m "I appreciate the warning. . . perhaps not the mess though. . ." 
            else:
                ch_m "What a mess, a warning would have been appreciated." 
                
    jump Mystique_Orgasm_After

# Start Spunk Belly / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_SpunkBelly:
    call Mystique_Sex_Launch("hotdog")
    $ Speed = 0
    if newgirl["Mystique"].Addict >= 60 and ApprovalCheck("Mystique", 1000, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) and newgirl["Mystique"].Swallow:
            $ newgirl["Mystique"].Eyes = "manic"
            $ newgirl["Mystique"].Blush = 1
            call Mystique_BJ_Launch("cum")
            if Trigger == "sex":
                "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            elif Trigger == "anal":                
                "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            $ newgirl["Mystique"].Mouth = "lipbite"
            $ newgirl["Mystique"].Spunk.append("mouth")
            "When she finishes, she draws her hand across her lips."
            call MystiqueFace("bemused")
            $ newgirl["Mystique"].Spunk.remove("mouth")
            ch_m "I'm sorry, [newgirl[Mystique].Petname], but that would have been a waste."
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -5)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)
            jump Mystique_Swallowed
    $ P_Cock = "out"
    $ P_Spunk = "out"
    $ newgirl["Mystique"].Spunk.append("belly")
    if Trigger == "sex":
            "You pull out of her pussy with a pop and spray all over her belly."
    elif Trigger == "anal":
            "You pull out of her ass with a pop and spray all over her belly."
    else:
            "You pick up the pace and with a grunt you spray all over her belly."
        
                  
    if newgirl["Mystique"].Addict >= 60 and ApprovalCheck("Mystique", 800, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) and newgirl["Mystique"].Swallow: 
            #if she's manic and has swallowed
            $ newgirl["Mystique"].Eyes = "manic"
            $ newgirl["Mystique"].Blush = 1        
            "Mystique's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
            call MystiqueFace("manic", 1)
            $ newgirl["Mystique"].Spunk.append("mouth")
            $ newgirl["Mystique"].Mouth = "smile"
            ch_m "Well, [newgirl[Mystique].Petname], I just couldn't let that go to waste."
            $ newgirl["Mystique"].Spunk.remove("mouth")  
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
            jump Mystique_Swallowed
          
        
    #else . . .
    call MystiqueFace("sexy", 1)    
    ch_m "Mmmm, all over the place. . ."
    #call Mystique_Sex_Reset
    jump Mystique_Orgasm_After

# Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_SpunkBack: 
    call Mystique_Doggy_Launch("hotdog")
    $ Speed = 0
    if newgirl["Mystique"].Addict >= 60 and ApprovalCheck("Mystique", 1000, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed))  and newgirl["Mystique"].Swallow:
            $ newgirl["Mystique"].Eyes = "manic"
            $ newgirl["Mystique"].Blush = 1
            call Mystique_BJ_Launch("cum")
            if Trigger == "sex":
                "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            elif Trigger == "anal":                
                "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            $ newgirl["Mystique"].Mouth = "lipbite"
            $ newgirl["Mystique"].Spunk.append("mouth")
            "When she finishes, she draws her hand across her lips."
            call MystiqueFace("bemused")
            $ newgirl["Mystique"].Spunk.remove("mouth")
            ch_m "I'm sorry, [newgirl[Mystique].Petname], but that would have been a waste."
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -5)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)
            jump Mystique_Swallowed
    $ P_Cock = "out"
    $ P_Spunk = "out"
    $ newgirl["Mystique"].Spunk.append("back")
    if Trigger == "sex":
            "You pull out of her pussy with a pop and spray all over her backside."
    elif Trigger == "anal":
            "You pull out of her ass with a pop and spray all over her backside."
    else:
            "You pick up the pace and with a grunt you spray all over her backside."
        
                  
    if newgirl["Mystique"].Addict >= 60 and ApprovalCheck("Mystique", 800, "I", Bonus = ((newgirl["Mystique"].Addict*10)- newgirl["Mystique"].Obed)) and newgirl["Mystique"].Swallow: 
            #if she's manic and has swallowed
            $ newgirl["Mystique"].Eyes = "manic"
            $ newgirl["Mystique"].Blush = 1        
            "Mystique's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
            call MystiqueFace("manic", 1)
            $ newgirl["Mystique"].Spunk.append("mouth")
            $ newgirl["Mystique"].Mouth = "smile"
            ch_m "Well, [newgirl[Mystique].Petname], I just couldn't let that go to waste."
            $ newgirl["Mystique"].Spunk.remove("mouth")
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
            jump Mystique_Swallowed
          
        
    #else . . .
    call MystiqueFace("sexy", 1)
    ch_m "Hmm. . . you made a mess. . ."  
    #call Mystique_Sex_Reset
    jump Mystique_Orgasm_After
    
   
#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_Handy_Finish:
    if renpy.showing("Mystique_SexSprite"):
        call Mystique_Sex_Reset
    call Mystique_HJ_Launch("cum")
    $ Speed = 2        
    $ newgirl["Mystique"].Spunk.append("hand")  
    if renpy.showing("Mystique_HJ_Animation"):                                  
            "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands." 
    else:
            "She grins and starts jerking you off, placing her left hand over your tip. You burst all over her hands." 
    $ Speed = 0
    
    if newgirl["Mystique"].Addict > 80 or "hungry" in newgirl["Mystique"].Traits:
            $ newgirl["Mystique"].Eyes = "manic"
            $ newgirl["Mystique"].Spunk.remove("hand")
            $ newgirl["Mystique"].Spunk.append("mouth")
            $ newgirl["Mystique"].Mouth = "smile"
            "She licks her hands off with a satisfied grin."
            $ newgirl["Mystique"].Spunk.remove("mouth")
            ch_m "Hmmm. . ."
    else:
            call MystiqueFace("bemused")
            $ newgirl["Mystique"].Spunk.remove("hand")
            "She wipes her hands off, but takes a quick sniff when she's done and smiles."
            ch_m "I appreciate the warning." 
            jump Mystique_Orgasm_After


#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_Swallowed: 
        $ newgirl["Mystique"].Swallow += 1
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
        $ newgirl["Mystique"].Addict -= 20    
        if "mouth" in newgirl["Mystique"].Spunk:
                $ newgirl["Mystique"].Spunk.remove("mouth")
        if "full" not in newgirl["Mystique"].RecentActions and Action_Check("Mystique", "recent", "swallowed") >= 5: 
                $ newgirl["Mystique"].RecentActions.append("full")    
                call MystiqueFace("surprised", 1)
                ch_m "-ehem-"
                call MystiqueFace("sexy", 1)
                ch_m "Excuse me [newgirl[Mystique].Petname], it must have been something I ate."
        $ newgirl["Mystique"].RecentActions.append("swallowed")                      
        $ newgirl["Mystique"].DailyActions.append("swallowed") 
        $ newgirl["Mystique"].Addictionrate += 2
        if "addictive" in P_Traits:
                $ newgirl["Mystique"].Addictionrate += 2
        if Trigger == "anal":    
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 2)
        if newgirl["Mystique"].Swallow == 1:
                $ newgirl["Mystique"].SEXP += 12
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5)
        jump Mystique_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_Creampied:
    if Trigger == "sex":
            $ newgirl["Mystique"].CreamP += 1
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 10)
            $ newgirl["Mystique"].RecentActions.append("creampie sex")                      
            $ newgirl["Mystique"].DailyActions.append("creampie sex") 
    elif Trigger == "anal":
            $ newgirl["Mystique"].CreamA += 1
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)
            $ newgirl["Mystique"].RecentActions.append("creampie anal")                      
            $ newgirl["Mystique"].DailyActions.append("creampie anal") 
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
    $ newgirl["Mystique"].Addict -= 30
    $ newgirl["Mystique"].Addictionrate += 2
    if "addictive" in P_Traits:
            $ newgirl["Mystique"].Addictionrate += 3
    if newgirl["Mystique"].CreamP == 1:
            $ newgirl["Mystique"].SEXP += 10
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5)
    #call Mystique_Sex_Reset

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Mystique_Orgasm_After:
        $ Line = "What next?"
        $ P_Semen -= 1
        $ P_Focus = 0
        $ Speed = 0  
        menu:
                "Want her to clean you off?"
                "Yes":
                    call Mystique_CleanCock
                "No":
                    pass
        if newgirl["Mystique"].Spunk:
                call Mystique_Cleanup
        $ Situation = 0
        return
        
        
label Mystique_CleanCock:
    $ Line = "What next?"
#    $ newgirl["Mystique"].Girl_Arms = 2
    $ P_Cock = "out"
    $ Speed = 0    
    if Trigger == "anal" and not ApprovalCheck("Mystique", 1600, TabM=1) and not newgirl["Mystique"].Addict >= 80:
            "She wipes your cock clean."
    elif newgirl["Mystique"].Blow > 3 or newgirl["Mystique"].Swallow: 
            if ApprovalCheck("Mystique", 1200, TabM=1) or newgirl["Mystique"].Addict >= 60:
                    call Mystique_BJ_Launch("cum")
                    $ Speed = 1
                    call MystiqueFace("sucking", 1) 
                    if ApprovalCheck("Mystique", 1500, TabM=1):
                        if newgirl["Mystique"].Love > newgirl["Mystique"].Inbt and newgirl["Mystique"].Love > newgirl["Mystique"].Obed:
                            "She looks up at you lovingly as she licks your cock clean."            
                        elif newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
                            $ newgirl["Mystique"].Eyes = "side"
                            "She dutifully licks your cock clean with lowered eyes."
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)                
                        else:
                            "She happily licks your cock clean." 
                    elif newgirl["Mystique"].Addict >= 60:
                            "She hungrily and thoroughly licks your cock clean."   
                    else:
                        "She licks you cock clean." 
                    call MystiqueFace("sexy") 
                    call Mystique_BJ_Reset            
            else:
                    if not renpy.showing("Mystique_HJ_Animation"):
                        call Mystique_HJ_Launch("cum") 
                    "She wipes your cock clean."  
    else:
                    if not renpy.showing("Mystique_HJ_Animation"):
                        call Mystique_HJ_Launch("cum") 
                    "She wipes your cock clean." 
    #call MystiqueFace("sexy", 1)
    #if ApprovalCheck("Mystique", 1200, TabM=1):
    #    if "hand" in newgirl["Mystique"].Spunk:
    #        $ newgirl["Mystique"].Spunk.remove("hand")
    #    $ newgirl["Mystique"].Spunk.append("mouth")
    #    "Mystique wipes your cock clean, and then licks her hands clean."
    #    $ newgirl["Mystique"].Spunk.remove("mouth")
    #    $ newgirl["Mystique"].Swallow += 1
    #    if newgirl["Mystique"].Swallow == 1:
    #            $ newgirl["Mystique"].SEXP += 12
    #            call MystiqueFace("sexy", 2, Mouth="kiss", Eyes="down")
    #            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5)
    #            "She gets a very excited look on her face as she does so."
    #            call MystiqueFace("sexy", 1)
    #    else:
    #            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)
    #else:
    #    if "hand" in newgirl["Mystique"].Spunk:
    #        $ newgirl["Mystique"].Spunk.remove("hand")
    #    "Mystique wipes your cock clean, and then wipes off her hands."
    $ P_Spunk = 0
    call MystiqueFace("sexy") 
    call Mystique_HJ_Reset 
    return
    
# End You Cumming //////////////////////////////////////////////////////////////////////////////////


# Mystique Lusty face check ////////////////////////////////////////////////////////////////////////////////
label MystiqueLust(Extreme = 0):
                
    if newgirl["Mystique"].Lust >= 90:        
            $ newgirl["Mystique"].Blush = 2
    elif newgirl["Mystique"].Lust >= 40:        
            $ newgirl["Mystique"].Blush = 1 
        
    if newgirl["Mystique"].Lust >= 80:
            $ newgirl["Mystique"].Wet = 2 
    elif newgirl["Mystique"].Lust >= 50:
            $ newgirl["Mystique"].Wet = 1
            
    if newgirl["Mystique"].Loc == "bg teacher":
            #this prevents her face from changing if she's just being a teacher.
            return
    elif Partner != "Mystique" and (Trigger == "kissing" or Trigger2 == "kissing" or Trigger5 == "kiss both" or Trigger5 == "kiss girl"):  
            #If Mystique is kissing and is primary
            $ newgirl["Mystique"].Eyes = "closed"
            if newgirl["Mystique"].Kissed >= 10 and newgirl["Mystique"].Inbt >= 300:
                $ newgirl["Mystique"].Mouth = "sucking"
            elif newgirl["Mystique"].Kissed > 1 and newgirl["Mystique"].Addict >= 50:            
                $ newgirl["Mystique"].Mouth = "sucking"
            else:
                $ newgirl["Mystique"].Mouth = "kiss"            
                
    elif Partner == "Mystique" and Trigger4 == "kissing":   
            #If Mystique is kissing in a threesome action
            $ newgirl["Mystique"].Eyes = "closed"
            if newgirl["Mystique"].Kissed >= 10 and newgirl["Mystique"].Inbt >= 300:
                $ newgirl["Mystique"].Mouth = "sucking"
            elif newgirl["Mystique"].Kissed > 1 and newgirl["Mystique"].Addict >= 50:            
                $ newgirl["Mystique"].Mouth = "sucking"
            else:
                $ newgirl["Mystique"].Mouth = "kiss"
            
    else:    
            #If Mystique is not kissing someone
            if newgirl["Mystique"].Lust >= 90:
                    $ newgirl["Mystique"].Eyes = "closed"
                    $ newgirl["Mystique"].Brows = "sad"
                    $ newgirl["Mystique"].Mouth = "surprised"
            elif newgirl["Mystique"].Lust >= 70:
                    $ newgirl["Mystique"].Eyes = "sexy"
                    $ newgirl["Mystique"].Brows = "sad"
                    $ newgirl["Mystique"].Mouth = "lipbite"
            elif newgirl["Mystique"].Lust >= 50 and not Extreme:
                    $ newgirl["Mystique"].Eyes = "sexy"
                    $ newgirl["Mystique"].Brows = "sad"
                    $ newgirl["Mystique"].Mouth = "lipbite"
            elif newgirl["Mystique"].Lust >= 30 and not Extreme:
                    $ newgirl["Mystique"].Eyes = "sexy"
                    $ newgirl["Mystique"].Brows = "normal"
                    $ newgirl["Mystique"].Mouth = "lipbite"
            elif not Extreme:
                    $ newgirl["Mystique"].Eyes = "sexy"
                    $ newgirl["Mystique"].Brows = "normal"
                    $ newgirl["Mystique"].Mouth = "normal"    
    
    if Partner == "Mystique" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ newgirl["Mystique"].Mouth = "tongue"  
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ newgirl["Mystique"].Mouth = "tongue"  
                    
    if newgirl["Mystique"].OCount >= 10:   
            #If you've fucked her senseless
            $ newgirl["Mystique"].Eyes = "stunned"
            $ newgirl["Mystique"].Mouth = "tongue"   
                
    return

# End faces

#  Mystique Orgasm //////////////////////////

label Mystique_Cumming:
    $ newgirl["Mystique"].Eyes = "surprised"
    $ newgirl["Mystique"].Brows = "sad"
    $ newgirl["Mystique"].Mouth = "sucking"
    $ newgirl["Mystique"].Blush = 1
    ch_m ". . . !"
    $ Speed = 0
    if renpy.showing("Mystique_SexSprite"):
            show Mystique_SexSprite #fix, test this
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
    $ Speed = 1
    $ Line = renpy.random.choice(["Mystique is suddenly rocked with spasms, holding back a muffled scream.", 
                "Mystique grabs on tightly as her body shakes with pleasure.", 
                "Mystique stiffens and lets out a low moan.",
                "Mystique's body quivers and suddenly goes still."])
    "[Line]"
    
    $ newgirl["Mystique"].Eyes = "closed"
    $ newgirl["Mystique"].Brows = "sad"
    $ newgirl["Mystique"].Mouth = "tongue"
    $ Line = renpy.random.choice(["Uuuuuh. . . lovely.", 
                "I really enjoyed that one. . .", 
                "Hmmmm. . . .",
                "That was. . . great. . ."])
    ch_m "[Line]"
           
    
    $ newgirl["Mystique"].Lust = 30 if "hotblooded" in newgirl["Mystique"].Traits else 0 
    $ newgirl["Mystique"].Lust += (newgirl["Mystique"].OCount * 5)
    $ newgirl["Mystique"].Lust = 80 if newgirl["Mystique"].Lust >= 80 else newgirl["Mystique"].Lust    
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
            
    if "unsatisfied" in newgirl["Mystique"].RecentActions:  #If she had been unsatisfied, you satisfied her. . .        
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            if "unsatisfied" in newgirl["Mystique"].DailyActions:
                ch_m "Making up for past mistakes, [newgirl[Mystique].Petname]?"
            call DrainWord("Mystique","unsatisfied")
    $ newgirl["Mystique"].Org += 1
    $ Line = 0
      
    if Trigger != "masturbation":
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 40, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)            
    #Orgasm count
            if Trigger != "blow" and Trigger != "hand":
                $ newgirl["Mystique"].OCount += 1        
                if newgirl["Mystique"].OCount == 2:
                        $ newgirl["Mystique"].Brows = "confused"
                        ch_m "Excellent job, [newgirl[Mystique].Petname]. . ."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)            
                elif newgirl["Mystique"].OCount == 3: #5
                        $ newgirl["Mystique"].Brows = "confused"            
                        ch_m "You . . .certainly. . . have some. . . stamina. . ."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 2)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)                    
                elif newgirl["Mystique"].OCount == 5: #10
                    $ newgirl["Mystique"].Mouth = "tongue"    
                    ch_m "You're . . .practically. . . exhausting. . ."
                    menu:
                        ch_m "would. . . you. . . mind. . . a break?"
                        "Finish up." if P_FocusX:
                            "You release your concentration. . ."                 
                            $ P_FocusX = 0
                            $ P_Focus += 15                    
                        "Let's try something else." if MultiAction:  
                            $ Situation = "shift"
                        "No, I'm not done yet.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck("Mystique", 1000, TabM=1) or ApprovalCheck("Mystique", 400, "O", TabM=1):
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 3)
                                    $ newgirl["Mystique"].Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                                else:
                                    call MystiqueFace("angry", 1)
                                    "She scowls at you, pulls out with a pop, and wipes herself off."
                                    ch_m "Learn to take a hint. . ."
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                            else:
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                $ newgirl["Mystique"].Eyes = "stunned"
                                "She drifts off into incoherent moans."  
                #end Ocount stuff
    return
    
# End Mystique Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Mystique Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Mystique_Cleanup(Options = [], Cnt = 0, Line = "random", Cleaned = 0):
    if not newgirl["Mystique"].Spunk:
        $ newgirl["Mystique"].Wet = 0
        return     
        
    if newgirl["Mystique"].Addict > 80 and newgirl["Mystique"].Swallow:
        #if she likes cum, she prefers to eat it. 
        $ Line = "eat"            
        $ newgirl["Mystique"].Eyes = "manic"
        $ newgirl["Mystique"].Mouth = "smile" 
    elif "painted" in newgirl["Mystique"].RecentActions and ApprovalCheck("Mystique", 1000, "OI"):
        return
    elif ApprovalCheck("Mystique", 1200, "LO"):  
        $ Line = "ask"            
    elif not ApprovalCheck("Mystique", 400, "I"):
        call MystiqueFace("bemused") 
        $ Line = "clean"   
    else:
        $ Line = "ask"      
   
    $ Cleaned = 1 if "cleaned" in newgirl["Mystique"].DailyActions else 0
    $ newgirl["Mystique"].RecentActions.append("cleaned") 
    $ newgirl["Mystique"].DailyActions.append("cleaned") 
    
    if Line == "ask":
            $ Line = "random"
            "She looks down at the spunk covering her."
            menu:
                "What do you suggest Mystique do about cleaning up?"
                "You should leave it where it is.":
                        if ApprovalCheck("Mystique", 900, "I") or "exhibitionist" in newgirl["Mystique"].Traits:
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5) 
                                $ Line = "leave"  
                                call MystiqueFace("sly") 
                                ch_m "Hmm. . . I suppose I could use some accessories. . "
                        elif ApprovalCheck("Mystique", 600, "I") and ApprovalCheck("Mystique", 1200, "LO"):
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5) 
                                $ Line = "leave"  
                                call MystiqueFace("surprised",2) 
                                ch_m "Hmm. . . if you insist. . ."
                                call MystiqueFace("sly",1) 
                        
                        else:
                            call MystiqueFace("angry") 
                            menu:
                                ch_m "Excuse me?" 
                                "Please?":
                                    if ApprovalCheck("Mystique", 1800):
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 3) 
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                                        ch_m "Well. Ok."
                                        $ Line = "leave"  
                                    elif Cleaned:
                                        call MystiqueFace("angry") 
                                        ch_m "I believe I've made myself clear."
                                    elif ApprovalCheck("Mystique", 800):
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1) 
                                        ch_m "You're persistant, but no."
                                    else:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 75, -5)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, -10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                                        call MystiqueFace("angry") 
                                        ch_m "Of course not."
                                "I insist.":
                                    call MystiqueFace("sad") 
                                    if ApprovalCheck("Mystique", 400, "I") and ApprovalCheck("Mystique", 1200, "LO"):
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 3)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                                        ch_m "Well then."
                                        $ Line = "leave"  
                                    elif ApprovalCheck("Mystique", 800, "O"):
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                                        ch_m "If I must."
                                        $ Line = "leave"  
                                    elif Cleaned:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -1)
                                        call MystiqueFace("angry") 
                                        ch_m "That's enough of that."
                                    elif ApprovalCheck("Mystique", 800):
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -1)
                                        call MystiqueFace("sad") 
                                        ch_m "Don't push me." 
                                    else:
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10)
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                        call MystiqueFace("angry") 
                                        ch_m "Obviously not."
                                        
                                "Never mind then.":
                                    ch_m "Ok. . ."                            
                        #end "leave it"
                        
                "You should just eat it.":
                        call MystiqueFace("sly") 
                        if "hungry" in newgirl["Mystique"].Traits or (newgirl["Mystique"].Swallow >= 5 and ApprovalCheck("Mystique", 800)): 
                                #lots of swallows
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5) 
                                $ Line = "eat"   
                                ch_m "Well, I suppose I could. . ."
                        elif newgirl["Mystique"].Swallow and ApprovalCheck("Mystique", 800): 
                                #few swallows
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5) 
                                $ Line = "eat"   
                                ch_m "You do have a unique flavor. . ."
                        elif ApprovalCheck("Mystique", 1200): 
                                #no swallows, but likes you
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                                $ Line = "eat"   
                                ch_m "I have been a bit curious. . ."
                        elif ApprovalCheck("Mystique", 400): 
                                #Likes you well enough, but won't
                                call MystiqueFace("sad") 
                                ch_m "I doubt that."
                        else: 
                                #doesn't like you.
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -3)
                                call MystiqueFace("angry") 
                                ch_m "No."
                        #end eat it
                              
                "You should just clean it up.":
                        if ApprovalCheck("Mystique", 600, "I") and not ApprovalCheck("Mystique", 1500, "LO"): #rebellious
                                call MystiqueFace("sly") 
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 10) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
                                ch_m "Hmmm. . . don't I look good like this? . ."
                                $ Line = "leave"   
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                        call MystiqueFace("smile") 
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                    "No, clean it up.": 
                                        if ApprovalCheck("Mystique", 600, "O"):
                                            call MystiqueFace("sad") 
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                            ch_m "Oh, if I must. . ."
                                            $ Line = "clean"  
                                        elif ApprovalCheck("Mystique", 1200, "LO"):
                                            call MystiqueFace("sad") 
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                            ch_m "Spoilsport. . ."
                                            $ Line = "clean"   
                                        else:
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -5)
                                            ch_m "I'm afraid you don't have any say in the matter."
                                                                                    
                        else: #agrees
                                call MystiqueFace("bemused") 
                                $ Line = "clean"   
                                ch_m "If I must. . ."
                        #end clean it up
                        
                "Say nothing. [[leave it to her]":
                    $ Line = "random"
            #end "asked"
                
                
    if Line == "random":
            $ Options = ["clean"]
            if newgirl["Mystique"].Swallow and ApprovalCheck("Mystique", 800):
                $ Options.append("eat") 
                if newgirl["Mystique"].Swallow >=5:                            
                    $ Options.append("eat") 
                if "hungry" in newgirl["Mystique"].Traits:                
                    $ Options.append("eat") 
            if ApprovalCheck("Mystique", 600, "I"):
                $ Options.append("leave") 
                if ApprovalCheck("Mystique", 800, "I"):
                    $ Options.append("leave") 
                if "exhibitionist" in newgirl["Mystique"].Traits:
                    $ Options.append("leave") 
                    
            $ renpy.random.shuffle(Options)
            
            $ Line = Options[0]
            #end "random"
            
            
    if Line == "leave":
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 1) 
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in newgirl["Mystique"].Spunk: 
                    $ newgirl["Mystique"].Spunk.remove("hand")
                    if newgirl["Mystique"].Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."   
            if "mouth" in newgirl["Mystique"].Spunk:                  
                    $ newgirl["Mystique"].Spunk.remove("mouth")
            $ newgirl["Mystique"].RecentActions.append("painted")  #means she left the jiz on                   
            $ newgirl["Mystique"].DailyActions.append("painted")                         
            return
            #end "leave it"

    $ Cnt = 0
    $ newgirl["Mystique"].Spunk.append("hand")
    if "mouth" in newgirl["Mystique"].Spunk and Line != "eat":
            $ newgirl["Mystique"].Spunk.remove("mouth")
            "She spits out the spunk in her mouth and dribbling down her chin,"
            $ Cnt += 1
    if "hair" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("hair")
            if Cnt:            
                "then she wipes the spunk out of her hair,"
            else:
                "She wipes the spunk out of her hair,"
            $ Cnt += 1
    if "facial" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("facial")
            if Cnt:
                "then she wipes the spunk off of her face,"   
            else:
                "She wipes the spunk off of her face,"   
            $ Cnt += 1         
    if "tits" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("tits")
            if Cnt:
                "then she wipes the spunk off of her chest,"   
            else:
                "She wipes the spunk off of her chest," 
            $ Cnt += 1           
    if "back" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("back")
            if Cnt:
                "then she wipes the spunk off of her back,"   
            else:
                "She wipes the spunk off her lower back," 
            $ Cnt += 1     
    if "in" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("in")
            if Cnt:
                "then she wipes the spunk inside her pussy,"   
            else:
                "She wipes the spunk inside her pussy,"     
            $ Cnt += 1 
    if "anal" in newgirl["Mystique"].Spunk and (ApprovalCheck("Mystique", 800, "I") or Line != "eat"):
            while "anal" in newgirl["Mystique"].Spunk:
                $ newgirl["Mystique"].Spunk.remove("anal")
            if Cnt:
                "then she wipes the spunk dripping out of her ass,"   
            else:
                "She wipes the spunk dripping our of her ass,"
            $ Cnt += 1            
    if "hand" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("hand")
            if Line == "eat":                    
                $ newgirl["Mystique"].Spunk.append("mouth")
                if Cnt and "anal" in newgirl["Mystique"].Spunk:
                    "then licks her hands off with a satisfied grin," 
                if Cnt:
                    "and finally she licks her hands off with a satisfied grin." 
                else:
                    "She licks her hands off with a satisfied grin."   
                    
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
                $ newgirl["Mystique"].Spunk.remove("mouth")
                $ newgirl["Mystique"].Swallow += 1     
                $ newgirl["Mystique"].Addict -= (10*Cnt)
                if newgirl["Mystique"].Swallow == 1:
                    $ newgirl["Mystique"].SEXP += 12
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5)
                $ newgirl["Mystique"].RecentActions.append("swallowed")                     
                $ newgirl["Mystique"].DailyActions.append("swallowed") 
            else:
                if Cnt:
                    "and finally, she wipes her hands off with a nearby tissue." 
                else:
                    "She wipes her hands off with a nearby tissue."                    
            $ Cnt += 1
    if "anal" in newgirl["Mystique"].Spunk:
            $ newgirl["Mystique"].Spunk.remove("anal")
            if Cnt:
                "Afterward, she wipes the spunk dripping our of her ass."
            else:
                "She wipes the spunk dripping out of her ass."
    $ newgirl["Mystique"].Wet = 0        
    $ del newgirl["Mystique"].Spunk[:]   
    if Cnt >= 5:
            $ newgirl["Mystique"].Eyes = "surprised"
            ch_m "I really was a \"cum dumpster\" there."
            $ newgirl["Mystique"].Eyes = "sexy"
    elif Cnt >=3:
            ch_m "Well that was a lot of work."
    elif Line == "eat" and newgirl["Mystique"].Swallow >= 5:
            ch_m "Mmmm, now I'm hungry for more."
    return    
    
# End Mystique Clean-Up /////////////////////////////////////////////////////////////////////////////////////

