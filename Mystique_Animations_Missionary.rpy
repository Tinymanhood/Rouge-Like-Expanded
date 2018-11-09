# Mystique Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Mystique_Blue_SexSprite:            
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Hotdog_Body_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Sex_Body_FootAnimStatic",
            "True", "Mystique_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Mystique_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Mystique_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Mystique_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Mystique_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Mystique_Hotdog_Legs_Anim2",
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Mystique_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Mystique_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Mystique_Sex_Legs_FootAnimStatic",
            "True", "Mystique_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Mystique_Sex_Body_Static:
    contains:
            "Mystique_Sex_Body"
    pos (650,230)
            
image Mystique_Sex_Legs_Static:
    contains:
            "Mystique_Sex_Legs"
    pos (650,230)

image Mystique_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Mystique_SexSprite
        (1120,840),
        #(350,-275), "Mystique_HairBack_Sex",    #(260,-350)   (402 -200 with 0 rotation)                                                                                #Hair underlayer
        (350,-275), "Mystique_HairBack_Sex",
        (0,0), ConditionSwitch(                                                                                 #Body Base
        #     "E_Pierce == 'barbell'", "images/MystiqueSex/Mystique_Sex_Body_Barbell.png",   
        #     "E_Pierce == 'ring'", "images/MystiqueSex/Mystique_Sex_Body_Ring.png",   
            "True", "images/MystiqueSex/Mystique_Sex_Body.png",             
            ), 
        # (0,0), ConditionSwitch(                                                                                 #necklace
        #     "newgirl['Mystique'].Neck == 'black choker'", "images/MystiqueSex/Mystique_Sex_Choker_Black.png",
        #     "newgirl['Mystique'].Neck == 'choker'", "images/MystiqueSex/Mystique_Sex_Choker_White.png",
        #     "newgirl['Mystique'].Neck == 'NewX'", "images/MystiqueSex/Mystique_Sex_New_NeckX_White.png",
        #     "newgirl['Mystique'].Neck == 'black NewX'", "images/MystiqueSex/Mystique_Sex_New_NeckX_Black.png",
        #     "True", Null(),
        #     ),  
        (350,-275), "Mystique_Head_Sex_2",  #check positioning (400,-300)
        # (0,0), ConditionSwitch(                                                                                 #gloves
        #     "E_Arms == 'black gloves'", "images/MystiqueSex/Mystique_Sex_Gloves_Black.png",
        #     "E_Arms == 'white gloves'", "images/MystiqueSex/Mystique_Sex_Gloves_White.png",
        #     "True", Null(),
        #     ), 
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not newgirl['Mystique'].Chest", Null(),        
        #     "E_Chest == 'cami'", "images/MystiqueSex/Mystique_Sex_Under_Cami.png",
        #     "E_Chest == 'sports bra'", "images/MystiqueSex/Mystique_Sex_Under_SportsBra.png",
        #     "E_Chest == 'bra'", "images/MystiqueSex/Mystique_Sex_Under_Bra.png",
            "newgirl['Mystique'].Chest == 'bra'", "images/MystiqueSex/Mystique_Sex_Under_Bra.png",
            # "E_Chest == 'black corset'", "images/MystiqueSex/Mystique_Sex_Corset_Black.png",
            # "E_Chest == 'corset'", "images/MystiqueSex/Mystique_Sex_Corset_White.png",
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/MystiqueSex/Mystique_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
        # (0,0), ConditionSwitch(                                                                                 #Overshirt
        #     "not newgirl['Mystique'].Over", Null(),
        #     "E_Over == 'pink top'", "images/MystiqueSex/Mystique_Sex_Over_PinkShirt.png",           
        #     "E_Over == 'red shirt'", "images/MystiqueSex/Mystique_Sex_Over_RedShirt.png",   
        #     "E_Over == 'towel'", "images/MystiqueSex/Mystique_Sex_Over_Towel.png",       
        #     "True", Null(), 
        #     ),  
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/MystiqueSex/Mystique_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Mystique_Sex_HairBack:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(                                                                         #Hair
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSprite/Mystique_hair_basic.png",
            "True", Null(), 
            ),   

        )                
    anchor (0.6, 0.0)                
    zoom .75 

image Mystique_Sex_Head:
    LiveComposite(
        (555,673), 
        #(0,0), ConditionSwitch(       
        #    "(E_Hair == 'wet' or E_Water) and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_Red.png",
        #    "(E_Hair == 'wet' or E_Water) and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairbackWet_White.png",
        #    "(E_Hair == 'wet' or E_Water) and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackbackWet.png",
        #    "E_Hair == 'wet' or E_Water", "images/EmmaSprite/EmmaSprite_Head_HairbackWet.png",
        #    "E_Hair and E_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hairback_Red.png",   
        #    "E_Hair and E_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hairback_White.png",   
        #    "E_Hair and E_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackback.png",   
        #    "E_Hair", "images/EmmaSprite/EmmaSprite_Head_Hairback.png",   
        #    "True", Null(),        
        #    ),
        (0,0), ConditionSwitch(                                                                         #head 
            #"renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/MystiqueSprite/Mystique_head_base.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #brows
            # "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            # "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            # "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            # "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            # "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/MystiqueSprite/Mystique_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/MystiqueSprite/Mystique_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/MystiqueSprite/Mystique_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/MystiqueSprite/Mystique_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/MystiqueSprite/Mystique_brows_confused.png",
            "True", "images/MystiqueSprite/Mystique_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(                                                                         #Blush
#            "R_Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), "Mystique Blink",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "newgirl['Mystique'].Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                         #Hair
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSex/Mystique_sex_hair_front.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/MystiqueSprite/Mystique_mouth_tongue.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "Speed == 3 and Trigger == 'blow'", "images/MystiqueSprite/Mystique_bj_mouth2.png", #sucking
            "Speed == 4 and Trigger == 'blow'", "images/MystiqueSprite/Mystique_bj_mouth2.png", #deepthroat   
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueSprite/Mystique_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueSprite/Mystique_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueSprite/Mystique_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueSprite/Mystique_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueSprite/Mystique_mouth_smile_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueSprite/Mystique_mouth_tongue_w.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/MystiqueSprite/Mystique_mouth_lipbite_w.png",      
            "newgirl['Mystique'].Mouth == 'normal'", "images/MystiqueSprite/Mystique_mouth_normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueSprite/Mystique_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueSprite/Mystique_mouth_sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueSprite/Mystique_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueSprite/Mystique_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueSprite/Mystique_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueSprite/Mystique_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueSprite/Mystique_mouth_tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/MystiqueSprite/Mystique_mouth_grimace.png",          
            "True", "images/MystiqueSprite/Mystique_mouth_normal.png",
            ),
        # (0,0), ConditionSwitch(                                                                         #Mouth spunk               
        #     "'mouth' not in E_Spunk", Null(),
        #     "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
        #     "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
        #     "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
        #     ), 
        (0,0), ConditionSwitch(                                                                         #facial spunk               
            "'facial' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        # (0,0), ConditionSwitch(                                                                         #Hair Water
        #     "not E_Water", Null(),
        #     "E_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
        #     "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
        #     ),
        (0,0), ConditionSwitch(                                                                         #hair spunk               
            "'hair' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .75 

image Mystique_Head_Sex_2:
    "Mystique_Sex_Head"
    # #zoom .75
    # zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 1.9
    pos (175,-110)
    offset (-230, 30)

# image Mystique_Hair_Back_Sex_2:
#     "Mystique_BJ_Head"
#     # #zoom .75
#     # zoom 4.05
#     # pos (275,-110)
#     # offset (-240, -200) #-140 - 125
#     zoom 1.9
#     pos (175,-110)
#     offset (-230, 30)

image Mystique_Head_Sex:
    # The head used for the sex pose, referenced by Mystique_Sex_Body
    "Mystique_Sex_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate 5
    xzoom -1
    
image Mystique_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Mystique_Sex_Body            
    "Mystique_Sex_HairBack"
    zoom 1.9
    pos (175,-110)
    offset (-230, 30)



#image Mystique_Sex_Legs = LiveComposite(  
image Mystique_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Mystique_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].LegsUp", "images/MystiqueSex/Mystique_Sex_Legs_LegsUp.png",
            "True", "images/MystiqueSex/Mystique_Sex_Legs.png",
            ),                                                     #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].LegsUp", Null(),
            "newgirl['Mystique'].Water", "images/MystiqueSex/Mystique_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), "Mystique_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Mystique_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "newgirl['Mystique'].PantiesDown", Null(),     
            # "newgirl['Mystique'].Panties == 'bikini'", "images/MystiqueSex/Mystique_Sex_Panty_BikiniBottom_White.png",          
            # "newgirl['Mystique'].Panties == 'white panties'", "images/MystiqueSex/Mystique_Sex_Panty_White.png",          
            # "newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueSex/Mystique_Sex_Panty_Black.png",    
            "True", Null(),                     
            ),  
        # (0,0), ConditionSwitch(                                                                                 #Legs Layer
        #     "E_Upskirt", Null(),                               
        #     "E_Legs == 'capris' and newgirl['Mystique'].Wet > 1", "images/MystiqueSex/Mystique_Sex_Pants_Blue_Wet.png",
        #     "E_Legs == 'capris'", "images/MystiqueSex/Mystique_Sex_Pants_Blue.png",
        #     "E_Legs == 'black jeans' and newgirl['Mystique'].Wet > 1", "images/MystiqueSex/Mystique_Sex_Pants_BlacE_Wet.png",
        #     "E_Legs == 'black jeans'", "images/MystiqueSex/Mystique_Sex_Pants_Black.png",
        #     "E_Legs == 'shorts' and newgirl['Mystique'].Wet > 1", "images/MystiqueSex/Mystique_Sex_Shorts_Wet.png",
        #     "E_Legs == 'shorts'", "images/MystiqueSex/Mystique_Sex_Shorts.png",
        #     "E_Legs == 'yoga pants' and newgirl['Mystique'].Wet > 1", "images/MystiqueSex/Mystique_Sex_Pants_Yoga_Wet.png",
        #     "E_Legs == 'yoga pants'", "images/MystiqueSex/Mystique_Sex_Pants_Yoga.png",
        #     "True", Null(),                      
        #     ),   
        # (0,0), ConditionSwitch(                                                                                 #Over Layer
        #     "E_Over == 'towel'", "images/MystiqueSex/Mystique_Sex_Towel_Legs.png",
        #     "True", Null(),                    
        #     ),   
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/MystiqueSex/Mystique_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Mystique_Hotdog_Zero_Anim2",
            "Speed", "Mystique_Hotdog_Zero_Anim1",
            "True", "Mystique_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Mystique_Footcock_Zero_Anim2",
            "Speed", "Mystique_Footcock_Zero_Anim1",
            "True", "Mystique_Footcock_Static",   
            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Mystique_Sex_Feet",  
            "newgirl['Mystique'].LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Mystique_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Mystique_Sex_Feet", "images/MystiqueSex/Mystique_Sex_FeetMask.png"), 
            "True", "Mystique_Sex_Feet",            
            ),
        )
    
image Mystique_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Mystique_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            "newgirl['Mystique'].LegsUp", "images/MystiqueSex/Mystique_Sex_Feet_LegsUp.png",
            "True", "images/MystiqueSex/Mystique_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/MystiqueSex/Mystique_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        # (0,0), ConditionSwitch(                                                                                 #Legs Layer
        #     "E_Upskirt", Null(),                               
        #     "E_Legs == 'capris'", "images/MystiqueSex/Mystique_Sex_Feet_Blue.png",
        #     "E_Legs == 'black jeans'", "images/MystiqueSex/Mystique_Sex_Feet_Black.png",
        #     "E_Legs == 'yoga pants'", "images/MystiqueSex/Mystique_Sex_Feet_Yoga.png",
        #     "True", Null(),                      
        #     ),   
        )
           
image TestingSolid:
        #this is a blank solid I use to test things.
        contains:
            Solid("#75d7ec", xysize=(1500,1500))
            alpha 0.2
            
#Start Animations for Mystique's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Mystique_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "images/MystiqueSex/Mystique_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not newgirl['Mystique'].Pubes", Null(),         
                "True", "images/MystiqueSex/Mystique_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Sex_Zero_Anim0", "Mystique_Pussy_Open_Mask") 
            
image Mystique_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "images/MystiqueSex/Mystique_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not newgirl['Mystique'].Pubes", Null(),         
                "True", "images/MystiqueSex/Mystique_Sex_Pubes_Open.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Sex_Zero_Anim1", "Mystique_Pussy_Open_Mask") 

image Mystique_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/MystiqueSex/Mystique_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not newgirl['Mystique'].Pubes", Null(),         
                "True", "images/MystiqueSex/Mystique_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Sex_Zero_Anim2", "Mystique_Pussy_Fucking_Mask") 

image Mystique_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/MystiqueSex/Mystique_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(             
                "not newgirl['Mystique'].Pubes", Null(),         
                "True", "images/MystiqueSex/Mystique_Sex_Pubes_Fucking.png",  
                ),  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Sex_Zero_Anim3", "Mystique_Pussy_Fucking_Mask") 
            
image Mystique_Pussy_Fucking_Mask:
        #This is the mask image for Mystique's wide open pussy
        contains:
            "images/MystiqueSex/Mystique_Sex_Pussy_Mask.png"   

image Mystique_Pussy_Open_Mask:                
        #This is the mask image for Mystique's wide open pussy
        contains:
            "images/MystiqueSex/Mystique_Sex_Pussy_Mask.png"  
            yoffset 3            

image Mystique_Pussy_Spunk_Heading:                
    "images/MystiqueSex/Mystique_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
            
image Mystique_Sex_Pussy:            
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/MystiqueSex/Mystique_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/MystiqueSex/Mystique_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/MystiqueSex/Mystique_Sex_Pussy_Closed.png",    
                "Trigger == 'lick pussy'", "images/MystiqueSex/Mystique_Sex_Pussy_Open.png",   
                "True", "images/MystiqueSex/Mystique_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not newgirl['Mystique'].Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/MystiqueSex/Mystique_Sex_WetPussy_F.png",
                "True", "images/MystiqueSex/Mystique_Sex_WetPussy_C.png",
                )
    # contains: 
    #         #ring piercing
    #         ConditionSwitch(  
    #             "E_Pierce != 'ring'", Null(),
    #             "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/MystiqueSex/Mystique_Sex_Pussy_Ring.png",
    #             "True", "images/MystiqueSex/Mystique_Sex_Pussy_RingF.png",
    #             ) 
    # contains: 
    #         #barbell piercing
    #         ConditionSwitch(  
    #             "E_Pierce != 'barbell'", Null(),
    #             "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/MystiqueSex/Mystique_Sex_Pussy_Barbell.png",
    #             "True", "images/MystiqueSex/Mystique_Sex_Pussy_BarbellF.png",
    #             )             
    contains:
            # pubes
            ConditionSwitch(    
                "not newgirl['Mystique'].Pubes", Null(),         
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/MystiqueSex/Mystique_Sex_Pubes_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/MystiqueSex/Mystique_Sex_Pubes_Open.png",
                "P_Sprite and P_Cock == 'in'", "images/MystiqueSex/Mystique_Sex_Pubes_Closed.png", 
                "Trigger == 'lick pussy'", "images/MystiqueSex/Mystique_Sex_Pubes_Open.png", 
                "True", "images/MystiqueSex/Mystique_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in newgirl['Mystique'].Spunk", "images/MystiqueSex/Mystique_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not P_Sprite", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 3", AlphaMask("Mystique_Sex_Zero_Anim3", "Mystique_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("Mystique_Sex_Zero_Anim2", "Mystique_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("Mystique_Sex_Zero_Anim1", "Mystique_Pussy_Open_Mask"),
                "P_Sprite and P_Cock == 'in'", AlphaMask("Mystique_Sex_Zero_Anim0", "Mystique_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Mystique_Pussy_Spunk_Heading",   
                "True", "images/MystiqueSex/Mystique_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Mystique Pussy composite
            
#End Animations for Mystique's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Mystique_Sex_Zero_Anim0:
        #this is Mystique's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Mystique_Sex_Zero_Anim1:
        #this is Mystique's sex animation, Speed 1 (heading)
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
            
image Mystique_Sex_Zero_Anim2:
        #this is Mystique's sex animation, Speed 2 (slow)
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
            
image Mystique_Sex_Zero_Anim3:
        #this is Mystique's sex animation, Speed 3 (fast)
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

#Start Animations for Mystique's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Mystique_Sex_Legs_Anim1:
        #this is the animation for Mystique's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Mystique_Sex_Legs_Anim2:            
        #this is the animation for Mystique's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Mystique_Sex_Legs_Anim3:
        #this is the animation for Mystique's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,0)
                repeat 
#End Animations for Mystique's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Mystique's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Mystique_Sex_Body_Anim1:
        #this is the animation for Mystique's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Mystique_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat 
            
image Mystique_Sex_Body_Anim2:            
        #this is the animation for Mystique's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat 
            
image Mystique_Sex_Body_Anim3:
        #this is the animation for Mystique's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Mystique_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,10)
                repeat 
#End Animations for Mystique's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /            





#Start Animations for Mystique's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Mystique_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/MystiqueSex/Mystique_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/MystiqueSex/Mystique_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Mystique_Anal_Tip", 
            "E_Loose", "images/MystiqueSex/Mystique_Sex_Hole_Loose.png",   
            "True", "images/MystiqueSex/Mystique_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/MystiqueSex/Mystique_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Mystique_Anal_Spunk_Heading_Under",
                "True", "images/MystiqueSex/Mystique_Sex_Spunk_Anal_Closed.png",  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Mystique_Anal_Zero_Anim3", "Mystique_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Mystique_Anal_Zero_Anim2", "Mystique_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Mystique_Anal_Zero_Anim1", "Mystique_Anal_Fucking_Mask"),
            "True", AlphaMask("Mystique_Anal_Zero_Anim0", "Mystique_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in newgirl['Mystique'].Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Mystique_Anal_Spunk_Heading_Over",
                "True", "images/MystiqueSex/Mystique_Sex_Spunk_Anal_Over.png",  
                )  
            
                
image Mystique_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "Mystique_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Anal_Zero_Anim0", "Mystique_Anal_Fucking_Mask") 
            
image Mystique_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "Mystique_Anal_Heading"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Anal_Zero_Anim1", "Mystique_Anal_Fucking_Mask") 

image Mystique_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow). 
    contains:
            # The background plate of her pussy
            "images/MystiqueSex/Mystique_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Anal_Zero_Anim2", "Mystique_Anal_Fucking_Mask") 
            
image Mystique_Anal_Fucking3:  
    # This is the visual for her pussy during the Speed 3 mode (fast). 
    contains:
            # The background plate of her pussy
            "images/MystiqueSex/Mystique_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Mystique_Anal_Zero_Anim3", "Mystique_Anal_Fucking_Mask") 
            
image Mystique_Anal_Fucking_Mask:
        #This is the mask image for Mystique's wide open pussy
        contains:
            "images/MystiqueSex/Mystique_Sex_Hole_Mask.png"               

image Mystique_Anal_Open_Mask:            
        #This is the mask image for Mystique's wide open pussy
        contains:
            "images/MystiqueSex/Mystique_Sex_Hole_Mask.png"  
            yoffset 3

image Mystique_Anal_Heading:                
    "images/MystiqueSex/Mystique_Sex_Hole_Open.png"
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

image Mystique_Anal_Spunk_Heading_Over:                
    "images/MystiqueSex/Mystique_Sex_Spunk_Anal_Over.png"
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

image Mystique_Anal_Spunk_Heading_Under:                
    "images/MystiqueSex/Mystique_Sex_Spunk_Anal_Under.png"
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

image Mystique_Anal_Tip:                
    "images/MystiqueSex/Mystique_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
            
#End Animations for Mystique's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Mystique_Anal_Zero_Anim0:
        #this is Mystique's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Mystique_Anal_Zero_Anim1:
        #this is Mystique's sex animation, Speed 1 (heading)
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
            
image Mystique_Anal_Zero_Anim2:
        #this is Mystique's sex animation, Speed 2 (slow)
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
            
image Mystique_Anal_Zero_Anim3:
        #this is Mystique's sex animation, Speed 3 (fast)
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
image Mystique_Hotdog_Zero_Anim0:
        #this is Mystique's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4
            
image Mystique_Hotdog_Zero_Anim1:
        #this is Mystique's sex animation, Speed 1 (heading)
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

image Mystique_Hotdog_Zero_Anim2:
        #this is Mystique's sex animation, Speed 3 (fast)
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

image Mystique_Hotdog_Body_Anim2:
        #this is the animation for Mystique's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Mystique_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat 
                
image Mystique_Hotdog_Legs_Anim2:
        #this is the animation for Mystique's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat 
                
#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Mystique's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Mystique_Footcock:   
    contains:
            subpixel True
            "Blowcock"
            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Mystique_Footcock_Static:    
    contains:
            subpixel True
            "Mystique_Footcock"
            pos (392,295)
    pos (750,230)
                
image Mystique_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Mystique_Footcock"
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
              
image Mystique_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Mystique_Footcock"
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

transform Mystique_Footcock_Zero_Anim1A():
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
                
transform Mystique_Footcock_Zero_Anim2A():
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
                
transform Mystique_Footcock_StaticA():  
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat 
            
image Mystique_Sex_Legs_FootAnim1:            
        #this is the animation for Mystique's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
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
                
image Mystique_Sex_Legs_FootAnim2:            
        #this is the animation for Mystique's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
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
                
image Mystique_Sex_Legs_FootAnimStatic:            
        #this is the animation for Mystique's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
           
transform Mystique_Sex_Legs_FootAnim1A():            
        #this is the animation for Mystique's lower body during Footjobs, Speed 2 (slow)
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
                
transform Mystique_Sex_Legs_FootAnim2A():            
        #this is the animation for Mystique's lower body during Footjobs, Speed 2 (slow)
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
                
transform Mystique_Sex_Legs_FootAnimStaticA():            
        #this is the animation for Mystique's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
                
#End Animations for Mystique's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Mystique's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
image Mystique_Sex_Body_FootAnim1:            
        #this is the animation for Mystique's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Body"
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
  
image Mystique_Sex_Body_FootAnim2:            
        #this is the animation for Mystique's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Body"
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
                
image Mystique_Sex_Body_FootAnimStatic:            
        #this is the animation for Mystique's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Mystique_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
 
transform Mystique_Sex_Body_FootAnim1A():            
        #this is the animation for Mystique's upper body during Footjobs, Speed 2 (slow)
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
  
transform Mystique_Sex_Body_FootAnim2A():            
        #this is the animation for Mystique's upper body during Footjobs, Speed 2 (slow)
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
                
transform Mystique_Sex_Body_FootAnimStaticA():            
        #this is the animation for Mystique's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat 
#End Animations for Mystique's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Mystique_Sex_Launch(Line = "solo"): 
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
    if renpy.showing("Mystique_SexSprite"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Mystique_Sprite  
    show Mystique_SexSprite zorder 150        
    with dissolve
    return
    
label Mystique_Sex_Reset:
    if not renpy.showing("Mystique_SexSprite") and not renpy.showing("Mystique_Doggy"):
        return
    #$ newgirl["Mystique"].Girl_Arms = 2  
    #$ newgirl["Mystique"].LooksLike = "Mystique"
    #if P_Focus >= 100:
    #    "You lose control of your powers and Mystique turns back into her original form"
    #else:
    #    "Mystique turns back into her original form"
    if renpy.showing("Mystique_SexSprite"):
        hide Mystique_SexSprite
    elif renpy.showing("Mystique_Doggy"):
        hide Mystique_Doggy
    
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
    
# End Mystique Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
