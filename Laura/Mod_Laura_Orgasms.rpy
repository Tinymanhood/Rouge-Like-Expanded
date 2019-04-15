# Start You Cumming //////////////////////////////////////////////////////////////////////////////////

label PLaura_Cumming:
    call Shift_Focus("Laura")
            
    if Trigger == "blow":
            $ Tempmod += 5
        
    if newgirl["Laura"].Addict > 75:
            $ Tempmod += 20
    elif newgirl["Laura"].Addict > 50:
            $ Tempmod += 5
    
    if newgirl["Laura"].Swallow >= 10:
            $ Tempmod += 15  
    elif newgirl["Laura"].Swallow >= 3:
            $ Tempmod += 5
        
    if (newgirl["Laura"].CreamP + newgirl["Laura"].CreamA) >= 10:
            $ Tempmod += 15 
    elif (newgirl["Laura"].CreamP + newgirl["Laura"].CreamA) >= 3:
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
    
    call LauraFace("sexy") 
    
    menu:
        "[Line]"
        "Warn her":
                $ Situation = "warn"
#                jump Laura_No_Cum           #fix, temporary
                jump Laura_Warn_Her
            
        "Ask to cum in her mouth": 
                $ Situation = "asked"
#                jump Laura_No_Cum           #fix, temporary
                jump Laura_In_Mouth                            
        "Cum in her mouth without asking" if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                $ Situation = "auto"
#                jump Laura_No_Cum           #fix, temporary
                jump Laura_In_Mouth
        
        "Ask to cum inside her" if Trigger == "sex":
                $ Situation = "asked"
                jump Laura_Creampie_P        
        "Ask to cum inside her" if Trigger == "anal":
                $ Situation = "asked"
                jump Laura_Creampie_A
                
        "Cum inside her" if Trigger == "sex":
                $ Situation = "auto"
                jump Laura_Creampie_P        
        "Cum inside her" if Trigger == "anal":
                $ Situation = "auto"
                jump Laura_Creampie_A
            
        "Cum on her face":
#                jump Laura_No_Cum           #fix, temporary
                jump Laura_Facial   
                
        "Cum on her tits":
                jump Laura_No_Cum           #fix, temporary
                jump Laura_TitSpunk   
                
        "Cum on her belly" if Trigger == "sex" or Trigger == "anal" or Trigger == "hotdog":
                jump Laura_SpunkBelly
            
        "Pull back":
            if LauraBJShowing:
                    if newgirl["Laura"].Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed)) and newgirl["Laura"].Swallow:
                            $ newgirl["Laura"].Eyes = "manic"
                            $ Speed = 0
                            if LauraBJShowing:
                                call Laura_BJ_Launch_(Speed = Speed)
                            "You pull out of her mouth with a pop, and her eyes widen in surprise."
                            $ newgirl["Laura"].Mouth = "sucking"
                            $ newgirl["Laura"].Spunk.append("mouth")
                            $ newgirl["Laura"].Spunk.append("chin")
                            $ Speed = 4
                            if LauraBJShowing:
                                call Laura_BJ_Launch_(Speed = Speed)
                            "She leaps at your cock and sucks it deep, draining your fluids hungrily." 
                            $ Speed = 0
                            if LauraBJShowing:
                                call Laura_BJ_Launch_(Speed = Speed)
                            $ newgirl["Laura"].Mouth = "lipbite"
                            "When she finishes, she draws her hand across her lips."
                            call LauraFace("bemused")
                            ch_l "Sorry, [newgirl[Laura].Petname], but I couldn't let that go to waste."
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, -5)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)
                            jump Laura_Swallowed                            
                    call Laura_BJ_Reset                
            elif renpy.showing("Laura_HJ_Animation"):
                    call Laura_HJ_Reset                
            elif renpy.showing("Laura_TJ_Animation"):
                    call Laura_TJ_Reset               
            elif renpy.showing("Laura_SexSprite"):
                    call Laura_Sex_Reset  
            if ApprovalCheck("Laura", 500, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed)) and newgirl["Laura"].Addict > 50 and newgirl["Laura"].Swallow: #If addict + Inbt is > obedience + 50. . .
                    $ newgirl["Laura"].Eyes = "manic"
                    $ newgirl["Laura"].Mouth = "kiss"
                    $ Speed = 0
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "Her eyes widen in panic."
                    ch_l "You wouldn't reconsider, [newgirl[Laura].Petname]?" 
                    $ newgirl["Laura"].Blush = 2
                    menu:
                        extend ""
                        "Ok, if you'll swallow it.":
                                if Trigger != "blow": 
                                    call Laura_BJ_Launch_("cum")
                                call LauraFace("sucking") 
                                $ Speed = 4
                                if LauraBJShowing:
                                    call Laura_BJ_Launch_(Speed = Speed)
                                "She nods and puts the tip into her mouth. as you release she gulps it down hungrily."
                                call LauraFace("sexy")                      
                                $ newgirl["Laura"].Mouth = "sucking"
                                $ newgirl["Laura"].Spunk.append("mouth")
                                $ newgirl["Laura"].Spunk.append("chin")
                                ". . ."
                                $ Speed = 0
                                if LauraBJShowing:
                                            call Laura_BJ_Launch_(Speed = Speed)
                                call LauraFace("sad")                       
                                $ newgirl["Laura"].Mouth = "lipbite"
                                ch_l "Yum."  
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                jump Laura_Swallowed                                
                        "No, we're done for now.": #If addict is > obedience + 50. . .
                                if ApprovalCheck("Laura", 250, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed)) or newgirl["Laura"].Addict > 75:                            
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -2)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3)
                                        if Trigger != "blow":
                                            call Laura_BJ_Launch_("cum")
                                            $ Speed = 4
                                            if LauraBJShowing:
                                                call Laura_BJ_Launch_(Speed = Speed)
                                        "She dives down on you and you can't resist filling her throat."
                                        $ Speed = 0
                                        if LauraBJShowing:
                                            call Laura_BJ_Launch_(Speed = Speed)
                                        ch_l "Now we are."
                                        jump Laura_Swallowed                                
                                else:                         
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5)
                                        call LauraFace("sad")
                                        $ newgirl["Laura"].Brows = "confused"
                                        ch_l "Dick."
                                        $ Line = 0
                                        $ P_Focus -= 5
                                        return  
                    #manic, wanted to swallow
                    
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
            "You pull pull back away from her. She looks up at you and licks her lips." 
            ch_l "So now what?"
            $ Line = 0
            $ P_Focus = 95
            return
            #end "pull back"
#End Main orgasm menu

label Laura_No_Cum:
        #this is a temporary thing until this system is complete
        call LauraFace("confused", Mouth="smirk") 
        if Situation == "warn":
            ch_p "I'm about to. . . blow. . ."
            ch_l "Oh? Cool."
        elif Situation == "asked":        
            ch_p "I'm about to. . . blow. . ."
            ch_p "Could I. . . come in your mouth?"
            ch_l "Hmmm, I don't think so."
        else:
            ch_l "Not so fast, [newgirl[Laura].Petname]."         
        if not renpy.showing("Laura_HJ_Animation"):
            $ newgirl["Laura"].Girl_Arms = 2
        call LauraFace("sly",1) 
        ch_l "For now just come in my hand here. . ."
        $ newgirl["Laura"].Spunk.append("hand") 
        "She grabs the head of your cock and you gush into it."
        ch_l "Bit of a mess. . ."         
        jump Laura_Orgasm_After


label Laura_Warn_Her:            
        "You let her know that you're going to come."
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5) if newgirl["Laura"].Obed >= 500 else newgirl["Laura"].Obed   
        if "hungry" in newgirl["Laura"].Traits and D20 >= 5:
                if renpy.showing("Laura_SexSprite"):
                    call Laura_BJ_Launch_("cum")   
                    "She grins and pulls out with a pop, and begins to suck you off."
                $ Speed = 4
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                call LauraFace("sucking")       
                ". . ."
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                $ newgirl["Laura"].Spunk.append("mouth")
                $ newgirl["Laura"].Spunk.append("chin")
                if not LauraBJShowing:
                    "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:                    
                    "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."        
                call LauraFace("sexy")
                $ newgirl["Laura"].Mouth = "smile"
                ch_l "Yum, thanks for the heads up."     
                jump Laura_Swallowed
        #End Hungy take-over
            
        if Trigger == "sex" and newgirl["Laura"].CreamP >= 5: 
                # She's Creampied a few times
                call LauraFace("sexy")
                $ P_Cock = "in"
                $ newgirl["Laura"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She smiles and speeds up her actions, causing you to erupt inside her."   
                if newgirl["Laura"].Lust >= 85: 
                    call Laura_Cumming  
                jump Laura_Creampied
        
        elif Trigger == "sex" and newgirl["Laura"].CreamP and D20 >= 10:  
                # She's Creampied at least once
                call LauraFace("sly")
                $ P_Cock = "in"
                $ newgirl["Laura"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She gets a michevious look and speeds up, you burst inside her."          
                if newgirl["Laura"].Lust >= 85: 
                    call Laura_Cumming  
                jump Laura_Creampied
            
        elif Trigger == "anal" and newgirl["Laura"].CreamA >= 5: 
                # She's Anal Creampied a few times
                call LauraFace("sexy")
                $ P_Cock = "anal"
                $ newgirl["Laura"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She smiles and speeds up her actions, causing you to erupt inside her."         
                if newgirl["Laura"].Lust >= 85: 
                    call Laura_Cumming  
                jump Laura_Creampied
        
        elif Trigger == "anal" and newgirl["Laura"].CreamA and D20 >= 10: 
                # She's Anal Creampied at least once
                call LauraFace("sly")
                $ P_Cock = "anal"
                $ newgirl["Laura"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She gets a michevious look and speeds up, you burst inside her."    
                if newgirl["Laura"].Lust >= 85: 
                    call Laura_Cumming          
                jump Laura_Creampied
            
        elif Trigger != "anal" and newgirl["Laura"].Swallow >= 5: 
                #If she's swallowed a lot     
                if renpy.showing("Laura_TJ_Animation"):  
                        if newgirl["Laura"].Blow >= 5 or Speed >= 3:          
                                call LauraFace("tongue")
                                $ Speed = 5 #shallow animation
                                if LauraBJShowing:
                                    call Laura_BJ_Launch_(Speed = Speed)
                                $ newgirl["Laura"].Spunk.append("mouth")
                                $ newgirl["Laura"].Spunk.append("chin")
                                "She makes a little humming sound, but keeps sucking."
                        else: 
                                jump Laura_Facial
                elif LauraBJShowing:            
                        call LauraFace("sucking")
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "She makes a little humming sound, but keeps sucking."
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
                else:
                        call Laura_BJ_Launch_("cum")
                        $ Speed = 2
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        call LauraFace("sucking")
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        "She smiles and then puts your tip in her mouth."
                        $ Speed = 5
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."                
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                call LauraFace("sexy")
                $ newgirl["Laura"].Mouth = "smile"
                ch_l "Yum, thanks for the heads up."  
                jump Laura_Swallowed
            
        elif newgirl["Laura"].Swallow and D20 >= 10:  
                #She's swallowed before, but not a lot  
                if renpy.showing("Laura_SexSprite"):
                    call Laura_HJ_Launch("cum") 
                    "She grins and pulls out with a pop, and begins to stroke you off."
                $ Speed = 2
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                if renpy.showing("Laura_TJ_Animation") or LauraBJShowing: 
                    if renpy.showing("Laura_TJ_Animation"): 
                        if newgirl["Laura"].Blow >= 5 or Speed >= 3:          
                                call LauraFace("tongue")
                                $ Speed = 5 #shallow animation
                                if LauraBJShowing:
                                    call Laura_BJ_Launch_(Speed = Speed)
                                $ newgirl["Laura"].Spunk.append("mouth")
                                $ newgirl["Laura"].Spunk.append("chin")
                        else: 
                                jump Laura_Facial
                    elif LauraBJShowing: 
                            #if she's blowing
                            call LauraFace("sucking")
                            $ newgirl["Laura"].Spunk.append("mouth")
                            $ newgirl["Laura"].Spunk.append("chin")
                    $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "She makes a little humming sound, but keeps sucking."
                    "When you finish filling her mouth, she gags a little, but manages to swallow it."
                    $ Speed = 0
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    call LauraFace("sexy")
                    $ newgirl["Laura"].Mouth = "smile"
                    if newgirl["Laura"].Addict > 50:
                            $ newgirl["Laura"].Eyes = "manic"
                            "She gulps it down hungrily and licks her lips."
                    call LauraFace("bemused")
                    ch_l "Hmm. . . an intense taste, thanks for the heads up."
                    jump Laura_Swallowed                    
                    #fix, add titjob option here.   
                else:
                        #If she's handying
                        jump Laura_Handy_Finish    
        #end if she's swallowed        
            
        elif ApprovalCheck("Laura", 1000):                    
                #warned but likes you and experienced
                if newgirl["Laura"].SEXP > 20 and renpy.showing("Laura_SexSprite"):
                        "She gently pushes you back off of her."
                        jump Laura_SpunkBelly
                elif newgirl["Laura"].SEXP > 20:
                        jump Laura_Facial            
        
                if renpy.showing("Laura_HJ_Animation") and newgirl["Laura"].Hand:
                        jump Laura_Handy_Finish
                elif LauraBJShowing and newgirl["Laura"].Blow:
                        jump Laura_Handy_Finish
                elif renpy.showing("Laura_TJ_Animation") and newgirl["Laura"].Tit:
                        jump Laura_TitSpunk
                elif renpy.showing("Laura_SexSprite") and newgirl["Laura"].Sex and Trigger == "sex":
                        "She gently pushes you back off of her."
                        jump Laura_SpunkBelly
                elif renpy.showing("Laura_SexSprite") and newgirl["Laura"].Anal and Trigger == "anal":
                        "She gently pushes you back off of her."
                        jump Laura_SpunkBelly
                
        # Else. . . not experienced or she's not a huge fan, 
        if Trigger == "sex" or Trigger == "anal":
                call Laura_Sex_Reset
                "She pulls off of you and grabs your cock in her hand."
                jump Laura_Handy_Finish
        elif renpy.showing("Laura_TJ_Animation"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump Laura_TitSpunk
        elif renpy.showing("Laura_SexSprite"):#hotdogging
                "She smiles and starts rubbing against you a bit faster."
                jump Laura_SpunkBelly
        else:
                jump Laura_Handy_Finish
    #End "Warn her" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
                      
                      
#Cum in mouth start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_In_Mouth:      
            
    if Trigger == "anal":
            $ Tempmod -= 15
    if "hungry" not in newgirl["Laura"].Traits and newgirl["Laura"].Addict <= 50 and "full" in newgirl["Laura"].RecentActions:
            $ Tempmod -= 15                  
                
    if Situation == "auto":
                $ Situation = 0
                if renpy.showing("Laura_TJ_Animation"):         
                        call LauraFace("tongue")
                elif not LauraBJShowing:
                        call Laura_BJ_Launch_("cum")
                $ newgirl["Laura"].Eyes = "down"
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                if LauraBJShowing:
                    call Laura_BJ_Launch_(Speed = Speed)
                "You grab her head and cum in her mouth"  
                $ newgirl["Laura"].Eyes = "closed"      
                if renpy.showing("Laura_TJ_Animation"): 
                        show Laura_TJ_Animation
                        with vpunch
                else:
                        #show Laura_BJ_Animation
                        $ renpy.show("Laura_BJ_Body_" + str(Speed))
                        with vpunch
                if "full" in newgirl["Laura"].RecentActions:
                        #if she's had enough
                        call LauraFace("bemused")
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "She gags a little, but manages to swallow it."
                        $ newgirl["Laura"].Spunk.remove("mouth")
                        ch_l "Hmm. . . I'm kinda full. . ."
                        ch_l "Maybe keep it outside. . ."
                elif newgirl["Laura"].Swallow >= 5 or "hungry" in newgirl["Laura"].Traits:
                        #if she likes to swallow
                        call LauraFace("sexy")
                        $ newgirl["Laura"].Mouth = "smile"
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        "She quickly gulps it down and wipes her mouth."
                        $ newgirl["Laura"].Spunk.remove("mouth")
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        ch_l "Yum."
                        call LauraFace
                elif newgirl["Laura"].Swallow:
                        call LauraFace("bemused")
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "She gags a little, but manages to swallow it."
                        $ newgirl["Laura"].Spunk.remove("mouth")
                        ch_l "Your. . . flavor is. . . distinct, but maybe a heads up?"
                        call LauraFace
                elif not newgirl["Laura"].Swallow and newgirl["Laura"].Addict >= 50 and newgirl["Laura"].Inbt < 400 and newgirl["Laura"].Blow < 10:
                        call LauraFace("bemused", 1)
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        ". . ."            
                        $ newgirl["Laura"].Spunk.remove("mouth")
                        $ newgirl["Laura"].Spunk.append("hand")
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
                        $ newgirl["Laura"].Spunk.remove("hand")
                        ch_l "That certainly is. . . intense. . ."
                        $ newgirl["Laura"].Addictionrate += 1
                        if "addictive" in P_Traits:
                            $ newgirl["Laura"].Addictionrate += 1
                        call LauraFace
                        jump Laura_Orgasm_After
                elif not newgirl["Laura"].Swallow and newgirl["Laura"].Addict >= 50:
                        call LauraFace("sexy")
                        $ newgirl["Laura"].Mouth = "tongue"
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        ". . ."
                        $ newgirl["Laura"].Spunk.remove("mouth")
                        $ newgirl["Laura"].Spunk.append("hand")
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
                        $ newgirl["Laura"].Spunk.remove("hand")
                        ch_l "I should be mad, but. . ."
                        call LauraFace
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                elif not newgirl["Laura"].Swallow:
                        if ApprovalCheck("Laura", 800, "LI") and ApprovalCheck("Laura", 400, "OI"):
                            call LauraFace("angry")
                        else:
                            call LauraFace("bemused")
                            $ newgirl["Laura"].Mouth = "tongue"
                        $ newgirl["Laura"].Spunk.append("mouth")
                        $ newgirl["Laura"].Spunk.append("chin")
                        ". . ."
                        $ newgirl["Laura"].Spunk.append("hand")
                        $ Speed = 0
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        "She gags and spits it into her palm."   
                        menu:
                            ch_l "What's the deal just cumming in my mouth like that?"
                            "Sorry about that.":
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                                    $ newgirl["Laura"].Addictionrate += 1
                                    if "addictive" in P_Traits:
                                        $ newgirl["Laura"].Addictionrate += 1
                                    call LauraFace("smile", 1)
                                    ch_l "Fine. . ."
                                    ch_l "Just warn me next time. . ."
                                    jump Laura_Orgasm_After
                                
                            "Why don't you try swallowing it?":
                                    if ApprovalCheck("Laura", 1200):
                                        "She tentatively licks her hand, and then gulps it down."
                                        $ newgirl["Laura"].Spunk.remove("hand")
                                        call LauraFace("sexy", 1)
                                        $ newgirl["Laura"].Spunk.append("mouth")
                                        ch_l "Wasn't that bad. . ."
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                                        $ newgirl["Laura"].Spunk.remove("mouth")
                                    elif ApprovalCheck("Laura", 1200, "OI", Bonus = (newgirl["Laura"].Addict*10)):
                                        call LauraFace("bemused", 1)
                                        $ newgirl["Laura"].Brows = "normal" 
                                        $ newgirl["Laura"].Mouth = "sad"
                                        $ newgirl["Laura"].Spunk.remove("hand")
                                        $ newgirl["Laura"].Spunk.append("mouth")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ newgirl["Laura"].Spunk.remove("mouth")
                                        ch_l "Not my favorite flavor. . ."
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                                    else:
                                        $ newgirl["Laura"].Spunk.remove("hand")
                                        "She scowls at you and wipes her hand off. Then she licks her lips."
                                        jump Laura_Orgasm_After
                                    
                            "Swallow it, now.":
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 30, -1, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1, 1)                    
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -1, 1)
                                    if ApprovalCheck("Laura", 1200, "OI") or newgirl["Laura"].Addict >= 50:                            
                                        call LauraFace("sad", 1)
                                        $ newgirl["Laura"].Spunk.append("mouth")
                                        $ newgirl["Laura"].Spunk.remove("hand")
                                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                                        $ newgirl["Laura"].Spunk.remove("mouth")
                                        ch_l "Not my favorite flavor. . ."
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                                    else:         
                                        $ newgirl["Laura"].Spunk.remove("hand")               
                                        "She scowls at you and wipes her hand off. Then she licks her lips."                        
                                        jump Laura_Orgasm_After
                else:                
                            jump Laura_Orgasm_After
                                
                jump Laura_Swallowed
                #end if not asked/auto / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
    
    $ Situation = 0
    "You ask if you can cum in her mouth."
    if renpy.showing("Laura_SexSprite"):
            call Laura_HJ_Launch("cum")
        
    if "full" in newgirl["Laura"].RecentActions:
            pass
        
    elif newgirl["Laura"].Swallow >= 5 or "hungry" in newgirl["Laura"].Traits:  
            # If she's swallowed 5 times, 
            if renpy.showing("Laura_TJ_Animation"):         
                call LauraFace("tongue",Eyes="down")
                $ Speed = 5 #shallow animation
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She nods and bends down to put the tip between her lips."
            elif not LauraBJShowing:
                call Laura_BJ_Launch_("cum")           
                call LauraFace("tongue",Eyes="down")
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She nods and bends down to put the tip between her lips."
            else:                 
                call LauraFace("tongue",Eyes="down")
                $ newgirl["Laura"].Brows = "confused"
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She nods and hums a \"yes\" sound."   
            $ newgirl["Laura"].Spunk.append("mouth")
            $ newgirl["Laura"].Spunk.append("chin")
            "After you cum, she quickly gulps it down and wipes her mouth."
            ". . ."
            call LauraFace("sexy")            
            $ Speed = 0
            if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
            ch_l "Yum."
            $ newgirl["Laura"].Spunk.remove("mouth")
            jump Laura_Swallowed
        
    elif newgirl["Laura"].Addict >= 80 and newgirl["Laura"].Swallow: 
            #addicted           
            if renpy.showing("Laura_TJ_Animation"):         
                call LauraFace("tongue",Eyes="down")
                $ Speed = 5 #shallow animation
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She gently puts the tip to her lips, just as you blow."
            elif not LauraBJShowing:
                call Laura_BJ_Launch_("cum")           
                call LauraFace("tongue",Eyes="down")
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She gently puts the tip to her lips, just as you blow."
            else:                 
                call LauraFace("tongue",Eyes="down")
                $ newgirl["Laura"].Brows = "confused"
                $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                "She nods and hums a \"yes\" sound."                    
            $ newgirl["Laura"].Spunk.append("mouth")
            $ newgirl["Laura"].Spunk.append("chin")
            "She gags a little, but quickly swallows it."
            ". . ."
            $ Speed = 0
            if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
            call LauraFace("sexy")
            $ newgirl["Laura"].Mouth = "smile"
            ch_l "Can't say I didn't enjoy that . ."
            $ newgirl["Laura"].Spunk.remove("mouth")
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 5)
            jump Laura_Swallowed
            
    elif newgirl["Laura"].Swallow:                
            if ApprovalCheck("Laura", 900):
                if renpy.showing("Laura_TJ_Animation"):         
                    call LauraFace("tongue",Eyes="down")
                    $ Speed = 5 #shallow animation
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "She gently puts the tip to her lips, just as you blow."
                elif not LauraBJShowing:
                    call Laura_BJ_Launch_("cum")           
                    call LauraFace("tongue",Eyes="down")
                    $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "She gently puts the tip to her lips, just as you blow."
                else:                 
                    call LauraFace("tongue",Eyes="down")
                    $ newgirl["Laura"].Brows = "confused"
                    $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "She tilts her head and hums a \"hmm?\" sound."
                $ newgirl["Laura"].Spunk.append("mouth")
                $ newgirl["Laura"].Spunk.append("chin")
                $ newgirl["Laura"].Brows = "normal"
                $ newgirl["Laura"].Eyes = "sexy"
                ". . ."
                $ Speed = 0
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                call LauraFace("sexy")
                $ newgirl["Laura"].Spunk.append("mouth")
                $ newgirl["Laura"].Spunk.append("chin")
                ch_l "It grows on you. . ."
                $ newgirl["Laura"].Spunk.remove("mouth")
                jump Laura_Swallowed
     
    #If she hasn't swallowed or doesn't automatically want to. . .  
    
    if  ApprovalCheck("Laura", 300, "LI") or ApprovalCheck("Laura", 300, "OI"): 
        call LauraFace("bemused")
        $ newgirl["Laura"].Eyes = "sexy"
    else:
        call LauraFace("angry")
        
    $ Speed = 0    
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    
    if "full" in newgirl["Laura"].RecentActions:
            ch_l "I'm stuffed, [newgirl[Laura].Petname]. . ." 
    else:
            ch_l "I don't know why. . ."
    
    menu:
        extend ""
        "Sorry about that.":
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 3)
                $ newgirl["Laura"].Addictionrate += 1
                if "addictive" in P_Traits:
                    $ newgirl["Laura"].Addictionrate += 1
                call LauraFace("smile", 1)
                ch_l "Hmm. . ."
                if ApprovalCheck("Laura", 1200, TabM=1) and "full" not in newgirl["Laura"].RecentActions:
                    $ Approval = 2 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)  
                    call LauraFace("sexy", 1)
                    ch_l "Maybe a little. . ."
                else:
                    jump Laura_Handy_Finish                
            
        "Give it a try, you might like it." if "full" not in newgirl["Laura"].RecentActions:
                if ApprovalCheck("Laura", 1200, TabM=1):  
                    $ Approval = 2
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 5)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 3)
                    $ newgirl["Laura"].Brows = "confused"  
                    $ newgirl["Laura"].Eyes = "sexy"
                    ch_l "If you insist. . ."
                else:     
                    $ newgirl["Laura"].Addictionrate += 1
                    if "addictive" in P_Traits:
                        $ newgirl["Laura"].Addictionrate += 1
                    $ newgirl["Laura"].Blush = 1
                    ch_l "You think I don't have a nose, [newgirl[Laura].Petname]?"
                    jump Laura_Handy_Finish
                            
        "Seriously, put it in your mouth.":
                if ApprovalCheck("Laura", 1500, "LI", TabM=1) or ApprovalCheck("Laura", 1200, "OI", TabM=1):
                        call LauraFace("sucking", 1)
                elif ApprovalCheck("Laura", 1000, "OI", Bonus = (newgirl["Laura"].Addict*10)): #Mild addiction included                
                        call LauraFace("angry", 1)
                else: 
                        #You insisted, she refused. 
                        call LauraFace("angry", 1)
                        "She scowls at you, drops you cock and pulls back."
                        call Laura_HJ_Launch("cum")
                        call Laura_HJ_Reset                
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                        ch_l "Seriously, you eat a dick."
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                        $ newgirl["Laura"].RecentActions.append("angry")
                        $ newgirl["Laura"].DailyActions.append("angry")   
                        $ Line = 0
                        return      
                if renpy.showing("Laura_TJ_Animation"):         
                    call LauraFace("tongue")
                    $ Speed = 5 #shallow animation
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                else:
                    $ newgirl["Laura"].Mouth = "sucking"
                    call Laura_BJ_Launch_("cum")            
                    $ Speed = 5 
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5)
    
    if renpy.showing("Laura_TJ_Animation"):          
        call LauraFace("tongue")
        $ Speed = 5 #shallow animation                         
        if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    elif not LauraBJShowing:
        call Laura_BJ_Launch_("cum")     
        $ Speed = 6 if Speed == 4 else 5 #6 if deep throating, 5 if not
        if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    $ newgirl["Laura"].Spunk.append("mouth")
    $ newgirl["Laura"].Spunk.append("chin")
    if ApprovalCheck("Laura", 1200):            
            "She gently puts the tip to her lips, just as you blow."
            "She coughs a little, but quickly swallows it." 
    else:
            "She tentatively places the tip in her mouth, and you blast inside it."
            "She quickly gulps it down."                    
            call LauraFace("sexy")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)        
    $ newgirl["Laura"].Mouth = "sucking"
    ". . ."   
    $ Speed = 0            
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    call LauraFace("sexy") 
    
    if ApprovalCheck("Laura", 1000) and newgirl["Laura"].Swallow >= 3:
            ch_l "Mmmmm. . ."    
    elif ApprovalCheck("Laura", 800):                
            ch_l "Takes a little getting used to. . ."
    else:
            call LauraFace("sad")
            ch_l "That's. . . intense. . ."   
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 3)
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)            
    $ newgirl["Laura"].Blow += 1
    jump Laura_Swallowed     
    #end Laura in mouth  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Creampie_P:
        if Trigger == "sex" and Situation == "auto":
                $ P_Cock = "in"
                $ newgirl["Laura"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 4
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                if ApprovalCheck("Laura", 1300) or newgirl["Laura"].CreamP:              
                        call LauraFace("surprised", Eyes="down")
                        "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."  
                        call LauraFace("sexy")
                        if newgirl["Laura"].Lust >= 85: 
                            call Laura_Cumming
                else:
                    if newgirl["Laura"].Lust >= 85: 
                            "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                            call Laura_Cumming                
                    else:
                            "You come in her pussy. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call LauraFace("angry")
                    ch_l "Hey, maybe a heads up?"
                    call LauraFace("bemused")
                    ch_l "Not that it didn't feel good. . ."
                    
                jump Laura_Creampied
        
        #else (You ask her if it's ok):
        if ApprovalCheck("Laura", 1200) or newgirl["Laura"].CreamP:        
                call LauraFace("sexy")
                if newgirl["Laura"].CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif newgirl["Laura"].CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "in"
                $ newgirl["Laura"].Spunk.append("in")
                $ P_Spunk = "in"
                $ Speed = 4
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                if newgirl["Laura"].Lust >= 85: 
                    call Laura_Cumming  
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1) 
                ch_l "Very. . . filling."
                jump Laura_Creampied
        else:
                call LauraFace("sexy")
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2) 
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2) 
                ch_l "Thanks for the heads up *grunt* [newgirl[Laura].Petname], but let's not."
        jump Laura_SpunkBelly

#Start Anal Creampie  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Creampie_A:                             
        # These need conditionals added    
        if Trigger == "anal" and Situation == "auto":
                $ P_Cock = "anal"
                $ newgirl["Laura"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 4
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                if ApprovalCheck("Laura", 1200) or newgirl["Laura"].CreamP:              
                    call LauraFace("surprised", 1, Eyes="down")
                    "You come in her ass. Her eyes widen in surprise, but she takes it in stride."  
                    call LauraFace("sexy")
                    if newgirl["Laura"].Lust >= 85: 
                        call Laura_Cumming
                else:
                    if newgirl["Laura"].Lust >= 85: 
                        "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                        call Laura_Cumming                
                    else:
                        "You come in her ass. Her eyes widen in surprise and she pulls out."
                    $ P_Cock = "out"
                    call LauraFace("angry")
                    ch_l "No advanced warning, [newgirl[Laura].Petname]?"
                    call LauraFace("bemused")
                    ch_l "That was pretty filling. . ."
                jump Laura_Creampied
            
        #else (You ask her if it's ok):
        if ApprovalCheck("Laura", 1200) or newgirl["Laura"].CreamP:        
                call LauraFace("sexy")
                if newgirl["Laura"].CreamP >= 3:
                    "She smiles and speeds up her actions, causing you to erupt inside her."  
                elif newgirl["Laura"].CreamP:
                    "She gets a michevious look and speeds up, you burst inside her." 
                else:
                    "As you continue to pound her, she nods her head."
                $ P_Cock = "anal"
                $ newgirl["Laura"].Spunk.append("anal")
                $ P_Spunk = "anal"
                $ Speed = 4
                if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                if newgirl["Laura"].Lust >= 85: 
                    call Laura_Cumming  
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1) 
                ch_l "Mmmm, so full. . ."
                jump Laura_Creampied
        else:
                call LauraFace("sexy")     
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2) 
                ch_l "Thanks for warning me *grunt* [newgirl[Laura].Petname], but perhaps not."
        jump Laura_SpunkBelly
            
#Start Facial  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label Laura_Facial: 
    if LauraBJShowing:       
            if newgirl["Laura"].Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed)) and newgirl["Laura"].Swallow:
                    $ newgirl["Laura"].Eyes = "manic"
                    $ newgirl["Laura"].Blush = 1
                    $ Speed = 0
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    $ Speed = 4
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    $ newgirl["Laura"].Spunk.append("mouth")
                    $ newgirl["Laura"].Spunk.append("chin")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ newgirl["Laura"].Mouth = "lipbite"
                    $ Speed = 0
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "When she finishes, she draws her hand across her lips."
                    call LauraFace("bemused")
                    $ newgirl["Laura"].Spunk.remove("mouth")
                    ch_l "I'm sorry, [newgirl[Laura].Petname], but waste not want not."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -5)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)
                    jump Laura_Swallowed
            call Laura_HJ_Launch("cum")
            $ Speed = 2
            if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
            if "hair" in newgirl["Laura"].Spunk:
                pass
            elif "facial" in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.append("hair")
            else:
                $ newgirl["Laura"].Spunk.append("facial")
            "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
            $ Speed = 0
            if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
            jump Laura_Orgasm_After
    
    if not renpy.showing("Laura_TJ_Animation") and not renpy.showing("Laura_HJ_Animation"):      
            call Laura_HJ_Launch("cum")
            $ Speed = 2
            if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    if "hair" in newgirl["Laura"].Spunk:
        pass
    elif "facial" in newgirl["Laura"].Spunk:
        $ newgirl["Laura"].Spunk.append("hair")
    else:
        $ newgirl["Laura"].Spunk.append("facial")
    "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
    $ Speed = 0
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)

    if Situation == "warn":
        ch_l "Thanks for the warning. . . maybe not the mess though. . ." 
    else:
        ch_l "What a mess, maybe a heads up next time?" 
                
    jump Laura_Orgasm_After

#Start titjob spunk  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
label Laura_TitSpunk: 
    if LauraBJShowing:       
            if newgirl["Laura"].Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed)) and newgirl["Laura"].Swallow:
                    $ newgirl["Laura"].Eyes = "manic"
                    $ newgirl["Laura"].Blush = 1
                    $ Speed = 0
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "You pull out of her mouth with a pop, and her eyes widen in surprise." 
                    $ Speed = 4
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    $ newgirl["Laura"].Spunk.append("mouth")
                    $ newgirl["Laura"].Spunk.append("chin")
                    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
                    $ newgirl["Laura"].Mouth = "lipbite"
                    $ Speed = 0
                    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
                    "When she finishes, she draws her hand across her lips."
                    call LauraFace("bemused")
                    $ newgirl["Laura"].Spunk.remove("mouth")
                    ch_l "I'm sorry, [newgirl[Laura].Petname], but waste not want not."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -5)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)
                    jump Laura_Swallowed
               
    if not renpy.showing("Laura_TJ_Animation") and not renpy.showing("Laura_HJ_Animation") and not LauraBJShowing:      
            call Laura_TJ_Launch("cum")
    $ newgirl["Laura"].Spunk.append("tits")
    $ Speed = 0
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    "As you're about to finish, you speed up and spray all over her chest."

    if Situation == "warn":
        ch_l "Thanks for the warning. . . maybe not the mess though. . ." 
    else:
        ch_l "What a mess, maybe a heads up next time?" 
                
    jump Laura_Orgasm_After
    
# Start Spunk back  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_SpunkBelly:   
    
    call Laura_Sex_Launch("hotdog")
    if newgirl["Laura"].Addict >= 60 and ApprovalCheck("Laura", 1000, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed))  and newgirl["Laura"].Swallow:
            $ newgirl["Laura"].Eyes = "manic"
            $ newgirl["Laura"].Blush = 1
            call Laura_BJ_Launch_("cum")
            if Trigger == "sex":
                "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            elif Trigger == "anal":                
                "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
            $ newgirl["Laura"].Mouth = "lipbite"
            $ newgirl["Laura"].Spunk.append("mouth")
            "When she finishes, she draws her hand across her lips."
            call LauraFace("bemused")
            $ newgirl["Laura"].Spunk.remove("mouth")
            ch_l "Sorry, [newgirl[Laura].Petname], but I couldn't let that go to waste."
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -5)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)
            jump Laura_Swallowed
    $ P_Cock = "out"
    $ P_Spunk = "out"    
    $ Speed = 4
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    $ newgirl["Laura"].Spunk.append("belly")
    if Trigger == "sex":
            "You pull out of her pussy with a pop and spray all over her belly."
    elif Trigger == "anal":
            "You pull out of her ass with a pop and spray all over her belly."
    else:
            "You pick up the pace and with a grunt you spray all over her belly."
        
                  
    if newgirl["Laura"].Addict >= 60 and ApprovalCheck("Laura", 800, "I", Bonus = ((newgirl["Laura"].Addict*10)- newgirl["Laura"].Obed)) and newgirl["Laura"].Swallow: 
            #if she's manic and has swallowed
            $ newgirl["Laura"].Eyes = "manic"
            $ newgirl["Laura"].Blush = 1        
            "Laura's eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
            call LauraFace("manic", 1)
            $ newgirl["Laura"].Spunk.append("mouth")
            $ newgirl["Laura"].Mouth = "smile"
            ch_l "Well, [newgirl[Laura].Petname], I just couldn't let that go to waste."
            $ newgirl["Laura"].Spunk.remove("mouth")
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
            jump Laura_Swallowed
          
        
    #else . . .
    call LauraFace("sexy", 1)
    ch_l "Hmm. . . what a mess. . ."  
#    call Laura_Sex_Reset
    jump Laura_Orgasm_After
    
   
#Start Handy finish  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Handy_Finish:
    if renpy.showing("Laura_SexSprite"):
        call Laura_Sex_Reset
    call Laura_HJ_Launch("cum")
    $ Speed = 2        
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    $ newgirl["Laura"].Spunk.append("hand")  
    if renpy.showing("Laura_HJ_Animation"):                                  
            "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands." 
    else:
            "She grins and starts jerking you off, placing her left hand over your tip. You burst all over her hands." 
    $ Speed = 0
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    
    if newgirl["Laura"].Addict > 80 or "hungry" in newgirl["Laura"].Traits:
            $ newgirl["Laura"].Eyes = "manic"
            $ newgirl["Laura"].Spunk.remove("hand")
            $ newgirl["Laura"].Spunk.append("mouth")
            $ newgirl["Laura"].Mouth = "smile"
            "She licks her hands off with a satisfied grin."
            $ newgirl["Laura"].Spunk.remove("mouth")
            ch_l "Hmmm. . ."
    else:
            call LauraFace("bemused")
            $ newgirl["Laura"].Spunk.remove("hand")
            "She wipes her hands off, but takes a quick sniff when she's done and smiles."
            ch_l "Thanks for the heads up." 
            jump Laura_Orgasm_After


#Start Swallowed  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Swallowed: 
        $ newgirl["Laura"].Swallow += 1
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
        $ newgirl["Laura"].Addict -= 20    
        if "mouth" in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.remove("mouth")
        if "full" not in newgirl["Laura"].RecentActions and Action_Check("Laura", "recent", "swallowed") >= 5: 
                $ newgirl["Laura"].RecentActions.append("full")    
                call LauraFace("surprised", 1)
                ch_l "-ehem-"
                call LauraFace("sexy", 1)
                ch_l "Excuse me [newgirl[Laura].Petname], it must have been something I ate."
        $ newgirl["Laura"].RecentActions.append("swallowed")                      
        $ newgirl["Laura"].DailyActions.append("swallowed") 
        $ newgirl["Laura"].Addictionrate += 2
        if "addictive" in P_Traits:
                $ newgirl["Laura"].Addictionrate += 2
        if Trigger == "anal":    
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 2)
        if newgirl["Laura"].Swallow == 1:
                $newgirl["Laura"].SEXP += 12
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 5)
        jump Laura_Orgasm_After

#Start Creampied  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Creampied:
    if Trigger == "sex":
            $ newgirl["Laura"].CreamP += 1
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 10)
            $ newgirl["Laura"].RecentActions.append("creampie sex")                      
            $ newgirl["Laura"].DailyActions.append("creampie sex") 
    elif Trigger == "anal":
            $ newgirl["Laura"].CreamA += 1
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5)
            $ newgirl["Laura"].RecentActions.append("creampie anal")                      
            $ newgirl["Laura"].DailyActions.append("creampie anal") 
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
    $ newgirl["Laura"].Addict -= 30
    $ newgirl["Laura"].Addictionrate += 2
    if "addictive" in P_Traits:
            $ newgirl["Laura"].Addictionrate += 3
    if newgirl["Laura"].CreamP == 1:
            $newgirl["Laura"].SEXP += 10
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 5)
#    call Laura_Sex_Reset

# Clean-up / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Orgasm_After:
        $ Line = "What next?"
        if not renpy.showing("Laura_HJ_Animation"):
            $ newgirl["Laura"].Girl_Arms = 1
        $ P_Semen -= 1
        $ P_Focus = 0
        $ Speed = 0  
        if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
        menu:
                "Want her to clean you off?"
                "Yes":
                    call Laura_CleanCock
                "No":
                    pass
        if newgirl["Laura"].Spunk:
                call Laura_Cleanup
        $ Situation = 0
        return
        
        
label Laura_CleanCock:
        $ Line = "What next?"
        if not renpy.showing("Laura_HJ_Animation"):
            $ newgirl["Laura"].Girl_Arms = 1
        $ P_Cock = "out"
        $ Speed = 0    
        if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
        if Trigger == "anal" and not ApprovalCheck("Laura", 1600, TabM=1) and not newgirl["Laura"].Addict >= 80:
                "She wipes your cock clean."
        elif "classcaught" in newgirl["Laura"].RecentActions and bg_current == "bg classroom" and newgirl["Laura"].SEXP <= 10:
                #this skips this step if you haven't done much yet
                "She wipes your cock clean."
        elif newgirl["Laura"].Blow > 3 or newgirl["Laura"].Swallow: 
                if ApprovalCheck("Laura", 1200, TabM=1) or newgirl["Laura"].Addict >= 60:
                        call Laura_BJ_Launch_("cum")
                        $ Speed = 1
                        if LauraBJShowing:
                            call Laura_BJ_Launch_(Speed = Speed)
                        call LauraFace("sucking", 1) 
                        if ApprovalCheck("Laura", 1500, TabM=1):
                            if newgirl["Laura"].Love > newgirl["Laura"].Inbt and newgirl["Laura"].Love > newgirl["Laura"].Obed:
                                $ newgirl["Laura"].Eyes = "sly"
                                "She looks up at you lovingly as she licks your cock clean."            
                            elif newgirl["Laura"].Obed > newgirl["Laura"].Inbt:
                                $ newgirl["Laura"].Eyes = "side"
                                "She dutifully licks your cock clean with lowered eyes."
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 3)                
                            else:
                                "She happily licks your cock clean." 
                        elif newgirl["Laura"].Addict >= 60:
                                "She hungrily and thoroughly licks your cock clean."   
                        else:
                            "She licks you cock clean." 
                        call LauraFace("sexy")  
                else:
                        if not renpy.showing("Laura_HJ_Animation"):
                            call Laura_HJ_Launch("cum") 
                        "She wipes your cock clean."  
        else:
                        if not renpy.showing("Laura_HJ_Animation"):
                            call Laura_HJ_Launch("cum") 
                        "She wipes your cock clean."         
        $ P_Spunk = 0
        call LauraFace("sexy") 
        return
    
# End You Cumming //////////////////////////////////////////////////////////////////////////////////


# Laura Lusty face check ////////////////////////////////////////////////////////////////////////////////
label LauraLust(Extreme = 0, Kissing = 0):
                
    if newgirl["Laura"].Lust >= 90:        
            $ newgirl["Laura"].Blush = 2
    elif newgirl["Laura"].Lust >= 40:        
            $ newgirl["Laura"].Blush = 1 
        
    if newgirl["Laura"].Lust >= 80:
            $ newgirl["Laura"].Wet = 2 
    elif newgirl["Laura"].Lust >= 50:
            $ newgirl["Laura"].Wet = 1
            
    if newgirl["Laura"].Loc == "bg teacher" and not Extreme:
            #this prevents her face from changing if she's just being a teacher.
            return
       
    if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1
    elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1   
    elif Partner != "Laura":
            #If Laura is kissing and is primary
            if Trigger == "kiss you" or Trigger2 == "kiss you":  
                $ Kissing = 1
    elif Trigger4 == "kiss you":   
            #If Laura is kissing you in a threesome action
            $ Kissing = 1
            
    if Kissing:
            $ newgirl["Laura"].Eyes = "closed"
            if newgirl["Laura"].Kissed >= 10 and newgirl["Laura"].Inbt >= 300:
                $ newgirl["Laura"].Mouth = "sucking"
            elif newgirl["Laura"].Kissed > 1 and newgirl["Laura"].Addict >= 50:            
                $ newgirl["Laura"].Mouth = "sucking"
            else:
                $ newgirl["Laura"].Mouth = "kiss"
    else:    
            #If Laura is not kissing someone
            if newgirl["Laura"].Lust >= 90:
                    $ newgirl["Laura"].Eyes = "closed"
                    $ newgirl["Laura"].Brows = "sad"
                    $ newgirl["Laura"].Mouth = "surprised"
            elif newgirl["Laura"].Lust >= 70:
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "sad"
                    $ newgirl["Laura"].Mouth = "lipbite"
            elif newgirl["Laura"].Lust >= 50 and not Extreme:
                    $ newgirl["Laura"].Eyes = "squint"
                    $ newgirl["Laura"].Brows = "sad"
                    $ newgirl["Laura"].Mouth = "lipbite"
            elif newgirl["Laura"].Lust >= 30 and not Extreme:
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "normal"
                    $ newgirl["Laura"].Mouth = "smirk"
            elif not Extreme:
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "normal"
                    $ newgirl["Laura"].Mouth = "smirk"    
            if newgirl["Laura"].Lust < 50 and not Extreme and not ApprovalCheck("Laura", 1000):
                $ newgirl["Laura"].Eyes = "side"
    
    if Partner == "Laura" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ newgirl["Laura"].Mouth = "tongue"  
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ newgirl["Laura"].Mouth = "tongue"  
                    
    if newgirl["Laura"].OCount >= 10:   
            #If you've fucked her senseless
            $ newgirl["Laura"].Eyes = "stunned"
            $ newgirl["Laura"].Mouth = "tongue"   
                
    return

# End faces

#  Laura Orgasm //////////////////////////

label Laura_Cumming:
    $ newgirl["Laura"].Eyes = "surprised"
    $ newgirl["Laura"].Brows = "sad"
    $ newgirl["Laura"].Mouth = "tongue"
    $ newgirl["Laura"].Blush = 1
    ch_l ". . . !"
    $ Speed = 0
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    if renpy.showing("Laura_SexSprite"):
            show Laura_SexSprite #fix, test this
            with vpunch
    elif LauraBJShowing:           #fix, make this animation work better when paused for this effect.
            # show Laura_BJ_Animation
            $ renpy.show("Laura_BJ_Body_" + str(Speed))
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
    $ Speed = 1
    if LauraBJShowing:
                        call Laura_BJ_Launch_(Speed = Speed)
    $ Line = renpy.random.choice(["Laura is suddenly rocked with spasms, holding back a muffled scream.", 
                "Laura grabs on tightly as her body shakes with pleasure.", 
                "Laura stiffens and lets out a low moan.",
                "Laura's body quivers and suddenly goes still."])
    "[Line]"
    
    $ newgirl["Laura"].Eyes = "closed"
    $ newgirl["Laura"].Brows = "sad"
    $ newgirl["Laura"].Mouth = "tongue"
    $ Line = renpy.random.choice(["Oooooh. . .", 
                "That was a good one. . .", 
                "Hmmmm. . . .",
                "That was. . ."])
    ch_l "[Line]"
           
    
    $ newgirl["Laura"].Lust = 30 if "hotblooded" in newgirl["Laura"].Traits else 0 
    $ newgirl["Laura"].Lust += (newgirl["Laura"].OCount * 5)
    $ newgirl["Laura"].Lust = 80 if newgirl["Laura"].Lust >= 80 else newgirl["Laura"].Lust    
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
            
    if "unsatisfied" in newgirl["Laura"].RecentActions:  #If she had been unsatisfied, you satisfied her. . .        
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            if "unsatisfied" in newgirl["Laura"].DailyActions:
                ch_l "Thanks for evening the score, [newgirl[Laura].Petname]?"
            call DrainWord("Laura","unsatisfied")
    $ newgirl["Laura"].OCount += 1        
    $ newgirl["Laura"].Org += 1
    $ Line = 0
      
    if Trigger != "masturbation":
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 40, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)  
            if newgirl["Laura"].OCount == 1:
                    # if she's angry, but not too angry, then reduce that on the first O of the time block.
                    $ newgirl["Laura"].ForcedCount -= 1 if 5 > newgirl["Laura"].ForcedCount > 0 else 0 
            
            #checks to check reaction of other girls
            if K_Loc == bg_current and "noticed laura" in K_RecentActions:                     
                    $ K_Lust += 15 if K_LikeNewGirl["Laura"] >= 500 else 10
                    $ K_Lust += 5 if K_Les >= 5 else 0
            elif R_Loc == bg_current and "noticed laura" in R_RecentActions: 
                    $ R_Lust += 15 if R_LikeNewGirl["Laura"] >= 500 else 10
                    $ R_Lust += 5 if R_Les >= 5 else 0 
            elif E_Loc == bg_current and "noticed laura" in E_RecentActions: 
                    $ E_Lust += 15 if E_LikeNewGirl["Laura"] >= 500 else 10
                    $ E_Lust += 5 if E_Les >= 5 else 0 
            if Partner == "Laura":
                    #If the active girl is someone else
                    call Partner_Cumming("Laura")
                    
            #Orgasm count
            if Trigger != "blow" and Trigger != "hand" and Partner != "Laura":
                if newgirl["Laura"].OCount == 2:
                        $ newgirl["Laura"].Brows = "confused"
                        ch_l "Hey, good job, [newgirl[Laura].Petname]. . ."
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)            
                elif newgirl["Laura"].OCount == 3: #5
                        $ newgirl["Laura"].Brows = "confused"            
                        ch_l "You can. . . definitely. . . keep up. . ."
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 2)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 1)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)                    
                elif newgirl["Laura"].OCount == 6 and Partner != "Laura": #10
                    $ newgirl["Laura"].Mouth = "tongue"    
                    ch_l "I don't. . . usually. . . wear out. . . this easy. . ."
                    menu:
                        ch_l "could. . . we. . . take. . . a break?"
                        "Finish up." if P_FocusX:
                            "You release your concentration. . ."                 
                            $ P_FocusX = 0
                            $ P_Focus += 15                    
                        "Let's try something else." if MultiAction:  
                            $ Situation = "shift"
                        "No, I'm not done yet.":
                            if Trigger == "sex" or Trigger == "anal":
                                if ApprovalCheck("Laura", 1000, TabM=1) or ApprovalCheck("Laura", 400, "O", TabM=1):
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 3)
                                    $ newgirl["Laura"].Eyes = "stunned"
                                    "She drifts off into incoherent moans."
                                else:
                                    call LauraFace("angry", 1)
                                    "She scowls at you, pulls out with a pop, and wipes herself off."
                                    ch_l "Learn to take a hint. . ."
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                            else:
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                $ newgirl["Laura"].Eyes = "stunned"
                                "She drifts off into incoherent moans."  
                #end Ocount stuff
    if Trigger == "strip":
            call AllReset("Laura")
            show Laura_Sprite at Laura_Dance1()
            "Laura begins to dance again."
    return
    
# End Laura Orgasm /////////////////////////////////////////////////////////////////////////////////////


# Start Laura Clean-Up /////////////////////////////////////////////////////////////////////////////////////
label Laura_Cleanup(Choice = "random", Options = [], Cnt = 0, Cleaned = 0):
    
    if Choice == "after":
            # This is at the end of a session            
            if not newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Wet = 0
                return    
            $ Cnt = 1  
        
    if newgirl["Laura"].Addict > 80 and newgirl["Laura"].Swallow:
        #if she likes cum, she prefers to eat it. 
        $ Choice = "eat"            
        $ newgirl["Laura"].Eyes = "manic"
        $ newgirl["Laura"].Mouth = "smile" 
    elif Cnt and "taboo" not in newgirl["Laura"].History:
        $ Choice = "clean"           
    elif Choice == "ask":
        pass
    elif "painted" in newgirl["Laura"].RecentActions and ApprovalCheck("Laura", 1000, "OI"):
        return
    elif ApprovalCheck("Laura", 1200, "LO"):  
        $ Choice = "ask"            
    elif not ApprovalCheck("Laura", 400, "I"):
        call LauraFace("bemused") 
        $ Choice = "clean"   
    else:
        $ Choice = "ask"      
   
    $ Cleaned = 1 if "cleaned" in newgirl["Laura"].DailyActions else 0
    $ newgirl["Laura"].RecentActions.append("cleaned") 
    $ newgirl["Laura"].DailyActions.append("cleaned") 
    
    if Choice == "ask":
            $ Choice = "random"
            "She looks down at the spunk covering her."
            menu:
                "What do you suggest Laura do about cleaning up?"
                "You should leave it where it is.":
                        if not Cnt:
                            # If this isn't the end of the session
                            if ApprovalCheck("Laura", 300, "I") or ApprovalCheck("Laura", 1000):
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Inbt, 50, 1)
                                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 2) 
                                    $ Choice = "leave"  
                                    call LauraFace("sly") 
                                    ch_l "Hmm. . ."
                            else:
                                    call LauraFace("sly") 
                                    ch_l "Eh, I'm not a fan of mess, [newgirl[Laura].Petname]." 
                        elif ApprovalCheck("Laura", 900, "I") or "exhibitionist" in newgirl["Laura"].Traits:
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
                                $ Choice = "leave"  
                                call LauraFace("sly") 
                                ch_l "Hmm. . . I do like the glow it gives me. . "
                        elif ApprovalCheck("Laura", 600, "I") and ApprovalCheck("Laura", 1200, "LO"):
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
                                $ Choice = "leave"  
                                call LauraFace("surprised",2) 
                                ch_l "Hmm. . . if you insist. . ."
                                call LauraFace("sly",1) 
                        
                        else:
                            call LauraFace("angry") 
                            menu:
                                ch_l "Excuse me?" 
                                "Please?":
                                    if ApprovalCheck("Laura", 1800):
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 85, 1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 3) 
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                                        ch_l "Fine."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        call LauraFace("angry") 
                                        ch_l "I'm in no mood for this."
                                    elif ApprovalCheck("Laura", 800):
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1) 
                                        ch_l "You're certainly persistant, but no."
                                    else:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 75, -5)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, -10)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                                        call LauraFace("angry") 
                                        ch_l "You've gotta be joking."
                                "I insist.":
                                    call LauraFace("sad") 
                                    if ApprovalCheck("Laura", 400, "I") and ApprovalCheck("Laura", 1200, "LO"):
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 3)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                                        ch_l "Fine."
                                        $ Choice = "leave"  
                                    elif ApprovalCheck("Laura", 800, "O"):
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -10)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 10)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 5)
                                        ch_l "If you insist."
                                        $ Choice = "leave"  
                                    elif Cleaned:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -1)
                                        call LauraFace("angry") 
                                        ch_l "Enough out of you."
                                    elif ApprovalCheck("Laura", 800):
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -1)
                                        call LauraFace("sad") 
                                        ch_l "Don't push it." 
                                    else:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -10)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                        call LauraFace("angry") 
                                        ch_l "Hell no."
                                        
                                "Never mind then.":
                                    ch_l "Ok. . ."                            
                        #end "leave it"
                        
                "You should just eat it.":
                        call LauraFace("sly") 
                        if "hungry" in newgirl["Laura"].Traits or (newgirl["Laura"].Swallow >= 5 and ApprovalCheck("Laura", 800)): 
                                #lots of swallows
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
                                $ Choice = "eat"   
                                "She licks her lips. . ."
                        elif newgirl["Laura"].Swallow and ApprovalCheck("Laura", 800): 
                                #few swallows
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2) 
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
                                $ Choice = "eat"   
                                ch_l "You do taste pretty good. . ."
                        elif ApprovalCheck("Laura", 1200): 
                                #no swallows, but likes you
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                                $ Choice = "eat"   
                                ch_l "I have been thinking about it. . ."
                        elif ApprovalCheck("Laura", 400): 
                                #Likes you well enough, but won't
                                call LauraFace("sad") 
                                ch_l "Yeah, but I won't. . ."
                        else: 
                                #doesn't like you.
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -3)
                                call LauraFace("angry") 
                                ch_l "Nope."
                        #end eat it
                              
                "You should just clean it up.":
                        if ApprovalCheck("Laura", 600, "I") and not ApprovalCheck("Laura", 1500, "LO"): #rebellious
                                call LauraFace("sly") 
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 10) 
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 5) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                                ch_l "I could. . ."
                                ch_l "-but I don't want to. . ."
                                $ Choice = "leave"   
                                menu:
                                    extend ""
                                    "Ok, fine.":
                                        call LauraFace("smile") 
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 5)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                                    "No, clean it up.": 
                                        if ApprovalCheck("Laura", 600, "O"):
                                            call LauraFace("sad") 
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                                            ch_l "Oh, fine. . ."
                                            $ Choice = "clean"  
                                        elif ApprovalCheck("Laura", 1200, "LO"):
                                            call LauraFace("sad") 
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3)
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                                            ch_l "Booo. . ."
                                            $ Choice = "clean"   
                                        else:
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5)
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -5)
                                            ch_l "Too bad."
                                                                                    
                        else: #agrees
                                call LauraFace("bemused") 
                                $ Choice = "clean"   
                                ch_l "Whatever. . ."
                        #end clean it up
                        
                "Say nothing. [[leave it to her]":
                    $ Choice = "random"
            #end "asked"
                
                
    if Choice == "random":
            $ Options = ["clean"]
            if newgirl["Laura"].Swallow and ApprovalCheck("Laura", 800):
                    $ Options.append("eat") 
                    if newgirl["Laura"].Swallow >=5:                            
                        $ Options.append("eat") 
                    if "hungry" in newgirl["Laura"].Traits:                
                        $ Options.append("eat") 
            if ApprovalCheck("Laura", 600, "I"):
                    if not Cnt:
                        $ Options.append("leave") 
                    if not Cnt or ApprovalCheck("Laura", 800, "I"):
                        $ Options.append("leave") 
                    if "exhibitionist" in newgirl["Laura"].Traits:
                        $ Options.append("leave") 
                                        
            $ renpy.random.shuffle(Options)
            
            $ Choice = Options[0]
            #end "random"
            
            
    if Choice == "leave":
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2) 
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 1) 
            "She leaves the jiz right where it is and gives you a wink."
            if "hand" in newgirl["Laura"].Spunk: 
                    $ newgirl["Laura"].Spunk.remove("hand")
                    if newgirl["Laura"].Swallow:
                        "She does lick off her hand though."
                    else:
                        "She does wipe her hand off though."   
            if "mouth" in newgirl["Laura"].Spunk:                  
                    $ newgirl["Laura"].Spunk.remove("mouth")
            if Cnt:
                    # if this is final clean-up and left the jiz on   
                    $ newgirl["Laura"].RecentActions.append("painted")                  
                    $ newgirl["Laura"].DailyActions.append("painted")                         
            return
            #end "leave it"
              
    $ Cnt = 0
    $ newgirl["Laura"].Spunk.append("hand")
    if "mouth" in newgirl["Laura"].Spunk and Choice != "eat":
            $ newgirl["Laura"].Spunk.remove("mouth")
            "She spits out the spunk in her mouth and dribbling down her chin,"
            $ Cnt += 1
            if "chin" not in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.append("chin")
    if "chin" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("chin")
            if Cnt:            
                "then she wipes the spunk off her chin,"
            else:
                "She wipes the spunk off her chin,"
            $ Cnt += 1
    if "hair" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("hair")
            if Cnt:            
                "then she wipes the spunk out of her hair,"
            else:
                "She wipes the spunk out of her hair,"
            $ Cnt += 1
    if "facial" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("facial")
            if Cnt:
                "then she wipes the spunk off of her face,"   
            else:
                "She wipes the spunk off of her face,"   
            $ Cnt += 1         
    if "tits" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("tits")
            if Cnt:
                "then she wipes the spunk off of her chest,"   
            else:
                "She wipes the spunk off of her chest," 
            $ Cnt += 1           
    if "belly" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("belly")
            if Cnt:
                "then she wipes the spunk off of her belly,"   
            else:
                "She wipes the spunk off her belly," 
            $ Cnt += 1     
    if "in" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("in")
            if Cnt:
                "then she wipes the spunk inside her pussy,"   
            else:
                "She wipes the spunk inside her pussy,"     
            $ Cnt += 1 
    if "anal" in newgirl["Laura"].Spunk and (ApprovalCheck("Laura", 800, "I") or Choice != "eat"):
            while "anal" in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.remove("anal")
            if Cnt:
                "then she wipes the spunk dripping out of her ass,"   
            else:
                "She wipes the spunk dripping our of her ass,"
            $ Cnt += 1            
    if "hand" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("hand")
            if Choice == "eat":                    
                $ newgirl["Laura"].Spunk.append("mouth")
                if Cnt and "anal" in newgirl["Laura"].Spunk:
                    "then licks her hands off with a satisfied grin," 
                if Cnt:
                    "and finally she licks her hands off with a satisfied grin." 
                else:
                    "She licks her hands off with a satisfied grin."   
                    
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2) 
                $ newgirl["Laura"].Spunk.remove("mouth")
                $ newgirl["Laura"].Swallow += 1     
                $ newgirl["Laura"].Addict -= (10*Cnt)
                if newgirl["Laura"].Swallow == 1:
                    $ newgirl["Laura"].SEXP += 12
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 5)
                $ newgirl["Laura"].RecentActions.append("swallowed")                     
                $ newgirl["Laura"].DailyActions.append("swallowed") 
            else:
                if Cnt:
                    "and finally, she wipes her hands off with a nearby tissue." 
                else:
                    "She wipes her hands off with a nearby tissue."                    
            $ Cnt += 1
    if "anal" in newgirl["Laura"].Spunk:
            $ newgirl["Laura"].Spunk.remove("anal")
            if Cnt:
                "Afterward, she wipes the spunk dripping our of her ass."
            else:
                "She wipes the spunk dripping out of her ass."
    $ newgirl["Laura"].Wet = 0        
    $ del newgirl["Laura"].Spunk[:]   
    if Cnt >= 5:
            $ newgirl["Laura"].Eyes = "surprised"
            ch_l "There was a lot more to that than I'd noticed. . ."
            $ newgirl["Laura"].Eyes = "sexy"
    elif Cnt >=3:
            ch_l "You made a real mess there."
    elif Choice == "eat" and newgirl["Laura"].Swallow >= 5:
            ch_l "Mmmm, got any more?"
    return    
    
# End Laura Clean-Up /////////////////////////////////////////////////////////////////////////////////////

