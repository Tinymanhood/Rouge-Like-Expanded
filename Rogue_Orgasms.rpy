# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label PR_Cumming:
    call Shift_Focus("Rogue")
    if Trigger == "blow":
            $ Tempmod += 5
        
    if R_Addict > 75:
            $ Tempmod += 20
    elif R_Addict > 50:
            $ Tempmod += 5
    
    if R_Swallow >= 10:
            $ Tempmod += 15  
    elif R_Swallow >= 3:
            $ Tempmod += 5
        
    if (R_CreamP + R_CreamA) >= 10:
            $ Tempmod += 15 
    elif (R_CreamP + R_CreamA) >= 3:
            $ Tempmod += 5        
       
    $ D20 = renpy.random.randint(1, 20) 
    
# intro lines    
    if Trigger == "hand":
            $ Line = "As she strokes, you're about ready to come. . ."
    elif Trigger == "blow":
            $ Line = "As she sucks at you, you start to feel about to come. . ."
    elif Trigger == "titjob":
            $ Line = "As you rub into her cleavage, you start to feel about to come. . ."
    elif Trigger == "sex" or Trigger == "anal":
            $ Line = "As you thrust into her, you feel about to blow. . ."
    elif Trigger == "hotdog":
            $ Line = "As you grind into her, you feel about to blow. . ."
    else:        
            $ Line = "You start to feel about to come. . ."    
    
    call RogueFace("sexy") 
    
    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
                jump R_Warn_Her
            
        "Ask to cum in her mouth": 
                $ Situation = "asked"
                jump R_In_Mouth                            
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                $ Situation = "auto"
                jump R_In_Mouth
        
        "Ask to cum inside her" if Trigger == "sex":
                $ Situation = "asked"
                jump R_Creampie_P        
        "Ask to cum inside her" if Trigger == "anal":
                $ Situation = "asked"
                jump R_Creampie_A
                
        "Cum inside her" if Trigger == "sex":
                $ Situation = "auto"
                jump R_Creampie_P        
        "Cum inside her" if Trigger == "anal":
                $ Situation = "auto"
                jump R_Creampie_A
            
        "Cum on her face":
                jump R_Facial            
        "Cum on her ass" if Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog":
                jump R_SpunkBack
            
        "Pull back":
            if renpy.showing("Rogue_BJ_Animation"):
                    if R_Addict >= 60 and ApprovalCheck("Rogue", 1000, "I", Bonus = ((R_Addict*10)- R_Obed)) and R_Swallow:
                            $ R_Eyes = "manic"
                            $ Speed = 0
                            "You pull out of her mouth with a pop, and her eyes widen in surprise."
                            $ R_Mouth = "sucking"
                            $ R_Spunk.append("mouth")
                            $ Speed = 4
                            "She leaps at your cock and sucks it deep, draining your fluids hungrily." 
                            $ Speed = 0
                            $ R_Mouth = "lipbite"
                            "When she finishes, she licks her lips."
                            call RogueFace("bemused")
                            ch_r "Sorry, [R_Petname], I just couldn't let that go to waste."
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, -5)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 10)
                            jump R_Swallowed                            
                    call Rogue_BJ_Reset                
            elif renpy.showing("Rogue_HJ_Animation"):
                    call Rogue_HJ_Reset                
            elif renpy.showing("Rogue_Doggy"):
                    call Rogue_Doggy_Reset                    
            if ApprovalCheck("Rogue", 500, "I", Bonus = ((R_Addict*10)- R_Obed)) and R_Addict > 50 and R_Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ R_Eyes = "manic"
                    $ R_Mouth = "kiss"
                    $ Speed = 0
                    "Her eyes widen in panic."
                    ch_r "Are you sure you won't reconsider, [R_Petname]?" 
                    $ R_Blush = 2
                    menu:
                        extend ""
                        "Ok, if you'll swallow it.":
                                if Trigger != "blow": 
                                    call Rogue_BJ_Launch("cum")
                                call RogueFace("sucking") 
                                $ Speed = 2
                                "She nods and puts the tip into her mouth. as you release she gulps it down hungrily."
                                call RogueFace("sexy")                      
                                $ R_Mouth = "sucking"
                                $ R_Spunk.append("mouth")
                                ". . ."
                                $ Speed = 0
                                call RogueFace("sad")                       
                                $ R_Mouth = "lipbite"
                                ch_r "That would have been such a waste otherwise."   
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                                jump R_Swallowed                                
                        "No, we're done for now.": #If addict is > obedience + 50. . .
                                if ApprovalCheck("Rogue", 250, "I", Bonus = ((R_Addict*10)- R_Obed)) or R_Addict > 75:                            
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, -2)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3)
                                        if Trigger != "blow":
                                            call Rogue_BJ_Launch("cum")
                                            $ Speed = 4
                                        "She dives down on you and you can't resist filling her throat."
                                        $ Speed = 0
                                        ch_r "I. . . just can't pass this up."
                                        jump R_Swallowed                                
                                else:                         
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 3)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                                        call RogueFace("sad")
                                        $ R_Brows = "confused"
                                        ch_r "ok. . ."
                                        $ Line = 0
                                        $ P_Focus -= 5
                                        return  
                    #manic, wanted to swallow
                    
            call RogueFace("sexy", 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips." 
            ch_r "Well [R_Petname], what next then?"
            $ Line = 0
            $ P_Focus = 95
            return
            #end "pull back"
#End Main orgasm menu


label R_Warn_Her:                                                                                                                       #Warn her start
        "You let her know that you're going to come."
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 3)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5) if R_Obed >= 500 else R_Obed   
        if "hungry" in R_Traits and D20 >= 5:
                if renpy.showing("Rogue_Doggy"):
                    call Rogue_HJ_Launch("cum")   
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                call RogueFace("sucking")       
                ". . ."
                $ Speed = 0
                $ R_Spunk.append("mouth")
                if not renpy.showing("Rogue_BJ_Animation"):
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:                    
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."        
                call RogueFace("sexy")
                $ R_Mouth = "smile"
                ch_r "That was real sweet, [R_Petname], thanks for the head's up."        
                jump R_Swallowed
        #End Hungy take-over
            
        if Trigger == "sex" and R_CreamP >= 5: 
                # She's Creampied a few times
                call RogueFace("sexy")
                $ P_Cock = "in"
                $ R_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."   
                if R_Lust >= 85: 
                    call R_Cumming  
                jump R_Creampied
        
        elif Trigger == "sex" and R_CreamP and D20 >= 10:  
                # She's Creampied at least once
                call RogueFace("sexy")
                $ P_Cock = "in"
                $ R_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."          
                if R_Lust >= 85: 
                    call R_Cumming  
                jump R_Creampied
            
        elif Trigger == "anal" and R_CreamA >= 5: 
                # She's Anal Creampied a few times
                call RogueFace("sexy")
                $ P_Cock = "anal"
                $ R_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She smiles and speeds up her actions, causing you to erupt inside her."         
                if R_Lust >= 85: 
                    call R_Cumming  
                jump R_Creampied
        
        elif Trigger == "anal" and R_CreamA and D20 >= 10: 
                # She's Anal Creampied at least once
                call RogueFace("sexy")
                $ P_Cock = "anal"
                $ R_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                "She gets a michevious look and speeds up, you burst inside her."    
                if R_Lust >= 85: 
                    call R_Cumming          
                jump R_Creampied
            
        elif Trigger != "anal" and R_Swallow >= 5: 
                #If she's swallowed a lot                
                if renpy.showing("Rogue_BJ_Animation"):            
                        call RogueFace("sucking")
                        $ R_Spunk.append("mouth")
                        "She makes a little humming sound, but keeps sucking."
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:
                        if renpy.showing("Rogue_Doggy"):
                            call Rogue_BJ_Launch("cum")
                            $ Speed = 2
                        call RogueFace("sucking")
                        $ R_Spunk.append("mouth")
                        "She smiles and then puts your tip in her mouth."
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."                
                $ Speed = 0
                call RogueFace("sexy")
                $ R_Mouth = "smile"
                ch_r "That was real sweet, [R_Petname], thanks for the head's up."  
                jump R_Swallowed
            
        elif R_Swallow and D20 >= 10:  
                #She's swallowed before, but not a lot  
                if renpy.showing("Rogue_Doggy"):
                    call Rogue_HJ_Launch("cum") 
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                if renpy.showing("Rogue_BJ_Animation"): 
                        #if she's blowing
                        call RogueFace("sucking")
                        $ R_Spunk.append("mouth")
                        "She makes a little humming sound, but keeps sucking."
                        "When you finish filling her mouth, she gags a little, but manages to swallow it."
                        $ Speed = 0
                        call RogueFace("sexy")
                        $ R_Mouth = "smile"
                        if R_Addict > 50:
                                $ R_Eyes = "manic"
                                "She gulps it down hungrily and licks her lips."
                        call RogueFace("bemused")
                        ch_r "I'm still starting to get used to that, thanks for the head's up."
                        jump R_Swallowed                    
                        #fix, add titjob option here.   
                else:
                        #If she's handying
                        jump R_Handy_Finish    
        #end if she's swallowed        
            
        elif ApprovalCheck("Rogue", 1000):                    
                #warned but likes you and experienced
                if R_SEXP > 20 and renpy.showing("Rogue_Doggy"):
                        "She gently pushes you back off of her."
                        jump R_SpunkBack
                elif R_SEXP > 20:
                        jump R_Facial            
        
                if renpy.showing("Rogue_HJ_Animation") and R_Hand:
                        jump R_Handy_Finish
                elif renpy.showing("Rogue_BJ_Animation") and R_Blow:
                        jump R_Handy_Finish
                elif renpy.showing("Rogue_TJ_Animation") and R_Tit:
                        jump R_Facial
                elif renpy.showing("Rogue_Doggy") and R_Sex and Trigger == "sex":
                        "She gently pushes you back off of her."
                        jump R_SpunkBack
                elif renpy.showing("Rogue_Doggy") and R_Anal and Trigger == "anal":
                        "She gently pushes you back off of her."
                        jump R_SpunkBack
        
        
        # Else. . . not experienced or she's not a huge fan, 
        if renpy.showing("Rogue_BJ_Animation"):
                $ Situation = "auto"
                jump R_In_Mouth
        elif Trigger == "sex" or Trigger == "anal":
                call Rogue_Doggy_Reset
                "She pulls off of you and grabs your cock in her hand."
                jump R_Handy_Finish
        elif renpy.showing("Rogue_Doggy"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump R_SpunkBack
        else:
                jump R_Facial
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
                      
                      
#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_In_Mouth:      
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in R_Traits and R_Addict <= 50 and "full" in R_RecentActions:
            $ Tempmod -= 15                  
                
    if Situation == "auto":
                $ Situation = 0
                if not renpy.showing("Rogue_BJ_Animation"):
                        call Rogue_BJ_Launch("cum")
                $ Speed = 2
                "You grab her head and cum in her mouth"  
                $R_Eyes = "closed"        
                show Rogue_BJ_Animation
                with vpunch
                if "full" in R_RecentActions:
                        #if she's had enough
                        call RogueFace("bemused")
                        $ R_Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ R_Spunk.remove("mouth")
                        ch_r "Um, I. . . I think I've had enough for now, could we maybe. . ."
                        ch_r ". . . put that stuff someplace else?"
                elif R_Swallow >= 5 or "hungry" in R_Traits:
                        #if she likes to swallow
                        call RogueFace("sexy")
                        $ R_Mouth = "smile"
                        $ R_Spunk.append("mouth")
                        "She quickly gulps it down and wipes her mouth."
                        $ R_Spunk.remove("mouth")
                        $ Speed = 0
                        ch_r "That was real sweet, [R_Petname]."
                        call RogueFace
                elif R_Swallow:
                        call RogueFace("bemused")
                        $ R_Spunk.append("mouth")
                        $ Speed = 0
                        "She gags a little, but manages to swallow it."
                        $ R_Spunk.remove("mouth")
                        ch_r "I'm starting to get used to that, but warn me next time?"
                        call RogueFace
                elif not R_Swallow and R_Addict >= 50 and R_Inbt < 400 and R_Blow < 10:
                        call RogueFace("bemused", 1)
                        $ R_Spunk.append("mouth")
                        ". . ."            
                        $ R_Spunk.remove("mouth")
                        $ R_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ R_Spunk.remove("hand")
                        ch_r "I. . . don't really like the taste of that."
                        $ R_Addictionrate += 1
                        if "addictive" in P_Traits:
                            $ R_Addictionrate += 1
                        call RogueFace
                        jump R_Orgasm_After
                elif not R_Swallow and R_Addict >= 50:
                        call RogueFace("sexy")
                        $ R_Mouth = "tongue"
                        $ R_Spunk.append("mouth")
                        ". . ."
                        $ R_Spunk.remove("mouth")
                        $ R_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ R_Spunk.remove("hand")
                        ch_r "I would be mad, but you taste so sweet, [R_Petname]."  
                        call RogueFace
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                elif not R_Swallow:
                        if ApprovalCheck("Rogue", 800, "LI") and ApprovalCheck("Rogue", 400, "OI"):
                            call RogueFace("angry")
                            $ R_Spunk.append("mouth")
                        else:
                            call RogueFace("bemused")
                            $ R_Mouth = "tongue"
                            $ R_Spunk.append("mouth")
                        ". . ."
                        $ R_Spunk.append("hand")
                        $ Speed = 0
                        "She gags and spits it into her palm."   
                        menu:
                            ch_r "Hey, who said you could come in my mouth, [R_Petname]?"
                            "Sorry about that.":
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                                    $ R_Addictionrate += 1
                                    if "addictive" in P_Traits:
                                        $ R_Addictionrate += 1
                                    call RogueFace("smile", 1)
                                    ch_r "Aw, well a little warning wouldn't hurt, [R_Petname]."
                                    jump R_Orgasm_After
                                
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck("Rogue", 1200):
                                        "She tentatively licks her hand, and then gulps it down."
                                        $ R_Spunk.remove("hand")
                                        call RogueFace("sexy", 1)
                                        $ R_Spunk.append("mouth")
                                        ch_r "Hmm, that really wasn't half bad, [R_Petname]."
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                                        $ R_Spunk.remove("mouth")
                                    elif ApprovalCheck("Rogue", 1200, "OI", Bonus = (R_Addict*10)):
                                        call RogueFace("bemused", 1)
                                        $ R_Brows = "normal" 
                                        $ R_Mouth = "sad"
                                        $ R_Spunk.remove("hand")
                                        $ R_Spunk.append("mouth")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ R_Spunk.remove("mouth")
                                        ch_r "I'm not really a fan of that, [R_Petname]."
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                                    else:
                                        $ R_Spunk.remove("hand")
                                        "She scowls at you and wipes her hand off. Then she licks her lips."
                                        jump R_Orgasm_After
                                    
                            "Swallow it, now.":
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 30, -1, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -1, 1)                    
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -1, 1)
                                    if ApprovalCheck("Rogue", 1200, "OI") or R_Addict >= 50:                            
                                        call RogueFace("sad", 1)
                                        $ R_Spunk.append("mouth")
                                        $ R_Spunk.remove("hand")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ R_Spunk.remove("mouth")
                                        ch_r "I'm not really a fan of that, [R_Petname]."
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                                    else:         
                                        $ R_Spunk.remove("hand")               
                                        "She scowls at you and wipes her hand off. Then she licks her lips."                        
                                        jump R_Orgasm_After
                else:                
                            jump R_Orgasm_After
                                
                jump R_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    
    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing("Rogue_Doggy"):
            call Rogue_HJ_Launch("cum")
        
    if "full" in R_RecentActions:
            pass
        
    elif R_Swallow >= 5 or "hungry" in R_Traits:  
            # If she's swallowed 5 times, 
            call RogueFace("sucking")
            if not renpy.showing("Rogue_BJ_Animation"):
                call Rogue_BJ_Launch("cum")            
                $ Speed = 2
                "She nods and bends down to put the tip between her lips. After you cum, she quickly gulps it down and wipes her mouth."
            else:            
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
            $ R_Spunk.append("mouth")
            ". . ."
            call RogueFace("sexy")            
            $ Speed = 0
            ch_r "That was real sweet, [R_Petname]."
            $ R_Spunk.remove("mouth")
            jump R_Swallowed
        
    elif R_Addict >= 80 and R_Swallow: 
            #addicted
            $ R_Brows = "confused"
            $ R_Eyes = "manic"
            if not renpy.showing("Rogue_BJ_Animation"):
                call Rogue_BJ_Launch("cum")            
                $ Speed = 2    
                "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow. She gags a little, but quickly swallows it."
            else:            
                $ Speed = 2
                "She nods and hums a \"yes\" sound."
            $ R_Mouth = "sucking"
            $ R_Spunk.append("mouth")
            ". . ."
            $ Speed = 0
            call RogueFace("sexy")
            $ R_Mouth = "smile"
            ch_r "I would be mad, but you taste so sweet, [R_Petname]."
            $ R_Spunk.remove("mouth")
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 5)
            jump R_Swallowed
            
    elif R_Swallow:                
            if ApprovalCheck("Rogue", 900):
                $ R_Brows = "confused"
                if not renpy.showing("Rogue_BJ_Animation"):
                    call Rogue_BJ_Launch("cum")            
                    $ Speed = 2    
                    "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow. She gags a little, but quickly swallows it."
                else:            
                    $ Speed = 2
                    "She tilts her head and hums a \"huh?\" sound."
                $ R_Mouth = "sucking"
                $ R_Spunk.append("mouth")
                $ R_Brows = "normal"
                $ R_Eyes = "sexy"
                ". . ."
                $ Speed = 0
                call RogueFace("sexy")
                $ R_Spunk.append("mouth")
                ch_r "I'm starting to get used to that."
                $ R_Spunk.remove("mouth")
                jump R_Swallowed
     
    #If she hasn't swallowed or doesn't automatically want to. . .  
    
    if  ApprovalCheck("Rogue", 300, "LI") or ApprovalCheck("Rogue", 300, "OI"): 
        call RogueFace("bemused")
        $ R_Eyes = "sexy"
    else:
        call RogueFace("angry")
        
    $ Speed = 0    
    
    if "full" in R_RecentActions:
            ch_r "I'm feeling a bit. . . \"full\" right now, [R_Petname]. . ." 
    else:
            ch_r "What makes you think I'd want that, [R_Petname]?"
    
    menu:
        extend ""
        "Sorry about that.":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                $ R_Addictionrate += 1
                if "addictive" in P_Traits:
                    $ R_Addictionrate += 1
                call RogueFace("smile", 1)
                ch_r "Well, maybe it would taste as sweet as your words, [R_Petname]."
                if ApprovalCheck("Rogue", 1200, TabM=1) and "full" not in R_RecentActions:
                    $ Approval = 2 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)  
                    call RogueFace("sexy", 1)
                    ch_r "Maybe it is worth a try. . ."
                else:
                    jump R_Handy_Finish                
            
        "Give it a try, you might like it." if "full" not in R_RecentActions:
                if ApprovalCheck("Rogue", 1200, TabM=1):  
                    $ Approval = 2
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                    $ R_Brows = "confused"  
                    $ R_Eyes = "sexy"
                    ch_r "If you say so. . ."
                else:     
                    $ R_Addictionrate += 1
                    if "addictive" in P_Traits:
                        $ R_Addictionrate += 1
                    $ R_Blush = 1
                    ch_r "You wish, [R_Petname]."
                    jump R_Handy_Finish
                            
        "Seriously, put it in your mouth.":
                if ApprovalCheck("Rogue", 1500, "LI", TabM=1) or ApprovalCheck("Rogue", 1200, "OI", TabM=1):
                        call RogueFace("sucking", 1)
                elif ApprovalCheck("Rogue", 1000, "OI", Bonus = (R_Addict*10)): #Mild addiction included                
                        call RogueFace("angry", 1)
                else: 
                        #You insisted, she refused. 
                        call RogueFace("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call Rogue_HJ_Launch("cum")
                        call Rogue_HJ_Reset                
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                        ch_r "Well if that's your attitude you can handle your own business."
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")   
                        $ Line = 0
                        return                    
                $ R_Mouth = "sucking"
                call Rogue_BJ_Launch("cum")            
                $ Speed = 2     
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
        
    if not renpy.showing("Rogue_BJ_Animation"):
        call Rogue_BJ_Launch("cum")            
    $ Speed = 2    
    if ApprovalCheck("Rogue", 1200):            
            "She gently puts the tip to her lips, just as you blow."
            "She gags a little, but quickly swallows it." 
    else:
            "She tentatively places the tip in her mouth, and you blast inside it. She quickly gulps it down."                    
            call RogueFace("sexy")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)        
    $ R_Mouth = "sucking"
    $ R_Spunk.append("mouth")
    ". . ."   
    $ Speed = 0            
    call RogueFace("sexy") 
    
    if ApprovalCheck("Rogue", 1000) and R_Swallow >= 3:
            ch_r "I'm starting to get used to that."    
    elif ApprovalCheck("Rogue", 800):                
            ch_r "Hmm, that really wasn't half bad, [R_Petname]."
    else:
            call RogueFace("sad")
            ch_r "I'm not really a fan of that, [R_Petname]."   
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 3)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)            
    $ R_Blow += 1
    jump R_Swallowed     
    #end Rogue in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_Creampie_P:
        if Trigger == "sex" and Situation == "auto":
                $ P_Cock = "in"
                $ R_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if ApprovalCheck("Rogue", 1300) or R_CreamP:              
                        call RogueFace("surprised")
                        "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."  
                        call RogueFace("sexy")
                        if R_Lust >= 85: 
                            call R_Cumming
                else:
                    if R_Lust >= 85: 
                            "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                            call R_Cumming                
                    else:
                            "You come in her pussy. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call RogueFace("angry")
                    ch_r "Hey, a little warning next time, huh?"
                    call RogueFace("bemused")
                    ch_r "Still, that didn't feel {i}so{/i} bad. . ."
                    
                jump R_Creampied
        
        #else (You ask her if it's ok):
        if ApprovalCheck("Rogue", 1200) or R_CreamP:        
                call RogueFace("sexy")
                if R_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif R_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "in"
                $ R_Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if R_Lust >= 85: 
                    call R_Cumming  
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1) 
                ch_r "Hmm, you know how to fill me up {i}right.{/i}"
                jump R_Creampied
        else:
                call RogueFace("sexy")
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2) 
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2) 
                ch_r "Thanks for the heads up *grunt* [R_Petname], but I'd rather you didn't."
        jump R_SpunkBack

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_Creampie_A:                             
        # These need conditionals added    
        if Trigger == "anal" and Situation == "auto":
                $ P_Cock = "anal"
                $ R_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if ApprovalCheck("Rogue", 1200) or R_CreamP:              
                    call RogueFace("surprised", 1)
                    "You come in her ass. Her eyes widen in surprise, but she takes it in stride."  
                    call RogueFace("sexy")
                    if R_Lust >= 85: 
                        call R_Cumming
                else:
                    if R_Lust >= 85: 
                        "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                        call R_Cumming                
                    else:
                        "You come in her ass. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call RogueFace("angry")
                    ch_r "Hey, warn a girl, huh?"
                    call RogueFace("bemused")
                    ch_r "but. . . I guess it did feel pretty good. . ."
                jump R_Creampied
            
        #else (You ask her if it's ok):
        if ApprovalCheck("Rogue", 1200) or R_CreamP:        
                call RogueFace("sexy")
                if R_CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif R_CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "anal"
                $ R_Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if R_Lust >= 85: 
                    call R_Cumming  
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1) 
                ch_r "Hmm, I feel so full. . ."
                jump R_Creampied
        else:
                call RogueFace("sexy")     
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2) 
                ch_r "Thanks for the heads up *grunt* [R_Petname], but I'd rather you didn't."
        jump R_SpunkBack
            
#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label R_Facial: 
    if renpy.showing("Rogue_BJ_Animation"):       
            if R_Addict >= 60 and ApprovalCheck("Rogue", 1000, "I", Bonus = ((R_Addict*10)- R_Obed)) and R_Swallow:
                    $ R_Eyes = "manic"
                    $ R_Blush = 1
                    $ Speed = 0
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    $ Speed = 4
                    $ R_Spunk.append("mouth")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ R_Mouth = "lipbite"
                    $ Speed = 0
                    "When she finishes, she licks her lips."
                    call RogueFace("bemused")
                    $ R_Spunk.remove("mouth")
                    ch_r "Sorry, [R_Petname], I just couldn't let that go to waste."
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 10)
                    jump R_Swallowed
            call Rogue_HJ_Launch("cum")
            $ Speed = 2
            $ R_Spunk.append("facial")
            "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
            $ Speed = 0
    
    elif renpy.showing("Rogue_TJ_Animation"):   
            $ R_Spunk.append("facial")
            if not R_Tit:                       
                "She glances up but continues to rub her breasts up and down on your cock. When you come, you spray all over her face."
            else:
                "As you're about to finish, you aim squarely at her face, and spray all over it."  
            $ Speed = 0
            
    elif renpy.showing("Rogue_HJ_Animation"):       
            $ R_Spunk.append("facial")
            if not R_Hand:                       
                "She looks a bit confused but continues to stroke while staring at it like a live snake. When you finish, you spray all over her face."
            else:
                "As you're about to finish, you aim squarely at her face, and spray all over it."  
            $ Speed = 0
    else:        
            call Rogue_HJ_Launch("cum")
            $ Speed = 2
            $ R_Spunk.append("facial")
            "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
            $ Speed = 0
    
            if Situation == "warn":
                ch_r "Thanks for the warning, [R_Petname]. Such a mess though. . ."  
            else:
                ch_r "What a mess, you could have warned me." 
                
    jump R_Orgasm_After


# Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_SpunkBack: 
    call Rogue_Doggy_Launch("hotdog")
    $ Speed = 0
    if R_Addict >= 60 and ApprovalCheck("Rogue", 1000, "I", Bonus = ((R_Addict*10)- R_Obed))  and R_Swallow:
            $ R_Eyes = "manic"
            $ R_Blush = 1
            call Rogue_BJ_Launch("cum")
            if Trigger == "sex":
                "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            elif Trigger == "anal":                
                "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            $ R_Mouth = "lipbite"
            $ R_Spunk.append("mouth")
            "When she finishes, she licks her lips."
            call RogueFace("bemused")
            $ R_Spunk.remove("mouth")
            ch_r "Sorry, [R_Petname], I just couldn't let that go to waste."
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 10)
            jump R_Swallowed
    $ P_Cock = "out"
    $ P_Spunk = "out"
    $ R_Spunk.append("back")
    if Trigger == "sex":
            "You pull out of her pussy with a pop and spray all over her backside."
    elif Trigger == "anal":
            "You pull out of her ass with a pop and spray all over her backside."
    else:
            "You pick up the pace and with a grunt you spray all over her backside."
        
                  
    if R_Addict >= 60 and ApprovalCheck("Rogue", 800, "I", Bonus = ((R_Addict*10)- R_Obed)) and R_Swallow: 
            #if she's manic and has swallowed
            $ R_Eyes = "manic"
            $ R_Blush = 1        
            "Rogue's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
            call RogueFace("manic", 1)
            $ R_Spunk.append("mouth")
            $ R_Mouth = "smile"
            ch_r "Well, [R_Petname], I just couldn't let that go to waste."
            $ R_Spunk.remove("mouth")
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
            jump R_Swallowed
          
        
    #else . . .
    call RogueFace("sexy", 1)
    ch_r "Thanks for the courtesy, [R_Petname]. Such a mess though. . ." 
    call Rogue_Doggy_Reset
    jump R_Orgasm_After
    
   
#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_Handy_Finish:
    if renpy.showing("Rogue_Doggy"):
        call Rogue_Doggy_Reset
    call Rogue_HJ_Launch("cum")
    $ Speed = 2        
    $ R_Spunk.append("hand")  
    if renpy.showing("Rogue_HJ_Animation"):                                  
            "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands." 
    else:
            "She grins and starts jerking you off, placing her left hand over your tip. You burst all over her hands." 
    $ Speed = 0
    
    if R_Addict > 80 or "hungry" in R_Traits:
            $ R_Eyes = "manic"
            $ R_Spunk.remove("hand")
            $ R_Spunk.append("mouth")
            $ R_Mouth = "smile"
            "She licks her hands off with a satisfied grin."
            $ R_Spunk.remove("mouth")
            ch_r "Hmmm. . ."
    else:
            call RogueFace("bemused")
            $ R_Spunk.remove("hand")
            "She wipes her hands off, but takes a quick sniff when she's done and smiles."
            ch_r "Thanks for the head's up."     
            jump R_Orgasm_After


#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_Swallowed: 
        $ R_Swallow += 1
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
        $ R_Addict -= 20    
        if "mouth" in R_Spunk:
                $ R_Spunk.remove("mouth")
        if "full" not in R_RecentActions and Action_Check("Rogue", "recent", "swallowed") >= 5: 
                $ R_RecentActions.append("full")    
                call RogueFace("surprised", 1)
                ch_r "-buurp-"
                call RogueFace("sexy", 1)
                ch_r "S'cuse me [R_Petname], must have been something I ate."
        $ R_RecentActions.append("swallowed")                      
        $ R_DailyActions.append("swallowed") 
        $ R_Addictionrate += 2
        if "addictive" in P_Traits:
                $ R_Addictionrate += 2
        if Trigger == "anal":    
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 2)
        if R_Swallow == 1:
                $R_SEXP += 12
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 5)
        jump R_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_Creampied:
    if Trigger == "sex":
            $ R_CreamP += 1
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 10)
            $ R_RecentActions.append("creampie sex")                      
            $ R_DailyActions.append("creampie sex") 
    elif Trigger == "anal":
            $ R_CreamA += 1
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)
            $ R_RecentActions.append("creampie anal")                      
            $ R_DailyActions.append("creampie anal") 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
    $ R_Addict -= 30
    $ R_Addictionrate += 2
    if "addictive" in P_Traits:
            $ R_Addictionrate += 3
    if R_CreamP == 1:
            $R_SEXP += 10
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 5)
    call Rogue_Doggy_Reset

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label R_Orgasm_After:
    $ Line = 0
    $ Rogue_Arms = 1
    $ P_Semen -= 1
    $ P_Focus = 0
    $ P_Cock = "out"
    $ P_Spunk = 0
    $ Speed = 0    
    if Trigger == "anal" and not ApprovalCheck("Rogue", 1600, TabM=1) and not R_Addict >= 80:
            "She wipes your cock clean."
    elif R_Blow > 3 or R_Swallow: 
            if ApprovalCheck("Rogue", 1200, TabM=1) or R_Addict >= 60:
                    call Rogue_BJ_Launch("cum")
                    $ Speed = 1
                    call RogueFace("sucking", 1) 
                    if ApprovalCheck("Rogue", 1500, TabM=1):
                        if R_Love > R_Inbt and R_Love > R_Obed:
                            "She looks up at you lovingly as she licks your cock clean."            
                        elif R_Obed > R_Inbt:
                            $ R_Eyes = "side"
                            "She dutifully licks your cock clean with lowered eyes."
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)                
                        else:
                            "She happily licks your cock clean." 
                    elif R_Addict >= 60:
                            "She hungrily and thoroughly licks your cock clean."   
                    else:
                        "She licks you cock clean." 
                    call RogueFace("sexy") 
                    call Rogue_BJ_Reset            
            else:
                    if not renpy.showing("Rogue_HJ_Animation"):
                        call Rogue_HJ_Launch("cum") 
                    "She wipes your cock clean."  
    else:
                    if not renpy.showing("Rogue_HJ_Animation"):
                        call Rogue_HJ_Launch("cum") 
                    "She wipes your cock clean." 
    call RogueFace("sexy") 
    call Rogue_HJ_Reset 
    if R_Spunk and not ApprovalCheck("Rogue", 400, "I"):
                call Rogue_Cleanup
    elif R_Spunk:    
        menu:
            extend""
            "And maybe clean yourself up too?":            
                call Rogue_Cleanup
            "[[Say nothing.]":
                call Rogue_Cleanup
    $ Situation = 0
    return
    
# End You Cumming //////////////////////////////////////////////////////////////////////////////////


# Rogue Lusty face check ////////////////////////////////////////////////////////////////////////////////
label RogueLust(Extreme = 0):
    if R_Lust >= 40:        
            $ R_Blush = 1
        
    if R_Lust >= 80:
            $ R_Wet = 2 
    elif R_Lust >= 50:
            $ R_Wet = 1
    
    if Partner != "Rogue" and (Trigger == "kissing" or Trigger2 == "kissing" or Trigger5 == "kiss both" or Trigger5 == "kiss girl"):  
            #If Rogue is kissing and is primary
            $ R_Eyes = "closed"
            if R_Kissed >= 10 and R_Inbt >= 300:
                $ R_Mouth = "sucking"
            elif R_Kissed > 1 and R_Addict >= 50:            
                $ R_Mouth = "sucking"
            else:
                $ R_Mouth = "kiss"
                            
    elif Partner == "Rogue" and Trigger4 == "kissing":   
            #If Rogue is kissing in a threesome action
            $ R_Eyes = "closed"
            if R_Kissed >= 10 and R_Inbt >= 300:
                $ R_Mouth = "sucking"
            elif R_Kissed > 1 and R_Addict >= 50:            
                $ R_Mouth = "sucking"
            else:
                $ R_Mouth = "kiss"
            
    else:    
            #If Rogue is not kissing someone
            if R_Lust >= 90:
                    $ R_Eyes = "closed"
                    $ R_Brows = "sad"
                    $ R_Mouth = "surprised"
            elif R_Lust >= 70:
                    $ R_Eyes = "sexy"
                    $ R_Brows = "sad"
                    $ R_Mouth = "lipbite"
            elif R_Lust >= 50 and not Extreme:
                    $ R_Eyes = "sexy"
                    $ R_Brows = "sad"
                    $ R_Mouth = "lipbite"
            elif R_Lust >= 30 and not Extreme:
                    $ R_Eyes = "sexy"
                    $ R_Brows = "normal"
                    if renpy.showing("Rogue_Doggy"):
                            $ R_Mouth = "lipbite"
                    else:
                            $ R_Mouth = "kiss"
            elif not Extreme:
                    $ R_Eyes = "sexy"
                    $ R_Brows = "normal"
                    $ R_Mouth = "normal"    
    
    if Partner == "Rogue" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ R_Mouth = "tongue"   
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ R_Mouth = "tongue"  
                    
    if R_OCount >= 10:   
            #If you've fucked her senseless
            $ R_Eyes = "stunned"
            $ R_Mouth = "tongue"   
            
    if not R_Loose:     
            #if anal hurts. . .
            if Partner != "Rogue" and (Trigger == "anal" or Trigger == "dildo anal" or Trigger3 == "dildo anal"):  
                $ R_Eyes = "closed"
                $ R_Brows = "angry"
    
    return

# End faces

#  Rogue Orgasm //////////////////////////

label R_Cumming:
    $ R_Eyes = "surprised"
    $ R_Brows = "sad"
    $ R_Mouth = "sucking"
    $ R_Blush = 1
    ch_r ". . . !"
    $ Speed = 0
    if renpy.showing("Rogue_Doggy"):
            show Rogue_Doggy #fix, test this
            with vpunch
    elif renpy.showing("Rogue_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Rogue_BJ_Animation
            with vpunch
    elif renpy.showing("Rogue_TJ_Animation"):
            show Rogue_TJ_Animation  
            with vpunch
    elif renpy.showing("Rogue_HJ_Animation"):
            show Rogue_HJ_Animation  
            with vpunch
    else:
            show Rogue
            with vpunch
    $ Speed = 1
    $ Line = renpy.random.choice(["Rogue is suddenly rocked with spasms, holding back a muffled scream.", 
                "Rogue grabs on tightly as her body shakes with pleasure.", 
                "Rogue stiffens and lets out a low moan.",
                "Rogue's body quivers and suddenly goes still."])
    "[Line]"
    
    $ R_Eyes = "closed"
    $ R_Brows = "sad"
    $ R_Mouth = "tongue"
    $ Line = renpy.random.choice(["Wow. . .  just, wow.", 
                "Ah don't know what came over me. . .", 
                "Hmmmm. . . .",
                "That, felt good. Thatfeltrealgood."])
    ch_r "[Line]"
           
    
    $ R_Lust = 30 if "hotblooded" in R_Traits else 0 
    $ R_Lust += (R_OCount * 5)
    $ R_Lust = 80 if R_Lust >= 80 else R_Lust    
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)
            
    if "unsatisfied" in R_RecentActions:  #If she had been unsatisfied, you satisfied her. . .        
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            if "unsatisfied" in R_DailyActions:
                ch_r "I guess that makes up for earlier, [R_Petname]."
            call DrainWord("Rogue","unsatisfied")
    $ R_Org += 1
    $ Line = 0
      
    if Trigger != "masturbation":
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 40, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)            
    #Orgasm count
            if Trigger != "blow" and Trigger != "hand":
                $ R_OCount += 1        
                if R_OCount == 2:
                        $ R_Brows = "confused"
                        ch_r "Wow. . . that was amazing. . ."
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)            
                elif R_OCount == 3: #5
                        $ R_Brows = "confused"            
                        ch_r "You. . . can. . . really. . . keep. . . it. . . up. . . huh?"
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)                    
                elif R_OCount == 5: #10
                    $ R_Mouth = "tongue"    
                    ch_r "I'm . . .really. . . getting. . . worn. . . out . . ."
                    menu:
                        ch_r "could. . . we. . . cool. . . off?"
                        "Finish up." if P_FocusX:
                            "You release your concentration. . ."                 
                            $ P_FocusX = 0
                            $ P_Focus += 15                    
                        "Let's try something else." if MultiAction:  
                            $ Situation = "shift"
                        "No, I'm not done yet.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck("Rogue", 1000, TabM=1) or ApprovalCheck("Rogue", 400, "O", TabM=1):
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
                                    $ R_Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                                else:
                                    call RogueFace("angry", 1)
                                    "She scowls at you, pulls out with a pop, and wipes herself off."
                                    ch_r "Well if that's your attitude you can handle your own business."
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                            else:
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                $ R_Eyes = "stunned"
                                "She drifts off into incoherent moans."  
                #end Ocount stuff
    return
    
# End Rogue Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Rogue Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Rogue_Cleanup(Options = [], Cnt = 0, Line = "random", Cleaned = 0):
    if not R_Spunk:
        $ R_Wet = 0
        return     
        
    if R_Addict > 80 and R_Swallow:
        #if she likes cum, she prefers to eat it. 
        $ Line = "eat"            
        $ R_Eyes = "manic"
        $ R_Mouth = "smile" 
    elif "painted" in R_RecentActions and ApprovalCheck("Rogue", 1000, "OI"):
        return
    elif ApprovalCheck("Rogue", 1200, "LO"):  
        $ Line = "ask"            
    elif not ApprovalCheck("Rogue", 400, "I"):
        call RogueFace("bemused") 
        $ Line = "clean"   
    else:
        $ Line = "ask"      
   
    $ Cleaned = 1 if "cleaned" in R_DailyActions else 0
    $ R_RecentActions.append("cleaned") 
    $ R_DailyActions.append("cleaned") 
    
    if Line == "ask":
            $ Line = "random"
            "She looks down at the spunk covering her."
            menu:
                "What do you suggest Rogue do about cleaning up?"
                "You should leave it where it is.":
                        if ApprovalCheck("Rogue", 900, "I") or "exhibitionist" in R_Traits:
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5) 
                                $ Line = "leave"  
                                call RogueFace("sly") 
                                ch_r "Ooh, I like where your head is at. . "
                        elif ApprovalCheck("Rogue", 600, "I") and ApprovalCheck("Rogue", 1200, "LO"):
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5) 
                                $ Line = "leave"  
                                call RogueFace("surprised",2) 
                                ch_r "Well, I guess I could. . ."
                                call RogueFace("sly",1) 
                        
                        else:
                            call RogueFace("angry") 
                            menu:
                                ch_r "Now you're just being ridiculous!" 
                                "Please?":
                                    if ApprovalCheck("Rogue", 1800):
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 3) 
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                                        ch_r "Oh, fine!"
                                        $ Line = "leave"  
                                    elif Cleaned:
                                        call RogueFace("angry") 
                                        ch_r "Seriously, stop bugging me about this."
                                    elif ApprovalCheck("Rogue", 800):
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1) 
                                        ch_r "You're persistant, but no way."
                                    else:
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 75, -5)
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 40, -10)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                                        call RogueFace("angry") 
                                        ch_r "Don't be an asshole."
                                "I insist.":
                                    call RogueFace("sad") 
                                    if ApprovalCheck("Rogue", 400, "I") and ApprovalCheck("Rogue", 1200, "LO"):
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 3)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                                        ch_r "Alright, fine."
                                        $ Line = "leave"  
                                    elif ApprovalCheck("Rogue", 800, "O"):
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10)
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 5)
                                        ch_r "If you have to insist."
                                        $ Line = "leave"  
                                    elif Cleaned:
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -5)
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -1)
                                        call RogueFace("angry") 
                                        ch_r "Seriously, stop bugging me about this."
                                    elif ApprovalCheck("Rogue", 800):
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3)
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -1)
                                        call RogueFace("sad") 
                                        ch_r "Sorry, that's just a bridge too far." 
                                    else:
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10)
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                        call RogueFace("angry") 
                                        ch_r "Well {i}I{/i} insist you don't know how to talk to a lady!"
                                        
                                "Never mind then.":
                                    ch_r "Alright then. . ."                            
                        #end "leave it"
                        
                "You should just eat it.":
                        call RogueFace("sly") 
                        if "hungry" in R_Traits or (R_Swallow >= 5 and ApprovalCheck("Rogue", 800)): 
                                #lots of swallows
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5) 
                                $ Line = "eat"   
                                ch_r "I am a bit peckish. . ."
                        elif R_Swallow and ApprovalCheck("Rogue", 800): 
                                #few swallows
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5) 
                                $ Line = "eat"   
                                ch_r "I guess it wasn't so bad last time. . ."
                        elif ApprovalCheck("Rogue", 1200): 
                                #no swallows, but likes you
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                                $ Line = "eat"   
                                ch_r "I suppose I could give it a go. . ."
                        elif ApprovalCheck("Rogue", 400): 
                                #Likes you well enough, but won't
                                call RogueFace("sad") 
                                ch_r "Sorry, I just don't think I could."
                        else: 
                                #doesn't like you.
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -5)
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -3)
                                call RogueFace("angry") 
                                ch_r "No."
                        #end eat it
                              
                "You should just clean it up.":
                        if ApprovalCheck("Rogue", 600, "I") and not ApprovalCheck("Rogue", 1500, "LO"): #rebellious
                                call RogueFace("sly") 
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 10) 
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 5) 
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5) 
                                ch_r "I don't know, [R_Petname], I kind of like it where it is. . ."
                                $ Line = "leave"   
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                        call RogueFace("smile") 
                                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 5)
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                    "No, clean it up.": 
                                        if ApprovalCheck("Rogue", 600, "O"):
                                            call RogueFace("sad") 
                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                                            ch_r "If that's what you really want. . ."
                                            $ Line = "clean"  
                                        elif ApprovalCheck("Rogue", 1200, "LO"):
                                            call RogueFace("sad") 
                                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3)
                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                            ch_r "You take the fun out of this. . ."
                                            $ Line = "clean"   
                                        else:
                                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5)
                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -5)
                                            ch_r "I {i}said{/i} it's stay'in."
                                                                                    
                        else: #agrees
                                call RogueFace("bemused") 
                                $ Line = "clean"   
                                ch_r "Ok, I guess. . ."
                        #end clean it up
                        
                "Say nothing. [[leave it to her]":
                    $ Line = "random"
            #end "asked"
                
                
    if Line == "random":
            $ Options = ["clean"]
            if R_Swallow and ApprovalCheck("Rogue", 800):
                $ Options.append("eat") 
                if R_Swallow >=5:                            
                    $ Options.append("eat") 
                if "hungry" in R_Traits:                
                    $ Options.append("eat") 
            if ApprovalCheck("Rogue", 600, "I"):
                $ Options.append("leave") 
                if ApprovalCheck("Rogue", 800, "I"):
                    $ Options.append("leave") 
                if "exhibitionist" in R_Traits:
                    $ Options.append("leave") 
                    
            $ renpy.random.shuffle(Options)
            
            $ Line = Options[0]
            #end "random"
            
            
    if Line == "leave":
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 1) 
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in R_Spunk: 
                    $ R_Spunk.remove("hand")
                    if R_Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."   
            if "mouth" in R_Spunk:                  
                    $ R_Spunk.remove("mouth")
            $ R_RecentActions.append("painted")  #means she left the jiz on                   
            $ R_DailyActions.append("painted")                         
            return
            #end "leave it"

    $ Cnt = 0
    $ R_Spunk.append("hand")
    if "mouth" in R_Spunk and Line != "eat":
            $ R_Spunk.remove("mouth")
            "She spits out the spunk in her mouth and dribbling down her chin,"
            $ Cnt += 1
    if "hair" in R_Spunk:
            $ R_Spunk.remove("hair")
            if Cnt:            
                "then she wipes the spunk out of her hair,"
            else:
                "She wipes the spunk out of her hair,"
            $ Cnt += 1
    if "facial" in R_Spunk:
            $ R_Spunk.remove("facial")
            if Cnt:
                "then she wipes the spunk off of her face,"   
            else:
                "She wipes the spunk off of her face,"   
            $ Cnt += 1         
    if "tits" in R_Spunk:
            $ R_Spunk.remove("tits")
            if Cnt:
                "then she wipes the spunk off of her chest,"   
            else:
                "She wipes the spunk off of her chest," 
            $ Cnt += 1           
    if "back" in R_Spunk:
            $ R_Spunk.remove("back")
            if Cnt:
                "then she wipes the spunk off of her back,"   
            else:
                "She wipes the spunk off her lower back," 
            $ Cnt += 1     
    if "in" in R_Spunk:
            $ R_Spunk.remove("in")
            if Cnt:
                "then she wipes the spunk inside her pussy,"   
            else:
                "She wipes the spunk inside her pussy,"     
            $ Cnt += 1 
    if "anal" in R_Spunk and (ApprovalCheck("Rogue", 800, "I") or Line != "eat"):
            while "anal" in R_Spunk:
                $ R_Spunk.remove("anal")
            if Cnt:
                "then she wipes the spunk dripping out of her ass,"   
            else:
                "She wipes the spunk dripping our of her ass,"
            $ Cnt += 1            
    if "hand" in R_Spunk:
            $ R_Spunk.remove("hand")
            if Line == "eat":                    
                $ R_Spunk.append("mouth")
                if Cnt and "anal" in R_Spunk:
                    "then licks her hands off with a satisfied grin," 
                if Cnt:
                    "and finally she licks her hands off with a satisfied grin." 
                else:
                    "She licks her hands off with a satisfied grin."   
                    
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2) 
                $ R_Spunk.remove("mouth")
                $ R_Swallow += 1     
                $ R_Addict -= (10*Cnt)
                if R_Swallow == 1:
                    $ R_SEXP += 12
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 5)
                $ R_RecentActions.append("swallowed")                     
                $ R_DailyActions.append("swallowed") 
            else:
                if Cnt:
                    "and finally, she wipes her hands off with a nearby tissue." 
                else:
                    "She wipes her hands off with a nearby tissue."                    
            $ Cnt += 1
    if "anal" in R_Spunk:
            $ R_Spunk.remove("anal")
            if Cnt:
                "Afterward, she wipes the spunk dripping our of her ass."
            else:
                "She wipes the spunk dripping out of her ass."
    $ R_Wet = 0        
    $ del R_Spunk[:]   
    if Cnt >= 5:
            $ R_Eyes = "surprised"
            ch_r "Wow, you really painted me white!"
            $ R_Eyes = "sexy"
    elif Cnt >=3:
            ch_r "That was a real mess you left me to clean up."
    elif Line == "eat" and R_Swallow >= 5:
            ch_r "That was delcious."
    return    
    
# End Rogue Clean-Up /////////////////////////////////////////////////////////////////////////////////////

