﻿# This is the section for Laura's sex-related dialog options to be chosen. 

label Laura_SexDialog(TempLine = 0, TempLust = 0, TempLust2 = 0):    
    if Situation == "skip" and Line:
            # if the action was set by a previous trigger, skip this element
            $ Situation = 0
            return
    
    if Trigger == "hand":
            $ Line = "Laura continues stroke your cock. "
               
            if not Speed:
                        $ Line = "Laura holds your cock in her hand. "
                        if newgirl["Laura"].Hand > 2:
                                $ Line = Line + "She just seems to be enjoying the feel of it"
                                $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
                        else:
                                $ Line = Line + "She just seems to be looking it over"
                                $ TempLust += 2 if newgirl["Laura"].Lust < 40 else 0
                                $ TempFocus += -3 if P_Focus > 50 else 2
                            
                        $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 2
                        return
            
            if newgirl["Laura"].Hand > 4:                          # After the 5th time 
                        if Speed <= 1:                      #slow 
                            $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching", 
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])   
                            
                            $ TempFocus += 20 if P_Focus > 70 else 5
                                  
                        else:                               #fast
                            $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching", 
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"]) 
                            
                            $ TempFocus += 20 if P_Focus < 40 else 5        
                    
            elif 2 < newgirl["Laura"].Hand <= 4:                       #third through 5th time
                        if Speed <= 1:                      #slow
                            $ Line = Line + renpy.random.choice(["She's beginning to figure things out, her fingers cause tingles as they caress the shaft", 
                                    "She's still learning, but learning fast. Her hands sure are smooth", 
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She gently caresses the shaft, and cups the balls in her other hand, giving them a warm massage"])  
                            
                            $ TempFocus += 15 if P_Focus > 60 else 5
                            
                        else:                               #fast
                            $ Line = Line + renpy.random.choice(["She's beginning to figure things out, her fingers cause tingles as they caress the shaft", 
                                    "She's still learning, but learning fast. Her hands sure are smooth", 
                                    "Her hands glide smoothly across your cock",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She quickly strokes your cock, with a very deft pressure"]) 
                            
                            $ TempFocus += 15 if P_Focus < 60 else 7         
                
            else:                                   #First and second time
                    if Speed <= 1:                      #slow
                        $ Line = Line + renpy.random.choice(["Laura seems determined, carefully stroking your cock", 
                                "She moves her hands up and down the shaft. She's a little rough at this, but at least she tries", 
                                "She strokes you gently. She isn't quite sure what to make of the balls",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This may take a few tries"])     
                        
                        $ TempFocus += 12 if P_Focus > 60 else 5         
                    else:                               #fast 
                        $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips out of her hand", 
                                "She rapidly moves her hands up and down the shaft. She's a little rough at this, but at least she tries", 
                                "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This train is out of control"])  
                        
                        $ TempFocus += 10 if P_Focus > 60 else 2         
                    
            $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
            $ TempLust += 2 if newgirl["Laura"].Hand > 2 else 0
            $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 2
            
    #End Handy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////
          
          
    elif Trigger == "titjob":     
            #This can only ever be a primary action. 
            
            if not Speed:
                        if newgirl["Laura"].Tit > 2:
                            $ Line = "Laura begins to slide her breasts up and down"
                        else:
                            $ Line = "Laura squeezes her breasts together and slowly moves them along your shaft"
                        $ Speed = 1
                        $ TempFocus += 12 if P_Focus < 60 else 6                      
                        $ TempLust += 6 if newgirl["Laura"].Lust > 60 else 3 
                        return
            
            if newgirl["Laura"].Tit > 4 and newgirl["Laura"].Blow:                                        #5th+ and blown
                        if Speed <= 1:                                              #slow
                            $ Line = renpy.random.choice(["Laura slides her breasts up and down around your cock", 
                                    "Laura lightly licks the head as it pops up between her tits", 
                                    "Laura has a smooth motion going now, gentle and precise",
                                    "Laura pauses to rub her nipples across the shaft",
                                    "In between strokes Laura gently sucks on the head",
                                    "Laura drips some spittle down to make sure you're properly lubed",
                                    "Laura gently caresses the shaft between her tits"])            
                            
                            $ TempFocus += 15 if P_Focus < 70 else 5                      
                            $ TempLust += 7 if newgirl["Laura"].Lust > 60 else 4       
                        else:                                                       #fast
                            $ Line = renpy.random.choice(["Laura rapidly slides her breasts up and down around your cock", 
                                    "Laura licks away at the head every time it pops up between her tits", 
                                    "Laura has a smooth motion going now, quick by efficient",
                                    "Laura dances her nipples across the shaft",
                                    "In as she strokes faster and faster, Laura bends down to suck on the head",
                                    "Laura covers her tits with drool to keep them well lubed",
                                    "Laura rapidly caresses the shaft between her tits"])
                            
                            $ TempFocus += 20 if P_Focus > 40 else 5                      
                            $ TempLust += 6 if newgirl["Laura"].Lust > 70 else 4    
                     
                
            elif newgirl["Laura"].Tit > 1:                                                 #third through 5th time
                    if Speed <= 1:                                              #slow
                        $ Line = renpy.random.choice(["Laura juggles her breasts up and down around your cock", 
                                "Laura lightly strokes the head as it pops up between her tits", 
                                "Laura has a smooth motion going now, gentle and precise",
                                "Laura pauses to rub her nipples across the shaft",
                                "Laura gently caresses the shaft between her tits"]) 
                        
                        $ TempFocus += 15 if P_Focus < 60 else 5                      
                        $ TempLust += 6 if newgirl["Laura"].Lust > 60 else 3                        
                    else:                                                       #fast
                        $ Line = renpy.random.choice(["Laura rapidly juggles her breasts up and down around your cock", 
                            "Laura lightly brushes the head with her chin as it pops up between her tits", 
                            "Laura moves them up and down in a fluid rocking motion",
                            "Laura bounces her whole body up and down",
                            "Laura rapidly slides the shaft between her tits"])   
                        
                        $ TempFocus += 15 if P_Focus > 50 else 7                      
                        $ TempLust += 6 if newgirl["Laura"].Lust > 60 else 4    
                       
            else:                                                           #First and second time
                    if Speed <= 1:                                              #slow
                        $ Line = renpy.random.choice(["Laura sort of squishes her breasts back and forth around your cock", 
                            "Laura slides the cock up and down between her cleavage", 
                            "Laura kind of bounces her tits around your cock",
                            "Laura smooshes her cleavage as tight as she can and rubs up and down"])
                        
                        $ TempFocus += 12 if P_Focus < 60 else 6                      
                        $ TempLust += 6 if newgirl["Laura"].Lust > 60 else 3    
                                        
                    else:                                                       #fast
                        $ Line = renpy.random.choice(["Laura sort of bounces her breasts off your cock", 
                            "Laura tries to quickly slide the cock up and down between her cleavage, but it tends to slide out", 
                            "Laura slaps her tits against your dick",
                            "Laura smooshes her cleavage as tight as she can and rubs up and down quite quickly"])  
                        
                        $ TempFocus += 8 if P_Focus > 70 else 4                      
                        $ TempLust += 5 if newgirl["Laura"].Lust > 60 else 3    
              
            $ newgirl["Laura"].Addict -= 2
    #End Action Titfuck ///////////////////////////////////////////////////////////////////////////////
           
           
    elif Trigger == "blow":
        
            if not Speed: #if Laura is not moving                
                    if "hungry" in newgirl["Laura"].Traits:
                            call LauraFace("sly")
                            $ Line = "Laura stares at your cock. She licks her lips in anticipation"
                            $ TempLust += 3 if newgirl["Laura"].Lust < 40 else 1                    
                    elif newgirl["Laura"].Blow > 2:
                            call LauraFace("sly")
                            $ Line = "Laura stares at your cock. She seems pretty excited about it"
                            $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
                    else:
                            call LauraFace("perplexed")
                            $ Line = "Laura stares at your cock with trepidation"
                            $ TempLust += 2 if newgirl["Laura"].Lust < 40 else 0                    
                            $ TempFocus += -3 if P_Focus > 50 else 2
                        
                    if newgirl["Laura"].Blow <= 1 or (newgirl["Laura"].Obed >= 500 and newgirl["Laura"].Obed > newgirl["Laura"].Inbt):
                            $ TempLust += 2 if newgirl["Laura"].Lust > 60 else 0                 
                            $ Line = Line + ", but she seems to be waiting for some instruction"
                    else:
                            $ Line = Line + ", and then she gets started licking your cock"
                            $ Speed = 1
                        
                    return
                               
                
            elif Speed < 2: 
                        $ Line = "Laura continues to lick your cock. "        #if Laura is the primary but is licking
            else: 
                        $ Line = "Laura continues to suck your cock. "        #if Laura is the primary and is heading or sucking
             
            if Speed == 1:                                                                  #Speed 1 (licking)
                    if newgirl["Laura"].Blow > 4:                                                                  #After the 5th time
                            $ Line = Line + renpy.random.choice(["Her deft licks have become almost masterful, your cock twitches with each stroke", 
                                    "She gently blows across the head as she covers your cock in smooth licks", 
                                    "How many licks to the center of your cock? No way you're finding out",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and gentle licks",
                                    "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge dances around it"])  
                            $ TempFocus += 20 if P_Focus < 70 else 15                   
                            $ TempLust += 2 if newgirl["Laura"].Lust > 80 else 1
                        
                    elif newgirl["Laura"].Blow > 1:                                                                #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her tongue makes your hair stand on end", 
                                    "She's still learning, but learning fast. She seems eager to use her mouth for more than talk", 
                                    "She's settled into a gentle licking pace that washes over you like a warm bath",
                                    "She licks gently up and down the shaft. She's a little rough at this, but at least she tries", 
                                    "Her tongue moves carefully along the shaft",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She licks her way down the shaft, and gently teases the balls"]) 
                            $ TempFocus += 20 if P_Focus > 60 else 10                      
                            $ TempLust += 2 if newgirl["Laura"].Lust > 80 else 1    
                        
                    else:                                                                           #First and second time
                            $ Line = Line + renpy.random.choice(["Laura makes up for her inexperience with determination, carefully licking your cock", 
                                    "She takes a small lick and grimaces at the taste",
                                    "She tentatively kisses around the head a bit",            
                                    "She nibbles one of your balls, but stops when you wince",
                                    "She licks all over your dick, but she doesn't really have a handle on it"])  
                            $ TempFocus += 15 if P_Focus > 60 else 5                  
                    $ newgirl["Laura"].Addict -= 2
                
            elif Speed == 2:                                                                    #Speed 2 (heading)
                    if newgirl["Laura"].Blow > 4:                                                                  #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke", 
                                    "She rapidly bobs up and down on your cock, a frenzy of motion", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge swirls rapidly around it"]) 
                            $ TempFocus += 20 if P_Focus < 80 else 10                      
                            $ TempLust += 2 if newgirl["Laura"].Lust > 70 else 1    
                        
                    elif newgirl["Laura"].Blow > 1:                                                                #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the head", 
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip", 
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way around the head",
                                    "Her mouth envelopes the head, then she quickly draws it in and draws back with a pop"]) 
                            $ TempFocus += 15 if P_Focus > 80 else 10                      
                            $ TempLust += 1 if newgirl["Laura"].Lust > 60 else 0    
                        
                    else:                                                                           # First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often pops out of her mouth", 
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",             
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"]) 
                            $ TempFocus += 9 if P_Focus > 80 else 3    
                    $ newgirl["Laura"].Addict -= 2           
                
            elif Speed == 3:                                                                    #Speed 3 (sucking)
                    if newgirl["Laura"].Blow > 4:                                                                  #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke", 
                                    "She smoothly bobs up and down on your cock, a frenzy of motion", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the shaft into her mouth and her tounge swirls rapidly around it"]) 
                            $ TempFocus += 22 if P_Focus > 40 else 10                      
                            $ TempLust += 3 if newgirl["Laura"].Lust > 60 else 1    
                        
                    elif newgirl["Laura"].Blow > 1:                                                                #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft", 
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip", 
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way up and down the shaft as her mouth envelopes you",
                                    "Her mouth envelopes the shaft, then she quickly draws it in and draws back with a pop"])
                            $ TempFocus += 15 if P_Focus > 50 else 5  
                        
                    else:                                                                           #First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for putting it all the way in, and grimaces at the taste", 
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries", 
                                    "She sucks up and down your cock very quickly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"]) 
                            $ TempFocus += 6 if P_Focus < 50 else 3 
                    $ newgirl["Laura"].Addict -= 2 if D20S > 10 else 3
                        
                 
            else:#Speed = 4                                                                     #Speed 4+ (Deep Throat)
                    if newgirl["Laura"].Blow > 4:                                                                  #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke", 
                                    "She rapidly bobs to the base of your cock, a frenzy of motion", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the entire shaft into her mouth and her tounge swirls rapidly around it"])  
                            $ TempFocus += 25 if P_Focus > 40 else 8                      
                            $ TempLust += 3 if newgirl["Laura"].Lust > 60 else 2    
                        
                    elif newgirl["Laura"].Blow > 1:                                                                #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft", 
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip", 
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She completely envelops the shaft with her throat.",
                                    "Her mouth envelopes the head, then she quickly draws it all the way in and draws back with a pop"])  
                            $ TempFocus += 20 if P_Focus > 40 else 5                      
                            $ TempLust += -3 if newgirl["Laura"].Lust < 60 else -1                        
                            $ TempLust += 5 if newgirl["Laura"].Obed > 500 else 0  
                        
                    else:                                                                            #First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for going so deep, and gags a bit", 
                                    "She puts the whole shaft in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries", 
                                    "She draws your cock into her mouth very qucikly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"]) 
                            $ TempFocus += 15 if P_Focus > 80 else 5                      
                            $ TempLust += -5 if newgirl["Laura"].Lust < 60 else -2                       
                            $ TempLust += 7 if newgirl["Laura"].Obed > 500 else 0  
                    $ newgirl["Laura"].Addict -= 3
           
    # end newgirl["Laura"].Blowjob                                 //////////////////////////////////////////////////////////////////////////////
        
    elif Trigger == "sex": #Trigger4 not available
        
            if not Speed: #if Laura is not moving   
                    $ Line = "She seems to be waiting for you to do something. . "
                    return
                        
            elif Speed < 2: 
                    $ Line = "You continue to pound Laura. "        #if Laura is the primary but is licking
            else: 
                    $ Line = "You continue to slowly drive into Laura. "        #if Laura is the primary and is heading or sucking
            
            if newgirl["Laura"].Sex > 4:
                if Speed > 1:                       # After the 5th time fast
                        $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                            "You thrust into her and she squeaks a bit",
                            "You quickly grind back and forth inside her",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at her",    
                            "She grinds furiously back and forth along your cock"])
                        $ TempFocus += 18 if P_Focus > 50 else 12                   
                        $ TempLust += 16 if newgirl["Laura"].Lust > 70 else 10                    
                else:                        # After the 5th time slow
                        $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                            "You thrust into her and she coos a bit",
                            "You slowly grind back and forth inside her",
                            "You alternate between long and slow thrusts, and the occasional quick one",
                            "You slowly slide back and forth near the entrance",    
                            "She slides slowly back and forth along your cock, teasing you"])
                        $ TempFocus += 14 if P_Focus < 60 else 12                   
                        $ TempLust += 12 if 40 > newgirl["Laura"].Lust > 90 else 10                        
                        
            elif newgirl["Laura"].Sex > 1:
                if Speed > 1:             #third through 5th time fast
                    $ Line = Line + renpy.random.choice(["Laura bounces rapidly against your cock", 
                        "You thrust into her and she squeaks a bit",
                        "You quickly grind back and forth inside her",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You pound away at her",    
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += 12 if P_Focus > 50 else 9                   
                    $ TempLust += 14 if newgirl["Laura"].Lust > 80 else 10
                else:             #third through 5th time slow
                    $ Line = Line + renpy.random.choice(["she bumps slowly against your cock", 
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",    
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 12 if P_Focus < 70 else 7                   
                    $ TempLust += 10 if 50 > newgirl["Laura"].Lust > 90 else 8
                    
            else:
                if Speed > 1:            # First and second time fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust into her and she squeeks in pain",
                        "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                        "You pound away at her",    
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                    $ TempFocus += 10 if P_Focus > 60 else 9                   
                    $ TempLust += 10 if newgirl["Laura"].Lust > 80 else 6
                else:            # First and second time slow
                    $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",    
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 10 if P_Focus < 70 else 9                   
                    $ TempLust += 8 if 60 > newgirl["Laura"].Lust > 90 else 6
                    
            $ newgirl["Laura"].Addict -= 2
            
    # end newgirl["Laura"].Sex                                 ////////////////////////////////////////////////////////////////////////////// 
            
    elif Trigger == "hotdog": #Trigger4 not available
            #TempLust2 in this action is how much lower body clothing she has on, it gets cleared at the end.
            $ TempLust2 = 2
            if newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #if panties are in the way
                $ TempLust2 -= 1
            if HoseNum("Laura") >= 6: #if complete hose
                $ TempLust2 -= 1        
            if newgirl["Laura"].Legs and not newgirl["Laura"].Upskirt: #If pants/skirt is up
                $ TempLust2 -= 2 if TempLust2 <= 2 else TempLust2
                
            if not Speed:
                $ Line = "She seems to be waiting for you to do something. . "
                return
            elif Speed < 2: 
                    $ Line = "You continue to hotdog Laura. "       
            else: 
                    $ Line = "You continue to grind against Laura. " 
                    
            if newgirl["Laura"].Hotdog >= 2:
                if Speed > 1:       # After the 2ndtime fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust against her and she squeaks a bit",
                        "You quickly grind back and forth along her crack",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You grind away at her",    
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += (TempLust2 + 8) if P_Focus < 60 else (TempLust2 + 4)
                    $ TempLust += (TempLust2 + 8) if 50 > newgirl["Laura"].Lust > 80 else (TempLust2 + 2)
                    
                elif Speed:        #2nd time slow
                    $ Line = Line + renpy.random.choice(["She grinds slowly against your cock", 
                        "You thrust against her and she coos a bit",
                        "You slowly rub the tip across her pussy",
                        "You alternate between long and slow thrusts, and the occasional rapid ones",
                        "You slowly slide back and forth near her rim",    
                        "She slides slowly back and forth along your cock, teasing you"])                    
                    $ TempFocus += (TempLust2 + 8) if P_Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 7) if 30 > newgirl["Laura"].Lust > 70 else (TempLust2 + 3)
                    
            else: #If you haven't done hotdog before       
                if Speed > 1:       #fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust into her and she squeeks in surprise",
                        "You quickly grind back and forth against her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally sliding out and having to stick it back in",
                        "You pound away at her",    
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])                    
                    $ TempFocus += (TempLust2 + 5) if P_Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 4) if 50 > newgirl["Laura"].Lust > 80 else (TempLust2 + 2)
                    
                elif Speed:         #slow
                    $ Line = Line + renpy.random.choice(["She grinds slowly against your cock", 
                        "You thrust into her crack and she squeaks a bit",
                        "You slowly grind back and forth across her rear",            
                        "You slowly slide back and forth near her rim",    
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += (TempLust2 + 5) if P_Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 5) if 50 > newgirl["Laura"].Lust > 70 else (TempLust2 + 2)
            
            if TempLust2:
                $ newgirl["Laura"].Addict -= 1  
                $ TempLust2 = 0
        
    # end newgirl["Laura"].Hotdog                                 //////////////////////////////////////////////////////////////////////////////
            
         
    elif Trigger == "anal": #Trigger4 not available
        
            if not Speed:
                $ Line = "She seems to be waiting for you to do something. . "
                return
                
            elif Speed < 2: 
                    $ Line = "You continue to pound into Laura's ass. "       
            else: 
                    $ Line = "You continue to push into Laura's ass. " 
                    
                 
            if newgirl["Laura"].Anal >= 5:
                    if Speed > 1:#Fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",    
                                "She grinds furiously back and forth along your cock"])
                            $ TempFocus += 19 if P_Focus > 60 else 13                   
                            $ TempLust += 14 if newgirl["Laura"].Lust > 80 else 9
                        
                    else:#Slow
                            $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                                "You thrust into her and she coos a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",    
                                "She slides slowly back and forth along your cock, teasing you"])
                            $ TempFocus += 13 if P_Focus > 60 else 10                   
                            $ TempLust += 12 if 50 < newgirl["Laura"].Lust < 90 else 8
                              
            else: #if newgirl["Laura"].Loose:     #You've done some anal stuff before       
                    if Speed > 1:             #third through 5th time fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",    
                                "She grinds furiously back and forth along your cock"])                            
                            $ TempFocus += 13 if P_Focus > 60 else 9                   
                            $ TempLust += 12 if newgirl["Laura"].Lust > 80 else 6
                        
                    elif Speed:             #third through 5th time
                            $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",    
                                "She slides slowly back and forth along your cock"])
                            $ TempFocus += 14 if P_Focus > 60 else 9                   
                            $ TempLust += 8 if 70 > newgirl["Laura"].Lust > 90 else 4
            
                            
            $ TempLust = 0 if (newgirl["Laura"].Lust - TempLust) < 0 else TempLust
            
    # end newgirl["Laura"].Anal                                 //////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "fondle breasts":   
                    $ Line = "You continue to fondle Laura. "    
                    if newgirl["Laura"].Over and newgirl["Laura"].Chest: #Full top
                                $ Line = Line + renpy.random.choice(["You reach under her layers of clothing and massage her breasts", 
                                    "You pass your hands gently over her warm breasts", 
                                    "Her firm nipples catch on the fabric of her top as you grasp her warm flesh",
                                    "She gasps as you grasp her under her top"])
                                $ TempFocus += 2 if P_Focus < 40 else 1  
                                $ TempLust += 4 if newgirl["Laura"].Lust > 50 else 2
                    elif newgirl["Laura"].Over:        #Just overtop
                                $ Line = Line + renpy.random.choice(["You reach under her top and massage her breasts", 
                                    "You pass your hands gently over her warm breasts", 
                                    "Her nipples catch on the fabric of her top as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her top"])
                                $ TempFocus += 2 if P_Focus < 50 else 1
                                $ TempLust += 4 if newgirl["Laura"].Lust > 50 else 2   
                    elif newgirl["Laura"].Chest:       #just bra
                                $ Line = Line + renpy.random.choice(["You reach under her tight top and massage her breasts", 
                                    "You pass your hands gently over her warm breasts", 
                                    "Her nipples catch on the fabric of her top as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her top"])
                                $ TempFocus += 3 if P_Focus < 60 else 2    
                                $ TempLust += 5 if newgirl["Laura"].Lust > 50 else 2    
                    elif newgirl["Laura"].Pierce: #pierced
                                $ Line = Line + renpy.random.choice(["You reach out and massage her glorious breasts", 
                                    "You pass your hands gently over her warm breasts, and blow across her pierced nipples", 
                                    "Her piercings catch lightly on your fingers as you grasp her warm flesh, you can see the nipples stiffen",
                                    "She gasps as you lightly thumb across her pierced nipples"])
                                $ TempFocus += 4 if P_Focus < 70 else 2 
                                $ TempLust += 6 if newgirl["Laura"].Lust > 40 else 4  
                    else: #topless
                                $ Line = Line + renpy.random.choice(["You reach out and massage her glorious breasts", 
                                    "You pass your hands gently over her warm breasts, and blow across her nipples", 
                                    "Her nipples catch lightly on your fingers as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you lightly thumb her rigid nipples"])
                                $ TempFocus += 4 if P_Focus < 60 else 2 
                                $ TempLust += 6 if newgirl["Laura"].Lust > 50 else 3  
                    $ newgirl["Laura"].Addict -= 2
                  
    # end R Fondle breasts                                 //////////////////////////////////////////////////////////////////////////////
    elif Trigger == "suck breasts":  
                    $ Line = "You continue to suck on Laura's breasts. "    
                    if newgirl["Laura"].Over and newgirl["Laura"].Chest: #Full top
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the layered tops",
                                        "You  place a nipple between your lips, and give it a quick tug through the layered tops",
                                        "She gasps as you gently nibble her rigid nipples poking through her tops"])      
                                $ TempFocus += 2 if P_Focus < 50 else 1  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 30 else 1
                    elif newgirl["Laura"].Over:        #Just overtop
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the light top",
                                        "You tease her nipples with your tongue through the fabric",
                                        "You slowly lick her nipples through her moist top", 
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her top"])    
                                $ TempFocus += 2 if P_Focus < 50 else 1
                                $ TempLust += 5 if newgirl["Laura"].Lust > 50 else 3
                    elif newgirl["Laura"].Chest:       #just bra
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You tease her nipples with your tongue through her top",
                                        "You slowly lick her nipples through her moist top", 
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her top"])   
                                $ TempFocus += 4 if P_Focus < 60 else 3    
                                $ TempLust += 5 if newgirl["Laura"].Lust > 50 else 2    
                    elif newgirl["Laura"].Pierce: #pierced
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her piercings with your tongue",
                                    "You slowly lick around, and then blow across her nipples", 
                                    "You gently place a pierced nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if P_Focus < 70 else 4 
                                $ TempLust += 10 if newgirl["Laura"].Lust > 40 else 7
                                $ newgirl["Laura"].Addict -= 2
                    else: #topless
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her nipples with your tongue",
                                    "You slowly lick around, and then blow across her nipples", 
                                    "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if P_Focus < 60 else 3 
                                $ TempLust += 10 if newgirl["Laura"].Lust > 50 else 7  
                                $ newgirl["Laura"].Addict -= 2
           
    # end R Suck breasts                                 //////////////////////////////////////////////////////////////////////////////
        
    elif Trigger == "fondle thighs":  #Trigger4 not available
                    $ Line = "You continue to massage Laura's thighs. "   
                    
                    if (newgirl["Laura"].Legs == "leather pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                $ Line = renpy.random.choice(["Her legs twitch a bit in her jeans as you caress them", 
                                        "She gasps as you stroke her warm thighs through the jeans",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her . . ."])                              
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 1 if newgirl["Laura"].Lust < 50 else 0
                            
                    elif newgirl["Laura"].Legs == "skirt" and HoseNum("Laura") >= 5: # skirt with full hose          
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs", 
                                        "You lift her skirt a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her lightly covered thighs",
                                        "You slide a hand up her inner thigh, to just below her . . ."])
                                $ TempFocus += 2 if P_Focus < 40 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 40 else 0                                
                                $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 0                            
                    elif newgirl["Laura"].Legs == "skirt" and newgirl["Laura"].Hose: #skirt with stockings         
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs", 
                                        "You lift her skirt a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose"])
                                $ TempFocus += 2 if P_Focus < 50 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 50 else 0                               
                                $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 0                            
                    elif newgirl["Laura"].Legs == "skirt":  #and no hose
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs", 
                                        "You lift her skirt a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just her skirt"])
                                $ TempFocus += 2 if P_Focus < 50 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 50 else 0                               
                                $ newgirl["Laura"].Addict -= 2 if D20S > 10 else 1                                
                    elif HoseNum("Laura") >= 5: # just hose
                                $ Line = renpy.random.choice(["You reach out and stroke her lightly covered thighs", 
                                        "You lift her leg a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, the smooth faberic creasing",
                                        "You slide a hand up her inner thigh, to just below her. . ."])
                                $ TempFocus += 2 if P_Focus < 40 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 40 else 0                               
                                $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 0
                    elif newgirl["Laura"].Hose: #just stockings
                                $ Line = renpy.random.choice(["You reach out and stroke her thighs", 
                                        "You lift her leg a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose",
                                        "You slide a hand up her inner thigh, to just below her. . ."])
                                $ TempFocus += 2 if P_Focus < 50 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 50 else 0                               
                                $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 0
                    else: #nude legs
                                $ Line = renpy.random.choice(["You reach out and stroke her thighs", 
                                        "You lift her leg a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her. . ."])
                                $ TempFocus += 2 if P_Focus < 50 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 50 else 0                               
                                $ newgirl["Laura"].Addict -= 2 if D20S > 10 else 1
        
    # end R fondle thighs                               //////////////////////////////////////////////////////////////////////////////
     
     
    elif Trigger == "fondle pussy":
                    if Speed == 2 and D20S <= 10:
                            $ Line = renpy.random.choice(["You continue to finger Laura's pussy. ", 
                                                    "You continue to finger bang Laura's pussy. ",
                                                    "You continue to finger blast Laura's pussy. "])
                                            
                            if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                            $ Line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her pussy underneath", 
                                                    "You push her panties aside, and slide a finger between her lips", 
                                                    "You slide a finger into her pussy and stroke the top", 
                                                    "You pull her pants out a bit and she gasps as you slide two fingers between her lips", 
                                                    "You rub her clit with your palm as you dive into her pussy with your middle finger"]) 
                            elif newgirl["Laura"].Legs == "skirt":
                                    if newgirl["Laura"].Panties == "shorts" and not newgirl["Laura"].PantiesDown: #shorts on
                                            $ Line = renpy.random.choice(["You push her skirt and shorts up, and slide a finger between her lips", 
                                                    "You slide a finger into her pussy and stroke the top", 
                                                    "You lift her skirt a bit and she gasps as you pull her shorts up and slide two fingers between her lips", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                            $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide a finger between her lips", 
                                                    "You slide a finger into her pussy and stroke the top", 
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and slide two fingers between her lips", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                            $ Line = renpy.random.choice(["You push her skirt aside, and slide a finger between her lips", 
                                                    "You slide a finger into her pussy and stroke the top", 
                                                    "You lift her skirt a bit and she gasps as you slide two fingers between her lips", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"]) 
                                            $ TempFocus += 2 
                                            $ TempLust += 2                            
                            #no skirt or pants
                            elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                        $ Line = renpy.random.choice(["You push her panties aside, and slide a finger between her lips", 
                                                "You slide a finger into her pussy and stroke the top", 
                                                "You lift her panties a bit and she gasps as you slide two fingers between her lips"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and slide a finger between her lips", 
                                                "You slide a finger into her pussy and stroke the top", 
                                                "You lift her lips a bit and she gasps as you slide two fingers between them", 
                                                "You rub her clit with your thumb as you dive into her pussy with your middle finger"]) 
                                        $ TempFocus += 2 
                                        $ TempLust += 2
                                
                            $ TempFocus += 4 if P_Focus < 50 else 3  
                            $ TempLust += 6 if newgirl["Laura"].Lust > 40 else 3
                            $ newgirl["Laura"].Addict -= 2  
                                
                    else: #if not fingerblasting or not high rolls
                            $ Line = renpy.random.choice(["You continue to stroke Laura's pussy. ", 
                                                    "You continue to rub Laura's pussy. ",
                                                    "You continue to caress Laura's pussy. "])
                                            
                            if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                            $ Line = renpy.random.choice(["You reach out and brush your hands across her pussy through the jeans", 
                                                    "You slide a hand down her pants, and brush your hands across her pussy underneath", 
                                                    "You put your hand against her mound and grind against it", 
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the jeans",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                                
                            elif newgirl["Laura"].Legs == "skirt":
                                    if newgirl["Laura"].Panties == "shorts" and not newgirl["Laura"].PantiesDown: #shorts on
                                            $ Line = renpy.random.choice(["You reach under skirt and ran your hands over the thin shorts covering her", 
                                                    "You slide a hand up the leg of her shorts, and brush your hands across her pussy underneath", 
                                                    "You put your hand against her mound and grind against it", 
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"]) 
                                    elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                            $ Line = renpy.random.choice(["You reach under skirt and brush across her panties", 
                                                    "You lift her skirt a bit and grind against her panties", 
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and stroke her lips", 
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her",
                                                    "She gasps as you rub her pussy through her panties",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])  
                                    elif HoseNum("Laura") >= 5: #just hose
                                            $ Line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric", 
                                                    "You grab her hose and pull them taut, elliciting a small gasp",
                                                    "You put your hand against her mound and grind against it", 
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material", 
                                                    "Her legs twitch a bit as you press your thumb against her",
                                                    "She gasps as you reach under her hose and lightly stroke her ass",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    else: #skirt, but nothing else
                                            $ Line = renpy.random.choice(["You reach under skirt and brush across her bare lips", 
                                                    "You lift her skirt a bit and grind against her warm mound", 
                                                    "You lift her skirt a bit and she gasps as you stroke her moist lips", 
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her"
                                                    "She gasps as you rub her bare pussy",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                            if D20S <= 10:
                                                $ TempFocus += 3 if P_Focus < 50 else 1  
                                                $ TempLust += 4 if newgirl["Laura"].Lust > 40 else 2
                                                $ newgirl["Laura"].Addict -= 2  
                                            else: #If it touches skin
                                                $ TempFocus += 1 
                                                $ TempLust += 1
                            
                            #no skirt or pants
                            elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her panties", 
                                                "You grab her panties and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material", 
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her panties and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif HoseNum("Laura") >= 5: #just hose
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric", 
                                                "You grab her hose and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material", 
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her hose and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her bare lips", 
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips", 
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                        if D20S <= 10:
                                            $ TempFocus += 3 if P_Focus < 50 else 1  
                                            $ TempLust += 4 if newgirl["Laura"].Lust > 40 else 2
                                            $ newgirl["Laura"].Addict -= 2  
                                        else: #If it touches skin
                                            $ TempFocus += 1 
                                            $ TempLust += 1
                                
                            if D20S > 10:#If it touches skin
                                $ TempFocus += 3 if P_Focus < 50 else 1  
                                $ TempLust += 4 if newgirl["Laura"].Lust > 40 else 2
                                $ newgirl["Laura"].Addict -= 2  
                            else: 
                                $ TempFocus += 2 if P_Focus < 50 else 1  
                                $ TempLust += 2 if newgirl["Laura"].Lust > 40 else 1
                                
        
    # end R fondle pussy                               /////////////////////////////////////////////////////////////////////////////
    
    
    elif Trigger == "lick pussy":
                            $ Line = renpy.random.choice(["You continue to lick Laura's pussy. ", 
                                                    "You continue to suck Laura's pussy. ",
                                                    "You continue to tongue Laura's pussy. "])
                                            
                            if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                            $ Line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her, even through the thick material",
                                                    "She gasps as you press on her clit through the thick fabric",
                                                    "You rub her clit with your nose as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the surface of her jeans", 
                                                    "With a little nibble, you tug at the denim", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"]) 
                                            $ TempFocus += 1 if P_Focus < 70 else 0  
                                            $ TempLust += 3 if newgirl["Laura"].Lust > 60 else 2
                            else:                    
                                if newgirl["Laura"].Legs == "skirt":
                                        if newgirl["Laura"].Panties == "shorts" and not newgirl["Laura"].PantiesDown: #shorts on
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her shorts",                 
                                                        "You bend down and lick the edges of her lips through the shorts",                 
                                                        "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin shorts", 
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her panties",                 
                                                        "You bend down and stroke the edges of her panties with your tongue",                 
                                                        "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin panties", 
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        elif HoseNum("Laura") >= 5: #just hose
                                               $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her hose",                 
                                                        "You bend down and stroke the edges of her lips through the hose",                 
                                                        "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin hose", 
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        else: #skirt, but nothing else
                                                $ Line = renpy.random.choice(["You push her skirt aside and stroke her lips with your tongue", 
                                                        "You slide your tongue into her pussy and flick the roof with deft strokes", 
                                                        "You spread the lips back and she gasps as you slide your tongue between them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick around her lips", 
                                                        "With a little nibble, you tug on her lower lips",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])            
                                                if D20S <= 10:
                                                    $ TempFocus += 3 if P_Focus < 70 else 1  
                                                    $ TempLust += 4 if newgirl["Laura"].Lust > 60 else 2
                                                    $ newgirl["Laura"].Addict -= 3  
                                                else: #If it touches skin
                                                    $ TempFocus += 1 
                                                    $ TempLust += 1
                                
                                #no skirt or pants
                                elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",                 
                                                    "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin panties", 
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                elif HoseNum("Laura") >= 5: #just hose
                                           $ Line = renpy.random.choice(["You bend down and stroke her lips with your tongue",                 
                                                    "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin hose", 
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                else: #nothing
                                            $ Line = renpy.random.choice(["You bend down and stroke her lips with your tongue", 
                                                    "You slide your tongue into her pussy and flick the roof with deft strokes", 
                                                    "You spread the lips back and she gasps as you slide your tongue between them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick around her lips", 
                                                    "With a little nibble, you tug on her lower lips",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                            if D20S <= 10: 
                                                $ TempFocus += 3 if P_Focus < 70 else 1  
                                                $ TempLust += 4 if newgirl["Laura"].Lust > 60 else 2
                                                $ newgirl["Laura"].Addict -= 3  
                                            else: #If it touches skin
                                                $ TempFocus += 1 
                                                $ TempLust += 1
                                    
                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 4 if P_Focus < 70 else 1  
                                    $ TempLust += 10 if newgirl["Laura"].Lust > 60 else 5
                                    $ newgirl["Laura"].Addict -= 3  
                                else: 
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 5 if newgirl["Laura"].Lust > 60 else 3
                                
    # end R lick pussy                               /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "fondle ass":                  
                        $ Line = renpy.random.choice(["You continue to fondle Laura's ass. ", 
                                                "You continue to feel up Laura's ass. ",
                                                "You continue to grope Laura's ass. "])
                                        
                        if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across the back of her jeans", 
                                                "You slide a hand down her pants, and firmly cup her ass", 
                                                "You put your hand against her rear and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the jeans",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])  
                                            
                        elif newgirl["Laura"].Legs == "skirt":
                                if newgirl["Laura"].Panties == "shorts" and not newgirl["Laura"].PantiesDown: #shorts on
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her shorts", 
                                                "You lift her skirt a bit and grind against her shorts", 
                                                "You lift her skirt a bit and she gasps as you pull her shorts aside and stroke across her butt", 
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her shorts",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her panties", 
                                                "You lift her skirt a bit and grind against her panties", 
                                                "You lift her skirt a bit and she gasps as you pull her panties aside and stroke across her butt", 
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her panties",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                elif HoseNum("Laura") >= 5: #just hose
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her hose", 
                                                "You lift her skirt a bit and grind against her hose", 
                                                "You lift her skirt a bit and she gasps as you pull her hose aside and stroke across her butt", 
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her hose",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                else: #skirt, but nothing else
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her bare ass", 
                                                "You lift her skirt a bit and grind against her warm cheeks", 
                                                "You lift her skirt a bit and she gasps as you stroke asshole", 
                                                "Her legs twitch a bit beneath her skirt as you press your thumb against her firm rear",
                                                "She gasps as you rub her bare hole",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"]) 
                                        if D20S <= 10:
                                            $ TempFocus += 2 if P_Focus < 50 else 1  
                                            $ TempLust += 3 if newgirl["Laura"].Lust > 40 else 2
                                            $ newgirl["Laura"].Addict -= 1  
                                        else: #If it touches skin
                                            $ TempFocus += 1 
                                            $ TempLust += 1
                        
                        #no skirt or pants
                        elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: # panties   
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks", 
                                            "You grab her panties and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material", 
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her panties and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])  
                        elif HoseNum("Laura") >= 5: #just hose
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks", 
                                            "You grab her hose and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material", 
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her hose and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])  
                        else: #nothing
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her bare ass", 
                                            "You put your hand against her firm rear and grind against it", 
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole", 
                                            "Her legs twitch a bit as you press your thumb against her",
                                            "She gasps as you reach under her and lightly stroke her ass",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                    if D20S <= 10:
                                        $ TempFocus += 2 if P_Focus < 50 else 1  
                                        $ TempLust += 3 if newgirl["Laura"].Lust > 40 else 2
                                        $ newgirl["Laura"].Addict -= 1  
                                    else: #If it touches skin
                                        $ TempFocus += 1 
                                        $ TempLust += 1
                            
                        if D20S > 10:#If it touches skin
                            $ TempFocus += 2 if P_Focus < 50 else 1  
                            $ TempLust += 3 if newgirl["Laura"].Lust > 40 else 2
                            $ newgirl["Laura"].Addict -= 1  
                        else: 
                            $ TempFocus += 2 if P_Focus < 50 else 1  
                            $ TempLust += 2 if newgirl["Laura"].Lust > 40 else 1
                                
    # end R fondle ass                               /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "insert ass":
                            $ Line = renpy.random.choice(["You continue to finger Laura's asshole. ", 
                                                    "You continue to finger bang Laura's asshole. ",
                                                    "You continue to finger Laura's rim. "])
                                            
                            if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                            $ Line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her anus", 
                                                    "You push her panties aside, and slide a finger between her cheeks", 
                                                    "You slide a finger into her tight anus", 
                                                    "You pull her pants out a bit and she gasps as you slide a finger up her hole", 
                                                    "You gasps as you rub her asshole with your fingers"]) 
                            elif newgirl["Laura"].Legs == "skirt":
                                    if newgirl["Laura"].Panties == "shorts" and not newgirl["Laura"].PantiesDown: #shorts on
                                            $ Line = renpy.random.choice(["You push her skirt and shorts up, and slide a finger into her anus", 
                                                    "You slide a finger into her tight anus", 
                                                    "You lift her skirt a bit and she gasps as you pull her shorts up and slide a finger into her anus", 
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
                                    elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                           $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide a finger into her anus", 
                                                    "You slide a finger into her tight anus", 
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and slide a finger into her anus", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                             $ Line = renpy.random.choice(["You push her skirt aside, and slide a finger into her anus", 
                                                    "You slide a finger into her tight anus", 
                                                    "You lift her skirt a bit and she gasps as you slide a finger into her anus", 
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"]) 
                            #no skirt or pants
                            elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                        $ Line = renpy.random.choice(["You push her panties aside, and slide a finger into her anus", 
                                                "You slide a finger into her tight anus", 
                                                "You lift her panties a bit and she gasps as you and slide a finger into her anus"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and slide a finger into her anus", 
                                                "You slide a finger into her tight anus", 
                                                "You lift her lips a bit and she gasps as you  slide a finger into her anus",  
                                                "You rub her pussy with your thumb as you dive into her anus with your middle finger"]) 
                                                                
                            $ TempFocus += 2 if P_Focus < 50 else 1  
                            $ TempLust += 6 if newgirl["Laura"].Lust > 70 else 3
                                    
                            $ newgirl["Laura"].Addict -= 2  
                                        
    # end R insert ass                              /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "lick ass":
                            $ Line = renpy.random.choice(["You continue to lick Laura's ass. ", 
                                                    "You continue to suck Laura's ass. ",
                                                    "You continue to tongue Laura's ass. "])
                                            
                            if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                                $ Line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her anus, even through the thick material",
                                                        "She gasps as you press on her asshole through the thick fabric",
                                                        "You put your hand against her mound and lick the surface of her jeans", 
                                                        "With a little nibble, you tug at the denim"])  
                                                $ TempFocus += 1 if P_Focus < 70 else 0  
                                                $ TempLust += 1 if newgirl["Laura"].Lust < 60 else 0
                            else:                    
                                if newgirl["Laura"].Legs == "skirt":
                                        if newgirl["Laura"].Panties == "shorts" and not newgirl["Laura"].PantiesDown: #shorts on
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her shorts",                 
                                                        "You bend down and stroke the edges of her shorts with your tongue",                 
                                                        "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it", 
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])  
                                        elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her panties",                 
                                                        "You bend down and stroke the edges of her panties with your tongue",                 
                                                        "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it", 
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])  
                                        elif HoseNum("Laura") >= 5: #just hose
                                               $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her hose",                 
                                                        "You bend down and stroke the edges of her hose with your tongue",                 
                                                        "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it", 
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])  
                                        else: #skirt
                                                $ Line = renpy.random.choice(["You push her skirt aside and stroke her asshole with your tongue", 
                                                        "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her asshole",
                                                        "She gasps as you suck on her anus",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "You put your hand against her mound and lick around her rim", 
                                                        "You slowly lick into her gap and she gasps as you press the rim apart"])         
                                                if D20S <= 10:
                                                    $ TempFocus += 2 if P_Focus < 70 else 0  
                                                    $ TempLust += 3 if newgirl["Laura"].Lust > 60 else 1
                                                    $ newgirl["Laura"].Addict -= 3  
                                                else: #If it touches skin
                                                    $ TempFocus += 1 
                                                    $ TempLust += 1
                                
                                #no skirt or pants
                                elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown: #Just panties
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",                 
                                                    "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"]) 
                                elif HoseNum("Laura") >= 5: #just hose
                                           $ Line = renpy.random.choice(["You bend down and stroke the edges of her hose with your tongue",                 
                                                    "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"]) 
                                else: #nothing
                                            $ Line = renpy.random.choice(["You bend down and stroke her rim with your tongue", 
                                                    "You slide your tongue into her asshole and flick the roof with deft strokes", 
                                                    "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her rim",
                                                    "She gasps as you suck on her hole",
                                                    "You rub her clit with your thumb as you dive into her asshole with your tongue",
                                                    "You knead her cheeks and lick around her rim", 
                                                    "With a little nibble, you toss her salad",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])  
                                            if D20S <= 10: 
                                                $ TempFocus += 2 if P_Focus < 70 else 0  
                                                $ TempLust += 3 if newgirl["Laura"].Lust > 60 else 1
                                                $ newgirl["Laura"].Addict -= 3  
                                            else: #If it touches skin
                                                $ TempFocus += 1 
                                                $ TempLust += 1
                                    
                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 3 if P_Focus < 70 else 0  
                                    $ TempLust += 9 if newgirl["Laura"].Lust > 60 else 4
                                    $ newgirl["Laura"].Addict -= 3  
                                else: 
                                    $ TempFocus += 1 if P_Focus < 50 else 0  
                                    $ TempLust += 4 if newgirl["Laura"].Lust > 60 else 2
                                                   
    # end R lick ass                               /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "dildo pussy":                            
                        if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her jeans", 
                                        "You slap the dildo lightly against her mound"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 1
                        elif HoseNum("Laura") >= 10:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her tights", 
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 1
                        elif HoseNum("Laura") >= 5:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her hose", 
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 1
                        else:
                                if newgirl["Laura"].Legs == "skirt" and newgirl["Laura"].Panties:            
                                    $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her pussy", 
                                            "You slide the toy deep into her pussy", 
                                            "She gasps as you rotate the dildo within her tight pussy",
                                            "You rub her clit with your thumb as you dive into her puss with the rubber phallus"])
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 8 if newgirl["Laura"].Lust > 70 else 5
                                elif newgirl["Laura"].Legs == "skirt":            
                                    $ Line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole", 
                                            "You slide the toy deep into her pussy",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight puss", 
                                            "She gasps as you rotate the dildo within her slit",
                                            "You rub her clit with your thumb as you dive into her pussy with the rubber phallus"])
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 8 if newgirl["Laura"].Lust > 70 else 5
                                elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown:            
                                    $ Line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight pussy", 
                                            "You slide the dildo into her moist slit and stroke it rapidly", 
                                            "You lift her panties a bit and she gasps as you slide the dildo between her lower lips", 
                                            "She gasps as you rub her tight pussy with the toy",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight slit through the thin material"])
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 8 if newgirl["Laura"].Lust > 70 else 5
                                else:            
                                    $ Line = renpy.random.choice(["You reach out and slide the dildo along her mound", 
                                            "You slide the toy into her pussy and stroke it slowly", 
                                            "You pull her lips apart and she gasps as you slide the dildo between them", 
                                            "You can feel her twitching as you press your thumb against her clit",
                                            "She gasps as you rub her clit with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her wet pussy"])            
                                    $ TempFocus += 3 if P_Focus < 50 else 1  
                                    $ TempLust += 10 if newgirl["Laura"].Lust > 70 else 8
    # end R dildo pussy                              /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "dildo anal":
                        if (newgirl["Laura"].Legs == "pants" or newgirl["Laura"].Legs == "mesh pants") and not newgirl["Laura"].Upskirt:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her jeans", 
                                        "You slap the dildo lightly against her ass"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 1
                        elif HoseNum("Laura") >= 10:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her tights", 
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 1
                        elif HoseNum("Laura") >= 5:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her hose", 
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 1
                        else:
                                if newgirl["Laura"].Legs == "skirt" and newgirl["Laura"].Panties:            
                                    $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her ass", 
                                            "You slide the toy deep into her ass", 
                                            "She gasps as you rotate the dildo within her tight asshole",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 9 if newgirl["Laura"].Lust > 70 else 6
                                elif newgirl["Laura"].Legs == "skirt":            
                                    $ Line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole", 
                                            "You slide the toy deep into her ass",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight anus", 
                                            "She gasps as you rotate the dildo within her ass",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 9 if newgirl["Laura"].Lust > 70 else 6
                                elif newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown:            
                                    $ Line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight ass", 
                                            "You slide the dildo into her ass and stroke it rapidly", 
                                            "You lift her panties a bit and she gasps as you slide the dildo between her cheeks", 
                                            "She gasps as you rub her tight asshole with the toy",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight anus through the thin material"])
                                    $ TempFocus += 2 if P_Focus < 50 else 1  
                                    $ TempLust += 8 if newgirl["Laura"].Lust > 70 else 6
                                else:            
                                    $ Line = renpy.random.choice(["You reach out and slide the dildo between her cheeks", 
                                            "You slide the toy into her asshole and stroke it against the sides", 
                                            "You pull her cheeks apart and she gasps as you slide the dildo between them", 
                                            "You can feel her twitching as you press your thumb against her anus",
                                            "She gasps as you rub her anus with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her firm anus"])            
                                    $ TempFocus += 3 if P_Focus < 50 else 1  
                                    $ TempLust += 11 if newgirl["Laura"].Lust > 70 else 7
    # end R dildo ass                              /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "masturbation":
                call Laura_Self_Lines  
                if "unseen" not in newgirl["Laura"].RecentActions:
                    if Trigger2 == "jackin" or "cockout" in P_RecentActions:
                            $ TempLust += 2
                
    # end R Masturbation                               /////////////////////////////////////////////////////////////////////////////
    elif Trigger == "lesbian":
                call Laura_SexDialog_Threeway("lesbian")      
    
    elif Trigger == "foot":
                        $ Line = "Laura continues stroke your cock with her feet. "
                           
                        if not Speed:
                                    if newgirl["Laura"].Foot > 2:
                                            $ Line = Line + "She just seems to be enjoying the feel of it"
                                            $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
                                    else:
                                            $ Line = Line + "She just seems to be looking it over"
                                            $ TempLust += 2 if newgirl["Laura"].Lust < 40 else 0
                                            $ TempFocus += -3 if P_Focus > 50 else 2
                                        
                                    $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 2
                                    return
                        
                        if newgirl["Laura"].Foot > 4:                          # After the 5th time 
                                    if Speed <= 1:                      #slow 
                                        $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])   
                                        
                                        $ TempFocus += 20 if P_Focus > 70 else 5
                                              
                                    else:                               #fast
                                        $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching", 
                                                "Her expert strokes will have you boiling over in seconds",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"]) 
                                        
                                        $ TempFocus += 20 if P_Focus < 40 else 5        
                                
                        elif newgirl["Laura"].Foot >= 3:                       #third through 5th time
                                    if Speed <= 1:                      #slow
                                        $ Line = Line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft", 
                                                "She's still learning, but learning fast", 
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She gently caresses the shaft, and brushes the balls in her other foot, giving them a light massage"])  
                                        
                                        $ TempFocus += 15 if P_Focus > 60 else 5
                                        
                                    else:                               #fast
                                        $ Line = Line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft", 
                                                "She's still learning, but learning fast", 
                                                "Her feet glide smoothly across your cock",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She quickly strokes your cock, with a very deft pressure"]) 
                                        
                                        $ TempFocus += 15 if P_Focus < 60 else 7         
                            
                        else:                                   #First and second time
                                if Speed <= 1:                      #slow
                                    $ Line = Line + renpy.random.choice(["Kitty makes up for her inexperience with determination, carefully stroking your cock", 
                                            "She moves her feet up and down the shaft. She's a little rough at this, but at least she tries", 
                                            "She strokes you gently. She isn't quite sure what to do with the balls",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This may take a few tries"])     
                                    
                                    $ TempFocus += 10 if P_Focus > 60 else 5         
                                else:                               #fast 
                                    $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips between her feet", 
                                            "She rapidly moves her feet up and down the shaft. She's a little rough at this, but at least she tries", 
                                            "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This train is out of control"])  
                                    
                                    $ TempFocus += 8 if P_Focus > 60 else 2         
                                
                        $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
                        $ TempLust += 3 if newgirl["Laura"].Foot > 2 else 0
                        $ newgirl["Laura"].Addict -= 1
            
    #End Footy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "kiss you":  
                        $ newgirl["Laura"].Addict -= 3 
                        if newgirl["Laura"].Kissed > 10 and newgirl["Laura"].Love >= 700:#Loving
                                $ Line = renpy.random.choice(["She hungrily presses her lips against yours", 
                                        "Her lips part as you hold her close",    
                                        "You nibble her neck as she groans in pleasure",
                                        "You squeeze her tightly as your tongues jostle",
                                        "Her tongue dances around yours",
                                        "She nibbles your ear as her hands slide across your back",
                                        "Your hands slide down her body as your lips press hers"])
                                $ TempFocus += 1 if P_Focus < 50 else 0  
                                $ TempFocus += 1 if P_Focus < 90 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 0
                                $ TempLust += 1 if newgirl["Laura"].Lust < 90 else 0
                        elif newgirl["Laura"].Kissed > 5:#reasonably experienced        
                                $ Line = renpy.random.choice(["She confidently presses her lips against yours", 
                                        "You softly kiss her plump lips", 
                                        "Her lips part as you hold her close",    
                                        "You nibble her neck as she coos in pleasure",
                                        "You squeeze her tightly as your lips connect",
                                        "Her tongue flickers out to meet yours",
                                        "Your hands slide down her body as your lips brush hers"])
                                $ TempFocus += 1 if P_Focus < 70 else 0  
                                $ TempLust += 3 if newgirl["Laura"].Lust < 50 else 0
                                $ TempLust += 1 if newgirl["Laura"].Lust < 90 else 0
                        else:#basic kissing
                                $ Line = renpy.random.choice(["She tentatively presses her lips against yours", 
                                        "You softly kiss her plump lips", 
                                        "Her lips part slightly as you hold her close",
                                        "You squeeze her tightly as your lips connect",
                                        "Your hands slide down her body as your lips brush hers"]) 
                                $ TempFocus += 1 if P_Focus < 70 else 0  
                                $ TempLust += 2 if newgirl["Laura"].Lust < 30 else 0
                                $ TempLust += 1 if newgirl["Laura"].Lust < 70 else 0
                                
    # end R kissing                              /////////////////////////////////////////////////////////////////////////////
    else: #no Trigger was set, somehow
        "No trigger was set, or it was '[Trigger]'. Please tell Oni what happend up to this point."
        $ Line = "Huh."
       
    $ Line = Line + "."                        
    # Wrap-up
    $ PrimaryLust += TempLust
    $ SecondaryLust += TempLust2 + 2
        
    return
    
    
#end Laura_SexDialog Trigger1 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////













#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label Laura_Self_Lines(Mode = "T3", Action = Trigger3, TempLustX = 0): 
    # The Mode can be T3 for Trigger 3 for a masturbation option, or T5/Trigger5 if it's setting a Threeway action. 
    # call Laura_Self_Lines("T5",Trigger5) 
    # This sets a Action if there isn't one, or sets an intitial line
    $ Line = 0
    if not Action or D20S >= 15: 
            if Trigger != "masturbation" and "passive" in newgirl["Laura"].Traits:
                    # This bypasses self-set if Laura is told not to take initiative
                    $ Line = 0
                    return            
            call Laura_Self_Set(Mode, Action)
            
            if Mode == "T3": #Sets Action based on the result
                    $ Action = Trigger3
            else: #if Mode == "T5"
                    $ Action = Trigger5  
            if not Action: 
                    return
            elif Action == "hand" and not Line: 
                    $ Line = "Also, Laura continues stroke your cock. "
            elif not Line:        
                    $ Line = "Also, Laura continues to masturbate. "      
    elif Action == "hand": 
            $ Line = "Laura continues stroke your cock. "
    else:        
            $ Line = renpy.random.choice(["Laura continues to masturbate. ", 
                    "Laura's hands move across her body. ",
                    "Laura continues to feel herself. ",
                    "Laura can't keep still. "]) 
            
    if Action == "hand": 
            $ Line = Line + renpy.random.choice(["She lightly strokes the shaft, fingers sliding along the vein", 
                    "She grasps the shaft firmly, and slowly slides along its length", 
                    "She's becoming something of a handjob expert, making up for years of lost time",
                    "Her expert strokes will have you boiling over in seconds",
                    "She strokes the shaft vigorously, lightly touching the tip",
                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                    "Her hand slides slowly down your shaft"]) 
            $ TempFocus += 10 if P_Focus > 60 else 4
            $ TempFocus += 2 if newgirl["Laura"].Hand > 2 else 0
                    
            $ TempLustX += 2 if newgirl["Laura"].Lust < 60 else 1
            $ TempLustX += 2 if newgirl["Laura"].Hand > 2 else 0
            $ newgirl["Laura"].Addict -= 1            
    else:
        if newgirl["Laura"].Lust >= 80:   
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
                            "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                            "She  spreads her lower lips and runs the device along the inner lining",
                            "She presses the toy deep into her and the vibrations send a shock through her body"])
            else: # Action == "fondle breasts"
                    $ Line = Line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                            "Her hands squeeze at her breasts, massaging them firmly with both hands",                 
                            "She hungrily cups her breasts and moves them in rapid circles",
                            "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                            "She firmly pinches her nipples and gives them steady tugs",
                            "She passionately rubs her breasts, desperately tugging at her nipples"])     
            #End newgirl["Laura"].Lust >= 80
            
                
        elif newgirl["Laura"].Lust >= 50:   
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her mound, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly across her delta, occasionally grazing her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides a finger up and down the crease of her pussy", 
                                "She lets out a gasp as her fingers brush against her erect clit"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",  
                                "She traces the rubber phallus slowly down her body, barely grazing her mound",  
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",                
                                "She gently slides the phallus up and down the crease of her pussy", 
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her ass, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly along her crack, occasionally grazing her asshole",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the tight hole within",
                                "She gently slides a finger up and down the crease of ass", 
                                "She lets out a gasp as her fingers brush against her puckered hole"]) 
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
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
                #End newgirl["Laura"].Lust >= 50
                
        else: #if newgirl["Laura"].Lust < 50:      
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely grazing her mound", 
                                "Her fingers move lightly across her pubic region, subtly avoiding her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "Her hands move along her sides, carefully caressing them"])  
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her mound",                 
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely passing smoothly across her hips", 
                                "Her fingers move lightly across her crack, subtly avoiding her rosebud",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "Her hands move along her sides, carefully caressing them"])              
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])   
                #End newgirl["Laura"].Lust 0-60
        #End Laura Action masturbation dialog        
                        
            
        # Laura Self-stat boosts  
        $ TempLustX += 4 if newgirl["Laura"].Lust > 80 else 0        
        $ TempLustX += 5 if newgirl["Laura"].Lust < 40 else 3                   #Bonus if she is relatively low lust
        $ TempLustX += 5 if Trigger == "masturbation" else 0     #Bonus if masturbation is her primary action
        
        if Partner != "Laura": #If this is a primary, Trigger3 action
            $ TempLust = TempLustX
        else: #If this is a Secondary, Trigger5 action
            $ TempLust2 = TempLustX
        
        $ TempFocus += 3         
        $ TempFocus += 1 if P_Focus < 50 else 0 
        
    #End Laura Action all dialog     
    
    return
# end Laura_Self_Lines / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Laura_Self_Set / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Self_Set(Mode = "T3", Action = Trigger3, Length=0, Count2=0, Options =[]): 
    #If T3/Trigger3 is sent, this is for Laura's Primary role, offhand behavior
    #If T5/Trigger5 is sent, this is for Laura's Second role, threesome behavior
    if Mode == "T3" and Trigger != "masturbation":
            # This cuts it out if she's submissive or not horny enough to get busy
            if "sub" in newgirl["Laura"].Traits:
                return
            #if she's inexperienced or shy, skip this
            if Taboo and newgirl["Laura"].SEXP >= 50 and ApprovalCheck("Laura", 500, "I"):
                if newgirl["Laura"].Lust <= 50:
                    return
            elif newgirl["Laura"].SEXP >= 25 and ApprovalCheck("Laura", 300, "I"):
                if newgirl["Laura"].Lust <= 30:
                    return
            else:
                    return
    
    if Trigger == "masturbation":
                $ Options = ["fondle pussy", "fondle breasts", "fondle ass"]
                if "dildo" in newgirl["Laura"].Inventory:
                        $ Options.append("dildo pussy")  
                        $ Options.append("dildo anal")                  
                if "vibrator" in newgirl["Laura"].Inventory:            
                        $ Options.append("vibrator pussy") 
            
    else:
                if Mode != "T5" and Trigger in ("fondle pussy", "fondle breasts", "fondle thighs", "kiss you", "fondle ass", "suck breasts") and newgirl["Laura"].Hand >= 5:
                        $ Options.append("hand")
                    
                if Trigger not in ("sex", "fondle pussy", "lick pussy", "dildo pussy"):
                        if "dildo" in newgirl["Laura"].Inventory:
                            $ Options.append("dildo pussy")    
                        $ Options.append("fondle pussy") 
                
                if Trigger not in ("anal", "fondle ass", "insert ass", "lick ass", "dildo anal"):
                        if "dildo" in newgirl["Laura"].Inventory:
                            $ Options.append("dildo anal")
                        $ Options.append("fondle ass") 
                
                if "vibrator" in newgirl["Laura"].Inventory:
                        $ Options.append("vibrator pussy")
                
                if Trigger not in ("fondle breasts", "suck breasts"):
                        $ Options.append("fondle breasts") 
                    
                if "fondle pussy" not in Options and (newgirl["Laura"].Obed < newgirl["Laura"].Inbt):
                        $ Options.append("fondle pussy")
                    
                if "fondle ass" not in Options and (newgirl["Laura"].Obed < newgirl["Laura"].Inbt):
                        $ Options.append("fondle ass")
                    
                if "fondle breasts" not in Options and (newgirl["Laura"].Obed < newgirl["Laura"].Inbt):
                        $ Options.append("fondle breasts")
    # End filling options
    
    $ Length = len(Options)-1
    $ D20 = renpy.random.randint(1, 20)    
    if D20 >=18:
            $ Count2 = 0
    elif D20 >= 15:
            $ Count2 = 1
    elif D20 >= 12:
            $ Count2 = 2
    elif D20 >= 10:
            $ Count2 = 3
    else:        
            $ Count2 = renpy.random.randint(0, Length)
            
    $ Count2 = Length if Count2 > Length else Count2
    if Action != Options[Count2]: #If the action remains the same as it was.
            $ Action = Options[Count2] #Sets Action to the selected Option
            if Action == "hand": 
                    $ Line = "Laura slides her hand down and firmly grabs your dick. "   
                    $ Approval = 3
            elif Action == "fondle pussy":
                    $ Line = "Laura's hand slides down and begins to stroke her pussy. "
            elif Action == "dildo pussy":
                    $ Line = "Laura pulls out her dildo and draws it toward her pussy. " 
            elif Action == "fondle ass":
                    $ Line = "Laura's hand slides behind her body, reaching toward her ass. " 
            elif Action == "dildo anal":
                    $ Line = "Laura pulls out her dildo and reaches it behind her. "
            elif Action == "vibrator pussy":
                    $ Line = "Laura pulls out her vibrator and strokes it across her body. "      
            else: # Action == "fondle breasts"
                    $ Line = "Laura's hands slide up her body and begin to kneed her breasts. "
    elif Action == "hand": 
            $ Line = "Also, Laura continues stroke your cock. "
    else:        
            $ Line = "Also, Laura continues to masturbate. "
            
    if Mode == "T3": #Sets Action based on the result
        $ Trigger3 = Action
    else:
        $ Trigger5 = Action                            
            
    return

# end Laura self-set / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Laura Threeway Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_SexDialog_Threeway(Mode = 0, Action = 0, ActiveGirl = Primary, TempLine = 0, TempLust = 0, TempLust2 = 0, TempFocus = 0):
    # This is the dialog checked for Trigger 4, activated when Laura is the second girl in a scene, or for Lesbian activities.
    # if Mode is "lesbian" then it means she's doing a girl/girl sequence, and activating secondary dialogs.
    # By default, ActiveGirl will be the primary and this sequence will build text for what the secondary girl does.
    # In "lesbian" mode, ActiveGirl will be the secondary girl, and this sequence will build text for what the primary will do to her.
    # Lesbian Trigger1 dialog calls "call Laura_SexDialog_Threeway("lesbian")"
    
    call Laura_Threeway_Set(Mode = Mode)   #Picks a new activty on a 7-9 roll or when not set, otherwise returns
    
    if Mode == "lesbian":
            $ Action = Trigger3
            $ ActiveGirl = Secondary  
    else:
            $ Action = Trigger4
            
    if Line:        
            #if it picked something, it should have set a line and returned
            return  
    elif not Action:
            $ Action = "watch"
            
    if Action == "hand":
                    if D20S <= 8 and (Trigger == "blow" or Trigger == "hand"): #This is a random bonus dialog
                        if Trigger == "blow": #If Kitty is blowing you                                    
                            $ Line = renpy.random.choice(["Laura's fingers brush against " + ActiveGirl + "'s lips as they work",
                                    "Laura and " + ActiveGirl + " pause for a second to briefly kiss", 
                                    "Laura takes a turn to suck on the head before passing it back",
                                    "Laura and " + ActiveGirl + " get into an alternating rhythm"]) 
                        elif Trigger == "hand":  #If Kitty is handying you
                            $ Line = renpy.random.choice(["Laura's fingers brush against " + ActiveGirl + "'s as they work",
                                    "Laura strokes " + ActiveGirl + "'s palm as she works", 
                                    "Laura takes a turn to stroke a few times before passing it back",
                                    "Laura and " + ActiveGirl + " get into an alternating rhythm"])   
                    else:                
                        if Trigger == "hand": #if another girl is also handy
                                $ Line = "Laura also continues to stroke your cock"
                        else: #if the other girl is doing something else
                                $ Line = "Laura continues stroke your cock" 
                                
                        $ Line = Line + renpy.random.choice([", lightly stroking the shaft, fingers sliding along the vein", 
                                ", grasping the shaft firmly, and slowly sliding along its length", 
                                ", making up for years of lost time",
                                ", her expert strokes will have you boiling over in seconds",
                                ", stroking the shaft vigorously, lightly touching the tip",
                                ", moving very smoothly, stroking casually",
                                ", hand sliding slowly down your shaft"]) 
                    $ TempFocus += 3 if P_Focus > 70 else 2
                          
                    $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
                    $ TempLust += 2 if newgirl["Laura"].Hand > 2 else 0
                    $ newgirl["Laura"].Addict -= 1 if D20S > 10 else 2
                    
    # end newgirl["Laura"].Hand Threeway                                //////////////////////////////////////////////////////////////////////////////
                             
    elif Action == "blow":
                    if Speed > 2 and Trigger == "blow":
                        $ Line = "Since " + ActiveGirl + " is working so hard, Laura settles for the occasional nibble or lick."
                        $ TempFocus += 5 if P_Focus > 60 else 3                      
                        $ TempLust += 2 if newgirl["Laura"].Lust > 80 else 1    
                    else:
                        if D20S <= 8 and (Trigger == "blow" or Trigger == "hand"): #This is a random bonus dialog
                            if Trigger == "blow": #If Kitty is blowing you
                                $ Line = renpy.random.choice(["Laura's tongue brushes against " + ActiveGirl + "'s as they work",
                                        "Laura and " + ActiveGirl + " pause for a second to briefly kiss", 
                                        "Laura takes a turn to suck on the head before passing it back",
                                        "Laura and " + ActiveGirl + " get into an alternating rhythm"]) 
                            elif Trigger == "hand": #If Kitty is handying you
                                $ Line = renpy.random.choice(["Laura's tongue brushes against " + ActiveGirl + "'s hand as they work",
                                        "Laura licks " + ActiveGirl + "'s palm as she works", 
                                        "Laura takes a turn to stroke a few times before passing it back",
                                        "Laura and " + ActiveGirl + " get into an alternating rhythm"])  
                            $ TempLust2 += 1 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 0                
                        else:
                            if Trigger == "blow": #if another girl is also blowing
                                    $ Line = "Laura also continues to lick your cock"
                            else: #if the other girl is doing something else
                                    $ Line = "Also, Laura continues lick your cock"     
                            
                            $ Line = Line + renpy.random.choice([", settling into a gentle licking pace along the base",
                                    ", licking gently up and down the shaft", 
                                    ", her tongue moves carefully along the shaft",
                                    ", really starting to learn some clever tricks to making you feel good",
                                    ", licking her way down the shaft, and gently teasing the balls"]) 
                        
                        $ TempFocus += 20 if P_Focus > 60 else 10                      
                        $ TempLust += 2 if newgirl["Laura"].Lust > 80 else 1    
                              
                        $ newgirl["Laura"].Addict -= 2
    # end newgirl["Laura"].Blowjob Threeway                                //////////////////////////////////////////////////////////////////////////////
            
    elif Action == "fondle breasts":    
                        if Trigger2 == "fondle breasts" and Trigger != "lesbian": #if you're also fondling them,
                            $ Line = "Laura also continues to fondle " + ActiveGirl + "'s breasts" 
                        else:
                            $ Line = "Laura continues to fondle " + ActiveGirl + "'s breasts" 
                            
                        $ Line = Line + renpy.random.choice([", giving little tugs to her nipples", 
                                        ", cupping them firmly with both hands",                 
                                        ", gently moving them in slowly increasing circles",
                                        ", then moves her hands from her breasts to rub her neck",
                                        ", firmly pinching her nipples and giving them a tug",
                                        ", passing repeatedly against her rigid nipples"])  
                        $ TempLust += 2 if ApprovalCheck("Laura", 500, "I") else 1  # Laura's lust
                        $ TempLust2 += 5 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 2
                        $ TempFocus += 1 
    # end R Fondle breasts Threeway                                //////////////////////////////////////////////////////////////////////////////
    
    
    elif Action == "suck breasts":  
                        if Trigger2 == "fondle breasts" and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = "Laura also continues to suck " + ActiveGirl + "'s breasts" 
                        else:
                                $ Line = "Laura continues to suck " + ActiveGirl + "'s breasts" 
                            
                        $ Line = Line + renpy.random.choice([", giving little tugs to her nipple", 
                                        ", cupping them firmly with both hands",               
                                        ", then moves her hands down along her side",
                                        ", licking slowly up her chest",
                                        ", firmly nibbling her nipples and giving them a tug",
                                        ", nibbling repeatedly at her rigid nipples"])  
                        $ TempLust += 2 if ApprovalCheck("Laura", 500, "I") else 1  # Laura's lust
                        $ TempLust2 += 4 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 2
                        $ TempFocus += 1                      
    # end R Suck breasts Threeway                                //////////////////////////////////////////////////////////////////////////////
        
     
    elif Action == "fondle pussy":
                        if (Trigger == "fondle pussy" or Trigger2 == "fondle pussy") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = "Laura also continues to fondle " + ActiveGirl + "'s pussy" 
                                $ Templine = renpy.random.choice([", stroking across her clit",   
                                        ", the two of you taking turns in your motions",              
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing against it vigorously",
                                        ", stroking into it vigorously",
                                        ", pressing firmly into it",
                                        ", sliding firmly into it",
                                        ", moving inside it with slow undulating motions",
                                        ", moving with slow undulating motions"])  
                        else:    
                                $ Line = "Laura continues to fondle " + ActiveGirl + "'s pussy" 
                                $ Templine = renpy.random.choice([", running fingers gently up her cleft", 
                                        ", stroking across her clit",                 
                                        ", taking a little taste of the warm juices on her finger",
                                        ", rubbing against it vigorously",
                                        "a",
                                        "b",
                                        "c",
                                        ", moving with slow undulating motions"])  
                            
                                #a, b, and c can change depending on other circumstances at the time. 
                                if Templine == "a":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brush against your cock as it goes in" 
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", your tongue slides past her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brush against the dildo as it goes in" 
                                    else:
                                            $ Templine = ", stroking into it vigorously"
                                elif Templine == "b":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brushing up against your balls as you sink in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", you briefly suck on one of her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ Templine = ", sliding firmly into it"
                                elif Templine == "c":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brush against your cock as it goes in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", your tongue slides along her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ Templine = ", moving inside it with slow undulating motions"
                                #End if the other girl is not fondling
                        $ Line = Line + Templine
                            
                        $ TempLust += 2 if ApprovalCheck("Laura", 500, "I") else 1  # Laura's lust
                        $ TempLust2 += 5 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 3
                        $ TempFocus += 1  
        
    # end R fondle pussy Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    
    elif Action == "lick pussy":
                        if (Trigger == "lick pussy" or Trigger2 == "lick  pussy") and Trigger != "lesbian": #if you're also fondling them,
                            $ Line = "Laura also continues to lick " + ActiveGirl + "'s pussy" 
                        else:    
                            $ Line = "Laura continues to lick " + ActiveGirl + "'s pussy" 
                            
                        $ Templine = renpy.random.choice([", running her tongue gently up her cleft", 
                                    ", stroking across her clit",                 
                                    ", taking a little taste of the warm juices flowing out",
                                    ", lapping against it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])  
                        
                        #a, b, and c can change depending on other circumstances at the time. 
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in" 
                                elif Trigger == "lick pussy":
                                        $ Templine = ", her tongue brushing against yours as you work"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides along your fingers" 
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue brushes along the dildo as it goes in" 
                                else:
                                        $ Templine = ", lapping into it vigorously"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her longue lapping against your balls as you sink in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", you briefly kiss as you take turns"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides past your fingers" 
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"
                           
                        $ Line = Line + Templine
                                                    
                        $ TempLust += 3 if ApprovalCheck("Laura", 600, "I") else 1  # Laura's lust
                        $ TempLust2 += 7 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 4
                        $ TempFocus += 3  
        
    # end R lick pussy Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "fondle ass":
                        if Trigger2 == "fondle ass" and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = "Laura also continues to fondle " + ActiveGirl + "'s ass" 
                                $ Line = Line + renpy.random.choice([", stroking across her rear",   
                                        ", the two of you taking turns in your motions",              
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])  
                        else:
                                $ Line = "Laura continues to fondle " + ActiveGirl + "'s ass" 
                                $ Line = Line + renpy.random.choice([", running fingers gently up her cleft", 
                                        ", stroking across her rear",                 
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"]) 
                                                    
                        $ TempLust += 1 if ApprovalCheck("Laura", 500, "I") else 0  # Laura's lust
                        $ TempLust2 += 3 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 1
                        $ TempFocus += 1  
    # end R fondle ass Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    
    elif Action == "insert ass":
                        if (Trigger == "insert ass" or Trigger2 == "insert ass") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = "Laura also continues to stroke " + ActiveGirl + "'s ass" 
                        else:    
                                $ Line = "Laura continues to stroke " + ActiveGirl + "'s ass" 
                            
                        $ Templine = renpy.random.choice([", stroking across her rim",  
                                    ", stroking across her hole",                 
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])  
                        
                        #a, b, and c can change depending on other circumstances at the time. 
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brush against your cock as it goes in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her fingers circling yours" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers brush against the dildo as it goes in" 
                                else:
                                        $ Templine = ", running fingers gently up her cleft"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brushing up against your balls as you sink in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", the two of you taking turns in your motions"     
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers run along the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brush against your cock as it goes in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her fingers intertwine yours" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers brush against the dildo as it goes in" 
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"
                           
                        $ Line = Line + Templine
                        
                        if ActiveGirl == "Kitty" and not K_Loose:
                                        $ TempLust2 -= 3
                        $ TempLust += 2 if ApprovalCheck("Laura", 700, "I") else 1  # Laura's lust
                        $ TempLust2 += 5 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 3
                        $ TempFocus += 1  
        
    # end R insert ass Threeway                             /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "lick ass":
                        if (Trigger == "lick ass" or Trigger2 == "lick ass") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = "Laura also continues to lick " + ActiveGirl + "'s ass" 
                        else:    
                                $ Line = "Laura continues to lick " + ActiveGirl + "'s ass" 
                            
                        $ Templine = renpy.random.choice([", tonguing across her rim", 
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])  
                        
                        #a, b, and c can change depending on other circumstances at the time. 
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in" 
                                elif Trigger == "lick ass":
                                        $ Templine = ", her tongue brushing against yours as you work"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides along your fingers" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue brushes along the dildo as it goes in" 
                                else:
                                        $ Templine = ", lapping into it vigorously"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her longue lapping against your balls as you sink in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", you briefly kiss as you take turns"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides past your fingers" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"
                           
                        $ Line = Line + Templine 
                            
                        $ TempLust += 3 if ApprovalCheck("Laura", 800, "I") else 1  # Laura's lust
                        $ TempLust2 += 4 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 2
                        $ TempFocus += 3  
        
    # end R lick ass Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "masturbation":            
                        call Laura_Self_Lines("T5",Trigger5)  
                        $ TempLust = 0
                
    # end R Masturbation Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action in ("kiss you", "kiss girl", "kiss both"):
                        if Trigger == "blow" and newgirl["Laura"].Blow > 5 and Trigger4 == "kiss girl":
                                    $ Line = "Laura also continues to kiss " + ActiveGirl
                                    $ Line = Line + renpy.random.choice([", occasionally taking a lick of your cock as well", 
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", taking the occasional lick down your shaft",
                                            ", nudging her aside to kiss the head of your cock"])
                        elif Trigger == "blow" and Trigger4 == "kiss girl":
                                    $ Line = "Laura also continues to kiss " + ActiveGirl
                                    $ Line = Line + renpy.random.choice([", occasionally bumping into your cock as well", 
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", trailing kisses down her neck"])
                        else: #they're just kissing
                                    if Action == "kiss girl" or Mode == "lesbian":
                                        if Trigger == "lesbian" and Partner != "Laura":
                                                $ Line = "Laura continues to make out with " + ActiveGirl
                                        else:                                            
                                                $ Line = "Laura also continues to make out with " + ActiveGirl
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air", 
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])
                                    elif Action == "kiss you":
                                        $ Line = "Laura also continues to make out with you" 
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air", 
                                                ", licking along your cheek",
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", occasionally nibbling at your ears",
                                                ", trailing kisses down your neck"])
                                    else: #Action == "kiss both":
                                        $ Line = "Laura also continues to make out with both of you"
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air", 
                                                ", licking along your cheek",
                                                ", occasionally nibbling your lip as well", 
                                                ", nudging you aside to get a deep kiss in",
                                                ", all three of your tongues swirling",
                                                ", nudging her aside to give you a deep kiss"
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])
                        
                        $ TempLust += 1 if ApprovalCheck("Laura", 500, "I") else 0  # Laura's lust
                        $ TempLust += 1 if GirlLikeCheck("Laura",ActiveGirl) >= 800 else 0
                        $ TempLust2 += 2 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 1 
                        $ TempFocus += 1  
    # end R Kissing Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "watch":
                        $ Line = "Laura continues to watch the two of you" 
                        $ Line = Line + renpy.random.choice([", shifting uncomfortably", 
                                        ", readjusting her clothes",                 
                                        ", glancing at the door",               
                                        ", taking in " + ActiveGirl + "'s body",
                                        ", transfixed by the action"]) 
                            
                        $ TempLust += 1 if GirlLikeCheck("Laura",ActiveGirl) >= 600 else 0  # Laura's lust
                        $ TempLust += 2 if GirlLikeCheck("Laura",ActiveGirl) >= 800 else 1  # Laura's lust
                        $ TempLust2 += 1 if ApprovalCheck(ActiveGirl, 500, "I") else 0
                        $ TempLust2 += 1 if ApprovalCheck(ActiveGirl, 700, "I") else 0                        
                        $ TempFocus += 1  
    # end R watching Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    else:
        "Nothing triggered. 1:[Trigger], 2:[Trigger2], 3:[Trigger3], 4:[Trigger4], 5:[Trigger5]" #diagnostic
    
    # Wrap-up
    $ TempLust2 += 2
    if Mode == "lesbian":        
            $ PrimaryLust += (TempLust * 3)
            $ SecondaryLust += (TempLust2 * 3)
    else:
            $ SecondaryLust += TempLust
            $ PrimaryLust += TempLust2
        
    $ P_Focus += TempFocus
    return
    
    
#end Laura_SexDialog_Threeway //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Start Laura Threeway-set ////////////////////////////////////////////////////////////////////////

label Laura_Threeway_Set(Preset = 0, Mode = 0, Action = Trigger4, ActiveGirl = Primary, State = "watcher", TempLust = 0, TempLust2 = 0, TempFocus = 0):
            # Action defaults to Trigger4, the action of the seondary girl and ActiveGirl to the lead girl in the scene
            # In lesbian mode, Action becomes Trigger3, the secondary action of the primary girl, and ActiveGirl is the secondary girl
            # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
            # for Lesbian: Laura_Threeway_Set("activity", "lesbian", Trigger3, "Laura")
            # for Threeway: Laura_Threeway_Set("activity", 0, Trigger4, "Other girl")
            # ThreeCount is a value that gets set to a few digits lower then the current Round
            # The girl will not arbitrarily change motions until after this value has been passed.
            
            $ D20 = renpy.random.randint(1, 20)
            if not Preset: 
                    #if no preset is offered
                    if Mode == "lesbian": 
                            #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                            
                            if Trigger3 == "kiss girl" and newgirl["Laura"].Lust <= 20 and newgirl["Laura"].Org < 1:
                                    # If kissing at low lust, keep doing it
                                    return
                            elif Trigger3 and ThreeCount <= Round:
                                    # If a Trigger3 is already set and it's under the count, return
                                    return
                    elif Trigger4 and D20 < 15 and Trigger4 != "watch": 
                            #If there is a trigger, it's not set to "watch," and the roll is good, continue
                            return
                    elif Trigger4 and ThreeCount <= Round:
                            # if there's not a Preset, and it's only been X turns since the last change, return.
                            return
            $ Options = ["watch", "masturbation", "masturbation", "masturbation"]
                        
            if Trigger == "lesbian":
                    $ State = "lesbian"
                    if Secondary != "Laura":
                            $ ActiveGirl = Secondary
                    $ Options = ["kiss girl","kiss girl"]        
                    if Preset in ("hand","blow","kiss you","kiss both"):
                            #if you send it presets that you want the other girl to touch you. . .
                            $ State = "threeway"   
                    elif Preset:
                            pass
                    elif GirlLikeCheck("Laura",ActiveGirl) >= 600 and ApprovalCheck("Laura", 500, "I"):
                            pass
                    else:
                            #this returns if she doesn't like the other girl enough to do anything more.
                            if Action != "kiss girl":                                
                                    $ Line = "Laura gives " + ActiveGirl + " a passionate kiss"
                                    $ Action = "kiss girl" 
                                    $ Trigger3 = "kiss girl" 
                                    if "lesbian" not in newgirl["Laura"].RecentActions:
                                            $ newgirl["Laura"].Les += 1
                                            $ newgirl["Laura"].RecentActions.append("lesbian")    
                            return
                        
            elif not ApprovalCheck("Laura", 500, "I"): # If Laura is too timid to do anything
                    pass            
            elif GirlLikeCheck("Laura",ActiveGirl) >= 600 and ApprovalCheck("Laura", (1500-(10*newgirl["Laura"].Les)-(10*(GirlLikeCheck("Laura",ActiveGirl)-60)))): 
                    #If she likes both of you a lot, threeway
                    $ State = "threeway"
            elif ApprovalCheck("Laura", 1000): 
                    #If she likes you well enough, Hetero
                    $ State = "hetero"            
            elif GirlLikeCheck("Laura",ActiveGirl) >= 700: 
                    #if she doesn't like you but likes the other girl, lesbian
                    $ State = "lesbian"
                    
            if State == "lesbian" or State == "threeway":  
                $ Options.extend(("fondle breasts","suck breasts","fondle pussy","fondle ass","kiss girl")) 
                
                if ApprovalCheck("Laura", 800, "I") or GirlLikeCheck("Laura",ActiveGirl) >= 800:
                    $ Options.append("lick pussy")
                if ApprovalCheck("Laura", 900, "I") and GirlLikeCheck("Laura",ActiveGirl) >= 900:
                    $ Options.append("lick ass") 
#                if "dildo" in newgirl["Laura"].Inventory: #add later once these systems are done
#                    $ Options.append("dildo pussy") 
#                    if newgirl["Laura"].Loose:
#                        $ Options.append("dildo ass") 
#                if "vibrator" in newgirl["Laura"].Inventory:
#                    $ Options.append("vibrator") 
                    
            if State == "hetero" or State == "threeway":
                    $ Options.extend(("hand","blow","kiss you"))                 
            $ renpy.random.shuffle(Options)
            
            if Preset:
                if Preset in Options:
                        #if the suggested action is in the possible actions. . .
                        $ Options[0] = Preset 
                        ch_l "Ok, that seems legit. . ."
                elif ApprovalCheck("Laura", 750, "I") or ApprovalCheck("Laura", 1500):
                        #if the suggestion is not in the options, but she's game anyway
                        $ Options[0] = Preset 
                        ch_l "Worth a shot. . ."  
                else:
                        ch_l "Nah, not my style. . ."
                    
            #Sets opening lines. . .
            if Options[0] == Action:                          
                    #If it's the same result, just hop back
                    return
            elif Mode == "lesbian":
                    $ Line = "Laura shifts her position"
            elif not Trigger4 or Trigger4 == "masturbation":    
                    #If this is the first action,
                    $ Line = "Laura moves closer"            
            else:                                              
                    #If this is a new action
                    $ Line = "Laura shifts her position"
                    
                    
            if Options[0] == "masturbation":
                        $ Action = "masturbation"  
                        call Laura_Self_Lines("T5",Trigger5)
            elif Options[0] == "hand":
                        call Seen_First_Peen(1)
                        $ Line = Line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "hand"   
                        show Laura zorder newgirl["Laura"].GirlLayer:
                                ease 1 ypos 200 
                        $ Approval = 4
                        
                        $ TempFocus += 3 if P_Focus > 70 else 2                              
                        $ TempLust += 2 if newgirl["Laura"].Lust < 60 else 0
                        $ TempLust += 2 if newgirl["Laura"].Hand > 2 else 0
                        $ newgirl["Laura"].Addict -= 1 if D20 > 10 else 2
            elif Options[0] == "blow":
                        call Seen_First_Peen(1)
                        $ Line = Line + " before she slides down and begins to slowly lick your cock"
                        show Laura zorder newgirl["Laura"].GirlLayer:
                                ease 1 ypos 200 
                        $ Action = "blow"     
                        $ Approval = 4
                        
                        $ TempFocus += 20 if P_Focus > 60 else 10                      
                        $ TempLust += 2 if newgirl["Laura"].Lust > 80 else 1  
                        $ newgirl["Laura"].Addict -= 2
            #the above three do not apply to lesbian actions.
                        
            elif Options[0] == "fondle breasts":
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slides her hands along " + ActiveGirl + "'s breasts" 
                        $ Action = "fondle breasts"   
                        if "lesbian" not in newgirl["Laura"].RecentActions:
                                $ newgirl["Laura"].Les += 1
                                $ newgirl["Laura"].RecentActions.append("lesbian") 
                        $ TempLust += 2 if ApprovalCheck("Laura", 500, "I") else 1  # Laura's lust
                        $ TempLust2 += 4 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 2
                        $ TempFocus += 1 
            elif Options[0] == "suck breasts":
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slurps " + ActiveGirl + "'s nipple into her mouth" 
                        $ Action = "suck breasts"    
                        if "lesbian" not in newgirl["Laura"].RecentActions:
                                $ newgirl["Laura"].Les += 1
                                $ newgirl["Laura"].RecentActions.append("lesbian") 
                        $ TempLust += 2 if ApprovalCheck("Laura", 500, "I") else 1  # Laura's lust
                        $ TempLust2 += 5 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 2
                        $ TempFocus += 1  
            elif Options[0] == "fondle pussy":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her finger along " + ActiveGirl + "'s pussy" 
                        $ Action = "fondle pussy"  
                        if "lesbian" not in newgirl["Laura"].RecentActions:
                                $ newgirl["Laura"].Les += 1
                                $ newgirl["Laura"].RecentActions.append("lesbian")                  
                        $ TempLust += 2 if ApprovalCheck("Laura", 500, "I") else 1  # Laura's lust
                        $ TempLust2 += 5 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 3
                        $ TempFocus += 2  
            elif Options[0] == "lick pussy":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her tongue along " + ActiveGirl + "'s pussy" 
                        $ Action = "lick pussy"  
                        if "lesbian" not in newgirl["Laura"].RecentActions:
                                $ newgirl["Laura"].Les += 1
                                $ newgirl["Laura"].RecentActions.append("lesbian") 
                        $ TempLust += 3 if ApprovalCheck("Laura", 600, "I") else 1  # Laura's lust
                        $ TempLust2 += 8 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 5
                        $ TempFocus += 3  
            elif Options[0] == "fondle ass": 
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and gives " + ActiveGirl + "'s ass a firm squeeze" 
                        $ Action = "fondle ass" 
                        if "lesbian" not in newgirl["Laura"].RecentActions:
                                $ newgirl["Laura"].Les += 1
                                $ newgirl["Laura"].RecentActions.append("lesbian")                
                        $ TempLust += 1 if ApprovalCheck("Laura", 400, "I") else 0  # Laura's lust
                        $ TempLust2 += 3 if GirlLikeCheck(ActiveGirl,"Laura") >= 600 else 2
                        $ TempFocus += 1  
            elif Options[0] == "lick ass":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and starts to lick around " + ActiveGirl + "'s ass" 
                        $ Action = "lick ass"  
                        if "lesbian" not in newgirl["Laura"].RecentActions:
                                $ newgirl["Laura"].Les += 1
                                $ newgirl["Laura"].RecentActions.append("lesbian") 
                        $ TempLust += 3 if ApprovalCheck("Laura", 800, "I") else 1  # Laura's lust
                        $ TempLust2 += 6 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 4
                        $ TempFocus += 2  
                        
            elif Options[0] == "kiss girl" or Mode == "lesbian":                               
                        $ Line = Line + " and gives " + ActiveGirl + " a passionate kiss"
                        $ Action = "kiss girl"
                        if Mode != "lesbian" and "kiss you" in Options:
                                if Trigger == "kiss you":
                                        $ Action = "kiss both"                        
                                elif Trigger3 == "kiss you":
                                        $ Action = "kiss both"           
                                elif Trigger4 == "kiss you":
                                        $ Action = "kiss both" 
                        $ TempFocus += 1  
            elif Options[0] == "kiss you":   
                        $ Line = Line + " and gives you a passionate kiss"
                        $ Action = "kiss you"  
                        if "kiss girl" in Options: 
                                if Trigger == "kiss you":
                                        $ Action = "kiss both"                         
                                elif Trigger3 == "kiss you":
                                        $ Action = "kiss both"           
                                elif Trigger4 == "kiss you":
                                        $ Action = "kiss both" 
                        $ TempLust += 1 
                        $ TempFocus += 1 
                        
#            elif Options[0] == "dildo pussy":  
#            elif Options[0] == "dildo ass":        
#            elif Options[0] == "vibrator":    

            else:
                        $ Line = "Laura is just watching the two of you intensely"
                        $ Action = "watch"
                        $ TempLust += 1 if GirlLikeCheck("Laura",ActiveGirl) >= 600 else 0  # Laura's lust
                        $ TempLust += 2 if GirlLikeCheck("Laura",ActiveGirl) >= 800 else 1  # Laura's lust
                        $ TempLust2 += 1 if ApprovalCheck(ActiveGirl, 500, "I") else 0
                        $ TempLust2 += 1 if ApprovalCheck(ActiveGirl, 700, "I") else 0
                        $ TempFocus += 1 
            
            if Action == "kiss girl" or Action == "kiss both":
                    #If there's a semi-lesbian make-out. . .
                    if "lesbian" not in newgirl["Laura"].RecentActions:
                            $ newgirl["Laura"].Les += 1
                            $ newgirl["Laura"].RecentActions.append("lesbian")           
                    $ TempLust += 1 if ApprovalCheck("Laura", 500, "I") else 0  # Laura's lust
                    $ TempLust += 1 if GirlLikeCheck("Laura",ActiveGirl) >= 800 else 0
                    $ TempLust2 += 2 if GirlLikeCheck(ActiveGirl,"Laura") >= 800 else 1
                    $ TempFocus += 1 
                                
            # Wrap-up
            if Preset:
                    $ ThreeCount = Round - 2
            else: 
                    #this sets a delay before the values change again on their own
                    $ ThreeCount = Round - 1
            $ TempLust2 += 2       
            if Mode == "lesbian":
                #Sets Primary Girl's secondary action
                $ Trigger3 = Action                
                $ PrimaryLust += (TempLust * 3)
                $ SecondaryLust += (TempLust2 * 3)
            elif Mode == "start":                
                #Sets Laura's action and Lust if this is a starting action
                $ Trigger4 = Action
                $ newgirl["Laura"].Lust += TempLust2
            else:
                #Sets Secondary girl's action
                $ Trigger4 = Action
                $ SecondaryLust += TempLust
                $ PrimaryLust += TempLust2
            $ P_Focus += TempFocus

            return

# end Laura Threeway-set ////////////////////////////////////////////////////////////////////////