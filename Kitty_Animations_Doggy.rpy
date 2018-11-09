# Basic character Sprites
# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
image Kitty_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Kitty_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Kitty_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Kitty_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Kitty_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Kitty_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Kitty_Doggy_Fuck_Top",
            "True", "Kitty_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Kitty_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Kitty_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Kitty_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Kitty_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Kitty_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Kitty_Doggy_Fuck_Ass",
            "True", "Kitty_Doggy_Ass",            
            ),
        )
    align (0.6,0.0)
    
            
image Kitty_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            #"K_Water", Null(), 
            #"R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackB.png",   
            #"R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeB.png",   
            #"R_Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairB.png",   
            #"True", Null(),   
            "K_HairColor == 'blonde' and K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Blonde.png",
            "K_HairColor == 'blonde' and K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail_Blonde.png", 
            "K_HairColor == 'red' and K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Red.png",
            "K_HairColor == 'red' and K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail_Red.png",               
            "K_HairColor == 'black' and K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Black.png",
            "K_HairColor == 'black' and K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail_Black.png",
            "K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair.png",
            "K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Hair.png",
            ),   
        #(0,0), ConditionSwitch(                                                                                 #Mouth
        #    "R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGag.png",
        #    "True", Null(), #Rogue_Doggy_BallGag
        #    ),
        (0,0), ConditionSwitch(          
            "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Body.png",
            "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Body.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Body.png",
            ),  
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            "K_Tan", Null(),
            "'mouth' in K_Spunk and K_Gag", "images/KittyDoggy/Kitty_Doggy_Mouth_BlowW.png",
            "K_Gag", "images/KittyDoggy/Kitty_Doggy_Mouth_Blow.png",            
            "'mouth' in K_Spunk and K_Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Mouth_LipbiteW.png",
            "'mouth' in K_Spunk and K_Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Mouth_SurprisedW.png",
            "'mouth' in K_Spunk and K_Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Mouth_BlowW.png",
            "'mouth' in K_Spunk and K_Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Mouth_SadW.png",
            "'mouth' in K_Spunk and K_Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Mouth_SmileW.png",   
            "'mouth' in K_Spunk and K_Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Mouth_TongueW.png",  
            "'mouth' in K_Spunk", "images/KittyDoggy/Kitty_Doggy_Mouth_NormalW.png",   
            "K_Mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            "K_Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Mouth_Lipbite.png",
            "K_Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Mouth_Blow.png",            
            "K_Mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_Mouth_Surprised.png",
            "K_Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Mouth_Sad.png",
            "K_Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "K_Mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "K_Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Mouth_Surprised.png",       
            "K_Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png", 
            "True", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            #"R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGagTop.png",
            #"'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            #"R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            "not K_Tan", Null(),
            "'mouth' in K_Spunk and K_Gag", "images/KittyDoggy/Kitty_Doggy_T3Mouth_BlowW.png",
            "K_Gag", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Blow.png", 
            "'mouth' in K_Spunk and K_Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_LipbiteW.png",
            "'mouth' in K_Spunk and K_Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_SurprisedW.png",
            "'mouth' in K_Spunk and K_Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_BlowW.png",
            "'mouth' in K_Spunk and K_Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_SadW.png",
            "'mouth' in K_Spunk and K_Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_SmileW.png",   
            "'mouth' in K_Spunk and K_Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_TongueW.png",  
            "'mouth' in K_Spunk", "images/KittyDoggy/Kitty_Doggy_T3Mouth_NormalW.png",   
            "K_Mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Normal.png",
            "K_Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Lipbite.png",
            "K_Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Blow.png",            
            "K_Mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Surprised.png",
            "K_Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Sad.png",
            "K_Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Smile.png",
            "K_Mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Smile.png",
            "K_Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Surprised.png",       
            "K_Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Tongue.png", 
            "True", "images/KittyDoggy/Kitty_Doggy_T3Mouth_Smile.png", 
            ),
                                                              #Body base
        #(0,0), ConditionSwitch(                                                                                 #Blush
        #    #"R_Blush and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BlushEvoBallGag.png",
        #    "K_Blush", "images/KittyDoggy/Kitty_Doggy_BlushEvo.png",
        #    "True", Null(), 
        #    ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "K_Gag == 'ballgag'", "images/KittyDoggy/Kitty_Doggy_Ballgag.png",
            "True", Null(), #Kitty_Doggy_Gag
            ),
        (0,0), ConditionSwitch(                                                                                 #Brows
            "K_Brows == 'normal'", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            "K_Brows == 'angry'", "images/KittyDoggy/Kitty_Doggy_Brows_Angry.png",
            "K_Brows == 'sad'", "images/KittyDoggy/Kitty_Doggy_Brows_Sad.png",
            "K_Brows == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Brows_Surprised.png",        
            "K_Brows == 'confused'", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            ),     
        (0,0), "Kitty Doggy Blink",
        (0,0), ConditionSwitch(
            "K_Blindfold", "images/KittyDoggy/Kitty_Doggy_Blindfold.png",  
            "True", Null(),
            ),                                                                             #Eyes
        #(0,0), ConditionSwitch(                                                                                 #Collar
        #    "R_Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
        #    "True", Null(),                #R_Arms == 'gloved' or not R_Arms
        #    ),  
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not K_Chest", Null(),        
        #    "R_Chest == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
        #    "R_Chest == 'tank short'", "images/RogueDoggy/Rogue_Doggy_Chest_TankShort.png",
        #    "R_Chest == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
        #    "R_Chest == 'sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png",
        #    "R_Chest == 'red sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_RYSportsBra.png",
        #    "R_Chest == 'blue sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_BYSportsBra.png",
            "K_Chest == 'black top'", "images/KittyDoggy/Kitty_Doggy_ChestBlackTop.png",
            "K_Chest == 'orange top'", "images/KittyDoggy/Kitty_Doggy_ChestOrangeTop.png",
            "K_Chest == 'purple bikini bra'", "images/KittyDoggy/Kitty_Doggy_Chest_PurpleBikini.png",
            "K_Chest == 'bra'", "images/KittyDoggy/Kitty_Doggy_Chest_UnderBra.png",
            "K_Chest == 'lace bra'", "images/KittyDoggy/Kitty_Doggy_Chest_LaceBra.png",
            "K_Chest == 'darker lace bra'", "images/KittyDoggy/Kitty_Doggy_Chest_DarkerLace.png",
        #    "R_Chest == 'bra'", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
        #    "R_Chest == 'cheerleader'", "images/RogueDoggy/Rouge_Doggy_Cheerleader_Outfit.png",
            "True", Null(),            
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not K_Over", Null(),
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
            "K_Over == 'black dress'", "images/KittyDoggy/Kitty_Doggy_Over_DressTop.png",
            "K_Over == 'towel'", "images/KittyDoggy/Kitty_Doggy_Over_TowelTop.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                                 #Hair
            #"R_Water and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackWet.png",   
            #"R_Water and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeWet.png",   
            #"R_Water", "images/RogueDoggy/Rogue_Doggy_HairWet.png",   
            #"R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackF.png",   
            #"R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeF.png",   
            #"R_Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairF.png",   
            #"True and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackF.png",                     
            #"True and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeF.png",   
            "K_HairColor == 'blonde' and K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Blonde.png",
            "K_HairColor == 'blonde' and K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail_Blonde.png", 
            "K_HairColor == 'red' and K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Red.png",
            "K_HairColor == 'red' and K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail_Red.png",                  
            "K_HairColor == 'black' and K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Black.png",
            "K_HairColor == 'black' and K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail_Black.png",
            "K_Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair.png",
            "K_Hair == 'evo'", "images/KittyDoggy/Kitty_Doggy_Hair_Ponytail.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Hair.png",
            ),                    
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Ear.png",   
            "True", Null(),              
            ),
        (0,0), ConditionSwitch(
            "K_Headband == 'pink'", "images/KittyDoggy/Kitty_Doggy_Headband_Pink.png",
            "K_Headband == 'black'", "images/KittyDoggy/Kitty_Doggy_Headband_Black.png",
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not K_Spunk", Null(),
            "'facial' in K_Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
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

image Kitty_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "not K_Upskirt", Null(),  
            #"K_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            #"K_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            #"K_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",    
            "K_Legs == 'shorts'", "images/KittyDoggy/Kitty_Doggy_Shorts_Back.png",   
            #"K_Panties == 'purple bikini panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Down_Back_Purple.png",   
            #"K_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Back.png",   
            #"K_Panties == 'lace panties' or K_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",  
            #"K_Panties == 'swimsuit1' or K_Panties == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit.png",  
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "not K_PantiesDown or (K_Legs == 'pants' and not K_Upskirt)", Null(),  
            #"K_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            #"K_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            #"K_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",    
            "K_Panties == 'green panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Down_Back_Green.png",   
            "K_Panties == 'purple bikini panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Down_Back_Purple.png",   
            #"K_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Back.png",   
            #"K_Panties == 'lace panties' or K_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",  
            #"K_Panties == 'swimsuit1' or K_Panties == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Ass.png",   
            "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Ass.png",   
            "True", "images/KittyDoggy/Kitty_Doggy_Ass.png",              
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "K_Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        #(0,0), ConditionSwitch(                                                                                 #Hose
        #    "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
        #    "True", Null(),
        #    ),             
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "not K_PantiesDown or (K_Legs == 'pants' and not K_Upskirt)", Null(),
        #    "R_Panties == 'shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png",
        #    "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down_Wet.png",
        #    "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down_Wet.png", #fix turn this on when graphics fixed
        #    "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png",
        #    "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down.png",
        #    "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down.png", 
        #    "R_Panties == 'green panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "K_Panties == 'green panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Down_Green.png", 
            "K_Panties == 'purple bikini panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Down_Purple.png", 
        #    "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Down_Wet.png",
        #    "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Down.png",  
        #    "R_Panties == 'lace panties' or R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite           
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Kitty_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Kitty_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Kitty_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Kitty_Pussy",    
            "K_Tan and Trigger == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_Open.png",   
            "K_Tan == 'tan3' and Trigger == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_Open.png",   
            "Trigger == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_Pussy_Open.png",   
            "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_Closed.png", 
            "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_Closed.png", 
            "True", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png", 
            ),   
        #(0,0), ConditionSwitch(                                                                                 #pubes              
        #    "not R_Pubes", Null(),         
        #    "P_Sprite and P_Cock == 'in'", Null(),
        #    "R_Legs == 'pants' and not R_Upskirt and R_HairColor == 'black'", "images/KittyDoggy/Rogue_Doggy_PubesBlack_Panties.png",   
        #    "R_Legs == 'pants' and not R_Upskirt and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_PubesBlonde_Panties.png",   
        #    "R_Legs == 'pants' and not R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
        #    "R_PantiesDown and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_PubesBlack.png",  
        #    "R_PantiesDown and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_PubesBlonde.png",  
        #    "R_PantiesDown", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
        #    "R_Panties and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_PubesBlack_Panties.png",
        #    "R_Panties and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_PubesBlonde_Panties.png",
        #    "R_Panties", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
        #    "R_Hose and R_Hose != 'stockings' and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_PubesBlack_Panties.png",   
        #    "R_Hose and R_Hose != 'stockings' and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_PubesBlonde_Panties.png",   
        #    "R_Hose and R_Hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
        #    "True and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_PubesBlack.png",  
        #    "True and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_PubesBlonde.png",  
        #    "True", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
        #    ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Piercings          
            "P_Sprite", Null(),             
            "K_Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pussy_Ring.png",            
            #"R_Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "True", Null(),  
            ),   
        (0,0), ConditionSwitch(                                                                                 #Anus Composite            
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Kitty_Doggy_Anal_Fucking3",         
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Kitty_Doggy_Anal_Fucking2",         
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Kitty_Doggy_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Kitty_Doggy_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Kitty_Anal",  
            "P_Sprite and P_Cock == 'plug' and Speed", "Kitty_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and K_Plugged", "images/KittyDoggy/Kitty_Doggy_Plugged.png",  
            "P_Sprite and P_Cock == 'plug'", "Kitty_Anal_Plug",  
            "K_Plugged", "images/KittyDoggy/Kitty_Doggy_Plugged.png",   
            "K_Tan and K_Loose", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",   
            "K_Tan == 'tan3' and K_Loose", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",   
            "K_Loose", "images/KittyDoggy/Kitty_Doggy_Asshole_Loose.png",   
            "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Tight.png", 
            "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Tight.png", 
            "True", "images/KittyDoggy/Kitty_Doggy_Asshole_Tight.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            "K_Spank >= 1 and K_Spank <= 4 and K_Plugged", "images/KittyDoggy/Kitty_Doggy_SpankPlugged1.png",
            "K_Spank >= 1 and K_Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/KittyDoggy/Kitty_Doggy_SpankAnal1.png",
            "K_Spank >= 1 and K_Spank <= 4", "images/KittyDoggy/Kitty_Doggy_Spank1.png",
            "K_Spank >= 5 and K_Spank <= 10 and K_Plugged", "images/KittyDoggy/Kitty_Doggy_SpankPlugged2.png",
            "K_Spank >= 5 and K_Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/KittyDoggy/Kitty_Doggy_SpankAnal2.png",
            "K_Spank >= 5 and K_Spank <= 10", "images/KittyDoggy/Kitty_Doggy_Spank2.png",
            "K_Spank >= 11 and K_Plugged", "images/KittyDoggy/Kitty_Doggy_SpankPlugged3.png",
            "K_Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/KittyDoggy/Kitty_Doggy_SpankAnal3.png",
            "K_Spank >= 11", "images/KittyDoggy/Kitty_Doggy_Spank3.png",
            "True", Null(),
            ),           
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in K_Spunk and P_Sprite", Null(),   
            "'anal' in K_Spunk and P_Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "'anal' in K_Spunk and K_Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "'anal' in K_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "K_PantiesDown", Null(),     
        #    "K_Panties == 'shorts' and K_Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",
        #    "R_Panties == 'red shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_RYShorts_Wet.png",
        #    "R_Panties == 'blue shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_BYShorts_Wet.png",          
        #    "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
        #    "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts.png",
        #    "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts.png",
        #    "K_Panties == 'green panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",          
            "K_Panties == 'green panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png", 
            "K_Panties == 'purple bikini panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Purple.png", 
        #    "R_Panties == 'black large panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Wet.png",          
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
            "K_Legs == 'shorts' and K_Upskirt and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_Shorts_Down_Wet.png",
            "K_Legs == 'shorts' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Shorts_Down.png",            
            "K_Legs == 'shorts' and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_Shorts_Wet.png",
            "K_Legs == 'shorts'", "images/KittyDoggy/Kitty_Doggy_Shorts.png",

            "K_Legs == 'blue shorts' and K_Upskirt and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_BlueShorts_Down_Wet.png",
            "K_Legs == 'blue shorts' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_BlueShorts_Down.png",            
            "K_Legs == 'blue shorts' and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_BlueShorts_Wet.png",
            "K_Legs == 'blue shorts'", "images/KittyDoggy/Kitty_Doggy_BlueShorts.png",

            "K_Legs == 'white shorts' and K_Upskirt and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_BlueShorts_Down_Wet.png",
            "K_Legs == 'white shorts' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_BlueShorts_Down.png",            
            "K_Legs == 'white shorts' and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_BlueShorts_Wet.png",
            "K_Legs == 'white shorts'", "images/KittyDoggy/Kitty_Doggy_BlueShorts.png",

            "K_Legs == 'capris' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Capris_Down.png",            
            "K_Legs == 'capris' and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_Capris_Wet.png",
            "K_Legs == 'capris'", "images/KittyDoggy/Kitty_Doggy_Legs_Capris.png",
            "K_Legs == 'black jeans' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_BlackJeans_Down.png",            
            "K_Legs == 'black jeans' and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlackJeans_Wet.png",
            "K_Legs == 'black jeans'", "images/KittyDoggy/Kitty_Doggy_Legs_BlackJeans.png",
            "K_Legs == 'yoga pants' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png",            
            "K_Legs == 'yoga pants' and K_Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Wet.png",
            "K_Legs == 'yoga pants'", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png",
        #    "K_Legs == 'orange skirt' and K_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_UpAnal.png",   
            "K_Legs == 'orange skirt' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_SkirtOrange_Up.png",   
            "K_Legs == 'orange skirt'", "images/KittyDoggy/Kitty_Doggy_SkirtOrange.png", 
            "K_Legs == 'white skirt' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_SkirtWhite_Up.png",   
            "K_Legs == 'white skirt'", "images/KittyDoggy/Kitty_Doggy_SkirtWhite.png", 
            "K_Legs == 'black skirt' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_SkirtBlack_Up.png",   
            "K_Legs == 'black skirt'", "images/KittyDoggy/Kitty_Doggy_SkirtBlack.png", 
        #    "K_Legs == 'skirtshort' and K_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/KittyDoggy/Kitty_Doggy_Legs_SkirtShort_UpAnal.png",   
        #    "K_Legs == 'skirtshort' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_SkirtShort_Up.png",   
        #    "K_Legs == 'skirtshort'", "images/KittyDoggy/Kitty_Doggy_Legs_SkirtShort.png", 
        #    "K_Legs == 'cheerleader skirt' and K_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/KittyDoggy/Kitty_Doggy_CheerleadeK_Skirt_UpAnal.png",   
        #    "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/KittyDoggy/Kitty_Doggy_Cheerleader_Skirt_Up.png",   
        #    "R_Legs == 'cheerleader skirt'", "images/KittyDoggy/Kitty_Doggy_Cheerleader_Skirt.png", 
        #    "R_Legs == 'cheerleader skirtshort' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/KittyDoggy/Kitty_Doggy_Cheerleader_SkirtShort_UpAnal.png",   
        #    "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/KittyDoggy/Kitty_Doggy_Cheerleader_SkirtShort_Up.png",   
        #    "R_Legs == 'cheerleader skirtshort'", "images/KittyDoggy/Kitty_Doggy_Cheerleader_SkirtShort.png", 
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
        #    "R_Over == 'nighty' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",            
        #    "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png", Kitty_Doggy_Over_Dress
            "K_Over == 'black dress' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Over_Dress_Up.png",            
            "K_Over == 'black dress'", "images/KittyDoggy/Kitty_Doggy_Over_Dress.png",            
            "K_Over == 'towel' and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_Over_TowelAss_Up.png",            
            "K_Over == 'towel'", "images/KittyDoggy/Kitty_Doggy_Over_TowelAss.png",
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in K_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),   
            #"(K_Legs == 'orange skirt' or K_Legs == 'cheerleader skirt') and K_Upskirt", "images/KittyDoggy/Kitty_Doggy_HotdogUpskirtOrangeBack.png",  
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png", 
            ),    
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),            
            #"(K_Legs == 'orange skirt' or K_Legs == 'cheerleader skirt') and K_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/KittyDoggy/Kitty_Doggy_HotdogMask_Upskirt.png"),
            #"(K_Legs == 'orange skirt' or K_Legs == 'cheerleader skirt') and K_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/KittyDoggy/Kitty_Doggy_HotdogMask_Upskirt.png"),
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

image Kitty Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(          
    "K_Eyes == 'sexy'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
    "K_Eyes == 'side'", "images/KittyDoggy/Kitty_Doggy_Eyes_Side.png",
    "K_Eyes == 'normal'", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
    "K_Eyes == 'closed'", "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png",
    "K_Eyes == 'manic'", "images/KittyDoggy/Kitty_Doggy_Eyes_Surprised.png",
    "K_Eyes == 'down'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",           
    "K_Eyes == 'stunned'", "images/KittyDoggy/Kitty_Doggy_Eyes_Stunned.png",
    "K_Eyes == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Eyes_Surprised.png",
    "K_Eyes == 'squint'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
    "True", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
    ),
    3
    # This randomizes the time between blinking.
    "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png"
    .25
    repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              #Pussy fucking animations    
image Kitty_Pussy:                                                                                              #Full Animation for speed 0    
    contains:  
        "Kitty_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png",
        # ),                                                                                 #Base
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (169,460) #Out stroke
    contains:
        "Kitty_Doggy_Pussy_FMask"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FMask.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FMask.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FMask.png",
        # ),                                                                                   #Mask

image Kitty_Pussy_Moving:                                                                                       #Full Animation for speed 1
    subpixel True
    contains:                                                                                   #Base
        "Kitty_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png",
        # ),    
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518) 
        xzoom 1
    contains:                                                                                   #Base
        "Kitty_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png",
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
        
            
image Kitty_Pussy_Heading: #This is the image impacted by the mask for the pussy flap in "Kitty_Pussy_Moving"
    contains:                                                                                   #Mask
        "Kitty_Doggy_Pussy_FHeading"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHeading.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHeading.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FHeading.png",
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

image Kitty_Pussy_Fucking2:                                                                                      #Full Animation for speed 2
    contains:                                                                                   #Base
        "Kitty_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png",
        # ),   
    contains:                                                                                   #Base
        "Kitty_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png",
        # ),  
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        

image Kitty_Pussy_Fucking3:                                                                                      #Full Animation for speed 3
    contains:                                                                                   #Base
        "Kitty_Doggy_Pussy_FBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png",
        # ),   
    contains:                                                                                   #Base
        "Kitty_Doggy_Pussy_FHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png",
        # ),   
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
image Kitty_Anal2:                                                                                               #Anal static
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        # ),         
    contains:
        "Kitty_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)
    contains:                                                                                   #Mask
        "Kitty_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask.png",
        # ),  
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5    
    contains:  
        "Kitty_Doggy_Anal_FullCheeks"                                                                                 #Cheeks
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        # ),  


image Kitty_Anal:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "Kitty_Doggy_Asshole_Loose"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Asshole_Loose.png",
        # ),    
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Kitty_Anal_Plug_Stopped:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
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

image Kitty_Anal_Plug:                                                                                               #Anal static Loose
    #contains:                                                                                   #Base
    #    ConditionSwitch(          
    #    "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
    #    "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
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
image Kitty_Doggy_Anal_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        # ),     
    contains:
        "Kitty_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
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
        "Kitty_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask.png",
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
        "Kitty_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        # ),  

image Kitty_Anal_Plug_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        # ),     
        #"images/KittyDoggy/Kitty_Doggy_Anal_HeadingBase.png"    
    contains:
        "Kitty_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
        # ),                                         #Hole
        #"images/KittyDoggy/Kitty_Doggy_Anal_HeadingBase.png"                                       #Hole
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
        "Kitty_Doggy_Anal_FullMask_Plug"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask_Plug.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask_Plug.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask_Plug.png",
        # ),  
        #"images/KittyDoggy/Kitty_Doggy_Anal_HeadingMask_Plug.png"
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
        "Kitty_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        # ),  



image Kitty_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"         
        ypos 0
        block:     
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
            
image Kitty_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
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
            
image Kitty_Doggy_Anal_Fucking:                                                                                       #Animation for speed 2 Ass
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        # ),     
    contains:                                                                                   #Hole
        "Kitty_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Kitty_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
    #     # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/KittyDoggy/Kitty_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal1", "images/KittyDoggy/Kitty_Doggy_AnalMask.png")
    contains:                                                                                   #Mask
        "Kitty_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Kitty_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        # ),  


image Kitty_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"         
        ypos 15#28
        pause .4
        block: 
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28 
            repeat
            
image Kitty_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
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

image Kitty_Doggy_Anal_Fucking2:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        # ),     
    contains:                                                                                   #Hole
        "Kitty_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Kitty_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
    #     # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/KittyDoggy/Kitty_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/KittyDoggy/Kitty_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        "Kitty_Doggy_Anal_FullMask"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Kitty_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        # ),  

image Kitty_Doggy_Anal_Fucking3:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        "Kitty_Doggy_Anal_FullBase"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        # ),      
    contains:                                                                                   #Hole
        "Kitty_Doggy_Anal_FullHole"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
        # ),    
    # contains:
    #     "Kitty_Doggy_Asshole_Loose"
    #     # ConditionSwitch(          
    #     # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
    #     # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
    #     # "True", "images/KittyDoggy/Kitty_Doggy_Asshole_Loose.png",
    #     # ),  
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal3", "images/KittyDoggy/Kitty_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        "Kitty_Doggy_Anal_FullMask3"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask3.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask3.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask3.png",
        # ),  
    contains:                                                                                   #Cheeks
        "Kitty_Doggy_Anal_FullCheeks"
        # ConditionSwitch(          
        # "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        # "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        # ),  


image Kitty_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20             
            pause .05
            repeat
            
image Kitty_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5 
            pause .05
            repeat #.90


image Kitty_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20             
            pause .05
            repeat
            
image Kitty_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
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
label Kitty_Doggy_Launch(Line = "massage"): 
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
    if renpy.showing("Kitty_Doggy"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Kitty_Sprite  
    show Kitty_Doggy at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return
    
label Kitty_Doggy_Reset:
    if not renpy.showing("Kitty_Doggy"):
        return
    $ Kitty_Arms = 2      
    hide Kitty_Doggy
    if K_Gag == "ballgag":
        $ K_Gag = 0
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
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
image Kitty_Doggy_Anal_FullMask:
    contains:                                                                                   #Mask
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask.png",
        ), 
image Kitty_Doggy_Anal_FullBase:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullBase.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png",
        ),
image Kitty_Doggy_Anal_FullHole:      
    contains:                                                                                   #Hole
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullHole.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png",
        ), 
image Kitty_Doggy_Asshole_Loose:  
    contains:
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Asshole_Loose.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Asshole_Loose.png",
        ),  
image Kitty_Doggy_Anal_FullMask3:    
    contains:                                                                                   #Mask
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask3.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask3.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask3.png",
        ),
image Kitty_Doggy_Anal_FullCheeks:
    contains:                                                                                   #Cheeks
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullCheeks.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullCheeks.png",
        ), 

##### Pussy #####

image Kitty_Doggy_Pussy_FBase:
    contains:  
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FBase.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png",
        ),  

image Kitty_Doggy_Pussy_FMask:
    contains:
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FMask.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FMask.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FMask.png",
        ), 

image Kitty_Doggy_Pussy_FHole:
    contains:                                                                                   #Base
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHole.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png",
        ), 

image Kitty_Doggy_Pussy_FHeading:
    contains:
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHeading.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Pussy_FHeading.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Pussy_FHeading.png",
        ), 

image Kitty_Doggy_Anal_FullMask_Plug:
    contains:                                                                                   #Mask
        ConditionSwitch(          
        "K_Tan", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask_Plug.png",
        "K_Tan == 'tan3'", "images/KittyDoggy/Kitty_Doggy_T3Anal_FullMask_Plug.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Anal_FullMask_Plug.png",
        ), 