label Rogue_Strip_Study:
    $ Count = 0
    $ Count2 = 1
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .    
    
    ch_r "Alright, [R_Petname], I'll make this simple. I'll ask you a quiz question, get it right, I take something off. . ."
    ch_r "Get three wrong, and we're done for the night. Good luck."
    while Count2:        
        "Question [Count2],"
        call Quiz_Question_Rogue from _call_Quiz_Question_Rogue
        $ Count2 += 1
        if _return:
            call Rogue_Strip_Study_Right from _call_Rogue_Strip_Study_Right
        else:
            $ Count += 1
            call Rogue_Strip_Study_Wrong from _call_Rogue_Strip_Study_Wrong        
    return
            
label Rogue_Strip_Study_Right:
    if R_Hose:  # Will she lose the hose?
        "She slowly removes her hose. . ."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 3)
        $ R_Hose = 0
        return    
        
    if R_Over: #will she lose the top?
        if R_SeenChest or (R_Chest and ApprovalCheck("Rogue", 300)) or ApprovalCheck("Rogue", 850):
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 25, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            "She pulls her [R_Over] off and throws it aside."            
            $ R_Over = 0
            
        else:
            ch_r "You know, I don't really think I'm ready for this, sorry [R_Petname]. I shouldn't have led you on."
            $ Count2 = 0
        return   
        
    if R_Legs:   #will she lose the pants/skirt?
        if (R_SeenPanties and R_SeenPussy) or (R_Panties and (ApprovalCheck("Rogue", 700) or R_SeenPanties)) or ApprovalCheck("Rogue", 950):  
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            if R_Legs == "skirt":
                "She unzips her skirt and slides it off."
            else:
                "She unzips her jeans and slides them down her legs."            
            $ R_Legs = 0 
            if R_Panties:
                if not R_SeenPanties:   
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)  
                    $ R_SeenPanties = 1
            else:
                #R seen pussy
                $ R_Blush = 1
                "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                
        else:
            ch_r "You know, I don't really think I'm ready for this, sorry [R_Petname]. I shouldn't have led you on."
            $ Count2 = 0
        return     
    
    if R_Chest: # Will she go topless?
        if ApprovalCheck("Rogue", 900) or (R_SeenChest and ApprovalCheck("Rogue", 600)):
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 1)
            "She pulls her [R_Chest] over her head and tosses it aside."                    
            $ R_Chest = 0  
            if not R_SeenChest:   
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)  
                call Rogue_First_Topless(1) from _call_Rogue_First_Topless_17
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)
        else:
             ch_r "I know a deal's a deal, but I'd like to keep my top on, ok [R_Petname]? Sorry about that."
             $ Count2 = 0
        return  
            
    if R_Panties: # Will she go bottomless?
        if ApprovalCheck("Rogue", 950) or (R_SeenPussy and ApprovalCheck("Rogue", 600)):    
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)    
            "She slides her [R_Panties] off, leaving her pussy bare."             
            $ R_Panties = 0   
            if not R_SeenPussy:
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 4)
                call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_21
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 75, 20)
        else:
             ch_r "Look, this has gone a bit far, [R_Petname]. I'd like to call it a night."
             $ Count2 = 0
        return  
            
    ch_r "Well, that's another right answer, but I don't have a stitch left to take off. . ."     
    $ Count2 = 0
    $ Tempmod = 50
    call Rogue_SexMenu from _call_Rogue_SexMenu_17    
    ch_r "Well I sure enjoyed that."
    return
    
label Rogue_Strip_Study_Wrong:
    if Count == 1:
        ch_r "Bzzt, too bad, [R_Petname]."
    elif Count == 2:
        ch_r "Oh, you're really not good at this. Come on, you've only got one more shot."
    elif Count > 2:
        ch_r "And you are out of here! Sorry, [R_Petname], thanks for playing, you're done."
        $ Count2 = 0
        
    return
    
label Quiz_Question_Rogue:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_r "Who was the first person who I used my powers on?"
            "A. Colby":
                return 0
            "B. Renly":
                return 0
            "C. Remy":
                return 0
            "D. Cody":
                return 1
    if QuizOrder[Count2] == 2:
        menu:
            ch_r "Where did I live before moving to Xaviers?"
            "A. Lousiana":
                return 0
            "B. Mississippi":
                return 1
            "C. Connecticut":
                return 0
            "D. Tennessee":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_r "What was the first power I. . . borrowed?"
            "A. Mystique's shape shifting":
                return 0
            "B. Shadowcat's phasing":
                return 0
            "C. Nightcrawler's teleport":
                return 1
            "D. Cyclops's eyebeams":
                return 0
    if QuizOrder[Count2] == 4:
        menu:
            ch_r "What mutant raised me as my parent before my powers manifested."
            "A. Magneto":
                return 0
            "B. Mystique":
                return 1
            "C. Xavier":
                return 0
            "D. Belasco":
                return 0
    if QuizOrder[Count2] == 5:
        menu:
            ch_r "I eventually joined the X-Men after Mystique attacked me, where?"
            "A. At school":
                return 0
            "B. At the beach":
                return 0
            "C. In the mountains":
                return 1
            "D. In the bayou":
                return 0
    if QuizOrder[Count2] == 6:
        menu:
            ch_r "When Magneto was selecting the fittest mutants for Asteroid M, I was captured after beating which member of the Brotherhood?"
            "A. Blob":
                return 0
            "B. Avalanche":
                return 0
            "C. Toad":
                "That's right, [R_Petname], I slammed that frog tongue in a car door"
                "Better not make me angry."
                return 1
            "D. Quicksilver":
                return 0
                
    #remove this once I have enough questions
    "You answer the question correctly."
    return 1


#////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////

label Kitty_Strip_Study:
    $ Count = 0
    $ Count2 = 1
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .   
    call KittyFace("perplexed", 2) from _call_KittyFace_628
    ch_k "Ok, so[K_like]if you get a question right. . . I'll take off a piece of clothing. . ."
    ch_k "But you only get three tries." 
    call KittyFace("sly", 1) from _call_KittyFace_629
    while Count2:        
        "Question [Count2],"
        call Quiz_Question_Kitty from _call_Quiz_Question_Kitty
        $ Count2 += 1
        if _return:
            call Kitty_Strip_Study_Right from _call_Kitty_Strip_Study_Right
        else:
            $ Count += 1
            call Kitty_Strip_Study_Wrong from _call_Kitty_Strip_Study_Wrong        
    return
            
label Kitty_Strip_Study_Right:
    if K_Hose:  # Will she lose the hose?
        "She slowly removes her hose. . ."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 3)
        $ K_Hose = 0
        return    
        
    if K_Over: #will she lose the top?
        if K_SeenChest or (K_Chest and ApprovalCheck("Kitty", 300)) or ApprovalCheck("Kitty", 850):
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 25, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
            "She lets her [K_Over] drop to the floor."            
            $ K_Over = 0
            
        else:  
            call KittyFace("perplexed", 2) from _call_KittyFace_630
            ch_k "Sorry, don't mean to be a tease, but I just can't handle this yet."  
            call KittyFace("bemused", 1) from _call_KittyFace_631
            $ Count2 = 0
        return   
        
    if K_Legs:   #will she lose the pants/skirt?
        if (K_SeenPanties and K_SeenPussy) or (K_Panties and (ApprovalCheck("Kitty", 700) or K_SeenPanties)) or ApprovalCheck("Kitty", 950):  
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
            "She lets her [K_Legs] pool at her feet."      
            $ K_Legs = 0 
            if K_Panties:
                if not K_SeenPanties:   
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)  
                    $ K_SeenPanties = 1
            else:
                #R seen pussy
                $ K_Blush = 2
                "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                $ K_Blush = 1
                
        else:
            ch_k "Sorry, don't mean to be a tease, but I just can't handle this yet." 
            $ Count2 = 0
        return     
    
    if K_Chest: # Will she go topless?
        if ApprovalCheck("Kitty", 900) or (K_SeenChest and ApprovalCheck("Kitty", 600)):
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 1)
            "She lets her [K_Chest] drop into a pile at her feet."                    
            $ K_Chest = 0  
            if not K_SeenChest:   
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)  
                call Kitty_First_Topless(1) from _call_Kitty_First_Topless_5
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)
        else:
             ch_k "So. . . I know this is a bit late to mention it, but I'd like to keep my top on?"
             $ Count2 = 0
        return  
            
    if K_Panties: # Will she go bottomless?
        if ApprovalCheck("Kitty", 950) or (K_SeenPussy and ApprovalCheck("Kitty", 600)):    
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 2)    
            "She shrugs and her [K_Panties] drop to the floor, leaving her pussy bare."             
            $ K_Panties = 0   
            if not K_SeenPussy:
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 4)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 4)
                call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_12
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 75, 20)
        else:
            call KittyFace("perplexed", 2) from _call_KittyFace_632
            ch_k "Wow, I. . . I'm not really ready for this sort of thing, I'm sorry!"
            call KittyFace("perplexed", 1) from _call_KittyFace_633
            $ Count2 = 0
        return  
            
    call KittyFace("sly", 1) from _call_KittyFace_634
    ch_k "So. . . you got that one right. . ."
    $ K_Eyes = "down"
    ch_k ". . . but I'm not[K_like]wearing anything else. . ."     
    call KittyFace("sly", 1) from _call_KittyFace_635
    $ Count2 = 0
    $ Tempmod = 50
    call Kitty_SexMenu from _call_Kitty_SexMenu_1    
    ch_k "I think I learned a few things there. . ."
    return
    
label Kitty_Strip_Study_Wrong:
    call KittyFace("sly", 1) from _call_KittyFace_636
    if Count == 1:
        ch_k "Nope."
    elif Count == 2:
        ch_k "{i}So{/i} close. One more try."
    elif Count > 2:
        ch_k "Aw, too bad, so sad. Maybe next time."
        $ Count2 = 0
        
    return

label Quiz_Question_Kitty:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_k "Ok, do you[K_like]know where I come from? What's my home town?"
            "A. Chicago, Illinois": 
                return 0 
            "B. Deerfield, Illinois": 
                return 1 
            "C. New York City, New York":        
                return 0 
            "D. St. Louis, Missouri": 
                return 0 
    if QuizOrder[Count2] == 2:          
        menu: 
            ch_k "What's my mutant power called?"
            "A. Disappearing": 
                return 0 
            "B. Ghosting": 
                return 0 
            "C. Phasing": 
                return 1 
            "D. Shifting": 
                return 0 
    if QuizOrder[Count2] == 3: 
        menu:
            ch_k "So. . . don't laugh, but I have this stuffed animal I sleep with[K_like]every night. Know his name?"
            "A. Draco": 
                return 0 
            "B. Flipper": 
                return 0 
            "C. Lockheed": 
                return 1 
            "D. N'gari": 
                return 0 
                    
    if QuizOrder[Count2] == 4: 
        menu:                
            ch_k "Okay. Did you know that Dr. McCoy takes a handful of students that're falling behind in their Earth Science studies on a private tutoring retreat? Know where he takes them?"
            "A. The Great Redwood Forest, California": 
                return 1 
            "B. Mount McKinley, Alaska": 
                return 0 
            "C. Mount Rushmore, South Dakota": 
                return 0 
            "D. Yellowstone National Park, Wyoming": 
                return 0 
    if QuizOrder[Count2] == 5: 
        menu:
            ch_k "One of the worst threats we have to worry about as mutants are the giant robots called Sentinels. Do you know who built them?"
            "A. Arcade": 
                return 0 
            "B. Bolivar Trask": 
                return 1 
            "C. Magneto": 
                return 0 
            "D. Unus the Untouchable": 
                return 0 
    if QuizOrder[Count2] == 6: 
        menu:
            ch_k "Y'know, we didn't always have classes here at the Institute. For a while, all the students here went to a local public school. Know which one?" 
            "A. Bayville High School": 
                return 1 
            "B. King Memorial High School":
                return 0 
            "C. Riverside High School": 
                return 0 
            "D. Seth Paine High School": 
                return 0 
    if QuizOrder[Count2] == 7: 
        menu:
            ch_k "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
            "A. Jean Grey": 
                return 0 
            "B. Lance Alvers": 
                return 1 
            "C. Mystique": 
                return 0 
            "D. Professor Xavier": 
                return 0 
    if QuizOrder[Count2] == 8: 
        ch_k "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation." 
        ch_k "Even though it was a lot of fun, we ended up disbanding after that." 
        menu:
            ch_k "Anyway, know what the name we chose for the group was?"
            "A. The Bayville Avengers": 
                return 0 
            "B. The Bayville Brawlers": 
                return 0 
            "C. The Bayville Harpies": 
                return 0 
            "D. The Bayville Sirens": 
                return 1 
    if QuizOrder[Count2] == 9: 
        menu:
            ch_k "Okay[K_like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
            "A. A hot shower": 
                return 0 
            "B. Methyl Ethyl Ketone": 
                return 0 
            "C. Isolation": 
                return 1 
            "D. Tomato Juice": 
                return 0 
    if QuizOrder[Count2] == 10: 
        menu:
            ch_k "When I'm using my powers, I'm not[K_like]{i}totally{/i} invulnerable. Who has powers that can still affect me?"
            "A. Blob": 
                return 0 
            "B. Magneto": 
                return 0 
            "C. Quicksilver": 
                return 0 
            "D. Scarlet Witch": 
                return 1

 #remove this once I have enough questions
    "You answer the question correctly."
    return 1
    
#label Quiz:
#    $ Count = 0                                         #This is the number of times you've gotten a wrong answer. 
#    $ Count2 = 1                                        #this is the position in the quis so far. 
#    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # The entire list of objects. . .
#    $ renpy.random.shuffle(QuizOrder)                   # . . .shuffled randomly. . .    This is optional, and if you want to skip randomization then you can just increment a counter instead of this.
    
#    while Count2:                                       #This cycles so long as Count2 is greater than zero
#        "Question [Count2],"
#        call Quiz_Question
#        $ Count2 += 1                                   #This increments to the next question in the list after ti asks each one
#        if _return:                                     #the _return variable is whatever the Quiz Questions lable returns.
#            "You got it right!"
#            $ Score += 1                                #This tallies the right answers as you make them
#        else:
#            "Bzzt, Wrong answer"
#            $ Count += 1
#        if Count2 >= 14: #set this to one under the total number of questions
#            "You're done. Your score is [Score] out of 15."            
#            $ Count2 = 0           
#        elif Count > 2:                                 #this kicks you out if you get three wrong, remove that if you don't want it. 
#            "Too bad, you're done"
#            $ Count2 = 0                                #This breaks the cycle and returns the player to where he started the quiz. 
#    return
    
#label Quiz_Question:
#    if QuizOrder[Count2] == 1:                          #This asks the first question, set each following question to a number.
#        menu:
#            "Question"
#            "A. ":
#                return 1                                #the correct answer sends a 1, the incorrect answers send back a zero. 
#            "B. ":
#                return 0
#            "C. ":
#                return 0
#            "D. ":
#                return 0


          