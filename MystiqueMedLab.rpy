# Start MystiqueMedLabStart
# Update her other events to match
label MystiqueMedLabStart:
    $ bg_current = "bg classroom"
    $ newgirl["Mystique"].Outfit = "teacher"
    call CleartheRoom("Mystique",0,1)
    $ newgirl['Mystique'].Loc = "bg teacher"
    call Shift_Focus("Mystique")
    call Set_The_Scene
    $ Mystique_SpriteLoc = StageCenter      
    $ newgirl["Mystique"].GirlName = "Ms. Darkholme"
    
    "You enter the classroom and see that [newgirl[Mystique].GirlName] is already standing behind the podium."   
    call NewGirl_Face("Mystique", "normal")
    ch_m "Good morning, everyone, please find your seats so we can get started"
    "You quickly find your seat and get settled."
    with Pause(1)
    "A few moments later Ms. Darkholme begins the class." 
    "For some reason you feel really tired today and you quickly start to dose off."
    call BlinkEyes
    scene black
    with Pause(1)
    call CleartheRoom("Mystique",0,1)
    $ newgirl["Mystique"].Loc = "bg classroom"
    "You suddenly feel someone tapping on your shoulder."
    call NewGirl_Face("Mystique", "angry")
    $ newgirl["Mystique"].Girl_Arms = 1
    call Set_The_Scene
    "Ms. Darkholme stands before you with a strict face."
    call NewGirl_Face("Mystique", "angry")
    "She stares at you for a bit and looks like she's about to give you a scolding for falling asleep during class."
    "But then she starts smiling."
    call NewGirl_Face("Mystique", "grimace")
    ch_m "Calm down, Mr. [Playername], I'm just messing with you."
    call NewGirl_Face("Mystique", "normal")
    ch_m "This might be a bit unusual, but I have a favor to ask of you."
    menu:
        extend ""
        "Sure!":
            ch_p "Sure! What can I do for you, [newgirl[Mystique].GirlName]?"
            call NewGirl_Face("Mystique", "smile")
            "She seems happy with my reply and puts on a smile."
            ch_m "I need you to meet me in the med lab tonight."
            menu:   
                extend ""  
                "The med lab?":
                    "In your head you start going through the possible reasons for why she would want you there."
                    "She's just a teacher after all..."
                    call NewGirl_Face("Mystique", "sly")
                    "She quickly notices the look of confusion on your face."
                    ch_m "You look a bit confused, Mr. [Playername]."
                    ch_m "I bet you're wondering why I want you in the med lab."
                    call NewGirl_Face("Mystique", "normal")
                    ch_m "Allow me to explain."
                    ch_m "You see, besides filling in for Professor McCoy in class, I've also taken over his duties in the lab."
                    ch_m "I just want to do some medical checks on you, to see if you are all healthy and in good shape."
                    menu:
                        extend ""
                        "Why?":
                            ch_p "I don't understand why you're so interested in me, [newgirl[Mystique].GirlName]."
                            ch_p "As far as I know you haven't asked this of any other student."
                            call NewGirl_Face("Mystique", "sly")
                            ch_m "I'm interested in your powers."
                            ch_m "They are quite impressive, and in the wrong hands, could pose a huge risk to every mutant out there."
                            ch_m "Even to the strongest of them, like Professor Xavier and Magneto!"
                            with Pause(1)
                            ch_p "Oh..."
                            with Pause(1)
                            ch_p "So I'm pretty special, right?"
                            call NewGirl_Face("Mystique", "laugh")
                            "She immediately starts laughing."
                            ch_m "Don't let it get to your head, Mr. [Playername]."
                            ch_m "Like this boy I met once said..."
                            with Pause(1)
                            ch_m "With great power comes great responsability!"
                            with Pause(1)
                            ch_p "Hm, he sounds like a little sissy if you ask me.."
                            call NewGirl_Face("Mystique", "angry")
                            ch_m "...."
                            call NewGirl_Face("Mystique", "normal")
                            ch_m "Anyways, what do you say? Will you meet me in the med lab tonight?"
                            menu:
                                extend ""
                                "Yes": 
                                    ch_p "Okay, [newgirl[Mystique].GirlName], I'll be there!"
                                    call NewGirl_Face("Mystique", "sly")
                                    ch_m "Good, I'll see you tonight then, Mr. [Playername]"
                                "Flirty response":
                                    ch_p "At night, huh? So you're thinking about something naugty, right?"
                                    call NewGirl_Face("Mystique", "sexy")
                                    ch_m "That wasn't the plan, but maybe I'll se about rewarding you if you behave."
                                    call NewGirl_Face("Mystique", "normal")
                                    ch_m "See you tonight, Mr. [Playername]."
                                            
                            
                    
            
        
    return
    
    
    
    