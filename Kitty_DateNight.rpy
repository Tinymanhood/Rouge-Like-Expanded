# Date Night //////////////////////////////////////////////////////////////////////
# Count = price of things
# Count2 = tempmod

label Kitty_Date_Night:
    call Shift_Focus("Kitty")
    if "askeddate" in K_RecentActions:  
        call KittyFace("angry")
        ch_k "Geez, stop bothering me already!"  
        return 
    $ K_RecentActions.append("askeddate")    
    
    if K_Break[0] and "ex" in K_Traits:
        call KittyFace("angry")
        ch_k "You can't just pretend that nothing happened!"  
        return     
    elif ApprovalCheck("Kitty", 1200) and "ex" in K_Traits:
        call KittyFace("bemused")
        $ K_Brows = "sad"        
        if "no summon" in K_RecentActions:  
            ch_k "Well, I was doing something, but I guess if we're going out. . ."              
        else:
            ch_k "I don't know, we used to have fun. I guess so."          
        if "deadbeat" in K_History:  
            call KittyFace("angry")
            $ K_Mouth = "grimace"
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
            ch_k "But you're definitely paying this time!"
            call KittyFace("bemused")            
    elif "ex" in K_Traits:
        call KittyFace("angry")
        $ K_Eyes = "side"                
        ch_k "I[K_like]don't think so." 
        return 
    elif "deadbeat" in K_History:  
        call KittyFace("angry")             
        menu:
            ch_k "Last time we went out, you[K_like]left me with the check!" 
            "Sorry about that, I'll take care of the check this time.":
                if ApprovalCheck("Kitty", 650):
                    call KittyFace("sad")
                    ch_k "Well, I guess I can give you another chance, just don't disappoint me again."
                else:
                    call KittyFace("angry")
                    "Yeah[K_like]fool me once. . . no thanks, [K_Petname]." 
                    return
            "Yeah, so?":
                if ApprovalCheck("Kitty", 1400):
                    call KittyFace("angry")                    
                    $ K_Mouth = "grimace"
                    ch_k "Why do I[K_like]put up with you?"
                    call KittyFace("bemused")        
                elif ApprovalCheck("Rogue", 500, "O"):
                    call KittyFace("sad")
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 3)
                    ch_k "Well, I guess we can still have fun. . ."
                elif ApprovalCheck("Kitty", 650):
                    call KittyFace("angry")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2) 
                    ch_k "Yeah[K_like]I'm going out with {i}you,{/i} dick."  
                    return 
                else:
                    call KittyFace("angry")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, -3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2) 
                    ch_k "Asshole."  
                    return             
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 3)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
    elif ApprovalCheck("Kitty", 650):
        call KittyFace("smile")
        if "no summon" in K_RecentActions:  
            ch_k "Well, I was doing something, but I guess if we're going out. . ." 
        else:
            ch_k "Sure, where to?"
    elif ApprovalCheck("Kitty", 500):
        call KittyFace("perplexed")
        if "no summon" in K_RecentActions:  
            ch_k "Sorry, I told you I was busy." 
        else:
            ch_k "Um[K_like]I guess we could. . ."
    elif ApprovalCheck("Kitty", 400):                
        call KittyFace("angry")
        $ K_Eyes = "side"
        ch_k "I've[K_like]got better things to do. . ."
        return
    else:
        call KittyFace("angry")
        ch_r "[K_Like]no way."
        return              
    $ renpy.pop_call()
    
    $ Taboo = 40
    if K_Schedule[7]:
        #if she has a date outfit set
        if K_Schedule[7] == 2:
            $ K_Outfit = "red outfit"
        elif K_Schedule[7] == 3:
            $ K_Outfit = "custom1"
        elif K_Schedule[7] == 4:
            $ K_Outfit = "gym"
        elif K_Schedule[7] == 5:
            $ K_Outfit = "custom2"
        elif K_Schedule[7] == 6:
            $ K_Outfit = "custom3"
        else:
            $ K_Outfit = "pink outfit"
    else:
        $ Options = ["pink outfit", "red outfit"]
        $ Options.append("custom1") if K_Custom[0] == 2 else Options
        $ Options.append("custom2") if K_Custom2[0] == 2 else Options
        $ Options.append("custom3") if K_Custom3[0] == 2 else Options
        $ renpy.random.shuffle(Options) 
        $ K_Outfit = Options[0]
        $ del Options[:]  
    call CleartheRoom("Kitty",0,1)   
    $ K_Loc = "date"
    $ bg_current = "date"  
    call KittyOutfit(Changed=1)
    call Set_The_Scene    
    menu:
        ch_k "So[K_like]where would you like to go?"
        "To the movies.":
            $ K_RecentActions.append("movie")                      
            $ K_DailyActions.append("movie") 
        "To a restaurant.":
            $ K_RecentActions.append("dinner")                      
            $ K_DailyActions.append("dinner") 
        "Dinner and a movie.":
            $ K_RecentActions.append("movie")                      
            $ K_DailyActions.append("movie") 
            $ K_RecentActions.append("dinner")                      
            $ K_DailyActions.append("dinner") 
        "Never Mind.":
            call KittyFace("sad")
            ch_k "Oh, ok. Maybe later?"
            call KittyFace
            jump Kitty_Chat            
    ch_k "K, let's get going then."
    show blackscreen onlayer black with dissolve
    $ Count = 0    
    $ Party = []
    

if "dinner" not in K_RecentActions:
    "You head to the local theater and check out the film listings."
    jump K_Date_Movies
    
label K_Date_Dinner:
    "You go to one of the nicer restaurants in town. The food is quality but reasonably affordable." 
    $ bg_current = "bg restaurant"
    $ K_Loc = "bg restaurant"
    call Set_The_Scene
    
    menu:
        "You order. . ."
        "Surf and turf for you and Kitty. ($20 each)":
            call KittyFace("sad")
            $ K_Brows = "surprised"
            ch_k "Um, I[K_like]don't really eat shellfish. . ."  
            call KittyFace
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)
            $ Count = 20
            $ Count2 -= 11
            $ Line = "steak and a juicy lobster"
        "Steak for the both of you. ($15 each)":  
            call KittyFace("smile")
            ch_k "Sounds delish."
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 5)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 2)
            $ Count = 15
            $ Line = "medium rare ribeye"
        "Chicken for both of you. ($10 each)":
            call KittyFace("smile")
            ch_k "Chicken's fine."
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 3)
            $ Count = 10
            $ Line = "pangrilled chicken thighs"
        "Just a salad for each of you. ($5 each)":
            $ K_Mouth = "sad"
            $ K_Eyes = "sexy"
            $ K_Brows = "confused"            
            ch_k "I do enjoy a nice salad."  
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -3)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ Count = 5
            $ Line = "fresh garden salad"
        "Why don't you choose, Kitty?":
            call KittyFace("smile")
            ch_k "Well thanks, [K_Petname]. I think we'll have the steak."            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 7)   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 2) 
            $ Count = 15
            $ Line = "medium rare ribeye"
            
    "You eat your meals" # add options here
    if Line == "steak and a juicy lobster":
        $ Line = "You eat your "+ Line + ", Kitty eats the steak but pushes the lobster to the side."
    else:
        $ Line = "You eat your "+ Line + ", and have a pleasant conversation over the meal."
    "[Line]"    
    call KittyFace("sexy", 1)
    
    $ del Options[:]  
    $ Options = ["nothing"]
        
    if K_Anal and ApprovalCheck("Kitty", 1500) and Count >=15: 
        $ Options.append("anal")        
    if K_Sex and ApprovalCheck("Kitty", 1500) and Count >=10:
        $ Options.append("sex")
    if K_Blow and ApprovalCheck("Kitty", 1300) and Count >=10:
        $ Options.append("blow")      
    if K_Hand and ApprovalCheck("Kitty", 1000) and Count >=10:
        $ Options.append("hand")
    if K_FondleP and ApprovalCheck("Kitty", 1000) and Count >=10:
        $ Options.append("pussy")
    if ApprovalCheck("Kitty", 1000) and Count >=10:
        $ Options.append("foot")
        
    $ renpy.random.shuffle(Options) 
    
    if Options[0] == "nothing":
        pass
    elif Options[0] == "anal":        
        "Halfway through the meal, Kitty gets a sly look on her face, nods her head suggestively towards the restrooms, and then excuses herself."
        "A few seconds later, you follow her and she drags you inside, locking the door behind you. She spends the next several minutes taking it up the ass."
        ch_k "That was {i}so{/i} worth it."  
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 9)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3)
        $ K_SeenPeen += 1
        $ K_Anal += 1
        $ P_Semen -= 1
        $ K_RecentActions.append("anal")                      
        $ K_DailyActions.append("anal") 
    elif Options[0] == "sex":
        "Halfway through the meal, Kitty gets a sly look on her face, nods her head suggestively towards the restrooms, and then excuses herself."
        "A few seconds later, you follow her and she drags you inside, locking the door behind you. She spends the next several minutes fucking you raw."
        ch_k "That was a workout."
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 8)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
        $ K_SeenPeen += 1
        $ K_Sex += 1
        $ P_Semen -= 1            
        $ K_RecentActions.append("sex")                      
        $ K_DailyActions.append("sex") 
    elif Options[0] == "blow":
        "Halfway through the meal, Kitty gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants. She then procedes to blow you for several minutes until you cum."
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 6)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
        $ K_RecentActions.append("blow")                      
        $ K_DailyActions.append("blow") 
        if K_Swallow:
            "Kitty wipes her mouth as she climbs out from under the table."
            ch_k "That hit the spot. . ."            
            $ K_Addict -= 20
            $ K_Swallow += 1  
            $ K_RecentActions.append("swallow")                      
            $ K_DailyActions.append("swallow")       
        else:
            "Kitty grabs the napkin off your lap and uses it to collect the jiz."
            ch_k "I feel kinda sorry for the busboys."
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 4)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
        $ K_SeenPeen += 1
        $ K_Blow += 1
        $ P_Semen -= 1
    elif Options[0] == "hand":
        "Halfway through the meal, Kitty gets a sly look on her face, then shifts her chair around next to yours."
        "She unzips your pants under the table, and proceeds to caress your cock, stroking it until you cum into the napkin."
        ch_k "I feel kinda sorry for the busboys."
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 4)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
        $ K_Hand += 1
        $ P_Semen -= 1
        $ K_RecentActions.append("hand")                      
        $ K_DailyActions.append("hand") 
    elif Options[0] == "pussy":
        "Halfway through the meal, Kitty gets a sly look on her face, then shifts her chair around next to yours."
        if PantsNum("Kitty") > 5:
            "She takes your hand and pulls it over to her crotch, shoving it down her pants. You can feel that she's warm as a furnace."
        else:
            "She takes your hand and pulls it down to her crotch, shoving it under her skirt. You can feel that she's warm as a furnace."
        "You stroke her pussy for several minutes, until finally she shudders in orgasm and slowly pulls your hand free with a sly smile."
        ch_k "Thanks, [K_Petname], I needed that."
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 5)            
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 2)
        $ K_FondleP += 1
        $ K_Org += 1
        $ K_RecentActions.append("fondle pussy")                      
        $ K_DailyActions.append("fondle pussy") 
    elif Options[0] == "foot":
        "Halfway through the meal, Kitty gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock. After several minutes of this, she pulls back."
        ch_k "Just a taste of things to come, [K_Petname]."
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3)
     
    $ del Options[:]       
    call KittyFace(B = 0)
    
    $ Count = 20 if Count == 4 else Count #resets price of the meal if you picked surf and turf
    
    call K_Date_Paying 
    if Count2 >= 30:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 15)   
    elif Count2 >= 20:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 10)     
    elif Count2 >= 10:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 5) 
    
    if "movie" not in K_RecentActions:
        "After dinner, you head back to the dorms and escort Kitty to her room."       
        jump K_Date_End
        
    #else:    
    "After dinner, you head to the local theater and check out the film listings."   
        
label K_Date_Movies:    
    $ bg_current = "bg movies"
    $ K_Loc = "bg movies"
    call Set_The_Scene 
    $ Count = 10
    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
    menu:
        "What would you like to see?"
        "A romantic comedy.":
            call KittyFace("smile")
            $ K_Eyes = "surprised"
            ch_k "Aw, how cuuuute!"   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 3)
            $ Count2 += 5
            $ K_RecentActions.append("romcom") 
        "An action movie.":
            call KittyFace("sexy")
            ch_k "Action movies are kind of fun." 
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 4)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
            $ Count2 += 5
            $ K_RecentActions.append("action") 
        "A horror movie.":
            call KittyFace("sad")
            $ K_Eyes = "surprised"
            ch_k "It won't be {i}too{/i} scary, right?."                
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
            $ Count2 += 15
            $ K_RecentActions.append("horror") 
        "An acclaimed drama.":
            call KittyFace("bemused")
            ch_k "I heard this was a good one!"   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 3)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            $ Count2 += 20
            $ K_RecentActions.append("drama") 
        "Let Kitty pick.":
            call KittyFace("smile")
            ch_k "How sweet, [K_Petname]. Let's see the drama."            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 4)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
            $ Count2 += 20
            $ K_RecentActions.append("drama") 
            
    call K_Date_Paying      
    if Count2 >= 50:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 25) 
    elif Count2 >= 40:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 20)  
    elif Count2 >= 30:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 15)   
    elif Count2 >= 20:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 10)     
    elif Count2 >= 10:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 5)   
                
    if "romcom" in K_RecentActions:      
        $ Count += 2
        $ Line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one.", 
                    "You watch the movie, which is about a girl is mercilessly stalked by some weird guy until she eventually decides she loves him. They live hapily ever after.", 
                    "In this movie, the lead goes to all her friend's weddings, but can't get it together herself. She dies alone. Just kidding, she gets married at the end.", 
                    "You watch the movie, in which a bunch of college girls go on a wild adventure and have lots of random sex.",
                    "This movie is about a girl who's convinced to live in a sex dungeon, and really seems to enjoy it.",
                    "This movie is about a girl who works for a fashion house and is bullied by her boss, until they become friends."])        
    elif "action" in K_RecentActions: 
        $ Count += 1
        $ Line = renpy.random.choice(["You watch the movie, which is about an ex marine fighting aliens.", 
                    "You watch the movie, which is about a girl is mercilessly stalked by some weird guy until she eventually decides she loves him. They live hapily ever after. There are also a lot of explosions.", 
                    "In this movie, giant robots are fighting animal mash-ups, with the fate of the world in the balance.", 
                    "You watch the movie, in which a team of non-mutant superhumans are apparently fighting some sort of silvery robots in Eastern Europe.",
                    "This movie is about a superhuman powerhouse that nearly wrecks a town, and yet is not arrested for it by the humans. Must be the hammer.",
                    "This movie is about 90 minutes of constant explosions and lensflares."])
    elif "horror" in K_RecentActions: 
        $ Count += 4
        $ Line = renpy.random.choice(["You watch the movie, which is about an adorkable girl who can't choose between two hunky guys. She picks the other one. The guys are a fishman and a skeleton.", 
                    "You watch the movie, which is about a girl is mercilessly stalked by some weird guy until she eventually gives in and marries him. Her life is an endless hell.", 
                    "In this movie, a group of teens are trapped in a wilderness cabin. They have a lot of random sex as some shadowy monster kills them one by one.", 
                    "In this movie, a group of teens are trapped in an abandoned motel. They have a lot of random sex as some shadowy monster kills them one by one.", 
                    "This movie is about a girl who's convinced to live in a sex dungeon, and she's eventually murdered.",
                    "In this movie, a group of teens are trapped in a spaceship. They have a lot of random sex as some shadowy monster kills them one by one."])
    elif "drama" in K_RecentActions: 
        $ Count += 5
        $ Line = renpy.random.choice(["You watch the movie, which is about a mature woman who can't choose between two eligible widowers. She picks the other one.", 
                    "You watch the movie, which is a documentary about a girl is mercilessly stalked by some weird guy until she eventually decides she gets a restraining order.", 
                    "In this movie, which is a biopic about a great historical leader.", 
                    "You watch the movie, in which a disabled person struggles with his various disabilities, and eventually overcomes them, and/or dies.",
                    "This movie is about a lot of yelling and crying as some very serious issues are explored by an ensemble cast."])
    "[Line]"
    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if (D20 + Count) >= 10 and ApprovalCheck("Kitty", 500, Bonus=(10*Count2)):
        call KittyFace("kiss", 1)
        if "romcom" in K_RecentActions: 
            "Halfway through the movie, inspired by the action on screen, Kitty turns to you and starts to make out with you."
        elif "action" in K_RecentActions:        
            "Halfway through the movie, adrenaline pumping from the action on screen, Kitty turns to you and starts to make out with you."
        elif "horror" in K_RecentActions:  
            "Halfway through the movie, freaked out by the tension on screen, Kitty huddles in your arms, and then starts to make out with you."
        elif "drama" in K_RecentActions:   
            "Halfway through the movie, Kitty turns to you with a shrug and starts to make out with you."
        $ K_RecentActions.append("kissing")                      
        $ K_DailyActions.append("kissing") 
    
        if K_Anal and ApprovalCheck("Kitty", 2000, Bonus=(10*Count2)) and K_Legs != "pants":
                    call KittyFace("sexy", 1)
                    if K_Panties:
                        "As you make out, Kitty reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Kitty reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if K_CreamA:
                        if K_Panties:
                            "After several minutes of this, you can't take it anymore and come inside her. She pulls her panties back up and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her. She wipes off as best she can and shifts back into her seat."
                        $ K_CreamA += 1
                        $ K_RecentActions.append("creampie anal")                      
                        $ K_DailyActions.append("creampie anal") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if K_Swallow:
                            "You cum into the popcorn bucket, which she then finishes off."
                            $ K_Addict -= 20
                            $ K_Swallow += 1
                            $ K_Spunk.append("mouth")                          
                            $ K_RecentActions.append("swallowed")                      
                            $ K_DailyActions.append("swallowed") 
                        else:
                            "You cum into the popcorn bucket, which she phases into the floor."
                    ch_k "Talk about a \"4D\" movie."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 3)
                    $ K_SeenPeen += 1
                    $ K_Anal += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("anal")                      
                    $ K_DailyActions.append("anal")  
        elif K_Sex and ApprovalCheck("Kitty", 2000, Bonus=(10*Count2)) and K_Legs != "pants":
                    call KittyFace("sexy", 1)
                    if K_Panties:
                        "As you make out, Kitty reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Kitty reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if K_CreamP:
                        if K_Panties:
                            "After several minutes of this, you can't take it anymore and come inside her. She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her. She wipes up as best she can and returns to her seat."
                        $ K_CreamP += 1
                        $ K_RecentActions.append("creampie sex")                      
                        $ K_DailyActions.append("creampie sex") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if K_Swallow:
                            "You cum into the popcorn bucket, which she then finishes off."   
                            $ K_Spunk.append("mouth")   
                            $ K_Addict -= 20
                            $ K_Swallow += 1
                            $ K_RecentActions.append("swallowed")                      
                            $ K_DailyActions.append("swallowed") 
                        else:
                            "You cum into the popcorn bucket, which she phases into the floor."
                    ch_k "Talk about a \"4D\" movie."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 3)
                    $ K_SeenPeen += 1
                    $ K_Sex += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("sex")                      
                    $ K_DailyActions.append("sex")             
        elif K_Blow and ApprovalCheck("Kitty", 1300, Bonus=(10*Count2)):
                    call KittyFace("sucking", 1)
                    "As you make out, Kitty reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    "She sucks on it contentedly for several minutes before you finally cum."            
                    $ K_Spunk.append("mouth")  
                    if K_Swallow:
                        "Kitty wipes her mouth as she shifts back into her seat and washes it down with some soda."
                        call KittyFace("sexy")
                        ch_k "Mmmm, that hit the spot. . ."
                        $ K_Addict -= 20
                        $ K_Swallow += 1
                        $ K_RecentActions.append("swallowed")                      
                        $ K_DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she phases into the floor."
                        ch_k "That should give archeolgists a surprise."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
                    $ K_SeenPeen += 1
                    $ K_Blow += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("blow")                      
                    $ K_DailyActions.append("blow") 
        elif K_Hand and K_FondleP and ApprovalCheck("Kitty", 1000, Bonus=(10*Count2)):
                    call KittyFace("sexy")
                    "As you make out, Kitty reaches down and pulls out your cock. She then leans over and begins to stroke it."  
                    call KittyFace("surprised")
                    if K_Legs:
                            "You also lean over, reach into her [K_Legs], and begin to stroke her pussy."
                    elif K_Hose:
                            "You also lean in, reach under her [K_Hose], and begin to stroke her pussy."
                    elif K_Panties:
                            "You also lean in, reach under her panties, and begin to stroke her pussy."
                    else:
                            "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    call KittyFace("sexy", 1)
                    $ K_Eyes = "closed"
                    "After several minutes of this, she shudders in orgasm, which sets you off as well. She catches the jiz in the popcorn bucket."
                    $ K_Eyes = "sexy"
                    if K_Swallow:
                            "She finishes off the remaining popcorn with a grin."                    
                            $ K_Spunk.append("mouth")  
                            ch_k "Best topping they got here, [K_Petname]."     
                            $ K_Addict -= 20
                            $ K_Swallow += 1
                            $ K_RecentActions.append("swallowed")                      
                            $ K_DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she phases into the floor."
                        ch_k "That should give archeolgists a surprise."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
                    $ K_FondleP += 1
                    $ K_Org += 1        
                    $ K_Hand += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("hand")                      
                    $ K_DailyActions.append("hand") 
        elif K_Hand and ApprovalCheck("Kitty", 1000, Bonus=(10*Count2)):
                    call KittyFace("sexy")
                    "As you make out, Kitty reaches down and pulls out your cock. She then leans over and begins to stroke it."
                    "After several minutes of this, you begin to feel it rising up, and she catches the jiz in the popcorn bucket."
                    if K_Swallow:
                            "She finishes off the remaining popcorn with a grin."                    
                            $ K_Spunk.append("mouth")  
                            ch_k "Best topping they got here, [K_Petname]."
                            $ K_Addict -= 20
                            $ K_Swallow += 1
                            $ K_RecentActions.append("swallowed")                      
                            $ K_DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she phases into the floor."
                        ch_k "That should give archeolgists a surprise."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
                    $ K_SeenPeen += 1
                    $ K_Hand += 1
                    $ P_Semen -= 1
                    $ K_RecentActions.append("hand")                      
                    $ K_DailyActions.append("hand") 
        elif K_FondleP and ApprovalCheck("Kitty", 900, Bonus=(10*Count2)):
                    call KittyFace("sexy")                    
                    if K_Legs:
                            "You also lean over, reach into her [K_Legs], and begin to stroke her pussy."
                    elif K_Hose:
                            "As you make out, Kitty grabs your hand and shoves it down her [K_Hose]."
                    elif K_Panties:
                            "As you make out, Kitty grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, Kitty grabs your hand and shoves it between her legs."
                    $ K_Eyes = "closed"
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ K_Eyes = "sexy"
                    ch_k "Hmm, that felt great, [K_Petname]."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2)
                    $ K_FondleP += 1
                    $ K_Org += 1    
                    $ K_RecentActions.append("fondle pussy")                      
                    $ K_DailyActions.append("fondle pussy") 
        elif ApprovalCheck("Kitty", 1200, Bonus=(5*Count2)) and K_Panties:
                    call KittyFace("sexy")
                    "After making out for a few minutes, Kitty gets a sly look on her face and reaches into her pocket."
                    "After a a second, she hands you a cloth lump, apparently her panties." 
                    $ K_DailyActions.append("pantyless") 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
                    $ K_Panties = 0
                    ch_k "[K_Like]hold on to those for me, uh?"
        elif ApprovalCheck("Kitty", 1200, Bonus=(5*Count2)):
                    call KittyFace("sexy")
                    "After making out for a few minutes, Kitty gets a sly look on her face, then shifts a bit lower in her seat."
                    if K_Legs == "pants":
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."  
                    elif K_Legs == "shorts":
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."   
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
                    call Kitty_First_Bottomless(1)
                    ch_k "Just giving you a little taste. . ."
        #End sex options
    
    call KittyOutfit
    "After the movie, you head back to the dorms and escort Kitty to her room."

label K_Date_End:   
    $ Taboo = 0
    $ bg_current = "bg kitty"
    $ K_Loc = "bg kitty"
    call Set_The_Scene
    
    if "romcom" in K_RecentActions:
        $ Count2 += 5
    elif "horror" in K_RecentActions: 
        $ Count2 -= 10
    elif "drama" in K_RecentActions: 
        $ Count2 -= 15         
    call Wait(Outfit = 0)
    if Count2 < 0:      
        call KittyFace("angry", 0)
        $ K_Eyes = "side"
        ch_k "You[K_like]really need to get your shit together, [Playername]."
        "You return to your room."        
        $ bg_current = "bg player"         
        $ Count2 = 0
        jump Player_Room
    else: 
        $ K_DailyActions.append("dated") 
        if Count2 > 20:
            call KittyFace("sexy", 1)
            ch_k "That was fun, [K_Petname]. Do you have to go . . ."            
        else:
            call KittyFace("smile", 1)
            ch_k "Well that was fun, [K_Petname]. Text me later."
        
        $ K_Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                if ApprovalCheck("Kitty", 600, Bonus=(10*Count2)):
                    $ K_Mouth = "smile"
                    ch_k "Heh, I guess so. . ."
                    $ MultiAction = 0
                    call K_KissPrep 
                    $ MultiAction = 1
                if ApprovalCheck("Kitty", 900, Bonus=(10*Count2)):
                    call KittyFace("sexy", 1)
                    ch_k "Hmmm . . ."   
                    ch_k "Maybe. . . come inside for a minute?"
                else:
                    call KittyFace("smile", 1)
                    ch_k "That was nice, text you later!"  
                    "You return to your room."
                    $ bg_current = "bg player"  
                    $ Count2 = 0
                    jump Player_Room
            "Could I come in for a bit?":
                if ApprovalCheck("Kitty", 800, Bonus=(10*Count2)):
                    call KittyFace("sexy", 1)
                    ch_k "Heh, I guess so. . ."
            "Ok, good night then.":
                call KittyFace("confused", 1)
                "Kitty looks a little confused, but you head back to your room."
                $ bg_current = "bg player"  
                $ Count2 = 0
                jump Player_Room
                
                
    # Kitty lets you into her room:
    $ bg_current = "bg kitty"  
    call Set_The_Scene
    call KittyFace("sexy", 1)
    ch_k "So[K_like]here we are. . . "
    $ Tempmod = Count2
    call Kitty_SexMenu                       # You have what sex you can get away with
    
    if "angry" in K_RecentActions:         
        "Kitty shoves you out into the hall. You head back to your room."
        $ bg_current = "bg player"  
        $ Count2 = 0
        jump Player_Room
    
    if True:    #fix remove after sloopover added     
        "Afterwards, you head back to your room for the night."
        $ bg_current = "bg player"  
        $ Count2 = 0
        jump Player_Room
        
    call Kitty_Sleepover 
    jump Kitty_Room #should never be reached

label Kitty_Date_Over:
    $ K_RecentActions.append("angry")   
    call KittyFace("angry")
    ch_k "You know what?" 
    ch_k "[Playername]'s a Jerk!" 
    "Kitty storms out, and you head back to the dorms alone."
    $ bg_current = "bg player"   
    $ Count = 0
    $ Count2 = 0
    jump Player_Room

label K_Date_Paying:    
    menu:
        "Who's paying?"
        "I've got it." if P_Cash >= (2*Count):
            call KittyFace("sexy", 1)
            ch_k "[K_Like]that's really nice of you."
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2) 
            if Count >= 15: 
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 2)
            $ P_Cash -= (2*Count)
            $ Count2 += Count            
            if "deadbeat" in K_History:  
                $ K_History.remove("deadbeat") 
            
        "Kitty, you pay.":    
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -7)
            if Count >= 15:
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -6)
            if ApprovalCheck("Kitty", 800):
                call KittyFace("sad")
                ch_k "Huh? I mean I guess I can. . ."
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 3)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
            else:
                "As if! You're paying for yourself, [K_Petname]." 
                call KittyFace("angry")
                if P_Cash >= Count: 
                    "You split the check."
                    $ P_Cash -= Count
                else:
                    ch_p "I really can't cover it. Here's all I've got."
                    $ Count2 += P_Cash
                    $ P_Cash = 0
                    $ Count2 -= Count
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -3)
                    call KittyFace("sad")
                    ch_k "Geez, I guess I can cover it."
                if "deadbeat" not in K_History:  
                    $ K_History.append("deadbeat") 
                else:
                    jump Kitty_Date_Over
                    
                
        "Let's split it." if P_Cash >= Count: 
            if Count >= 15:
                $ Count2  -= 10
            if ApprovalCheck("Kitty", 600):
                call KittyFace("sad")
                $ K_Mouth = "normal"
                ch_k "Yeah[K_like]ok."
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
            else:
                call KittyFace("angry")
                $ K_Eyes = "side"
                ch_k "Jerk."                
                if Count >= 15:
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -3)
            $ P_Cash -= Count
            
        "I really can't afford it. . ." if P_Cash < Count:
            $ Count2 -= Count            
            if Count >= 15:
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -4)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
            call KittyFace("sad")
            if ApprovalCheck("Kitty", 800):
                ch_k "That's so[K_like]sad."                
            else:
                $ K_Brows = "angry"
                ch_k "I wouldn't have gone out with you if I'd known you were such a bum." 
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 3)
                if "deadbeat" not in K_History:  
                    $ K_History.append("deadbeat") 
                else:
                    jump Kitty_Date_Over
    $ Count = 0
    return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
