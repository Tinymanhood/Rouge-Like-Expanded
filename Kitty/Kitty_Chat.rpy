
# star Kitty chat interface
label Kitty_Chat:
    call KittyFace 
    call Shift_Focus("Kitty") 
    call Change_Focus("Kitty") 
    
    if K_Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in K_RecentActions:
                ch_k "I'm[K_like]going to keep my distance 'til this blows over."
                return
    if "angry" in K_RecentActions:
                ch_k "I'm[K_like]so mad at you right now!"
                return
    menu:
        ch_k "So[K_like]what did you want to talk about, [K_Petname]?"
        "Come on over." if K_Loc != bg_current:
                    if Room_Full():
                        "It's already pretty crowded here."
                        menu:
                            "Did you want to ask someone to leave?"
                            "Rogue" if R_Loc == bg_current:
                                call Rogue_Dismissed 
                            "Emma" if E_Loc == bg_current:
                                call Emma_Dismissed 
                    else:
                        call Kitty_Summon 

        "Send a dick pic." if K_Loc != bg_current:

                    "You send Kitty a picture of your dick"

                    if K_SEXP < 10:
                            #call KittyFace("surprised", 2) 
                            #$ K_Eyes = "down"
                            ch_k "Wtf dude."  
                            call KittyFace("angry", 1) 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 5) 
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")  
                            #$ renpy.pop_call()
                    elif K_SEXP <= 15:            
                            ch_k "..."
                            #call KittyFace("perplexed", 1) 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 8)
                    elif ApprovalCheck("Kitty", 1200, TabM = 3):
                            #call KittyFace("surprised", 1) 
                            #$ K_Eyes = "down"
                            ch_k "I miss your 8=====D"            
                            #call KittyFace("sly", 1) 
                            call Kitty_Sent_Selfie(1) 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 8)
                    elif ApprovalCheck("Kitty", 500, "I", TabM=2):
                            call KittyFace("surprised", 1) 
                            #$ K_Eyes = "down"
                            #"Kitty glances at it, but just smiles in amusement."
                            ch_k "wow"            
                            call Kitty_Sent_Selfie 

                            #call KittyFace("sly", 1) 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 10)
                    else:
                            #call KittyFace("angry", 1) 
                            #$ K_Eyes = "down"
                            #"Kitty glances down at your cock with a scowl."        
                            #$ K_Eyes = "sexy"                
                            ch_k "I should block you"
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")  
  

        "Ask Kitty to leave" if K_Loc == bg_current:
                    call Kitty_Dismissed 
                    return
        
        "Flirt with her." if not K_Chat[5]:
                    call Kitty_Flirt 
        "Flirt with her. (locked)" if K_Chat[5]:  
                    pass

        "Show me the plug." if K_Plugged:

                    if ApprovalCheck("Kitty", 1450, TabM = 3) or ApprovalCheck("Kitty", 800, "O") or "exhibitionist" in K_Traits: # 145, 160, 175, Taboo -160(355)
                        call KittyFaceSpecial("sexy",1) 
                        ch_k "Ok [K_Petname]."
                        call Kitty_Doggy_Launch("plug") 
                        "Kitty points her ass towards you."
                        #if K_Legs == "skirt" or K_Legs == "skirtshort" or K_Legs == "cheerleader skirt" or K_Legs == "cheerleader skirtshort":
                        if K_Legs:
                            $ K_Upskirt = 1
                            if K_Legs == "orange skirt" or K_Legs == "black skirt" or K_Legs == "white skirt":
                                "Lifts up her skirt."
                            else:
                                "She pulls down her [K_Legs]"
                            pause .1
                            #if K_Hose == "tights":
                            #    $ Temp_K_Hose = K_Hose            
                            #    $ K_Hose = 0
                            #    "And pulls down her tights"
                            #    pause .1
                            #if K_Panties and K_Panties != "lace panties" and K_Panties != "black panties":
                            #    $ K_PantiesDown = 1
                            #    "And pulls down her [K_Panties]"
                            #    pause .1
                            ch_k "There, you happy?"
                            call Kitty_Show_Plug 
                            $ K_PantiesDown = 0
                            pause .1
                            #if Temp_K_Hose:
                            #    $ K_Hose = Temp_K_Hose
                            #    pause .1
                            $ K_Upskirt = 0
                            pause
                        #elif K_Legs == "pants":
                        #    #$ Temp_K_Legs = K_Legs            
                        #    $ K_Upskirt = 1
                        #    #$ K_Legs = 0
                        #    "Kitty pulls down her pants."  
                        #    pause .1
                        #    if K_Panties and K_Panties != "lace panties" and K_Panties != "black panties":
                        #        $ K_PantiesDown = 1
                        #        "And pulls down her [K_Panties]"
                        #        pause .1
                        #    ch_k "There, you happy?"
                        #    pause .1
                        #    call Kitty_Show_Plug
                        #    $ K_PantiesDown = 0
                        #    pause .1
                        #    #$ K_Legs = Temp_K_Legs
                        #    $ K_Upskirt = 0
                        #    pause
                        #elif K_Panties and K_Panties != "lace panties" and K_Panties != "black panties" and K_Panties != "swimsuit1" and K_Panties != "swimsuit2":
                        #    $ K_PantiesDown = 1
                        #    "And pulls down her [K_Panties]"
                        #    ch_k "There, you happy?"
                        #    call Kitty_Show_Plug
                        #    $ K_PantiesDown = 0
                        #    pause
                        else:
                            ch_k "There, you happy?"
                            call Kitty_Show_Plug 
                            pause


                        call Kitty_Doggy_Reset 
                    else:
                        if Taboo:
                            ch_k "Not here [K_Petname]"
                        else:
                            ch_k "No"

        "Take Rogue's clothes off" if R_Loc == bg_current:
                    "Hey, let's prank Rogue, why don't you phase her clothes off?"
                    if ApprovalCheck("Kitty", 600):
                        call KittyFace("sly",0) 
                        ch_k "Hmmm, sounds like a good idea"

                            menu:

                                "Which parts?"
                                
                                "Her top" if R_Over or R_Chest:    
                                    ch_k "Ok"
    
                                    if R_Over:     
                                        $ R_Over = 0
                                    if R_Chest:     
                                        $ R_Chest = 0
                                    if R_BodySuit:
                                        $ R_BodySuit = 0
                
                                    call RogueFace("surprised", 2) 
                                    "Kitty grabs Rogue's clothes and phase them out of Rogue's body using her powers."
                                    $ R_SeenChest += 1 
                                    if not R_Panties and not R_Legs and HoseNum("Rogue") < 10:
                                        $ R_SeenPussy += 1 
                                    
        
                                "Her bottoms" if R_Legs or R_Panties or R_Hose:
                                    ch_k "Ok"
    
                                    if R_Legs:     
                                        $ R_Legs = 0
                                    if R_Panties:     
                                        $ R_Panties = 0
                                    if R_Hose:     
                                        $ R_Hose = 0
                                    if R_BodySuit:
                                        $ R_BodySuit = 0
        
        
                                    call RogueFace("surprised", 2) 
                                    "Kitty grabs Rogue's clothes and phase them out of Rogue's body using her powers."
                                    $ R_SeenPussy += 1 
                                    if not R_Over and not R_Chest:
                                        $ R_SeenChest += 1 

        
                                "Never mind":
                                    pass

                        if not Taboo: #no taboo
                            if "exhibitionist" in R_Traits:
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 4) 
                                call RogueFace("sexy", 1) 
                                ch_r "Oh, naughty, [R_Petname]!"
                                ch_r "You could have just asked, you know. . ."
                                "She looks around taking pleasure at having her body exposed"
                                "And takes her time to put her clothes back on"
                                call RogueFace("smile",1) 
                            elif ApprovalCheck("Rogue", 850, "L"):
                                call RogueFace("sexy", 1) 
                                ch_r "Oh, naughty!"
                                ch_r "You could have just asked, you know. . ."
                            elif ApprovalCheck("Rogue", 700, "L"):
                                call RogueFace("sexy", 1) 
                                ch_r "[R_Petname], Kitty! A little warning!"
                            elif ApprovalCheck("Rogue", 600, "L"):
                                call RogueFace("bemused", 1) 
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -3)           
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)  
                                ch_r "Wha?! [R_Petname], Kitty? . . I don't usually. . ."
                            elif ApprovalCheck("Rogue", 1100):
                                call RogueFace("angry", 1) 
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5)           
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)  
                                ch_r "Wha! [R_Petname]!"
                            else: 
                                ch_r "Nooo!"
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -50) 
                                "With a sudden embarrassed start, Rogue panics. She takes off while trying to cover her naked parts."
                                        
                                call RogueFace("angry", 1) 
                                $ R_RecentActions.append("angry")
                                $ R_DailyActions.append("angry")
                                call AllReset("Rogue") 
                                call Remove_Girl("Rogue") 
                                call RogueOutfit 

                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 7)             
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 3)           
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 4)  
                            
                        else: #taboo
                            if "exhibitionist" in R_Traits:
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 10) 
                                call RogueFace("sexy", 1) 
                                ch_r "Oh, naughty, [R_Petname]!"
                                ch_r "You could have just asked, you know. . ."
                                "She looks around taking pleasure at having her body exposed"
                                "The fact this is a public place gives her even more pleasure"
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 10) 
                                call RogueFace("smile",1) 
                                "Rogue takes her time to put her clothes back on"
                            elif ApprovalCheck("Rogue", 850, "L") and ApprovalCheck("Rogue", 1500):
                                call RogueFace("sexy", 1) 
                                ch_r "Oh, naughty, [R_Petname]!"
                                ch_r "You could have just asked, you know. . ."
                            elif ApprovalCheck("Rogue", 700, "L") and ApprovalCheck("Rogue", 1500):
                                call RogueFace("sexy", 1) 
                                ch_r "[R_Petname], Kitty! A little warning!"
                            elif ApprovalCheck("Rogue", 700, "L"):
                                call RogueFace("bemused", 1) 
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -3)           
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)  
                                ch_r "[R_Petname], Kitty! This isn't the time or place for this!"
                            elif ApprovalCheck("Rogue", 1200):
                                call RogueFace("angry", 1) 
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5)           
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)  
                                ch_r "Wha! [R_Petname]!"
                            else: 
                                ch_r "Nooo!"
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -50) 
                                "With a sudden embarrassed start, Rogue panics. She takes off while trying to cover her naked parts."
                                        
                                call RogueFace("angry", 1) 
                                $ R_RecentActions.append("angry")
                                $ R_DailyActions.append("angry")
                                call AllReset("Rogue") 
                                call Remove_Girl("Rogue") 
                                call RogueOutfit 

                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 7)             
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 4)           
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 4)  
                            call Rogue_First_Bottomless(1) 
                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 1) 
                        #if "exhibitionist" in R_Traits:
                        #End Flip her Skirt   
                        #call AllReset("Rogue")
                        call RogueOutfit 
                        call KittyFace("smile",0) 
                        ch_k "Hahaha, that was funny [K_Petname]"
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 5)

                    else:
                        ch_k "Not happening [K_Petname]"
                        pass
            
        "Sex Menu" if K_Loc == bg_current:
                    if K_Love >= K_Obed:   
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    if "angry" in K_RecentActions:  
                        ch_k "Not even!"
                    elif ApprovalCheck("Kitty", 600, "LI"):
                        call KittyFace("sexy") 
                        ch_k "Mmmm, ok, [K_Petname]."
                        call Kitty_SexMenu 
                        return
                    elif ApprovalCheck("Kitty", 400, "OI"):
                        ch_k "Yes, [K_Petname]."
                        call Kitty_SexMenu 
                        return
                    else:
                        ch_k "No thanks, [K_Petname]."          
                          
        "I just wanted to talk. . .":
                    call Kitty_Chitchat 
                    
        "Kitty's settings":
                    ch_p "Let's talk about you."
                    call Kitty_Settings 
        
        "Relationship status":
                    ch_p "Could we talk about us?"  
                    if "relationship" in K_DailyActions:
                        ch_k "I think we've done enough talking about \"us\" for one day."
                    elif K_Loc == bg_current:
                        call Kitty_Relationship 
                    else:
                        ch_k "That seems like something we'd want to do face to face."
                        ch_k "Maybe later?"
                        
        "Could I get your number?" if "Kitty" not in Digits:
                    if ApprovalCheck("Kitty", 400, "L") or ApprovalCheck("Kitty", 200, "I"):
                        ch_k "OMG[K_like]sure."
                        $ Digits.append("Kitty") 
                    elif ApprovalCheck("Kitty", 200, "O"):
                        ch_k "[K_Like]fine."             
                        $ Digits.append("Kitty")
                    else:
                        ch_k "[K_Like]I'd rather not?"  

        "Remove blindfold" if K_Blindfold:
                    ch_k "Ok"
                    "Her blindfold falls through her"
                    $ K_Blindfold = 0
                        
        "Gifts" if K_Loc == bg_current:
                    ch_p "I'd like to give you something."
                    call Kitty_Gifts 
                        
        "Add her to party" if "Kitty" not in Party and K_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    if ApprovalCheck("Kitty", 650):
                        $ Party.append("Kitty")
                        ch_k "[K_Like]where to?"
                        return
                    elif not ApprovalCheck("Kitty", 400):
                        ch_k "Ew, no."
                    else:
                        ch_k "I think I'll stay here."
        "Disband party" if "Kitty" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Kitty")       
                    call Kitty_Schedule(0) 
                    if K_Loc == bg_current:
                        ch_k "Good to know, but I'm[K_like] fine here."
                    else:
                        ch_k "Cool, later."
                        call Set_The_Scene 
                    return
                
        
        "Date" if Current_Time == "Evening":
                    ch_p "Do you want to go on a date tonight?"
                    call Kitty_Date_Night 

        "Talk with Rogue" if R_Loc == bg_current:
                jump Rogue_Chat

        "Talk with Emma" if E_Loc == bg_current:
                jump Emma_Chat

        "Talk with Mystique" if newgirl["Mystique"].Loc == bg_current:
                jump Mystique_Chat
                
        "Never mind.":
                    return
    jump Kitty_Chat


#Rogue Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Kitty_Relationship:
    menu:
        ch_k "What did you want to talk about?"
        
        "Do you want to be my girlfriend?" if "dating" not in K_Traits and "ex" not in K_Traits:
                $ K_DailyActions.append("relationship")
                if "asked boyfriend" in K_DailyActions and "angry" in K_DailyActions:
                    call KittyFace("angry", 1) 
                    ch_k "For real, buzz off."
                    return
                elif "asked boyfriend" in K_DailyActions:
                    call KittyFace("angry", 1) 
                    ch_k "Still \"nope.\""
                    return
                elif K_Break[0]:                    
                    call KittyFace("angry", 1) 
                    ch_k "Not while you're dating her. . ."
                    if "dating" in R_Traits:   
                        $ K_DailyActions.append("asked boyfriend")                     
                        return
                    elif "ex" in R_Traits:
                        ch_p "I'm not anymore."
                                
                $ K_DailyActions.append("asked boyfriend")
                
                if K_Event[5]:
                    call KittyFace("bemused", 1) 
                    ch_k "I {i}did{/i} ask you about that. . ."
                else:
                    call KittyFace("surprised", 2) 
                    ch_k "I don't know, [K_Petname]. . ." 
                    call KittyFace("smile", 1) 
                
                call Kitty_OtherWoman 
                
                if K_Love >= 800:
                    call KittyFace("surprised", 1) 
                    $ K_Mouth = "smile"
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 40)
                    ch_k "YES!"
                    if "boyfriend" not in K_Petnames:
                        $ K_Petnames.append("boyfriend")                
                    $ K_Traits.append("dating")
                    "Kitty leaps in and kisses you deeply."
                    call KittyFace("kiss", 1) 
                    $ K_Kissed += 1
                elif K_Obed >= 500:
                    call KittyFace("perplexed") 
                    ch_k "Maybe not so much \"dating\". . ."
                elif K_Inbt >= 500:
                    call KittyFace("smile") 
                    ch_k "That's not[K_like]where I'm at right now?"
                else:
                    call KittyFace("perplexed", 1) 
                    ch_k "I don't really feel that way about you right now, [K_Petname]."
                    
        "When you said you loved me. . ." if "lover" not in K_Traits and K_Event[6] >= 20:
                call Kitty_Love_Redux 
        
        "Do you want to get back together?" if "ex" in K_Traits:
                $ K_DailyActions.append("relationship")
                if "asked boyfriend" in K_DailyActions and "angry" in K_DailyActions:
                    call KittyFace("angry", 1) 
                    ch_k "Seriously, buzz off."
                    return
                elif "asked boyfriend" in K_DailyActions:
                    call KittyFace("angry", 1) 
                    ch_k "Still no."
                    return
                elif K_Break[0]: 
                    call KittyFace("angry", 1) 
                    if "dating" in R_Traits:   
                        ch_k "Not while you're with her."
                        return
                    elif "ex" in R_Traits:
                        ch_k "Not while you're with her."
                        ch_p "I'm not anymore."
                        $ K_Break[0] = 0
                    else:    
                        if not ApprovalCheck("Kitty", 1500) or K_Break[1] > 5:
                            ch_k "Give it a rest."
                        else:
                            call KittyFace("sad", 1) 
                            ch_k "Too soon."
                        $ K_DailyActions.append("asked boyfriend")
                        return
                
                $ K_DailyActions.append("asked boyfriend")
                
                $ Cnt = 0
                call Kitty_OtherWoman 
                                        
                if K_Love >= 800:
                    call KittyFace("surprised", 1) 
                    $ K_Mouth = "smile"
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
                    ch_k "Well, I guess, sure!"
                    if "boyfriend" not in K_Petnames:
                        $ K_Petnames.append("boyfriend")                
                    $ K_Traits.append("dating")          
                    $ K_Traits.remove("ex")
                    "Kitty leaps in and kisses you deeply."
                    call KittyFace("kiss", 1) 
                    $ K_Kissed += 1
                elif K_Love >= 600 and ApprovalCheck("Kitty", 1500):
                    call KittyFace("smile", 1) 
                    $ K_Mouth = "smile"
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
                    ch_k "Um, ok, I guess."
                    if "boyfriend" not in K_Petnames:
                        $ K_Petnames.append("boyfriend")                
                    $ K_Traits.append("dating")             
                    $ K_Traits.remove("ex")
                    "Kitty gives you a quick kiss."
                    call KittyFace("kiss", 1) 
                    $ K_Kissed += 1
                elif K_Obed >= 500:
                    call KittyFace("sad") 
                    ch_k "I think we're better like this."   
                elif K_Inbt >= 500:
                    call KittyFace("perplexed") 
                    ch_k "I kind of like what we have right now."
                else:
                    call KittyFace("perplexed", 1) 
                    ch_k "I'm not ready to get burned again."
                
        # End Back Together
                    
                               
#        "I think we should break up." if "dating" in R_Traits: #ApprovalCheck("Rogue", 950, "L", Bonus = (B/3)):
#            if "breakup talk" in R_RecentActions:
#                ch_r "We were {i}just{/i} over this, not even funny."
#            elif "breakup talk" in R_DailyActions:
#                ch_r "Tired of me again that quick?" 
#                ch_r "We're not having this talk today, [R_Petname]."
#            else:
#                call Rogue_Breakup                
            
            
#        "I'd like to bring Kitty into this." if "poly kitty" not in R_Traits and not K_Break[0]:    #fix nonfunctional yet, switch over to Kitty stuff
            
#            if "asked threesome" in R_RecentActions:
#                ch_r "Persistence will NOT be rewarded here."
#                return
#            elif "asked threesome" in R_DailyActions:
#                ch_r "I don't think my answer's changing any time soon." 
#                return
#            else:
#                $ R_DailyActions.append("asked threesome")                
#                $Cnt = int((R_LikeKitty - 500)/2)
#                menu:
#                    ch_r "What does she think about this?"
                        
#                    "She said I can be with you too." if "poly rogue" in K_Traits:
#                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
#                            call RogueFace("smile", 1)
#                            if R_Love >= R_Obed:
#                                ch_r "Just so long as we can be together, I can share."
#                            elif R_Obed >= R_Inbt:
#                                ch_r "I'm ok with that if she is."
#                            else:
#                                ch_r "Yeah, I mean I guess so."
#                                $ R_Traits.append("poly kitty")
#                        else:
#                            call RogueFace("angry", 1)
#                            ch_r "Well maybe she did, but I don't want to share."  
                    
#                    "I could ask if she'd be ok with me dating you both." if "poly rogue" not in K_Traits:
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
#                        if R_LikeKitty >= 700:
#                            ch_r "I have to say I've kind of been thinking about it myself."  
#                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
#                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
#                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
#                        elif R_LikeKitty >= 500:
#                            ch_r "I guess, if that's what you want. . ." 
#                        elif R_Obed >= 700:
#                            ch_r "If that's what you want. . ." 
#                        else:
#                            ch_r "I can't really stand her, I don't think so."  
                            
                        
#                    "You're right, I was dumb to ask.":
#                        call RogueFace("sad")
#                        ch_r "Yeah, you were."  
                        
            #end Kitty Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in K_Petnames and "sir" in K_History:
                if "asked sub" in K_RecentActions:
                        ch_k "We[K_like]{i}just{/i} went over this."
                elif "asked sub" in K_DailyActions:
                        ch_k "I think you made yourself {i}perfectly{/i} clear earlier. . ."            
                else:
                        call Kitty_Sub_Asked 
        "You said you wanted me to be your Master?" if "master" not in K_Petnames and "master" in K_History:
                if "asked sub" in K_RecentActions:
                        ch_k "We[K_like]{i}just{/i} went over this."
                elif "asked sub" in K_DailyActions:
                        ch_k "I think you made yourself {i}perfectly{/i} clear earlier. . ."            
                else:
                        call Kitty_Sub_Asked 
                        
        "Never Mind":
            return
              
    return

label Kitty_OtherWoman:
    $ Cnt = 0
    if "dating" in R_Traits:
        call KittyFace("perplexed") 
        menu: 
            ch_k "But you're with Rogue right now."
            "She said I can be with you too." if "poly kitty" in R_Traits:
                $Cnt = int((K_LikeRogue - 500)/2)
                if ApprovalCheck("Kitty", 1800, Bonus = Cnt):
                    call KittyFace("smile", 1) 
                    if K_Love >= K_Obed:
                        ch_k "Just so long as we can be together, I can share."
                    elif K_Obed >= K_Inbt:
                        ch_k "I'm ok with that if she is."
                    else:
                        ch_k "Yeah, I mean I guess so."
                        $ K_Traits.append("poly rogue")
                else:
                    call KittyFace("angry", 1) 
                    ch_k "Well maybe she did, but I don't want to share."  
                    $ renpy.pop_call()                                          #This causes it to jump past the previous menu on the return
            
            "I could ask if she'd be ok with me dating you both." if "poly kitty" not in R_Traits:
                $Cnt = int((K_LikeRogue - 500)/2)
                if ApprovalCheck("Kitty", 1800, Bonus = Cnt):
                    call KittyFace("smile", 1) 
                    if K_Love >= K_Obed:
                        ch_k "Just so long as we can be together, I can share."
                    elif K_Obed >= K_Inbt:
                        ch_k "I'm ok with that if she is."
                    else:
                        ch_k "Yeah, I mean I guess so."                        
                    ch_k "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call KittyFace("angry", 1) 
                    ch_k "Well maybe she would, but I don't want to share."      
                $ renpy.pop_call()
            
            "What she doesn't know won't hurt her.":
                $Cnt = int((K_LikeRogue - 500)/2)
                if not ApprovalCheck("Kitty", 1800, Bonus = -(int((K_LikeRogue - 600)/2))): #checks if Rogue likes you more than Kitty
                    call KittyFace("angry", 1) 
                    if not ApprovalCheck("Kitty", 1800):
                        ch_k "Well I don't like you that much either."
                    else:
                        ch_k "Well I'm not cool with that, Rogue's a friend of mine."                    
                    $ renpy.pop_call() 
                    
                else:
                    call KittyFace("smile", 1) 
                    if K_Love >= K_Obed:
                        ch_k "I really do want to be together with you."
                    elif K_Obed >= K_Inbt:
                        ch_k "If that's how you want it to be."
                    else:
                        ch_k "I suppose that's true."
                    $ K_Traits.append("poly rogue")
                    $ K_Traits.append("downlow")
                
            "I can break it off with her.":
                call KittyFace("sad") 
                ch_k "Well then maybe I'll see you tomorrow after you have."                                   
                $ renpy.pop_call()
                
            "You're right, I was dumb to ask.":
                call KittyFace("sad") 
                ch_k "We had a good thing there. Maybe some day. . ."                    
                $ renpy.pop_call()   

    if "dating" in E_Traits:
        call KittyFace("perplexed") 
        menu: 
            ch_k "But you're with Emma right now."
            "She said I can be with you too." if "poly kitty" in E_Traits:
                $Cnt = int((K_LikeEmma - 500)/2)
                if ApprovalCheck("Kitty", 1800, Bonus = Cnt):
                    call KittyFace("smile", 1) 
                    if K_Love >= K_Obed:
                        ch_k "Just so long as we can be together, I can share."
                    elif K_Obed >= K_Inbt:
                        ch_k "I'm ok with that if she is."
                    else:
                        ch_k "Yeah, I mean I guess so."
                        $ K_Traits.append("poly emma")
                else:
                    call KittyFace("angry", 1) 
                    ch_k "Well maybe she did, but I don't want to share."  
                    $ renpy.pop_call() 

            "I could ask if she'd be ok with me dating you both." if "poly kitty" not in E_Traits:
                $Cnt = int((K_LikeEmma - 500)/2)
                if ApprovalCheck("Kitty", 1800, Bonus = Cnt):
                    call KittyFace("smile", 1) 
                    if K_Love >= K_Obed:
                        ch_k "Just so long as we can be together, I can share."
                    elif K_Obed >= K_Inbt:
                        ch_k "I'm ok with that if she is."
                    else:
                        ch_k "Yeah, I mean I guess so."                        
                    ch_k "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call KittyFace("angry", 1) 
                    ch_k "Well maybe she would, but I don't want to share."      
                $ renpy.pop_call()
            
            "What she doesn't know won't hurt her.":
                $Cnt = int((K_LikeEmma - 500)/2)
                if not ApprovalCheck("Kitty", 1800, Bonus = -(int((K_LikeEmma - 600)/2))): #checks if Emma likes you more than Kitty
                    call KittyFace("angry", 1) 
                    if not ApprovalCheck("Kitty", 1800):
                        ch_k "Well I don't like you that much either."
                    else:
                        ch_k "Well I'm not cool with that, Emma's a friend of mine."                    
                    $ renpy.pop_call() 
                    
                else:
                    call KittyFace("smile", 1) 
                    if K_Love >= K_Obed:
                        ch_k "I really do want to be together with you."
                    elif K_Obed >= K_Inbt:
                        ch_k "If that's how you want it to be."
                    else:
                        ch_k "I suppose that's true."
                    $ K_Traits.append("poly emma")
                    $ K_Traits.append("downlow")
                
            "I can break it off with her.":
                call KittyFace("sad") 
                ch_k "Well then maybe I'll see you tomorrow after you have."                                   
                $ renpy.pop_call()
                
            "You're right, I was dumb to ask.":
                call KittyFace("sad") 
                ch_k "We had a good thing there. Maybe some day. . ."                    
                $ renpy.pop_call()                   
                
    return
    
label Kitty_Settings:
    menu:
        "Wardrobe": 
                ch_p "I wanted to talk about your style."
                if K_Loc != "bg player" and K_Loc != "bg kitty":  
                    if Taboo:
                        if "exhibitionist" in K_Traits:
                            ch_k "Mmmmm. . ."  
                        elif ApprovalCheck("Kitty", 900, TabM=4) or ApprovalCheck("Kitty", 400, "I", TabM=3): 
                            ch_k "This is[K_like]pretty. . . exposed. . ."
                        else:
                            ch_k "This is[K_like]pretty exposed, right?"
                            ch_k "Can't we talk about this in our rooms?"
                            return
                    call Kitty_Clothes 
                elif ApprovalCheck("Kitty", 600, "L") or ApprovalCheck("Kitty", 300, "O"):
                    ch_k "[K_Like]what were you thinking here?"
                    call Kitty_Clothes 
                else:
                    ch_k "I'll let you know when I care what you think."

        "Wear this vibrator to class" if "vibeclass" not in K_Traits:
                if "exhibitionist" in K_Traits:
                    call KittyFaceSpecial("sexy",1) 
                    ch_k "Oooh, naughty. . ."  
                elif ApprovalCheck("Kitty", 1000, TabM=3) or ApprovalCheck("Kitty", 800, "I") or ApprovalCheck("Kitty", 750, "O"): 
                    call KittyFaceSpecial("surprised",1) 
                    ch_k "Well, I mean, yeah, I guess I could. . ."
                else:
                    call KittyFaceSpecial("angry",1) 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5) 
                    ch_k "You wish."
                    return
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 5) 
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5) 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 5) 
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5) 
                $ K_Traits.append("vibeclass")
                
        "Don't wear the vibrator to class" if "vibeclass" in K_Traits:
                ch_k "Ok"
                $ K_Traits.remove("vibeclass")
                
        "Shift her Personality" if ApprovalCheck("Kitty", 900, "L", TabM=0) or ApprovalCheck("Kitty", 900, "O", TabM=0) or ApprovalCheck("Kitty", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Kitty_Personality 
            
        "Your Pet Name":
            ch_p "Could we talk about my pet name?"
            if ApprovalCheck("Kitty", 600, "L", TabM=0) or ApprovalCheck("Kitty", 300, "O", TabM=0):
                call Kitty_Names 
            else:
                $ K_Mouth = "smile"
                ch_k "It's your name, [K_Petname]."
                
        "Her Pet Name":
                ch_p "I've got a pet name for you, you know?"
                if ApprovalCheck("Kitty", 600, "L", TabM=0):
                    ch_k "[K_Like]tell me!" 
                elif ApprovalCheck("Kitty", 300, "O", TabM=0):
                    ch_k "What did you want to call me?"
                else:
                    ch_k "I bet it's a great one. . ."            
                call Kitty_Pet 
        
        "\"Like\" options":    
                ch_p "So you[K_like]say \"[K_like]\" a lot. . ."      
                if ApprovalCheck("Kitty", 800):
                    call KittyLike 
                else:
                    ch_k "[K_Like]what's it to you?"

        "Stop sending me nudes" if K_Nudes == 1:
                $ K_Nudes = 0
                ch_k "Ok"
        
        "Send me nudes" if K_Nudes == 0:
                $ K_Nudes = 1
                ch_k "Ok"                
            
        "Other girls":
                menu:
                    ch_p "How do you feel about. . ."
                    "Rogue?":
                        call Kitty_AboutRogue 
                    "Never mind.":
                        pass
            
        "Follow options" if "follow" in K_Traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_k "Yeah?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in K_Traits:
                        call KittyFace("perplexed") 
                        ch_k "Um[K_like]okay."
                        if "follow" not in K_DailyActions:
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -2)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 5) 
                        $ K_Traits.append("freetravels")
                        $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in K_Traits:
                        call KittyFace("perplexed") 
                        ch_k "Um[K_like]okay."
                        if "follow" not in K_DailyActions:
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 2) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2) 
                        $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in K_Traits:
                        if ApprovalCheck("Kitty", 500, "O") or ApprovalCheck("Kitty", 900, "L"):   
                            call KittyFace("smile") 
                            ch_k "Aw, you miss me when I'm not around!"
                            if "follow" not in K_DailyActions:
                                if K_Love > 90:
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 99, 2)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 5)                             
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -5, 1) 
                            $ Line = "lock"
                        else:
                            call KittyFace("angry") 
                            ch_k "Well, who cares what you think?"
                            
                    "Never mind.":
                        ch_k "Ooookay."
                        
                if Line:
                    $ K_DailyActions.append("follow")                
                    if "freetravels" in K_Traits:
                        $ K_Traits.remove("freetravels") 
                    if "asktravels" in K_Traits:
                        $ K_Traits.remove("asktravels") 
                    if "lockedtravels" in K_Traits:
                        $ K_Traits.remove("lockedtravels") 
                
                    if Line == "free":
                        $ K_Traits.append("freetravels")            
                    elif Line == "ask":
                        $ K_Traits.append("asktravels")                
                    elif Line == "lock":
                        $ K_Traits.append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in K_DailyActions and "no ask gym" not in K_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_k "Ok, thanks."
                    $ K_Traits.append("no ask gym")
        "Gym clothes" if "no ask gym" in K_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."   
                    ch_k "Fine, whatever."
                    $ K_Traits.remove("no ask gym")
                    
        "Tasks" if "sir" in K_Petnames:
                ch_p "I have some tasks for you."
                call Kitty_Controls 
            
        "Never mind.":
            return  
    return

# End Kitty Chat



## Kitty Chitchat /////////////////// #Work in progress
label Kitty_Chitchat(O=0, Options = ["default","default","default"]):
    if O:                                               #adds only a specific option that was sent
        $ Options [O]
    else:
        
        if "Kitty" not in Digits:
                if ApprovalCheck("Kitty", 500, "L") or ApprovalCheck("Kitty", 250, "I"):
                    ch_k "You know, I never got around to giving you my number, here you go."
                    $ Digits.append("Kitty")  
                    return
                elif ApprovalCheck("Kitty", 250, "O"):
                    ch_k "You know, you should probably have my number, here you go."             
                    $ Digits.append("Kitty")
                    return
                
        if "hungry" not in K_Traits and (K_Swallow + K_Chat[2]) >= 10 and K_Loc == bg_current:  #She's swallowed a lot        
                call Kitty_Hungry 
                return  
        
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in K_DailyActions:
#            $ Options.append("caught")
        if K_Event[0] and "key" not in K_Chat:
            $ Options.append("key")
        if "lover" in K_Petnames and ApprovalCheck("Kitty", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in K_DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in K_DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in K_DailyActions:
            $ Options.append("corruption")
        
        if K_Date >= 1:
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in K_DailyActions and "cheek" not in K_Chat:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if K_Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in K_DailyActions:
            #If you've caught Kitty showering today
            $ Options.append("showercaught")
        if "fondle breasts" in K_DailyActions or "fondle pussy" in K_DailyActions or "fondle ass" in K_DailyActions:
            #If you've fondled Kitty today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in K_Inventory and "256 Shades of Grey" in K_Inventory and "Avengers Tower Penthouse" in K_Inventory:   
            #If you've given Kitty the books
            if "book" not in K_Chat:
                $ Options.append("booked")
        if "lace bra" in K_Inventory or "lace panties" in K_Inventory:   
            #If you've given Kitty the lingerie
            if "lingerie" not in K_Chat:
                $ Options.append("lingerie")
        if K_Hand:   
            #If Kitty's given a handjob
            $ Options.append("handy")
        if K_Swallow:   
            #If Kitty's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in K_DailyActions or "painted" in K_DailyActions:
            #If Kitty's been facialed
            $ Options.append("facial")
        if K_Sleep:
            #If Kitty's slept over
            $ Options.append("sleep")
        if K_CreamP or K_CreamA:
            #If Kitty's been creampied
            $ Options.append("creampie")
        if K_Sex or K_Anal:
            #If Kitty's been sexed
            $ Options.append("sexed")
        if K_Anal:
            #If Kitty's been analed
            $ Options.append("anal")
            
#        if not K_Chat[0] and K_Sex:
#            $ Options.append("virgin")    
            
        if (bg_current == "bg kitty" or bg_current == "bg player") and "relationship" not in K_DailyActions:
            if "boyfriend" not in K_Petnames and ApprovalCheck("Kitty", 750, "L"): # K_Event[5]
                $ Options.append("boyfriend?")
#            elif "lover" not in K_Petnames and ApprovalCheck("Kitty", 900, "L"): # K_Event[6]        
#                $ Options.append("lover?")
            elif "sir" not in K_Petnames and ApprovalCheck("Kitty", 500, "O"): # K_Event[7]
                $ Options.append("sir?")      
#            elif "daddy" not in K_Petnames and ApprovalCheck("Kitty", 750, "L") and ApprovalCheck("Kitty", 500, "O") and ApprovalCheck("Kitty", 500, "I"): # K_Event[5]
#                $ Options.append("daddy?")
            elif "master" not in K_Petnames and ApprovalCheck("Kitty", 900, "O"): # K_Event[8]
                $ Options.append("master?")
#            elif "sex friend" not in K_Petnames and ApprovalCheck("Kitty", 500, "I"): # K_Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in K_Petnames and ApprovalCheck("Kitty", 900, "I"): # K_Event[10]
#                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Kitty", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ K_DailyActions.append("cologne chat") 
        call KittyFace("confused") 
        ch_k "(sniff, sniff). . . is that. . . chimp? . . ."
        call KittyFace("perplexed", 1) 
        ch_k ". . . but it's[K_like]. . . {i}sexy{/i} chimp?"    
    elif Options[0] == "purple":              
        $ K_DailyActions.append("cologne chat") 
        call KittyFace("sly",1) 
        ch_k "(sniff, sniff). . . huh, what's that smell? . ."
        ch_k ". . . could I get you something?"    
    elif Options[0] == "corruption":              
        $ K_DailyActions.append("cologne chat") 
        call KittyFace("confused") 
        ch_k "(sniff, sniff). . . that's pretty overpowering. . ."
        call KittyFace("sly") 
        ch_k ". . . I may not be able to keep my hands to myself. . ."
                
    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in K_Chat:
                    ch_k "We've really got to stop making a habit of getting caught."
                    if not ApprovalCheck("Kitty", 500, "I"):
                         ch_k "Or not. . ."
            else:    
                    ch_k "I did not enjoy getting dragged to the Professor's office like that."
                    if not ApprovalCheck("Kitty", 500, "I"):
                        ch_k "I don't know about doing it in public anymore."
                    else:
                        ch_k "It was kind of hot though. . ."
                    $ K_Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            $ Line = "I'm glad you have my key now,"
            if K_SEXP <= 15:
                $ Line = Line + " just don't use it for any funny business. . ."
            else:
                $ Line = Line + " maybe you could . . . \"surprise\" me sometime. . ."
            ch_k "[Line]"
            $ K_Chat.append("key") 
        
    elif Options[0] == "cheek":
            #Kitty's response to having her cheek touched.
            ch_k "So,[K_Petname]. . .y'know how you[K_like]kinda just brushed my cheek before?"
            ch_p "Yeah?  Was that okay?"
            call KittyFace("smile",1) 
            ch_k "More than just {i}okay{/i}."
            $ K_Chat.append("cheek") 
            
    elif Options[0] == "dated":
            #Kitty's response to having gone on a date with the Player.
            ch_k "Heya,[K_Petname].  I[K_like]had a lot of fun last night.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Kitty's response to having been kissed by the Player.
            call KittyFace("sly",1) 
            ch_k "[K_Like]. . .anybody ever tell you how good a kisser you are, [K_Petname]?"
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        call KittyFace("smile",1) 
                        ch_k "I think maybe you can show me {i}how{/i} good[K_like]whenever you want."
                "No. You think?":
                        ch_k "Yeah.  I do. [K_Like]a {i}lot{/i}."

    elif Options[0] == "dangerroom":
            #Kitty's response to Player working out in the Danger Room while Kitty is present
            call KittyFace("sly",1) 
            ch_k "Hey,[K_Petname].  I watched you working out in the Danger Room, earlier.  You looked[K_like]{i}so{/i} cute in your X-Men uniform!"

    elif Options[0] == "showercaught":
            #Kitty's response to being caught in the shower.
            if "shower" in K_Chat: 
                ch_k "Hope you liked the view earlier. . ."                       
            else:
                ch_k "So, you run into a lot of people in the shower. . .or just[K_like]me?"            
                $ K_Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 5)    
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2) 
                            if ApprovalCheck("Kitty", 1200):
                                call KittyFace("sly",1) 
                                ch_k "Yeah?  {i}Maybe{/i} you should[K_like]have accidents like that more often."
                            call KittyFace("smile") 
                            ch_k "It's cool, [K_Petname]. Eveybody makes mistakes. . . sometimes."
                    "Just you.":        
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 5)   
                            if ApprovalCheck("Kitty", 1000) or ApprovalCheck("Kitty", 700, "L"):      
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3)    
                                    call KittyFace("sly",1) 
                                    ch_k "You know how to make a girl feel special, [K_Petname]."
                            else:                
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5) 
                                    call KittyFace("angry") 
                                    ch_k "You're {i}such{/i} a creep, [Playername], y'know that?"                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Kitty", 1200):                     
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3)          
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5) 
                                    call KittyFace("sly",1) 
                                    ch_k "Hmm. . .next time, we'll have to[K_like]take advantage of the moment."
                            elif ApprovalCheck("Kitty", 800):                          
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 5)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5) 
                                    call KittyFace("perplexed",2) 
                                    ch_k "Wha. . . um. . . okay?"
                                    $ K_Blush = 1
                            else:                
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10) 
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10)          
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)  
                                    call KittyFace("angry") 
                                    ch_k "You're such a creep, [K_Petname], y'know that?"

    elif Options[0] == "fondled":
            #Kitty's response to being felt up.
            if K_FondleB + K_FondleP + K_FondleA >= 15:
                ch_k "I want your hands on me." 
            else:                
                ch_k "You know how you felt me up earlier?  I could kinda[K_like]get used to having your hands on me."

    elif Options[0] == "booked":
            #Kitty's response after a Player gives her the books from the shop.
            ch_k "So..I[K_like]read the books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        call KittyFace("sly",2) 
                        ch_k "They were[K_like]. . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":                     
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 5)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5) 
                        call KittyFace("angry") 
                        ch_k "Guess {i}you'll{/i} never find out, huh?"                
            $ K_Blush = 1
            $ K_Chat.append("book") 

    elif Options[0] == "lingerie":
            #Kitty's response to being given lingerie.
            call KittyFace("sly",2) 
            ch_k "[K_Petname], I wanted to thank you again for the. . .{i}stuff{/i} you bought me.  They're so cute!"
            $ K_Blush = 1
            $ K_Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Kitty's response after giving the Player a handjob.
            call KittyFace("sly",2) 
            ch_k "I was just thinking about how I[K_like]stroked your cock the other day. . ."
            ch_k "I loved the expression on your face. . .knowing I could[K_like]make you {i}feel{/i} like that."
            $ K_Blush = 1

    elif Options[0] == "blow":
            if "blow" not in K_Chat:
                    #Kitty's response after giving the Player a blowjob.
                    call KittyFace("sly",2) 
                    ch_k "So. . .uhm, be honest with me, [K_Petname]?"
                    ch_k "When I gave you head. . . was it any good?"
                    ch_k "I kinda had a hard time getting all of you into my mouth."
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 10) 
                                    call KittyFace("sexy",1) 
                                    ch_k "Awesome.  'Cause I can't wait to try again."
                        "Honest? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck("Kitty", 300, "I") or not ApprovalCheck("Kitty", 800):                     
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 10)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10) 
                                    call KittyFace("perplexed",1) 
                                    ch_k "Yeah?  Well then maybe I'll get some practice in before we do it again."
                                else:                              
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 15)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5) 
                                    call KittyFace("sexy",1) 
                                    ch_k "Yeah?  Well, I'm[K_Petname]looking forward our next training session, then."                                    
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 10)   
                                call KittyFace("angry",2) 
                                ch_k "Guess you're gonna have to[K_like]figure out a way to get it to suck itself then from now on. . .{i}jerk{/i}."
                    $ K_Blush = 1
                    $ K_Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["You know, I kinda like how you taste.", 
                            "You're a real jaw-breaker.", 
                            "Let me know if you want some more lollipop licks.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_k "[Line]"

    elif Options[0] == "swallowed":
            #Kitty's response after swallowing the Player's cum.
            if "swallow" in K_Chat:                
                ch_k "I'd like another taste sometime."
            else:
                ch_k "So. . .I was[K_like]just thinking about the other day.  Y'know, that was the first time I[K_like]swallowed."
                call KittyFace("sly",1) 
                ch_k "Not bad. . ."
                $ K_Chat.append("swallow") 

    elif Options[0] == "facial":
            #Kitty's response after taking a facial from the Player.
            ch_k "Hey. . .this is gonna sound kinda[K_like]weird, but. . ."
            call KittyFace("sexy",2) 
            ch_k "I feel so {i}sexy{/i} when you cum on my face."
            $ K_Blush = 1

    elif Options[0] == "sleepover":
            #Kitty's response after sleeping with the Player.
            ch_k "I[K_like] totally can't stop thinking about the other night.  It was {i}so{/i} perfect."

    elif Options[0] == "creampie":
            #Another of Kitty's responses after having sex with the Player.
            "Kitty draws close to you so she can whisper into your ear."
            ch_k "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Kitty after having sex with the Player.
            ch_k "So. . .I want you to know something. . ."
            call KittyFace("sexy",2) 
            ch_k ". . .[K_Like]every time I masturbate. . ."
            ch_k "I think about how it felt, with you inside of me."
            $ K_Blush = 1

    elif Options[0] == "anal":
            #Kitty's response after getting anal from the Player.
            call KittyFace("sly",2) 
            ch_k "Y'know. . .after the other night, I'm kinda having trouble[K_like]sitting down."
            call KittyFace("sexy",2) 
            ch_k "{i}Totally{/i} worth it, though."
            $ K_Blush = 1
        
    elif Options[0] == "boyfriend?":
        call Kitty_BF 
#    elif Options[0] == "lover?":
#        call Kitty_Love
    elif Options[0] == "sir?":
        call Kitty_Sub 
    elif Options[0] == "master?":
        call Kitty_Master 
#    elif Options[0] == "sexfriend?":
#        call Kitty_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Kitty_Fuckbuddy 
#    elif Options[0] == "daddy?":
#        call Kitty_Daddy  
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to see your face.", 
                "Stop bothering me.",
                "Leave me alone."])
        ch_k "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    call KittyFace("smile") 
                    ch_k "I'm[K_like]{i}so{/i} excited [K_Petname]! I {i}totally{/i} aced Professor McCoy's Computer Science test!"
            elif D20 == 2:
                    call KittyFace("down") 
                    ch_k "Ever have[K_like]one of those days where it seems like the whole world's out to get you?"
            elif D20 == 3:
                    call KittyFace("surprised") 
                    ch_k "I can't believe how much stuff I've gotta get done today!"
            elif D20 == 4:
                    call KittyFace("down") 
                    ch_k "Hey, [K_Petname]. I got[K_like]the world's worst sleep last night. I feel like I could[K_like]curl up and go to bed right here."
            elif D20 == 5:
                    call KittyFace("smile") 
                    ch_k "Wow! Isn't it[K_like]{i}so{/i} nice out right now?"
            elif D20 == 6:
                    call KittyFace("startled") 
                    ch_k "I had[K_like]the worst nightmare last night. I dreamed the N'Garai demon was chasing me throught the Mansion!"
            elif D20 == 7:
                    call KittyFace("smile") 
                    ch_k "So awesome. I have[K_like]a lunch date tomorrow with my total bestie!"
            elif D20 == 8:
                    call KittyFace("sad") 
                    ch_k "Y'know, I totally love it here in Salem Center. But I have to admit. . .I kinda miss Deerfield sometimes."
            elif D20 == 9:
                    call KittyFace("confused") 
                    ch_k "So weird. Ever since Professor Xavier telepathically taught me Russian, I kinda find myself[K_like]daydreaming in Cyrillic."
            elif D20 == 10:
                    call KittyFace("smile") 
                    ch_k "{i}So{/i} nerdy, I know. But I[K_like]totally had the best idea for this OS I'm writing for the Mansion's computers in the shower today!"
            elif D20 == 11:
                    call KittyFace("smile") 
                    ch_k "I[K_like]totally can't wait 'til dance class tomorrow! We're starting modern this semester!"
            elif D20 == 12:
                    call KittyFace("down") 
                    ch_k "I heard a few of the others are going to Harry's Hideaway tomorrow. I have[K_like]{i}so{/i}much homework to do, though!"
            elif D20 == 13:
                    call KittyFace("smile") 
                    ch_k "This probably sounds[K_like]totally random, but, I could {i}so{/i} go for ice cream right now!"
            elif D20 == 14:
                    call KittyFace("sad") 
                    ch_k "I hate thinking about how so many people[K_like]totally hate mutants for no good reason. It's so depressing."
            elif D20 == 15:
                    call KittyFace("startled") 
                    ch_k "I think I[K_like]tweaked something in my thigh in the Danger Room, yesterday. It feel like I have a bruise that goes right through it!"
            else:
                    call KittyFace("startled") 
                    ch_k "You're fun to hang with."
        
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Kitty_Flirt:
    
    if K_Loc == bg_current:         
        $ K_Chat[5] = 1                                         #can only flirt once per cycle. 
        menu:        
#            "Compliment her":
                
#            "Say you love her":
                
            "Touch her cheek.":                                                                                 #Touch her cheek 
                    call K_TouchCheek 
                            
            "Kiss her cheek":                                                                                   #Kiss her cheek
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Kitty", 700, "L", TabM=1):
                        call KittyFace("sexy", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2) 
                        ch_k ". . ."
                        ch_k "Wow."
                    elif ApprovalCheck("Kitty", 500, "L", TabM=1):
                        call KittyFace("surprised", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 2)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, 1) 
                        ch_k ". . . hey! What's the deal?"
                    elif ApprovalCheck("Kitty", 300, "L", TabM=1):                    
                        call KittyFace("angry", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -1)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 1) 
                        ch_k "I don't[K_like]like you like that?"
                    else: 
                        call KittyFace("angry", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 5)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 3) 
                        ch_k "Keep off me!"
                    if "addict kitty" in P_Traits:
                        $ K_Addict -= 1
                        $ K_Addictionrate += 1
                        $ K_Addictionrate = 3 if K_Addictionrate < 3 else K_Addictionrate 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Kitty", 1000, TabM=1) or ApprovalCheck("Kitty", 600, "L", TabM=1):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Kitty", 1000) or ApprovalCheck("Kitty", 600, "L"):  
                        call KittyFace("bemused", 1) 
                        $ K_Eyes = "side"         
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -5)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                        "You lean close for a kiss, but Kitty gently elbows your ribs."
                        ch_k "Not in public, [K_Petname]." 
                        return
                    else:                
                        call KittyFace("angry", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -15)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -5)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 5) 
                        "You lean close for a kiss, but Kitty gently elbows your ribs."
                        ch_k "Keep your distance, [K_Petname]." 
                        return
                    if K_Kissed:
                            if ApprovalCheck("Kitty", 800, "L", TabM=1):
                                call KittyFace("sexy", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                                ch_k "Mmmmmmm. . ."
                            elif ApprovalCheck("Kitty", 700, "L", TabM=1):
                                call KittyFace("sexy", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2) 
                                ch_k "Hmm, \"hello\"to you too, [K_Petname]?"
                            elif ApprovalCheck("Kitty", 550, "L", TabM=1):
                                call KittyFace("surprised", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2) 
                                ch_k "That's[K_like]a bit forward?"
                            elif ApprovalCheck("Kitty", 300, "L", TabM=1):
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -8)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 3)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                                ch_k "Dude!"
                            else: 
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -15)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 6)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 3) 
                                ch_k "Back off, [K_Petname]."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Kitty", 800, "L", TabM=1):
                                call KittyFace("surprised", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 30)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 15)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 15)
                                ch_k ". . ."
                                ch_k "Hmmm, that was nice. . ."
                                call KittyFace("sexy") 
                                ch_k "Let me know if you want to do that again, [K_Petname]."
                            elif ApprovalCheck("Kitty", 650, "L", TabM=1):
                                call KittyFace("surprised", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 25)            
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 20)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 15)
                                ch_k "Huh?"
                                ch_k "I, um[K_like]don't know what to do with that. . ."
                            elif ApprovalCheck("Kitty", 500, "L", TabM=1):
                                call KittyFace("surprised", 1) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 20)
                                ch_k "What's the deal, [K_Petname]?!"
                            elif ApprovalCheck("Kitty", 800, TabM=1):
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -10) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 20)
                                ch_k "the hell, [K_Petname]?!"
                            else: 
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -15) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 40)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 25)
                                ch_k "[K_Like]WTF?!"
                            
                    $ K_Kissed += 1  
                    if "addict kitty" in P_Traits:
                        $ K_Addict -= 1
                        $ K_Addictionrate += 1
                        $ K_Addictionrate = 3 if K_Addictionrate < 3 else K_Addictionrate 
                        
                    if ApprovalCheck("Kitty", 700, TabM=1):
                        if K_Love > K_Obed and K_Love > K_Inbt:
                            ch_k "More smooches, [K_Petname]!"
                        elif K_Obed > K_Inbt:
                            ch_k "I'd be open to more if you are."
                        else:
                            ch_k "We could keep going, [K_Petname]."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3)  
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, 3) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                                call Kitty_SexAct("kissing") 
                                return
                            "Not now [[no].":
                                call KittyFace("bemused", 1) 
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 40, 1) 
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 4) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                                ch_k "Oh, way to[K_like]tease a girl!"
                            "Nope.":
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -2) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 4)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                                ch_k "Don't string me along here, [K_Petname]."
                    else:
                        ch_k "Well[K_like]don't do it again."
                    #End Kiss her
                
            "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Kitty", 300, TabM=1):        
                        "You lean over and wrap Kitty in a warm hug."
                    else:                
                        call KittyFace("angry", 1) 
                        "You lean in with your arms wide, but Kitty slips under you and takes a step back."
                        ch_k "What's the deal, [K_Petname]?" 
                        return
                        
                    if K_SEXP >= 30: 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 3)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 2) 
                        call KittyFace("sexy") 
                        ch_k "You're warming me up, [K_Petname]."
                    elif ApprovalCheck("Kitty", 800, "L", TabM=1):
                        call KittyFace("sexy") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1) 
                        ch_k "Hmm, warm huggies."
                    elif ApprovalCheck("Kitty", 550, TabM=1):
                        call KittyFace("surprised", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)        
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)  
                        ch_k "Hey[K_like]what is this about?"
                    elif ApprovalCheck("Kitty", 450, TabM=1):
                        call KittyFace("angry", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)        
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
                        ch_k "I'm not comfortable with this. . ."
                    else: 
                        call KittyFace("angry", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 40, -4)       
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
                        ch_k "What was that about, [K_Petname]?"   
                        
            "Slap her ass" if K_Loc == bg_current:                                                              #Slap her ass
                    call K_Slap_Ass 
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call KittyFace("surprised", 1) 
                    if K_SEXP >= 5 and ApprovalCheck("Kitty", 700, TabM=1):        
                        "You come up to Kitty from behind and quickly pinch her butt."
                    else:                
                        "You come up to Kitty from behind and quickly pinch her butt."
                        call KittyFace("angry") 
                        "She slaps your hand away and rounds on you."
                        ch_k "Hey! Bad touch!" 
                        return
                        
                    if K_SEXP >= 40: 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)           
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        call KittyFace("sexy") 
                        ch_k "Purrrr, Kitty like."
                    elif ApprovalCheck("Kitty", 800, "L", TabM=1):
                        call KittyFace("sexy") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)           
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                        ch_k "Hmm, you know it, [K_Petname]."
                    elif ApprovalCheck("Kitty", 1000, TabM=1):
                        call KittyFace("surprised") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)           
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 3)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                        ch_k "Ooh! Hey!"
                    elif ApprovalCheck("Kitty", 800, TabM=1):
                        call KittyFace("angry") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -4)           
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 4)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 3)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1) 
                        ch_k "Dude!"
                    else: 
                        call KittyFace("angry") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -8)           
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 5)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 4)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                        ch_k "Ow! That hurt!"  

            "Open those zippers" if K_Panties == "zipper panties" or K_Chest == "bustier bra":
                    call KittyFace("sexy",2) 
                    ch_k "Ok, [K_Petname]"
                    "She opens the zippers"
                    $ K_Panties = "zipper panties open"
                    $ K_Chest = "bustier bra open"
                    $ K_Outfit = "zipper bondage open"
                    $ K_Shame = K_OutfitShame[1]
                    
            "Pull her panties down" if not K_Legs and K_Panties and not K_PantiesDown and K_Panties != "swimsuit3" and K_Panties != "zipper panties" and K_Panties != "zipper panties open":
                    call KittyFace("surprised", 1) 
                    #$ R_Upskirt = 1
                    $ K_PantiesDown = 1
                    pause 0.5            
                    #$ R_PantiesDown = 0
                    #$ R_Upskirt = 0
                    $ K_PantiesDown = 0
                    "You sneak up on Kitty from behind and pull her panties down quickly!"
                    
                    if not Taboo: #no taboo
                        if ApprovalCheck("Kitty", 850, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "Oh, naughty, [K_Petname]!"
                            ch_k "You could have just asked, you know. . ."
                        elif ApprovalCheck("Kitty", 700, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "[K_Petname]! A little warning!"
                        elif ApprovalCheck("Kitty", 600, "L"):
                            call KittyFace("bemused", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 3)  
                            ch_k "Wha?! [K_Petname]? . . I don't usually. . ."
                        elif ApprovalCheck("Kitty", 500):
                            call KittyFace("angry", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)  
                            ch_k "Wha! [K_Petname]!"
                        else: 
                            call KittyFace("angry", 1) 
                            ch_k "What the fuck, [K_Petname]!"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)           
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                            ch_k "Not cool"  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 7)             
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 3)           
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 4)  
                        call Kitty_First_Bottomless(1) 
                        
                    else: #no panties, taboo
                        if ApprovalCheck("Kitty", 850, "L") and ApprovalCheck("Kitty", 1500):
                            call KittyFace("sexy", 1) 
                            ch_k "Oh, naughty, [K_Petname]!"
                            ch_k "You could have just asked, you know. . ."
                        elif ApprovalCheck("Kitty", 700, "L") and ApprovalCheck("Kitty", 1500):
                            call KittyFace("sexy", 1) 
                            ch_k "[K_Petname]! A little warning!"
                        elif ApprovalCheck("Kitty", 700, "L"):
                            call KittyFace("bemused", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 3)  
                            ch_k "[K_Petname]! This isn't the time or place for this!"
                        elif ApprovalCheck("Kitty", 1000):
                            call KittyFace("angry", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)  
                            ch_k "Wha! [K_Petname]!"
                        else: 
                            call KittyFace("angry", 1) 
                            ch_k "What the fuck, [K_Petname]!"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)           
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                            ch_k "Not cool" 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 7)             
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 4)           
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 4)  
                        call Kitty_First_Bottomless(1) 
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 1) 
                    if "exhibitionist" in K_Traits:
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 4) 
                    #End Flip her Skirt   

            "Pull her shorts down" if (K_Legs == "shorts" or K_Legs == "blue shorts" or K_Legs == "white shorts") and not K_PantiesDown and not K_Upskirt:
                    call KittyFace("surprised", 1) 
                    $ K_Upskirt = 1
                    #$ K_PantiesDown = 1
                    pause 0.5            
                    #$ R_PantiesDown = 0
                    $ K_Upskirt = 0
                    #$ K_PantiesDown = 0
                    "You sneak up on Kitty from behind and pull her shorts down quickly!"
                    
                    if not Taboo: #no taboo
                        if ApprovalCheck("Kitty", 850, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "Oh, naughty, [K_Petname]!"
                            ch_k "You could have just asked, you know. . ."
                        elif ApprovalCheck("Kitty", 700, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "[K_Petname]! A little warning!"
                        elif ApprovalCheck("Kitty", 600, "L"):
                            call KittyFace("bemused", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 3)  
                            ch_k "Wha?! [K_Petname]? . . I don't usually. . ."
                        elif ApprovalCheck("Kitty", 500):
                            call KittyFace("angry", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)  
                            ch_k "Wha! [K_Petname]!"
                        else: 
                            call KittyFace("angry", 1) 
                            ch_k "What the fuck, [K_Petname]!"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)           
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                            ch_k "Not cool"  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)             
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)           
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1)  
                        if K_Panties:
                            $ K_SeenPanties = 1
                        else:
                            call Kitty_First_Bottomless(1) 
                        
                    else: #no panties, taboo
                        if ApprovalCheck("Kitty", 850, "L") and ApprovalCheck("Kitty", 1500):
                            call KittyFace("sexy", 1) 
                            ch_k "Oh, naughty, [K_Petname]!"
                            ch_k "You could have just asked, you know. . ."
                        elif ApprovalCheck("Kitty", 700, "L") and ApprovalCheck("Kitty", 1500):
                            call KittyFace("sexy", 1) 
                            ch_k "[K_Petname]! A little warning!"
                        elif ApprovalCheck("Kitty", 700, "L"):
                            call KittyFace("bemused", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 3)  
                            ch_k "[K_Petname]! This isn't the time or place for this!"
                        elif ApprovalCheck("Kitty", 1000):
                            call KittyFace("angry", 1) 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)           
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)  
                            ch_k "Wha! [K_Petname]!"
                        else: 
                            call KittyFace("angry", 1) 
                            ch_k "What the fuck, [K_Petname]!"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)           
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                            ch_k "Not cool" 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)             
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)           
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)  
                        if K_Panties:
                            $ K_SeenPanties = 1
                        else:
                            call Kitty_First_Bottomless(1) 
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 1) 
                    if "exhibitionist" in K_Traits:
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 4) 
                    #End Flip her Skirt 


            "Grab her tit":                                                                                     #Grab her tit
                    call KittyFace("surprised", 1) 
                    if K_SEXP >= 5 and ApprovalCheck("Kitty", 700, TabM=2):        
                        "You come up to Kitty and quickly honk her boob."
                    else:             
                        "You come up to Kitty and quickly honk her boob."
                        call KittyFace("angry") 
                        show Kitty_Sprite
                        with vpunch
                        "She slaps your hand away and elbows you in the ribs."
                        ch_k "[K_Like]WTF, [K_Petname]?" 
                        return
                        
                    if K_SEXP >= 40: 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2) 
                        call KittyFace("sexy") 
                        ch_k "Hmm, I'm glad I can't phase right now, [K_Petname]."
                        $ Count = 10
                    elif ApprovalCheck("Kitty", 850, "L", TabM=1):
                        call KittyFace("sexy") 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1) 
                        ch_k "Hmm, keep it there, [K_Petname]."
                        $ Count = 7
                    elif ApprovalCheck("Kitty", 1200, TabM=1):
                        call KittyFace("perplexed") 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 1)         
                        ch_k "Kinda forward, [K_Petname]."
                        $ Count = 5
                    elif ApprovalCheck("Kitty", 900, TabM=1):
                        call KittyFace("angry") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 4)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 1) 
                        ch_k "You might want to move that?"
                        $ Count = 3
                    else: 
                        call KittyFace("angry") 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -8)          
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 5)            
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 2) 
                        ch_k "You wanna lose that hand?" 
                        $ Count = 2
                              
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
                    ch_k "Um, are you done yet?"
                    while Count > 0:
                        if Count == 6:
                            call KittyFace("sexy", 1) 
                            ch_k "Mmmmm, I do kinda like it. . ."  
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 2)       
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
                        elif Count == 3:
                            call KittyFace("perplexed") 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 1) 
                            ch_k "Not that it's not nice, [K_Petname], but maybe stop?"
                        elif Count == 2:
                            call KittyFace("angry") 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -1) 
                            ch_k "Ok, give it a rest."
                        elif Count == 1:
                            call KittyFace("angry") 
                            ch_k "Back it up, [K_Petname]!"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5) 
                            show Kitty_Sprite
                            with vpunch
                            "She elbows you in the ribs."
                            ch_k "WTF, [K_Petname]?" 
                            $ Count = 1                     
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_k "That wasn't[K_like]{i}so{/i} bad. . ."  
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2)         
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                                    elif Count <= 4:
                                        ch_k "Probably for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        ch_k "That wasn't[K_like]{i}so{/i} bad. . ."          
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 4) 
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
                                    elif Count >= 4:
                                        ch_k "A real joker, [K_Petname]."
                                    else:
                                        call KittyFace("angry") 
                                        ch_k "Douche."
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if K_FondleB and ApprovalCheck("Kitty", 1100, TabM=2):                                
                                        call KittyFace("sexy",1) 
                                        $ K_Eyes = "closed"
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5) 
                                    else:
                                        call KittyFace("perplexed") 
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 2) 
                                        $ Count -= 1
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 4)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)
                                    ch_k "Umm. . ."
                                    
                                "Just leave it there.":
                                    if Count == 5:
                                        call KittyFace("perplexed") 
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 3) 
                                        ch_k "Huh."                            
                                    elif Count == 2:
                                        call KittyFace("perplexed") 
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 1) 
                                        ch_k "This is getting a bit uncomfortable."
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)            
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
                                    
                            
                    
                    if K_FondleB and ApprovalCheck("Kitty", 1200, TabM = 3): 
                        call KittyFace("sexy", 1) 
                        ch_k "I wouldn't mind if we kept. . . you know. . ."
                        menu:
                            extend ""
                            "Yeah!":
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 3)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                                call Kitty_SexAct("breasts") 
                                return
                            "Nah, that was enough.":
                                call KittyFace("sad", 1) 
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -2)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 4)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2) 
                                ch_k "Whatevs."
                    elif ApprovalCheck("Kitty", 900, TabM = 3):  
                        $ K_Brows = "confused"
                        $ K_Eyes = "sexy"
                        $ K_Mouth = "smile"
                        ch_k "You enjoy that?"
                    elif ApprovalCheck("Kitty", 900): 
                        call KittyFace("angry", 1) 
                        ch_k "How could you do that in public?"
                    else:
                        call KittyFace("angry", 1) 
                        ch_k "[K_like]keep your hands to yourself!"
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Kitty from behind and gently rub her shoulders."
                    if K_SEXP >= 30:
                        call KittyFace("sexy") 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)
                        "She sinks back into your hands"
                        ch_k "Hmm, getting frisky, [K_Petname]?"
                    elif ApprovalCheck("Kitty", 650, "L"):
                        call KittyFace("sexy") 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)
                        ch_k "Purr, that's nice, [K_Petname]."
                    elif ApprovalCheck("Kitty", 500):
                        call KittyFace("surprised", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                        ch_k "Oh, hey, [K_Petname]. What's up?"
                    elif ApprovalCheck("Kitty", 400):
                        call KittyFace("angry", 1) 
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -1)
                        if Taboo:
                            ch_k "Hey[K_like]maybe chill out, [K_Petname]?"
                        else:
                            ch_k "Whoa, back it up."
                    else: 
                        call KittyFace("angry", 1) 
                        "She slaps your hands away."
                        ch_k "No touchy!"           
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 3)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
              
            "Ask for her panties" if K_Panties != "swimsuit3":
                    call Kitty_AskPanties 
                    
            "Never mind [[exit]":
                    $ K_Chat[5] = 0  
                    return
    else:
        "Kitty isn't around."
            
    return



label Kitty_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not K_Panties or K_Panties == "shorts" or K_Panties == "blue shorts" or K_Panties == "white shorts":
        if ApprovalCheck("Kitty", 900):
            call KittyFace("sexy", 1) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 40, 10)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 10) 
            ch_k "I might. . . if I had any. . ."
            
        elif ApprovalCheck("Kitty", 500):
            call KittyFace("bemused", 2) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, -3)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)
            ch_k "Um[K_like]what?"
            $ K_Blush = 1
            
        else:       
            call KittyFace("angry", 1) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, -5)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
            ch_k "WTF?!"
            $ K_Blush = 0
            show Kitty_Sprite at SpriteLoc(K_SpriteLoc) with vpunch
            "She slaps you in the face."
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
            
    else:
        if K_SeenPussy and ApprovalCheck("Kitty", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif K_SeenPanties and ApprovalCheck("Kitty", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in K_Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in K_Traits or "sex friend" in K_Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in K_RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if K_Legs == "pants" or HoseNum("Kitty") >= 10: 
            if ApprovalCheck("Kitty", 1000, "OI", TabM = 2) or "exhibitionist" in K_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Kitty", 900, TabM = 2):
                $ Line = "change"
                
        elif K_Legs == "skirt":
            if ApprovalCheck("Kitty", 600, "OI", TabM = 2) or "exhibitionist" in K_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Kitty", 1100, TabM = 2):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Kitty", 1200, TabM = 2) or "exhibitionist" in K_Traits:
                $ Line = "here"
        
        
        if Line == "here":                              
                #She's agreed to change and will do it here
                call KittyFace("sly") 
                if K_Legs == "skirt":      
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 4)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 4)
                else: #no pants or skirt         
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 6)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 6) 
                
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)    
                call Remove_Panties("Kitty") 
                    
                if Taboo:
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
                    if "exhibitionist" in K_Traits: 
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5)
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)        
            
        elif Line:                                      
                    #She's agreed to change, but leaves the room to do it.       
                    call KittyFace("bemused", 1) 
                    menu:
                        ch_k "Could you turn around?"
                        "OK.": 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5) 
                            call KittyFace("smile", 1) 
                            ch_k "Thanks, [K_Petname]."
                            call KittyFace("sly", 1) 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2)         
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 4)            
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 4)
                            show blackscreen onlayer black 
                            "You turn around"   
                            $ K_DailyActions.append("pantyless")
                            call KittyOutfit 
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Kitty") 
                            "When you turn back, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Kitty", 1000, "LI"): 
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 5)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 5)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5) 
                                call KittyFace("sly", 1) 
                                ch_k "Oh, you think there's a show?"
                            else:                 
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, -3)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5) 
                                ch_k "Apparently so."
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Kitty", 600, "OI"): 
                                call KittyFace("bemused", 1) 
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 5)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 10)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5) 
                                ch_k "Ok."
                                call KittyFace("sexy") 
                            else:        
                                call KittyFace("angry", 1) 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, -5)            
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5) 
                                ch_k "Huh, maybe[K_like]have a little respect?"
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call KittyFace("sly", 1) 
                                if K_Legs or HoseNum("Kitty") >= 10:   
                                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)         
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 3)            
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5)  
                                        
                                call Remove_Panties("Kitty") 
                                
        else:                                           #She refuses.    
            call KittyFace("angry", 2) 
            if not ApprovalCheck("Kitty", 500):
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 3)            
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                ch_k "You think I'd do that?"
                $ K_RecentActions.append("angry")
                $ K_DailyActions.append("angry")   
                
            elif not ApprovalCheck("Kitty", 500, TabM = 5):
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5) 
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 5)            
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5) 
                ch_k "I mean, here?"                                
                $ K_RecentActions.append("angry")
                $ K_DailyActions.append("angry")   
                
            else:
                call KittyFace("bemused", 2) 
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3)            
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                if Taboo:            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
                    
                if K_Love >= K_Inbt or K_Obed >= K_Inbt:
                    ch_k "Maybe you'll earn that, [K_Petname]."
                else:
                    call KittyFace("perplexed") 
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, -2)    
                    ch_k "You're nasty, [K_Petname]."
            $ K_Blush = 1
                
    $ Tempmod = Store       
    $ Line = 0
    return

    # End Ask for Panties   //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


# Kitty Control interface ///////////////////
label Kitty_Controls:
    menu:
        "I'd like you to call me something else":
            call Kitty_Names 
            return
        "I'd like you to come over for some action." if K_Loc != bg_current:
            ch_k "Ok, I'll be right over."
            $ K_Loc = bg_current 
            call Set_The_Scene 
            call Kitty_SexMenu 
            return
        "I'd like to get busy." if K_Loc == bg_current:
            ch_k "Oh do you?"
            call Kitty_SexMenu 
            return
        "I want you to stop taking your own initiative." if "sub" not in K_Traits:
            $ K_Traits.append("sub")
            ch_k "You're the boss, [K_Petname]."                
        "Exit.":
            return
    jump Kitty_Controls
return

# start Kitty_Gifts//////////////////////////////////////////////////////////
label Kitty_Gifts:  
    if P_Inventory == []:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Give her a dildo." if "dildo" in P_Inventory: #If you have a Dildo, you'll give it.
            $ Count = K_Inventory.count("dildo")
            if "dildo" not in K_Inventory:                            
                "You give Kitty the dildo."
                $ K_Blush = 1
                $ Kitty_Arms = 2
                $ K_Held = "dildo"
                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 600, "I"):                    
                    call KittyFace("bemused") 
                    $ P_Inventory.remove("dildo")
                    $ K_Inventory.append("dildo")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 30)
                    ch_k "I'm sure I can find some place to store it. . ."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                elif ApprovalCheck("Kitty", 800) or ApprovalCheck("Kitty", 400, "I"):
                    call KittyFace("confused") 
                    $ P_Inventory.remove("dildo")
                    $ K_Inventory.append("dildo")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 10)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 10)
                    ch_k "I don't know what. . ."  
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 5)
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                    call KittyFace("surprised") 
                    ch_k "Oh!"
                    ch_k "Oh. . . I'll just[K_like]put it away."
                    call KittyFace("bemused") 
                elif "offered gift" in K_DailyActions:
                    call KittyFace("angry") 
                    "She hands it back to you."
                    ch_k "I think I[K_like]made myself clear about inappropriate gifts?"     
                else:
                    call KittyFace("angry") 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, 20)                    
                    ch_k "I- you shouldn't be giving girls stuff like this!"                     
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                    "She hands it back to you."
                    $ K_DailyActions.append("offered gift") 
            elif Count == 1:
                ch_k "Why stop with one. . ."
            else: 
                ch_k "I only have so many places to store these."
            $ K_Held = 0
            $ Kitty_Arms = 2
            
            
        "Give her the vibrator." if "vibrator" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = K_Inventory.count("vibrator")
            if "vibrator" not in K_Inventory:                            
                "You give Kitty the Shocker Vibrator."
                $ K_Blush = 1
                $ Kitty_Arms = 2
                $ K_Held = "vibrator"
                if ApprovalCheck("Kitty", 700):                    
                    call KittyFace("bemused") 
                    $ P_Inventory.remove("vibrator")
                    $ K_Inventory.append("vibrator")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 30)
                    ch_k "Well this is. . . [[bzzzt]- "
                    ch_k "-interesting. . ."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                elif ApprovalCheck("Kitty", 400):
                    call KittyFace("confused") 
                    $ P_Inventory.remove("vibrator")
                    $ K_Inventory.append("vibrator")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 10)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 10)
                    ch_k "I've heard these are very relaxing. . ."  
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                    call KittyFace("surprised") 
                    ch_k "-for my back!"
                    call KittyFace("bemused", 1) 
                elif "offered gift" in K_DailyActions:
                    call KittyFace("angry") 
                    "She hands it back to you."
                    ch_k "I think I[K_like]made myself clear about inappropriate gifts?"   
                else:
                    call KittyFace("angry") 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, 20)                    
                    ch_k "I can't really see the point."                     
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 5)
                    "She hands it back to you."
                    $ K_DailyActions.append("offered gift") 
            else: 
                ch_k "I already have one of these."
            $ K_Held = 0
            $ Kitty_Arms = 2
            
            
        "Give her the lace bra." if "lace bra" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = K_Inventory.count("lace bra")
            if "lace bra" not in K_Inventory:                            
                "You give Kitty the lace bra."
                if ApprovalCheck("Kitty", 1200):                    
                    call KittyFace("bemused") 
                    $ P_Inventory.remove("lace bra")
                    $ K_Inventory.append("lace bra")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 25)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 20)
                    ch_k "At least you appreciate what I've got."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                elif ApprovalCheck("Kitty", 800):
                    call KittyFace("confused",1) 
                    $ P_Inventory.remove("lace bra")
                    $ K_Inventory.append("lace bra")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 15)
                    ch_k "This is. . . see-through. . ."                    
                    call KittyFace("bemused",1) 
                elif ApprovalCheck("Kitty", 600):
                    call KittyFace("confused",2) 
                    $ P_Inventory.remove("lace bra")
                    $ K_Inventory.append("lace bra")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 20)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 25)
                    ch_k "I don't know why you'd give me this, it's not like I'd wear it. . ."                     
                    call KittyFace("bemused",1) 
                elif "no gift bra" in K_RecentActions:
                    call KittyFace("angry",2) 
                    ch_k "I just told you no, stop being a creepazoid!"
                elif "no gift bra" in K_DailyActions:
                    call KittyFace("angry",2) 
                    ch_k "I haven't changed my mind, stop bothering me!"      
                else:
                    call KittyFace("angry",2) 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, 20)  
                    if "no gift panties" in K_DailyActions:                    
                        ch_k "I don't want these either!"                       
                    else:                   
                        ch_k "You just- just don't be thinking about my breasts!"                     
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 5)
                    $ K_Blush = 1
                    "She hands it back to you."
                    $ K_RecentActions.append("no gift bra")                      
                    $ K_DailyActions.append("no gift bra") 
            else: 
                ch_k "I already have one of those."                
            
        "Give her the lace panties." if "lace panties" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = K_Inventory.count("lace panties")
            if "lace panties" not in K_Inventory:                            
                "You give Kitty the lace panties."
                $ K_Blush = 1
                if ApprovalCheck("Kitty", 1200):                    
                    call KittyFace("bemused") 
                    $ P_Inventory.remove("lace panties")
                    $ K_Inventory.append("lace panties")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 30)
                    ch_k "These don't leave much to the imagination. . ."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                elif ApprovalCheck("Kitty", 900):
                    call KittyFace("confused",1) 
                    $ P_Inventory.remove("lace panties")
                    $ K_Inventory.append("lace panties")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 25)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 20)
                    ch_k "These are barely there. . ."                  
                    call KittyFace("bemused",1) 
                elif ApprovalCheck("Kitty", 700):
                    call KittyFace("confused",2) 
                    $ P_Inventory.remove("lace panties")
                    $ K_Inventory.append("lace panties")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 20)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 25)
                    ch_k "I- I wouldn't wear something like these. . ."                  
                    call KittyFace("bemused",1) 
                    ch_k "But I'll hold on to them. . ." 
                elif "no gift panties" in K_RecentActions:
                    call KittyFace("angry",2) 
                    ch_k "Ew I just told you no! What are you, obsessed?!"
                elif "no gift panties" in K_DailyActions:
                    call KittyFace("angry",2) 
                    ch_k "Look, my answer's still no, stop asking!"                      
                else:
                    call KittyFace("angry",2) 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -15)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, 20)
                    if "no gift bra" in K_DailyActions:                    
                        ch_k "I don't want these either!" 
                    elif K_SeenPanties:
                        ch_k "Just because you've seen my panties doesn't mean you get to pick them out."                          
                    else:
                        ch_k "Oh, don't you worry what I've got on down there."                     
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 5)
                    $ K_Blush = 1
                    "She hands them back to you."
                    $ K_RecentActions.append("no gift panties")                      
                    $ K_DailyActions.append("no gift panties") 
            else: 
                ch_k "I already have one of those."                
            
            
        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = K_Inventory.count("Dazzler and Longshot")
            if "Dazzler and Longshot" not in K_Inventory:                            
                "You give Kitty the book."
                $ K_Blush = 1
                if ApprovalCheck("Kitty", 600, "L"):                    
                    call KittyFace("smile") 
                    ch_k "Oh, this one's so sweet!"
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                else:
                    call KittyFace("confused") 
                    ch_k "Hm, worth the read I guess."  
                    call KittyFace("bemused") 
                $ P_Inventory.remove("Dazzler and Longshot")
                $ K_Inventory.append("Dazzler and Longshot") 
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 50) 
            else: 
                ch_k "I already have one of those."                
            
        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: #If you have a book, you'll give it.
            $ Count = K_Inventory.count("256 Shades of Grey")
            if "256 Shades of Grey" not in K_Inventory:                            
                "You give Kitty the book."
                $ K_Blush = 1
                if ApprovalCheck("Kitty", 500, "O"):                    
                    call KittyFace("bemused") 
                    ch_k "I'll give it a good look."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                else:
                    call KittyFace("confused") 
                    ch_k "Hmm, I guess I could read a few chapters."  
                    call KittyFace("bemused") 
                $ P_Inventory.remove("256 Shades of Grey")
                $ K_Inventory.append("256 Shades of Grey")                    
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 50)  
            else: 
                ch_k "I already have one of those."                
            
        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: #If you have a book, you'll give it.
            $ Count = K_Inventory.count("256 Shades of Grey")
            if "Avengers Tower Penthouse" not in K_Inventory:                            
                "You give Kitty the book."
                $ K_Blush = 1
                if ApprovalCheck("Kitty", 500, "I"):                    
                    call KittyFace("bemused") 
                    ch_k "This should be fun. . ."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 89, 10)
                else:
                    call KittyFace("confused") 
                    ch_k "Well. . . this is a bit. . . I could maybe learn a few things."  
                    call KittyFace("bemused") 
                $ P_Inventory.remove("Avengers Tower Penthouse")
                $ K_Inventory.append("Avengers Tower Penthouse")                    
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 50)  
            else: 
                ch_k "I already have one of those."                
            

        "Exit":
            pass
    
    return


# start Kitty_Names//////////////////////////////////////////////////////////
label Kitty_Names:    
    menu:
        ch_k "Oh? What would you like me to call you?"
        "Sweetie's fine.":
            $ K_Petname = "sweetie"
            ch_k "You got it, sweetie."
        "My initial's fine.":            
            $ K_Petname = Playername[:1]  #fix test this
            ch_k "You got it, [K_Petname]."
        "Call me by my name.":
            $ K_Petname = Playername            
            ch_k "If you'd rather, [K_Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in K_Petnames:
            $ K_Petname = "boyfriend"
            ch_k "Sure thing, [K_Petname]."
        "Call me \"lover\"." if "lover" in K_Petnames:
            $ K_Petname = "lover"
            ch_k "Oooh, love to, [K_Petname]."
        "Call me \"sir\"." if "sir" in K_Petnames:
            $ K_Petname = "sir"
            ch_k "Yes, [K_Petname]."
        "Call me \"master\"." if "master" in K_Petnames:
            $ K_Petname = "master"
            ch_k "As you wish, [K_Petname]."
        "Call me \"sex friend\"." if "sex friend" in K_Petnames:
            $ K_Petname = "sex friend"
            ch_k "Heh, very cheeky, [K_Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in K_Petnames:
            $ K_Petname = "fuck buddy"
            ch_k "I'm game if you are, [K_Petname]."        
        "Call me \"daddy\"." if "daddy" in K_Petnames:
            $ K_Petname = "daddy"
            ch_k "Oh! You bet, [K_Petname]."
        "Nevermind.":
            return
    return
# end Kitty_Names//////////////////////////////////////////////////////////

label Kitty_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Kitty.":
                        $ K_Pet = "Kitty"            
                        ch_k "I don't see why not, [K_Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ K_Pet = "girl"
                        if "boyfriend" in K_Petnames or ApprovalCheck("Kitty", 500, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "I'm totally your girl, [K_Petname]."
                        else:      
                            call KittyFace("angry") 
                            ch_k "I'm NOT your girl, [K_Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ K_Pet = "boo"
                        if "boyfriend" in K_Petnames or ApprovalCheck("Kitty", 500, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "Aw, I am your boo, [K_Petname]."
                        else:     
                            call KittyFace("angry") 
                            ch_k "I'm NOT your boo,  [K_Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ K_Pet = "bae"
                        if "boyfriend" in K_Petnames or ApprovalCheck("Kitty", 500, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "Aw, I am your bae, [K_Petname]."
                        else:     
                            call KittyFace("angry") 
                            ch_k "I'm NOT your bae,  [K_Petname]."
                            
                    "I think I'll call you \"baby\".":
                        $ K_Pet = "baby"
                        if "boyfriend" in K_Petnames or ApprovalCheck("Kitty", 500, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "Aw, cute, [K_Petname]."
                        else:     
                            call KittyFace("angry") 
                            ch_k "I'm not a baby!" 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ K_Pet = "sweetie"
                        if "boyfriend" in K_Petnames or ApprovalCheck("Kitty", 500, "L"):
                            ch_k "Aw, that's sweet, [K_Petname]."
                        else:     
                            call KittyFace("angry", 1) 
                            ch_k "Too saccharine, [K_Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ K_Pet = "sexy"
                        if "lover" in K_Petnames or ApprovalCheck("Kitty", 900):
                            call KittyFace("sexy", 1) 
                            ch_k "Mreow, [K_Petname]."
                        else:        
                            call KittyFace("angry", 1) 
                            ch_k "Not in public, [K_Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ K_Pet = "lover"
                        if "lover" in K_Petnames or ApprovalCheck("Kitty", 900):
                            call KittyFace("sexy", 1) 
                            ch_k "Love you too, [K_Petname]!"
                        else:      
                            call KittyFace("angry", 1) 
                            ch_k "Not in this lifetime, [K_Petname]."  
                    
                    "I think I'll call you \"kitten\".":
                        $ K_Pet = "baby"
                        if "boyfriend" in K_Petnames or ApprovalCheck("Kitty", 500, "L"):
                            call KittyFace("sexy", 1) 
                            ch_k "Purrr, [K_Petname]."
                        else:     
                            call KittyFace("angry") 
                            ch_k "Not really that cute, [K_Petname]" 
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ K_Pet = "slave"
                        if "master" in K_Petnames or ApprovalCheck("Kitty", 700, "O"):
                            call KittyFace("bemused", 1) 
                            ch_k "As you wish, [K_Petname]."
                        else:      
                            call KittyFace("angry", 1) 
                            ch_k "I'm not slave, [K_Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ K_Pet = "pet"
                        if "master" in K_Petnames or ApprovalCheck("Kitty", 600, "O"):
                            call KittyFace("bemused", 1) 
                            ch_k "Hmm, make sure to pet me, [K_Petname]."
                        else:             
                            call KittyFace("angry", 1) 
                            ch_k "I'm no house cat, [K_Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ K_Pet = "slut"
                        if "sex friend" in K_Petnames or ApprovalCheck("Kitty", 1000, "OI"):
                            call KittyFace("sexy") 
                            ch_k "If the name fits, [K_Petname]."
                        else:                
                            call KittyFace("angry", 1) 
                            $ K_Mouth = "surprised"
                            ch_k "Not unless you want to lose some teeth!" 
                            
                    "I think I'll call you \"whore\".":
                        $ K_Pet = "whore"
                        if "fuckbuddy" in K_Petnames or ApprovalCheck("Kitty", 1100, "OI"):
                            call KittyFace("sly") 
                            ch_k "Only for you though. . ."
                        else:        
                            call KittyFace("angry", 1) 
                            ch_k "Can you say that with a fat lip, [K_Petname]?" 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ K_Pet = "sugartits"
                        if "sex friend" in K_Petnames or ApprovalCheck("Kitty", 1400):
                            call KittyFace("sly", 1) 
                            ch_k "These little things?"
                        else:     
                            call KittyFace("angry", 1) 
                            ch_k "I would hope not, [K_Petname]." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ K_Pet = "sex friend"
                        if "sex friend" in K_Petnames or ApprovalCheck("Kitty", 600, "I"):
                            call KittyFace("sly") 
                            ch_k "Rreow. . ."
                        else:                
                            call KittyFace("angry", 1) 
                            ch_k "Not out loud, [K_Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ K_Pet = "fuckbuddy"
                        if "fuckbuddy" in K_Petnames or ApprovalCheck("Kitty", 700, "I"):
                            call KittyFace("sly") 
                            ch_k "Yup."
                        else:                
                            call KittyFace("angry", 1) 
                            $ K_Mouth = "surprised"
                            ch_k "Don't even joke, [K_Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ K_Pet = "baby girl"
                        if "daddy" in K_Petnames or ApprovalCheck("Kitty", 1200):
                            call KittyFace("smile", 1) 
                            ch_k "You know it, [K_Petname]."
                        else:                
                            call KittyFace("angry", 1) 
                            ch_k "I'm no kid!" 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Kitty_Namecheck(K_Pet = K_Pet, Cnt = 0, Ugh = 0):#K_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if K_Pet == "Kitty":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if K_Pet == "girl":                                         #easy options
        if ApprovalCheck("Kitty", 500, "L", TabM=1):            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -1)
            $ Ugh = 1
    elif K_Pet == "boo" or K_Pet == "bae":
        if ApprovalCheck("Kitty", 500, "L", TabM=1):
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -2)
            $ Ugh = 1
    elif K_Pet == "baby":    
        if ApprovalCheck("Kitty", 500, "L", TabM=1):
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 30, -1)
            $ Ugh = 1
    elif K_Pet == "kitten":
        if ApprovalCheck("Kitty", 600, "L", TabM=1):
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -1)
            $ Ugh = 1
    elif K_Pet == "sweetie":
        if not ApprovalCheck("Kitty", 500, "L", TabM=1):
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)  
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 40, -1)
            $ Ugh = 1
            
    elif K_Pet == "sexy" or K_Pet == "lover":
        if ApprovalCheck("Kitty", 900, TabM=1):                                                        #over 150
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
        else:                                                            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, (-1-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    elif K_Pet == "slave":                                        #tougher options
        if ApprovalCheck("Kitty", 800, "O", TabM=3):                                            #over 80
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, (3+Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, (2+Cnt))
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)     
        elif ApprovalCheck("Kitty", 500, "O", TabM=3):                                                  #between 50 and 80
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 81, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)        
        else:                                                                                           # under 50
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -1, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -1)
            $ Ugh = 1
    
    elif K_Pet == "pet":                                        #tougher options
        if ApprovalCheck("Kitty", 1500, TabM=2):                                            #over 150
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, (3+Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, (2+Cnt))
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)     
        elif ApprovalCheck("Kitty", 1200, TabM=2):                                                  #between 120 and 150
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 81, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)        
        else:                                                                                           # under 120
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -1, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -1)
            $ Ugh = 1
            
    elif K_Pet == "slut":
        if ApprovalCheck("Kitty", 500, "O", TabM=2) or ApprovalCheck("Kitty", 500, "I", TabM=2):        #over 50
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, (4+Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, (2+Cnt))
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1)
        elif ApprovalCheck("Kitty", 300, "O", TabM=2) or ApprovalCheck("Kitty", 300, "I", TabM=2):      #between 30 and 50
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-1-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, (2+Cnt))
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)        
        else:                                                                                           # under 40
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-2-Cnt))
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, (-1-Cnt), 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    elif K_Pet == "whore":
        if ApprovalCheck("Kitty", 600, "O", TabM=2) or ApprovalCheck("Kitty", 600, "I", TabM=2):        #over 60
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 4)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1)
        elif ApprovalCheck("Kitty", 400, "O", TabM=2) or ApprovalCheck("Kitty", 400, "I", TabM=2):      #between 40 and 60
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-2-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
        else:                                                                                           # under 40
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-3-Cnt))
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, (-2-Cnt), 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 21, 1, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    elif K_Pet == "sugartits":
        if ApprovalCheck("Kitty", 1500, TabM=1):                                                        #over 150
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
        else:                                                                       
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-2-Cnt))
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, (-1-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    elif K_Pet == "sex friend":    
        if ApprovalCheck("Kitty", 750, "O", TabM=1) or ApprovalCheck("Kitty", 600, "I", TabM=1):        #over 75/60
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 3)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1)
        elif ApprovalCheck("Kitty", 600, "O", TabM=1) or ApprovalCheck("Kitty", 400, "I", TabM=1):      #between 60/40 and 75/60
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 2)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-1-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
            $ K_Blush = 1
        else:                                                                                           # under 60/40
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -Cnt)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, (-1-Cnt), 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    elif K_Pet == "fuckbuddy":
        if ApprovalCheck("Kitty", 700, "O", TabM=2) or ApprovalCheck("Kitty", 700, "I", TabM=1):        #over 70/70
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 3)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 85, 1)
        elif ApprovalCheck("Kitty", 600, "O", TabM=2) or ApprovalCheck("Kitty", 500, "I", TabM=1):      #between 60/50 and 70/70
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 2)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-1-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
            $ K_Blush = 1
        else:                                                                                           #under 60/50
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -Cnt)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, (-2-Cnt), 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    elif K_Pet == "baby girl":
        if ApprovalCheck("Kitty", 1200, TabM=1):                                                        #over 150
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
        else:                                                                       
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, (-2-Cnt))
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, (-1-Cnt))
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Kitty_Personality//////////////////////////////////////////////////////////
label Kitty_Personality(Cnt = 0):   
    if not K_Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Kitty to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_k "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if K_Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_k "If[K_like]that's what you want, I could be a bit more obedient."
            $ K_Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if K_Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_k "I could always be a bit more wild if that's what you want."
            $ K_Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if K_Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_k "Ok, I could open up more."
            $ K_Chat[4] = 3
        "More Loving. [[Obedience to Love]" if K_Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_k "I'll try to."
            $ K_Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if K_Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_k "Oooh, kinky. . ."
            $ K_Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if K_Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_k "We do have fun together. . ."
            $ K_Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if K_Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_k "Um, ok."
            $ K_Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Kitty_Personality
        "Nevermind.":
            return
    return
# end Kitty_Personality//////////////////////////////////////////////////////////




# Kitty_Summon//////////////////////////////////////////////////////////

label Kitty_Summon(Tempmod=Tempmod):
    call KittyOutfit 
    if "no summon" in K_RecentActions:
                if "angry" in K_RecentActions:
                    ch_k "Get a clue, [K_Petname]!"
                elif Action_Check("Kitty", "recent", "no summon") > 1:
                    ch_k "I'm telling you to give it a rest!"
                    $ K_RecentActions.append("angry") 
                elif Current_Time == "Night": 
                    ch_k "Like I said, it's too late for that."
                else:
                    ch_k "Like I told you, I'm busy."   
                $ K_RecentActions.append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Kitty", 700, "L") or ApprovalCheck("Kitty", 300, "O"):                              #It's night time but she likes you.
                        ch_k "It's[K_like]getting kinda late, but we can hang out for a bit."
                        $ K_Loc = bg_current 
                        call Set_The_Scene 
                else:                                                           #It's night time and she isn't into you
                        ch_k "It's kinda late? Maybe tomorrow."       
                        $ K_RecentActions.append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if K_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif K_Loc == "bg dangerroom":    
        $ Tempmod = 10
    elif K_Loc == "bg pool":    
        $ Tempmod = 10
    elif K_Loc == "bg field":    
        $ Tempmod = 10
    elif K_Loc == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Kitty", 700, "L") or not ApprovalCheck("Kitty", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Kitty", 300):
                ch_k "I'm kinda busy, [K_Petname]."       
                $ K_RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in K_RecentActions:
                pass
        elif "goto" in K_RecentActions:
                ch_k "You {i}just{/i} left here, why not come back?"
        elif K_Loc == "bg classroom":
                ch_k "I'm[K_like]in class right now, [K_Petname], you up for it?"
        elif K_Loc == "bg dangerroom": 
                ch_k "I'm in the Danger Room, [K_Petname], want in?"
        elif K_Loc == "bg pool": 
                ch_k "I'm at the pool, [K_Petname], want in?"
        elif K_Loc == "bg field": 
                ch_k "I'm[K_like]gonna watch the match, [K_Petname], want to come?"    
        elif K_Loc == "bg campus": 
                ch_k "I'm chillin in the quad, [K_Petname], want to come?" 
        elif K_Loc == "bg kitty": 
                ch_k "I'm in my room, [K_Petname], want to hang?" 
        elif K_Loc == "bg player": 
                ch_k "I'm in your room, [K_Petname],come home. . ."   
        elif K_Loc == "bg showerroom":    
            if ApprovalCheck("Kitty", 1600):
                ch_k "I'm[K_like]in the shower right now, [K_Petname], want to get wet?"
            else:            
                ch_k "I'm[K_like]in the shower right now, [K_Petname], maybe we could touch base later."       
                $ K_RecentActions.append("no summon")         
                return      
        elif K_Loc == "hold":
                ch_k "I'm[K_like]kinda off the grid right now. Sorry?"       
                $ K_RecentActions.append("no summon") 
                return      
        else:        
                ch_k "Why don't you come over here, [K_Petname]?"    
           
           
        if "summoned" in K_RecentActions:
            ch_k "Ok, fiiiiine, but why are you dragging me all over?"           
            $ Line = "yes"            
        elif "goto" in K_RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_k "KK, Cya!"
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_k "OK."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Kitty", 600, "L") or ApprovalCheck("Kitty", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Kitty", 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Kitty", 1400):                         
                                #she is generally favorable 
                                ch_k "Ok, fine."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Kitty", 200, "O"):                                  
                                #she is not obedient  
                                ch_k "Whatever."    
                                ch_k "Here I am if you want me."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 55, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                    ch_k "See ya!"
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)                            
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                    ch_k "Oh, ok. Later then."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Kitty", 600, "L") or ApprovalCheck("Kitty", 1400):
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)                   
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Kitty", 600, "O"):                              
                        #she is obedient
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 1, 1)    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 40, -1)                
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Kitty", 1400):       
                        #she is generally favorable
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -1)  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)                                
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)  
                        ch_k "Ok, fine, [K_Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Kitty", 200, "O"):                                         
                        #she is not obedient   
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -4)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -2)   
                        ch_k "You're not my supervisor!"                             
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)    
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, -2)
                        ch_k "You know where to find me."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)                                    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -1, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if K_Love > K_Obed:
            ch_k "Sure!"
        else:
            ch_k "Ok, be there in a gif, [K_Petname]."
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ K_RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if K_Loc == "bg classroom":
                ch_k "I[K_like]really need to study, [K_Petname]." 
            elif K_Loc == "bg dangerroom": 
                ch_k "I'm just getting a workout in."
            else:
                ch_k "I'm sorry, [K_Petname], but I'm kinda busy."          
            $ K_RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ K_RecentActions.append("goto")  
            if K_Loc == "bg classroom":
                    ch_k "I'll hold a seat for you!"
                    jump Class_Room 
            elif K_Loc == "bg dangerroom": 
                    ch_k "I'll be warming up!"
                    jump Danger_Room
            elif K_Loc == "bg kitty":    
                    ch_k "I'll clean up a few things."
                    jump Kitty_Room
            elif K_Loc == "bg player": 
                    ch_k "I'll be here for you."
                    jump Player_Room
            elif K_Loc == "bg field": 
                    ch_k "I'll hold a seat for you!"
                    jump Field_Entry  
            elif K_Loc == "bg pool": 
                    ch_k "I'll be here for you."
                    jump Pool_Entry                
            elif K_Loc == "bg showerroom": 
                    ch_k "I guess I'll be lathering up."
                    jump Shower_Room
            elif K_Loc == "bg campus": 
                    ch_k "I've got a nice spot in the shade."
                    jump Campus
            else:
                    ch_k "You know, I'll just meet you in my room."
                    $ K_Loc = "bg kitty"
                    jump Kitty_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_k "Awwww, how sweet!"
    elif Line == "command": 
            ch_k "Very well, [K_Petname]."
        
    $ K_RecentActions.append("summoned")  
    $ Line = 0
    ch_k "I'll be right over."                                
    $ K_Loc = bg_current 
    call KittyOutfit 
    call Set_The_Scene 
    return

# End Kitty Summon ///////////////////    


label Kitty_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in K_RecentActions:
        call DrainWord("Kitty","leaving") 
    else:
        return
    
    if K_Loc == "hold":   
            # Activates if she's being moved out of play
            ch_k "I'm[K_like]going off the grid, see you later." 
            return
            
    if "Kitty" in Party or "lockedtravels" in K_Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ K_Loc = bg_current 
            return
      
    elif "freetravels" in K_Traits or not ApprovalCheck("Kitty", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call KittyOutfit 
            if GirlsNum: #if someone left before her
                        ch_k "Yeah, I'm headed out too."
                        
            if K_Loc == "bg classroom":
                        ch_k "I'm[K_like]headed to class right now."
            elif K_Loc == "bg dangerroom": 
                        ch_k "I'm[K_like]hitting the danger room."   
            elif K_Loc == "bg campus": 
                        ch_k "I'm[K_like]going to hang out on campus." 
            elif K_Loc == "bg kitty": 
                        ch_k "I'm[K_like]heading back to my room." 
            elif K_Loc == "bg player": 
                        ch_k "I'll[K_like]be heading to your room."
            elif K_Loc == "bg pool": 
                        ch_k "I'll[K_like]be heading to the pool."
            elif K_Loc == "bg field": 
                        ch_k "I'm headed to the field now."     
            elif K_Loc == "bg showerroom":    
                if ApprovalCheck("Kitty", 1400):
                        ch_k "I'm catching a shower, later!"
                else:            
                        ch_k "I'm outta here, later!"
            else:        
                        ch_k "I'm headed out, see you later."                  
            hide Kitty_Sprite
            return     
            #End Free Travels
    
    call KittyOutfit 
    
    if "follow" not in K_Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ K_Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if K_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif K_Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif K_Loc == "bg showerroom":    
        $ Tempmod = 40
    
    
    if GirlsNum: #if someone left before her
                ch_k "Yeah, I'm headed out too."
                
    if K_Loc == "bg classroom":
        ch_k "I'm headed to class right now, you could[K_like]join me."
    elif K_Loc == "bg dangerroom": 
        ch_k "I'm hitting the danger room, care to[K_like]join me?"    
    elif K_Loc == "bg campus": 
        ch_k "I'm going to[K_like]hang out on campus, want to chill with me?" 
    elif K_Loc == "bg kitty": 
        ch_k "I'm heading back to my room, want to[K_like]hang out?" 
    elif K_Loc == "bg player": 
        ch_k "I'll[K_like]be heading to your room."
    elif K_Loc == "bg field": 
        ch_k "I'm headed to the field now, care to[K_like]join me?"   
    elif K_Loc == "bg pool": 
        ch_k "I'm headed to the pool now, care to[K_like]join me?"   
    elif K_Loc == "bg showerroom":    
        if ApprovalCheck("Kitty", 1600):
            ch_k "I'm[K_like]hitting the showers, want to join me?"
        else:            
            ch_k "I'm hitting the showers, maybe we could[K_like]touch base later."
            return        
    elif K_Loc == "bg pool":        
        ch_k "I'm going [K_like] hang at the pool, wanna come with me, [K_Petname]?" 
    else:        
        ch_k "Wanna[K_like]come with me, [K_Petname]?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in K_RecentActions:
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 55, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in K_RecentActions:
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)                            
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                ch_k "Ok, cool. Talk to you later then."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Kitty", 600, "L") or ApprovalCheck("Kitty", 1400):                
                    if "followed" not in K_RecentActions:
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)                   
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in K_RecentActions:
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                    $ Line = "no"
                
        "No, stay here.":
                if ApprovalCheck("Kitty", 600, "O"):                              
                    #she is obedient
                    if "followed" not in K_RecentActions:
                        if K_Love >= 50:
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 40, -1)                
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Kitty", 1400):       
                    #she is generally favorable
                    if "followed" not in K_RecentActions:
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -1)  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)                                
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)  
                    ch_k "Uh, sure, I guess."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Kitty", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in K_RecentActions:
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -4)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -2)   
                    ch_k "[K_Like]in your dreams, [K_Petname]."  
                    if "followed" not in K_RecentActions:                       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)    
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, -2)
                    ch_k "I'm gone."                    
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in K_RecentActions:
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)                                    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -1, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ K_RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Kitty_Sprite
            call Gym_Clothes("auto", "Kitty") 
            call Pool_Clothes("auto", "Kitty") 
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if K_Loc == "bg classroom":
                ch_k "Totally can't, [K_Petname], Gotta study for the test." 
            elif K_Loc == "bg dangerroom": 
                ch_k "Sorry [K_Petname], but I[K_like]need the practice?"
            else:
                ch_k "I'm[K_like]sorry, [K_Petname], I've got things to do."         
            hide Kitty_Sprite
            call Gym_Clothes("auto", "Kitty") 
            call Pool_Clothes("auto", "Kitty") 
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainWord("All","leaving") 
            call DrainWord("All","arriving") 
            hide Kitty_Sprite
            call Gym_Clothes("auto", "Kitty") 
            call Pool_Clothes("auto", "Kitty") 
            if K_Loc == "bg classroom":
                ch_k "Cool, study buddy!"            
                jump Class_Room_Entry
            elif K_Loc == "bg dangerroom": 
                ch_k "I'll be ready and waiting!"
                jump Danger_Room_Entry
            elif K_Loc == "bg kitty": 
                ch_k "I'll meet you there."
                jump Kitty_Room
            elif K_Loc == "bg player": 
                ch_k "I'll be waiting."
                jump Player_Room                
            elif K_Loc == "bg showerroom": 
                ch_k "I guess I'll see you there."
                jump Shower_Room_Entry
            elif K_Loc == "bg campus": 
                ch_k "Let's head over there."
                jump Campus_Entry
            elif K_Loc == "bg pool":
                ch_k "Let's go for a swim"
                jump Pool_Entry
            elif K_Loc == "bg field":
                ch_k "Don't be too late!"
                jump Field_Entry
            else:            
                ch_k "You know, I'll just meet you in my room."
                $ K_Loc = "bg kitty"
                jump Kitty_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_k "I guess[K_like]I couldn't leave you lonely. . ."
    elif Line == "command": 
            ch_k "Humph, ok."
    
    $ Line = 0
    ch_k "I guess I can stick around."                                
    $ K_Loc = bg_current 
    return

# End Kitty Leave ///////////////////   

label Kitty_Dismissed(Leaving = 0):
    if "Kitty" in Party:        
            $ Party.remove("Kitty")
    call Kitty_Schedule(0) 
    menu:
        "You can leave if you like.":
                if K_Loc != bg_current and not ApprovalCheck("Kitty", 600, "O"):
                        ch_k "Well, I think I'll stay."
                else:
                        ch_k "Ok, later!"
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if K_Loc != bg_current and not ApprovalCheck("Kitty", 800, "LO"):
                        ch_k "I've got nowhere better to be."
                elif not ApprovalCheck("Kitty", 500, "LO"):
                        ch_k "Yeah, no."               
                else:
                        if "dismissed" not in K_DailyActions:
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 7)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
                        ch_k "Sure, ok." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if K_Loc != bg_current and not ApprovalCheck("Kitty", 450, "O"):
                        ch_k "Um, no."
                elif not ApprovalCheck("Kitty", 250, "O"):
                        call KittyFace("confused") 
                        ch_k "Not when you've got me curious."
                else:
                        if "dismissed" not in K_DailyActions:
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 10)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 7)
                        ch_k "Um, ok."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
                
    if not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if K_Loc != bg_current and (ApprovalCheck("Kitty", 1200, "LO") or ApprovalCheck("Kitty", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in K_DailyActions:
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 10)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                ch_k "Um, ok."  
                                $ Leaving = 1                                  
                        elif K_Loc != bg_current and (ApprovalCheck("Kitty", 1000, "LO") or ApprovalCheck("Kitty", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in K_DailyActions:
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -5, 1)
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 10)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                call KittyFace("angry") 
                                ch_k "Fine, jerk!"      
                                $ Leaving = 1                         
                        elif K_Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in K_DailyActions:
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -5, 1)
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -10, 1)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3)
                                call KittyFace("angry") 
                                ch_k "Noooope."          
                        elif ApprovalCheck("Kitty", 1400, "LO") or ApprovalCheck("Kitty", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in K_DailyActions:
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -5, 1)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                call KittyFace("sad") 
                                ch_k "Um, sure, fine."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in K_DailyActions:
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -5, 1)
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -10, 1)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -5)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
                                call KittyFace("sad") 
                                ch_k "Yeah right."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in K_DailyActions:
            $ K_DailyActions.append("dismissed")        
    if Leaving == 0:
            # Stay
            $ K_Loc = bg_current
    else:
            # Go
            if K_Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg kitty":
                $ K_Loc = "bg campus"
            else:
                $ K_Loc = "bg kitty"
            hide Kitty_Sprite
            "Kitty heads out." 
    return
    #end "you can leave"
    

label Kitty_AboutRogue:
    ch_k "What do I think about her? Well. . ."
    
    if "poly rogue" in K_Traits:  
        ch_k "You know we're[K_like]close. . ."    
    elif K_LikeRogue >= 900:
        ch_k "She's[K_like]really sexy. . ."
    elif K_LikeRogue >= 800:
        ch_k "She's my bestie, and maybe. . ."    
    elif K_LikeRogue >= 700:
        ch_k "She's[K_like]my bestie!"
    elif K_LikeRogue >= 600:
        ch_k "We're[K_like]friends and all."
    elif K_LikeRogue >= 500:
        ch_k "She's not[K_like]a jerk or anything."
    elif K_LikeRogue >= 400:
        ch_k "I'm kinda[K_like]over her."
    elif K_LikeRogue >= 300:
        ch_k "That basic bitch gotta go." 
    else:
        ch_k "That slut?"
          
    return
    
#End Kitty_AboutRogue
    

## Kitty's Clothes ///////////////////
label Kitty_Clothes:    
    call KittyFace 
    menu:
        ch_k "So[K_like]you wanted to talk about my clothes?"
        "Let's talk about your outfits.":
                    jump Kitty_Clothes_Outfits        
        "Let's talk about your over shirts.":
                    jump Kitty_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Kitty_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Kitty_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Kitty_Clothes_Misc
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Kitty_OutfitShame(3,1) 
                    "Custom 2":
                                call Kitty_OutfitShame(5,1) 
                    "Custom 3":
                                call Kitty_OutfitShame(6,1) 
                    "Custom 4":
                                call Kitty_OutfitShame(11,1) 
                    "Custom 5":
                                call Kitty_OutfitShame(12,1) 
                    "Custom 6":
                                call Kitty_OutfitShame(13,1) 
                    "Custom 7":
                                call Kitty_OutfitShame(14,1) 
                    "Gym Clothes":
                                call Kitty_OutfitShame(7,1) 
                    "Sleepwear":
                                call Kitty_OutfitShame(9,1) 
                    "Never mind":
                                pass
        "Never mind, you look good like that.":
                if "wardrobe" not in K_RecentActions: 
                        #Apply stat boosts only if it's the first time this turn 
                        if K_Chat[1] <= 1:                
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 15)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 20)
                                ch_k "That's[K_like]really nice of you to say."
                        elif K_Chat[1] <= 10:
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 5)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 7)
                                ch_k "I like it too." 
                        elif K_Chat[1] <= 50:
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 1)  
                                ch_k "Yeah."
                        else:
                                ch_k "Sure."                    
                        $ K_RecentActions.append("wardrobe")   
                $ K_OutfitDay = K_Outfit           
                $ K_Chat[1] += 1                
                return
            
    jump Kitty_Clothes
    #End of Kitty Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Kitty_Clothes_Outfits:                                                                                 # Outfits
        "I really like that pink shirt and capris outfit you wear.":                   #Green
            call KittyOutfit("pink outfit") 
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ K_Outfit = "pink outfit"
                    $ K_Shame = K_OutfitShame[1]
                    ch_k "I used to wear that one[K_like]every day!"
                "Let's try something else though.":
                    ch_k "K."

        "Put on that black dress":                   #Green
            call KittyOutfit("black dress") 
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ K_Outfit = "black dress"
                    $ K_Shame = K_OutfitShame[1]
                    ch_k "This is [K_like] so classy!"
                "Let's try something else though.":
                    ch_k "K."  

        "Put on that kitty lingerie":                   #Green
            call KittyOutfit("kitty lingerie") 
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ K_Outfit = "kitty lingerie"
                    if K_Headband != "black" and K_Headband != "pink":
                        $ K_Headband = "black"
                    $ K_Shame = K_OutfitShame[1]
                    ch_k "This is [K_like] so sexy!"
                "Let's try something else though.":
                    ch_k "K."  

        "Put on that bondage outfit" if K_Bondage:
            call KittyOutfit("zipper bondage") 
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ K_Outfit = "zipper bondage"
                    $ K_Shame = K_OutfitShame[1]
                    ch_k "This is [K_like] so naughty!"
                "Let's try something else though.":
                    ch_k "K."            
                    
        "That red shirt and black jeans look really nice on you.":                           #Pink  
            call KittyOutfit("red outfit") 
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ K_Outfit = "red outfit"
                    $ K_Shame = K_OutfitShame[2]
                    ch_k "That one[K_like]used to be my favorite too!"
                "Let's try something else though.":
                    ch_k "K."   

        "That violet shirt and black and blue pants outfit look really nice on you.":                           #Pink  
            call KittyOutfit("party outfit") 
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ K_Outfit = "party outfit"
                    $ K_Shame = K_OutfitShame[2]
                    ch_k "That one[K_like]used to be my favorite too!"
                "Let's try something else though.":
                    ch_k "K."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not K_Custom[0] and not K_Custom2[0] and not K_Custom3[0] and not K_Custom4[0] and not K_Custom5[0] and not K_Custom6[0] and not K_Custom7[0]:
                        pass       
                        
        "Remember that outfit we put together?" if K_Custom[0] or K_Custom2[0] or K_Custom3[0] or K_Custom4[0] or K_Custom5[0] or K_Custom6[0] or K_Custom7[0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not K_Custom[0]:
                        pass
                    "Throw on Custom 1" if K_Custom[0]:
                        call KittyOutfit("custom1") 
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not K_Custom2[0]:
                        pass
                    "Throw on Custom 2" if K_Custom2[0]:
                        call KittyOutfit("custom2") 
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not K_Custom3[0]:
                        pass
                    "Throw on Custom 3" if K_Custom3[0]:
                        call KittyOutfit("custom3") 
                        $ Cnt = 6
                    "Throw on Custom 4 (locked)" if not K_Custom4[0]:
                        pass
                    "Throw on Custom 4" if K_Custom4[0]:
                        call KittyOutfit("custom4") 
                        $ Cnt = 11
                    "Throw on Custom 5 (locked)" if not K_Custom5[0]:
                        pass
                    "Throw on Custom 5" if K_Custom5[0]:
                        call KittyOutfit("custom5") 
                        $ Cnt = 12
                    "Throw on Custom 6 (locked)" if not K_Custom6[0]:
                        pass
                    "Throw on Custom 6" if K_Custom6[0]:
                        call KittyOutfit("custom6") 
                        $ Cnt = 13
                    "Throw on Custom 7 (locked)" if not K_Custom7[0]:
                        pass
                    "Throw on Custom 7" if K_Custom7[0]:
                        call KittyOutfit("custom7") 
                        $ Cnt = 14
                    
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ K_Schedule[9] = "custom2"
                        elif Cnt == 6:
                            $ K_Schedule[9] = "custom3"
                        elif Cnt == 11:
                            $ K_Schedule[9] = "custom4"
                        elif Cnt == 12:
                            $ K_Schedule[9] = "custom5"
                        elif Cnt == 13:
                            $ K_Schedule[9] = "custom6"
                        elif Cnt == 14:
                            $ K_Schedule[9] = "custom7"
                        else:
                            $ K_Schedule[9] = "custom"
                        ch_k "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if K_Custom[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not K_Custom[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if K_Custom2[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom2[0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not K_Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if K_Custom3[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom3[0] = 0
                            "Custom 3 [[clear custom 1] (locked)" if not K_Custom3[0]:
                                pass
                            
                            "Custom 4 [[clear custom 4]" if K_Custom4[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom4[0] = 0
                            "Custom 4 [[clear custom 1] (locked)" if not K_Custom4[0]:
                                pass
                            "Custom 5 [[clear custom 5]" if K_Custom5[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom5[0] = 0
                            "Custom 5 [[clear custom 1] (locked)" if not K_Custom5[0]:
                                pass
                            "Custom 6 [[clear custom 6]" if K_Custom6[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom6[0] = 0
                            "Custom 6 [[clear custom 1] (locked)" if not K_Custom6[0]:
                                pass
                            "Custom 7 [[clear custom 7]" if K_Custom7[0]:
                                ch_k "Ok, no problem."
                                $ K_Custom7[0] = 0
                            "Custom 7 [[clear custom 1] (locked)" if not K_Custom7[0]:
                                pass
                            "Never mind, [[back].":
                                pass    
                                            
                                            
                    "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                        pass
                    "You should wear this one out." if Cnt:
                        call Kitty_Custom_Out(Cnt) 
                    "Ok, back to what we were talking about. . .":
                        $ Cnt = 0
                        jump Kitty_Clothes_Outfits                    
        
        "Your birthday suit looks really great. . .":                                     #Nude
            call KittyFace("sexy", 1) 
            $ Line = 0
            if not K_Chest and not K_Panties and not K_Over and not K_Legs and not K_Hose:                
                ch_k "You're kidding, right?"  
            elif K_SeenChest and K_SeenPussy and ApprovalCheck("Kitty", 1200, TabM=4):
                ch_k "[K_Like]Reow. . ."  
                $ Line = 1
            elif ApprovalCheck("Kitty", 2000, TabM=4):
                ch_k "You don't[K_like]mess around, huh."    
                $ Line = 1
            elif K_SeenChest and K_SeenPussy and ApprovalCheck("Kitty", 1200, TabM=0):
                ch_k "[K_Like]this is a little exposed. . ."  
            elif ApprovalCheck("Kitty", 2000, TabM=0):
                ch_k "Maybe if we were alone?" 
            elif ApprovalCheck("Kitty", 1000, TabM=0):                
                call KittyFace("surprised", 2) 
                ch_k "[K_Like]get to know a girl first, [K_Petname]."
                $ K_Blush = 1
            else:
                call KittyFace("angry", 1) 
                ch_k "Yeah[K_like]it does."    
                
            if Line:                                                            #If she got nude. . .                            
                call KittyOutfit("nude") 
                "She lets all her clothes drop into a pile at her feet."
                call Kitty_First_Topless 
                call Kitty_First_Bottomless(1) 
                call KittyFace("sexy") 
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in K_Traits:
                            ch_k "I'm[K_like]getting a little wet just thinking about it." 
                            $ K_Outfit = "nude"
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 10) 
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 5) 
                            $ K_Shame = K_OutfitShame[0]
                        elif ApprovalCheck("Kitty", 800, "I") and ApprovalCheck("Kitty", 2800, TabM=0):                    
                            ch_k "I guess we could. . ."
                            $ K_Outfit = "nude"
                            $ K_Shame = K_OutfitShame[0]
                        else:
                            call KittyFace("sexy", 1) 
                            $ K_Eyes = "surprised"
                            ch_k "No way! That'd be[K_like]totally embarrassing!" 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in K_Traits:
                            ch_k "Aw, do I have to?"                         
                        elif ApprovalCheck("Kitty", 800, "I") and ApprovalCheck("Kitty", 2800, TabM=0):       
                            call KittyFace("bemused", 1) 
                            ch_k "It's a good thing you didn't[K_like]ask me to wear this outside."
                            ch_k "A good thing. . ."
                        else:
                            call KittyFace("confused", 1) 
                            ch_k "I[K_like]don't mind this around the room, but definitely not outside."   
            $ Line = 0
                
        "How about throwing on your sleepwear?":
            #fix add conditions
            call KittyOutfit("sleep") 
            
        "Let's talk about what you wear outside.":
            call Kitty_Clothes_Schedule 
            
        "Never mind":    
            jump Kitty_Clothes     
            
    jump Kitty_Clothes
    #End of Kitty Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Kitty_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no Overshirt?" if K_Over:
            call KittyFace("bemused", 1) 
            if ApprovalCheck("Kitty", 800, TabM=3) and (K_Chest or K_SeenChest):
                ch_k "Why not?"
            elif ApprovalCheck("Kitty", 1200, TabM=0):
                call Kitty_NoBra 
                if not _return:
                    jump Kitty_Clothes
            $ Line = K_Over
            $ K_Over = 0
            "She lets her [Line] drop to her feet."
            
        "Try on that pink shirt you have." if K_Over != "pink top":
            call KittyFace("bemused") 
            if K_Chest or K_SeenChest:
                ch_k "K."
            elif ApprovalCheck("Kitty", 800, TabM=0):
                ch_k "Yeah, ok."          
            else:
                call KittyFace("bemused", 1) 
                ch_k "This top is a little skimpy for what I have on under it."
                jump Kitty_Clothes    
            $ K_Over = "pink top"  

        "Try on that dark shirt you have." if K_Over != "dark top":
            call KittyFace("bemused") 
            if K_Chest or K_SeenChest:
                ch_k "K."
            elif ApprovalCheck("Kitty", 800, TabM=0):
                ch_k "Yeah, ok."          
            else:
                call KittyFace("bemused", 1) 
                ch_k "This top is a little skimpy for what I have on under it."
                jump Kitty_Clothes    
            $ K_Over = "dark top"   
                
        "How about that red t-shirt you have?" if K_Over != "red shirt":
            $ K_Over = "red shirt"  
            ch_k "This one?"

        "How about that purple t-shirt you have?" if K_Over != "purple shirt":
            $ K_Over = "purple shirt"  
            ch_k "This one?"

        "How about that violet shirt you have?" if K_Over != "violet shirt scarfless":
            $ K_Over = "violet shirt scarfless"  
            ch_k "This one?"
            
        "Maybe just throw on a towel?" if K_Over != "towel":
            call KittyFace("bemused", 1) 
            if K_Chest or K_SeenChest:
                ch_k "Weirdo."
            elif ApprovalCheck("Kitty", 1000, TabM=0):
                call KittyFace("perplexed", 1) 
                ch_k "I guess? . ."          
            else:
                ch_k "I don't think so with what I have on under it."
                jump Kitty_Clothes    
            $ K_Over = "towel"  

        "How about that black dress?" if K_Over != "black dress":
            if K_Legs:
                ch_k "I can't really wear that with my [K_Legs] on."
            elif ApprovalCheck("Kitty", 1100, TabM=3):
                ch_k "Sure. . ."
                $ K_Over = "black dress"   

            else:
                ch_k "That's a bit . . . revealing."  
                            
        "Never mind":
            pass
    jump Kitty_Clothes
    #End of Kitty Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Kitty_NoBra: #fix test this
        menu:
            ch_k "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":   
                        if K_SeenChest and ApprovalCheck("Kitty", 1000, TabM=3):
                                $ K_Blush = 2
                                ch_k "-not that that's a problem. . ."
                                $ K_Blush = 1                        
                        elif ApprovalCheck("Kitty", 1200, TabM=4):
                                $ K_Blush = 2
                                ch_k "-not that that's a problem. . ."
                                $ K_Blush = 1                
                        elif ApprovalCheck("Kitty", 900, TabM=2) and "lace bra" in K_Inventory:
                                ch_k "I could find {i}something{/i} to wear."
                                $ K_Chest  = "lace bra"    
                                "She pulls out her lace bra and passes it through her [K_Over]."
                        elif ApprovalCheck("Kitty", 800, TabM=2):
                                ch_k "Yeah, I guess."
                                $ K_Chest = "bra"
                                "She pulls out her bra and passes it through her [K_Over]."
                        elif ApprovalCheck("Kitty", 700, TabM=2):
                                ch_k "Yeah, I guess."
                                $ K_Chest = "cami"
                                "She pulls out her camisole and passes it through her [K_Over]."
                        elif ApprovalCheck("Kitty", 600, TabM=2):
                                ch_k "Yeah, I guess."
                                $ K_Chest = "sports bra"
                                "She pulls out her sports bra and passes it through her [K_Over]."
                        else:
                                ch_k "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Kitty", 1100, "LI", TabM=2) and K_Love > K_Inbt:               
                                ch_k "I guess for you. . ."
                        elif ApprovalCheck("Kitty", 700, "OI", TabM=2) and K_Obed > K_Inbt:
                                ch_k "Sure. . ."
                        elif ApprovalCheck("Kitty", 600, "I", TabM=2):
                                ch_k "Yeah. . ."
                        elif ApprovalCheck("Kitty", 1300, TabM=2):
                                ch_k "Okay, fine."
                        else: 
                                call KittyFace("surprised") 
                                $ K_Brows = "angry"
                                if Taboo:
                                    ch_k "Not in public,[K_Petname]!"
                                else:
                                    ch_k "I don't like you {i}that{/i} much,[K_Petname]!"
                                return 0
                                
                    
            "Never mind.":
                        ch_k "Ok. . ."
                        return 0
        return 1
        #End of Kitty bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Kitty_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the pants." if PantsNum("Kitty") > 5:
            call KittyFace("sexy", 1) 
            if K_SeenPanties and K_Panties and ApprovalCheck("Kitty", 500, TabM=5):
                ch_k "K."
            elif K_SeenPussy and ApprovalCheck("Kitty", 900, TabM=4):
                ch_k "Yeah, ok."
            elif ApprovalCheck("Kitty", 1300, TabM=2) and K_Panties:
                ch_k "For you, I guess. . ."
            elif ApprovalCheck("Kitty", 800) and not K_Panties:
                call Kitty_NoPantiesOn 
                if not _return:
                    jump Kitty_Clothes
            else:
                ch_k "Lol, not around you."
                if not K_Panties:
                    ch_k "I not {i}wearing any panties{/i}. . ."
                jump Kitty_Clothes
            $ K_Legs = 0    
            "She lets her pants drop through her to the ground."
            if K_Panties:                
                $ K_SeenPanties = 1
            else:
                call Kitty_First_Bottomless
        
        "Why don't you lose the shorts?" if PantsNum("Kitty") == 5:
            call KittyFace("sexy", 1) 
            if K_SeenPussy and ApprovalCheck("Kitty", 900, TabM=4): 
                # You've seen her pussy
                if ApprovalCheck("Kitty", 800, "L"):                  
                    ch_k "Well, not that I mind you seeing it. . ."
                elif ApprovalCheck("Kitty", 500, "O"):
                    ch_k "I guess. . ."
                elif ApprovalCheck("Kitty", 350, "I"):
                    ch_k "Hrmm. . ."
                else:
                    ch_k "Okay, okay."
                    
            elif ApprovalCheck("Kitty", 800) and not K_Panties:                       
                #she's not wearing anything over them
                call Kitty_NoPantiesOn 
                if not _return:
                    jump Kitty_Clothes
                    
            else:                                                      
                #she's wearing panties
                if not ApprovalCheck("Kitty", 700, TabM=3): #700+1200
                        ch_k "I'm not really comfortable with that right now. . ."
                        jump Kitty_Clothes_Under                    
                elif ApprovalCheck("Kitty", 800, "L", TabM=3):               
                        ch_k "Well aren't you cheeky. . ."
                elif ApprovalCheck("Kitty", 500, "O", TabM=3): #500+400
                        ch_k "Fine by me."
                elif ApprovalCheck("Kitty", 350, "I", TabM=3):
                        ch_k "Oooh, naughty."
                else:
                        ch_k "Oh, I guess I could."  
                    
            $ K_Legs  = 0       
            "She lets her shorts fall to the ground."
            
            if K_Panties:                
                $ K_SeenPanties = 1
            else:
                call Kitty_First_Bottomless 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  


        "Why don't you lose the skirt?" if PantsNum("Kitty") == 3:
            call KittyFace("sexy", 1) 
            if K_SeenPussy and ApprovalCheck("Kitty", 900, TabM=4): 
                # You've seen her pussy
                if ApprovalCheck("Kitty", 800, "L"):                  
                    ch_k "Well, not that I mind you seeing it. . ."
                elif ApprovalCheck("Kitty", 500, "O"):
                    ch_k "I guess. . ."
                elif ApprovalCheck("Kitty", 350, "I"):
                    ch_k "Hrmm. . ."
                else:
                    ch_k "Okay, okay."
                    
            elif ApprovalCheck("Kitty", 800) and not K_Panties:                       
                #she's not wearing anything over them
                call Kitty_NoPantiesOn 
                if not _return:
                    jump Kitty_Clothes
                    
            else:                                                      
                #she's wearing panties
                if not ApprovalCheck("Kitty", 700, TabM=3): #700+1200
                        ch_k "I'm not really comfortable with that right now. . ."
                        jump Kitty_Clothes_Under                    
                elif ApprovalCheck("Kitty", 800, "L", TabM=3):               
                        ch_k "Well aren't you cheeky. . ."
                elif ApprovalCheck("Kitty", 500, "O", TabM=3): #500+400
                        ch_k "Fine by me."
                elif ApprovalCheck("Kitty", 350, "I", TabM=3):
                        ch_k "Oooh, naughty."
                else:
                        ch_k "Oh, I guess I could."  
                    
            $ K_Legs  = 0       
            "She lets her skirt fall to the ground."
            
            if K_Panties:                
                $ K_SeenPanties = 1
            else:
                call Kitty_First_Bottomless 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  
            
        
        "You look great in those capris." if K_Legs != "capris":
            ch_k "Yeah, ok."
            $ K_Legs = "capris"
                
        "You look great in those black jeans." if K_Legs != "black jeans":
            ch_k "K, no problem."
            $ K_Legs = "black jeans"

        "You look great in those black blue pants." if K_Legs != "black blue pants":
            ch_k "K, no problem."
            $ K_Legs = "black blue pants"
        
        "You look great in yoga pants." if K_Legs != "yoga pants":
            ch_k "Yeah, ok."
            $ K_Legs = "yoga pants"
            
        "What about wearing your yellow shorts?" if K_Legs != "shorts":
            ch_k "K, no problem."
            $ K_Legs = "shorts"  

        "What about wearing your blue shorts?" if K_Legs != "blue shorts":
            ch_k "K, no problem."
            $ K_Legs = "blue shorts" 

        "What about wearing your white shorts?" if K_Legs != "white shorts":
            ch_k "K, no problem."
            $ K_Legs = "white shorts"    

        "Your butt looks cute in that orange skirt." if K_Legs != "orange skirt":
            ch_k "Meoww~"
            $ K_Legs = "orange skirt"

        "Your butt looks cute in that white skirt." if K_Legs != "white skirt":
            ch_k "Meoww~"
            $ K_Legs = "white skirt"

        "Your butt looks cute in that black skirt." if K_Legs != "black skirt":
            ch_k "Meoww~"
            $ K_Legs = "black skirt"

        "Those leather pants look real tight on you." if K_Legs != "leather pants":
            ch_k "Mm~ That's hot."
            $ K_Legs = "leather pants"
            
                   
                                
        "Never mind":
            pass
    jump Kitty_Clothes
    #End of Kitty Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Kitty_NoPantiesOn: #fix test this
        menu:
            ch_k "These are[K_like]all I have on."
            "Then you could slip on a pair of panties. . .":   
                        if K_SeenPussy and ApprovalCheck("Kitty", 1100, TabM=4):
                                $ K_Blush = 2
                                ch_k "I didn't say that bothered me. . ."
                                $ K_Blush = 1                        
                        elif ApprovalCheck("Kitty", 1500, TabM=4):
                                $ K_Blush = 2
                                ch_k "I didn't say that bothered me. . ."
                                $ K_Blush = 1                
                        elif ApprovalCheck("Kitty", 800, TabM=4) and "lace panties" in K_Inventory:
                                ch_k "I like how you think."
                                $ K_Panties  = "lace panties"    
                                "She pulls out her lace panties and pulls them up through her shorts."
                        elif ApprovalCheck("Kitty", 700, TabM=4):
                                ch_k "Yeah, I guess."
                                $ K_Panties = "green panties"
                                "She pulls out her green panties and pulls them up through her shorts."
                        else:
                                ch_k "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Kitty", 1100, "LI", TabM=3) and K_Love > K_Inbt:               
                                ch_k "Well, not that I mind you seeing it. . ."
                        elif ApprovalCheck("Kitty", 700, "OI", TabM=3) and K_Obed > K_Inbt:
                                ch_k "I guess. . ."
                        elif ApprovalCheck("Kitty", 600, "I", TabM=3):
                                ch_k "Hrmm. . ."
                        elif ApprovalCheck("Kitty", 1300, TabM=3):
                                ch_k "Okay, okay."
                        else: 
                                call KittyFace("surprised") 
                                $ K_Brows = "angry"
                                if Taboo:
                                    ch_k "Not in public, [K_Petname]!"
                                else:
                                    ch_k "I don't like you {i}that{/i} much, [K_Petname]!"
                                return 0
                                
            "Never mind.":
                ch_k "Ok. . ."
                return 0
        return 1
        #End of Kitty Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Kitty_Clothes_Under:                                                                                                 # Tops    
        

        "Tops and bras":
            menu Kitty_Clothes_Under_Tops:  

                "How about you lose the [K_Chest]?" if K_Chest and "swimsuit" not in K_Chest:
                    call KittyFace("bemused", 1) 
                    if K_SeenChest and ApprovalCheck("Kitty", 900, TabM=2.7):
                        ch_k "Sure."    
                    elif ApprovalCheck("Kitty", 1100, TabM=2):
                        if Taboo:
                            ch_k "I'm kind of nervous. . ."
                        else:
                            ch_k "If it's just you. . ."
                    elif K_Over == "pink top" or K_Over == "dark top" and ApprovalCheck("Kitty", 600, TabM=2):
                        ch_k "This look is a bit revealing. . ."  
                    elif K_Over == "red shirt" or K_Over == "purple shirt" or K_Over == "violet shirt scarfless" or K_Over == "violet shirt scarf" and ApprovalCheck("Kitty", 500, TabM=2):
                        ch_k "I guess I could. . ."  
                    elif not K_Over:
                        ch_k "Not without a little coverage, for modesty."
                        jump Kitty_Clothes 
                    else:
                        ch_k "I don't think so, [K_Petname]."
                        jump Kitty_Clothes 
                    $ Line = K_Chest
                    $ K_Chest = 0
                    if K_Over:
                        "She reaches into her [K_Over] grabs her [Line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [Line] fall to the ground."
                    jump Kitty_Clothes_Under_Tops 
            
                "Try on that yellow camisole." if K_Chest != "cami":
                    call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    $ K_Chest = "cami"
                    jump Kitty_Clothes_Under_Tops

                "Try on that white camisole." if K_Chest != "white cami":
                    call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    $ K_Chest = "white cami"
                    jump Kitty_Clothes_Under_Tops
                             
                "Try on that orange top." if K_Chest != "orange top":
                    call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    $ K_Chest = "orange top" 
                    jump Kitty_Clothes_Under_Tops  

                "Try on that black mfg top." if K_Chest != "black top":
                    call Kitty_Swimsuit_Change_Top 
                    ch_k "Ok."
                    $ K_Chest = "black top" 
                    jump Kitty_Clothes_Under_Tops          
        
                "How about that leather top?" if K_Chest != "leather top":
                    call Kitty_Swimsuit_Change_Top 
                    ch_k "Mkay."
                    $ K_Chest = "leather top"
                    jump Kitty_Clothes_Under_Tops
                    
                "I like that strapless bra." if K_Chest != "bra":
                    if K_SeenChest or ApprovalCheck("Kitty", 1200, TabM=2):
                        call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        $ K_Chest = "bra"         
                    else:                
                        ch_k "I'm not really comfortable with that. . ."  
                    jump Kitty_Clothes_Under_Tops
                        
                "I like that lace bra." if "lace bra" in K_Inventory and K_Chest != "lace bra":
                    if K_SeenChest or ApprovalCheck("Kitty", 1300, TabM=2):
                        call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        $ K_Chest = "lace bra"         
                    else:                
                        ch_k "It's pretty skimpy. . ." 
                    jump Kitty_Clothes_Under_Tops 

                "I like that darker lace bra." if "lace bra" in K_Inventory and K_Chest != "darker lace bra":
                    if K_SeenChest or ApprovalCheck("Kitty", 1300, TabM=2):
                        call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        $ K_Chest = "darker lace bra"         
                    else:                
                        ch_k "It's pretty skimpy. . ." 
                    jump Kitty_Clothes_Under_Tops 

                "I like that kitty lingerie top." if K_Chest != "kitty lingerie top":
                    if K_SeenChest or ApprovalCheck("Kitty", 1300, TabM=2):
                        call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        $ K_Chest = "kitty lingerie top"         
                    else:                
                        ch_k "It's pretty skimpy. . ." 
                    jump Kitty_Clothes_Under_Tops 
                    
                "I like that sports bra." if K_Chest != "sports bra":
                    if K_SeenChest or ApprovalCheck("Kitty", 1000, TabM=2):
                        call Kitty_Swimsuit_Change_Top 
                        ch_k "K."   
                        $ K_Chest = "sports bra"         
                    else:                
                        ch_k "I'm not sure about that. . ."
                    jump Kitty_Clothes_Under_Tops

                "Go back":  
                    jump Kitty_Clothes_Under

                
                                                                                                                            #Panties        
        
        "Panties": 
            
            menu Kitty_Clothes_Under_Panties:  

                "You could lose those panties. . ." if K_Panties and "swimsuit" not in K_Panties:
                    call KittyFace("bemused", 1) 
                    if ApprovalCheck("Kitty", 900) and (K_Legs or (K_SeenPussy and not Taboo)):
                        #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                        
                        if ApprovalCheck("Kitty", 850, "L"):               
                                ch_k "Well, if you ask me nicely. . ."
                        elif ApprovalCheck("Kitty", 500, "O"):
                                ch_k "For you, ok."
                        elif ApprovalCheck("Kitty", 350, "I"):
                                ch_k "[[snort]."
                        else:
                                ch_k "Yeah, I guess."         
                    else:                       #low approval or not wearing pants or in public 
                        if ApprovalCheck("Kitty", 1100, "LI", TabM=3) and K_Love > K_Inbt:               
                                ch_k "Well, not that I mind you seeing it. . ."
                        elif ApprovalCheck("Kitty", 700, "OI", TabM=3) and K_Obed > K_Inbt:
                                ch_k "I guess. . ."
                        elif ApprovalCheck("Kitty", 600, "I", TabM=3):
                                ch_k "Hrmm. . ."
                        elif ApprovalCheck("Kitty", 1300, TabM=3):
                                ch_k "Okay, okay."
                        else: 
                                call KittyFace("surprised") 
                                $ K_Brows = "angry"
                                if Taboo:
                                    ch_k "Not in public, [K_Petname]!"
                                else:
                                    ch_k "I don't like you that much, [K_Petname]!"
                                jump Kitty_Clothes
                                
                                
                    $ Line = K_Panties
                    $ K_Panties = 0  
                    if K_Legs:
                        "She reaches into her pocket, grabs hold of something, and then pulls her [Line] out, droping them to the ground."                
                    else:
                        "She lets her [Line] drop to the ground."
                        call Kitty_First_Bottomless 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                    jump Kitty_Clothes_Under_Panties  

                "Why don't you wear the green panties instead?" if K_Panties and K_Panties != "green panties":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            call Kitty_Swimsuit_Change_Bottom 
                            ch_k "K."
                            $ K_Panties = "green panties"  
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Clothes_Under_Panties

                "Why don't you wear the white panties instead?" if K_Panties and K_Panties != "white panties":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            call Kitty_Swimsuit_Change_Bottom 
                            ch_k "K."
                            $ K_Panties = "white panties"  
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Clothes_Under_Panties
                        
                "Why don't you wear the lace panties instead?" if "lace panties" in K_Inventory and K_Panties and K_Panties != "lace panties":
                    if ApprovalCheck("Kitty", 1300, TabM=3):
                            call Kitty_Swimsuit_Change_Bottom 
                            ch_k "I guess."
                            $ K_Panties = "lace panties"
                    else:
                            ch_k "That's[K_like]none of your business."
                    jump Kitty_Clothes_Under_Panties

                "Why don't you wear the darker lace panties instead?" if "lace panties" in K_Inventory and K_Panties and K_Panties != "darker lace panties":
                    if ApprovalCheck("Kitty", 1300, TabM=3):
                            call Kitty_Swimsuit_Change_Bottom 
                            ch_k "I guess."
                            $ K_Panties = "darker lace panties"
                    else:
                            ch_k "That's[K_like]none of your business."
                    jump Kitty_Clothes_Under_Panties

                "Why don't you wear the kitty lingerie panties instead?" if K_Panties != "kitty lingerie panties":
                    if ApprovalCheck("Kitty", 1300, TabM=3):
                            call Kitty_Swimsuit_Change_Bottom 
                            ch_k "I guess."
                            $ K_Panties = "kitty lingerie panties"
                    else:
                            ch_k "That's[K_like]none of your business."
                    jump Kitty_Clothes_Under_Panties

                "You know, you could wear some panties with that. . ." if not K_Panties:
                    call KittyFace("bemused", 1) 
                    if (K_Love+K_Obed) <= (2* K_Inbt):
                        $ K_Mouth = "smile"
                        ch_k "I think I'd. . . rather not."
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)
                        menu:
                            "Wear them":
                                pass
                            "Ok":
                                jump Kitty_Clothes
                    call Kitty_Swimsuit_Change_Bottom 
                    menu:
                        ch_k "I guess. . ."
                        "How about the green ones?":
                            ch_k "Sure, ok."
                            $ K_Panties = "green panties"
                        "How about the white ones?":
                            ch_k "Sure, ok."
                            $ K_Panties = "white panties"
                        "How about the purple bikini?":
                            ch_k "Sure, ok."
                            $ K_Panties = "purple bikini panties"
                        "How about the lace ones?" if "lace panties" in K_Inventory:
                            ch_k "Alright."                
                            $ K_Panties  = "lace panties"
                        "How about the darker lace ones?" if "lace panties" in K_Inventory:
                            ch_k "Alright."                
                            $ K_Panties  = "darker lace panties"
                        "How about the kitty lingerie ones?":
                            ch_k "Alright."                
                            $ K_Panties  = "kitty lingerie panties"
                    jump Kitty_Clothes_Under_Panties

                "Go back":  
                    jump Kitty_Clothes_Under

        "Socks and Stockings": 
            
            menu Kitty_Clothes_Under_Hoses:  

                "You could lose those socks. . ." if K_Hose and K_Hose != "stockings":
                    ch_k "K."
                    $ K_Hose = 0
                    jump Kitty_Clothes_Under_Hoses  

                "You could lose those stockings. . ." if K_Hose == "stockings":
                    ch_k "K."
                    $ K_Hose = 0
                    jump Kitty_Clothes_Under_Hoses  

                "Why don't you wear those stockings?" if K_Hose != "stockings":
                    ch_k "K."
                    $ K_Hose = "stockings"  
                    jump Kitty_Clothes_Under_Hoses

                "Why don't you wear those black socks" if K_Hose != "black socks":
                    ch_k "K."
                    $ K_Hose = "black socks"  
                    jump Kitty_Clothes_Under_Hoses

                "Why don't you wear those white socks" if K_Hose != "white socks":
                    ch_k "K."
                    $ K_Hose = "white socks"  
                    jump Kitty_Clothes_Under_Hoses

                "Why don't you wear those pink socks" if K_Hose != "pink socks":
                    ch_k "K."
                    $ K_Hose = "pink socks"  
                    jump Kitty_Clothes_Under_Hoses

                "Go back":  
                    jump Kitty_Clothes_Under

        "How about your swimsuits.":

            menu Kitty_Clothes_Under_SwimSuits:

                "Why don't you wear the swimsuit3" if K_Panties != "swimsuit3" or K_Chest != "swimsuit3":
                    if ApprovalCheck("Kitty", 1200, TabM=3):
                        ch_k "Sure."
                        $ K_Panties = "swimsuit3"
                        $ K_Chest = "swimsuit3"
                    else:
                        ch_r "I don't see how that's any business of yours, [K_Petname]."
                    jump Kitty_Clothes_Under_SwimSuits

                "Remove the swimsuit" if K_Panties == "swimsuit3" or K_Chest == "swimsuit3":
                                call Kitty_Remove_Swimsuit 
                                jump Kitty_Clothes_Under_SwimSuits

                "Why don't you wear the purple bikini bra?" if K_Chest != "purple bikini bra":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            call Kitty_Swimsuit_Change_Top 
                            ch_k "K."
                            $ K_Chest = "purple bikini bra"  
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Clothes_Under_SwimSuits

                "Why don't you wear the purple bikini panties?" if K_Panties != "purple bikini panties":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            call Kitty_Swimsuit_Change_Bottom 
                            ch_k "K."
                            $ K_Panties = "purple bikini panties"  
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Clothes_Under_SwimSuits

                "Why don't you wear the red bikini bra?" if K_Chest != "red bikini bra":
                    if ApprovalCheck("Kitty", 1100, TabM=3):
                            call Kitty_Swimsuit_Change_Top 
                            ch_k "K."
                            $ K_Chest = "red bikini bra"  
                    else:                
                            ch_k "I don't think that's any of your beeswax."
                    jump Kitty_Clothes_Under_SwimSuits

                "Nevermind":
                    jump Kitty_Clothes_Under

        "Never mind":
            pass
    jump Kitty_Clothes
    #End of Kitty Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Kitty_Clothes_Misc:
        "Let's talk about your hair":
            menu Kitty_Clothes_Misc_Hair:                                                                                                                    #Misc
        
                "You look good with your hair up." if K_Hair != "evo":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Hair = "evo"
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Hair

                "Maybe let your hair down." if K_Hair != "long":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "You think?"
                        $ K_Hair = "long"
                    else:
                        ch_k "I[K_like]kinda prefer to keep it up."
                    jump Kitty_Clothes_Misc_Hair

                "You should go for that wet look with your hair." if K_Hair != "wet":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        "She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_Hair = "wet"
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Clothes_Misc_Hair

                "Dye your hair black." if K_HairColor != "black":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairColor = "black"
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Clothes_Misc_Hair

                "Dye your hair blonde." if K_HairColor != "blonde":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairColor = "blonde"
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Clothes_Misc_Hair

                "Dye your hair red." if K_HairColor != "red":
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairColor = "red"
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Clothes_Misc_Hair

                "Change the color of you hair back." if K_HairColor == "black" or K_HairColor == "blonde" or K_HairColor == "red":    
                    if ApprovalCheck("Kitty", 800):
                        ch_k "You think so?"
                        #"She rummages in her bag and grabs some gel, running it through her hair."
                        ch_k "Like this?"
                        $ K_HairColor = 0
                    else:
                        ch_k "It's too high maintenance."
                    jump Kitty_Clothes_Misc_Hair

                "Go back":
                    jump Kitty_Clothes_Misc

        "Let's talk about your headband":
            menu Kitty_Clothes_Misc_Headband:                                                                                                                    #Misc
        
                "You look good with the black kitty headband." if K_Headband != "black":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Headband = "black"
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Headband

                "You look good with  the pink kitty headband." if K_Headband != "pink":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Headband = "pink"
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Headband

                "You look good without the headband." if K_Headband == "black" or K_Headband == "pink":
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Headband = 0
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Headband

                "Go back":
                    jump Kitty_Clothes_Misc

        "Let's talk about your tan":
            menu Kitty_Clothes_Misc_Tan:

                "I like the first tan style" if K_Tan != 'tan':
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Tan = "tan"
                        $ K_DynamicTan[0] = 0
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Tan
    
                "I like the second tan style" if K_Tan != 'tan2':
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Tan = "tan2"
                        $ K_DynamicTan[0] = 0
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Tan

                "I like the third tan style" if K_Tan != 'tan3':
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Tan = "tan3"
                        $ K_DynamicTan[0] = 0
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Tan

                "I like the fourth special tan style":
                    if ApprovalCheck("Kitty", 600):
                        "This tan style will tan her according to her clothes, you won't be able to see it unless you remove her clothes after it"
                        ch_k "Like this?"
                        $ K_Tan = "tan3"
                        $ K_DynamicTan[0] = 1
                        $ K_DynamicTan[2] = K_Legs
                        $ K_DynamicTan[3] = K_Chest
                        $ K_DynamicTan[4] = K_Panties
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Tan
        
                "I prefer without the tan" if K_Tan != 0:
                    if ApprovalCheck("Kitty", 600):
                        ch_k "Like this?"
                        $ K_Tan = 0
                        $ K_DynamicTan[0] = 0
                    else:
                        ch_k "Yeah, I know that."
                    jump Kitty_Clothes_Misc_Tan
    
                "Never mind":
                    jump Kitty_Clothes_Misc
        
        "You know, I like some nice hair down there. Maybe grow it out." if not K_Pubes and "pubes" in K_Todo:
            call KittyFace("bemused", 1) 
            ch_k "[[snort] You've got to give it some time!"
        "You know, I like some nice hair down there. Maybe grow it out." if not K_Pubes and "pubes" not in K_Todo:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1150, TabM=0)
            if ApprovalCheck("Kitty", 850, "L", TabM=0) or (Approval and K_Love > 2 * K_Obed):               
                ch_k "I guess I could. . ."
            elif ApprovalCheck("Kitty", 500, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "You want a furry kitty to pet?"
            elif ApprovalCheck("Kitty", 400, "O", TabM=0) or Approval:
                ch_k "If you want me to. . ."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Not that it's any of your business, [K_Petname]."
                jump Kitty_Clothes
            $ K_Todo.append("pubes")
            $ K_PubeC = 6
        
        "I like it waxed clean down there." if K_Pubes == 1:
            call KittyFace("bemused", 1) 
            if "shave" in K_Todo:
                ch_k "I know, I know. I'll take care of it later."
            else:
                $ Approval = ApprovalCheck("Kitty", 1150, TabM=0)
                
                if ApprovalCheck("Kitty", 850, "L", TabM=0) or (Approval and K_Love > 2 * K_Obed):               
                    ch_k "I guess I could tidy up a bit. . ."
                elif ApprovalCheck("Kitty", 500, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                    ch_k "I'll keep it smooth."
                elif ApprovalCheck("Kitty", 400, "O", TabM=0) or Approval:
                    ch_k "I'll get it done."
                else: 
                    call KittyFace("surprised") 
                    $ K_Brows = "angry"
                    ch_k "Not that it's any of your business, [K_Petname]."
                    jump Kitty_Clothes
                $ K_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not K_SeenPussy and not K_SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if K_Pierce != "ring" and (K_SeenPussy or K_SeenChest) and "ring" not in K_Todo:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1350, TabM=0)
            if ApprovalCheck("Kitty", 900, "L", TabM=0) or (Approval and K_Love > 2* K_Obed):   
                ch_k "If you think they'd look good on me. . ."
            elif ApprovalCheck("Kitty", 600, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "I think they'd look great too!"
            elif ApprovalCheck("Kitty", 500, "O", TabM=0) or Approval:
                ch_k "K, I'll take care of it."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Not that it's any of your business, [K_Petname]."
                jump Kitty_Clothes            
            $ K_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if K_Pierce != "barbell" and (K_SeenPussy or K_SeenChest)and "barbell" not in K_Todo:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1350, TabM=0)
            if ApprovalCheck("Kitty", 900, "L", TabM=0) or (Approval and K_Love > 2 * K_Obed): 
                ch_k "If you think they'd look good on me. . ."
            elif ApprovalCheck("Kitty", 600, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "I think they'd look great too!"
            elif ApprovalCheck("Kitty", 500, "O", TabM=0) or Approval:
                ch_k "K, I'll take care of it."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Not that it's any of your business, [K_Petname]."
                jump Kitty_Clothes                
            $ K_Todo.append("barbell")
            $ K_Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if K_Pierce:
            call KittyFace("bemused", 1) 
            $ Approval = ApprovalCheck("Kitty", 1350, TabM=0)
            if ApprovalCheck("Kitty", 950, "L", TabM=0) or (Approval and K_Love > K_Obed):   
                ch_k "I guess if they're getting in the way . ."
            elif ApprovalCheck("Kitty", 700, "I", TabM=0) or (Approval and K_Inbt > K_Obed):
                ch_k "They were getting a little annoying."
            elif ApprovalCheck("Kitty", 600, "O", TabM=0) or Approval:
                ch_k "I'll take them out then."
            else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                ch_k "Well {i}I{/i} kinda like'em."
                jump Kitty_Clothes            
            $ K_Pierce = 0 
        "Why don't you try on that gold necklace." if K_Neck != "gold necklace":
            ch_k "Ok. . ."         
            $ K_Neck = "gold necklace"
        "Why don't you try on that star necklace." if K_Neck != "star necklace":
            ch_k "Ok. . ."         
            $ K_Neck = "star necklace"
        "Why don't you try on that scarf." if K_Neck != "scarf":
            ch_k "Ok. . ."         
            $ K_Neck = "scarf"
        "Maybe go without a necklace." if K_Neck and K_Neck != "scarf":
            ch_k "Ok. . ."         
            $ K_Neck = 0
        "Maybe go without the scarf." if (K_Neck and K_Neck == "scarf"):
            ch_k "Ok. . ."         
            $ K_Neck = 0

        "Why don't you wear those black gloves." if not K_Gloves:
            ch_k "Ok. . ."         
            $ K_Gloves = "black gloves"
        "Why don't you remove these gloves." if K_Gloves:
            ch_k "Ok. . ."         
            $ K_Gloves = 0
            
        "Never mind":
            pass         
    jump Kitty_Clothes
    #End of Kitty Misc Wardrobe
    
return
#End Kitty Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Kitty_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        
        if ApprovalCheck("Kitty", 1500, "LO"):
                ch_k "Let me know what you like."
                $ Cnt = 3
        elif ApprovalCheck("Kitty", 1200, "LO"):
                ch_k "I could let you pick a few days. . ."
                $ Cnt = 2
        elif ApprovalCheck("Kitty", 1000, "LO"):
                ch_k "We could talk about weekends, maybe. . ."
                $ Cnt = 1
        else:
                ch_k "I think I'll[K_like]figure out my own outfits."
                return
            
        
        menu:
                extend ""
                "On Monday you should wear. . ." if Cnt > 1:
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[0] = _return
                "On Monday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Tuesday you should wear. . ." if Cnt > 2:
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[1] = _return        
                "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Wednesday you should wear. . ." if Cnt > 1:
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[2] = _return
                "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                    pass   
                    
                "On Thursday you should wear. . ." if Cnt > 2:
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[3] = _return
                "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Friday you should wear. . ." if Cnt > 1:
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[4] = _return
                "On Friday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Saturday you should wear. . .":
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[5] = _return
                    
                "On Sunday you should wear. . .":
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[6] = _return
                    
                "In our rooms you should wear. . .":
                    call Kitty_Clothes_ScheduleB(99) 
                    $ K_Schedule[9] = _return   
                    
                "On dates you should wear. . .":
                    call Kitty_Clothes_ScheduleB 
                    $ K_Schedule[7] = _return    
                    
                "Never mind":
                    return        
        jump Kitty_Clothes_Schedule
    
    
    
label Kitty_Clothes_ScheduleB(Count = 0):
#This is called by Kitty_Clothes_Schedule when setting her outfit for a given day
#If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes
            
            menu:
                "That pink outfit, with the jeans.":
                    $ Count = 1
                "Your red shirt outfit.":
                    $ Count = 2
                "That outfit we put together [[custom]" if K_Custom[0] or K_Custom2[0] or K_Custom3[0] or K_Custom4[0] or K_Custom5[0] or K_Custom6[0] or K_Custom7[0]:
                            menu:
                                "Like, which?"
                                "The first one. (locked)" if not K_Custom[0]:
                                    pass
                                "The first one." if K_Custom[0]:
                                    if K_Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."
                                        
                                "The second one. (locked)" if not K_Custom2[0]:
                                    pass
                                "The second one." if K_Custom2[0]:
                                    if K_Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."
                                        
                                "The third one. (locked)" if not K_Custom3[0]:
                                    pass
                                "The third one." if K_Custom3[0]:
                                    if K_Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."

                                "The fourth one. (locked)" if not K_Custom4[0]:
                                    pass
                                "The fourth one." if K_Custom4[0]:
                                    if K_Custom4[0] == 2 or Count == 99:
                                        $ Count = 11
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."

                                "The fifth one. (locked)" if not K_Custom5[0]:
                                    pass
                                "The fifth one." if K_Custom5[0]:
                                    if K_Custom5[0] == 2 or Count == 99:
                                        $ Count = 12
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."

                                "The sixth one. (locked)" if not K_Custom6[0]:
                                    pass
                                "The sixth one." if K_Custom6[0]:
                                    if K_Custom6[0] == 2 or Count == 99:
                                        $ Count = 13
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."

                                "The seventh one. (locked)" if not K_Custom7[0]:
                                    pass
                                "The seventh one." if K_Custom7[0]:
                                    if K_Custom7[0] == 2 or Count == 99:
                                        $ Count = 14
                                    else:
                                        ch_k "I said I'm not[K_like]wearing that one out."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    $ Count = 4
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_k "Ok, sure, I'll wear that."
            else:
                        ch_k "I'll just wear whatever then."
            return Count    
#End Kitty Clothes Scheduling Check

#label Kitty_Clothes_Sleepwear: #fix fill this out
#            $ K_OutfitShame[4] = 50
            
#            if K_Chest == "tank":                                               #If she's wearing a bra of some kind
#                $ Count = 20
#            elif K_Chest == "buttoned tank":
#                $ Count = 15
#            elif K_Chest == "sports bra":
#                $ Count = 15
#            elif K_Chest == "bra":
#                $ Count = 10    
#            elif K_Chest == "lace bra":
#                $ Count = 5
#            else:     #K_Chest == 0:
#                if K_Pierce:
#                    $ Count = -5
#                else:
#                    $ Count = 0
            
#            if K_Over == "pink top":                                            #If she's wearing an overshirt 
#                $ Count += 15
#            elif K_Over == "hoodie":      
#                $ Count += 15
#            elif K_Over == "mesh top":      
#                $ Count += 5
#            elif K_Over == "towel":      
#                $ Count += 10
#            #else: nothing    
            
#            $ Count = 20 if Count >= 20 else Count
               
#            $ K_OutfitShame[4] -= Count                  #Set Outfit shame for the upper half    
#            $ Count = 0         
            
#            if not K_Legs or not K_Panties:                                     #If she's missing something on her legs        
#                        if K_Legs == "pants":                   #If wearing pants commando
#                            $ Count = 25
#                        elif K_Legs:                            #If wearing a skirt commando
#                            $ Count = 20
#                        elif K_Panties == "shorts":             #If wearing shorts
#                            $ Count = 25  
#                        elif K_Panties == "green panties":      #If wearing only green panties
#                            $ Count = 10
#                        elif K_Panties == "lace panties":       #If wearing only lace panties
#                            $ Count = 5
#                        elif K_Panties:                         #If wearing only any other panties
#                            $ Count = 7
#                        #else: nothing
                
#                        if HoseNum("Kitty") >= 10:
#                            $ Count = 25 if Count < 25 else Count
#                        elif HoseNum("Kitty") >= 5:            
#                            $ Count += 5        
                                
#                        if K_Over == "towel" and Count:         #If wearing a Towel and anything else
#                            $ Count = 25
#                        elif K_Over == "towel":                 #If just wearing a Towel
#                            $ Count = 15        
#            else:                                       #If wearing both legs and panties
#                        $ Count = 30        
                  
                
#            $ K_OutfitShame[4] -= Count                  #Set Outfit shame for the lower half
            
#            $ K_Sleepwear[0] = K_Gloves
#            $ K_Sleepwear[1] = K_Legs
#            $ K_Sleepwear[2] = K_Over
#            $ K_Sleepwear[3] = K_Neck
#            $ K_Sleepwear[4] = K_Chest
#            $ K_Sleepwear[5] = K_Panties 
#            $ K_Sleepwear[6] = K_Hose 
#            ch_k "Ok, this could work for sleepwear."
                
#            return
##End Kitty Sleepwear Set.



label Kitty_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call KittyFace("sexy", 1) 
            if "exhibitionist" in K_Traits:  
                        ch_k "Hmm, I'm getting excited. . ."  
                        if Custom == 5 and K_Custom2[0] == 2:
                            $ K_Outfit = "custom2"                    
                            $ K_Shame = K_OutfitShame[5]
                        elif Custom == 6 and K_Custom3[0] == 2:
                            $ K_Outfit = "custom3"                    
                            $ K_Shame = K_OutfitShame[6]
                        elif Custom == 11 and K_Custom4[0] == 2:
                            $ K_Outfit = "custom4"                    
                            $ K_Shame = K_OutfitShame[11]
                        elif Custom == 12 and K_Custom5[0] == 2:
                            $ K_Outfit = "custom5"                    
                            $ K_Shame = K_OutfitShame[12]
                        elif Custom == 13 and K_Custom6[0] == 2:
                            $ K_Outfit = "custom6"                    
                            $ K_Shame = K_OutfitShame[13]
                        elif Custom == 14 and K_Custom7[0] == 2:
                            $ K_Outfit = "custom7"                    
                            $ K_Shame = K_OutfitShame[14]
                        else: #if custom 1:
                            $ K_Outfit = "custom1"                    
                            $ K_Shame = K_OutfitShame[3]            
                        return    
            
            if Custom == 5 and K_Custom2[0] == 2:
                        $ K_Outfit = "custom2"   
            elif Custom == 6 and K_Custom3[0] == 2:
                        $ K_Outfit = "custom3"    
            elif Custom == 11 and K_Custom4[0] == 2:
                        $ K_Outfit = "custom4"    
            elif Custom == 12 and K_Custom5[0] == 2:
                        $ K_Outfit = "custom5"    
            elif Custom == 13 and K_Custom6[0] == 2:
                        $ K_Outfit = "custom6"    
            elif Custom == 14 and K_Custom7[0] == 2:
                        $ K_Outfit = "custom7"   
            elif K_Custom[0] == 2: #if custom 1:
                        $ K_Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ K_Shame = K_OutfitShame[Custom]          
                        if K_OutfitShame[Custom] >= 50:
                            ch_k "This is. . . kinda slutty. . ."
                        elif K_OutfitShame[Custom] >= 25:
                            ch_k "I'm not really comfortable with this one. . ."
                        elif K_OutfitShame[Custom] >= 15:
                            call KittyFace("bemused", 1) 
                            ch_k "I'll give it a shot. . ."
                        else:
                            ch_k "Yeah, I like that one too."
            else:
                        #She's decided not to wear this out
                        if K_OutfitShame[Custom] >= 50:
                            call KittyFace("angry", 1) 
                            ch_k "You have GOT to be kidding me here."
                        elif K_OutfitShame[Custom] >= 25:
                            call KittyFace("angry", 1) 
                            ch_k "This is just between us."
                        else:
                            call KittyFace("surprised", 1) 
                            ch_k "I can't wear this out!"  
            return
# End Kitty Custom Out
                                
                                
label Kitty_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):                                                                             #sets custom outfit    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 7
            
            if not Check and not Taboo:
                #if this is not a custom check and you're in a safe space,
                return
                        
            #If she's wearing a bra of some kind
            if K_Chest == "cami":  
                $ Count = 15
            elif K_Chest == "white cami":  
                $ Count = 15
            elif K_Chest == "sports bra":
                $ Count = 15
            elif K_Chest == "purple bikini bra":
                $ Count = 15
            elif K_Chest == "red bikini bra":
                $ Count = 15
            elif K_Chest == "orange top":
                $ Count = 25
            elif K_Chest == "black top":
                $ Count = 25
            elif K_Chest == "leather top":
                $ Count = 25
            elif K_Chest == "bra":
                $ Count = 10   
            elif K_Chest == "lace bra":
                $ Count = 5  
            elif K_Chest == "darker lace bra":
                $ Count = 5   
            elif K_Chest == "kitty lingerie top":
                $ Count = 5   
            elif K_Chest == "bustier bra":
                $ Count = 5
            else:     #K_Chest == 0
                if K_Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if K_Over == "pink top":                                             
                $ Count += 15
            elif K_Over == "dark top":                                             
                $ Count += 15
            elif K_Over == "red shirt":      
                $ Count += 20
            elif K_Over == "violet shirt scarfless":      
                $ Count += 20
            elif K_Over == "violet shirt scarf":      
                $ Count += 20
            elif K_Over == "purple shirt":      
                $ Count += 20
            elif K_Over == "black dress":                                             
                $ Count += 40
            elif K_Over == "towel":      
                $ Count += 10
            #else: nothing    
            
            call KittyFace("sexy", 0) 
            if Custom == 9:
                pass
            elif Count >= 20:
                $ Count = 20
                if Check:
                    ch_k "This is[K_like]totally a cute top."
            elif not Check:
                pass
            elif Count >= 10 and (ApprovalCheck("Kitty", 1200, TabM=0) or ApprovalCheck("Kitty", 500, "I", TabM=0)):  
                ch_k "Kinda hot top."        
            elif Count >= 10:
                ch_k "I wouldn't[K_like]feel comfortable in this top."
            elif Count >= 5 and (ApprovalCheck("Kitty", 2300, TabM=0) or ApprovalCheck("Kitty", 800, "I", TabM=0)):  
                ch_k "This top is is[K_like]kinda breezy. . ."        
            elif Count >= 5:        
                call KittyFace("startled", 1) 
                ch_k "This top is[K_like]way too slutty."
            elif (ApprovalCheck("Kitty", 2700, TabM=0) or ApprovalCheck("Kitty", 950, "I", TabM=0)):  
                ch_k "Is it hot in here? Whew. . ."        
            else:
                call KittyFace("bemused", 1) 
                ch_k "I wouldn't wear this out, but maybe indoors."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half    
            $ Count = 0         
            
            if K_Legs and K_Panties: 
                        $ Count = 30               
            else: #If she's missing something on her legs    
                        if PantsNum("Kitty") > 5:               #If wearing pants commando
                            $ Count = 25
                        elif PantsNum("Kitty") == 5:               #If wearing shorts commando
                            $ Count = 25 
                        # elif K_Legs == "shorts":                #If wearing shorts
                        #     $ Count = 20 
                        # elif K_Legs == "blue shorts":                #If wearing shorts
                        #     $ Count = 20 
                        # elif K_Legs == "white shorts":                #If wearing shorts
                        #     $ Count = 20 
                        elif PantsNum("Kitty") == 3:               #If wearing skirt commando
                            $ Count = 20 
                        # elif K_Legs == "orange skirt":                #If wearing shorts
                        #     $ Count = 20 
                        # elif K_Legs == "white skirt":                #If wearing shorts
                        #     $ Count = 20 
                        # elif K_Legs == "black skirt":                #If wearing shorts
                        #     $ Count = 20  
                        elif K_Legs:                            #If wearing anything else commando
                            $ Count = 20  
                        elif K_Panties == "purple bikini panties":      #If wearing only bikini purple
                            $ Count = 15      
                        elif K_Panties == "green panties":      #If wearing only green panties
                            $ Count = 10
                        elif K_Panties == "white panties":      #If wearing only green panties
                            $ Count = 10
                        elif K_Panties == "lace panties":       #If wearing only lace panties
                            $ Count = 5
                        elif K_Panties == "darker lace panties":       #If wearing only lace panties
                            $ Count = 5
                        elif K_Panties == "kitty lingerie panties":       #If wearing only kitty lingerie panties
                            $ Count = 5
                        elif K_Panties == "swimsuit3":
                            $ Count = 30
                        elif K_Panties == "zipper panties":
                            $ Count = 3
                        elif K_Panties:                         #If wearing only any other panties
                            $ Count = 1
                        #else: 0
                        
                        if HoseNum("Kitty") >= 10:
                            $ Count = 25 if Count < 25 else Count
                            
                        if K_Over == "towel" and Count:         #If wearing a Towel and anything else
                            $ Count = 25
                        elif K_Over == "towel":                 #If just wearing a Towel
                            $ Count = 15   
                            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass
            elif Custom == 9:
                        pass
            elif Count >= 20:
                        if PantsNum("Kitty") > 5:
                            ch_k "and these pants look cute on me."
                        elif PantsNum("Kitty") == 5:
                            ch_k "and these shorts look cute on me."
                        elif PantsNum("Kitty") == 3:
                            ch_k "and this is a cute skirt."
                        
                        # elif K_Legs == "shorts":
                        #     ch_k "and these are cute shorts." 
                        # elif K_Legs == "blue shorts":
                        #     ch_k "and these are cute shorts." 
                        # elif K_Legs == "white shorts":
                        #     ch_k "and these are cute shorts." 
                        # elif K_Legs == "orange skirt":
                        #     ch_k "and this is a cute skirt." 
                        # elif K_Legs == "white skirt":
                        #     ch_k "and this is a cute skirt." 
                        # elif K_Legs == "black skirt":
                        #     ch_k "and this is a cute skirt."  
                        elif HoseNum("Kitty") >= 10:
                            ch_k "I guess these [K_Hose] will work fine."
                        else:
                            ch_k "The towel's an odd choice. . ."
                        if not K_Panties and ApprovalCheck("Kitty", 500, "I", TabM=0):
                            ch_k "I like going without panties."           
                        elif not K_Panties:
                            ch_k "It's a little uncomfortable without panties."
                    
            elif Count >= 10 and (ApprovalCheck("Kitty", 2000, TabM=0) or ApprovalCheck("Kitty", 700, "I", TabM=0)):
                    ch_k "I'm not sure about the coverage down here. . ."        
            elif Count >= 10:
                    call KittyFace("angry", 1) 
                    ch_k "I'm barely covered down here. . ."                
            elif (ApprovalCheck("Kitty", 2500, TabM=0) or ApprovalCheck("Kitty", 800, "I", TabM=0)):  
                    ch_k "kinda chilly. . ."        
            else:
                    ch_k "if it's just[K_like]you and me. . ."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check
                    if Custom == 7:
                        ch_p "So would you work out in that?"
                    elif Custom == 9:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                        
                    call KittyFace("sexy", 0) 
                    if Taboo >= 40: #K_Loc != "bg player" and K_Loc != "bg kitty": 
                        call KittyFace("confused",1) 
                        $ K_Mouth = "smile"
                        ch_k "Kinda late to ask, right?" 
                    elif "exhibitionist" in K_Traits and Tempshame <= 20:        
                        ch_k "I'm getting wet just thinking about it. . ."
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 10)
                    elif Tempshame <= 5:
                        call KittyFace("smile") 
                        ch_k "Sure, it's a cute look!"
                    elif Tempshame <= 15 and (ApprovalCheck("Kitty", 1700, TabM=0, C = 0) or ApprovalCheck("Kitty", 400, "I", TabM=0, C = 0)):        
                        ch_k "It's pretty hot, right?"
                    elif Custom == 9:
                        #if it's sleepwear      
                        call KittyFace("bemused", 1) 
                        if Tempshame >= 30:
                            ch_k "This is[K_like]pretty exposed, but ok."  
                        elif Tempshame >= 15:
                            ch_k "It's kinda naughty, I like it."  
                        else:
                            ch_k "Yeah, these are fine."                        
                    elif Tempshame <= 15:  
                        call KittyFace("bemused", 1) 
                        ch_k "It's kinda slutty to wear out."
                        $ Agree = 0
                    elif Tempshame <= 25 and (ApprovalCheck("Kitty", 2300, TabM=0, C = 0) or ApprovalCheck("Kitty", 700, "I", TabM=0, C = 0)):
                        ch_k "So sexy, but I can handle it."
                    elif Tempshame <= 25:
                        call KittyFace("angry", 1) 
                        ch_k "{i}Way{/i} too sexy for outside."
                        $ Agree = 0
                    elif (ApprovalCheck("Kitty", 2500, TabM=0, C = 0) or ApprovalCheck("Kitty", 800, "I", TabM=0, C = 0)):
                        call KittyFace("bemused", 1) 
                        ch_k "OMG, I can't believe I'm doing this."
                    else:
                        call KittyFace("angry", 1) 
                        ch_k "I - can't - even."
                        $ Agree = 0
                        
                    $ K_OutfitShame[Custom] = Tempshame                     
                    if Custom == 5:
                            $ K_Custom2[1] = K_Gloves  
                            $ K_Custom2[2] = K_Legs 
                            $ K_Custom2[3] = K_Over
                            $ K_Custom2[5] = K_Chest 
                            $ K_Custom2[6] = K_Panties
                            $ K_Custom2[8] = K_Hair
                            $ K_Custom2[9] = K_Hose
                            $ K_Custom2[0] = 2 if Agree else 1           
                    elif Custom == 6:
                            $ K_Custom3[1] = K_Gloves  
                            $ K_Custom3[2] = K_Legs 
                            $ K_Custom3[3] = K_Over
                            $ K_Custom3[5] = K_Chest 
                            $ K_Custom3[6] = K_Panties
                            $ K_Custom3[8] = K_Hair
                            $ K_Custom3[9] = K_Hose
                            $ K_Custom3[0] = 2 if Agree else 1           
                    elif Custom == 11:
                            $ K_Custom4[1] = K_Gloves  
                            $ K_Custom4[2] = K_Legs 
                            $ K_Custom4[3] = K_Over
                            $ K_Custom4[5] = K_Chest 
                            $ K_Custom4[6] = K_Panties
                            $ K_Custom4[8] = K_Hair
                            $ K_Custom4[9] = K_Hose
                            $ K_Custom4[0] = 2 if Agree else 1           
                    elif Custom == 12:
                            $ K_Custom5[1] = K_Gloves  
                            $ K_Custom5[2] = K_Legs 
                            $ K_Custom5[3] = K_Over
                            $ K_Custom5[5] = K_Chest 
                            $ K_Custom5[6] = K_Panties
                            $ K_Custom5[8] = K_Hair
                            $ K_Custom5[9] = K_Hose
                            $ K_Custom5[0] = 2 if Agree else 1           
                    elif Custom == 13:
                            $ K_Custom6[1] = K_Gloves  
                            $ K_Custom6[2] = K_Legs 
                            $ K_Custom6[3] = K_Over
                            $ K_Custom6[5] = K_Chest 
                            $ K_Custom6[6] = K_Panties
                            $ K_Custom6[8] = K_Hair
                            $ K_Custom6[9] = K_Hose
                            $ K_Custom6[0] = 2 if Agree else 1           
                    elif Custom == 14:
                            $ K_Custom7[1] = K_Gloves  
                            $ K_Custom7[2] = K_Legs 
                            $ K_Custom7[3] = K_Over
                            $ K_Custom7[5] = K_Chest 
                            $ K_Custom7[6] = K_Panties
                            $ K_Custom7[8] = K_Hair
                            $ K_Custom7[9] = K_Hose
                            $ K_Custom7[0] = 2 if Agree else 1
                    elif Custom == 7 and Agree:
                            $ K_Gym[1] = K_Gloves  
                            $ K_Gym[2] = K_Legs 
                            $ K_Gym[3] = K_Over
                            $ K_Gym[5] = K_Chest 
                            $ K_Gym[6] = K_Panties
                            $ K_Gym[8] = K_Hair
                            $ K_Gym[9] = K_Hose
                            $ K_Gym[0] = 2   
                    elif Custom == 9:                            
                            $ K_Sleepwear[1] = K_Gloves  
                            $ K_Sleepwear[2] = K_Legs 
                            $ K_Sleepwear[3] = K_Over
                            $ K_Sleepwear[4] = K_Neck 
                            $ K_Sleepwear[5] = K_Chest 
                            $ K_Sleepwear[6] = K_Panties
                            $ K_Sleepwear[8] = K_Hair
                            $ K_Sleepwear[9] = K_Hose
                            $ K_Sleepwear[0] = 2 if Agree else 1   
                    else: #Typically Custom == 3
                            $ K_Custom[1] = K_Gloves  
                            $ K_Custom[2] = K_Legs 
                            $ K_Custom[3] = K_Over
                            $ K_Custom[5] = K_Chest 
                            $ K_Custom[6] = K_Panties
                            $ K_Custom[8] = K_Hair
                            $ K_Custom[9] = K_Hose
                            $ K_Custom[0] = 2 if Agree else 1
                    #End check    
            $ K_Shame = Tempshame
            
            if Check:
                    pass
            elif "exhibitionist" in K_Traits: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif K_Over == "towel" and K_Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Kitty", 1700) or ApprovalCheck("Kitty", 600, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and K_Loc == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 20 and K_Loc == "bg pool": 
                    #If the outfit is light but she's in the pool
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Kitty", 2300) or ApprovalCheck("Kitty", 800, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Kitty", 2600) or ApprovalCheck("Kitty", 950, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif Custom == 9 and not Taboo:
                    pass
            elif K_Over == "black dress":
                    pass
            elif K_Loc == "bg showerroom":
                    ch_k "One sec, I gotta change real quick."
                    $ K_Outfit = renpy.random.choice(["pink outfit", "red outfit"])
                    #$ K_Water = 0
                    call KittyOutfit(Changed = 1) 
                    ch_k "I wouldn't want to be seen like that."
            else:
                    ch_k "One sec, I gotta change real quick."
                    $ K_Outfit = renpy.random.choice(["pink outfit", "red outfit"])
                    $ K_Water = 0
                    call KittyOutfit(Changed = 1) 
                    ch_k "I wouldn't want to be seen like that."
                    
            return        

#End Kitty Custom clothes check.
    
# start kitty hungry //////////////////////////////////////////////////////////
label Kitty_Hungry:
    if K_Chat[3]:
        ch_k "You know, a kitty does like her milk. . ."
    elif K_Chat[2]:
        ch_k "You know, that serum of yours really has a kick to it. You should market that stuff!"
    else:
        ch_k "You know, a kitty does like her milk. . ."
    $ K_Traits.append("hungry")
return


# end kitty hungry //////////////////////////////////////////////////////////

label KittyLike:
    
    menu:
        ch_k "So[K_like]what would you prefer I say then?"
        "Like":
            $ K_like = ", like, "
            $ K_Like = "Like, "
            ch_k "I guess I do[K_like]say that alot, huh?"           
        "Um":
            $ K_like = ", um, "
            $ K_Like = "Um, "
            ch_k "[K_Like]if you say so."
        "So, uh":
            $ K_like = ", uh, "
            $ K_Like = "So, "
            ch_k "[K_Like]I guess I could[K_like]use that more."
        "Nyaa":
            if ApprovalCheck("Kitty", 1400):
                $ K_like = ", nyaa, "
                $ K_Like = "Nyaa, "
                ch_k "[K_Like]you are such a dork."
            elif ApprovalCheck("Kitty", 1000, "LO"):
                $ K_like = ", nyaa, "
                $ K_Like = "Nyaa, "
                ch_k "[K_Like]if that's what you want."
            else:
                ch_k "[K_Like]no way, weirdo."                
        "Fucking":
            if ApprovalCheck("Kitty", 400, "I"):
                $ K_like = " fucking "
                $ K_Like = "Fucking "            
                ch_k "[K_Like]yeah I will."            
            elif ApprovalCheck("Kitty", 1000, "LO"):
                $ K_like = " fucking "
                $ K_Like = "Fucking "            
                ch_k "If you[K_like]say so."    
            else:    
                ch_k "I don't fucking think so."
                ch_k ". . .most of the time."   
        "Nothing":
            if ApprovalCheck("Kitty", 900, "LO"):
                $ K_like = " "
                $ K_Like = ". . . "
                ch_k "[K_Like] ok . . ."
            else:
                ch_k "I don't[K_like]think I could do that." 
    
    return
    
    
# Start Kitty first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Kitty_First_Les(0,1)
    if K_Les:
        return
    
    $ K_Les += 1
    $ K_RecentActions.append("lesbian")        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Kitty's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_k "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I Sugar, but it seemed like fun."
                else:
                    ch_r "It's all right Sugar, I'll take care of you."
        if K_LikeRogue >= 60 and ApprovalCheck("Kitty", (1500-(10*K_Les)-(10*(K_LikeRogue-60)))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Kitty", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif K_LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
                $ State = "lesbian"
        
        
        
        
        
        if "cockout" in P_RecentActions:
                call KittyFace("down", 2) 
                if GirlsNum:
                    "Kitty also glances down at your cock"
                else:
                    "Kitty glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        
        if Taboo and not ApprovalCheck("Kitty", 1500):
                call KittyFace("surprised", 2) 
                ch_k "Um, you should[K_like]put that away in public."
                call KittyFace("bemused", 1) 
                if K_SeenPeen == 1: 
                    ch_k "Or[K_like]maybe. . ."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)                
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 20)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 35)  
                    
        elif K_SeenPeen > 10:
                return    
        elif ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "L"):
                call KittyFace("sly",1) 
                if K_SeenPeen == 1: 
                    call KittyFace("surprised",2) 
                    ch_k "That's. . . impressive."
                    call KittyFace("bemused",1) 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3) 
                elif K_SeenPeen == 2:  
                    ch_k "I can't get over that."               
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7) 
                elif K_SeenPeen == 5: 
                    ch_k "There it is."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5)  
                elif K_SeenPeen == 10: 
                    ch_k "So beautiful."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
        else:
                call KittyFace("sad",1) 
                if K_SeenPeen == 1: 
                    call KittyFace("perplexed",1 ) 
                    ch_k "Well that happened. . ."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                elif K_SeenPeen < 5: 
                    call KittyFace("sad",0) 
                    ch_k "Huh."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                elif K_SeenPeen == 10: 
                    ch_k "[K_Like]put that away."               
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if K_SeenPeen > 10:
                    return
                elif ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "L"):
                        if K_SeenPeen == 1: 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3) 
                        elif K_SeenPeen == 2:              
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7) 
                        elif K_SeenPeen == 5: 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5)  
                        elif K_SeenPeen == 10: 
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)  
                else:
                        if K_SeenPeen == 1: 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                        elif K_SeenPeen < 5: 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                        elif K_SeenPeen == 10:              
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                            
    if K_SeenPeen == 1:            
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)                
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 25)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 20) 
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)
    
    return
# End Kitty first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   

label Kitty_Show_Plug:
    
    menu:
        "Slap her ass.":
            $ D20A = renpy.random.randint(1, 20) #Sets random seed factor for the encounter

            show Slap_Ass2 zorder 200
            call K_Slap_Ass 
            hide Slap_Ass2
            if Taboo and (D20A + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                call Kitty_Taboo 
            jump Kitty_Show_Plug
            

        "Very happy.":
            pass

    return

label Kitty_Swimsuit_Change_Top:
    if K_Chest != "swimsuit3":
        return

    if ApprovalCheck("Kitty", 900) and (K_Legs or (K_SeenPussy and not Taboo)):
        #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
        
        if ApprovalCheck("Kitty", 850, "L"):               
                ch_k "Well, if you ask me nicely. . ."
        elif ApprovalCheck("Kitty", 500, "O"):
                ch_k "For you, ok."
        elif ApprovalCheck("Kitty", 350, "I"):
                ch_k "[[snort]."
        else:
                ch_k "Yeah, I guess."         
    else:                       #low approval or not wearing pants or in public 
        if ApprovalCheck("Kitty", 1100, "LI", TabM=3) and K_Love > K_Inbt:               
                ch_k "Well, not that I mind you seeing it. . ."
        elif ApprovalCheck("Kitty", 700, "OI", TabM=3) and K_Obed > K_Inbt:
                ch_k "I guess. . ."
        elif ApprovalCheck("Kitty", 600, "I", TabM=3):
                ch_k "Hrmm. . ."
        elif ApprovalCheck("Kitty", 1300, TabM=3):
                ch_k "Okay, okay."
        else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                if Taboo:
                    ch_k "Not in public, [K_Petname]!"
                else:
                    ch_k "I don't like you that much, [K_Petname]!"
                jump Kitty_Clothes_Under_Top  
    
    $ K_Panties = 0  
    return


label Kitty_Swimsuit_Change_Bottom:
    if K_Panties != "swimsuit3":
        return

    if K_SeenChest and ApprovalCheck("Kitty", 900, TabM=2.7):
        ch_k "Sure."    
    elif ApprovalCheck("Kitty", 1100, TabM=2):
        if Taboo:
            ch_k "I'm kind of nervous. . ."
        else:
            ch_k "If it's just you. . ."
    elif K_Over == "pink top" or K_Over == "dark top" and ApprovalCheck("Kitty", 600, TabM=2):
        ch_k "This look is a bit revealing. . ."  
    elif K_Over == "red shirt" or K_Over == "purple shirt" or K_Over == "violet shirt scarfless" or K_Over == "violet shirt scarf" and ApprovalCheck("Kitty", 500, TabM=2):
        ch_k "I guess I could. . ."  
    elif not K_Over:
        ch_k "Not without a little coverage, for modesty."
        jump Kitty_Clothes_Under_Panties 
    else:
        ch_k "I don't think so, [K_Petname]."
        jump Kitty_Clothes_Under_Panties 

    $ K_Chest = 0
    return

label Kitty_Remove_Swimsuit:
    if K_Chest != "swimsuit3":
        return

    if ApprovalCheck("Kitty", 900) and (K_Legs or (K_SeenPussy and not Taboo)):
        #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
        
        if ApprovalCheck("Kitty", 850, "L"):               
                pass
        elif ApprovalCheck("Kitty", 500, "O"):
                pass
        elif ApprovalCheck("Kitty", 350, "I"):
                pass
        else:
                pass
    else:                       #low approval or not wearing pants or in public 
        if ApprovalCheck("Kitty", 1100, "LI", TabM=3) and K_Love > K_Inbt:               
                pass
        elif ApprovalCheck("Kitty", 700, "OI", TabM=3) and K_Obed > K_Inbt:
                pass
        elif ApprovalCheck("Kitty", 600, "I", TabM=3):
                pass
        elif ApprovalCheck("Kitty", 1300, TabM=3):
                pass
        else: 
                call KittyFace("surprised") 
                $ K_Brows = "angry"
                if Taboo:
                    ch_k "Not in public, [K_Petname]!"
                else:
                    ch_k "I don't like you that much, [K_Petname]!"
                jump Kitty_Clothes_Under_Top  
    
    call Kitty_Remove_Swimsuit_Top 
    $ K_Panties = 0  
    return

label Kitty_Remove_Swimsuit_Top:

    if K_SeenChest and ApprovalCheck("Kitty", 900, TabM=2.7):
        ch_k "Sure."    
    elif ApprovalCheck("Kitty", 1100, TabM=2):
        if Taboo:
            ch_k "I'm kind of nervous. . ."
        else:
            ch_k "If it's just you. . ."
    elif K_Over == "pink top" or K_Over == "dark top" and ApprovalCheck("Kitty", 600, TabM=2):
        ch_k "This look is a bit revealing. . ."  
    elif K_Over == "red shirt" or K_Over == "purple shirt" or K_Over == "violet shirt scarfless" or K_Over == "violet shirt scarf" and ApprovalCheck("Kitty", 500, TabM=2):
        ch_k "I guess I could. . ."  
    elif not K_Over:
        ch_k "Not without a little coverage, for modesty."
        jump Kitty_Clothes_Under_SwimSuits 
    else:
        ch_k "I don't think so, [K_Petname]."
        jump Kitty_Clothes_Under_SwimSuits 

    $ K_Chest = 0
    return
