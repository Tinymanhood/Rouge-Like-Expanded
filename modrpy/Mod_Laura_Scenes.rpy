
# start LauraMeet//////////////////////////////////////////////////////////

label LauraMeet(Topics=[],Loop=1):
    $ newgirl["Laura"].Legs = "mesh pants"
    $ newgirl["Laura"].Pubes = 1

    $ newgirl["Laura"].GirlName = "???"
    
    $ bg_current = "bg dangerroom"   
    call CleartheRoom("All",0,1)
    $ newgirl["Laura"].Loc = "bg dangerroom"  
    $ newgirl["Laura"].Love = 400        
    $ newgirl["Laura"].Obed = 0            
    $ newgirl["Laura"].Inbt = 200  
    call Shift_Focus("Laura")    
    $ newgirl["Laura"].SpriteLoc = StageCenter
    call Set_The_Scene(0)
    $ newgirl["Laura"].Petname = Playername   
    
    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."   
    call LauraFace("normal", 0) 
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc)
    "When you come to, a girl pulls you up by your arm."     
    call LauraFace("surprised", 0, Eyes="squint",Brows="sad") 
    ch_u "Oh, good, you don't look too damaged." 
    call LauraFace("smile", 0, Brows="sad") 
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door." 
    call LauraFace("smile", 0) 
    while Loop:
        menu:
            extend ""
            "Who are you?" if newgirl["Laura"].GirlName == "???":
                    call LauraFace("normal", 0) 
                    ch_l "I go by \"X-23\" in the field."
                    $ newgirl["Laura"].GirlName = "X-23"        
            "X-23? Is that your real name?" if newgirl["Laura"].GirlName == "X-23" and "X23" not in Topics:
                    call LauraFace("confused", 0) 
                    ch_l "It's the one I was born with."
                    $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and "Laura" not in Topics:
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 5) # Love
                    call LauraFace("normal", 0) 
                    ch_l "I also go by Laura. Laura Kinney."
                    call LauraFace("confused", 0, Mouth="normal") 
                    $ newgirl["Laura"].GirlName = "Laura"       
                    $ Topics.append("Laura")    
                    menu:
                        extend ""
                        "Nice to meet you Laura.": 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 5) # Love  
                            call LauraFace("normal", 0)                
                            ch_l "Yeah, ok."
                        "Hello Laura Laura Kinney.":
                            call LauraFace("confused", 0,Mouth="sucking")   
                            ch_l "It's just-"
                            call LauraFace("smile", 0,Brows="surprised")   
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 3) # Love   
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) # Inbt   
                            ch_l "Oh, get it."
                        "Ok, how did you get that name?":
                            call LauraFace("angry", 1,Eyes="side") 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2) # Love   
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2) # Obed 
                            ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if newgirl["Laura"].GirlName == "Laura" and "Laura" in Topics:
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2) # Love   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5) # Obed 
                    call LauraFace("sadside", 0,Brows="normal") 
                    ch_l "Suit yourself."
                    $ newgirl["Laura"].GirlName = "X-23"     
            "My name is [Playername]" if newgirl["Laura"].GirlName != "???" and "player" not in Topics:
                    call LauraFace("normal", 0) 
                    ch_l "Ok."     
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .and it's nice to meet you?":
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1) # Love 
                            call LauraFace("confused", 0,Mouth="normal")   
                            ch_l "Yeah, you too." 
                        "So. . .[[moving on]":
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 3) # Love   
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 1) # Obed
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) # Inbt  
                            
            "What are you doing here?" if "Training" not in Topics:
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -2) # Obed
                    call LauraFace("confused", 0) 
                    ch_l "Training. That's the point of this place."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "I meant in the school, I haven't seen you around before.":
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2) # Obed 
                        "Ok, that's fair.":
                                call LauraFace("normal", 0) 
                                ch_p "But are you new to this school?"
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 3) # Love   
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 4) # Obed
                    ch_l "I've been here since before your time."
                    ch_l "Mostly out in the field though."   
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:  
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2) # Love   
                    call LauraFace("normal", 0,Eyes="side") 
                    ch_l "I'll be heading out again soon." 
                    call LauraFace("normal", 0) 
                    ch_l "But I am planning to stick around after I get back from this mission."
                    $ Topics.append("Stay")
                
                        
            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2) # Love   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 8) # Obed  
                    call LauraFace("confused", 0) 
                    ch_l "It was a robot arm." 
                    call LauraFace("sad", 1,Eyes="leftside") 
                    ch_l "Like I said, sorry."                   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -3) # Obed
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) # Inbt  
                    call LauraFace("smile", 0,Brows="confused") 
                    ch_l "You probably should have ducked though."
                    $ Topics.append("WTF")
                
            "So what's your mutant power?" if newgirl["Laura"].GirlName != "???" and "claws" not in Topics:
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1) # Love   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 1) # Obed                    
                    call LauraFace("normal", 0) 
                    ch_l "I can heal fast."
                    $ newgirl["Laura"].Girl_Arms = 2
                    ch_l "Also I have claws."
                    $ newgirl["Laura"].Claws = 1
                    call LauraFace("smile", 0,Brows="confused") 
                    "snikt"
                    $ Topics.append("claws")
                    menu:                        
                        "Those claws look pretty sharp.":
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) # Inbt   
                                ch_l "Yeah, indestructible too." 
                        "Cool.":
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 3) # Love   
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2) # Obed
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) # Inbt   
                                call LauraFace("smile", 0,Brows="surprised") 
                                ch_l "Yeah, indestructible too." 
                        "Ouch.": 
                                $ newgirl["Laura"].Claws = 0
                                call LauraFace("confused", 0) 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2) # Love   
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -5) # Obed  
                                ch_l "Don't worry, I won't stab you." 
                                call LauraFace("confused", 0,Mouth="normal")      
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 7) # Inbt   
                                ch_l "Probably."  
                    $ newgirl["Laura"].Claws = 0
                    $ newgirl["Laura"].Girl_Arms = 1
                            
            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                    if newgirl["Laura"].Love >= 405: 
                            call LauraFace("smile", 0,Brows="confused") 
                            ch_l "Yeah, I guess."
                    else:
                            call LauraFace("normal", 0) 
                            ch_l "Not really."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) # Inbt   
                    $ Topics.append("powers")
                    ch_p "I'm immune to mutant powers and can shut them off." 
                    call LauraFace("smile", 0,Brows="confused") 
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 3) # Love   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 3) # Obed  
                    ch_l "Huh. Interesting. So you can stop me from healing?"
                    ch_p "Yeah. If I touch you, temporarily."  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2) # Obed 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 3) # Lust   
                    ch_l "Give it a try."
                    "She holds out her arm, and you grab it."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1) # Love   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2) # Obed 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5) # Lust  
                    call LauraFace("confused", 0) 
                    ch_l "Huh." 
                    call LauraFace("sexy", 1,Eyes="closed") 
                    "You can feel her shudder a little." 
                    call LauraFace("sexy", 1) 
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1) # Love   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 3) # Obed
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5) # Lust  
                    ch_l "That feels weird."  
                    call LauraFace("sexy", 1,Eyes="leftside") 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 1) # Obed 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 3) # Lust  
                    ch_l "-a little more \"alive\" than usual." 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 5) # Inbt  
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5) # Lust 
                    call LauraFace("sexy", 1,Brows="confused")   
                    ch_l "Almost. . . dangerous."
                
            "Never mind that. . . [[moving on]" if newgirl["Laura"].GirlName != "???":
                    $ Loop = 0
            
        if len(Topics) >= 3 and newgirl["Laura"].GirlName == "???":
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2) # Love   
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5) # Obed
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 5) # Inbt   
                ch_l "Oh, by the way, you can call me \"X-23\"."
                $ newgirl["Laura"].GirlName = "X-23"  
        if len(Topics) >= 8:
                $ Loop = 0
        
        
    #close while loop
    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2) # Love   
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 1) # Lust  
            call LauraFace("smile",0) 
            ch_l "Maybe I'll see you when I get back, [Playername]."
    else:
            call LauraFace("normal", 0) 
            ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2) # Obed
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) # Inbt  
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 3) # Lust   
            call LauraFace("smile", 1, Brows="confused") 
            ch_l "We should. . . spar."


    call LauraFace("sexy", B=2)
    ch_l "Hey, before I go, how about I give you a handjob so you can remember me?"
    call L_Handjob 
         
    $ newgirl["Laura"].Loc = "bg laura"         
    call Set_The_Scene
    
    "She dashes out of the room, headed for the hanger."
    
    $ newgirl["Laura"].History.append("met")
    $ bg_current = "bg dangerroom"            
    $ Round -= 10      
    call Shift_Focus("Rogue")
    return

# end LauraMeet//////////////////////////////////////////////////////////