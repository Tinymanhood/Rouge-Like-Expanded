   
label NewGirl_Noticed(Girl_ = "Mystique", Other = "Rogue", B = 0):
    if "noticed rogue" in newgirl[Girl_].RecentActions and Other == "Rogue":
            return
    if "noticed kitty" in newgirl[Girl_].RecentActions and Other == "Kitty":
            return
    if "noticed emma" in newgirl[Girl_].RecentActions and Other == "Emma":
            return
    
    call NewGirl_Face(Girl_,"surprised", 1) from _call_NewGirl_Face_332

    if Other == "Rogue":            
            "[Girl_] noticed what you and Rogue are up to."
            $ newgirl[Girl_].RecentActions.append("noticed rogue")
            if "poly rogue" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeRogue - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200
    elif Other == "Kitty":            
            "[Girl_] noticed what you and Kitty are up to."
            $ newgirl[Girl_].RecentActions.append("noticed kitty")
            if "poly kitty" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeKitty - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200

    elif Other == "Emma":            
            "[Girl_] noticed what you and Emma are up to."
            $ newgirl[Girl_].RecentActions.append("noticed emma")
            if "poly emma" in newgirl[Girl_].Traits:
                    $ B = (1000-(20*Taboo))  
            else:
                    $ B = (newgirl[Girl_].LikeEmma - 500)
                    if "dating" in newgirl[Girl_].Traits:
                        $ B -= 200

    elif Other in ModdedGirls:            
            call NewGirl_Face(Girl_, "surprised", 1) from _call_NewGirl_Face_333
            "[Girl_] noticed what you and [Other] are up to."
            $ newgirl[Girl_].RecentActions.append("noticed " + Other)
            $ PolyVariable = "poly " + Other
            if PolyVariable in newgirl[Girl_].Traits:
                $ B = (1000-(20*Taboo))  
            else:
                $ B = (newgirl[Girl_].LikeNewGirl[Other] - 500)               
                if "dating" in newgirl[Girl_].Traits:
                    $ B -= 200
                        
    $ Partner = Girl_
    if ApprovalCheck(Girl_, 2000, TabM=2, Bonus = B) or ApprovalCheck(Girl_, 950, "L", TabM=2, Bonus = (B/3)):
            #if she's very loose or really likes you
            call NewGirl_Face(Girl_,"sexy", 1) from _call_NewGirl_Face_334
            "She decides to join you."                                      
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 5)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 5) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 3) 
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other) 
            call NewGirl_Threeway_Set(Girl_) from _call_NewGirl_Threeway_Set
    elif ApprovalCheck(Girl_, 650, "O", TabM=2) and ApprovalCheck(Girl_, 450, "L", TabM=1) or ApprovalCheck(Girl_, 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call NewGirl_Face(Girl_,"sexy") from _call_NewGirl_Face_335
            "She takes a seat off to the side and watches."          
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 5) 
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 5)  
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 2)  
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other)
            call NewGirl_Threeway_Set(Girl_, "watch") from _call_NewGirl_Threeway_Set_1
    elif ApprovalCheck(Girl_, 650, "I", TabM=2) and ApprovalCheck(Girl_, 450, "L", TabM=1) or ApprovalCheck(Girl_, 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call NewGirl_Face(Girl_,"sexy") from _call_NewGirl_Face_336
            "She sits down and watches you intently."             
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 5) 
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 2)
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)     
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 5) 
            if Other == "Rogue" and "poly rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly rogue") 
            elif Other == "Kitty" and "poly kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly kitty") 
            elif Other == "Emma" and "poly emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly emma") 
            elif Other and ("poly " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("poly " + Other)
            call NewGirl_Threeway_Set(Girl_, "watch") from _call_NewGirl_Threeway_Set_2
    elif ApprovalCheck(Girl_, 1500, TabM=2, Bonus = B):
            call NewGirl_Face(Girl_,"perplexed", 1) from _call_NewGirl_Face_337
            "She looks a little annoyed, but she stays and watches."
            if newgirl[Girl_].Love >= newgirl[Girl_].Obed and newgirl[Girl_].Love >= newgirl[Girl_].Inbt:
                $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 2)
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)                     
            elif newgirl[Girl_].Obed >= newgirl[Girl_].Inbt:
                $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 2) 
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2)   
            else:
                $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, 2) 
                $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, 1)
                $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 1) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 90, 5)
            call NewGirl_Threeway_Set(Girl_, "watch") from _call_NewGirl_Threeway_Set_3
    elif ApprovalCheck(Girl_, 650, "L", TabM=1) or ApprovalCheck(Girl_, 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call NewGirl_Face(Girl_,"angry", 2) from _call_NewGirl_Face_338                
            if bg_current == ("bg " + Girl_): 
                    "She looks betrayed, and kicks you both out of the room."
            else:
                    "She looks betrayed, and storms out of the room."                   
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 200, -5) 
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 80, -5) 
            $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 70, -5) 
            $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 89, 10) 
            if Other == "Rogue" and "saw with rogue" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with rogue") 
            elif Other == "Kitty" and "saw with kitty" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with kitty")
            elif Other == "Emma" and "saw with emma" not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with emma") 
            elif Other and ("saw with " + Other) not in newgirl[Girl_].Traits: 
                    $ newgirl[Girl_].Traits.append("saw with " + Other) 
            $ Partner = 0
            if bg_current == ("bg " + Girl_): #Kicks you out if in Girl_'s room
                    $ newgirl[Girl_].RecentActions.append("angry")
                    call GirlsAngry from _call_GirlsAngry_13
            call Remove_Girl(Girl_) from _call_Remove_Girl_67
    else:
            #if she doesn't like you much
            call NewGirl_Face(Girl_,"surprised", 2) from _call_NewGirl_Face_339
            $ newgirl[Girl_].Inbt = Statupdate(Girl_, "Inbt", newgirl[Girl_].Inbt, 90, 2) 
            $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 40, 20)
            if Trigger != "kissing":
                    $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, -10) 
                    $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
                    $ newgirl[Girl_].Lust = Statupdate(Girl_, "Lust", newgirl[Girl_].Lust, 80, 10)
            if bg_current == ("bg " + Girl_):
                    $ newgirl[Girl_].Love = Statupdate(Girl_, "Love", newgirl[Girl_].Love, 90, -5) 
                    $ newgirl[Girl_].Obed = Statupdate(Girl_, "Obed", newgirl[Girl_].Obed, 90, -5)
                    "She looks annoyed, and shoves you both out of the room."                 
            elif Trigger != "kissing":
                "She looks annoyed, and storms out of the room." 
            else:
                "She looks a bit disgusted and walks away."                                  
            $ Partner = 0      
            if bg_current == ("bg " + Girl_): #Kicks you out if in Girl_'s room
                    $ newgirl[Girl_].RecentActions.append("angry")
                    call GirlsAngry from _call_GirlsAngry_14
            call Remove_Girl(Girl_) from _call_Remove_Girl_68
    return

label NewGirl_Face(Girl_ = "Mystique", Emote = "normal", B = 0, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
        if (newgirl[Girl_].Forced or "angry" in newgirl[Girl_].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl[Girl_].ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "angry"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "confused"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl[Girl_].Mouth = "tongue"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "surprised"
                $ newgirl[Girl_].Blush = 1
        elif Emote == "sad":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl[Girl_].Mouth = "lipbite"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl[Girl_].Mouth = "sucking"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl[Girl_].Mouth = "smirk"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "grimace":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "laugh":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
            
        if M:
                $ newgirl[Girl_].Eyes = "surprised"        
        if B > 1:
                $ newgirl[Girl_].Blush = 2
        elif B:
                $ newgirl[Girl_].Blush = 1
        else:
                $ newgirl[Girl_].Blush = 0
        
        if Mouth:
                $ newgirl[Girl_].Mouth = Mouth
        if Eyes:
                $ newgirl[Girl_].Eyes = Eyes
        if Brows:
                $ newgirl[Girl_].Brows = Brows
        
        return


label NewGirl_FaceSpecial(Girl_ = "Mystique", Emote = "normal", B = 0, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
            
        if Emote == "normal":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "angry"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl[Girl_].Mouth = "normal"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "confused"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl[Girl_].Mouth = "tongue"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "surprised"
                $ newgirl[Girl_].Blush = 1
        elif Emote == "sad":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl[Girl_].Mouth = "lipbite"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl[Girl_].Mouth = "sucking"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl[Girl_].Mouth = "kiss"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "surprised"
                $ newgirl[Girl_].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl[Girl_].Mouth = "sad"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl[Girl_].Mouth = "smile"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl[Girl_].Mouth = "smirk"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "grimace":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "normal"
                $ newgirl[Girl_].Eyes = "squint"
        elif Emote == "laugh":
                $ newgirl[Girl_].Mouth = "grimace"
                $ newgirl[Girl_].Brows = "sad"
                $ newgirl[Girl_].Eyes = "closed"
            
        if M:
                $ newgirl[Girl_].Eyes = "surprised"        
        if B > 1:
                $ newgirl[Girl_].Blush = 2
        elif B:
                $ newgirl[Girl_].Blush = 1
        else:
                $ newgirl[Girl_].Blush = 0
        
        if Mouth:
                $ newgirl[Girl_].Mouth = Mouth
        if Eyes:
                $ newgirl[Girl_].Eyes = Eyes
        if Brows:
                $ newgirl[Girl_].Brows = Brows
        
        return

label NewGirl_Threeway_Set(Girl_ = "Mystique", Preset = 0, Mode = 0, Action = Trigger4, ActiveGirl = Primary, State = "watcher", TempLust = 0, TempLust2 = 0, TempFocus = 0):
    # Action defaults to Trigger4, the action of the seondary girl and ActiveGirl to the lead girl in the scene
    # In lesbian mode, Action becomes Trigger3, the secondary action of the primary girl, and ActiveGirl is the secondary girl
    # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
    # for Lesbian: NewGirl_Threeway_Set("activity", "lesbian", Trigger3, Girl)
    # for Threeway: NewGirl_Threeway_Set("activity", 0, Trigger4, Girl)
    
            if Mode == "lesbian" and Trigger3:
                    #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                    if 5 <= D20S <= 15:
                            return
                    if Trigger3 == "kissing" and K_Lust <= 30:
                            # If kissing at low lust, keep doing it
                            return
            elif Trigger4 and D20S < 10 and Trigger4 != "watch": 
                    #If there is a trigger, it's not set to "watch," and the roll is good, continue
                    return
                    
            $ Options = ["watch", "masturbation", "masturbation", "masturbation"]
                        
            if Trigger == "lesbian":
                    $ State = "lesbian"
                    if Secondary != Girl_:
                            $ ActiveGirl = Secondary
                    $ Options = ["kiss girl","kiss girl","fondle ass"]                    
            elif not ApprovalCheck(Girl_, 500, "I"): # If Girl_ is too timid to do anything
                    pass
            elif Primary == "Rogue":
                    if newgirl[Girl_].LikeRogue >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeRogue-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl[Girl_].LikeRogue >= 700: #if she doesn't like you but likes Rogue, lesbian
                            $ State = "lesbian"
            elif Primary == "Kitty":
                    if newgirl[Girl_].LikeKitty >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeKitty-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl[Girl_].LikeKitty >= 700: #if she doesn't like you but likes Kitty, lesbian
                            $ State = "lesbian"
            elif Primary == "Emma":
                    if newgirl[Girl_].LikeKitty >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeKitty-60)))): #If she likes both of you a lot, threeway
                            $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                            $ State = "hetero"            
                    elif newgirl[Girl_].LikeKitty >= 700: #if she doesn't like you but likes Kitty, lesbian
                            $ State = "lesbian"
            else:
                #$ k = 0
                #while k < len(ModdedGirls):
                if Primary in ModdedGirls and Primary != Girl_:
                    if newgirl[Girl_].LikeOtherGirl[Primary] >= 500 and ApprovalCheck(Girl_, (1300-(10*newgirl[Girl_].Les)-(10*(newgirl[Girl_].LikeOtherGirl[Primary]-60)))): #If she likes both of you a lot, threeway
                        $ State = "threeway"
                    elif ApprovalCheck(Girl_, 1000): #If she likes you well enough, Hetero
                        $ State = "hetero"            
                    elif newgirl[Girl_].LikeOtherGirl[Primary] >= 700: #if she doesn't like you but likes Kitty, lesbian
                        $ State = "lesbian"    
                    #$ k += 1
            
            
            if State == "lesbian" or State == "threeway":
                $ Options.extend(("fondle breasts","suck breasts","fondle pussy","fondle ass","kiss girl")) 
                if ActiveGirl == "Rogue":
                            if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeRogue >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeRogue >= 800:
                                $ Options.append("lick ass")  
                elif ActiveGirl == "Kitty":
                            if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeKitty >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeKitty >= 800:
                                $ Options.append("lick ass") 
                elif ActiveGirl == "Emma":
                            if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeEmma >= 700:
                                $ Options.append("lick pussy")
                            if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeEmma >= 800:
                                $ Options.append("lick ass") 
                else:
                    # $ k = 0
                    # while k < len(ModdedGirls):
                    if ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                        if ApprovalCheck(Girl_, 800, "I") or newgirl[Girl_].LikeOtherGirl[ActiveGirl] >= 700:
                            $ Options.append("lick pussy")
                        if ApprovalCheck(Girl_, 900, "I") and newgirl[Girl_].LikeOtherGirl[ActiveGirl] >= 800:
                            $ Options.append("lick ass")     
                        # $ k += 1
                    
            if State == "hetero" or State == "threeway":
                    $ Options.extend(("hand","blow","kiss you"))                 
            $ renpy.random.shuffle(Options)
            
            if Preset in Options:
                    #if the suggested action is in the possible actions. . .
                    $ Options[0] = Preset 
                    ch_m "Oh, very well. . ."
            elif Preset:
                    ch_m "That doesn't really seem appropriate. . ."
                    
            #Sets opening lines. . .
            if Options[0] == Action:                          
                    #If it's the same result, just hop back
                    return
            elif Mode == "lesbian":
                    $ Line = Girl_ + " shifts her position"
            elif not Trigger4 or Trigger4 == "masturbation":    
                    #If this is the first action,
                    $ Line = Girl_ + " moves closer"            
            else:                                              
                    #If this is a new action
                    $ Line = Girl_ + " shifts her position"
                    
                    
            if Options[0] == "masturbation":
                        $ Action = "masturbation"  
                        if Trigger != "lesbian" and Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                                #Clear out Trigger 5 if it's for kissing.  
                                $ Trigger5 = 0 
                        call NewGirl_Self_Lines(Girl_,"T5",Trigger5) from _call_NewGirl_Self_Lines_1
            elif Options[0] == "hand":
                        $ Line = Line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "hand"   
                        
                        $ TempFocus += 3 if P_Focus > 70 else 2                              
                        $ TempLust += 2 if newgirl[Girl_].Lust < 60 else 0
                        $ TempLust += 2 if newgirl[Girl_].Hand > 2 else 0
                        $ newgirl[Girl_].Addict -= 1 if D20S > 10 else 2
            elif Options[0] == "blow":
                        $ Line = Line + " before she slides down and begins to slowly lick your cock"
                        $ Action = "blow"  
                        
                        $ TempFocus += 20 if P_Focus > 60 else 10                      
                        $ TempLust += 2 if newgirl[Girl_].Lust > 80 else 1  
                        $ newgirl[Girl_].Addict -= 2
            #the above three do not apply to lesbian actions.
                        
            elif Options[0] == "fondle breasts":
                        # call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slides her hands along " + ActiveGirl + "'s breasts" 
                        $ Action = "fondle breasts"   
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if R_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Kitty": #If Girl_ is fondling Kitty's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if K_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if E_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 2
                        $ TempFocus += 1 
            elif Options[0] == "suck breasts":
                        # call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slurps " + ActiveGirl + "'s nipple into her mouth" 
                        $ Action = "suck breasts"    
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 4 if R_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Kitty": #If Girl_ is sucking Kitty's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if K_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if E_LikeNewGirl[Girl_] >= 800 else 2
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 2
                        $ TempFocus += 1  
            elif Options[0] == "fondle pussy":
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her finger along " + ActiveGirl + "'s pussy" 
                        $ Action = "fondle pussy"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian")                         
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if R_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl == "Kitty": #If Girl_ is stroking Kitty's pussy
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if K_LikeNewGirl[Girl_] >= 800 else 3
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if E_LikeNewGirl[Girl_] >= 800 else 3
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 2 if ApprovalCheck(Girl_, 500, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 3
                        $ TempFocus += 2  
            elif Options[0] == "lick pussy":
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her tongue along " + ActiveGirl + "'s pussy" 
                        $ Action = "lick pussy"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if R_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl == "Kitty": #If Girl_ is licking Kitty's pussy
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if K_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if E_LikeNewGirl[Girl_] >= 800 else 4
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 3 if ApprovalCheck(Girl_, 600, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 7 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 4
                        $ TempFocus += 3  
            elif Options[0] == "fondle ass": 
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and gives " + ActiveGirl + "'s ass a firm squeeze" 
                        $ Action = "fondle ass" 
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian")                         
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if R_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl == "Kitty": #If Girl_ is fondling Kitty's ass
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if K_LikeNewGirl[Girl_] >= 600 else 1
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if E_LikeNewGirl[Girl_] >= 600 else 1
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 1 if ApprovalCheck(Girl_, 400, "I") else 0  # Girl_'s lust
                                $ TempLust2 += 3 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 600 else 1
                        $ TempFocus += 1  
            elif Options[0] == "lick ass":
                        # call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and starts to lick around " + ActiveGirl + "'s ass" 
                        $ Action = "lick ass"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if R_LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if R_Loose > 1 else 0
                        elif ActiveGirl == "Kitty": #If Girl_ is licking Kitty's ass
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if K_LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if K_Loose > 1 else 0
                        elif ActiveGirl == "Emma": #If Girl_ is fondling Emma's breasts
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if E_LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if E_Loose > 1 else 0
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 3 if ApprovalCheck(Girl_, 800, "I") else 1  # Girl_'s lust
                                $ TempLust2 += 5 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 2
                                $ TempLust2 += 2 if newgirl[ActiveGirl].Loose > 1 else 0
                        $ TempFocus += 2  
                        
            elif Options[0] == "kiss girl" or Mode == "lesbian":   
                        # call RThreewayBreasts_Launch #Launches position change                                
                        $ Line = Line + " and gives " + ActiveGirl + " a passionate kiss" #use T5 on this to choose targets
                        $ Action = "kissing"  
                        if Mode != "lesbian":
                            if "kiss you" in Options:
                                $ Trigger5 = "kiss both" 
                            else:
                                $ Trigger5 = "kiss girl"  
                        if "lesbian" not in newgirl[Girl_].RecentActions:
                                $ newgirl[Girl_].Les += 1
                                $ newgirl[Girl_].RecentActions.append("lesbian") 
                        if ActiveGirl == "Rogue": #If Girl_ is kissing Rogue
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeRogue >= 800 else 0
                                $ TempLust2 += 2 if R_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl == "Kitty": #If Girl_ is kissing Kitty
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeKitty >= 800 else 0
                                $ TempLust2 += 2 if K_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl == "Emma": #If Girl_ is Kissing Emma
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeEmma >= 800 else 0
                                $ TempLust2 += 2 if E_LikeNewGirl[Girl_] >= 800 else 1
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 800 else 0
                                $ TempLust2 += 2 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 1
                        $ TempFocus += 1  
            elif Options[0] == "kiss you":   
                        # call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and gives you a passionate kiss" #use T5 on this to choose targets
                        $ Action = "kissing"   
                        if "kiss girl" in Options:
                            $ Trigger5 = "kiss both" 
                            if "lesbian" not in newgirl[Girl_].RecentActions:
                                    $ newgirl[Girl_].Les += 1
                                    $ newgirl[Girl_].RecentActions.append("lesbian")                                     
                            if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeRogue >= 800 else 0
                                    $ TempLust2 += 2 if R_LikeNewGirl[Girl_] >= 800 else 1
                            elif ActiveGirl == "Kitty": #If Girl_ is kissing Kitty
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeKitty >= 800 else 0
                                    $ TempLust2 += 2 if K_LikeNewGirl[Girl_] >= 800 else 1
                            elif ActiveGirl == "Emma": #If Girl_ is Kissing Emma
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeEmma >= 800 else 0
                                    $ TempLust2 += 2 if E_LikeNewGirl[Girl_] >= 800 else 1
                            elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                    $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                    $ TempLust += 1 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 800 else 0
                                    $ TempLust2 += 2 if newgirl[ActiveGirl].LikeNewGirl[Girl_] >= 800 else 1
                            $ TempFocus += 1 
                        else:
                            $ Trigger5 = "kiss you" 
                        $ TempLust += 1 
                        $ TempFocus += 1 
                        
            # elif Options[0] == "dildo pussy":  
            # elif Options[0] == "dildo ass":        
            # elif Options[0] == "vibrator":    

            else:
                        "[Girl_] is just watching the two of you intently."
                        $ Action = "watch"
                        if ActiveGirl == "Rogue": #If Girl_ is fondling Rogue's breasts
                                $ TempLust += 1 if newgirl[Girl_].LikeRogue >= 600 else 0  # Girl_'s lust
                                $ TempLust += 2 if newgirl[Girl_].LikeRogue >= 800 else 1  # Girl_'s lust
                                $ TempLust2 += 1 if ApprovalCheck("Rogue", 500, "I") else 0
                                $ TempLust2 += 1 if ApprovalCheck("Rogue", 700, "I") else 0
                        elif ActiveGirl == "Kitty": #If Girl_ is watching Kitty
                                $ TempLust += 1 if newgirl[Girl_].LikeKitty >= 600 else 0  # Girl_'s lust
                                $ TempLust += 2 if newgirl[Girl_].LikeKitty >= 800 else 1  # Girl_'s lust
                                $ TempLust2 += 1 if ApprovalCheck("Kitty", 500, "I") else 0
                                $ TempLust2 += 1 if ApprovalCheck("Kitty", 700, "I") else 0
                        elif ActiveGirl == "Emma": #If Girl_ is watching Emma
                                $ TempLust += 1 if newgirl[Girl_].LikeEmma >= 600 else 0
                                $ TempLust += 2 if newgirl[Girl_].LikeEmma >= 800 else 1
                                $ TempLust += 1 if ApprovalCheck("Emma", 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if ApprovalCheck("Emma", 700, "I") else 0  # Girl_'s lust
                        elif ActiveGirl in ModdedGirls and ActiveGirl != Girl_:
                                $ TempLust += 1 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 600 else 0
                                $ TempLust += 2 if newgirl[Girl_].LikeNewGirl[ActiveGirl] >= 800 else 1
                                $ TempLust += 1 if ApprovalCheck(Girl_, 500, "I") else 0  # Girl_'s lust
                                $ TempLust += 1 if ApprovalCheck(Girl_, 700, "I") else 0  # Girl_'s lust
                        $ TempFocus += 1 
                 
            # Wrap-up
            $ TempLust2 += 2       
            if Mode == "lesbian":
                #Sets Primary Girl's secondary action
                $ Trigger3 = Action
                $ PrimaryLust += TempLust
                $ SecondaryLust += TempLust2
            else:
                #Sets Secondary girl's action
                $ Trigger4 = Action
                $ SecondaryLust += TempLust
                $ PrimaryLust += TempLust2
            $ P_Focus += TempFocus

            return

label NewGirl_Self_Lines(Girl_ = "Mystique", Mode = "T3", Action = Trigger3, TempLustX = 0): 
    # The Mode can be T3 for Trigger 3 for a masturbation option, or T5/Trigger5 if it's setting a Threeway action. 
    # call NewGirl_Self_Lines("T5",Trigger5) 
    # This sets a Action if there isn't one, or sets an initial line
    $ Line = 0
    if not Action or D20S >= 15: 
            if Trigger != "masturbation" and "passive" in newgirl[Girl_].Traits:
                    # This bypasses self-set if Girl_ is told not to take initiative
                    $ Line = 0
                    return            
            call Mystique_Self_Set(Mode, Action) from _call_Mystique_Self_Set
            
            if Mode == "T3": #Sets Action based on the result
                    $ Action = Trigger3
            else: #if Mode == "T5"
                    $ Action = Trigger5  
            if not Action: 
                    return
            elif (newgirl[Girl_].Over == "bondage" or newgirl[Girl_].Over == "bondage cuffs" or newgirl[Girl_].Over == "armbinder") and not Line:
                    $ Line = "Also, " + Girl_ + "continues stroke your cock. "
            elif Action == "hand" and not Line: 
                    $ Line = "Also, " + Girl_ + " continues stroke your cock. "
            elif not Line:        
                    $ Line = "Also, " + Girl_ + " continues to masturbate. "      
    elif Action == "hand": 
            $ Line = "" + Girl_ + " continues stroke your cock. "
    elif newgirl[Girl_].Over == "bondage" or newgirl[Girl_].Over == "bondage cuffs" or newgirl[Girl_].Over == "armbinder": 
            $ Line = renpy.random.choice(["" + Girl_ + " tries to move her arms around. ", 
                    "" + Girl_ + " can't keep still. ",
                    "" + Girl_ + " can't keep still. "])
    else:       
            $ Line = renpy.random.choice(["" + Girl_ + " continues to masturbate. ", 
                    "" + Girl_ + "'s hands move across her body. ",
                    "" + Girl_ + " continues to feel herself. ",
                    "" + Girl_ + " can't keep still. "]) 
            
    if Action == "hand": 
            $ Line = Line + renpy.random.choice(["She lightly strokes the shaft, fingers sliding along the vein", 
                    "She grasps the shaft firmly, and slowly slides along its length", 
                    "She's becoming something of a handjob expert, making up for years of lost time",
                    "Her expert strokes will have you boiling over in seconds",
                    "She strokes the shaft vigorously, lightly touching the tip",
                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                    "Her hand slides slowly down your shaft"]) 
            $ TempFocus += 10 if P_Focus > 60 else 4
            $ TempFocus += 2 if newgirl[Girl_].Hand > 2 else 0
                    
            $ TempLustX += 2 if newgirl[Girl_].Lust < 60 else 1
            $ TempLustX += 2 if newgirl[Girl_].Hand > 2 else 0
            $ newgirl[Girl_].Addict -= 1            
    else:
        if newgirl[Girl_].Lust >= 80:   
            if Action == "fondle pussy":
                    $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her mound, firmly stroking her clit", 
                            "She inserts two fingers into her dripping pussy and rapidly pistons them",
                            "She gasps as her fingers bury themselves deeply inside her",
                            "She gives a little squeal as she pinches her clit between her fingers",           
                            "She fingers move quickly across her mound, constantly sliding across her clit",
                            "She fingers move rapidly up and down her inner thighs and belly, building towards their center",
                            "She spreads her lower lips and furiously strokes the inner lining",
                            "She alternately dives her fingers into herself, and licks the juices off of them",
                            "She slides two fingers firmly in and out of her tight gap as she massages the clit with her palm",
                            "She rapidly circles her fingers against her erect clit",
                            "She quickly slides a finger up and down the crease of her pussy", 
                            "She lets out a moan as her fingers brush against her erect clit"])
            elif Action == "dildo pussy":
                    $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it", 
                            "She hungrily slams the dildo into her tight pussy, and pistons it in and out",
                            "She shoves the dildo firmly in and out of her grasping pussy",               
                            "She quickly slides the phallus up and down her crease"])
            elif Action == "fondle ass":
                    $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her ass, firmly stroking her tight hole", 
                            "She inserts a finger deep into her grasping hole and rapidly pistons it",
                            "She gasps as she buries a finger deeply into her tight anus",
                            "She gives a little squeal as she pinches her clit between her fingers",           
                            "Her fingers move quickly across her ass, constantly sliding across her rim",
                            "Her fingers move rapidly up and down her inner thighs and ass, building towards their center",
                            "She spreads her cheeks and furiously strokes the puckered rim",
                            "She slides two fingers firmly in and out of her tight hole",
                            "She rapidly circles her fingers against the sensitive rim",
                            "She lets out a moan as her fingers brush against her quivering hole"])
            elif Action == "dildo anal":
                    $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her ass, firmly rubbing into it", 
                            "She hungrily slams the dildo into her tight hole, and pistons it in and out",
                            "She shoves the dildo firmly in and out of her grasping asshole",               
                            "She quickly slides the phallus up and down the crease of her ass"])
            elif Action == "vibrator pussy":
                    $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                            "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                            "She slides the buzzing egg into her dripping pussy and tugs it in and out",    
                            "She presses the vibrator firmly against her clit and a shiver runs through her",                
                            "Her whirring toy is dragged up and down her inner thighs, slowing building towards their center",
                            "She  spreads her lower lips and runs the device along the inner lining",
                            "She presses the toy deep into her and the vibrations send a shock through her body"])
            else: # Action == "fondle breasts"
                    $ Line = Line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                            "Her hands squeeze at her breasts, massaging them firmly with both hands",                 
                            "She hungrily cups her breasts and moves them in rapid circles",
                            "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                            "She firmly pinches her nipples and gives them steady tugs",
                            "She passionately rubs her breasts, desperately tugging at her nipples"])     
            #End newgirl[Girl_].Lust >= 80
            
                
        elif newgirl[Girl_].Lust >= 50:   
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her mound, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly across her delta, occasionally grazing her lips",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides a finger up and down the crease of her pussy", 
                                "She lets out a gasp as her fingers brush against her erect clit"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",  
                                "She traces the rubber phallus slowly down her body, barely grazing her mound",  
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",                
                                "She gently slides the phallus up and down the crease of her pussy", 
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her ass, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly along her crack, occasionally grazing her asshole",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her cheeks and caresses the tight hole within",
                                "She gently slides a finger up and down the crease of ass", 
                                "She lets out a gasp as her fingers brush against her puckered hole"]) 
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",                  
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "Her hands firmly caress her breasts, massaging them in circular motions",
                                "Her hands move along her breasts, carefully caressing them",
                                "She gasps as her finger brushes against an erect nipple"])
                #End newgirl[Girl_].Lust >= 50
                
        else: #if newgirl[Girl_].Lust < 50:      
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely grazing her mound", 
                                "Her fingers move lightly across her pubic region, subtly avoiding her lips",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "Her hands move along her sides, carefully caressing them"])  
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her mound",                 
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely passing smoothly across her hips", 
                                "Her fingers move lightly across her crack, subtly avoiding her rosebud",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "Her hands move along her sides, carefully caressing them"])              
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowing building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])   
                #End newgirl[Girl_].Lust 0-60
        #End Girl_ Action masturbation dialog        
                        
            
        # Girl_ Self-stat boosts  
        $ TempLustX += 4 if newgirl[Girl_].Lust > 80 else 0        
        $ TempLustX += 5 if newgirl[Girl_].Lust < 40 else 3                   #Bonus if she is relatively low lust
        $ TempLustX += 5 if Trigger == "masturbation" else 0     #Bonus if masturbation is her primary action
        
        if Primary == Girl_: #If this is a primary, Trigger3 action
            $ TempLust = TempLustX
        else: #If this is a Secondary, Trigger5 action
            $ TempLust2 = TempLustX
        
        $ TempFocus += 3         
        $ TempFocus += 1 if P_Focus < 50 else 0 
        
    #End Girl_ Action all dialog     
    
    return

label NewGirl_Dirty_Talk(D20=0, TempCheck=0, Line=0):    
    $ D20 = renpy.random.randint(1, 20)   
    if D20 >= 15 and Secondary:
            #if it's a high roll and there is a second girl, do a threesome line
            #$ Line = "threesome" #fix this when there are threesome lines to add.
            $ Line = "partner"
    elif D20 >= 10 and Secondary:
            #if it's a medium roll and there is a second girl, do a partner line
            $ Line = "partner"
    else:
            #if it's a lower roll, do a single girl line. Primary
            $ Line = "primary"
        
    #Rogue    
    $ D20 = renpy.random.randint(1, 20)   
    if Primary == "Rogue" or (Line == "partner" and Secondary == "Rogue" and D20 >= 15):
            #If the primary is Rogue or Rogue is the Partner
            if D20 <= 5 or (R_SEXP <= 30 and ApprovalCheck("Rogue", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "Touching ya is so amazing, " + R_Petname + ".",
                            "Every time you touch me. . .it's like, I can't even put it into words.",
                            "Mmmm. . .right there.",
                            "Ya like that, " + R_Petname + "?"
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "I want ya so bad, " + R_Petname + ".",
                                "I'm all yours, " + R_Petname + ". Take me however ya want.",
                                "I love it when ya do that, " + R_Petname + ".",
                                "I love the look you get on your face when we do that, " + R_Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Rogue":
                        #if Rogue is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Rogue is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "Seems like you like this, huh, " + R_Petname + "?" #hand
                    elif TempCheck == "blow":
                        $ Line = "You taste so nice, " + R_Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Ohhh. . .that's sooo good." #sex
                    elif TempCheck == "anal":
                        $ Line = "It. . .hurts. But it kinda feels good, too." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "I want ya so bad, " + R_Petname + ".",
                                "I'm all yours, " + R_Petname + ". Take me however ya want.",
                                "I love it when ya do that, " + R_Petname + ".",
                                "I love the look you get on your face when we do that, " + R_Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_r "[Line]"
    #end Primary Rogue        
            
    elif Primary == "Kitty" or (Line == "partner" and Secondary == "Kitty" and D20 >= 15):
            if D20 <= 5 or (K_SEXP <= 30 and ApprovalCheck("Kitty", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "You're so amazing, " + K_Petname + ".",
                            "You know how to push, like, every one of my buttons. . .",
                            "Heh. . .{i}somebody{/i} seems to like that.",
                            "That's, like, {i}so{/i} good."
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + K_Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + K_Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + K_Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Kitty":
                        #if Kitty is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Kitty is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "I love the way it, like, feels in my hands." #hand
                    elif TempCheck == "blow":
                        $ Line = "I hope you don't think I'm, like, a slut for saying this. . .but I love how you taste, " + K_Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Oooohh. . .just like {i}that{/i}." #sex
                    elif TempCheck == "anal":
                        $ Line = "Please. . .go slow, 'kay?  You feel so {i}big{/i}." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + K_Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + K_Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + K_Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_k "[Line]"
                        
    #end Primary Kitty  

    elif Primary == "Emma" or (Line == "partner" and Secondary == "Emma" and D20 >= 15):
            if D20 <= 5 or (E_SEXP <= 30 and ApprovalCheck("Emma", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "You're incredible, " + E_Petname + ".",
                            "You're surprisingly skilled at this. . .",
                            "Well, that certainly got a positive response.",
                            "Exceptional work, darling.",
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "I'm overwhelmed, " + E_Petname + ".",
                                "Well now we have another skill to develop, " + E_Petname + ".",                                        
                                "Oooh, that's lovely. . .",
                                "More, I want more!",
                                "You're simply adorable, " + E_Petname + ".",
                                "Ooh, you'll {i}have{/i} to do that one again. . .",
                                "You certainly do leave an impression, " + E_Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Emma":
                        #if Emma is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Emma is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "I love the way it, like, feels in my hands." #hand
                    elif TempCheck == "blow":
                        $ Line = "I hope you don't think I'm, like, a slut for saying this. . .but I love how you taste, " + E_Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Oooohh. . .just like {i}that{/i}." #sex
                    elif TempCheck == "anal":
                        $ Line = "Please. . .go slow, 'kay?  You feel so {i}big{/i}." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + E_Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + E_Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + E_Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_e "[Line]"
                        
    #end Primary Emma  

    elif Primary == "Mystique" or (Line == "partner" and Secondary == "Mystique" and D20 >= 15):
            if D20 <= 5 or (newgirl["Mystique"].SEXP <= 30 and ApprovalCheck("Mystique", 400, "I")):
                    #If she's relatively inexperienced or there is a low roll
                    $ Line = renpy.random.choice([
                            "You're so amazing, " + newgirl["Mystique"].Petname + ".",
                            "You know how to push, like, every one of my buttons. . .",
                            "Heh. . .{i}somebody{/i} seems to like that.",
                            "That's, like, {i}so{/i} good."
                            ])
            elif D20 <= 15: 
                    #If she's relatively experienced and there's a moderate roll
                    $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + newgirl["Mystique"].Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + newgirl["Mystique"].Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + newgirl["Mystique"].Petname + "."
                                ])
            else: #a 15+ roll and experienced
                    if Primary == "Mystique":
                        #if Mystique is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger
                    else:
                        #if Mystique is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                    
                    if TempCheck == "hand":
                        $ Line = "I love the way it, like, feels in my hands." #hand
                    elif TempCheck == "blow":
                        $ Line = "I hope you don't think I'm, like, a slut for saying this. . .but I love how you taste, " + newgirl["Mystique"].Petname + "." #blow
                    elif TempCheck == "sex":
                        $ Line = "Oooohh. . .just like {i}that{/i}." #sex
                    elif TempCheck == "anal":
                        $ Line = "Please. . .go slow, 'kay?  You feel so {i}big{/i}." #anal
                    else:
                        #if it's none of those, this will work
                        $ Line = renpy.random.choice([
                                "This is {i}so{/i} hot, " + newgirl["Mystique"].Petname + ".",
                                "I think I just, like, discovered one of your other mutant powers, " + newgirl["Mystique"].Petname + ".",
                                "I like it.  Like, a {i}lot{/i}.",
                                "I've never wanted a guy like I want you, " + newgirl["Mystique"].Petname + "."
                                ])
            if Line and Line != "partner":
                    ch_m "[Line]"
                        
    #end Primary Mystique  

    return

label NewGirl_RemoveClothes(Girl_ = "Mystique"):
    
    $ newgirl[Girl_].Over = 0
    $ newgirl[Girl_].Legs = 0
    $ newgirl[Girl_].Chest = 0
    $ newgirl[Girl_].Panties = 0
    $ newgirl[Girl_].Neck = 0
    $ newgirl[Girl_].Hose = 0
    $ newgirl[Girl_].Glasses = 0

    return

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////