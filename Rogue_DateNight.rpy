# Date Night //////////////////////////////////////////////////////////////////////
# Count = price of things
# Count2 = tempmod

label Rogue_Date_Night:
    call Shift_Focus("Rogue")
    if "askeddate" in R_RecentActions:  
        call RogueFace("angry")
        ch_r "I think you got your answer already."  
        return 
    $ R_RecentActions.append("askeddate")    
    
    
    if R_Break[0] and "ex" in R_Traits:
        call RogueFace("angry")
        ch_r "Seriously? You're asking me that after what you just did?"  
        return           
    elif ApprovalCheck("Rogue", 1200) and "ex" in R_Traits:
        call RogueFace("bemused")
        $ R_Brows = "sad"
        if "no summon" in R_RecentActions:  
            ch_r "I was kinda busy, but I'd like to get out. . ." 
        else:
            ch_r "We had some fun, I guess we could go out, as friends maybe."        
        if "deadbeat" in R_History:  
            call RogueFace("angry")
            $ R_Mouth = "grimace"
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
            ch_r "You're paying though!"
            call RogueFace("bemused")            
    elif "ex" in R_Traits:
        call RogueFace("angry")
        $ R_Eyes = "side"                
        ch_r "I don't think we really worked out, [R_Petname]." 
        return 
    elif "deadbeat" in R_History:  
        call RogueFace("angry")             
        menu:
            ch_r "Remember last time, when you made me pay?" 
            "Sorry about that, I'll take care of the check this time.":
                if ApprovalCheck("Rogue", 650):
                    call RogueFace("sad")
                    "Ok, [R_Petname], you'd better."
                else:
                    call RogueFace("angry")
                    "Yeah, I'm not buy'in that hogwash, [R_Petname]." 
                    return
            "Yeah, so?":
                if ApprovalCheck("Rogue", 1400):
                    call RogueFace("angry")                    
                    $ R_Mouth = "grimace"
                    ch_r "It's a good thing you're so pretty."
                    call RogueFace("bemused")        
                elif ApprovalCheck("Rogue", 500, "O"):
                    call RogueFace("surprised")
                    ch_r ". . ."
                    call RogueFace("sad")
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
                    ch_r "I. . . guess I can pick up the check again. . ."
                elif ApprovalCheck("Rogue", 650):
                    call RogueFace("angry")
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2) 
                    ch_r "\"So\" it looks like we won't be going out again."  
                    return 
                else:
                    call RogueFace("angry")
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2) 
                    ch_r "Fuck off."  
                    return             
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 2)
    elif ApprovalCheck("Rogue", 650):
        call RogueFace("smile")
        if "no summon" in R_RecentActions:  
            ch_r "I was kinda busy, but I'd like to get out. . ." 
        else:
            ch_r "Yeah, sounds good. Where did you want to take me, [R_Petname]?"
    elif ApprovalCheck("Rogue", 400):                
        call RogueFace("angry")
        $ R_Eyes = "side"
        ch_r "I think I'm washing my hair tonight. . ."
        return
    else:
        call RogueFace("angry")
        ch_r "Yeah, you wish."
        return              
    $ renpy.pop_call()                
    $ Taboo = 40
    if R_Schedule[7]:
        # if she has a date outfit set
        if R_Schedule[7] == 2:
            $ R_Outfit = "evo_pink"
        elif R_Schedule[7] == 3:
            $ R_Outfit = "custom1"
        elif R_Schedule[7] == 4:
            $ R_Outfit = "gym"
        elif R_Schedule[7] == 5:
            $ R_Outfit = "custom2"
        elif R_Schedule[7] == 6:
            $ R_Outfit = "custom3"
        else:
            $ R_Outfit = "evo_green"
    else:
        $ Options = ["evo_pink", "evo_green"]
        $ Options.append("custom1") if R_Custom[0] == 2 else Options
        $ Options.append("custom2") if R_Custom2[0] == 2 else Options
        $ Options.append("custom3") if R_Custom3[0] == 2 else Options
        $ renpy.random.shuffle(Options) 
        $ R_Outfit = Options[0]
        $ del Options[:]  
    call CleartheRoom("Rogue",0,1) 
    $ R_Loc = "date"
    $ bg_current = "date"  
    call RogueOutfit(Changed=1)       
    call Set_The_Scene
    menu:
        ch_r "Where would you like to go?"
        "To the movies.":
            $ R_RecentActions.append("movie")                      
            $ R_DailyActions.append("movie") 
        "To a restaurant.":
            $ R_RecentActions.append("dinner")                      
            $ R_DailyActions.append("dinner") 
        "Dinner and a movie.":
            $ R_RecentActions.append("movie")                      
            $ R_DailyActions.append("movie") 
            $ R_RecentActions.append("dinner")                      
            $ R_DailyActions.append("dinner") 
        "Never Mind.":
            call RogueFace("sad")
            ch_r "Oh, ok. Maybe some other time then."
            call RogueFace
            jump Rogue_Chat            
    ch_r "Ok, that sounds like fun."
    show blackscreen onlayer black with dissolve
    $ Count = 0
    $ Party = []
    
if "dinner" not in R_RecentActions:
    "You head to the local theater and check out the film listings."
    jump R_Date_Movies
    
label R_Date_Dinner:
    "You go to one of the nicer restaurants in town. The food is quality but reasonably affordable." 
    $ bg_current = "bg restaurant"
    $ R_Loc = "bg restaurant"
    call Set_The_Scene
    
    menu:
        "You order. . ."
        "Surf and turf for you and Rogue. ($20 each)":
            call RogueFace("smile")
            $ R_Brows = "surprised"
            ch_r "Ooh, you're really pulling out the stops here."  
            call RogueFace
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 2)
            $ Count = 20
            $ Line = "steak and a juicy lobster"
        "Steak for the both of you. ($15 each)":  
            call RogueFace("smile")
            ch_r "I love a big, juicy steak."
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
            $ Count = 15
            $ Line = "medium rare ribeye"
        "Chicken for both of you. ($10 each)":
            call RogueFace("smile")
            ch_r "I could always go for some chicken."
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
            $ Count = 10
            $ Line = "pangrilled chicken thighs"
        "Just a salad for each of you. ($5 each)":
            $ R_Mouth = "sad"
            $ R_Eyes = "sexy"
            $ R_Brows = "confused"            
            ch_r "Well, I guess salad isn't that bad. . ."  
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -5)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            $ Count = 5
            $ Line = "fresh garden salad"
        "Why don't you choose, Rogue?":
            call RogueFace("smile")
            ch_r "Well thanks, [R_Petname]. I think we'll have the chicken."            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)        
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            $ Count = 10
            $ Line = "pangrilled chicken thighs"
            
    "You eat your meals" # add options here
    $ Line = "You eat your "+ Line + ", and have a pleasant conversation over the meal."
    "[Line]"    
    call RogueFace("sexy", 1)
    if R_Anal and ApprovalCheck("Rogue", 1500) and Count >=15:        
        "Halfway through the meal, Rogue gets a sly look on her face, nods her head suggestively towards the restrooms, and then excuses herself."
        "A few seconds later, you follow her and she drags you inside, locking the door behind you. She spends the next several minutes taking it up the ass."
        ch_r "I hope I'll still be able to sit down later."  
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 9)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3)
        $ R_Anal += 1
        $ R_SeenPeen += 1
        $ P_Semen -= 1        
        $ R_RecentActions.append("anal")                      
        $ R_DailyActions.append("anal") 
    elif R_Sex and ApprovalCheck("Rogue", 1500) and Count >=10:
        "Halfway through the meal, Rogue gets a sly look on her face, nods her head suggestively towards the restrooms, and then excuses herself."
        "A few seconds later, you follow her and she drags you inside, locking the door behind you. She spends the next several minutes fucking you raw."
        ch_r "I needed to work off that meal a bit."
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 8)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
        $ R_Sex += 1
        $ R_SeenPeen += 1
        $ P_Semen -= 1            
        $ R_RecentActions.append("sex")                      
        $ R_DailyActions.append("sex") 
    elif R_Blow and ApprovalCheck("Rogue", 1300) and Count >=10:
        "Halfway through the meal, Rogue gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants. She then procedes to blow you for several minutes until you cum."
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 6)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
        $ R_RecentActions.append("blow")                      
        $ R_DailyActions.append("blow") 
        if R_Swallow:
            "Rogue wipes her mouth as she climbs out from under the table."
            ch_r "I don't think we need desert, [R_Petname]."            
            $ R_Addict -= 20
            $ R_Swallow += 1  
            $ R_RecentActions.append("swallow")                      
            $ R_DailyActions.append("swallow")       
        else:
            "Rogue grabs the napkin off your lap and uses it to collect the jiz."
            ch_r "I bet the cleaning crew will enjoy that."
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 4)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
        $ R_SeenPeen += 1
        $ R_Blow += 1
        $ P_Semen -= 1
    elif R_Hand and ApprovalCheck("Rogue", 1000) and Count >=10:
        "Halfway through the meal, Rogue gets a sly look on her face, then shifts her chair around next to yours."
        "She unzips your pants under the table, and proceeds to caress your cock, stroking it until you cum into the napkin."
        ch_r "I bet the cleaning crew will enjoy that."
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 4)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
        $ R_Hand += 1
        $ P_Semen -= 1
        $ R_RecentActions.append("hand")                      
        $ R_DailyActions.append("hand") 
    elif R_FondleP and ApprovalCheck("Rogue", 1000) and Count >=10:
        "Halfway through the meal, Rogue gets a sly look on her face, then shifts her chair around next to yours."
        if R_Legs == "pants":
            "She takes your hand and pulls it over to her crotch, shoving it down her pants. You can feel that she's warm as a furnace."
        else:
            "She takes your hand and pulls it down to her crotch, shoving it under her skirt. You can feel that she's warm as a furnace."
        "You stroke her pussy for several minutes, until finally she shudders in orgasm and slowly pulls your hand free with a sly smile."
        ch_r "I needed to take a bit of the edge off, [R_Petname]."
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 3)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 5)            
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2)
        $ R_FondleP += 1
        $ R_Org += 1
        $ R_RecentActions.append("fondle pussy")                      
        $ R_DailyActions.append("fondle pussy") 
    elif ApprovalCheck("Rogue", 1000) and Count >=10:
        "Halfway through the meal, Rogue gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock. After several minutes of this, she pulls back."
        ch_r "Just a little downpayment on later, [R_Petname]."
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3)
    call RogueFace(B = 0)
    
    call R_Date_Paying 
    if Count2 >= 30:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 15)   
    elif Count2 >= 20:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 10)     
    elif Count2 >= 10:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5) 
    
    if "movie" not in R_RecentActions:
        "After dinner, you head back to the dorms and escort Rogue to her room."       
        jump R_Date_End
        
    #else:    
    "After dinner, you head to the local theater and check out the film listings."   
        
label R_Date_Movies:    
    $ bg_current = "bg movies"
    $ R_Loc = "bg movies"
    call Set_The_Scene 
    $ Count = 10
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
    menu:
        "What would you like to see?"
        "A romantic comedy.":
            call RogueFace("smile")
            $ R_Eyes = "surprised"
            ch_r "Oooh, I love a good rom-com, [R_Petname]. This should be great!"   
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 95, 4)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
            $ Count2 += 5
            $ R_RecentActions.append("romcom") 
        "An action movie.":
            call RogueFace("sexy")
            ch_r "Hmm, you know I'm always up for some action." 
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 95, 3)
            $ Count2 += 5
            $ R_RecentActions.append("action") 
        "A horror movie.":
            call RogueFace("sad")
            $ R_Eyes = "surprised"
            ch_r "I'm not really into the spooky stuff, [R_Petname]."                
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -3)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
            $ Count2 += 15
            $ R_RecentActions.append("horror") 
        "An acclaimed drama.":
            call RogueFace("bemused")
            ch_r "Hmmm, I have heard some good things about this one, could be interesting."   
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 95, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
            $ Count2 += 20
            $ R_RecentActions.append("drama") 
        "Let Rogue pick.":
            call RogueFace("smile")
            ch_r "How sweet, [R_Petname]. Let's see the romantic comedy."            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 4)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
            $ R_RecentActions.append("romcom") 
            
    call R_Date_Paying      
    if Count2 >= 50:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 25) 
    elif Count2 >= 40:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 20)  
    elif Count2 >= 30:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 15)   
    elif Count2 >= 20:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 10)     
    elif Count2 >= 10:
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5)   
                
    if "romcom" in R_RecentActions:      
        $ Count += 2
        $ Line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one.", 
                    "You watch the movie, which is about a girl is mercilessly stalked by some weird guy until she eventually decides she loves him. They live hapily ever after.", 
                    "In this movie, the lead goes to all her friend's weddings, but can't get it together herself. She dies alone. Just kidding, she gets married at the end.", 
                    "You watch the movie, in which a bunch of college girls go on a wild adventure and have lots of random sex.",
                    "This movie is about a girl who's convinced to live in a sex dungeon, and really seems to enjoy it.",
                    "This movie is about a girl who works for a fashion house and is bullied by her boss, until they become friends."])        
    elif "action" in R_RecentActions: 
        $ Count += 1
        $ Line = renpy.random.choice(["You watch the movie, which is about an ex marine fighting aliens.", 
                    "You watch the movie, which is about a girl is mercilessly stalked by some weird guy until she eventually decides she loves him. They live hapily ever after. There are also a lot of explosions.", 
                    "In this movie, giant robots are fighting animal mash-ups, with the fate of the world in the balance.", 
                    "You watch the movie, in which a team of non-mutant superhumans are apparently fighting some sort of silvery robots in Eastern Europe.",
                    "This movie is about a superhuman powerhouse that nearly wrecks a town, and yet is not arrested for it by the humans. Must be the hammer.",
                    "This movie is about 90 minutes of constant explosions and lensflares."])
    elif "horror" in R_RecentActions: 
        $ Count += 4
        $ Line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one. The guys are a fishman and a skeleton.", 
                    "You watch the movie, which is about a girl is mercilessly stalked by some weird guy until she eventually gives in and marries him. Her life is an endless hell.", 
                    "In this movie, a group of teens are trapped in a wilderness cabin. They have a lot of random sex as some shadowy monster kills them one by one.", 
                    "In this movie, a group of teens are trapped in an abandoned motel. They have a lot of random sex as some shadowy monster kills them one by one.", 
                    "This movie is about a girl who's convinced to live in a sex dungeon, and she's eventually murdered.",
                    "In this movie, a group of teens are trapped in a spaceship. They have a lot of random sex as some shadowy monster kills them one by one."])
    elif "drama" in R_RecentActions: 
        $ Count += 5
        $ Line = renpy.random.choice(["You watch the movie, which is about a mature woman who can't choose between two eligible widowers. She picks the other one.", 
                    "You watch the movie, which is a documentary about a girl is mercilessly stalked by some weird guy until she eventually decides she gets a restraining order.", 
                    "In this movie, which is a biopic about a great historical leader.", 
                    "You watch the movie, in which a disabled person struggles with his various disabilities, and eventually overcomes them, and/or dies.",
                    "This movie is about a lot of yelling and crying as some very serious issues are explored by an ensemble cast."])
    "[Line]"
    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if (D20 + Count) >= 10 and ApprovalCheck("Rogue", 500, Bonus=(10*Count2)):
        call RogueFace("kiss", 1)
        if "romcom" in R_RecentActions: 
            "Halfway through the movie, inspired by the action on screen, Rogue turns to you and starts to make out with you."
        elif "action" in R_RecentActions:        
            "Halfway through the movie, adrenaline pumping from the action on screen, Rogue turns to you and starts to make out with you."
        elif "horror" in R_RecentActions:  
            "Halfway through the movie, freaked out by the tension on screen, Rogue huddles in your arms, and then starts to make out with you."
        elif "drama" in R_RecentActions:   
            "Halfway through the movie, profoundly bored by the movie, Rogue turns to you with a shrug and starts to make out with you."
        $ R_RecentActions.append("kissing")                      
        $ R_DailyActions.append("kissing") 
    
        if R_Anal and ApprovalCheck("Rogue", 2000, Bonus=(10*Count2)) and R_Legs != "pants":
            call RogueFace("sexy", 1)
            if R_Panties:
                "As you make out, Rogue reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
            else:
                "As you make out, Rogue reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
            "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
#            if D20 >= 15:
#                $ Line = "anal"
#                jump R_Usher
            if R_CreamA:
                if R_Panties:
                    "After several minutes of this, you can't take it anymore and come inside her. She pulls her panties back up and returns to her seat."
                else:
                    "After several minutes of this, you can't take it anymore and come inside her. She wipes off as best she can and shifts back into her seat."
                $ R_CreamA += 1
                $ R_RecentActions.append("creampie anal")                      
                $ R_DailyActions.append("creampie anal") 
            else:
                "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                if R_Swallow:
                    "You cum into the popcorn bucket, which she then finishes off."
                    $ R_Addict -= 20
                    $ R_Swallow += 1
                    $ R_Spunk.append("mouth")                          
                    $ R_RecentActions.append("swallowed")                      
                    $ R_DailyActions.append("swallowed") 
                else:
                    "You cum into the popcorn bucket, which she sets in the seat next to her."
            ch_r "This makes for a better ride than a movie."            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 3)
            $ R_SeenPeen += 1
            $ R_Anal += 1
            $ P_Semen -= 1
            $ R_RecentActions.append("anal")                      
            $ R_DailyActions.append("anal")  
        elif R_Sex and ApprovalCheck("Rogue", 2000, Bonus=(10*Count2)) and R_Legs != "pants":
            call RogueFace("sexy", 1)
            if R_Panties:
                "As you make out, Rogue reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
            else:
                "As you make out, Rogue reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
            "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
#            if D20 >= 15:
#                $ Line = "sex"
#                jump R_Usher
            if R_CreamP:
                if R_Panties:
                    "After several minutes of this, you can't take it anymore and come inside her. She pulls her panties up over her dripping slit and returns to her seat."
                else:
                    "After several minutes of this, you can't take it anymore and come inside her. She wipes up as best she can and returns to her seat."
                $ R_CreamP += 1
                $ R_RecentActions.append("creampie sex")                      
                $ R_DailyActions.append("creampie sex") 
            else:
                "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                if R_Swallow:
                    "You cum into the popcorn bucket, which she then finishes off."   
                    $ R_Spunk.append("mouth")   
                    $ R_Addict -= 20
                    $ R_Swallow += 1
                    $ R_RecentActions.append("swallowed")                      
                    $ R_DailyActions.append("swallowed") 
                else:
                    "You cum into the popcorn bucket, which she sets in the seat next to her."
            ch_r "This makes for a better ride than a movie."
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 3)
            $ R_SeenPeen += 1
            $ R_Sex += 1
            $ P_Semen -= 1
            $ R_RecentActions.append("sex")                      
            $ R_DailyActions.append("sex")             
        elif R_Blow and ApprovalCheck("Rogue", 1300, Bonus=(10*Count2)):
            call RogueFace("sucking", 1)
            "As you make out, Rogue reaches down and undoes your fly. She then bends down and wraps her lips around it."
#            if D20 >= 17:
#                $ Line = "blow"
#                jump R_Usher
            "She sucks on it contentedly for several minutes before you finally cum."            
            $ R_Spunk.append("mouth")  
            if R_Swallow:
                "Rogue wipes her mouth as she shifts back into her seat and washes it down with some soda."
                call RogueFace("sexy")
                ch_r "Mmmm, refreshing. . ."
                $ R_Addict -= 20
                $ R_Swallow += 1
                $ R_RecentActions.append("swallowed")                      
                $ R_DailyActions.append("swallowed") 
            else:
                "Rogue spits the cum into the popcorn bucket and sets it aside."
                call RogueFace("sexy")
                ch_r "I bet the cleaning crew will enjoy that."
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
            $ R_Blow += 1
            $ P_Semen -= 1
            $ R_RecentActions.append("blow")                      
            $ R_DailyActions.append("blow") 
        elif R_Hand and R_FondleP and ApprovalCheck("Rogue", 1000, Bonus=(10*Count2)):
            call RogueFace("sexy")
            "As you make out, Rogue reaches down and pulls out your cock. She then leans over and begins to stroke it."  
            call RogueFace("surprised")
            if R_Panties:
                "You also lean over, reach under her panties, and begin to stroke her pussy."
            else:
                "You also lean over, notice she isn't wearing any panties, and begin to stroke her pussy."
            call RogueFace("sexy", 1)
#            if D20 >= 18:
#                $ Line = "mutual"
#                jump R_Usher
            $ R_Eyes = "closed"
            "After several minutes of this, she shudders in orgasm, which sets you off as well. She catches the jiz in the popcorn bucket."
            $ R_Eyes = "sexy"
            if R_Swallow:
                    "She finishes off the remaining popcorn with a grin."                    
                    $ R_Spunk.append("mouth")  
                    ch_r "Best topping they got here, [R_Petname]."     
                    $ R_Addict -= 20
                    $ R_Swallow += 1
                    $ R_RecentActions.append("swallowed")                      
                    $ R_DailyActions.append("swallowed") 
            else:
                "You cum into the popcorn bucket, which she sets in the seat next to her."
                ch_r "I bet the cleaning crew will enjoy that."
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
            $ R_SeenPeen += 1
            $ R_FondleP += 1
            $ R_Org += 1        
            $ R_Hand += 1
            $ P_Semen -= 1
            $ R_RecentActions.append("hand")                      
            $ R_DailyActions.append("hand") 
        elif R_Hand and ApprovalCheck("Rogue", 1000, Bonus=(10*Count2)):
            call RogueFace("sexy")
            "As you make out, Rogue reaches down and pulls out your cock. She then leans over and begins to stroke it."
#            if D20 >= 19:
#                $ Line = "hand"
#                jump R_Usher
            "After several minutes of this, you begin to feel it rising up, and she catches the jiz in the popcorn bucket."
            if R_Swallow:
                    "She finishes off the remaining popcorn with a grin."                    
                    $ R_Spunk.append("mouth")  
                    ch_r "Best topping they got here, [R_Petname]."
                    $ R_Addict -= 20
                    $ R_Swallow += 1
                    $ R_RecentActions.append("swallowed")                      
                    $ R_DailyActions.append("swallowed") 
            else:
                "You cum into the popcorn bucket, which she sets in the seat next to her."
                ch_r "I bet the cleaning crew will enjoy that."
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
            $ R_SeenPeen += 1
            $ R_Hand += 1
            $ P_Semen -= 1
            $ R_RecentActions.append("hand")                      
            $ R_DailyActions.append("hand") 
        elif R_FondleP and ApprovalCheck("Rogue", 900, Bonus=(10*Count2)):
            call RogueFace("sexy")
            if R_Legs == "pants":
                "As you make out, Rogue grabs your hand and shoves it down her pants."
            else:
                "As you make out, Rogue grabs your hand and shoves it up her skirt."
            if R_Panties:
                "You reach under her panties, and begin to stroke her pussy."
            else:
                "You notice she isn't wearing any panties, and begin to stroke her pussy."
#            if D20 >= 19:
#                $ Line = "fondle"
#                jump R_Usher
            $ R_Eyes = "closed"
            "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
            $ R_Eyes = "sexy"
            ch_r "Thanks [R_Petname]. I needed that. . . distraction."
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2)
            $ R_FondleP += 1
            $ R_Org += 1    
            $ R_RecentActions.append("fondle pussy")                      
            $ R_DailyActions.append("fondle pussy") 
        elif ApprovalCheck("Rogue", 1000, Bonus=(5*Count2)) and R_Panties:
            call RogueFace("sexy")
            "After making out for a few minutes, Rogue gets a sly look on her face, then shifts a bit lower in her seat."
            "After a few moments of wriggling, she hands you a cloth lump, apparently her panties."    
            $ R_DailyActions.append("pantyless") 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
            $ R_Panties = 0
            ch_r "Just a little downpayment on later, [R_Petname]."
        elif ApprovalCheck("Rogue", 1000, Bonus=(5*Count2)):
            call RogueFace("sexy")
            "After making out for a few minutes, Rogue gets a sly look on her face, then shifts a bit lower in her seat."
            if R_Legs == "pants":
                "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."    
            else:
                "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
            call Rogue_First_Bottomless(1)
            ch_r "Just a little downpayment on later, [R_Petname]."
    
    call RogueOutfit
    "After the movie, you head back to the dorms and escort Rogue to her room."

label R_Date_End:   
    $ Taboo = 0
    $ bg_current = "bg rogue"
    $ R_Loc = "bg rogue"
    call Set_The_Scene
    if "romcom" in R_RecentActions:
        $ Count2 += 5
    elif "horror" in R_RecentActions: 
        $ Count2 -= 5
    elif "drama" in R_RecentActions: 
        $ Count2 -= 20   
    call Wait(Outfit = 0)
    if Count2 < 0:      
        call RogueFace("angry", 0)
        $ R_Eyes = "side"
        ch_r "Well that was a waste of an evening. I'll see you around, [Playername]."
        "You return to your room."        
        $ bg_current = "bg player"         
        $ Count2 = 0
        jump Player_Room
    else: 
        $ R_DailyActions.append("dated") 
        if Count2 > 20:
            call RogueFace("sexy", 1)
            ch_r "Well that was a lot of fun, [R_Petname]. I don't want the night to end . . ."            
        else:
            call RogueFace("smile", 1)
            ch_r "Well that was a lot of fun, [R_Petname]. We'll have to do it again."
        
        $ R_Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                if ApprovalCheck("Rogue", 600, Bonus=(10*Count2)):
                    $ R_Mouth = "smile"
                    ch_r "Ok, [R_Petname]. I suppose you've earned it."
                    $ MultiAction = 0
                    call R_KissPrep 
                    $ MultiAction = 1
                if ApprovalCheck("Rogue", 900, Bonus=(10*Count2)):
                    call RogueFace("sexy", 1)
                    ch_r "That was real nice, how about you come inside for a minute. . ."   
                else:
                    call RogueFace("smile", 1)
                    ch_r "That was real nice, I'll see you later, [R_Petname]"  
                    "You return to your room."
                    $ bg_current = "bg player"  
                    $ Count2 = 0
                    jump Player_Room
            "Could I come in for a bit?":
                if ApprovalCheck("Rogue", 800, Bonus=(10*Count2)):
                    call RogueFace("sexy", 1)
                    ch_r "Alright, [R_Petname]. I think you've earned it."
            "Ok, good night then.":
                call RogueFace("confused", 1)
                "Rogue looks a little perplexed, but you head back to your room."
                $ bg_current = "bg player"  
                $ Count2 = 0
                jump Player_Room
                
                
    # Rogue lets you into her room:
    $ bg_current = "bg rogue"  
    call Set_The_Scene
    call RogueFace("sexy", 1)
    ch_r "So, [R_Petname], you've got me all alone, what are your intentions? . ."
    $ Tempmod = Count2
    call Rogue_SexMenu                       # You have what sex you can get away with
    
    if "angry" in R_RecentActions:         
        "Rogue shoves you out into the hall. You head back to your room."
        $ bg_current = "bg player"  
        $ Count2 = 0
        jump Player_Room
        
    call Rogue_Sleepover 
    jump Rogue_Room #should never be reached

label Rogue_Date_Over:
    $ R_RecentActions.append("angry")   
    call RogueFace("angry")
    ch_r "I think I'm done here, [R_Petname]." 
    "Rogue storms out, and you head back to the dorms alone."
    $ bg_current = "bg player"   
    $ Count = 0
    $ Count2 = 0
    jump Player_Room

label R_Date_Paying:    
    menu:
        "Who's paying?"
        "I've got it." if P_Cash >= (2*Count):
            call RogueFace("sexy", 1)
            ch_r "Oh, and such a gentleman."
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2) 
            if Count >= 15: 
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 2)
            $ P_Cash -= (2*Count)
            $ Count2 += Count
            if "deadbeat" in R_History:  
                $ R_History.remove("deadbeat")    
            
        "Rogue, you pay.":    
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -7)
            if Count >= 15:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -6)
            if ApprovalCheck("Rogue", 800):
                call RogueFace("sad")
                ch_r "Well, ok, I guess I can cover it this time."
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 3)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
            else:
                "I'm not gonna pick up your tab, [R_Petname]." 
                call RogueFace("angry")
                if P_Cash >= Count: 
                    "You split the check."
                    $ P_Cash -= Count
                else:
                    ch_p "I really can't cover it. Here's all I've got."
                    $ Count2 += P_Cash
                    $ P_Cash = 0
                    $ Count2 -= Count
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -3)
                    call RogueFace("sad")
                    ch_r "Ok, I'll cover the rest, this time."
                if "deadbeat" not in R_History:  
                    $ R_History.append("deadbeat") 
                else:
                    jump Rogue_Date_Over                
                    
                
        "Let's split it." if P_Cash >= Count: 
            if Count >= 15:
                $ Count2  -= 10
            if ApprovalCheck("Rogue", 600):
                call RogueFace("sad")
                $ R_Mouth = "normal"
                ch_r "Fine, I guess that's fair."
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            else:
                call RogueFace("angry")
                $ R_Eyes = "side"
                ch_r "Tch. Cheapskate."                
                if Count >= 15:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -3)
            $ P_Cash -= Count
            
        "I really can't afford it. . ." if P_Cash < Count:
            $ Count2 -= Count            
            if Count >= 15:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -4)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            call RogueFace("sad")
            if ApprovalCheck("Rogue", 800):
                ch_r "Aw, poor baby."                
            else:
                $ R_Brows = "angry"
                ch_r "Well that's pretty weak, asking a girl out when you can't even afford it." 
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 3)
                if "deadbeat" not in R_History:  
                    $ R_History.append("deadbeat") 
                else:
                    jump Rogue_Date_Over                
    $ Count = 0
    return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

