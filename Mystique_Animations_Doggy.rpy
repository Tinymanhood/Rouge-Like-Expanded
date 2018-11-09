# Basic character Sprites
# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
image Mystique_Blue_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Doggy_Fuck_Top",
            "True", "Mystique_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Doggy_Fuck_Ass",
            "True", "Mystique_Doggy_Ass",            
            ),
        )
    align (0.6,0.0)
    
            
image Mystique_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            #"newgirl['Mystique'].Water", Null(), 
            "True", "images/MystiqueDoggy/Mystique_Doggy_HairBack.png",
            ),   
        #(0,0), ConditionSwitch(                                                                                 #Mouth
        #    "R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGag.png",
        #    "True", Null(), #Rogue_Doggy_BallGag
        #    ),
        (0,0), ConditionSwitch(          
            # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Body.png",
            # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Body.png",
            "True", "images/MystiqueDoggy/Mystique_Doggy_Body.png",
            ),  
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            #"newgirl['Mystique'].Tan", Null(),
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag", "images/MystiqueDoggy/Mystique_Doggy_Mouth_BlowW.png",
            "newgirl['Mystique'].Gag", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Blow.png",            
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_LipbiteW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_SurprisedW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_BlowW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_SadW.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_SmileW.png",   
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_TongueW.png",  
            "'mouth' in newgirl['Mystique'].Spunk", "images/MystiqueDoggy/Mystique_Doggy_Mouth_NormalW.png",   
            "newgirl['Mystique'].Mouth == 'normal'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Blow.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Surprised.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'grimace'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Surprised.png",       
            "newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Tongue.png", 
            "True", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Smile.png", 
            ),
        # (0,0), ConditionSwitch(                                                                                 #Mouth
        #     "not newgirl['Mystique'].Tan", Null(),
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Gag", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_BlowW.png",
        #     "newgirl['Mystique'].Gag", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Blow.png", 
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_LipbiteW.png",
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_SurprisedW.png",
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_BlowW.png",
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_SadW.png",
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_SmileW.png",   
        #     "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_TongueW.png",  
        #     "'mouth' in newgirl['Mystique'].Spunk", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_NormalW.png",   
        #     "newgirl['Mystique'].Mouth == 'normal'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Normal.png",
        #     "newgirl['Mystique'].Mouth == 'lipbite'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Lipbite.png",
        #     "newgirl['Mystique'].Mouth == 'sucking'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Blow.png",            
        #     "newgirl['Mystique'].Mouth == 'kiss'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Surprised.png",
        #     "newgirl['Mystique'].Mouth == 'sad'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Sad.png",
        #     "newgirl['Mystique'].Mouth == 'smile'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Smile.png",
        #     "newgirl['Mystique'].Mouth == 'grimace'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Smile.png",
        #     "newgirl['Mystique'].Mouth == 'surprised'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Surprised.png",       
        #     "newgirl['Mystique'].Mouth == 'tongue'", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Tongue.png", 
        #     "True", "images/MystiqueDoggy/Mystique_Doggy_T3Mouth_Smile.png", 
        #     ),
                                                              #Body base
        #(0,0), ConditionSwitch(                                                                                 #Blush
        #    #"R_Blush and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BlushEvoBallGag.png",
        #    "newgirl['Mystique'].Blush", "images/MystiqueDoggy/Mystique_Doggy_BlushEvo.png",
        #    "True", Null(), 
        #    ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "newgirl['Mystique'].Gag == 'ballgag'", "images/MystiqueDoggy/Mystique_Doggy_Mouth_Ballgag.png",
            "True", Null(), #Mystique_Doggy_Gag
            ),
        (0,0), "Mystique Doggy Blink",
        (0,0), ConditionSwitch(                                                                                 #Brows
            "newgirl['Mystique'].Brows == 'normal'", "images/MystiqueDoggy/Mystique_Doggy_Brows_Normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/MystiqueDoggy/Mystique_Doggy_Brows_Angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/MystiqueDoggy/Mystique_Doggy_Brows_Sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/MystiqueDoggy/Mystique_Doggy_Brows_Surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/MystiqueDoggy/Mystique_Doggy_Brows_Normal.png",
            "True", "images/MystiqueDoggy/Mystique_Doggy_Brows_Normal.png",
            ),  
        # (0,0), ConditionSwitch(
        #     "newgirl['Mystique'].Blindfold", "images/MystiqueDoggy/Mystique_Doggy_Blindfold.png",  
        #     "True", Null(),
        #     ),                                                                             #Eyes
        #(0,0), ConditionSwitch(                                                                                 #Collar
        #    "R_Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
        #    "True", Null(),                #R_Arms == 'gloved' or not R_Arms
        #    ),  
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not newgirl['Mystique'].Chest", Null(),        
            "newgirl['Mystique'].Chest == 'top'", "images/MystiqueDoggy/Mystique_Doggy_Chest_Tank.png",
            "newgirl['Mystique'].Chest == 'slut short top'", "images/MystiqueDoggy/Mystique_Doggy_Chest_Tankshort_slut.png",
            "newgirl['Mystique'].Chest == 'short top'", "images/MystiqueDoggy/Mystique_Doggy_Chest_Tankshort.png",
            "True", Null(),            
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not newgirl['Mystique'].Over", Null(),
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
            "newgirl['Mystique'].Over == 'black hoodie'", "images/MystiqueDoggy/Mystique_Doggy_Over_DHoodie.png",
            #"newgirl['Mystique'].Over == 'towel'", "images/MystiqueDoggy/Mystique_Doggy_Over_TowelTop.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                                 #Hair
            # "newgirl['Mystique'].HairColor == 'black' and newgirl['Mystique'].Hair == 'long'", "images/MystiqueDoggy/Mystique_Doggy_Hair_Black.png",
            # "newgirl['Mystique'].HairColor == 'black' and newgirl['Mystique'].Hair == 'evo'", "images/MystiqueDoggy/Mystique_Doggy_Hair_Ponytail_Black.png",
            # "newgirl['Mystique'].Hair == 'long'", "images/MystiqueDoggy/Mystique_Doggy_Hair.png",
            # "newgirl['Mystique'].Hair == 'evo'", "images/MystiqueDoggy/Mystique_Doggy_Hair_Ponytail.png",
            "True", "images/MystiqueDoggy/Mystique_Doggy_Hair.png",
            ),                    
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not newgirl['Mystique'].Spunk", Null(),
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hair            
        #    "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png",
        #    "R_Over == 'blue hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_BHood.png",
        #    "R_Over == 'red hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_RHood.png",
        #    "R_Over == 'yellow hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_YHood.png",
            "newgirl['Mystique'].Over == 'black hoodie'", "images/MystiqueDoggy/Mystique_Doggy_Over_DHood.png",
        #    "R_Over == 'white hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_WHood.png", 
            "True", Null(),                     
            ),  
        )

image Mystique_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "not newgirl['Mystique'].PantiesDown or (newgirl['Mystique'].Legs == 'pants' and not newgirl['Mystique'].Upskirt)", Null(),  
            "newgirl['Mystique'].Panties == 'white panties'", "images/MystiqueDoggy/Mystique_Doggy_PantiesWhite_Back.png",
            "newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueDoggy/Mystique_Doggy_PantiesBlack_Back.png",
            "newgirl['Mystique'].Panties == 'bikini'", "images/MystiqueDoggy/Mystique_Doggy_BikiniWhite_Back.png",
            "newgirl['Mystique'].Panties == 'black bikini'", "images/MystiqueDoggy/Mystique_Doggy_BikiniBlack_Back.png",
            #"newgirl['Mystique'].Panties == 'blue shorts'", "images/MystiqueDoggy/Mystique_Doggy_Shorts_Back.png",    
            # "newgirl['Mystique'].Panties == 'green panties'", "images/MystiqueDoggy/Mystique_Doggy_Panties_Down_Back_Green.png",   
            # "newgirl['Mystique'].Panties == 'purple bikini panties'", "images/MystiqueDoggy/Mystique_Doggy_Panties_Down_Back_Purple.png",   
            #"newgirl['Mystique'].Panties == 'black large panties'", "images/MystiqueDoggy/Mystique_Doggy_UndiesBlack_Back.png",   
            #"newgirl['Mystique'].Panties == 'lace panties' or newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueDoggy/Mystique_Doggy_Panties_Back.png",  
            #"newgirl['Mystique'].Panties == 'swimsuit1' or newgirl['Mystique'].Panties == 'swimsuit2'", "images/MystiqueDoggy/Mystique_Doggy_Swimsuit.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Wet look
            # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Ass.png",   
            # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Ass.png",   
            "True", "images/MystiqueDoggy/Mystique_Doggy_Ass.png",              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "newgirl['Mystique'].Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        #(0,0), ConditionSwitch(                                                                                 #Hose
        #    "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
        #    "True", Null(),
        #    ),             
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "not newgirl['Mystique'].PantiesDown or (newgirl['Mystique'].Legs == 'pants' and not newgirl['Mystique'].Upskirt)", Null(),
        #    "R_Panties == 'shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png",
        #    "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down_Wet.png",
        #    "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down_Wet.png", #fix turn this on when graphics fixed
        #    "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png",
        #    "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down.png",
        #    "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down.png", 
        #    "R_Panties == 'green panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "newgirl['Mystique'].Panties == 'white panties'", "images/MystiqueDoggy/Mystique_Doggy_PantiesWhite_Down.png",
            "newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueDoggy/Mystique_Doggy_PantiesBlack_Down.png",
            "newgirl['Mystique'].Panties == 'bikini'", "images/MystiqueDoggy/Mystique_Doggy_BikiniWhite_Down.png",
            "newgirl['Mystique'].Panties == 'black bikini'", "images/MystiqueDoggy/Mystique_Doggy_BikiniBlack_Down.png",
        #    "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_UndiesBlacE_Down_Wet.png",
        #    "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlacE_Down.png",  
        #    "R_Panties == 'lace panties' or R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite           
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Mystique_Doggy_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Mystique_Doggy_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Mystique_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Mystique_Pussy",    
            # "newgirl['Mystique'].Tan and Trigger == 'lick pussy'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_Open.png",   
            # "newgirl['Mystique'].Tan == 'tan3' and Trigger == 'lick pussy'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_Open.png",   
            "Trigger == 'lick pussy'", "images/MystiqueDoggy/Mystique_Doggy_Pussy_Open.png",   
            # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_Closed.png", 
            # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_Closed.png", 
            "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_Closed.png", 
            ),   
        # (0,0), ConditionSwitch(                                                                                 #pubes              
        #    "not newgirl['Mystique'].Pubes", Null(),         
        #    "P_Sprite and P_Cock == 'in'", Null(),
        #    "newgirl['Mystique'].Legs == 'pants' and not newgirl['Mystique'].Upskirt and newgirl['Mystique'].HairColor == 'black'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlacE_Panties.png",   
        #    "newgirl['Mystique'].Legs == 'pants' and not newgirl['Mystique'].Upskirt and newgirl['Mystique'].HairColor == 'blonde'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlonde_Panties.png",   
        #    "newgirl['Mystique'].Legs == 'pants' and not newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Pubes_Panties.png",   
        #    "newgirl['Mystique'].PantiesDown and newgirl['Mystique'].HairColor == 'black'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlack.png",  
        #    "newgirl['Mystique'].PantiesDown and newgirl['Mystique'].HairColor == 'blonde'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlonde.png",  
        #    "newgirl['Mystique'].PantiesDown", "images/MystiqueDoggy/Mystique_Doggy_Pubes.png",  
        #    "newgirl['Mystique'].Panties and newgirl['Mystique'].HairColor == 'black'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlacE_Panties.png",
        #    "newgirl['Mystique'].Panties and newgirl['Mystique'].HairColor == 'blonde'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlonde_Panties.png",
        #    "newgirl['Mystique'].Panties", "images/MystiqueDoggy/Mystique_Doggy_Pubes_Panties.png",
        #    "newgirl['Mystique'].Hose and newgirl['Mystique'].Hose != 'stockings' and newgirl['Mystique'].HairColor == 'black'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlacE_Panties.png",   
        #    "newgirl['Mystique'].Hose and newgirl['Mystique'].Hose != 'stockings' and newgirl['Mystique'].HairColor == 'blonde'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlonde_Panties.png",   
        #    "newgirl['Mystique'].Hose and newgirl['Mystique'].Hose != 'stockings'", "images/MystiqueDoggy/Mystique_Doggy_Pubes_Panties.png",   
        #    "True and R_HairColor == 'black'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlack.png",  
        #    "True and R_HairColor == 'blonde'", "images/MystiqueDoggy/Mystique_Doggy_PubesBlonde.png",  
        #    "True", "images/MystiqueDoggy/Mystique_Doggy_Pubes.png",  
        #    ),  
        # (0,0), ConditionSwitch(                                                                                 #Pussy Piercings          
        #     "P_Sprite", Null(),             
        #     "newgirl['Mystique'].Pierce == 'ring'", "images/MystiqueDoggy/Mystique_Doggy_Pussy_Ring.png",            
        #     #"R_Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
        #     "True", Null(),  
        #     ),   
        (0,0), ConditionSwitch(                                                                                 #Anus Composite            
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Mystique_Doggy_Anal_Fucking3",         
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Mystique_Doggy_Anal_Fucking2",         
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Mystique_Doggy_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Mystique_Doggy_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Mystique_Anal",  
            "P_Sprite and P_Cock == 'plug' and Speed", "Mystique_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and newgirl['Mystique'].Plugged", "images/MystiqueDoggy/Mystique_Doggy_Plugged.png",  
            "P_Sprite and P_Cock == 'plug'", "Mystique_Anal_Plug",  
            "newgirl['Mystique'].Plugged", "images/MystiqueDoggy/Mystique_Doggy_Plugged.png",   
            # "newgirl['Mystique'].Tan and newgirl['Mystique'].Loose", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",   
            # "newgirl['Mystique'].Tan == 'tan3' and newgirl['Mystique'].Loose", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",   
            "newgirl['Mystique'].Loose", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Loose.png",   
            # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Tight.png", 
            # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Tight.png", 
            "True", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Tight.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and newgirl['Mystique'].Plugged", "images/MystiqueDoggy/Mystique_Doggy_SpankPlugged1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/MystiqueDoggy/Mystique_Doggy_SpankAnal1.png",
            "newgirl['Mystique'].Spank >= 1 and newgirl['Mystique'].Spank <= 4", "images/MystiqueDoggy/Mystique_Doggy_Spank1.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and newgirl['Mystique'].Plugged", "images/MystiqueDoggy/Mystique_Doggy_SpankPlugged2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/MystiqueDoggy/Mystique_Doggy_SpankAnal2.png",
            "newgirl['Mystique'].Spank >= 5 and newgirl['Mystique'].Spank <= 10", "images/MystiqueDoggy/Mystique_Doggy_Spank2.png",
            "newgirl['Mystique'].Spank >= 11 and newgirl['Mystique'].Plugged", "images/MystiqueDoggy/Mystique_Doggy_SpankPlugged3.png",
            "newgirl['Mystique'].Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/MystiqueDoggy/Mystique_Doggy_SpankAnal3.png",
            "newgirl['Mystique'].Spank >= 11", "images/MystiqueDoggy/Mystique_Doggy_Spank3.png",
            "True", Null(),
            ),           
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in newgirl['Mystique'].Spunk and P_Sprite", Null(),   
            "'anal' in newgirl['Mystique'].Spunk and P_Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "'anal' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "'anal' in newgirl['Mystique'].Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "newgirl['Mystique'].PantiesDown", Null(),     
        #    "newgirl['Mystique'].Panties == 'shorts' and newgirl['Mystique'].Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",
        #    "R_Panties == 'red shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_RYShorts_Wet.png",
        #    "R_Panties == 'blue shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_BYShorts_Wet.png",          
        #    "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
        #    "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts.png",
        #    "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts.png",
        #    "newgirl['Mystique'].Panties == 'green panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",          
            "newgirl['Mystique'].Panties == 'white panties'", "images/MystiqueDoggy/Mystique_Doggy_PantiesWhite.png",
            "newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueDoggy/Mystique_Doggy_PantiesBlack.png",
            "newgirl['Mystique'].Panties == 'bikini'", "images/MystiqueDoggy/Mystique_Doggy_BikiniWhite.png",
            "newgirl['Mystique'].Panties == 'black bikini'", "images/MystiqueDoggy/Mystique_Doggy_BikiniBlack.png",
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
            #"newgirl['Mystique'].Legs == 'capris' and newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Legs_Pants_Down.png",            
            #"newgirl['Mystique'].Legs == 'capris' and newgirl['Mystique'].Wet > 1", "images/MystiqueDoggy/Mystique_Doggy_Legs_Pants_Wet.png",
            #"newgirl['Mystique'].Legs == 'capris'", "images/MystiqueDoggy/Mystique_Doggy_Legs_Pants.png",
            "newgirl['Mystique'].Legs == 'black pants' and newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Pants_Black_Down.png",            
            "newgirl['Mystique'].Legs == 'black pants' and newgirl['Mystique'].Wet > 1", "images/MystiqueDoggy/Mystique_Doggy_Pants_Black_Wet.png",
            "newgirl['Mystique'].Legs == 'black pants'", "images/MystiqueDoggy/Mystique_Doggy_Pants_Black.png",
            "newgirl['Mystique'].Legs == 'pants' and newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Pants_White_Down.png",            
            "newgirl['Mystique'].Legs == 'pants' and newgirl['Mystique'].Wet > 1", "images/MystiqueDoggy/Mystique_Doggy_Pants_White_Wet.png",
            "newgirl['Mystique'].Legs == 'pants'", "images/MystiqueDoggy/Mystique_Doggy_Pants_White.png",
            "newgirl['Mystique'].Legs == 'skirt' and newgirl['Mystique'].Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/MystiqueDoggy/Mystique_Doggy_Legs_Skirt_UpAnal.png",   
            "newgirl['Mystique'].Legs == 'skirt' and newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Legs_Skirt_Up.png",   
            "newgirl['Mystique'].Legs == 'skirt'", "images/MystiqueDoggy/Mystique_Doggy_Legs_Skirt.png", 
            "newgirl['Mystique'].Legs == 'skirtshort' and newgirl['Mystique'].Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/MystiqueDoggy/Mystique_Doggy_Legs_SkirtShort_UpAnal.png",   
            "newgirl['Mystique'].Legs == 'skirtshort' and newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Legs_SkirtShort_Up.png",   
            "newgirl['Mystique'].Legs == 'skirtshort'", "images/MystiqueDoggy/Mystique_Doggy_Legs_SkirtShort.png", 
        #    "newgirl['Mystique'].Legs == 'cheerleader skirt' and newgirl['Mystique'].Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/MystiqueDoggy/Mystique_Doggy_CheerleadeK_Skirt_UpAnal.png",   
        #    "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Cheerleader_Skirt_Up.png",   
        #    "R_Legs == 'cheerleader skirt'", "images/MystiqueDoggy/Mystique_Doggy_Cheerleader_Skirt.png", 
        #    "R_Legs == 'cheerleader skirtshort' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/MystiqueDoggy/Mystique_Doggy_Cheerleader_SkirtShort_UpAnal.png",   
        #    "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Cheerleader_SkirtShort_Up.png",   
        #    "R_Legs == 'cheerleader skirtshort'", "images/MystiqueDoggy/Mystique_Doggy_Cheerleader_SkirtShort.png", 
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
        #    "R_Over == 'nighty' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",            
        #    "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            # "newgirl['Mystique'].Over == 'towel' and newgirl['Mystique'].Upskirt", "images/MystiqueDoggy/Mystique_Doggy_Over_TowelAss_Up.png",            
            # "newgirl['Mystique'].Over == 'towel'", "images/MystiqueDoggy/Mystique_Doggy_Over_TowelAss.png",
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in newgirl['Mystique'].Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
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

image Mystique Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(          
    "newgirl['Mystique'].Eyes == 'sexy'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Side.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Normal.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Sexy.png",           
    "newgirl['Mystique'].Eyes == 'stunned'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Stunned.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Surprised.png",
    "newgirl['Mystique'].Eyes == 'squint'", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Sexy.png",
    "True", "images/MystiqueDoggy/Mystique_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    "images/MystiqueDoggy/Mystique_Doggy_Eyes_Closed.png"
    .25
    repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              #Pussy fucking animations    
image Mystique_Pussy:                                                                                              #Full Animation for speed 0    
    contains:  
        "Mystique_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FBase.png",
        # ),                                                                                 #Base
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (169,460) #Out stroke
    contains:
        "Mystique_Doggy_Pussy_FMask"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FMask.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FMask.png",
        # ),                                                                                   #Mask

image Mystique_Pussy_Moving:                                                                                       #Full Animation for speed 1
    subpixel True
    contains:                                                                                   #Base
        "Mystique_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FBase.png",
        # ),    
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518) 
        xzoom 1
    contains:                                                                                   #Base
        "Mystique_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FHole.png",
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
        
            
image Mystique_Pussy_Heading: #This is the image impacted by the mask for the pussy flap in "Mystique_Pussy_Moving"
    contains:                                                                                   #Mask
        "Mystique_Doggy_Pussy_FHeading"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHeading.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHeading.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FHeading.png",
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

image Mystique_Doggy_Pussy_Fucking2:                                                                                      #Full Animation for speed 2
    contains:                                                                                   #Base
        "Mystique_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FBase.png",
        # ),   
    contains:                                                                                   #Base
        "Mystique_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FHole.png",
        # ),  
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        

image Mystique_Doggy_Pussy_Fucking3:                                                                                      #Full Animation for speed 3
    contains:                                                                                   #Base
        "Mystique_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FBase.png",
        # ),   
    contains:                                                                                   #Base
        "Mystique_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FHole.png",
        # ),   
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
image Mystique_Anal2:                                                                                               #Anal static
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        # ),         
    contains:
        "Mystique_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)
    contains:                                                                                   #Mask
        "Mystique_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask.png",
        # ),  
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5    
    contains:  
        "Mystique_Doggy_Anal_FullCheeks"                                                                                 #Cheeks
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        # ),  


image Mystique_Anal:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "Mystique_Doggy_Asshole_Loose"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Loose.png",
        # ),    
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Mystique_Anal_Plug_Stopped:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
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

image Mystique_Anal_Plug:                                                                                               #Anal static Loose
    #contains:                                                                                   #Base
    #    ConditionSwitch(          
    #    "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
    #    "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
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
image Mystique_Doggy_Anal_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        # ),     
    contains:
        "Mystique_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
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
        "Mystique_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask.png",
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
        "Mystique_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        # ),  

image Mystique_Anal_Plug_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        # ),     
        #"images/MystiqueDoggy/Mystique_Doggy_Anal_HeadingBase.png"    
    contains:
        "Mystique_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        #"images/MystiqueDoggy/Mystique_Doggy_Anal_HeadingBase.png"                                       #Hole
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
        "Mystique_Doggy_Anal_FullMask_Plug"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask_Plug.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask_Plug.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask_Plug.png",
        # ),  
        #"images/MystiqueDoggy/Mystique_Doggy_Anal_HeadingMask_Plug.png"
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
        "Mystique_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        # ),  



image Mystique_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Doggy_Body"         
        ypos 0
        block:     
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
            
image Mystique_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Doggy_Ass"
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
            
image Mystique_Doggy_Anal_Fucking:                                                                                       #Animation for speed 2 Ass
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        # ),     
    contains:                                                                                   #Hole
        "Mystique_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Mystique_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
    #     # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal1", "images/MystiqueDoggy/Mystique_Doggy_AnalMask.png")
    contains:                                                                                   #Mask
        "Mystique_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Mystique_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        # ),  


image Mystique_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Mystique_Doggy_Body"         
        ypos 15#28
        pause .4
        block: 
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28 
            repeat
            
image Mystique_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Mystique_Doggy_Ass"
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

image Mystique_Doggy_Anal_Fucking2:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        # ),     
    contains:                                                                                   #Hole
        "Mystique_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Mystique_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
    #     # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/MystiqueDoggy/Mystique_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        "Mystique_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Mystique_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        # ),  

image Mystique_Doggy_Anal_Fucking3:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        "Mystique_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        # ),      
    contains:                                                                                   #Hole
        "Mystique_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Mystique_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
    #     # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal3", "images/MystiqueDoggy/Mystique_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        "Mystique_Doggy_Anal_FullMask3"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask3.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask3.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask3.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Mystique_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        # ),  


image Mystique_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20             
            pause .05
            repeat
            
image Mystique_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5 
            pause .05
            repeat #.90


image Mystique_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Mystique_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20             
            pause .05
            repeat
            
image Mystique_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Mystique_Doggy_Ass"
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
label Mystique_Doggy_Launch(Line = "massage"): 
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
    if renpy.showing("Mystique_Doggy"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Mystique_Sprite  
    show Mystique_Doggy at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return
    
label Mystique_Doggy_Reset:
    if not renpy.showing("Mystique_Doggy"):
        return
    $ newgirl["Mystique"].Girl_Arms = 2      
    hide Mystique_Doggy
    if newgirl["Mystique"].Gag == "ballgag":
        $ newgirl["Mystique"].Gag = 0
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
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
image Mystique_Doggy_Anal_FullMask:
    contains:                                                                                   #Mask
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask.png",
        ), 
image Mystique_Doggy_Anal_FullBase:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullBase.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullBase.png",
        ),
image Mystique_Doggy_Anal_FullHole:      
    contains:                                                                                   #Hole
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullHole.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullHole.png",
        ), 
image Mystique_Doggy_Asshole_Loose:  
    contains:
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Asshole_Loose.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Asshole_Loose.png",
        ),  
image Mystique_Doggy_Anal_FullMask3:    
    contains:                                                                                   #Mask
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask3.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask3.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask3.png",
        ),
image Mystique_Doggy_Anal_FullCheeks:
    contains:                                                                                   #Cheeks
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullCheeks.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullCheeks.png",
        ), 

##### Pussy #####

image Mystique_Doggy_Pussy_FBase:
    contains:  
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FBase.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FBase.png",
        ),  

image Mystique_Doggy_Pussy_FMask:
    contains:
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FMask.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FMask.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FMask.png",
        ), 

image Mystique_Doggy_Pussy_FHole:
    contains:                                                                                   #Base
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHole.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FHole.png",
        ), 

image Mystique_Doggy_Pussy_FHeading:
    contains:
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHeading.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Pussy_FHeading.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Pussy_FHeading.png",
        ), 

image Mystique_Doggy_Anal_FullMask_Plug:
    contains:                                                                                   #Mask
        ConditionSwitch(          
        # "newgirl['Mystique'].Tan", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask_Plug.png",
        # "newgirl['Mystique'].Tan == 'tan3'", "images/MystiqueDoggy/Mystique_Doggy_T3Anal_FullMask_Plug.png",
        "True", "images/MystiqueDoggy/Mystique_Doggy_Anal_FullMask_Plug.png",
        ), 