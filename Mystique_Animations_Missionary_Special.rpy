# Mystique Missionary Transformations

image Mystique_SexSprite:
    ConditionSwitch(          
    "newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
    "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_SexSprite",
    "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_SexSprite",
    "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_SexSprite",
    "True", "Mystique_Blue_SexSprite",
    ),


# Emma Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Emma_SexSprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Common_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Common_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Common_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Common_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Common_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Common_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Common_Hotdog_Body_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Common_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Common_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Common_Sex_Body_FootAnimStatic",
            "True", "Mystique_Common_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Common_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Common_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Common_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Common_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Common_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Common_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Common_Hotdog_Legs_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Common_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Common_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Common_Sex_Legs_FootAnimStatic",
            "True", "Mystique_Common_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Mystique_Emma_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),
        (350,-275), "Mystique_Emma_HairBack_Sex",    #(260,-350)   (402 -200 with 0 rotation)                                                                                #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
        #     "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Sex_Body_Barbell.png",   
        #     "E_Pierce == 'ring'", "images/EmmaSex/Emma_Sex_Body_Ring.png",   
            "True", "images/EmmaSex/Emma_Sex_Body.png",             
            ), 
        (350,-275), "Mystique_Emma_Head_Sex",  #check positioning (400,-300)
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "True", "images/EmmaSex/Emma_Sex_Tits_Bare.png",
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/EmmaSex/Emma_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/EmmaSex/Emma_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Mystique_Emma_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Emma_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].LegsUp", "images/EmmaSex/Emma_Sex_Legs_LegsUp.png",
            "True", "images/EmmaSex/Emma_Sex_Legs.png",
            ),                                                     #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].LegsUp", Null(),
            "newgirl['Mystique'].Water", "images/EmmaSex/Emma_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Mystique_Emma_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Mystique_Emma_Sex_Pussy",                                                                         #Pussy Composite

        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/EmmaSex/Emma_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Emma_Hotdog_Zero_Anim2",
            "Speed", "Emma_Hotdog_Zero_Anim1",
            "True", "Emma_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Emma_Footcock_Zero_Anim2",
            "Speed", "Emma_Footcock_Zero_Anim1",
            "True", "Emma_Footcock_Static",   
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Mystique_Emma_Sex_Feet",  
            "E_LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Mystique_Emma_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Mystique_Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_FeetMask.png"), 
            "True", "Mystique_Emma_Sex_Feet",            
            ),
        )

image Mystique_Emma_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Emma_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].LegsUp", "images/EmmaSex/Emma_Sex_Feet_LegsUp.png",
            "True", "images/EmmaSex/Emma_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/EmmaSex/Emma_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        )

image Mystique_Emma_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Emma_Sex_Body            
    "Mystique_Emma_Sex_HairBack"
    zoom 1.5
    anchor (0.5,0.5)   
    rotate 5         
    xzoom -1

image Mystique_Emma_Sex_HairBack:
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
    zoom .48 

image Mystique_Emma_Head_Sex:
    # The head used for the sex pose, referenced by Emma_Sex_Body
    "Mystique_Emma_Sex_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate 5
    xzoom -1

image Mystique_Emma_Sex_Head:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(                                                                         #Face no blush not wet
            "newgirl['Mystique'].Blush or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #newgirl['Mystique'].Brows == 'normal'
            ),
        (0,0), ConditionSwitch(                                                                         #Face blush 1 not wet
            "newgirl['Mystique'].Blush != 1 or E_Hair == 'wet' or newgirl['Mystique'].Water", Null(),        
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #newgirl['Mystique'].Brows == 'normal'
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
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in newgirl['Mystique'].Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
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
            "newgirl['Mystique'].Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
            ), 
        
        (0,0), "Mystique_Emma Blink",                                                                           #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "newgirl['Mystique'].Brows == 'normal' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "newgirl['Mystique'].Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            "newgirl['Mystique'].Brows == 'confused' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "newgirl['Mystique'].Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
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
        )                
    anchor (0.6, 0.0)                
    zoom .48 

image Mystique_Emma_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/EmmaSex/Emma_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/EmmaSex/Emma_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Emma_Anal_Tip", 
            "newgirl['Mystique'].Loose", "images/EmmaSex/Emma_Sex_Hole_Loose.png",   
            "True", "images/EmmaSex/Emma_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/EmmaSex/Emma_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Emma_Anal_Spunk_Heading_Under",
                "True", "images/EmmaSex/Emma_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Emma_Anal_Zero_Anim3", "Emma_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Emma_Anal_Zero_Anim2", "Emma_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Emma_Anal_Zero_Anim1", "Emma_Anal_Fucking_Mask"),
            "True", AlphaMask("Emma_Anal_Zero_Anim0", "Emma_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Emma_Anal_Spunk_Heading_Over",
                "True", "images/EmmaSex/Emma_Sex_Spunk_Anal_Over.png",  
                )  

image Mystique_Emma_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/EmmaSex/Emma_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/EmmaSex/Emma_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/EmmaSex/Emma_Sex_Pussy_Closed.png",    
                "Trigger == 'lick pussy'", "images/EmmaSex/Emma_Sex_Pussy_Open.png",   
                "True", "images/EmmaSex/Emma_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not newgirl['Mystique'].Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/EmmaSex/Emma_Sex_WetPussy_F.png",
                "True", "images/EmmaSex/Emma_Sex_WetPussy_C.png",
                )
    # contains: 
    #         #ring piercing
    #         ConditionSwitch(  
    #             "E_Pierce != 'ring'", Null(),
    #             "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/EmmaSex/Emma_Sex_Pussy_Ring.png",
    #             "True", "images/EmmaSex/Emma_Sex_Pussy_RingF.png",
    #             ) 
    # contains: 
    #         #barbell piercing
    #         ConditionSwitch(  
    #             "E_Pierce != 'barbell'", Null(),
    #             "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/EmmaSex/Emma_Sex_Pussy_Barbell.png",
    #             "True", "images/EmmaSex/Emma_Sex_Pussy_BarbellF.png",
    #             )             
    contains:
            # pubes
            ConditionSwitch(    
                "not newgirl['Mystique'].Pubes", Null(),         
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/EmmaSex/Emma_Sex_Pubes_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/EmmaSex/Emma_Sex_Pubes_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/EmmaSex/Emma_Sex_Pubes_Closed.png", 
                "Trigger == 'lick pussy'", "images/EmmaSex/Emma_Sex_Pubes_Open.png", 
                "True", "images/EmmaSex/Emma_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in newgirl['Mystique'].Spunk", "images/EmmaSex/Emma_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not P_Sprite", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 3", AlphaMask("Emma_Sex_Zero_Anim3", "Emma_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("Emma_Sex_Zero_Anim2", "Emma_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("Emma_Sex_Zero_Anim1", "Emma_Pussy_Open_Mask"),
                "P_Sprite and P_Cock == 'in'", AlphaMask("Emma_Sex_Zero_Anim0", "Emma_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Emma_Pussy_Spunk_Heading",   
                "True", "images/EmmaSex/Emma_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Emma Pussy composite
# End Emma Section / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Rogue Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Rogue_SexSprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Common_Sex_Body_Anim3",  
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Common_Sex_Body_Anim2",#akiparcero
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Common_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Common_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Common_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Common_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Common_Hotdog_Body_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Common_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Common_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Common_Sex_Body_FootAnimStatic",
            "True", "Mystique_Common_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Common_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Common_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Common_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Common_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Common_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Common_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Common_Hotdog_Legs_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Common_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Common_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Common_Sex_Legs_FootAnimStatic",
            "True", "Mystique_Common_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Mystique_Rogue_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Rogue_SexSprite
        (1120,840),
        (140,-240), "Mystique_Rogue_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "True and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Body.png",             
            "True and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Body.png",             
            "True", "images/RogueSex/Rogue_Sex_Body.png",             
            ), 
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "not R_Pierce", Null(),
            "R_Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Tits_Barbell.png",   
            "R_Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_Tits_Ring.png",   
            "True", Null(),             
            ),  
        (140,-240), "Mystique_Rogue_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/RogueSex/Rogue_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/RogueSex/Rogue_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Mystique_Rogue_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Rogue_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "R_Tan == 'tan1' and newgirl['Mystique'].LegsUp", "images/RogueSex/Rogue_t1Sex_Legs_LegsUp.png",
            "R_Tan == 'tan' and newgirl['Mystique'].LegsUp", "images/RogueSex/Rogue_tSex_Legs_LegsUp.png",
            "R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Legs.png",                                              #Legs Base                                                      #Legs Base
            "R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Legs.png",                                              #Legs Base                                                      #Legs Base
            "newgirl['Mystique'].LegsUp", "images/RogueSex/Rogue_Sex_Legs_LegsUp.png",
            "True", "images/RogueSex/Rogue_Sex_Legs.png",
            ),
        (0,0), ConditionSwitch( 
            "newgirl['Mystique'].LegsUp", Null(),
            "newgirl['Mystique'].Water", "images/RogueSex/Rogue_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Mystique_Rogue_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Mystique_Rogue_Sex_Pussy",  

        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/RogueSex/Rogue_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Rogue_Hotdog_Zero_Anim2",
            "Speed", "Rogue_Hotdog_Zero_Anim1",
            "True", "Rogue_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Rogue_Footcock_Zero_Anim2",
            "Speed", "Rogue_Footcock_Zero_Anim1",
            "True", "Rogue_Footcock_Static",   
            ),
   
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Mystique_Rogue_Sex_Feet",  
            "newgirl['Mystique'].LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Mystique_Rogue_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Mystique_Rogue_Sex_Feet", "images/RogueSex/Rogue_Sex_FeetMask.png"), 
            "True", "Mystique_Rogue_Sex_Feet",            
            ),
        )
    
image Mystique_Rogue_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Rogue_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "R_Tan and newgirl['Mystique'].LegsUp", "images/RogueSex/Rogue_tSex_Feet_LegsUp.png",
            "newgirl['Mystique'].LegsUp", "images/RogueSex/Rogue_Sex_Feet_LegsUp.png",
            "R_Tan", "images/RogueSex/Rogue_tSex_Feet.png",                                                         #Legs Base
            "True", "images/RogueSex/Rogue_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/RogueSex/Rogue_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        )

image Mystique_Rogue_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Rogue_Sex_Body            
    "Mystique_Rogue_HairBack"
    zoom 1.4
    anchor (0.5,0.5)   
    #rotate -10  

image Mystique_Rogue_HairBack:
    LiveComposite(
        (416,610),    
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
        )

image Mystique_Rogue_Head_Sex:
    # The head used for the sex pose, referenced by Rogue_Sex_Body
    "Mystique_Rogue_Head"
    zoom 1.4
    anchor (0.5,0.5)
    #rotate -10

image Mystique_Rogue_Head:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(                                                                         #head 
            #"renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            "R_Tan and R_Hair == 'evo' and newgirl['Mystique'].Water", "images/RogueSprite/Rogue_thead_evowet.png",
            "R_Hair == 'evo' and newgirl['Mystique'].Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_Tan and R_Hair == 'evo' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2.png",
            "R_Hair == 'evo' and newgirl['Mystique'].Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_Tan and R_Hair == 'evo' and newgirl['Mystique'].Blush", "images/RogueSprite/Rogue_thead_evo_blush.png",
            "R_Hair == 'evo' and newgirl['Mystique'].Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_Tan and R_Hair == 'evo'", "images/RogueSprite/Rogue_thead_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "R_Tan", "images/RogueSprite/Rogue_thead_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
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
        (0,0), ConditionSwitch(                                                                         #face spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),
        )

image Mystique_Rogue_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/RogueSex/Rogue_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/RogueSex/Rogue_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Sex_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Rogue_Anal_Tip", 
            "newgirl['Mystique'].Loose", "images/RogueSex/Rogue_Sex_Hole_Loose.png",   
            "True", "images/RogueSex/Rogue_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/RogueSex/Rogue_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Rogue_Anal_Spunk_Heading_Under",
                "True", "images/RogueSex/Rogue_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask"),
            "True", AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Rogue_Anal_Spunk_Heading_Over",
                "True", "images/RogueSex/Rogue_Sex_Spunk_Anal_Over.png",  
                )  

image Mystique_Rogue_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Closed.png",
                "P_Sprite and P_Cock == 'in' and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Closed.png",
                "P_Sprite and P_Cock == 'in'", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                "Trigger == 'lick pussy' and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Open.png",
                "Trigger == 'lick pussy' and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "True and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Closed.png",
                "True and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Closed.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                )    
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not newgirl['Mystique'].Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_WetPussy_F.png",
                "True", "images/RogueSex/Rogue_Sex_WetPussy_C.png",
                )
    contains: 
            #ring piercing
            ConditionSwitch(  
                "R_Pierce != 'ring'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                ) 
    contains: 
            #barbell piercing
            ConditionSwitch(  
                "R_Pierce != 'barbell'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )  
    contains:
            # pubes
            ConditionSwitch(    
                "not newgirl['Mystique'].Pubes", Null(),         
                "R_HairColor == 'blonde'", "images/RogueSex/Rogue_Sex_Pubes_Blonde.png",
                "R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_Pubes_Black.png",
                "True", "images/RogueSex/Rogue_Sex_Pubes.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in newgirl['Mystique'].Spunk", "images/RogueSex/Rogue_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not P_Sprite", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "P_Sprite and P_Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Kitty_Pussy_Spunk_Heading",   
                "True", "images/RogueSex/Rogue_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Rogue Pussy composite
# End Rogue Section / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Kitty Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Kitty_SexSprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Common_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Common_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Common_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Common_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Common_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Common_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Common_Hotdog_Body_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Common_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Common_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Common_Sex_Body_FootAnimStatic",
            "True", "Mystique_Common_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Common_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Common_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Common_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Common_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Common_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Common_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Common_Hotdog_Legs_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Common_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Common_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Common_Sex_Legs_FootAnimStatic",
            "True", "Mystique_Common_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Mystique_Kitty_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Mystique_Kitty_SexSprite
        (1120,840),
        (260,-350), "Mystique_Kitty_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "K_Tan == 'tan'", "images/KittySex/Kitty_Sex_TBody.png",             
            "K_Tan == 'tan2'", "images/KittySex/Kitty_Sex_T2Body.png",
            "K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Body.png",
            "True", "images/KittySex/Kitty_Sex_Body.png",             
            ), 
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "not K_Pierce", Null(),             
            "K_Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Body_Tits_Barbell.png",   
            "K_Pierce == 'ring'", "images/KittySex/Kitty_Sex_Body_Tits_Ring.png",   
            "True", Null(),             
            ),            
        (260,-350), "Mystique_Kitty_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/KittySex/Kitty_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Mystique_Kitty_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "K_Tan == 'tan' and newgirl['Mystique'].LegsUp", "images/KittySex/Kitty_Sex_TLegs_LegsUp.png",
            "K_Tan == 'tan'", "images/KittySex/Kitty_Sex_TLegs.png",                                              #Legs Base                                                      #Legs Base
            "K_Tan == 'tan2' and newgirl['Mystique'].LegsUp", "images/KittySex/Kitty_Sex_T2Legs_LegsUp.png",
            "K_Tan == 'tan2'", "images/KittySex/Kitty_Sex_T2Legs.png",                                            #Legs Base                                                      #Legs Base
            "K_Tan == 'tan3' and newgirl['Mystique'].LegsUp", "images/KittySex/Kitty_Sex_T3Legs_LegsUp.png",
            "K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Legs.png",
            "newgirl['Mystique'].LegsUp", "images/KittySex/Kitty_Sex_Legs_LegsUp.png",
            "True", "images/KittySex/Kitty_Sex_Legs.png",
            ),
            
        (0,0), ConditionSwitch( 
            "newgirl['Mystique'].LegsUp", Null(),
            "newgirl['Mystique'].Water", "images/KittySex/Kitty_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Mystique_Kitty_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Mystique_Kitty_Sex_Pussy",  

        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Kitty_Hotdog_Zero_Anim2",
            "Speed", "Kitty_Hotdog_Zero_Anim1",
            "True", "Kitty_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Kitty_Footcock_Zero_Anim2",
            "Speed", "Kitty_Footcock_Zero_Anim1",
            "True", "Kitty_Footcock_Static",   
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Mystique_Kitty_Sex_Feet",  
            "newgirl['Mystique'].LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Mystique_Kitty_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Mystique_Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"), 
            "True", "Mystique_Kitty_Sex_Feet",            
            ),
        )

image Mystique_Kitty_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Mystique_Kitty_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            #"newgirl['Mystique'].LegsUp", Null(),
            "K_Tan and newgirl['Mystique'].LegsUp", "images/KittySex/Kitty_Sex_TFeet_LegsUp.png",
            "newgirl['Mystique'].LegsUp", "images/KittySex/Kitty_Sex_Feet_LegsUp.png",
            "K_Tan", "images/KittySex/Kitty_Sex_TFeet.png",                                                         #Legs Base
            "True", "images/KittySex/Kitty_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/KittySex/Kitty_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        )

image Mystique_Kitty_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Kitty_Sex_Body            
    "Mystique_Kitty_HairBack"
    zoom 1.5
    anchor (0.5,0.5)   
    rotate -10   

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

image Mystique_Kitty_Head_Sex:
    # The head used for the sex pose, referenced by Kitty_Sex_Body
    "Mystique_Kitty_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10
    
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
    
image Mystique_Kitty_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Kitty_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Kitty_Anal_Tip", 
            "newgirl['Mystique'].Loose", "images/KittySex/Kitty_Sex_Hole_Loose.png",   
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Kitty_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Kitty_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",  
                )  
  
image Mystique_Kitty_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed and K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Pussy_Closed.png",
                "P_Sprite and P_Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                "Trigger == 'lick pussy' and K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "True and K_Tan == 'tan3'", "images/KittySex/Kitty_Sex_T3Pussy_Closed.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                )    
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not newgirl['Mystique'].Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains: 
            #ring piercing
            ConditionSwitch(  
                "K_Pierce != 'ring'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                ) 
    contains: 
            #barbell piercing
            ConditionSwitch(  
                "K_Pierce != 'barbell'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )  
    contains:
            # pubes
            ConditionSwitch(    
                "not newgirl['Mystique'].Pubes", Null(),         
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and K_HairColor == 'black'", "images/KittySex/Kitty_Sex_PubesBlack_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed and K_HairColor == 'black'", "images/KittySex/Kitty_Sex_PubesBlack_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "P_Sprite and P_Cock == 'in' and K_HairColor == 'black'", "images/KittySex/Kitty_Sex_PubesBlack_Closed.png", 
                "P_Sprite and P_Cock == 'in'", "images/KittySex/Kitty_Sex_Pubes_Closed.png", 
                "Trigger == 'lick pussy' and K_HairColor == 'black'", "images/KittySex/Kitty_Sex_PubesBlack_Open.png", 
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_Sex_Pubes_Open.png", 
                "True and K_HairColor == 'black'", "images/KittySex/Kitty_Sex_PubesBlack_Closed.png",
                "True", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in newgirl['Mystique'].Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not P_Sprite", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "P_Sprite and P_Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Kitty_Pussy_Spunk_Heading",   
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",  
                )  
    #End Kitty Pussy composite
# End Kitty Section / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Common Section ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
image Mystique_Common_Sex_Body_Static:
    contains:
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
    pos (650,230)
            
image Mystique_Common_Sex_Legs_Static:
    contains:
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
    pos (650,230)

#Start Animations for Common's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Mystique_Common_Hotdog_Body_Anim2:
        #this is the animation for Emma's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat 

image Mystique_Common_Sex_Body_Anim1:
        #this is the animation for Emma's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat 
            
image Mystique_Common_Sex_Body_Anim2:
        #this is the animation for Emma's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat 
            
image Mystique_Common_Sex_Body_Anim3:
        #this is the animation for Emma's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,10)
                repeat 
#End Animations for Common's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /            


#Start Animations for Common's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Mystique_Common_Hotdog_Legs_Anim2:
        #this is the animation for Emma's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat 

image Mystique_Common_Sex_Legs_Anim1:
        #this is the animation for Emma's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Mystique_Common_Sex_Legs_Anim2:
        #this is the animation for Emma's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Mystique_Common_Sex_Legs_Anim3:
        #this is the animation for Emma's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,0)
                repeat 
#End Animations for Common's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Common's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
image Mystique_Common_Sex_Body_FootAnim1:
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-25)#(0,-5)
                ease .25 pos (0,-15)#(0,0)
                pause 1
                ease 2.50 pos (0,15)#(0,5)
                repeat 
        pos (750,230)
  
image Mystique_Common_Sex_Body_FootAnim2:
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 pos (0,-25)#(0,-5)
                ease .2 pos (0,-15)#(0,0)
                pause .2
                ease 1.0 pos (0,15)#(0,5)
                repeat 
        pos (750,230)
                
image Mystique_Common_Sex_Body_FootAnimStatic:
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Body",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Body",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
#End Animations for Common's Body during Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Common's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Mystique_Common_Sex_Legs_FootAnim1:
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-65)
                ease .25 pos (0,-60)
                pause 1
                ease 2.50 pos (0,25)#(0,10)
                repeat 
        pos (750,230)
                
image Mystique_Common_Sex_Legs_FootAnim2:
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 pos (0,-65)
                ease .2 pos (0,-60)
                pause .2
                ease 1.0 pos (0,25)#(0,10)
                repeat 
        pos (750,230)
                
image Mystique_Common_Sex_Legs_FootAnimStatic:
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            ConditionSwitch(          
            #"newgirl['Mystique'].LooksLike == 'Mystique'", "Mystique_Blue_SexSprite",
            "newgirl['Mystique'].LooksLike == 'Emma'", "Mystique_Emma_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Rogue'", "Mystique_Rogue_Sex_Legs",
            "newgirl['Mystique'].LooksLike == 'Kitty'", "Mystique_Kitty_Sex_Legs",
            #"True", "Mystique_Blue_SexSprite",
            ),
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
#End Animations for Common's Legs during Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
