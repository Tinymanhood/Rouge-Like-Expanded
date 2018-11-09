# Mystique Sprite Transformations

image Mystique_Sprite:
    ConditionSwitch(          
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_Sprite",
    "newgirl['Mystique'].LooksLike == 'Raven'", "Mystique_Raven_Sprite",
    "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sprite",
    "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sprite",
    "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sprite",
    "True", "Mystique_Blue_Sprite",
    ),

# Mystique Handjob Transformations

image Mystique_HJ_Animation:
    ConditionSwitch(          
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_HJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Raven'", "Mystique_Blue_HJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_HJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_HJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_HJ_Animation",
    "True", "Mystique_Blue_HJ_Animation",
    ),

# Mystique Blowjob Transformations

image Mystique_BJ_Animation:
    ConditionSwitch(          
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_BJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Raven'", "Mystique_Raven_BJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_BJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_BJ_Animation",
    "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_BJ_Animation",
    "True", "Mystique_Blue_BJ_Animation",
    ),


# Emma Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Emma_Sprite:
    LiveComposite(
        (402,965), 
        (0,0), ConditionSwitch(       
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_HairbackWet_Red.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_HairbackWet_White.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_HairBlackbackWet.png",
            "E_Hair == 'wet' or newgirl['Mystique'].Water", "images/EmmaSprite/EmmaSprite_HairbackWet.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Hairback_Red.png",   
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Hairback_White.png",   
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_HairBlackback.png",   
            "E_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(                                                                         #legs 
            "newgirl['Mystique'].Girl_Arms == 2", "images/EmmaSprite/EmmaSprite_Legs_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Legs_Arms1.png", #if E_Arms == 1         
            ),     
        (0,0), ConditionSwitch(                                                                         #pubes 
            "newgirl['Mystique'].Pubes", "images/EmmaSprite/EmmaSprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(                                                                         #Water effect 
            "newgirl['Mystique'].Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(                                                                         #Personal Wetness            
            "not newgirl['Mystique'].Wet", Null(),
            "newgirl['Mystique'].Wet == 2", "images/EmmaSprite/EmmaSprite_Wet2.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet1.png",
            ),     
        (0,0), ConditionSwitch(                                                                         #pussy spunk 
            "'pussy' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Pussy.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(                                                                         #arms 
            "newgirl['Mystique'].Girl_Arms == 2", "images/EmmaSprite/EmmaSprite_Arms2.png",         # one hand up
            "True", "images/EmmaSprite/EmmaSprite_Arms1.png", #if E_Arms == 1   # Crossed        
            ),  
        (0,0), ConditionSwitch(                                                                         #Water effect 
            "not newgirl['Mystique'].Water", Null(),             
            "newgirl['Mystique'].Girl_Arms == 2", "images/EmmaSprite/EmmaSprite_Water_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms1.png", #if E_Arms == 1      
            ), 
        (0,0), ConditionSwitch(                                                                         #tits
            "newgirl['Mystique'].Girl_Arms == 1", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
            "True", "images/EmmaSprite/EmmaSprite_TitsDown.png",   # E_TitsUp = 0
            ), 
        (0,0), ConditionSwitch(                                                                         #Water effect 
            "not newgirl['Mystique'].Water", Null(),             
            "newgirl['Mystique'].Girl_Arms == 1", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",  
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png", #if E_Arms == 1      
            ), 
        (55,0), "Mystique_EmmaSprite_Head",                                                                           #Head
        (0,0), ConditionSwitch(                                                                         #hand spunk 
            "newgirl['Mystique'].Girl_Arms != 2 or 'hand' not in newgirl['Mystique'].Spunk", Null(),  
            "'mouth' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Spunk_HandM.png",  
            "True", "images/EmmaSprite/EmmaSprite_Spunk_Hand.png",   
            ), 
        (0,0), ConditionSwitch(                                                                         #belly spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/EmmaSprite/Emma_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #UI tool for When Emma is masturbating using Trigger3 actions
            "newgirl['Mystique'].Loc == 'bg teacher'", Null(),
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_ESelf",            
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_E",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_E", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeBothBreast_E",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_E",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_E",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_E",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_E",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_E",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "newgirl['Mystique'].Loc == 'bg teacher'", Null(),
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Mystique'", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_E",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_E",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_E",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "newgirl['Mystique'].Loc == 'bg teacher'", Null(),
            "not Trigger or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_E",
            "Trigger == 'fondle thighs'", "GropeThigh_E",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_E",
            "Trigger == 'suck breasts'", "LickRightBreast_E",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_E",
            "Trigger == 'fondle pussy'", "GropePussy_E",
            "Trigger == 'lick pussy'", "Lickpussy_E",
            "Trigger == 'vibrator pussy'", "VibratorPussy_E",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_E",
            "Trigger == 'vibrator anal'", "VibratorAnal_E",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_E",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "newgirl['Mystique'].Loc == 'bg teacher'", Null(),
            "not Trigger2 or Ch_Focus != 'Mystique'", Null(),
            "not Trigger2 and not Trigger4 and Trigger == 'fondle breasts'", "GropeRightBreast_E",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_E",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeRightBreast_E",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_E",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_E",        
            "Trigger2 == 'fondle pussy'", "GropePussy_E",
            "Trigger2 == 'lick pussy'", "Lickpussy_E",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_E",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_E",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_E",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_E",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_E",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "newgirl['Mystique'].Loc == 'bg teacher'", Null(),
            "not Trigger4 or Ch_Focus != 'Mystique'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_E",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_E",            
            "Trigger4 == 'lick pussy'", "Lickpussy_E",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_E", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_E",  
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_E",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_E", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_E", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast_E",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(             
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Emma is secondary)
            "newgirl['Mystique'].Loc == 'bg teacher'", Null(),
            "not Trigger3 or Ch_Focus == 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_E",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_E",            
            "Trigger3 == 'lick pussy'", "Lickpussy_E",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_E", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_E",  
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_E",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_E", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_E", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_E",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),         
        )                
    anchor (0.6, 0.0)                
    zoom .75                

image Mystique_EmmaSprite_Head:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Blush or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Blush != 1 or E_Hair == 'wet' or E_Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Blush != 2 or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_Brows == 'normal'
            ),
        
         (0,0), ConditionSwitch(                                                                         #Face no blush wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Blush or (E_Hair != 'wet' and not newgirl['Mystique'].Water)", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Blush != 1 or (E_Hair != 'wet' and not newgirl['Mystique'].Water)", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Blush != 2 or (E_Hair != 'wet' and not newgirl['Mystique'].Water)", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_Brows == 'normal'
            ),
        
        (0,0), ConditionSwitch(                                                                         #Mouths        
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "newgirl['Mystique'].Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "newgirl['Mystique'].Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),   
        
        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "'mouth' not in newgirl['Mystique'].Spunk", Null(),
            "newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunnewgirl['Mystique'].MouthOpen.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunnewgirl['Mystique'].MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunnewgirl['Mystique'].Mouth.png",  
            ),  
        
        (0,0), "Mystique_Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            #"E_Brows == 'normal' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"E_Brows == 'normal' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "newgirl['Mystique'].Brows == 'normal' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            #"newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_White.png",
            #"newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_Red.png",
            "newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            #"newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_White.png",
            #"newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_Red.png",
            "newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            #"newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_White.png",        
            #"newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_Red.png",        
            "newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            #"newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_White.png",
            #"newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_Red.png",
            "newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            #"True and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"True and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "True and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "'facial' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "not E_Hair", Null(),
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairWet_White.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairWet_Red.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackWet.png",
            "E_Hair == 'wet' or newgirl['Mystique'].Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hair_White.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hair_Red.png",
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlack.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "not newgirl['Mystique'].Water", Null(),
            "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "'hair' in newgirl['Mystique'].Spunk and (E_Hair == 'wet' or E_Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5   

image Mystique_Emma Blink:
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
    "newgirl['Mystique'].Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'squint'", "Emma_Squint",
    "True", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png"
    .25
    repeat                

image Mystique_Emma_HJ_Animation:
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Emma_Hand_Under"), 
            "Speed == 1", At("Emma_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Under", Kitty_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Emma_Hand_Over"), 
            "Speed == 1", At("Emma_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Over", Kitty_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6

image Mystique_Emma_BJ_Animation:
    LiveComposite(    
        (787,913),             
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0", At("Mystique_Emma_BJ_HairBack", BJ_Starting()),                         
            "Speed == 1", At("Mystique_Emma_BJ_HairBack", BJ_Licking()),                         
            "Speed == 2", At("Mystique_Emma_BJ_HairBack", BJ_Heading()),                        
            "Speed == 3", At("Mystique_Emma_BJ_HairBack", BJ_Sucking()),
            "Speed == 4", At("Mystique_Emma_BJ_HairBack", BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # body, everything below the chin
            "Speed == 0", At("Mystique_Emma_BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("Mystique_Emma_BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("Mystique_Emma_BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("Mystique_Emma_BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("Mystique_Emma_BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # her head
            "Speed == 0", At("Mystique_Emma_BJ_Head_2", BJ_Starting()),                       
            #"Speed == 1", At("BJ_Head", BJ_Licking()),                       
            "Speed == 1", At("Mystique_Emma_BJ_Head_2", BJ_Licking()),                       
            "Speed == 2", At("Mystique_Emma_BJ_Head_2", BJ_Heading()),                     
            "Speed == 3", At("Mystique_Emma_BJ_Head_2", BJ_Sucking()),
            "Speed == 4", At("Mystique_Emma_BJ_Head_2", BJ_Deep()), 
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 # cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
         (0,0), ConditionSwitch(                                                                 # the masked overlay for when her head overlaps the cock
             "Speed < 3", Null(), 
             #"Speed == 2", At("Emma_BJ_Head_3", BJ_Heading()),
             "Speed == 3", At("Mystique_Emma_BJ_Head_3", BJ_Sucking()),
             "Speed == 4", At("Mystique_Emma_BJ_Head_3", BJ_Deep()), 
             #"Speed == 3", At(AlphaMask("Emma_BJ_Head_2", "Emma_BJ_Mask"), BJ_Sucking()),
             #"Speed == 4", At(AlphaMask("Emma_BJ_Head_2", "images/EmmaSprite/Emma_bj_facemask.png"), BJ_Deep()), 
             "True", Null(),
             ),    
         (0,0), ConditionSwitch(                                                                 # same as above, but for the heading animation
             #"Speed == 2", At("E_BJ_MaskHeadingComposite", BJ_Heading()),
             #"Speed == 2", At("Emma_BJ_Head_4", BJ_Heading()),
             "True", Null(),
             ),    
        )
    zoom .55
    anchor (.5,.5)
    
image Mystique_Emma_BJ_HairBack:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(       
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_Red.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_White.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackbackWet.png",
            "E_Hair == 'wet' or newgirl['Mystique'].Water", "images/EmmaSprite/EmmaSprite_Head_HairbackWet.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hairback_Red.png",   
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hairback_White.png",   
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackback.png",   
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hairback.png",   
            "True", Null(),        
            ),
        )
    anchor (0.6, 0.0)                
    zoom 2.025 
    offset (-240, -200)

image Mystique_Emma_BJ_Backdrop:
    "Mystique_Emma_Sprite"
    zoom 5.4
    pos (275,-110)
    offset (-465, -200) #-325, -125

image Mystique_Emma_BJ_Head_2:
    "Mystique_Emma_BJ_Head"
    #zoom .75
    zoom 4.05
    pos (275,-110)
    offset (-240, -200) #-140 - 125

image Mystique_Emma_BJ_Head_3:
    AlphaMask("Mystique_Emma_BJ_Head_2", "Emma_BJ_Mask")    #zoom .75
    #zoom 4.05
    pos (275,-110)
    offset (-240, -200) #-140 - 125

image Mystique_Emma_BJ_Head:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
            "newgirl['Mystique'].Blush or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
            "newgirl['Mystique'].Blush != 1 or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
            "newgirl['Mystique'].Blush != 2 or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #newgirl['Mystique'].Brows == 'normal'
            ),
        
         (0,0), ConditionSwitch(                                                                         #Face no blush wet
            "newgirl['Mystique'].Blush or (E_Hair != 'wet' and not newgirl['Mystique'].Water)", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #newgirl['Mystique'].Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
            "newgirl['Mystique'].Blush != 1 or (E_Hair != 'wet' and not newgirl['Mystique'].Water)", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #newgirl['Mystique'].Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
            "newgirl['Mystique'].Blush != 2 or (E_Hair != 'wet' and not newgirl['Mystique'].Water)", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #newgirl['Mystique'].Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            "Speed == 1 and Trigger == 'blow'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "Speed == 3 and Trigger == 'blow'", "images/EmmaSprite/Emma_bj_mouth.png", #sucking
            "Speed == 4 and Trigger == 'blow'", "images/EmmaSprite/Emma_bj_mouth.png", #deepthroat         
            "newgirl['Mystique'].Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "newgirl['Mystique'].Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
            "'mouth' not in newgirl['Mystique'].Spunk", Null(),
            "newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunnewgirl['Mystique'].MouthOpen.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunnewgirl['Mystique'].MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunnewgirl['Mystique'].Mouth.png",  
            ), 
        
        (0,0), "Mystique_Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            #"newgirl['Mystique'].Brows == 'normal' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"newgirl['Mystique'].Brows == 'normal' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "newgirl['Mystique'].Brows == 'normal' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            #"newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_White.png",
            #"newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_Red.png",
            "newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            #"newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_White.png",
            #"newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_Red.png",
            "newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            #"newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_White.png",        
            #"newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_Red.png",        
            "newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            #"newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_White.png",
            #"newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_Red.png",
            "newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            #"True and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"True and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "True and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not E_Hair", Null(),
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairWet_White.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairWet_Red.png",
            "(E_Hair == 'wet' or newgirl['Mystique'].Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackWet.png",
            "E_Hair == 'wet' or newgirl['Mystique'].Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hair_White.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hair_Red.png",
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlack.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "not newgirl['Mystique'].Water", Null(),
            "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in newgirl['Mystique'].Spunk and (E_Hair == 'wet' or newgirl['Mystique'].Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hands overlay
            "not P_Hands", Null(),
            "(newgirl['Mystique'].Water or E_Hair == 'wet') and P_Color == 'pink'", "images/EmmaSprite/Emma_Sprite_Wet_HeadHands_P.png",
            "(newgirl['Mystique'].Water or E_Hair == 'wet') and P_Color == 'green'", "images/EmmaSprite/Emma_Sprite_Wet_HeadHands_G.png",
            "(newgirl['Mystique'].Water or E_Hair == 'wet') and P_Color == 'brown'", "images/EmmaSprite/Emma_Sprite_Wet_HeadHands_B.png",
            "P_Color == 'pink'", "images/EmmaSprite/Emma_Sprite_HeadHands_P.png",
            "P_Color == 'green'", "images/EmmaSprite/Emma_Sprite_HeadHands_G.png",
            "P_Color == 'brown'", "images/EmmaSprite/Emma_Sprite_HeadHands_B.png",
            "True", Null(),
            ),   
        )                
    anchor (0.6, 0.0)                
    zoom .5 

# End Emma Section / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Rogue Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Rogue_Sprite:
    LiveComposite(
        (480,960),
        (0,0), ConditionSwitch(                                                                         #body 
            "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1body_bare.png",
            "R_Tan == 'tan'", "images/RogueSprite/Rogue_tbody_bare.png",
            "True", "images/RogueSprite/Rogue_body_bare.png",         
            ),  
        (0,0), ConditionSwitch(                                                                         #body 
            "newgirl['Mystique'].Pubes and R_HairColor == 'black'", "images/RogueSprite/Rogue_bodyhaired_pubesblack.png",
            "newgirl['Mystique'].Pubes and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_bodyhaired_pubesblonde.png",
            "newgirl['Mystique'].Pubes", "images/RogueSprite/Rogue_bodyhaired_pubes.png",   
            "True", Null(),         
            ),  
        (0,0), ConditionSwitch(                                                                         #body 
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_piercing_ring.png",            
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_piercing_barbell.png",
            "True", Null(),         
            ),   
        (0,0), ConditionSwitch(                                                                         #head 
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('Mystique_TJ_Animation')", Null(),
            "R_Tan and R_Hair == 'evo' and newgirl['Mystique'].Water", "images/RogueSprite/Rogue_thead_evowet.png",
            "R_Hair == 'evo' and newgirl['Mystique'].Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_Tan and R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2.png",
            "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_Tan and R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_thead_evo_blush.png",
            "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_Tan and R_Hair == 'evo'", "images/RogueSprite/Rogue_thead_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "R_Tan", "images/RogueSprite/Rogue_thead_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "R_Tan and newgirl['Mystique'].Girl_Arms == 1", "images/RogueSprite/Rogue_tarms1b_bare.png",                                                              #No gloves, no collar
            "newgirl['Mystique'].Girl_Arms == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "R_Tan", "images/RogueSprite/Rogue_tarms2b_bare.png",                                                                         #No gloves, no collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(                                                                         #chest layer
            "R_Tan == 'tan1' and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_t1chest_barbell.png",            
            "R_Tan == 'tan' and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_tchest_barbell.png",            
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            "R_Tan == 'tan1' and R_Pierce == 'ring'", "images/RogueSprite/Rogue_t1chest_rings.png",      
            "R_Tan == 'tan' and R_Pierce == 'ring'", "images/RogueSprite/Rogue_tchest_rings.png",      
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1chest_bare.png",     
            "R_Tan == 'tan'", "images/RogueSprite/Rogue_tchest_bare.png",     
            "True", "images/RogueSprite/Rogue_chest_bare.png",     
            ),   
        (0,0), ConditionSwitch(                                                                         #Personal Wetness            
            "not newgirl['Mystique'].Wet", Null(),
            "newgirl['Mystique'].Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
            ),              
        (0,0), ConditionSwitch(                                                                         #brows
            "newgirl['Mystique'].Brows == 'normal' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            "newgirl['Mystique'].Brows == 'angry' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            "newgirl['Mystique'].Brows == 'sad' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            "newgirl['Mystique'].Brows == 'surprised' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            "newgirl['Mystique'].Brows == 'confused' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/RogueSprite/Rogue_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/RogueSprite/Rogue_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/RogueSprite/Rogue_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/RogueSprite/Rogue_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/RogueSprite/Rogue_brows_confused.png",
            "True", "images/RogueSprite/Rogue_brows_normal.png",
            ),
        (0,0), ConditionSwitch(  
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",                                                                       #Mouths        
            "newgirl['Mystique'].Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                       #Mouths        
            "newgirl['Mystique'].Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                       #Mouths        
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue_w.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_tmouth_lipbite_w.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_mouth_lipbite_w.png",
            "newgirl['Mystique'].Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'lipbite'", "images/RogueSprite/Rogue_tmouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/RogueSprite/Rogue_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/RogueSprite/Rogue_mouth_grimace.png",           
            "True", "images/RogueSprite/Rogue_mouth_normal.png",
            ),            
        (0,0), "Mystique_Rogue Blink",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "newgirl['Mystique'].Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),                                                                           #Eyes
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "newgirl['Mystique'].Girl_Arms == 1", Null(),                                                              #No gloves, no collar
            "R_Tan", "images/RogueSprite/Rogue_tarms2b_bare_.png",                                                                         #No gloves, no collar
            "True", "images/RogueSprite/Rogue_arms2b_bare_.png",  
            ), 
                          
        (0,0), ConditionSwitch(                                                                         #water
            "newgirl['Mystique'].Water and newgirl['Mystique'].Girl_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "newgirl['Mystique'].Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         #soap
            "newgirl['Mystique'].Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('Mystique_TJ_Animation')", Null(),
            "R_Hair == 'evo' and newgirl['Mystique'].Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            "R_Hair == 'evo' and newgirl['Mystique'].Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            "R_Hair == 'evo' and newgirl['Mystique'].Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo.png",
            "True", Null(), 
            ),                           
        (0,0), ConditionSwitch(                                                                         #hand spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'hand' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Girl_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #face spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         #belly spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",  
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Mystique'", Null(), 
            #this doesn't activate unless Rogue is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                          
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy",
            "Trigger == 'fondle pussy'", "GropePussy",
            "Trigger == 'lick pussy'", "Lickpussy",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),                                              
            #When both triggers are the same, do nothing  
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",  
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy",
            "Trigger2 == 'lick pussy'", "Lickpussy",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Kitty's hand on her)
            "not Trigger4 or Ch_Focus != 'Mystique'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger4 == 'lick pussy'", "Lickpussy",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger4 == 'suck breasts'", "LickRightBreast",          
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Trigger3 or Ch_Focus == 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger3 == 'lick pussy'", "Lickpussy",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger3 == 'suck breasts'", "LickRightBreast",          
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",                 
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),            
        )                 
    anchor (0.6, 0.0)               
    zoom .75             
    
image Mystique_Rogue Blink:
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", "images/RogueSprite/Rogue_eyes_sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/RogueSprite/Rogue_eyes_side.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/RogueSprite/Rogue_eyes_surprised.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/RogueSprite/Rogue_eyes_normal.png",    
    "newgirl['Mystique'].Eyes == 'stunned'", "images/RogueSprite/Rogue_eyes_stunned.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/RogueSprite/Rogue_eyes_down.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/RogueSprite/Rogue_eyes_closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/RogueSprite/Rogue_eyes_manic.png",
    "newgirl['Mystique'].Eyes == 'squint'", "Rogue_Squint",
    "True", "images/RogueSprite/Rogue_eyes_normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueSprite/Rogue_eyes_closed.png"
    .25
    repeat                

image Mystique_Rogue_HJ_Animation:
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Rogue_Hand_Under"), 
            "Speed == 1", At("Rogue_Hand_Under", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Under", Rogue_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Rogue_Hand_Over"), 
            "Speed == 1", At("Rogue_Hand_Over", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Over", Rogue_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6

image Mystique_Rogue_BJ_Animation:
    LiveComposite(    
        (787,913),             
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0", At("Mystique_Rogue_BJ_HairBack", BJ_Starting()),                         
            "Speed == 1", At("Mystique_Rogue_BJ_HairBack", BJ_Licking()),                         
            "Speed == 2", At("Mystique_Rogue_BJ_HairBack", BJ_Heading()),                        
            "Speed == 3", At("Mystique_Rogue_BJ_HairBack", BJ_Sucking()),
            "Speed == 4", At("Mystique_Rogue_BJ_HairBack", BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # body, everything below the chin
            "Speed == 0", At("Mystique_Rogue_BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("Mystique_Rogue_BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("Mystique_Rogue_BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("Mystique_Rogue_BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("Mystique_Rogue_BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # her head
            "Speed == 0", At("Mystique_Rogue_BJ_Head", BJ_Starting()),                       
            "Speed == 1", At("Mystique_Rogue_BJ_Head", BJ_Licking()),                       
            "Speed == 2", At("Mystique_Rogue_BJ_Head", BJ_Heading()),                     
            "Speed == 3", At("Mystique_Rogue_BJ_Head", BJ_Sucking()),
            "Speed == 4", At("Mystique_Rogue_BJ_Head", BJ_Deep()), 
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 # cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("Mystique_Rogue_BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), BJ_Sucking()),
            "Speed == 4", At(AlphaMask("Mystique_Rogue_BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Mystique_Rogue_BJ_Head", "BJ_MaskHeadingComposite"), BJ_Heading()),
            "True", Null(),
            ),    
        )
    zoom .55
    anchor (.5,.5)
    
image Mystique_Rogue_BJ_HairBack:
    ConditionSwitch(                                                                            #Hair underlay
            "newgirl['Mystique'].Water and R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_back_wet.png",
            "newgirl['Mystique'].Water and R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_back_wet.png",
            "newgirl['Mystique'].Water and R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_back_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_back.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_back.png",
            "R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_back.png",
            "True", Null(),
            ),
    
image Mystique_Rogue_BJ_Backdrop:
    "Mystique_Rogue_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)
    
image Mystique_Rogue_BJ_Head:
    LiveComposite(    
        (787,913),     
        (0,0), ConditionSwitch(                                                                 #Hair back
            "newgirl['Mystique'].Water and R_Hair == 'evo' and R_HairColor == 'black'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlack_back_wet.png", "Mystique_Rogue_BJ_Backdrop"),
            "newgirl['Mystique'].Water and R_Hair == 'evo' and R_HairColor == 'blonde'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlonde_back_wet.png", "Mystique_Rogue_BJ_Backdrop"),
            "newgirl['Mystique'].Water and R_Hair == 'evo'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back_wet.png", "Mystique_Rogue_BJ_Backdrop"),
            "R_Hair == 'evo' and R_HairColor == 'black'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlack_back.png", "Mystique_Rogue_BJ_Backdrop"),
            "R_Hair == 'evo' and R_HairColor == 'blonde'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlonde_back.png", "Mystique_Rogue_BJ_Backdrop"),
            "R_Hair == 'evo'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back.png", "Mystique_Rogue_BJ_Backdrop"),
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                     
            "R_Tan and not Speed", "images/RogueBJFace/Rogue_tbj_face_base.png",    
            "not Speed", "images/RogueBJFace/Rogue_bj_face_base.png",    
            "R_Tan", "images/RogueBJFace/Rogue_tbj_face_base_s.png",
            "True", "images/RogueBJFace/Rogue_bj_face_base_s.png",
            ),   
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            "Speed == 1 and Trigger == 'blow' and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            "Speed == 1 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ring.png", #sucking
            "R_Tan and Speed == 2 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_tbj_mouth_licking_ring.png", #sucking
            "Speed == 2 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_licking_ring.png", #sucking
            "R_Tan and Speed == 3 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_tbj_mouth_sucking_ring.png", #sucking
            "Speed == 3 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_sucking_ring.png", #sucking
            "R_Tan and Speed == 4 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_tbj_mouth_sucking_ring.png", #deepthroat  
            "Speed == 4 and Trigger == 'blow' and newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_sucking_ring.png", #deepthroat  
            "newgirl['Mystique'].Gag == 'ringgag' and 'mouth' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            "newgirl['Mystique'].Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ring.png", 
            "Speed == 1 and Trigger == 'blow' and 'mouth' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "R_Tan and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png", #sucking
            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
            "R_Tan and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png", #deepthroat         
            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat         
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/RogueBJFace/Rogue_tbj_mouth_lipbiteS.png",              
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "R_Tan and 'mouth' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_tbj_mouth_lipbiteS.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
            "newgirl['Mystique'].Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            "R_Tan and newgirl['Mystique'].Mouth == 'lipbite'", "images/RogueBJFace/Rogue_tbj_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
            "newgirl['Mystique'].Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
            "newgirl['Mystique'].Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            ),       
        (316,590), ConditionSwitch(      #600               
            "Speed == 2 and not newgirl['Mystique'].Gag", At("BJ_MouthHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                                 #cum for under layer
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png",
            "not newgirl['Mystique'].Spunk or Trigger != 'blow' or 'mouth' not in newgirl['Mystique'].Spunk", Null(),
            "R_Tan and Speed == 3", "images/RogueBJFace/Rogue_tbj_face_under_sucking_cum.png",
            "Speed == 3", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
            "R_Tan and Speed == 4", "images/RogueBJFace/Rogue_tbj_face_under_sucking_cum.png",  
            "Speed == 4", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 #Brows
            "newgirl['Mystique'].Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "Mystique_Rogue_BJ Blink",                                                                #Eyes
        (0,0), ConditionSwitch(                                                                 #cum on the face
                "'facial' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png",
                "not newgirl['Mystique'].Spunk or Trigger != 'blow' or 'mouth' not in newgirl['Mystique'].Spunk", Null(),
                "Speed == 3", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "Speed == 4", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(                                                                                 #Collar
            "newgirl['Mystique'].Glasses", "images/RogueBJFace/Rogue_BJFace_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                 #Hair overlay
            "newgirl['Mystique'].Water and R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_wet.png",
            "newgirl['Mystique'].Water and R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_wet.png",
            "newgirl['Mystique'].Water and R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde.png",
            "R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hands overlay
            "not P_Hands", Null(),
            "(newgirl['Mystique'].Water or R_Hair == 'wet') and P_Color == 'pink'", "images/RogueBJFace/Rogue_bj_Wet_HeadHands_P.png",
            "(newgirl['Mystique'].Water or R_Hair == 'wet') and P_Color == 'green'", "images/RogueBJFace/Rogue_bj_Wet_HeadHands_G.png",
            "(newgirl['Mystique'].Water or R_Hair == 'wet') and P_Color == 'brown'", "images/RogueBJFace/Rogue_bj_Wet_HeadHands_B.png",
            "P_Color == 'pink'", "images/RogueBJFace/Rogue_bj_HeadHands_P.png",
            "P_Color == 'green'", "images/RogueBJFace/Rogue_bj_HeadHands_G.png",
            "P_Color == 'brown'", "images/RogueBJFace/Rogue_bj_HeadHands_B.png",
            "True", Null(),
            ), 
        )

image Mystique_Rogue_BJ Blink:
    ConditionSwitch(
        "newgirl['Mystique'].Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "newgirl['Mystique'].Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "newgirl['Mystique'].Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "newgirl['Mystique'].Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "newgirl['Mystique'].Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "newgirl['Mystique'].Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "newgirl['Mystique'].Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "newgirl['Mystique'].Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "newgirl['Mystique'].Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_squint.png",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    .25
    repeat

# End Rogue Section / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Kitty Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Kitty_Sprite:
    LiveComposite(
        (480,960),                                                                    
        (124,0), ConditionSwitch(
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "True", "Mystique_Kitty_HairBack",   
            ),         
        (0,0), ConditionSwitch(   
            "newgirl['Mystique'].Girl_Arms == 1 and K_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TArms1.png",
            "newgirl['Mystique'].Girl_Arms == 1 and K_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Arms1.png",
            "newgirl['Mystique'].Girl_Arms == 1 and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Arms1.png",
            "newgirl['Mystique'].Girl_Arms == 1", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                     #body
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TBody_Bare2.png",               
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Body_Bare2.png",
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",
            "newgirl['Mystique'].Girl_Arms == 2", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True and K_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TBody_Bare1.png",    
            "True and K_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Body_Bare1.png",
            "True and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Body_Bare1.png",
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",    
            ),
        (0,0), ConditionSwitch(                                                                         #body
            "newgirl['Mystique'].Pubes and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_Body_Hair_PubesBlack.png",               
            "newgirl['Mystique'].Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair_Pubes.png",               
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TBody_Bare2.png",               
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Body_Bare2.png",               
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",               
            "newgirl['Mystique'].Girl_Arms == 2", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True", Null(),  
            ),
        (0,0), ConditionSwitch(                                                                         #piercings bottom
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",   
            ),    
        (0,0), ConditionSwitch(                                                                         #wetness                    
            "newgirl['Mystique'].Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #Arms2               
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TArms2.png",
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Arms2.png",
            "newgirl['Mystique'].Girl_Arms == 2 and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Arms2.png",
            "newgirl['Mystique'].Girl_Arms == 2", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                         #chest
            "True and K_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_Tchest_bare.png",
            "True and K_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2chest_bare.png",
            "True and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3chest_bare.png",
            "True", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #piercings top
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",   
            ),    
        (0,0), ConditionSwitch(                                                                         #piercings over shirt
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",   
            ),    
        (0,0), ConditionSwitch(                                                                         #wet look
            "newgirl['Mystique'].Water and newgirl['Mystique'].Girl_Arms == 2", "images/KittySprite/Kitty_Sprite_Water2.png",
            "newgirl['Mystique'].Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),  
        (124,0), ConditionSwitch(
            "renpy.showing('Mystique_BJ_Animation')", Null(),
            "True", "Mystique_Kitty_Head",   
            ), 
        (0,0), ConditionSwitch(                                                                         #anal spunk
            "'anal' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                         #pussy spunk
            "'in' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                         #belly spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         #tits spunk
            "'tits' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
            #UI tool for When Kitty is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_K",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_K",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Mystique'", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_K",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_K",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_K",
            "Trigger == 'fondle thighs'", "GropeThigh_K",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_K",
            "Trigger == 'suck breasts'", "LickRightBreast_K",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_K",
            "Trigger == 'fondle pussy'", "GropePussy_K",
            "Trigger == 'lick pussy'", "Lickpussy_K",
            "Trigger == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger == 'vibrator anal'", "VibratorAnal_K",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Mystique'", Null(),
            "not Trigger2 and not Trigger4 and Trigger == 'fondle breasts'", "GropeRightBreast_K",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_K",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeRightBreast_K",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_K",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_K",        
            "Trigger2 == 'fondle pussy'", "GropePussy_K",
            "Trigger2 == 'lick pussy'", "Lickpussy_K",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_K",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_K",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_K",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_K",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_K",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != 'Mystique'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_K",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger4 == 'lick pussy'", "Lickpussy_K",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Kitty is secondary)
            "not Trigger3 or Ch_Focus == 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_K",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_K",            
            "Trigger3 == 'lick pussy'", "Lickpussy_K",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_K", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_K",  
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_K",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts' and (Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts')", "GirlGropeLeftBreast_K", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast_K",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),         
        )
    anchor (0.6, 0.0)
    zoom .75                      

image Mystique_Kitty_Head:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Water and K_Tan and newgirl['Mystique'].Blush == 1", "images/KittySprite/Kitty_Sprite_THead_Wet_Blush1.png",
            "newgirl['Mystique'].Water and newgirl['Mystique'].Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush1.png",
            "newgirl['Mystique'].Water and K_Tan and newgirl['Mystique'].Blush == 2", "images/KittySprite/Kitty_Sprite_THead_Wet_Blush2.png",
            "newgirl['Mystique'].Water and newgirl['Mystique'].Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush2.png",
            "newgirl['Mystique'].Water and K_Tan", "images/KittySprite/Kitty_Sprite_THead_Wet_Base.png",
            "newgirl['Mystique'].Water", "images/KittySprite/Kitty_Sprite_Head_Wet_Base.png",
            "newgirl['Mystique'].Blush == 1 and K_Tan", "images/KittySprite/Kitty_Sprite_THead_Evo_Blush1.png",
            "newgirl['Mystique'].Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush1.png",
            "newgirl['Mystique'].Blush == 2 and K_Tan", "images/KittySprite/Kitty_Sprite_THead_Evo_Blush2.png",
            "newgirl['Mystique'].Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush2.png",
            "True and K_Tan", "images/KittySprite/Kitty_Sprite_THead_Evo_Base.png",
            "True", "images/KittySprite/Kitty_Sprite_Head_Evo_Base.png",
            ),     
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "newgirl['Mystique'].Brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #"K_Gag", "images/KittySprite/Kitty_Sprite_Mouth_Ballgag.png",
            "newgirl['Mystique'].Mouth == 'normal' and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite' and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'kiss' and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Kiss.png",
            "newgirl['Mystique'].Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Mouth_Kiss.png",
            "newgirl['Mystique'].Mouth == 'sad' and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile' and K_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png", #fix add
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            ),      
        (0,0), ConditionSwitch(
            "'mouth' not in newgirl['Mystique'].Spunk", Null(),            
            "newgirl['Mystique'].Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "newgirl['Mystique'].Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Spunk_Kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Spunk_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Spunk_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Spunk_Surprised.png",
            "newgirl['Mystique'].Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Spunk_Tongue.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Spunk_Sucking.png", #fix add
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(
            "'facial' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),     
        (0,0), "Mystique_Kitty Blink",
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Blindfold", "images/KittySprite/Kitty_Sprite_Blindfold.png",  
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Water and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Wet.png",
            "newgirl['Mystique'].Water and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Wet.png",
            "newgirl['Mystique'].Water and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Wet.png",
            "newgirl['Mystique'].Water", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "K_Hair == 'evo' and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Evo.png",
            "K_Hair == 'evo' and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Evo.png",
            "K_Hair == 'evo' and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Evo.png",
            "K_Hair == 'evo'", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            "K_Hair == 'long' and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Long.png",
            "K_Hair == 'long' and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Long.png",
            "K_Hair == 'long' and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Long.png",
            "K_Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long.png",
            "K_Hair == 'wet' and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Wet.png",
            "K_Hair == 'wet' and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Wet.png",
            "K_Hair == 'wet' and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Wet.png",
            "K_Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "True and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Evo.png",
            "True and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Evo.png",
            "True and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Evo.png",
            "True", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            ),   
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Headband == 'pink'", "images/KittySprite/Kitty_Catband_Pink.png",
            "newgirl['Mystique'].Headband == 'black'", "images/KittySprite/Kitty_Catband_Black.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            "K_Hair == 'evo' and 'hair' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "K_Hair == 'long' and 'hair' in newgirl['Mystique'].Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "True", Null(),
            ),     
        )
    zoom .5

image Mystique_Kitty_HairBack:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Wet_Back.png",
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Wet_Back.png",
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Wet_Back.png",
            "newgirl['Mystique'].Water or K_Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
            "K_Hair == 'long' and K_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Long_Back.png",
            "K_Hair == 'long' and K_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Long_Back.png",
            "K_Hair == 'long' and K_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Long_Back.png",
            "K_Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
            "True", Null(),
            ),    
        )
    zoom .5
    
image Mystique_Kitty Blink:
    ConditionSwitch( 
    "newgirl['Mystique'].Eyes == 'sexy'", "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png", 
    "newgirl['Mystique'].Eyes == 'side'", "images/KittySprite/Kitty_Sprite_Eyes_Side.png",  
    "newgirl['Mystique'].Eyes == 'surprised'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "newgirl['Mystique'].Eyes == 'manic'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "newgirl['Mystique'].Eyes == 'normal'", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",  
    "newgirl['Mystique'].Eyes == 'down'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "newgirl['Mystique'].Eyes == 'stunned'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "newgirl['Mystique'].Eyes == 'squint'", "Kitty_Squint",  
    "newgirl['Mystique'].Eyes == 'closed'", "images/KittySprite/Kitty_Sprite_Eyes_Closed.png",    
    "True", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/KittySprite/Kitty_Sprite_Eyes_Closed.png"
    .25
    repeat 

image Mystique_Kitty_HJ_Animation:
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Kitty_Hand_Under"), 
            "Speed == 1", At("Kitty_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Kitty_Hand_Under", Kitty_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Kitty_Hand_Over"), 
            "Speed == 1", At("Kitty_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Kitty_Hand_Over", Kitty_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
      
image Mystique_Kitty_BJ_Animation:
    LiveComposite(    
        (858,928),      
        (0,0), ConditionSwitch(                                                                 
            # Kitty's body, everything below the chin
            "Speed == 0", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_0()),           #Static
            "Speed == 1", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_1()),           #Licking
            "Speed == 2", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_2()),           #Heading
            "Speed == 3", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_3()),           #Sucking
            "Speed == 4", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_4()),           #Deepthroat
            "Speed == 5", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_5()),           #Cumming High
            "Speed == 6", At("Mystique_Kitty_BJ_Backdrop", Kitty_BJ_Body_6()),           #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # Kitty's head Underlay
            "Speed == 0", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_0()),               #Static
            "Speed == 1", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_1()),               #Licking
            "Speed == 2", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_2()),               #Heading
            "Speed == 3", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Mystique_Kitty_BJ_Head", Kitty_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 
            # Cock
            "Speed == 0", At("Blowcock", Kitty_BJ_Cock_0()),                    #Static
            "Speed == 1", At("Blowcock", Kitty_BJ_Cock_1()),                    #Licking                        
            "Speed >= 2", At("Blowcock", Kitty_BJ_Cock_2()),                    #Heading+                        
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("Mystique_Kitty_BJ_Head", "Mystique_Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_3()), #Sucking
            "Speed == 4", At(AlphaMask("Mystique_Kitty_BJ_Head", "Mystique_Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_4()), #Deepthroat
            "Speed == 6", At(AlphaMask("Mystique_Kitty_BJ_Head", "Mystique_Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Mystique_Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_2()), #Heading
            "Speed == 5", At(AlphaMask("Mystique_Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),            
        (325,490), ConditionSwitch(                                                                
            # the over part of spunk
            "Speed < 3 or 'mouth' not in newgirl['Mystique'].Spunk", Null(),
            "Speed == 3", At("KittySuckingSpunk", Kitty_BJ_Head_3()), #Sucking
            "Speed == 4", At("KittySuckingSpunk", Kitty_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (325,490), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2 and 'mouth' in newgirl['Mystique'].Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_2()), #Heading
            "Speed == 5 and 'mouth' in newgirl['Mystique'].Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),   
        )
    zoom .55
    anchor (.5,.5)
     
image Mystique_Kitty_BJ_Backdrop:
    #Her Body under the head
    LiveComposite(    
        (858,928),  
        (0,0), ConditionSwitch(  
            "True and K_Tan == 'tan'", "images/KittyBJFace/Kitty_BJ_TBody.png",
            "True and K_Tan == 'tan2'", "images/KittyBJFace/Kitty_BJ_T2Body.png",
            "True and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_T3Body.png",
            "True", "images/KittyBJFace/Kitty_BJ_Body.png",                                                   
            ),
            #body
        (0,0), ConditionSwitch(                                                                  
            # piercings
            "not K_Pierce", Null(),                       
            "K_Pierce == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",      
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",   
            ),   
        )
    zoom 1.5 
    offset (-300,-200)
    
image Mystique_Kitty_BJ_Head:
    LiveComposite(    
        (858,928), 
        (0,0), ConditionSwitch(                                                                 
            #Hair back
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'blonde'", "images/KittyBJFace/Kitty_BJ_HairBlondeBackWet.png", #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'red'", "images/KittyBJFace/Kitty_BJ_HairRedBackWet.png", #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'black'", "images/KittyBJFace/Kitty_BJ_HairBlackBackWet.png", #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "(newgirl['Mystique'].Water or K_Hair == 'wet')", "images/KittyBJFace/Kitty_BJ_HairBackWet.png", #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 
            # Underface for sucking 
            "Speed > 2 and Speed != 5", Null(),            
            "newgirl['Mystique'].Water and newgirl['Mystique'].Blush and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceClosed_Wet_Blush.png",    
            "newgirl['Mystique'].Water and newgirl['Mystique'].Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",    
            "newgirl['Mystique'].Water and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceClosed_Wet.png", 
            "newgirl['Mystique'].Water", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png", 
            "newgirl['Mystique'].Blush and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceClosed_Blush.png",              
            "newgirl['Mystique'].Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",              
            "True and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceClosed.png",
            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
            ),   
        (0,0), ConditionSwitch(                                                                 
            # Underface for not sucking 
            "Speed <= 2 or Speed == 5", Null(),   #"Speed <= 2 or Trigger != 'blow' or Speed == 5", Null(), 
            "newgirl['Mystique'].Water and newgirl['Mystique'].Blush and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceOpen_Wet_Blush.png",    
            "newgirl['Mystique'].Water and newgirl['Mystique'].Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",    
            "newgirl['Mystique'].Water and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceOpen_Wet.png", 
            "newgirl['Mystique'].Water", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png", 
            "newgirl['Mystique'].Blush and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceOpen_Blush.png",              
            "newgirl['Mystique'].Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",              
            "True and K_Tan", "images/KittyBJFace/Kitty_BJ_TFaceOpen.png",
            "True", "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
            ),   
        
        (0,0), ConditionSwitch(                                                                         
            #Mouth
            "Speed == 1", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",  #licking
            "(Speed == 2 or Speed == 5)", Null(),                          #heading
            "Speed == 3", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #sucking
            "Speed == 4", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #deepthroat     
            "Speed == 6", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming        
            "newgirl['Mystique'].Mouth == 'normal' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TMouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'lipbite' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TMouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TMouth_Kiss.png",
            "newgirl['Mystique'].Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "newgirl['Mystique'].Mouth == 'sad' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TMouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TMouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TMouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Mouth_Surprised.png",          
            "newgirl['Mystique'].Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",    
            "True", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            ),       
        (428,605), ConditionSwitch(   
            # Heading Mouth
            "Speed == 2", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),  #heading 
            "Speed == 5", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnimC()), #cumming high   
            "True", Null(),
            ),  
        
        (0,0), ConditionSwitch(                                                                         
            #Spunk layer
            "'mouth' not in newgirl['Mystique'].Spunk", Null(), 
            "Speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png", #licking
            "Speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #sucking
            "Speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #deepthroat 
            "Speed == 6", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #cumming     
            "newgirl['Mystique'].Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "newgirl['Mystique'].Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #fix add
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Brows
            "newgirl['Mystique'].Brows == 'normal' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TBrows_Normal.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TBrows_Angry.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/KittyBJFace/Kitty_BJ_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TBrows_Sad.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/KittyBJFace/Kitty_BJ_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TBrows_Surprised.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/KittyBJFace/Kitty_BJ_Brows_Surprised.png",        
            "newgirl['Mystique'].Brows == 'confused' and K_Tan == 'tan3'", "images/KittyBJFace/Kitty_BJ_TBrows_Confused.png",
            "newgirl['Mystique'].Brows == 'confused'", "images/KittyBJFace/Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Mystique_Kitty BJ Blink",  
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Blindfold", "images/KittyBJFace/Kitty_BJ_Eyes_Blindfold.png",  
            "True", Null(),
            ),   
            #Eyes
        (0,0), ConditionSwitch(                                                                 
            #cum on the face
            "'facial' in newgirl['Mystique'].Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair overlay
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'red'", "images/KittyBJFace/Kitty_BJ_HairRed_Wet.png",
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'blonde'", "images/KittyBJFace/Kitty_BJ_HairBlonde_Wet.png",
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and K_HairColor == 'black'", "images/KittyBJFace/Kitty_BJ_HairBlack_Wet.png",
            "newgirl['Mystique'].Water or K_Hair == 'wet'", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png",
            "K_Hair == 'long' and K_HairColor == 'red'", "images/KittyBJFace/Kitty_BJ_HairRed_Long.png",
            "K_Hair == 'long' and K_HairColor == 'blonde'", "images/KittyBJFace/Kitty_BJ_HairBlonde_Long.png",
            "K_Hair == 'long' and K_HairColor == 'black'", "images/KittyBJFace/Kitty_BJ_HairBlack_Long.png",
            "K_Hair == 'long'", "images/KittyBJFace/Kitty_BJ_Hair_Long.png",
            "K_Hair == 'evo' and K_HairColor == 'red'", "images/KittyBJFace/Kitty_BJ_HairRed_Evo.png",
            "K_Hair == 'evo' and K_HairColor == 'blonde'", "images/KittyBJFace/Kitty_BJ_HairBlonde_Evo.png",
            "K_Hair == 'evo' and K_HairColor == 'black'", "images/KittyBJFace/Kitty_BJ_HairBlack_Evo.png",
            "K_Hair == 'evo'", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].Headband == 'pink'", "images/KittyBJFace/Kitty_BJ_Pink_Headband.png",
            "newgirl['Mystique'].Headband == 'black'", "images/KittyBJFace/Kitty_BJ_Black_Headband.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 
            #Hair water overlay
            "not newgirl['Mystique'].Water", Null(),            
            "Speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",         
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),        
        (0,0), ConditionSwitch(                                                                 
            #cum on the hair
            "'hair' in newgirl['Mystique'].Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hands overlay
            "not P_Hands", Null(),
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and P_Color == 'pink'", "images/KittyBJFace/Kitty_BJ_Wet_HeadHands_P.png",
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and P_Color == 'green'", "images/KittyBJFace/Kitty_BJ_Wet_HeadHands_G.png",
            "(newgirl['Mystique'].Water or K_Hair == 'wet') and P_Color == 'brown'", "images/KittyBJFace/Kitty_BJ_Wet_HeadHands_B.png",
            "P_Color == 'pink'", "images/KittyBJFace/Kitty_BJ_HeadHands_P.png",
            "P_Color == 'green'", "images/KittyBJFace/Kitty_BJ_HeadHands_G.png",
            "P_Color == 'brown'", "images/KittyBJFace/Kitty_BJ_HeadHands_B.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Mystique_Kitty BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "newgirl['Mystique'].Eyes == 'normal'", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",  
            "newgirl['Mystique'].Eyes == 'sexy'", "images/KittyBJFace/Kitty_BJ_Eyes_Sexy.png",  
            "newgirl['Mystique'].Eyes == 'closed'", "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png",
            "newgirl['Mystique'].Eyes == 'surprised'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "newgirl['Mystique'].Eyes == 'side'", "images/KittyBJFace/Kitty_BJ_Eyes_Side.png",
            "newgirl['Mystique'].Eyes == 'stunned'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "newgirl['Mystique'].Eyes == 'down'", "images/KittyBJFace/Kitty_BJ_Eyes_Down.png",
            "newgirl['Mystique'].Eyes == 'manic'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "newgirl['Mystique'].Eyes == 'squint'", "images/KittyBJFace/Kitty_BJ_Eyes_Squint.png",
            "True", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",  
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3    
        "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png"
        .25
        repeat

image Mystique_Kitty_BJ_MouthSuckingMask:
    #the mask used for sucking animations
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        zoom 1.4
    contains: #see if this works, if not remove it
        ConditionSwitch(
            "'mouth' not in newgirl['Mystique'].Spunk", Null(),  
            "Speed != 2 and Speed != 5", Null(),            
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",            
            )   
        zoom 1.4

# End Kitty Section / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
