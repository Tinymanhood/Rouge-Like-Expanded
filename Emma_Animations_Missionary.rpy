# Emma Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Emma_SexSprite:            
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Emma_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Emma_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Emma_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Emma_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Emma_Hotdog_Body_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Emma_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Emma_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Emma_Sex_Body_FootAnimStatic",
            "True", "Emma_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Emma_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Emma_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Emma_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Emma_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Emma_Hotdog_Legs_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Emma_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Emma_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Emma_Sex_Legs_FootAnimStatic",
            "True", "Emma_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Emma_Sex_Body_Static:
    contains:
            "Emma_Sex_Body"
    pos (650,230)
            
image Emma_Sex_Legs_Static:
    contains:
            "Emma_Sex_Legs"
    pos (650,230)

image Emma_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),
        (350,-275), "Emma_HairBack_Sex",    #(260,-350)   (402 -200 with 0 rotation)                                                                                #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
        #     "E_Pierce == 'barbell'", "images/EmmaSex/Emma_Sex_Body_Barbell.png",   
        #     "E_Pierce == 'ring'", "images/EmmaSex/Emma_Sex_Body_Ring.png",   
            "True", "images/EmmaSex/Emma_Sex_Body.png",             
            ), 
        (0,0), ConditionSwitch(                                                                                 #necklace
            "E_Neck == 'black choker'", "images/EmmaSex/Emma_Sex_Choker_Black.png",
            "E_Neck == 'choker'", "images/EmmaSex/Emma_Sex_Choker_White.png",
            "E_Neck == 'NewX'", "images/EmmaSex/Emma_Sex_New_NeckX_White.png",
            "E_Neck == 'black NewX'", "images/EmmaSex/Emma_Sex_New_NeckX_Black.png",
            "True", Null(),
            ),             
        (350,-275), "Emma_Head_Sex",  #check positioning (400,-300)
        (0,0), ConditionSwitch(                                                                                 #gloves
            "E_Arms == 'black gloves'", "images/EmmaSex/Emma_Sex_Gloves_Black.png",
            "E_Arms == 'white gloves'", "images/EmmaSex/Emma_Sex_Gloves_White.png",
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not E_Chest", "images/EmmaSex/Emma_Sex_Tits_Bare.png",        
        #     "E_Chest == 'cami'", "images/EmmaSex/Emma_Sex_Under_Cami.png",
        #     "E_Chest == 'sports bra'", "images/EmmaSex/Emma_Sex_Under_SportsBra.png",
        #     "E_Chest == 'bra'", "images/EmmaSex/Emma_Sex_Under_Bra.png",
            "E_Chest == 'bikini'", "images/EmmaSex/Emma_Sex_BikiniTop_White.png",
            "E_Chest == 'black corset'", "images/EmmaSex/Emma_Sex_Corset_Black.png",
            "E_Chest == 'corset'", "images/EmmaSex/Emma_Sex_Corset_White.png",
            "True", "images/EmmaSex/Emma_Sex_Tits_Bare.png",
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_Water", "images/EmmaSex/Emma_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not E_Over", Null(),
            "E_Over == 'jacket'", "images/EmmaSex/Emma_Sex_Jacket_White.png",           
            "E_Over == 'black jacket'", "images/EmmaSex/Emma_Sex_Jacket_Black.png",           
            # "E_Over == 'red shirt'", "images/EmmaSex/Emma_Sex_Over_RedShirt.png",   
            # "E_Over == 'towel'", "images/EmmaSex/Emma_Sex_Over_Towel.png",       
            "True", Null(), 
            ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in E_Spunk", "images/EmmaSex/Emma_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Emma_Sex_HairBack:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(       
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_Red.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_White.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackbackWet.png",
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairbackWet.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hairback_Red.png",   
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hairback_White.png",   
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackback.png",   
            "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hairback.png",   
            "True", Null(),        
            ),
        )
    anchor (0.6, 0.0)                
    zoom .48 

image Emma_Sex_Head:
    LiveComposite(
        (555,673), 
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
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "Speed == 3 and Trigger == 'blow'", "images/EmmaSprite/Emma_bj_mouth.png", #sucking
            "Speed == 4 and Trigger == 'blow'", "images/EmmaSprite/Emma_bj_mouth.png", #deepthroat         
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
            #"E_Brows == 'normal' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"E_Brows == 'normal' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "E_Brows == 'normal' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "E_Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            #"E_Brows == 'angry' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_White.png",
            #"E_Brows == 'angry' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_Red.png",
            "E_Brows == 'angry' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "E_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            #"E_Brows == 'sad' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_White.png",
            #"E_Brows == 'sad' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_Red.png",
            "E_Brows == 'sad' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "E_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            #"E_Brows == 'surprised' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_White.png",        
            #"E_Brows == 'surprised' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_Red.png",        
            "E_Brows == 'surprised' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "E_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            #"E_Brows == 'confused' and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_White.png",
            #"E_Brows == 'confused' and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_Red.png",
            "E_Brows == 'confused' and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "E_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            #"True and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"True and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "True and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in E_Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            "not E_Hair", Null(),
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairWet_White.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairWet_Red.png",
            "(E_Hair == 'wet' or E_Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackWet.png",
            "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hair_White.png",
            "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hair_Red.png",
            "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlack.png",
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
    zoom .48 

image Emma_Head_Sex:
    # The head used for the sex pose, referenced by Emma_Sex_Body
    "Emma_Sex_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate 5
    xzoom -1
    
image Emma_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Emma_Sex_Body            
    "Emma_Sex_HairBack"
    zoom 1.5
    anchor (0.5,0.5)   
    rotate 5         
    xzoom -1

#image Emma_Sex_Legs = LiveComposite(  
image Emma_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Emma_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "E_LegsUp", "images/EmmaSex/Emma_Sex_Legs_LegsUp.png",
            "True", "images/EmmaSex/Emma_Sex_Legs.png",
            ),                                                     #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "E_LegsUp", Null(),  
            "E_Hose == 'white thigh high'", "images/EmmaSex/Emma_Sex_Legs_ThighHighWhite.png",
            "E_Hose == 'black thigh high'", "images/EmmaSex/Emma_Sex_Legs_ThighHighBlack.png",
            "True", Null(),                     
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_LegsUp", Null(),
            "E_Water", "images/EmmaSex/Emma_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Emma_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Emma_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "E_PantiesDown", Null(),     
            "E_Panties == 'bikini'", "images/EmmaSex/Emma_Sex_Panty_BikiniBottom_White.png",          
            "E_Panties == 'white panties'", "images/EmmaSex/Emma_Sex_Panty_White.png",          
            "E_Panties == 'black panties'", "images/EmmaSex/Emma_Sex_Panty_Black.png",    
            "True", Null(),                     
            ),  
        # (0,0), ConditionSwitch(                                                                                 #Legs Layer
        #     "E_Upskirt", Null(),                               
        #     "E_Legs == 'capris' and E_Wet > 1", "images/EmmaSex/Emma_Sex_Pants_Blue_Wet.png",
        #     "E_Legs == 'capris'", "images/EmmaSex/Emma_Sex_Pants_Blue.png",
        #     "E_Legs == 'black jeans' and E_Wet > 1", "images/EmmaSex/Emma_Sex_Pants_BlacE_Wet.png",
        #     "E_Legs == 'black jeans'", "images/EmmaSex/Emma_Sex_Pants_Black.png",
        #     "E_Legs == 'shorts' and E_Wet > 1", "images/EmmaSex/Emma_Sex_Shorts_Wet.png",
        #     "E_Legs == 'shorts'", "images/EmmaSex/Emma_Sex_Shorts.png",
        #     "E_Legs == 'yoga pants' and E_Wet > 1", "images/EmmaSex/Emma_Sex_Pants_Yoga_Wet.png",
        #     "E_Legs == 'yoga pants'", "images/EmmaSex/Emma_Sex_Pants_Yoga.png",
        #     "True", Null(),                      
        #     ),   
        # (0,0), ConditionSwitch(                                                                                 #Over Layer
        #     "E_Over == 'towel'", "images/EmmaSex/Emma_Sex_Towel_Legs.png",
        #     "True", Null(),                    
        #     ),   
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in E_Spunk", "images/EmmaSex/Emma_Sex_Spunk_Pelvis.png",   
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
            "not Speed", "Emma_Sex_Feet",  
            "E_LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Emma_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_FeetMask.png"), 
            "True", "Emma_Sex_Feet",            
            ),
        )
    
image Emma_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Emma_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "E_LegsUp", "images/EmmaSex/Emma_Sex_Feet_LegsUp.png",
            "True", "images/EmmaSex/Emma_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "E_LegsUp and E_Hose == 'white thigh high'", "images/EmmaSex/Emma_Sex_LegsUp_Feet_ThighHighWhite.png",
            "E_LegsUp and E_Hose == 'black thigh high'", "images/EmmaSex/Emma_Sex_LegsUp_Feet_ThighHighBlack.png",
            "E_Hose == 'white thigh high'", "images/EmmaSex/Emma_Sex_Feet_ThighHighWhite.png",
            "E_Hose == 'black thigh high'", "images/EmmaSex/Emma_Sex_Feet_ThighHighBlack.png",
            "True", Null(),                     
            ),
        # (0,0), ConditionSwitch(                                                                                 #Panties back
        #     "not E_LegsUp", Null(),
        #     "E_Hose == 'white thigh high'", "images/EmmaSex/Emma_Sex_LegsUp_Feet_ThighHighWhite.png",
        #     "E_Hose == 'black thigh high'", "images/EmmaSex/Emma_Sex_LegsUp_Feet_ThighHighBlack.png",
        #     "True", Null(),                     
        #     ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_Water", "images/EmmaSex/Emma_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        # (0,0), ConditionSwitch(                                                                                 #Legs Layer
        #     "E_Upskirt", Null(),                               
        #     "E_Legs == 'capris'", "images/EmmaSex/Emma_Sex_Feet_Blue.png",
        #     "E_Legs == 'black jeans'", "images/EmmaSex/Emma_Sex_Feet_Black.png",
        #     "E_Legs == 'yoga pants'", "images/EmmaSex/Emma_Sex_Feet_Yoga.png",
        #     "True", Null(),                      
        #     ),   
        )
           
image TestingSolid:
        #this is a blank solid I use to test things.
        contains:
            Solid("#75d7ec", xysize=(1500,1500))
            alpha 0.2
            
#Start Animations for Emma's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "images/EmmaSex/Emma_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not E_Pubes", Null(),         
                "True", "images/EmmaSex/Emma_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Sex_Zero_Anim0", "Emma_Pussy_Open_Mask") 
            
image Emma_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "images/EmmaSex/Emma_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not E_Pubes", Null(),         
                "True", "images/EmmaSex/Emma_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Sex_Zero_Anim1", "Emma_Pussy_Open_Mask") 

image Emma_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/EmmaSex/Emma_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not E_Pubes", Null(),         
                "True", "images/EmmaSex/Emma_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Sex_Zero_Anim2", "Emma_Pussy_Fucking_Mask") 

image Emma_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/EmmaSex/Emma_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not E_Pubes", Null(),         
                "True", "images/EmmaSex/Emma_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Sex_Zero_Anim3", "Emma_Pussy_Fucking_Mask") 
            
image Emma_Pussy_Fucking_Mask:
        #This is the mask image for Emma's wide open pussy
        contains:
            "images/EmmaSex/Emma_Sex_Pussy_Mask.png"   

image Emma_Pussy_Open_Mask:                
        #This is the mask image for Emma's wide open pussy
        contains:
            "images/EmmaSex/Emma_Sex_Pussy_Mask.png"  
            yoffset 3            

image Emma_Pussy_Spunk_Heading:                
    "images/EmmaSex/Emma_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
            
image Emma_Sex_Pussy:            
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
                "not E_Wet", Null(),  
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
                "not E_Pubes", Null(),         
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/EmmaSex/Emma_Sex_Pubes_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/EmmaSex/Emma_Sex_Pubes_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/EmmaSex/Emma_Sex_Pubes_Closed.png", 
                "Trigger == 'lick pussy'", "images/EmmaSex/Emma_Sex_Pubes_Open.png", 
                "True", "images/EmmaSex/Emma_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in E_Spunk", "images/EmmaSex/Emma_Sex_Spunk_Puss_Under.png",   
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
                "'in' not in E_Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Emma_Pussy_Spunk_Heading",   
                "True", "images/EmmaSex/Emma_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Emma Pussy composite
            
#End Animations for Emma's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sex_Zero_Anim0:
        #this is Emma's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Emma_Sex_Zero_Anim1:
        #this is Emma's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,525) #X less is left, Y less is up(498,520)
            zoom 1.4
            block:
                ease 1 pos (498,510) #(498,500)
                pause 1
                ease 3 pos (498,525)
                repeat 
            
image Emma_Sex_Zero_Anim2:
        #this is Emma's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,380) #(500,470)
                pause 1
                ease 3 pos (500,490)
                repeat 
            
image Emma_Sex_Zero_Anim3:
        #this is Emma's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,380) #(500,470)
                pause .25
                ease 1.5 pos (500,490)
                repeat 
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Emma's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sex_Legs_Anim1:
        #this is the animation for Emma's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Emma_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Emma_Sex_Legs_Anim2:            
        #this is the animation for Emma's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Emma_Sex_Legs_Anim3:
        #this is the animation for Emma's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Emma_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,0)
                repeat 
#End Animations for Emma's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Emma's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sex_Body_Anim1:
        #this is the animation for Emma's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Emma_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat 
            
image Emma_Sex_Body_Anim2:            
        #this is the animation for Emma's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat 
            
image Emma_Sex_Body_Anim3:
        #this is the animation for Emma's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Emma_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,10)
                repeat 
#End Animations for Emma's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /            





#Start Animations for Emma's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/EmmaSex/Emma_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/EmmaSex/Emma_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Emma_Anal_Tip", 
            "E_Loose", "images/EmmaSex/Emma_Sex_Hole_Loose.png",   
            "True", "images/EmmaSex/Emma_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in E_Spunk", Null(),  
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
                "'anal' not in E_Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Emma_Anal_Spunk_Heading_Over",
                "True", "images/EmmaSex/Emma_Sex_Spunk_Anal_Over.png",  
                )  
            
                
image Emma_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "Emma_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Anal_Zero_Anim0", "Emma_Anal_Fucking_Mask") 
            
image Emma_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "Emma_Anal_Heading"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Anal_Zero_Anim1", "Emma_Anal_Fucking_Mask") 

image Emma_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/EmmaSex/Emma_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Anal_Zero_Anim2", "Emma_Anal_Fucking_Mask") 
            
image Emma_Anal_Fucking3:  
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/EmmaSex/Emma_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Emma_Anal_Zero_Anim3", "Emma_Anal_Fucking_Mask") 
            
image Emma_Anal_Fucking_Mask:
        #This is the mask image for Emma's wide open pussy
        contains:
            "images/EmmaSex/Emma_Sex_Hole_Mask.png"               

image Emma_Anal_Open_Mask:            
        #This is the mask image for Emma's wide open pussy
        contains:
            "images/EmmaSex/Emma_Sex_Hole_Mask.png"  
            yoffset 3

image Emma_Anal_Heading:                
    "images/EmmaSex/Emma_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0        
        ease .25 xzoom 0.9
        pause 1.50      
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat 

image Emma_Anal_Spunk_Heading_Over:                
    "images/EmmaSex/Emma_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:
        #total 5 second
        ease .75 xzoom 1.0   #(1.0)     
        pause 1.75      
        ease .25 xzoom 1.0  #(1.0) 
        ease 2.25 xzoom 0.8   #(0.6)
        repeat 

image Emma_Anal_Spunk_Heading_Under:                
    "images/EmmaSex/Emma_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0        
        ease .25 xzoom 0.95
        pause 1.50      
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat 

image Emma_Anal_Tip:                
    "images/EmmaSex/Emma_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
            
#End Animations for Emma's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Anal_Zero_Anim0:
        #this is Emma's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Emma_Anal_Zero_Anim1:
        #this is Emma's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,570) #(500,470)
                pause 1
                ease 3 pos (500,600)
                repeat 
            
image Emma_Anal_Zero_Anim2:
        #this is Emma's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,450) #(500,470)
                pause 1
                ease 3 pos (500,570)
                repeat 
            
image Emma_Anal_Zero_Anim3:
        #this is Emma's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,450) #(500,470)
                pause .25
                ease 1.5 pos (500,570)
                repeat 
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Hotdog_Zero_Anim0:
        #this is Emma's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4
            
image Emma_Hotdog_Zero_Anim1:
        #this is Emma's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,500) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (498,560) #(500,500)
                pause .5
                ease 1.5 pos (498,500)
                repeat 

image Emma_Hotdog_Zero_Anim2:
        #this is Emma's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,510) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .5 pos (500,400) #(500,470)
                pause .5
                ease 1 pos (500,510)
                repeat 

image Emma_Hotdog_Body_Anim2:
        #this is the animation for Emma's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Emma_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat 
                
image Emma_Hotdog_Legs_Anim2:
        #this is the animation for Emma's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Emma_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat 
                
#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Emma's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_Footcock:   
    contains:
            subpixel True
            "Blowcock"
            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Emma_Footcock_Static:    
    contains:
            subpixel True
            "Emma_Footcock"
            pos (392,295)
    pos (750,230)
                
image Emma_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Emma_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 ypos 360#65
                ease .25 ypos 355#60
                pause 1
                ease 2.50 ypos 270#285
                repeat 
    pos (750,230)
              
image Emma_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Emma_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 ypos 360
                ease .2 ypos 355
                pause .2
                ease 1.00 ypos 270
                repeat
    pos (750,230)

transform Emma_Footcock_Zero_Anim1A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset 60#65
                ease .25 yoffset 55#60
                pause 1
                ease 1.50 yoffset -30#285
                repeat 
                
transform Emma_Footcock_Zero_Anim2A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                repeat 
                
transform Emma_Footcock_StaticA():  
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat 
            
image Emma_Sex_Legs_FootAnim1:            
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Legs"
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
                
image Emma_Sex_Legs_FootAnim2:            
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Legs"
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
                
image Emma_Sex_Legs_FootAnimStatic:            
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
           
transform Emma_Sex_Legs_FootAnim1A():            
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -65
                ease .25 yoffset -60
                pause 1
                ease 1.50 yoffset 25
                repeat 
                
transform Emma_Sex_Legs_FootAnim2A():            
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                repeat 
                
transform Emma_Sex_Legs_FootAnimStaticA():            
        #this is the animation for Emma's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
                
#End Animations for Emma's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Emma's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
image Emma_Sex_Body_FootAnim1:            
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Body"
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
  
image Emma_Sex_Body_FootAnim2:            
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Body"
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
                
image Emma_Sex_Body_FootAnimStatic:            
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Emma_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
 
transform Emma_Sex_Body_FootAnim1A():            
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -25
                ease .25 yoffset -15
                pause 1
                ease 1.50 yoffset 15
                repeat 
  
transform Emma_Sex_Body_FootAnim2A():            
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                repeat 
                
transform Emma_Sex_Body_FootAnimStaticA():            
        #this is the animation for Emma's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
#End Animations for Emma's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Emma_Sex_Launch(Line = "solo"): 
    if Line == "sex":        
        $ P_Cock = "in"
    elif Line == "anal":
        $ P_Cock = "anal"
    elif Line == "solo":   
        $ P_Sprite = 0
        $ P_Cock = "out"
    elif Line == "hotdog":          
        $ P_Cock = "out"
    elif Line == "foot":          
        $ P_Cock = "foot"
    if not Trigger:
        $ Trigger = Line
    if renpy.showing("Emma_SexSprite"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Emma_Sprite  
    show Emma_SexSprite zorder 150        
    with dissolve
    return
    
label Emma_Sex_Reset:
    if not renpy.showing("Emma_SexSprite"):
        return
    #$ Emma_Arms = 2     
    hide Emma_SexSprite
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
    
# End Emma Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
