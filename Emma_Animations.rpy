# Basic character Sprites
image Emma_Sprite:
    LiveComposite(
        (402,965), 
#        (55,0), ConditionSwitch(                                                                         #hair back temporary
#            "not E_Hair", Null(),
#            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png",
#            "True", Null(),        
#            ),        
        (0,0), ConditionSwitch(                                                                         #hair back 
            "not E_Hair", Null(),
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_HairbackWet.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(                                                                         #panties down back 
            "E_PantiesDown and E_Panties == 'white panties'", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(                                                                         #legs 
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Legs_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Legs_Arms1.png", #if E_Arms == 1         
            ),     
        (0,0), ConditionSwitch(                                                                         #pubes 
            "E_Pubes", "images/EmmaSprite/EmmaSprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(                                                                         #Water effect 
            "E_Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(                                                                         #panties down if not wearing pants
            "not E_PantiesDown or (E_Legs and not E_Upskirt)", Null(),   
            "E_Panties == 'white panties'", "images/EmmaSprite/EmmaSprite_Panties_Down.png",  
            "True", Null(),        
            ),        
        (0,0), ConditionSwitch(                                                                         #panties up
            "E_PantiesDown and (not E_Legs or E_Upskirt)", Null(),   
            "E_Panties == 'white panties'", "images/EmmaSprite/EmmaSprite_Panties.png",  
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(                                                                         #pants    
            "E_Legs == 'pants' and not E_Upskirt", "images/EmmaSprite/EmmaSprite_Pants.png", 
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(                                                                         #Personal Wetness            
            "not E_Wet", Null(),
            "E_Legs and E_Wet <= 1", Null(),
            "E_Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "E_Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #E_Wet >1
            ),     
        (0,0), ConditionSwitch(                                                                         #pussy spunk 
            "E_Legs", Null(),
            "'pussy' in E_Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Pussy.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(                                                                         #Chest underlayer
            "E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetUnder.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                         #Towel underlayer
            "E_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Under.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                         #arms 
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Arms2.png",         # one hand up
            "True", "images/EmmaSprite/EmmaSprite_Arms1.png", #if E_Arms == 1   # Crossed        
            ),  
        (0,0), ConditionSwitch(                                                                         #Water effect 
            "not E_Water", Null(),             
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Water_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms1.png", #if E_Arms == 1      
            ), 
        (0,0), ConditionSwitch(                                                                         #gloves 
            "not E_Arms", Null(),  
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Gloves_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png", #if E_Arms == 1         
            ),   
        (0,0), ConditionSwitch(                                                                         #tits
#            "E_Pierce == 'barbell'", "images/EmmaSprite/Emma_chest_barbell.png",            
#            "E_Pierce == 'ring'", "images/EmmaSprite/Emma_chest_rings.png",      
            "Emma_Arms == 1 or E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra' or E_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
#            "E_TitsUp", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_TitsUp = 1
            "True", "images/EmmaSprite/EmmaSprite_TitsDown.png",   # E_TitsUp = 0
            ), 
        (0,0), ConditionSwitch(                                                                         #Water effect 
            "not E_Water", Null(),             
            "Emma_Arms == 1 or E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",  
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png", #if E_Arms == 1      
            ), 
        (0,0), ConditionSwitch(                                                                         #Chest layer
            "E_Chest == 'corset' and E_Over", "images/EmmaSprite/EmmaSprite_CorsetTitsX.png",   
            "E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits.png",   
            "True", Null(),              
            ),       
#        (0,0), ConditionSwitch(                                                                         #soap
#            "E_Water == 3", "images/EmmaSprite/Emma_body_wet3.png",
#            "True", Null(),                 
#            ),
        (0,0), ConditionSwitch(                                                                         #cape layer       
            "E_Over or E_Chest != 'corset'", Null(),  
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",              
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",   
            ), 
        (0,0), ConditionSwitch(                                                                         #Overshirt layer       
            "not E_Over", Null(),  
            "E_Over == 'jacket' and Emma_Arms == 2 and E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",      
            "E_Over == 'jacket' and Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Jacket_2Down.png",        
            "E_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up.png",       
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         #Towel Over layer       
            "not E_Over", Null(),  
            "E_Over == 'towel' and Emma_Arms == 2 and E_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",      
            "E_Over == 'towel' and Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Towel_Down2.png",        
            "E_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up1.png",          
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         #neck
            "E_Neck == 'choker'", "images/EmmaSprite/EmmaSprite_Neck_Choker.png",       
            "True", Null(), 
            ),  
        (55,0), "EmmaSprite_Head",                                                                           #Head
        
        (0,0), ConditionSwitch(                                                                         #hand spunk 
            "Emma_Arms != 2 or 'hand' not in E_Spunk", Null(),  
            "'mouth' in E_Spunk", "images/EmmaSprite/EmmaSprite_Spunk_HandM.png",  
            "True", "images/EmmaSprite/EmmaSprite_Spunk_Hand.png",   
            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not E_Held or Emma_Arms != 2", Null(), 
#            "Emma_Arms == 2 and E_Held == 'phone'", "images/EmmaSprite/Emma_held_phone.png",
#            "Emma_Arms == 2 and E_Held == 'dildo'", "images/EmmaSprite/Emma_held_dildo.png",
#            "Emma_Arms == 2 and E_Held == 'vibrator'", "images/EmmaSprite/Emma_held_vibrator.png",
#            "Emma_Arms == 2 and E_Held == 'panties'", "images/EmmaSprite/Emma_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Emma is masturbating using Trigger3 actions
            "E_Loc == 'bg teacher'", Null(),
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Emma'", Null(),
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
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Emma'", Null(), 
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_E",
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
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger or Ch_Focus != 'Emma'", Null(),
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
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger2 or Ch_Focus != 'Emma'", Null(),
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
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger4 or Ch_Focus != 'Emma'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_E",
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
            "E_Loc == 'bg teacher'", Null(),
            "not Trigger3 or Ch_Focus == 'Emma'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and K_Lust >= 70", "GirlFingerPussy_E",
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

image TempHairBack:
    "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png"         
    anchor (0.6, 0.0)                
    zoom .5       
    
image EmmaSprite_Head:
    LiveComposite(
        (555,673), 
#        (0,0), ConditionSwitch(                                                                         #hair back 
#            "E_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
#            "True", Null(),        
#            ),      
        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
            "E_Blush or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
            "E_Blush != 1 or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 not wet
            "E_Blush != 2 or E_Hair == 'wet' or E_Water", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_Brows == 'normal'
            ),
        
         (0,0), ConditionSwitch(                                                                         #Face no blush wet
            "E_Blush or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 wet
            "E_Blush != 1 or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 2 wet
            "E_Blush != 2 or (E_Hair != 'wet' and not E_Water)", Null(),        
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_Brows == 'normal'
            ),
        
        (0,0), ConditionSwitch(                                                                         #Mouths        
            "E_Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "E_Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "E_Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "E_Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "E_Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),   
        
        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
            "'mouth' not in E_Spunk", Null(),
            "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
            "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
            ),  
        
        (0,0), "Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "E_Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not E_Hair", Null(),
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "not E_Water", Null(),
            "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in E_Spunk and (E_Hair == 'wet' or E_Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",                         
            "'hair' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5   

image Emma Blink:
    ConditionSwitch(
    "E_Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
    "E_Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
    "E_Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
    "E_Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
    "E_Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
    "E_Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
    "E_Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_Eyes == 'squint'", "Emma_Squint",
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

image Emma_Squint:
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Squint.png"
    .25
    repeat             
# End Emma Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Test_Object:                 #this is the yellow rectangle
    contains:
        Solid("#d5f623", xysize=(1024, 678))
    anchor (0,0)
    alpha .8
    
image Emma_At_DeskB:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)
    contains:        
#        AlphaMask("Test_Object", "images/ClassroomFront.png")
        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
    contains:
        ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
                "True", "images/ClassroomPupils.png",                
                )      

image Emma_At_PodiumB:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)
    contains:        
#        AlphaMask("Test_Object", "images/ClassroomFront.png")
        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
    contains:
        ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
                "True", "images/ClassroomPupils.png",                
                )                     
        
image Emma_At_Desk:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)

image Emma_At_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)
            
        
label E_Kissing_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        ease 0.5 zoom 2
    return
    
label E_Kissing_Smooch:   
    call EmmaFace("kiss")  
    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaLayer:
        ease 0.5 xpos StageCenter zoom 2
        pause 1
        ease 0.5 xpos E_SpriteLoc zoom 1        
    call EmmaFace("sexy")  
    return
            
label E_Breasts_Launch(T = Trigger):    
    call Emma_Hide
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) zoom 2
    return
        
label E_Pussy_Launch(T = Trigger):
    call Emma_Hide    
    $ Trigger = T
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        ease 0.5 pos (700,-400) zoom 2
    return
        
label E_Pos_Reset(Pose = 0):
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1   
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1  
        alpha 1
    $ Trigger = Pose
    return
    
label Emma_Hide:
#        if renpy.showing("Emma_SexSprite"):
#            call Emma_Sex_Reset
        hide Emma_SexSprite
        hide Emma_HJ_Animation
        hide Emma_BJ_Animation
    #    hide Emma_TJ_Animation 
        return

label Emma_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Emma_HJ_Animation"):
        return    
    $ Speed = 0
    hide Emma_HJ_Animation with easeoutbottom
    show Emma_Sprite at SpriteLoc(StageRight) zorder EmmaLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Emma_Sprite zorder EmmaLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_E:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,400)#(215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_E:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,400)#(120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -90
        block: 
            ease 1 rotate -60 #-30
            ease 1 rotate -90 #-60 
            repeat

#image GropeBreast:
image LickRightBreast_E:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (105,375)#(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (85,345)#(95,370)            
            pause .5
            ease 1.5 rotate 30 pos (105,375)#(115,400)
            repeat
            
image LickLeftBreast_E:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (205,370) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (190,350)#(190,380)            
            pause .5
            ease 1.5 rotate 30 pos (205,370)#(200,410)
            repeat

image GropeThigh_E: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (180,670)#(200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (150,750) 
            ease 1 rotate 100 pos (180,670)   
            repeat

image GropePussy_E: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,600)#(210,640) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (200,585)
                ease .75 rotate 170 pos (200,600)   
            choice: 
                ease .5 rotate 190 pos (200,585)
                pause .25
                ease 1 rotate 170 pos (200,600)             
            repeat

image FingerPussy_E: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (210,665)#(220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (220,640)#(230,695)
                pause .5
                ease 1 rotate 50 pos (210,665)  #(220,730)     
            choice:                          
                ease .5 rotate 40 pos (220,640)
                pause .5
                ease 1.75 rotate 50 pos (210,665)  
            choice:                          
                ease 2 rotate 40 pos (220,640)
                pause .5
                ease 1 rotate 50 pos (210,665)  
            choice:                          
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665) 
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
            repeat
            
image Lickpussy_E:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (230,625)#(240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easein .5 rotate -50 pos (210,605) #(220,660)
            linear .5 rotate -60 pos (200,615) #(210,670)
            easeout 1 rotate 10 pos (230,625) #(240,680)
            repeat

image VibratorRightBreast_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380           
            pause .25
            repeat

image VibratorLeftBreast_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400           
            pause .25
            repeat
            
image VibratorPussy_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665           
            pause .25
            repeat

image VibratorAnal_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665           
            pause .25
            repeat
            
image VibratorPussyInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_E: 
    contains:
        "GirlGropeLeftBreast_E"
    contains:
        "GirlGropeRightBreast_E"
    
image GirlGropeLeftBreast_E:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block: 
            ease 1 rotate -40 pos (230,360)#(280,390)
            ease 1 rotate -20 pos (240,370)
            repeat

image GirlGropeRightBreast_E:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,380) #(110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -30 pos (90,410)#(110,410)
            ease 1 rotate -10 pos (90,380)
            repeat

image GirlGropeThigh_E: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel: 
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730            
            repeat
        parallel:            
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GirlGropePussy_ESelf:
    contains:
        "GirlGropePussy_E"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)
    
image GirlGropePussy_E: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,575)#(210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (205,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (205,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
            repeat

image GirlFingerPussy_E: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (220,640)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice: #Fast stroke
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat

# Start Emma Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label EmmaFace(Emote = E_Emote, B = E_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
        if (E_Forced or "angry" in E_RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif E_ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ E_Mouth = "normal"
                $ E_Brows = "normal"
                $ E_Eyes = "normal"
        elif Emote == "angry":
                $ E_Mouth = "sad"
                $ E_Brows = "angry"
                $ E_Eyes = "sexy"
        elif Emote == "bemused":
                $ E_Mouth = "normal"
                $ E_Brows = "sad"
                $ E_Eyes = "squint"
        elif Emote == "closed":
                $ E_Mouth = "normal"
                $ E_Brows = "sad"
                $ E_Eyes = "closed"  
        elif Emote == "confused":
                $ E_Mouth = "kiss"
                $ E_Brows = "confused"
                $ E_Eyes = "squint"
        elif Emote == "kiss":
                $ E_Mouth = "kiss"
                $ E_Brows = "sad"
                $ E_Eyes = "closed"
        elif Emote == "tongue":
                $ E_Mouth = "tongue"
                $ E_Brows = "sad"
                $ E_Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ E_Mouth = "smile"
                $ E_Brows = "sad"
                $ E_Eyes = "surprised"
                $ E_Blush = 1
        elif Emote == "sad":
                $ E_Mouth = "sad"
                $ E_Brows = "sad"
                $ E_Eyes = "sexy"
        elif Emote == "sadside":
                $ E_Mouth = "sad"
                $ E_Brows = "sad"
                $ E_Eyes = "side"
        elif Emote == "sexy":
                $ E_Mouth = "lipbite"
                $ E_Brows = "normal"
                $ E_Eyes = "squint"
        elif Emote == "smile":
                $ E_Mouth = "smile"
                $ E_Brows = "normal"
                $ E_Eyes = "normal"
        elif Emote == "sucking":
                $ E_Mouth = "sucking"
                $ E_Brows = "surprised"
                $ E_Eyes = "closed"
        elif Emote == "surprised":
                $ E_Mouth = "kiss"
                $ E_Brows = "surprised"
                $ E_Eyes = "surprised"
        elif Emote == "startled":
                $ E_Mouth = "smile"
                $ E_Brows = "surprised"
                $ E_Eyes = "surprised"
        elif Emote == "down":
                $ E_Mouth = "sad"
                $ E_Brows = "sad"
                $ E_Eyes = "down"  
        elif Emote == "perplexed":
                $ E_Mouth = "smile"
                $ E_Brows = "sad"
                $ E_Eyes = "normal"
        elif Emote == "sly":
                $ E_Mouth = "smirk"
                $ E_Brows = "normal"
                $ E_Eyes = "squint"
            
        if M:
                $ E_Eyes = "surprised"        
        if B > 1:
                $ E_Blush = 2
        elif B:
                $ E_Blush = 1
        else:
                $ E_Blush = 0
        
        if Mouth:
                $ E_Mouth = Mouth
        if Eyes:
                $ E_Eyes = Eyes
        if Brows:
                $ E_Brows = Brows
        
        return
        
        
# Emma's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label EmmaWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call E_Pos_Reset
                    "Face":
                        call E_Kissing_Launch(0)
                    "Body":
                        call E_Pussy_Launch(0)
                    "Back":
                        jump EmmaWardrobe 
        # Outfits
#        "Teacher outfit":
#            $ E_Outfit = "teacher"
#            call EmmaOutfit
#        "Super outfit":
#            $ E_Outfit = "costume"
#            call EmmaOutfit
        "Nude":
            $ E_Over = 0
            $ E_Chest = 0
            $ E_Legs = 0
            $ E_Panties = 0
            $ E_Gloves = 0
            $ E_Neck = 0
#            $ E_Outfit = "nude"
#            call EmmaOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [E_Over]" if E_Over:
                        $ E_Over = 0
                    "Add Jacket":
                        $ E_Over = "jacket"   
                        $ E_Arms = 0
                    "Add Towel":
                        $ E_Over = "towel"   
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe                
        "Tops":            
            while True:
                menu:
                    # Tops    
                    "Remove [E_Chest]" if E_Chest:
                        $ E_Chest = 0
                    "Add corset":
                        $ E_Chest = "corset"
#                    "Add sports bra":
#                        $ E_Chest = "sports bra"
#                    "Add buttoned tank top" if E_Over != "mesh top":
#                        $ E_Chest = "buttoned tank"
#                    "Add lace bra":
#                        $ E_Chest = "lace bra"
#                    "Add bra":
#                        $ E_Chest = "bra"                            
#                    "Toggle Piercings":
#                        if E_Pierce == "ring":
#                            $ E_Pierce = "barbell"
#                        elif E_Pierce == "barbell":
#                            $ E_Pierce = 0
#                        else:
#                            $ E_Pierce = "ring"
                    "Back":
                        jump EmmaWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if E_Legs:     
                        $ E_Legs = 0
                    "Add pants":
                        $ E_Legs = "pants"
                        $ E_Upskirt = 0
                    "Toggle upskirt":
                        if E_Upskirt:
                            $ E_Upskirt = 0
                        else:
                            $ E_Upskirt = 1
                    "Back":
                        jump EmmaWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
#                    "Hose":
#                        menu:
#                            "Add hose":     
#                                $ E_Hose = "stockings"  
#                            "Add garter":     
#                                $ E_Hose = "garterbelt"  
#                            "Add stockings and garter":     
#                                $ E_Hose = "stockings and garterbelt"  
#                            "Add pantyhose":     
#                                $ E_Hose = "pantyhose"   
#                            "Add tights":     
#                                $ E_Hose = "tights"   
#                            "Add ripped hose":     
#                                $ E_Hose = "ripped pantyhose"   
#                            "Add ripped tights":     
#                                $ E_Hose = "ripped tights"   
#                            "Add tights":     
#                                $ E_Hose = "tights"    
#                            "Remove hose" if E_Hose:     
#                                $ E_Hose = 0  
                    "Remove panties" if E_Panties:     
                        $ E_Panties = 0     
                    "Add black panties":
                        $ E_Panties = "white panties"
#                    "Add shorts":
#                        $ E_Panties = "shorts"
#                    "Add green panties":
#                        $ E_Panties = "green panties"  
#                    "Add lace panties":
#                        $ E_Panties = "lace panties"    
                    "pull down-up panties":
                        if E_PantiesDown:
                            $ E_PantiesDown = 0
                        else:
                            $ E_PantiesDown = 1
                    "Back":
                        jump EmmaWardrobe    
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call EmmaEmotionEditor
                    "Toggle Arms":
                        if Emma_Arms == 1:
                            $ Emma_Arms = 2
                        else:
                            $ Emma_Arms = 1
                    "Toggle Wetness":
                        if not E_Wet:
                            $ E_Wet = 1
                        elif E_Wet == 1:
                            $ E_Wet = 2
                        else:
                            $ E_Wet  = 0
                    "Toggle wet look":
                        if not E_Water:
                            $ E_Water = 1
                        elif E_Water == 1:
                            $ E_Water = 3
                        else:
                            $ E_Water  = 0
                    "Toggle pubes":
                        if not E_Pubes:
                            $ E_Pubes = 1
                        else:
                            $ E_Pubes = 0
                    "Toggle Pussy Spunk":
                        if "pussy" in E_Spunk:
                            $ E_Spunk.remove("pussy")
                        else:
                            $ E_Spunk.append("pussy")

#                    "Toggle held":
#                        if not E_Held:
#                            $ E_Held  = "phone"
#                        elif E_Held == "phone":
#                            $ E_Held  = "dildo"
#                        elif E_Held == "dildo":
#                            $ E_Held  = "vibrator"
#                        elif E_Held == "vibrator":
#                            $ E_Held  = "panties"
#                        else:
#                            $ E_Held  = 0  
                    "Add choker" if not E_Neck:
                        $ E_Neck = "choker"
                    "Remove choker" if E_Neck:
                        $ E_Neck = 0
                        
                    "Add Gloves" if not E_Arms:
                        $ E_Arms = "white gloves"
                    "Remove Gloves" if E_Arms:
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe               
#        "Set Custom Outfit #1.":
#            $ E_Custom[0] = 1
#            $ E_Custom[1] = E_Arms
#            $ E_Custom[2] = E_Legs
#            $ E_Custom[3] = E_Over
#            $ E_Custom[4] = E_Under #fix, this can be changed to something else, no longer necessary
#            $ E_Custom[5] = E_Chest
#            $ E_Custom[6] = E_Panties 
#            $ E_Custom[7] = E_Pubes 
#            $ E_Custom[8] = E_Hair
#            $ E_Custom[9] = E_Hose
#        "Wear Custom Outfit #[E_Custom[0]]." if E_Custom[0]:
#            $ Line = E_Outfit
#            $ E_Outfit = "custom1"
#            call RogueOutfit
#            $ E_Outfit = Line
        "Nothing":
            return
    jump EmmaWardrobe
return

label EmmaEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ E_Emote = "normal"
                    call EmmaFace
                "Angry":
                    $ E_Emote = "angry"
                    call EmmaFace
                "Smiling":
                    $ E_Emote = "smile"
                    call EmmaFace
                "Sexy":
                    $ E_Emote = "sexy"
                    call EmmaFace
                "Suprised":
                    $ E_Emote = "surprised"
                    call EmmaFace
                "Bemused":
                    $ E_Emote = "bemused"
                    call EmmaFace
                "Manic":
                    $ E_Emote = "manic"
                    call EmmaFace
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ E_Emote = "sad"
                    call EmmaFace
                "Sucking":
                    $ E_Emote = "sucking"
                    call EmmaFace
                "kiss":
                    $ E_Emote = "kiss"
                    call EmmaFace
                "Tongue":
                    $ E_Emote = "tongue"
                    call EmmaFace
                "confused":
                    $ E_Emote = "confused"
                    call EmmaFace
                "Closed":
                    $ E_Emote = "closed"
                    call EmmaFace
                "Down":
                    $ E_Emote = "down"
                    call EmmaFace
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ E_Emote = "sadside"
                    call EmmaFace
                "Startled":
                    $ E_Emote = "startled"
                    call EmmaFace
                "Perplexed":
                    $ E_Emote = "perplexed"
                    call EmmaFace
                "Sly":
                    $ E_Emote = "sly"
                    call EmmaFace
        "Toggle Mouth Spunk":
            if "mouth" in E_Spunk:
                $ E_Spunk.remove("mouth")
            else:
                $ E_Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in E_Spunk:
                $ E_Spunk.remove("hand")
            else:
                $ E_Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in E_Spunk and "hair" not in E_Spunk:
                $ E_Spunk.append("hair")
            elif "facial" in E_Spunk:
                $ E_Spunk.remove("facial")                
                $ E_Spunk.remove("hair")
            else:
                $ E_Spunk.append("facial")
            
        "Blush":
            if E_Blush == 2:
                $ E_Blush = 1
            elif E_Blush:
                $ E_Blush = 0
            else:
                $ E_Blush = 2  
        "Exit.":
            return
    jump EmmaEmotionEditor
return