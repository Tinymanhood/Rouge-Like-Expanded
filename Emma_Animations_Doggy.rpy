# Basic character Sprites
# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
image Emma_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Emma_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Emma_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Emma_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Emma_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Emma_Doggy_Fuck_Top",
            "True", "Emma_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Emma_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Emma_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Emma_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Emma_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Emma_Doggy_Fuck_Ass",
            "True", "Emma_Doggy_Ass",            
            ),
        )
    align (0.6,0.0)
    
            
image Emma_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            #"E_Water", Null(), 
            "True", "images/EmmaDoggy/Emma_Doggy_HairBack.png",
            ),   
        #(0,0), ConditionSwitch(                                                                                 #Mouth
        #    "R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGag.png",
        #    "True", Null(), #Rogue_Doggy_BallGag
        #    ),
        (0,0), ConditionSwitch(          
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Body.png",
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Body.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Body.png",
            ),  
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            #"E_Tan", Null(),
            "'mouth' in E_Spunk and E_Gag", "images/EmmaDoggy/Emma_Doggy_Mouth_BlowW.png",
            "E_Gag", "images/EmmaDoggy/Emma_Doggy_Mouth_Blow.png",            
            "'mouth' in E_Spunk and E_Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_Mouth_LipbiteW.png",
            "'mouth' in E_Spunk and E_Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Mouth_SurprisedW.png",
            "'mouth' in E_Spunk and E_Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Mouth_BlowW.png",
            "'mouth' in E_Spunk and E_Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_Mouth_SadW.png",
            "'mouth' in E_Spunk and E_Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Mouth_SmileW.png",   
            "'mouth' in E_Spunk and E_Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Mouth_TongueW.png",  
            "'mouth' in E_Spunk", "images/EmmaDoggy/Emma_Doggy_Mouth_NormalW.png",   
            "E_Mouth == 'normal'", "images/EmmaDoggy/Emma_Doggy_Mouth_Normal.png",
            "E_Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_Mouth_Lipbite.png",
            "E_Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Mouth_Blow.png",            
            "E_Mouth == 'kiss'", "images/EmmaDoggy/Emma_Doggy_Mouth_Surprised.png",
            "E_Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_Mouth_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png",
            "E_Mouth == 'grimace'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png",
            "E_Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Mouth_Surprised.png",       
            "E_Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Mouth_Tongue.png", 
            "True", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png", 
            ),
        # (0,0), ConditionSwitch(                                                                                 #Mouth
        #     "not E_Tan", Null(),
        #     "'mouth' in E_Spunk and E_Gag", "images/EmmaDoggy/Emma_Doggy_T3Mouth_BlowW.png",
        #     "E_Gag", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Blow.png", 
        #     "'mouth' in E_Spunk and E_Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_LipbiteW.png",
        #     "'mouth' in E_Spunk and E_Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_SurprisedW.png",
        #     "'mouth' in E_Spunk and E_Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_BlowW.png",
        #     "'mouth' in E_Spunk and E_Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_SadW.png",
        #     "'mouth' in E_Spunk and E_Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_SmileW.png",   
        #     "'mouth' in E_Spunk and E_Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_TongueW.png",  
        #     "'mouth' in E_Spunk", "images/EmmaDoggy/Emma_Doggy_T3Mouth_NormalW.png",   
        #     "E_Mouth == 'normal'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Normal.png",
        #     "E_Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Lipbite.png",
        #     "E_Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Blow.png",            
        #     "E_Mouth == 'kiss'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Surprised.png",
        #     "E_Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Sad.png",
        #     "E_Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Smile.png",
        #     "E_Mouth == 'grimace'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Smile.png",
        #     "E_Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Surprised.png",       
        #     "E_Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Tongue.png", 
        #     "True", "images/EmmaDoggy/Emma_Doggy_T3Mouth_Smile.png", 
        #     ),
                                                              #Body base
        #(0,0), ConditionSwitch(                                                                                 #Blush
        #    #"R_Blush and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BlushEvoBallGag.png",
        #    "E_Blush", "images/EmmaDoggy/Emma_Doggy_BlushEvo.png",
        #    "True", Null(), 
        #    ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "E_Gag == 'ballgag'", "images/EmmaDoggy/Emma_Doggy_Mouth_Ballgag.png",
            "True", Null(), #Emma_Doggy_Gag
            ),
        (0,0), "Emma Doggy Blink",
        (0,0), ConditionSwitch(                                                                                 #Brows
            "E_Brows == 'normal'", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            "E_Brows == 'angry'", "images/EmmaDoggy/Emma_Doggy_Brows_Angry.png",
            "E_Brows == 'sad'", "images/EmmaDoggy/Emma_Doggy_Brows_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Brows_Surprised.png",        
            "E_Brows == 'confused'", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            ),  
        # (0,0), ConditionSwitch(
        #     "E_Blindfold", "images/EmmaDoggy/Emma_Doggy_Blindfold.png",  
        #     "True", Null(),
        #     ),                                                                             #Eyes
        #(0,0), ConditionSwitch(                                                                                 #Collar
        #    "R_Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
        #    "True", Null(),                #R_Arms == 'gloved' or not R_Arms
        #    ),  
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not E_Chest", Null(),        
            "E_Chest == 'bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniTopWhite.png",
            "E_Chest == 'black bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniTopBlack.png",
            "E_Chest == 'corset'", "images/EmmaDoggy/Emma_Doggy_CorsetWhite.png",
            "E_Chest == 'black corset'", "images/EmmaDoggy/Emma_Doggy_CorsetBlack.png",
            "True", Null(),            
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not E_Over", Null(),
        #    "R_Over == 'mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png",
        #    "R_Over == 'white mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_WhiteMesh.png",
        #    "R_Over == 'blue mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_BlueMesh.png",
        #    "R_Over == 'red mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_RedMesh.png",
        #    "R_Over == 'yellow mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_YellowMesh.png",
        #    "R_Over == 'black mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_BlackMesh.png",           
        #    "R_Over == 'pink top'", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png",
        #    "R_Over == 'red top'", "images/RogueDoggy/Rogue_Doggy_Over_Red.png",             
        #    "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png",
        #    "R_Over == 'blue hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_BHoodie.png",
        #    "R_Over == 'red hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_RHoodie.png",
        #    "R_Over == 'yellow hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_YHoodie.png",
        #    "R_Over == 'black hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_DHoodie.png",
        #    "R_Over == 'white hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_WHoodie.png",           
        #    "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png",         
            "E_Over == 'towel'", "images/EmmaDoggy/Emma_Doggy_Over_TowelTop.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                                 #Hair
            # "E_HairColor == 'black' and E_Hair == 'long'", "images/EmmaDoggy/Emma_Doggy_Hair_Black.png",
            # "E_HairColor == 'black' and E_Hair == 'evo'", "images/EmmaDoggy/Emma_Doggy_Hair_Ponytail_Black.png",
            # "E_Hair == 'long'", "images/EmmaDoggy/Emma_Doggy_Hair.png",
            # "E_Hair == 'evo'", "images/EmmaDoggy/Emma_Doggy_Hair_Ponytail.png",
            "True", "images/EmmaDoggy/Emma_Doggy_HairFront.png",
            ),                    
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not E_Spunk", Null(),
            "'facial' in E_Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
            "True", Null(), 
            ),
        #(0,0), ConditionSwitch(                                                                                 #Hair            
        #    "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png",
        #    "R_Over == 'blue hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_BHood.png",
        #    "R_Over == 'red hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_RHood.png",
        #    "R_Over == 'yellow hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_YHood.png",
        #    "R_Over == 'black hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_DHood.png",
        #    "R_Over == 'white hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_WHood.png", 
        #    "True", Null(),                     
        #    ),  
        )

image Emma_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "not E_PantiesDown or (E_Legs == 'pants' and not E_Upskirt)", Null(),  
            "E_Panties == 'white panties'", "images/EmmaDoggy/Emma_Doggy_PantiesWhite_Back.png",
            "E_Panties == 'black panties'", "images/EmmaDoggy/Emma_Doggy_PantiesBlack_Back.png",
            "E_Panties == 'bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniWhite_Back.png",
            "E_Panties == 'black bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniBlack_Back.png",
            #"E_Panties == 'blue shorts'", "images/EmmaDoggy/Emma_Doggy_Shorts_Back.png",    
            # "E_Panties == 'green panties'", "images/EmmaDoggy/Emma_Doggy_Panties_Down_Back_Green.png",   
            # "E_Panties == 'purple bikini panties'", "images/EmmaDoggy/Emma_Doggy_Panties_Down_Back_Purple.png",   
            #"E_Panties == 'black large panties'", "images/EmmaDoggy/Emma_Doggy_UndiesBlack_Back.png",   
            #"E_Panties == 'lace panties' or E_Panties == 'black panties'", "images/EmmaDoggy/Emma_Doggy_Panties_Back.png",  
            #"E_Panties == 'swimsuit1' or E_Panties == 'swimsuit2'", "images/EmmaDoggy/Emma_Doggy_Swimsuit.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Wet look
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Ass.png",   
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Ass.png",   
            "True", "images/EmmaDoggy/Emma_Doggy_Ass.png",              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "not E_Hose", Null(),  
            "E_Hose == 'white thigh high'", "images/EmmaDoggy/Emma_Doggy_Legs_ThighHighWhite.png",
            "E_Hose == 'black thigh high'", "images/EmmaDoggy/Emma_Doggy_Legs_ThighHighBlack.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "E_Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        #(0,0), ConditionSwitch(                                                                                 #Hose
        #    "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
        #    "True", Null(),
        #    ),             
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "not E_PantiesDown or (E_Legs == 'pants' and not E_Upskirt)", Null(),
        #    "R_Panties == 'shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png",
        #    "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down_Wet.png",
        #    "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down_Wet.png", #fix turn this on when graphics fixed
        #    "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png",
        #    "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down.png",
        #    "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down.png", 
        #    "R_Panties == 'green panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "E_Panties == 'white panties'", "images/EmmaDoggy/Emma_Doggy_PantiesWhite_Down.png",
            "E_Panties == 'black panties'", "images/EmmaDoggy/Emma_Doggy_PantiesBlack_Down.png",
            "E_Panties == 'bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniWhite_Down.png",
            "E_Panties == 'black bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniBlack_Down.png",
        #    "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_UndiesBlacE_Down_Wet.png",
        #    "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlacE_Down.png",  
        #    "R_Panties == 'lace panties' or R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite           
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Emma_Doggy_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Emma_Doggy_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Emma_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Emma_Pussy",    
            # "E_Tan and Trigger == 'lick pussy'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Open.png",   
            # "E_Tan == 'tan3' and Trigger == 'lick pussy'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Open.png",   
            "Trigger == 'lick pussy'", "images/EmmaDoggy/Emma_Doggy_Pussy_Open.png",   
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Closed.png", 
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_Closed.png", 
            "True", "images/EmmaDoggy/Emma_Doggy_Pussy_Closed.png", 
            ),   
        # (0,0), ConditionSwitch(                                                                                 #pubes              
        #    "not E_Pubes", Null(),         
        #    "P_Sprite and P_Cock == 'in'", Null(),
        #    "E_Legs == 'pants' and not E_Upskirt and E_HairColor == 'black'", "images/EmmaDoggy/Emma_Doggy_PubesBlacE_Panties.png",   
        #    "E_Legs == 'pants' and not E_Upskirt and E_HairColor == 'blonde'", "images/EmmaDoggy/Emma_Doggy_PubesBlonde_Panties.png",   
        #    "E_Legs == 'pants' and not E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Pubes_Panties.png",   
        #    "E_PantiesDown and E_HairColor == 'black'", "images/EmmaDoggy/Emma_Doggy_PubesBlack.png",  
        #    "E_PantiesDown and E_HairColor == 'blonde'", "images/EmmaDoggy/Emma_Doggy_PubesBlonde.png",  
        #    "E_PantiesDown", "images/EmmaDoggy/Emma_Doggy_Pubes.png",  
        #    "E_Panties and E_HairColor == 'black'", "images/EmmaDoggy/Emma_Doggy_PubesBlacE_Panties.png",
        #    "E_Panties and E_HairColor == 'blonde'", "images/EmmaDoggy/Emma_Doggy_PubesBlonde_Panties.png",
        #    "E_Panties", "images/EmmaDoggy/Emma_Doggy_Pubes_Panties.png",
        #    "E_Hose and E_Hose != 'stockings' and E_HairColor == 'black'", "images/EmmaDoggy/Emma_Doggy_PubesBlacE_Panties.png",   
        #    "E_Hose and E_Hose != 'stockings' and E_HairColor == 'blonde'", "images/EmmaDoggy/Emma_Doggy_PubesBlonde_Panties.png",   
        #    "E_Hose and E_Hose != 'stockings'", "images/EmmaDoggy/Emma_Doggy_Pubes_Panties.png",   
        #    "True and R_HairColor == 'black'", "images/EmmaDoggy/Emma_Doggy_PubesBlack.png",  
        #    "True and R_HairColor == 'blonde'", "images/EmmaDoggy/Emma_Doggy_PubesBlonde.png",  
        #    "True", "images/EmmaDoggy/Emma_Doggy_Pubes.png",  
        #    ),  
        # (0,0), ConditionSwitch(                                                                                 #Pussy Piercings          
        #     "P_Sprite", Null(),             
        #     "E_Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pussy_Ring.png",            
        #     #"R_Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
        #     "True", Null(),  
        #     ),   
        (0,0), ConditionSwitch(                                                                                 #Anus Composite            
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Emma_Doggy_Anal_Fucking3",         
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Emma_Doggy_Anal_Fucking2",         
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Emma_Doggy_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Emma_Doggy_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Emma_Anal",  
            "P_Sprite and P_Cock == 'plug' and Speed", "Emma_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and E_Plugged", "images/EmmaDoggy/Emma_Doggy_Plugged.png",  
            "P_Sprite and P_Cock == 'plug'", "Emma_Anal_Plug",  
            "E_Plugged", "images/EmmaDoggy/Emma_Doggy_Plugged.png",   
            # "E_Tan and E_Loose", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",   
            # "E_Tan == 'tan3' and E_Loose", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",   
            "E_Loose", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",   
            # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Tight.png", 
            # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Tight.png", 
            "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Tight.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            "E_Spank >= 1 and E_Spank <= 4 and E_Plugged", "images/EmmaDoggy/Emma_Doggy_SpankPlugged1.png",
            "E_Spank >= 1 and E_Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/EmmaDoggy/Emma_Doggy_SpankAnal1.png",
            "E_Spank >= 1 and E_Spank <= 4", "images/EmmaDoggy/Emma_Doggy_Spank1.png",
            "E_Spank >= 5 and E_Spank <= 10 and E_Plugged", "images/EmmaDoggy/Emma_Doggy_SpankPlugged2.png",
            "E_Spank >= 5 and E_Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/EmmaDoggy/Emma_Doggy_SpankAnal2.png",
            "E_Spank >= 5 and E_Spank <= 10", "images/EmmaDoggy/Emma_Doggy_Spank2.png",
            "E_Spank >= 11 and E_Plugged", "images/EmmaDoggy/Emma_Doggy_SpankPlugged3.png",
            "E_Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/EmmaDoggy/Emma_Doggy_SpankAnal3.png",
            "E_Spank >= 11", "images/EmmaDoggy/Emma_Doggy_Spank3.png",
            "True", Null(),
            ),           
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in E_Spunk and P_Sprite", Null(),   
            "'anal' in E_Spunk and P_Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "'anal' in E_Spunk and E_Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "'anal' in E_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "E_PantiesDown", Null(),     
        #    "E_Panties == 'shorts' and E_Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",
        #    "R_Panties == 'red shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_RYShorts_Wet.png",
        #    "R_Panties == 'blue shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_BYShorts_Wet.png",          
        #    "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
        #    "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts.png",
        #    "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts.png",
        #    "E_Panties == 'green panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",          
            "E_Panties == 'white panties'", "images/EmmaDoggy/Emma_Doggy_PantiesWhite.png",
            "E_Panties == 'black panties'", "images/EmmaDoggy/Emma_Doggy_PantiesBlack.png",
            "E_Panties == 'bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniWhite.png",
            "E_Panties == 'black bikini'", "images/EmmaDoggy/Emma_Doggy_BikiniBlack.png",
        #    "R_Panties == 'black large panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_UndiesBlacE_Wet.png",          
        #    "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack.png",          
        #    "R_Panties == 'lace panties'", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png",                      
        #    "R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties.png", 
        #    "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit.png",  
            "True", Null(),                     
            ),  
        #(0,0), ConditionSwitch(                                                                         #full hose/tights  
        #    "P_Sprite and (P_Cock == 'in' or P_Cock == 'anal')", Null(), #fix this at some point, currently it clips tights
        #    "R_PantiesDown", Null(), 
        #    "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
        #    "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",    
        #    "R_Hose == 'tights' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
        #    "R_Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
        #    "R_Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",   
        #    "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
        #    "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
        #    "True", Null(), 
        #    ),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            #"E_Legs == 'capris' and E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Pants_Down.png",            
            #"E_Legs == 'capris' and E_Wet > 1", "images/EmmaDoggy/Emma_Doggy_Legs_Pants_Wet.png",
            #"E_Legs == 'capris'", "images/EmmaDoggy/Emma_Doggy_Legs_Pants.png",
            "E_Legs == 'black pants' and E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Pants_Black_Down.png",            
            "E_Legs == 'black pants' and E_Wet > 1", "images/EmmaDoggy/Emma_Doggy_Pants_Black_Wet.png",
            "E_Legs == 'black pants'", "images/EmmaDoggy/Emma_Doggy_Pants_Black.png",
            "E_Legs == 'pants' and E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Pants_White_Down.png",            
            "E_Legs == 'pants' and E_Wet > 1", "images/EmmaDoggy/Emma_Doggy_Pants_White_Wet.png",
            "E_Legs == 'pants'", "images/EmmaDoggy/Emma_Doggy_Pants_White.png",
        #    "E_Legs == 'skirt' and E_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/EmmaDoggy/Emma_Doggy_Legs_Skirt_UpAnal.png",   
        #    "E_Legs == 'skirt' and E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt_Up.png",   
        #    "E_Legs == 'skirt'", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt.png", 
        #    "E_Legs == 'skirtshort' and E_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/EmmaDoggy/Emma_Doggy_Legs_SkirtShort_UpAnal.png",   
        #    "E_Legs == 'skirtshort' and E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_SkirtShort_Up.png",   
        #    "E_Legs == 'skirtshort'", "images/EmmaDoggy/Emma_Doggy_Legs_SkirtShort.png", 
        #    "E_Legs == 'cheerleader skirt' and E_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/EmmaDoggy/Emma_Doggy_CheerleadeK_Skirt_UpAnal.png",   
        #    "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/EmmaDoggy/Emma_Doggy_Cheerleader_Skirt_Up.png",   
        #    "R_Legs == 'cheerleader skirt'", "images/EmmaDoggy/Emma_Doggy_Cheerleader_Skirt.png", 
        #    "R_Legs == 'cheerleader skirtshort' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/EmmaDoggy/Emma_Doggy_Cheerleader_SkirtShort_UpAnal.png",   
        #    "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/EmmaDoggy/Emma_Doggy_Cheerleader_SkirtShort_Up.png",   
        #    "R_Legs == 'cheerleader skirtshort'", "images/EmmaDoggy/Emma_Doggy_Cheerleader_SkirtShort.png", 
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
        #    "R_Over == 'nighty' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",            
        #    "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            "E_Over == 'towel' and E_Upskirt", "images/EmmaDoggy/Emma_Doggy_Over_TowelAss_Up.png",            
            "E_Over == 'towel'", "images/EmmaDoggy/Emma_Doggy_Over_TowelAss.png",
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in E_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),   
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",  
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png", 
            ),    
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),            
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            #"(R_Legs == 'skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMasE_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),    
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
        (0,0), ConditionSwitch(                                                                                 #UI tool layer
            "not UI_Tool", Null(),   
            "UI_Tool", "Slap_Ass",  
            #"not UI_Tool", "Slap_Ass",  
            "True", Null(),   
            ),   
        )

image Emma Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(          
    "E_Eyes == 'sexy'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",
    "E_Eyes == 'side'", "images/EmmaDoggy/Emma_Doggy_Eyes_Side.png",
    "E_Eyes == 'normal'", "images/EmmaDoggy/Emma_Doggy_Eyes_Normal.png",
    "E_Eyes == 'closed'", "images/EmmaDoggy/Emma_Doggy_Eyes_Closed.png",
    "E_Eyes == 'manic'", "images/EmmaDoggy/Emma_Doggy_Eyes_Surprised.png",
    "E_Eyes == 'down'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",           
    "E_Eyes == 'stunned'", "images/EmmaDoggy/Emma_Doggy_Eyes_Stunned.png",
    "E_Eyes == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Eyes_Surprised.png",
    "E_Eyes == 'squint'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",
    "True", "images/EmmaDoggy/Emma_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    "images/EmmaDoggy/Emma_Doggy_Eyes_Closed.png"
    .25
    repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              #Pussy fucking animations    
image Emma_Pussy:                                                                                              #Full Animation for speed 0    
    contains:  
        "Emma_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png",
        # ),                                                                                 #Base
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (169,460) #Out stroke
    contains:
        "Emma_Doggy_Pussy_FMask"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FMask.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FMask.png",
        # ),                                                                                   #Mask

image Emma_Pussy_Moving:                                                                                       #Full Animation for speed 1
    subpixel True
    contains:                                                                                   #Base
        "Emma_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png",
        # ),    
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518) 
        xzoom 1
    contains:                                                                                   #Base
        "Emma_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png",
        # ),    
        subpixel True
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat 
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Heading", "Rogue_Pussy_Mask")
    
    contains:                                                                                   #pussy flap
        AlphaMask("Rogue_Pussy_Heading", "Rogue_Pussy_Hole_Mask")  
        
            
image Emma_Pussy_Heading: #This is the image impacted by the mask for the pussy flap in "Emma_Pussy_Moving"
    contains:                                                                                   #Mask
        "Emma_Doggy_Pussy_FHeading"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHeading.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHeading.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FHeading.png",
        # ), 
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Emma_Doggy_Pussy_Fucking2:                                                                                      #Full Animation for speed 2
    contains:                                                                                   #Base
        "Emma_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png",
        # ),   
    contains:                                                                                   #Base
        "Emma_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png",
        # ),  
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        

image Emma_Doggy_Pussy_Fucking3:                                                                                      #Full Animation for speed 3
    contains:                                                                                   #Base
        "Emma_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png",
        # ),   
    contains:                                                                                   #Base
        "Emma_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png",
        # ),   
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
image Emma_Anal2:                                                                                               #Anal static
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),         
    contains:
        "Emma_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)
    contains:                                                                                   #Mask
        "Emma_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask.png",
        # ),  
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5    
    contains:  
        "Emma_Doggy_Anal_FullCheeks"                                                                                 #Cheeks
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        # ),  


image Emma_Anal:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "Emma_Doggy_Asshole_Loose"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",
        # ),    
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Emma_Anal_Plug_Stopped:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),     
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:                                                                                   #Cock
        "Plug_Doggy_Insert"
        pos (172,500)
        #anchor (0.50,0.69)
        #pos (208,500)
        #zoom 1.25

image Emma_Anal_Plug:                                                                                               #Anal static Loose
    #contains:                                                                                   #Base
    #    ConditionSwitch(          
    #    "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
    #    "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
    #    ),     
    #    anchor (0.50,0.69)
    #    pos (208,500)
    #    zoom 1.25
    contains:                                                                                   #Cock
        "Plug_Doggy_Insert"
        pos (172,500)
        #anchor (0.50,0.69)
        #pos (208,500)
        #zoom 1.25

        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Emma_Doggy_Anal_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),     
    contains:
        "Emma_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat 
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat
    contains:                                                                                   #Mask
        "Emma_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask.png",
        # ),  
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat             
    contains:                                                                                   #Cheeks
        "Emma_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        # ),  

image Emma_Anal_Plug_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),     
        #"images/EmmaDoggy/Emma_Doggy_Anal_HeadingBase.png"    
    contains:
        "Emma_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        #"images/EmmaDoggy/Emma_Doggy_Anal_HeadingBase.png"                                       #Hole
        anchor (0.52,0.69)
        pos (218,518)
        zoom .4
        block:
            #ease .25 zoom .8
            #pause .75
            #ease 1.5 zoom .3
            #repeat 
            ease .30 zoom .9
            pause .10
            ease .10 zoom .6
            #pause .75
            pause .75
            ease .25 zoom .9
            ease 1.0 zoom .4
            repeat 
    contains:                                                                                   #Cock
        "Plug_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .5  #up
            ease 1.5 ypos 500#505  down
            repeat
    contains:                                                                                   #Mask
        "Emma_Doggy_Anal_FullMask_Plug"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask_Plug.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask_Plug.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask_Plug.png",
        # ),  
        #"images/EmmaDoggy/Emma_Doggy_Anal_HeadingMask_Plug.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .4
        block:
            #ease .25 zoom .8
            #pause .75
            #ease 1.5 zoom .3
            #repeat 
            ease .30 zoom .9
            pause .10
            ease .10 zoom .6
            #pause .25
            pause .75
            ease .25 zoom .9
            ease 1.0 zoom .4
            repeat 
    contains:                                                                                   #Cock
        "images/RogueDoggy/Rogue_Doggy_Plug_In_Top.png", 
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .5
            ease 1.5 ypos 500#505
            repeat            
    contains:                                                                                   #Cheeks
        "Emma_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        # ),  



image Emma_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Emma_Doggy_Body"         
        ypos 0
        block:     
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
            
image Emma_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 0
        block:     
            pause .4
            ease .2 ypos -10
            easein .1 ypos -7          
            easeout .9 ypos 0
            pause .9
            repeat
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal1:                                                                                         #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat
            
image Emma_Doggy_Anal_Fucking:                                                                                       #Animation for speed 2 Ass
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),     
    contains:                                                                                   #Hole
        "Emma_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Emma_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
    #     # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal1", "images/EmmaDoggy/Emma_Doggy_AnalMask.png")
    contains:                                                                                   #Mask
        "Emma_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Emma_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        # ),  


image Emma_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Emma_Doggy_Body"         
        ypos 15#28
        pause .4
        block: 
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28 
            repeat
            
image Emma_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 0
        block:     
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0   
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              
image Zero_Doggy_Anal2:                                                                                         #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Zero_Doggy_Anal3:                                                                                         #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 360
            pause .1
            ease .3 ypos 465
            repeat

image Emma_Doggy_Anal_Fucking2:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),     
    contains:                                                                                   #Hole
        "Emma_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Emma_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
    #     # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/EmmaDoggy/Emma_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        "Emma_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Emma_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        # ),  

image Emma_Doggy_Anal_Fucking3:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        "Emma_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        # ),      
    contains:                                                                                   #Hole
        "Emma_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Emma_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
    #     # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal3", "images/EmmaDoggy/Emma_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        "Emma_Doggy_Anal_FullMask3"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask3.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask3.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask3.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Emma_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        # ),  


image Emma_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Emma_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20             
            pause .05
            repeat
            
image Emma_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5 
            pause .05
            repeat #.90


image Emma_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Emma_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20             
            pause .05
            repeat
            
image Emma_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5 
            pause .05
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             UI Tool animations

            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Doggy Launch/Reset
label Emma_Doggy_Launch(Line = "massage"): 
    if Line == "sex":        
        $ P_Cock = "in"
    elif Line == "anal":
        $ P_Cock = "anal"
    elif Line == "plug":
        $ P_Cock = "plug"
    elif Line == "solo":   
        $ P_Sprite = 0
        $ P_Cock = "out"
    elif Line == "massage":   
        $ P_Sprite = 0
        $ P_Cock = 0
    elif Line == "hotdog":          
        $ P_Cock = "out"
    elif Line == "foot":          
        $ P_Cock = "foot"
    if not Trigger:
        $ Trigger = Line
    if renpy.showing("Emma_Doggy"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Emma_Sprite  
    show Emma_Doggy at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return
    
label Emma_Doggy_Reset:
    if not renpy.showing("Emma_Doggy"):
        return
    $ Emma_Arms = 2      
    hide Emma_Doggy
    if E_Gag == "ballgag":
        $ E_Gag = 0
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    $ Speed = 0
    return
    
    
               
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue BJ element
#Rogue BJ Over Sprite Compositing

# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element
#### Anal #####
image Emma_Doggy_Anal_FullMask:
    contains:                                                                                   #Mask
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask.png",
        ), 
image Emma_Doggy_Anal_FullBase:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullBase.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png",
        ),
image Emma_Doggy_Anal_FullHole:      
    contains:                                                                                   #Hole
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullHole.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png",
        ), 
image Emma_Doggy_Asshole_Loose:  
    contains:
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Asshole_Loose.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Asshole_Loose.png",
        ),  
image Emma_Doggy_Anal_FullMask3:    
    contains:                                                                                   #Mask
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask3.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask3.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask3.png",
        ),
image Emma_Doggy_Anal_FullCheeks:
    contains:                                                                                   #Cheeks
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullCheeks.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullCheeks.png",
        ), 

##### Pussy #####

image Emma_Doggy_Pussy_FBase:
    contains:  
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FBase.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png",
        ),  

image Emma_Doggy_Pussy_FMask:
    contains:
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FMask.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FMask.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FMask.png",
        ), 

image Emma_Doggy_Pussy_FHole:
    contains:                                                                                   #Base
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHole.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png",
        ), 

image Emma_Doggy_Pussy_FHeading:
    contains:
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHeading.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Pussy_FHeading.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Pussy_FHeading.png",
        ), 

image Emma_Doggy_Anal_FullMask_Plug:
    contains:                                                                                   #Mask
        ConditionSwitch(          
        # "E_Tan", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask_Plug.png",
        # "E_Tan == 'tan3'", "images/EmmaDoggy/Emma_Doggy_T3Anal_FullMask_Plug.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Anal_FullMask_Plug.png",
        ), 