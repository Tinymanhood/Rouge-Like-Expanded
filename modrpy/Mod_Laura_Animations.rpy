# Basic character Sprites
image Laura_Sprite:
    LiveComposite(
        (402,965),
#        (55,0), ConditionSwitch(                                                                         #hair back temporary
#            "not L_Hair", Null(),
#            "L_Hair == 'wet' or L_Water", "images/LauraSprite/Laura_Sprite_Head_HairBackWet.png",
#            "True", Null(),        
#            ),        
        (0,0), ConditionSwitch(
            #hair back 
            "not newgirl['Laura'].Hair", Null(),
#            "L_Hair == 'wet' or L_Water", "images/LauraSprite/Laura_Sprite_HairbackWet.png",
            "newgirl['Laura'].Hair", "Laura_Sprite_HairBack",   
            "True", Null(),        
            ),   
#        (0,0), ConditionSwitch(            
#            #panties down back 
#            "not newgirl['Laura'].Panties or not newgirl['Laura'].PantiesDown or (newgirl['Laura'].Legs == 'pants' and not newgirl['Laura'].Upskirt)", Null(), 
#            "newgirl['Laura'].Panties == 'sports panties'", "images/LauraSprite/Laura_Sprite_Panties_Sports_DownBack.png",   
#            "True", "images/LauraSprite/Laura_Sprite_Panties_DownBack.png",   
#            ), 
        (0,0), ConditionSwitch(
            #backside of arms
            "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",   
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png", #if newgirl['Laura'].Arms == 1 
            ),     
#        (0,0), ConditionSwitch(
#            #arms wristband
#            "newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Right.png", # one hand up
#            "True", Null(),     
#            ), 
        #body
        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",
        (0,0), ConditionSwitch(
            #pubes 
            "newgirl['Laura'].Pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",   
            "True", Null(),        
            ),      
#        (0,0), ConditionSwitch(
#            #nude lower piercings        
#            "not newgirl['Laura'].Pierce", Null(),  
#            "newgirl['Laura'].Panties and not newgirl['Laura'].PantiesDown", Null(), 
#            "newgirl['Laura'].Legs != 'skirt' and newgirl['Laura'].Legs and not newgirl['Laura'].Upskirt", Null(), #skirt if wearing a skirt
#            "newgirl['Laura'].Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Pierce_Pussy_Barbell.png",  
#            "newgirl['Laura'].Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Pierce_Pussy_Ring.png",  
#            "True", Null(), 
#            ),  
#        (0,0), ConditionSwitch(
#            #Water effect 
#            "newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Water_Body.png",   
#            "True", Null(),        
#            ),      
        (0,0), ConditionSwitch(
            #panties    
            "not newgirl['Laura'].Panties", Null(),
#            "newgirl['Laura'].PantiesDown", ConditionSwitch(                   
#                    #if the panties are down
#                    "not newgirl['Laura'].Legs or newgirl['Laura'].Legs == 'skirt'", ConditionSwitch(                   
#                            #if she's wearing a skirt or nothing else
#                            "newgirl['Laura'].Panties == 'black panties'", "images/LauraSprite/Laura_Sprite_Panties_Leather_Down.png", 
#                            "True", Null(),
#                            ),         
#                    "True", Null(),
#                    ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
#                    "newgirl['Laura'].Wet", ConditionSwitch(   
#                        #if she's not wet
#                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather_Wet.png", 
#                        ),
                    "True", ConditionSwitch(   
                        #if she's wet
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),                    
                    ),    
            ),            
        (0,0), ConditionSwitch(
            #pants    
            "not newgirl['Laura'].Legs", Null(),
            "newgirl['Laura'].Upskirt", ConditionSwitch(                   
                        #if the skirt's up or pants down 
                        "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_SkirtUp.png", 
                        "True", Null(),
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "newgirl['Laura'].Wet", ConditionSwitch(   
                        #if she's not wet
                        "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
                        "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
                        "newgirl['Laura'].Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_YogaWet.png",       
                        "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(   
                        #if she's wet
                        "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
                        "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
                        "newgirl['Laura'].Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_Yoga.png",       
                        "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),    
            ),    
#        (0,0), ConditionSwitch(
#            #clothed lower piercings         
#            "newgirl['Laura'].Legs == 'skirt'", Null(),
#            "newgirl['Laura'].Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the barbell pericings 
#                    "newgirl['Laura'].Legs and not newgirl['Laura'].Upskirt", "images/LauraSprite/Laura_Sprite_Pierce_Pussy_BarOut.png",  
#                    "newgirl['Laura'].Panties and not newgirl['Laura'].PantiesDown", "images/LauraSprite/Laura_Sprite_Pierce_Pussy_BarOut.png", 
#                    "True", Null(),
#                    ),    
#            "newgirl['Laura'].Pierce == 'ring'", ConditionSwitch(   
#                    #if it's the ring pericings
#                    "newgirl['Laura'].Legs and not newgirl['Laura'].Upskirt", "images/LauraSprite/Laura_Sprite_Pierce_Pussy_RingOut.png",  
#                    "newgirl['Laura'].Panties and not newgirl['Laura'].PantiesDown", "images/LauraSprite/Laura_Sprite_Pierce_Pussy_RingOut.png", 
#                    "True", Null(),
#                    ),
#            "True", Null(), 
#            ),    
#        (0,0), ConditionSwitch(
#            #Personal Wetness            
#            "not newgirl['Laura'].Wet", Null(),
#            "newgirl['Laura'].Legs and newgirl['Laura'].Wet <= 1", Null(),
#            "newgirl['Laura'].Legs", "images/LauraSprite/Laura_Sprite_Wet.png",
#            "newgirl['Laura'].Wet == 1", "images/LauraSprite/Laura_Sprite_Wet.png",
#            "True", "images/LauraSprite/Laura_Sprite_Wet.png",       #newgirl['Laura'].Wet >1
#            ),     
#        (0,0), ConditionSwitch(
#            #pussy spunk 
#            "newgirl['Laura'].Legs", Null(),
#            "'pussy' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Pussy.png",
#            "True", Null(), 
#            ),  
#        (0,0), ConditionSwitch(
#            #belly spunk 
#            "'belly' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
#            "True", Null(), 
#            ),    
        
        (0,0), ConditionSwitch(
            #arms midlayer
            "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png", #if newgirl['Laura'].Arms == 1   # Crossed        
            ),  
#        (0,0), ConditionSwitch(
#            #Water effect on arms
#            "not newgirl['Laura'].Water", Null(),             
#            "newgirl['Laura'].Girl_Arms == 1", "images/LauraSprite/Laura_Sprite_Water_Arms1.png",   
#            "True", "images/LauraSprite/Laura_Sprite_Water_Arms2.png", #if newgirl['Laura'].Arms == 1      
#            ),         
        (0,0), ConditionSwitch(
            #arms wristband
            "newgirl['Laura'].Arms == 'wrists' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png", # one hand up
            "newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png", # one hand up
            "True", Null(),     
            ), 
        
        # tits
        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png", 
#        (0,0), ConditionSwitch(
#            #nude peircings      
#            #something about this entry makes all subsequent entries mis-aligned
#            "not newgirl['Laura'].Pierce", Null(),  
#            "newgirl['Laura'].Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the barbell pericings
#                    "newgirl['Laura'].Girl_Arms == 1", "images/LauraSprite/Laura_Sprite_Pierce_Up_Barbell.png",                     
#                    "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Pierce_Up_Barbell.png",   
#                    "newgirl['Laura'].Chest == 'lace bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_Barbell.png",    
#                    "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_Barbell.png",  
#                    "True", "images/LauraSprite/Laura_Sprite_Pierce_Down_Barbell.png",        
#                    ),                        
#            "newgirl['Laura'].Pierce == 'ring'", ConditionSwitch(                      
#                    #if it's the ring pericings                                 
#                    "newgirl['Laura'].Girl_Arms == 1", "images/LauraSprite/Laura_Sprite_Pierce_Up_Ring.png", 
#                    "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Pierce_Up_Ring.png",                          
#                    "newgirl['Laura'].Chest == 'lace bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_Ring.png", 
#                    "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_Ring.png", 
#                    "True", "images/LauraSprite/Laura_Sprite_Pierce_Down_Ring.png", 
#                    ),       
#            "True", Null(),  
#            ),    

        
        (0,0), ConditionSwitch(                          
            #neck
            "newgirl['Laura'].Neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
            "True", Null(), 
            ),  
#        (0,0), ConditionSwitch(
#            #Water effect 
#            "not newgirl['Laura'].Water", Null(),             
#            "newgirl['Laura'].Girl_Arms == 1 or newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Water_TitsUp.png",  
#            "True", "images/LauraSprite/Laura_Sprite_Water_TitsDown.png", #if newgirl['Laura'].Arms == 1      
#            ), 
        (0,0), ConditionSwitch(                                                                        
            #Chest layer
            "newgirl['Laura'].Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
            "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Bra_Sports.png",   
            "newgirl['Laura'].Chest == 'lace bra'", "images/LauraSprite/Laura_Sprite_Bra_Lace.png",   
            "True", Null(),              
            ),    
#        (0,0), ConditionSwitch(                                                                        
#            #clothed peircings        
#            "not newgirl['Laura'].Pierce or (not newgirl['Laura'].Over and not newgirl['Laura'].Chest)", Null(),  
#            "newgirl['Laura'].Pierce == 'barbell'", ConditionSwitch(   
#                    #if it's the barbell pericings
#                    "newgirl['Laura'].Girl_Arms == 1", "images/LauraSprite/Laura_Sprite_Pierce_Up_BarOut.png",  
#                    "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Pierce_Up_BarOut.png",   
#                    "newgirl['Laura'].Chest == 'lace bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_BarOut.png",    
#                    "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_BarOut.png",  
#                    "True", "images/LauraSprite/Laura_Sprite_Pierce_Down_BarOut.png", 
#                    ),    
#            "newgirl['Laura'].Pierce == 'ring'", ConditionSwitch(   
#                    #if it's the ring pericings
#                    "newgirl['Laura'].Girl_Arms == 1", "images/LauraSprite/Laura_Sprite_Pierce_Up_RingOut.png",  
#                    "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Pierce_Up_RingOut.png",   
#                    "newgirl['Laura'].Chest == 'lace bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_RingOut.png",    
#                    "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Pierce_Up_RingOut.png",  
#                    "True", "images/LauraSprite/Laura_Sprite_Pierce_Down_RingOut.png", 
#                    ),                 
#            "True", Null(), 
#            ),    
#        (0,0), ConditionSwitch(
#            #breast spunk      
#            "'tits' in newgirl['Laura'].Spunk", ConditionSwitch(   
#                    #if it's the barbell pericings
#                    "newgirl['Laura'].Girl_Arms == 1", "images/LauraSprite/Laura_Sprite_Spunk_TitsU.png",                     
#                    "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Spunk_TitsU.png",   
#                    "newgirl['Laura'].Chest == 'lace bra'", "images/LauraSprite/Laura_Sprite_Spunk_TitsU.png",    
#                    "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Spunk_TitsU.png",  
#                    "True", "images/LauraSprite/Laura_Sprite_Spunk_TitsD.png",        
#                    ),       
#            "True", Null(),  
#            ),   

        #Head
        (0,0), "Laura_Sprite_Head", #(55,0)
        
        (0,0), ConditionSwitch(
            #arms midlayer
            "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #arms wristband
            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #claws
            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Claws", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
            "True", Null(),     
            ), 
        
#        (0,0), ConditionSwitch( 
#            #hand spunk 
#            "newgirl['Laura'].Girl_Arms != 2 or 'hand' not in newgirl['Laura'].Spunk", Null(),  
#            "'mouth' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_HandM.png", 
#            "True", "images/LauraSprite/Laura_Sprite_Spunk_Hand.png",   
#            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not newgirl['Laura'].Held or newgirl['Laura'].Girl_Arms != 2", Null(), 
#            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Held == 'phone'", "images/LauraSprite/Laura_held_phone.png",
#            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Held == 'dildo'", "images/LauraSprite/Laura_held_dildo.png",
#            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Held == 'vibrator'", "images/LauraSprite/Laura_held_vibrator.png",
#            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Held == 'panties'", "images/LauraSprite/Laura_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Laura is masturbating using Trigger3 actions
            "newgirl['Laura'].Loc == 'bg teacher'", Null(),
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Laura'", Null(),
            
            #this is not a lesbian thing, and a trigger is set, and Laura is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_LSelf",  
            "Trigger3 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_L", 
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_L",   
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_L",
                        #else, fondle both
                    ),  
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_L",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_L",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_L",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_L",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_L",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "newgirl['Laura'].Loc == 'bg teacher'", Null(),
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Laura'", Null(), 
            
            #Laura is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Laura'].Lust >= 70", "GirlFingerPussy_L",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_L",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_L",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                
            #UI tool for Trigger1(primary) actions
            "newgirl['Laura'].Loc == 'bg teacher'", Null(),
            "not Trigger or Ch_Focus != 'Laura'", Null(),
            
            # Laura is primary and a sex trigger is active
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_L",
            "Trigger == 'fondle thighs'", "GropeThigh_L",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_L",
            "Trigger == 'suck breasts'", "LickRightBreast_L",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_L",
            "Trigger == 'fondle pussy'", "GropePussy_L",
            "Trigger == 'lick pussy'", "Lickpussy_L",
            "Trigger == 'vibrator pussy'", "VibratorPussy_L",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_L",
            "Trigger == 'vibrator anal'", "VibratorAnal_L",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_L",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "newgirl['Laura'].Loc == 'bg teacher'", Null(),
            "not Trigger2 or Ch_Focus != 'Laura'", Null(),
            
            #Laura is primary and an offhand trigger is active            
            "Trigger2 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_L", 
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_L",
                        #else, fondle right
                    ),  
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_L",       
                #When sucking right breast, vibrator left            
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_L",        
            "Trigger2 == 'fondle pussy'", "GropePussy_L",
            "Trigger2 == 'lick pussy'", "Lickpussy_L",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_L",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_L",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_L",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_L",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_L",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "newgirl['Laura'].Loc == 'bg teacher'", Null(),
            "not Trigger4 or Ch_Focus != 'Laura'", Null(),
            
            # There is a threesome trigger set and Laura is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Laura'].Lust >= 70", "GirlFingerPussy_L",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_L",            
            "Trigger4 == 'lick pussy'", "Lickpussy_L",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_L", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_L",              
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_L",   
                        #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_L", 
#                        #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_L", 
#                        #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_L",
                        #else, fondle right
                    ),                  
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),    
        (0,0), ConditionSwitch(             
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Laura is secondary)
            "newgirl['Laura'].Loc == 'bg teacher'", Null(),
            "Trigger != 'lesbian' or Ch_Focus == 'Laura' or not Trigger3", Null(),
            
            # If there is a Trigger3 and Laura is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Laura'].Lust >= 70", "GirlFingerPussy_L",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_L",            
            "Trigger3 == 'lick pussy'", "Lickpussy_L",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_L", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_L",              
            "Trigger3 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_L",   
                        #When zero is working the right breast, fondle left                                                  
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_L", 
                        #When zero is working the left breast, fondle right                                         
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_L", 
                        #When zero is working the right breast, fondle left 
                    "True", "GirlGropeRightBreast_L",
                        #else, fondle right
                    ),                             
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),         
        )                
    anchor (0.6, 0.0)   
    yoffset 15
    zoom .75                

image Laura_Sprite_HairBack:
    "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png"         
    anchor (0.6, 0.0)                
    zoom .5                   
    
image Laura_Sprite_Head:
    LiveComposite(
        (806,806),         
        (0,0), ConditionSwitch(
                # Face background plate
                "newgirl['Laura'].Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "newgirl['Laura'].Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(                                                                         #Mouths        
            "newgirl['Laura'].Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "newgirl['Laura'].Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "newgirl['Laura'].Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
            "newgirl['Laura'].Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "newgirl['Laura'].Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "newgirl['Laura'].Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "newgirl['Laura'].Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
            "newgirl['Laura'].Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
            "newgirl['Laura'].Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
            "newgirl['Laura'].Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
#            "newgirl['Laura'].Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",         
            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),   
        
#        (0,0), ConditionSwitch(                                                                         #Mouth spunk               
#            "'mouth' not in newgirl['Laura'].Spunk", Null(),
#            "newgirl['Laura'].Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Head_Spunk_MouthOpen.png",            
#            "newgirl['Laura'].Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Head_Spunk_MouthTongue.png",            
#            "True", "images/LauraSprite/Laura_Sprite_Head_Spunk_Mouth.png",  
#            ),  
                                                                             
        (0,0), ConditionSwitch(                                                                       
            #brows
            "newgirl['Laura'].Blush >= 2", ConditionSwitch(
                    "newgirl['Laura'].Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "newgirl['Laura'].Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "newgirl['Laura'].Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "newgirl['Laura'].Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
                    "newgirl['Laura'].Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "newgirl['Laura'].Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "newgirl['Laura'].Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "newgirl['Laura'].Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "newgirl['Laura'].Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
                    "newgirl['Laura'].Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Laura Blink",     #Eyes          
#        (0,0), ConditionSwitch(                                                                         #facial spunk               
#            "'facial' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Head_Spunk_Face.png",             
#            "True", Null(),
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #Hair
            "not newgirl['Laura'].Hair", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Head_HairWet.png",
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),        
#        (0,0), ConditionSwitch(                                                                         #Hair Water
#            "not newgirl['Laura'].Water", Null(),
#            "newgirl['Laura'].Hair == 'wet'", "images/LauraSprite/Laura_Sprite_Head_Water.png",
#            "True", "images/LauraSprite/Laura_Sprite_Head_Water.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #hair spunk               
#            "'hair' in newgirl['Laura'].Spunk and (newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water)", "images/LauraSprite/Laura_Sprite_Head_Spunk_HairWet.png",                         
#            "'hair' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Head_Spunk_HairWave.png",              
#            "True", Null(),
#            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .5   

image Laura Blink:
    ConditionSwitch(
    "newgirl['Laura'].Eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
    "newgirl['Laura'].Eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
    "newgirl['Laura'].Eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
    "newgirl['Laura'].Eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",    
    "newgirl['Laura'].Eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
    "newgirl['Laura'].Eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
    "newgirl['Laura'].Eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
    "newgirl['Laura'].Eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
    "newgirl['Laura'].Eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "newgirl['Laura'].Eyes == 'squint'", "Laura_Squint",
    "True", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/LauraSprite/Laura_Sprite_Eyes_Closed.png"
    .25
    repeat                

image Laura_Squint:            
    "images/LauraSprite/Laura_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/LauraSprite/Laura_Sprite_Eyes_Squint.png"
    .25
    repeat             
# End Laura Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Laura Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
       
        
        
label L_Kissing_Launch(T = Trigger):    
    call Laura_Hide
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(newgirl['Laura'].SpriteLoc) zorder newgirl['Laura'].GirlLayer
    show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl['Laura'].GirlLayer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label L_Kissing_Smooch:   
    call LauraFace("kiss")  
    show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl['Laura'].GirlLayer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos newgirl['Laura'].SpriteLoc zoom 1      
    show Laura_Sprite at SpriteLoc(newgirl['Laura'].SpriteLoc) zorder newgirl['Laura'].GirlLayer:
        zoom 1
    call LauraFace("sexy")  
    return
            
label L_Breasts_Launch(T = Trigger):    
    call Laura_Hide
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(newgirl['Laura'].SpriteLoc) zorder newgirl['Laura'].GirlLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
        
label L_Pussy_Launch(T = Trigger):
    call Laura_Hide    
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(newgirl['Laura'].SpriteLoc) zorder newgirl['Laura'].GirlLayer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label L_Pos_Reset(Pose = 0):    
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(newgirl['Laura'].SpriteLoc) zorder newgirl['Laura'].GirlLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1
    show Laura_Sprite zorder newgirl['Laura'].GirlLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1  
        alpha 1
        pos (newgirl['Laura'].SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Laura_Hide:
        if renpy.showing("Laura_SexSprite"):
            call Laura_Sex_Reset
        hide Laura_SexSprite
        hide Laura_HJ_Animation
        hide Laura_BJ_Animation
        hide Laura_TJ_Animation 
        return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_L:    
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

image GropeRightBreast_L:    
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
image LickRightBreast_L:   
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
            
image LickLeftBreast_L:   
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

image GropeThigh_L: 
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

image GropePussy_L: 
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

image FingerPussy_L: 
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
            
image Lickpussy_L:   
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

image VibratorRightBreast_L: 
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

image VibratorLeftBreast_L: 
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
            
image VibratorPussy_L: 
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

image VibratorAnal_L: 
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
            
image VibratorPussyInsert_L: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_L: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_L: 
    contains:
        "GirlGropeLeftBreast_L"
    contains:
        "GirlGropeRightBreast_L"
    
image GirlGropeLeftBreast_L:  
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

image GirlGropeRightBreast_L:    
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

image GirlGropeThigh_L: 
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

image GirlGropePussy_LSelf:
    contains:
        "GirlGropePussy_L"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)
    
image GirlGropePussy_L: 
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

image GirlFingerPussy_L: 
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

# Start Laura Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label LauraFace(Emote = newgirl['Laura'].Lmote, B = newgirl['Laura'].Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state                 
        $ Emote = newgirl['Laura'].Emote if Emote == 5 else Emote
        $ B = newgirl['Laura'].Blush if B == 5 else B
        
        if (newgirl['Laura'].Forced or "angry" in newgirl['Laura'].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl['Laura'].ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl['Laura'].Mouth = "normal"
                $ newgirl['Laura'].Brows = "normal"
                $ newgirl['Laura'].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl['Laura'].Mouth = "kiss"
                $ newgirl['Laura'].Brows = "angry"
                $ newgirl['Laura'].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl['Laura'].Mouth = "lipbite"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl['Laura'].Mouth = "normal"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl['Laura'].Mouth = "kiss"
                $ newgirl['Laura'].Brows = "confused"
                $ newgirl['Laura'].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl['Laura'].Mouth = "kiss"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl['Laura'].Mouth = "tongue"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl['Laura'].Mouth = "lipbite"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "surprised"
                $ newgirl['Laura'].Blush = 1
        elif Emote == "sad":
                $ newgirl['Laura'].Mouth = "sad"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl['Laura'].Mouth = "sad"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl['Laura'].Mouth = "lipbite"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "squint"
        elif Emote == "smile":
                if newgirl['Laura'].Love >= 700:
                    $ newgirl['Laura'].Mouth = "smile"
                else:
                    $ newgirl['Laura'].Mouth = "smirk"                
                $ newgirl['Laura'].Brows = "normal"
                $ newgirl['Laura'].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl['Laura'].Mouth = "sucking"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl['Laura'].Mouth = "kiss"
                $ newgirl['Laura'].Brows = "surprised"
                $ newgirl['Laura'].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl['Laura'].Mouth = "smile"
                $ newgirl['Laura'].Brows = "surprised"
                $ newgirl['Laura'].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl['Laura'].Mouth = "sad"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl['Laura'].Mouth = "smile"
                $ newgirl['Laura'].Brows = "sad"
                $ newgirl['Laura'].Eyes = "surprised"
        elif Emote == "sly":
                if newgirl['Laura'].Love >= 700:
                    $ newgirl['Laura'].Mouth = "smile"
                else:
                    $ newgirl['Laura'].Mouth = "smirk" 
                $ newgirl['Laura'].Brows = "confused"
                $ newgirl['Laura'].Eyes = "squint"
            
        if M:
                $ newgirl['Laura'].Eyes = "surprised"        
        if B > 1:
                $ newgirl['Laura'].Blush = 2
        elif B:
                $ newgirl['Laura'].Blush = 1
        else:
                $ newgirl['Laura'].Blush = 0
        
        if Mouth:
                $ newgirl['Laura'].Mouth = Mouth
        if Eyes:
                $ newgirl['Laura'].Eyes = Eyes
        if Brows:
                $ newgirl['Laura'].Brows = Brows
        
        return
        
        
# Laura's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label LauraWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call L_Pos_Reset
                    "Face":
                        call L_Kissing_Launch(0)
                    "Body":
                        call L_Pussy_Launch(0)
                    "Back":
                        jump LauraWardrobe 
        # Outfits
#        "Teacher outfit":
#            $ L_Outfit = "teacher"
#            call LauraOutfit
#        "Super outfit":
#            $ L_Outfit = "costume"
#            call LauraOutfit
        "Nude":
            $ newgirl['Laura'].Over = 0
            $ newgirl['Laura'].Chest = 0
            $ newgirl['Laura'].Legs = 0
            $ newgirl['Laura'].Panties = 0
            $ newgirl['Laura'].Gloves = 0
            $ newgirl['Laura'].Neck = 0
#            $ L_Outfit = "nude"
#            call LauraOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [newgirl[Laura].Over]" if newgirl['Laura'].Over:
                        $ newgirl['Laura'].Over = 0
                    "Add Jacket":
                        $ newgirl['Laura'].Over = "jacket"  
                    "Add Towel":
                        $ newgirl['Laura'].Over = "towel" 
                    "Add nighty":
                        $ newgirl['Laura'].Over = "nighty"   
                    "Back":
                        jump LauraWardrobe                
        "Chests":            
            while True:
                menu:
                    # Tops    
                    "Remove [newgirl[Laura].Chest]" if newgirl['Laura'].Chest:
                        $ newgirl['Laura'].Chest = 0
                    "Add leather bra":
                        $ newgirl['Laura'].Chest = "leather bra"
                    "Add sports bra":
                        $ newgirl['Laura'].Chest = "sports bra"
#                    "Add buttoned tank top" if newgirl['Laura'].Over != "mesh top":
#                        $ newgirl['Laura'].Chest = "buttoned tank"
                    "Add lace bra":
                        $ newgirl['Laura'].Chest = "lace bra"
#                    "Add bra":
#                        $ newgirl['Laura'].Chest = "bra"                            
#                    "Toggle Piercings":
#                        if newgirl['Laura'].Pierce == "ring":
#                            $ newgirl['Laura'].Pierce = "barbell"
#                        elif newgirl['Laura'].Pierce == "barbell":
#                            $ newgirl['Laura'].Pierce = 0
#                        else:
#                            $ newgirl['Laura'].Pierce = "ring"
                    "Back":
                        jump LauraWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if newgirl['Laura'].Legs:     
                        $ newgirl['Laura'].Legs = 0
                    "Add leather pants":
                        $ newgirl['Laura'].Legs = "leather pants"
                        $ newgirl['Laura'].Upskirt = 0
                    "Add mesh pants":
                        $ newgirl['Laura'].Legs = "mesh pants"
                        $ newgirl['Laura'].Upskirt = 0
#                    "Add skirt":
#                        $ newgirl['Laura'].Legs = "skirt"
#                        $ newgirl['Laura'].Upskirt = 0
                    "Toggle upskirt":
                        if newgirl['Laura'].Upskirt:
                            $ newgirl['Laura'].Upskirt = 0
                        else:
                            $ newgirl['Laura'].Upskirt = 1
                    "Back":
                        jump LauraWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
#                    "Hose":
#                        menu:
#                            "Add hose":     
#                                $ L_Hose = "stockings"  
#                            "Add garter":     
#                                $ L_Hose = "garterbelt"  
#                            "Add stockings and garter":     
#                                $ L_Hose = "stockings and garterbelt"  
#                            "Add pantyhose":     
#                                $ L_Hose = "pantyhose"   
#                            "Add tights":     
#                                $ L_Hose = "tights"   
#                            "Add ripped hose":     
#                                $ L_Hose = "ripped pantyhose"   
#                            "Add ripped tights":     
#                                $ L_Hose = "ripped tights"   
#                            "Add tights":     
#                                $ L_Hose = "tights"    
#                            "Remove hose" if L_Hose:     
#                                $ L_Hose = 0  

#                    "toggle boots":    
#                        if not L_Boots:
#                            $ L_Boots = "thigh boots"   
#                        else:
#                            $ L_Boots = 0     
                        
                    "Remove panties" if newgirl['Laura'].Panties:     
                        $ newgirl['Laura'].Panties = 0     
                    "Add black panties":
                        $ newgirl['Laura'].Panties = "black panties"
#                    "Add shorts":
#                        $ newgirl['Laura'].Panties = "shorts"
                    "Add sports panties":
                        $ newgirl['Laura'].Panties = "sports panties"  
#                    "Add lace panties":
#                        $ newgirl['Laura'].Panties = "lace panties"    
                    "pull down-up panties":
                        if newgirl['Laura'].PantiesDown:
                            $ newgirl['Laura'].PantiesDown = 0
                        else:
                            $ newgirl['Laura'].PantiesDown = 1
                    "Back":
                        jump LauraWardrobe    
        "Face":
            while True:
                menu: 
                    "Brows=[newgirl[Laura].Brows], Eyes=[newgirl[Laura].Eyes], Mouth=[newgirl[Laura].Mouth]"
                    "Emotions":
                            call LauraEmotionEditor
                    "Toggle Brows":
                            if newgirl['Laura'].Brows == "normal":
                                $ newgirl['Laura'].Brows = "angry"
                            elif newgirl['Laura'].Brows == "angry":
                                $ newgirl['Laura'].Brows = "confused"
                            elif newgirl['Laura'].Brows == "confused":
                                $ newgirl['Laura'].Brows = "sad"
                            elif newgirl['Laura'].Brows == "sad":
                                $ newgirl['Laura'].Brows = "surprised"
                            else:
                                $ newgirl['Laura'].Brows = "normal"
                    "Toggle Eyes Emotions":
                            if newgirl['Laura'].Eyes == "normal":                          
                                $ newgirl['Laura'].Eyes = "surprised"
                            elif newgirl['Laura'].Eyes == "surprised":
                                $ newgirl['Laura'].Eyes = "sexy"
                            elif newgirl['Laura'].Eyes == "sexy":
                                $ newgirl['Laura'].Eyes = "squint"
                            elif newgirl['Laura'].Eyes == "squint":
                                $ newgirl['Laura'].Eyes = "closed"
                            else:
                                $ newgirl['Laura'].Eyes = "normal"
                    "Toggle Eyes Directions":
                            if newgirl['Laura'].Eyes == "normal":
                                $ newgirl['Laura'].Eyes = "side"
                            elif newgirl['Laura'].Eyes == "side":
                                $ newgirl['Laura'].Eyes = "down"
                            elif newgirl['Laura'].Eyes == "down":
                                $ newgirl['Laura'].Eyes = "leftside"
                            elif newgirl['Laura'].Eyes == "leftside":
                                $ newgirl['Laura'].Eyes = "stunned"
                            else:
                                $ newgirl['Laura'].Eyes = "normal"  
                    "Toggle Mouth Normal":
                            if newgirl['Laura'].Mouth  == "normal":
                                $ newgirl['Laura'].Mouth = "sad"
                            elif newgirl['Laura'].Mouth == "sad":
                                $ newgirl['Laura'].Mouth = "smile"
                            elif newgirl['Laura'].Mouth == "smile":
                                $ newgirl['Laura'].Mouth = "surprised"
                            else:
                                $ newgirl['Laura'].Mouth = "normal"  
                    "Toggle Mouth Sexy":
                            if newgirl['Laura'].Mouth  == "normal":
                                $ newgirl['Laura'].Mouth = "kiss"
                            elif newgirl['Laura'].Mouth == "kiss":
                                $ newgirl['Laura'].Mouth = "sucking"
                            elif newgirl['Laura'].Mouth == "sucking":
                                $ newgirl['Laura'].Mouth = "tongue"
                            elif newgirl['Laura'].Mouth == "tongue":
                                $ newgirl['Laura'].Mouth = "lipbite"
                            else:
                                $ newgirl['Laura'].Mouth = "normal"  
                    "Toggle Blush":
                        if newgirl['Laura'].Blush == 1:
                            $ newgirl['Laura'].Blush = 2
                        elif newgirl['Laura'].Blush:
                            $ newgirl['Laura'].Blush = 0
                        else:
                            $ newgirl['Laura'].Blush = 1
                            
                    "Back":
                            jump LauraWardrobe    
        "Misc":
            while True:
                menu: 
                    "Toggle Arm pose":
                        if newgirl['Laura'].Girl_Arms == 1:
                            $ newgirl['Laura'].Girl_Arms = 2
                        else:
                            $ newgirl['Laura'].Girl_Arms = 1
                    "Toggle Claws":
                        if newgirl['Laura'].Claws:
                            $ newgirl['Laura'].Claws = 0
                        else:
                            $ newgirl['Laura'].Claws = 1
                    "Toggle Wetness" if False:
                        if not newgirl['Laura'].Wet:
                            $ newgirl['Laura'].Wet = 1
                        elif newgirl['Laura'].Wet == 1:
                            $ newgirl['Laura'].Wet = 2
                        else:
                            $ newgirl['Laura'].Wet  = 0
                    "Toggle wet look" if False:
                        if not newgirl['Laura'].Water:
                            $ newgirl['Laura'].Water = 1
                        elif newgirl['Laura'].Water == 1:
                            $ newgirl['Laura'].Water = 3
                        else:
                            $ newgirl['Laura'].Water  = 0
                    "Toggle pubes":
                        if not newgirl['Laura'].Pubes:
                            $ newgirl['Laura'].Pubes = 1
                        else:
                            $ newgirl['Laura'].Pubes = 0
                    "Toggle Pussy Spunk" if False:
                        if "pussy" in newgirl['Laura'].Spunk:
                            $ newgirl['Laura'].Spunk.remove("pussy")
                        else:
                            $ newgirl['Laura'].Spunk.append("pussy")
                    "Toggle Piercings":
                        if newgirl['Laura'].Pierce == "ring":
                            $ newgirl['Laura'].Pierce = "barbell"
                        elif newgirl['Laura'].Pierce == "barbell":
                            $ newgirl['Laura'].Pierce = 0
                        else:
                            $ newgirl['Laura'].Pierce = "ring"
                    "Add leash choker" if not newgirl['Laura'].Neck:
                        $ newgirl['Laura'].Neck = "leash choker"
                    "Remove choker" if newgirl['Laura'].Neck:
                        $ newgirl['Laura'].Neck = 0
                        
                    "Add wristbands" if not newgirl['Laura'].Arms:
                        $ newgirl['Laura'].Arms = "wrists"
                    "Remove Gloves" if newgirl['Laura'].Arms:
                        $ newgirl['Laura'].Arms = 0
                    "Back":
                        jump LauraWardrobe               
#        "Set Custom Outfit #1.":
#            $ newgirl['Laura'].Custom[0] = 1
#            $ newgirl['Laura'].Custom[1] = newgirl['Laura'].Arms
#            $ newgirl['Laura'].Custom[2] = newgirl['Laura'].Legs
#            $ newgirl['Laura'].Custom[3] = newgirl['Laura'].Over
#            $ newgirl['Laura'].Custom[4] = newgirl['Laura'].Under #fix, this can be changed to something else, no longer necessary
#            $ newgirl['Laura'].Custom[5] = newgirl['Laura'].Chest
#            $ newgirl['Laura'].Custom[6] = newgirl['Laura'].Panties 
#            $ newgirl['Laura'].Custom[7] = newgirl['Laura'].Pubes 
#            $ newgirl['Laura'].Custom[8] = newgirl['Laura'].Hair
#            $ newgirl['Laura'].Custom[9] = newgirl['Laura'].Hose
#        "Wear Custom Outfit #[newgirl[Laura].Custom[0]]." if newgirl['Laura'].Custom[0]:
#            $ Line = newgirl['Laura'].Outfit
#            $ newgirl['Laura'].Outfit = "custom1"
#            call RogueOutfit
#            $ newgirl['Laura'].Outfit = Line
        "Nothing":
            return
    jump LauraWardrobe
return

label LauraEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ newgirl['Laura'].Lmote = "normal"
                    call LauraFace
                "Angry":
                    $ newgirl['Laura'].Lmote = "angry"
                    call LauraFace
                "Smiling":
                    $ newgirl['Laura'].Lmote = "smile"
                    call LauraFace
                "Sexy":
                    $ newgirl['Laura'].Lmote = "sexy"
                    call LauraFace
                "Suprised":
                    $ newgirl['Laura'].Lmote = "surprised"
                    call LauraFace
                "Bemused":
                    $ newgirl['Laura'].Lmote = "bemused"
                    call LauraFace
                "Manic":
                    $ newgirl['Laura'].Lmote = "manic"
                    call LauraFace
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ newgirl['Laura'].Lmote = "sad"
                    call LauraFace
                "Sucking":
                    $ newgirl['Laura'].Lmote = "sucking"
                    call LauraFace
                "kiss":
                    $ newgirl['Laura'].Lmote = "kiss"
                    call LauraFace
                "Tongue":
                    $ newgirl['Laura'].Lmote = "tongue"
                    call LauraFace
                "confused":
                    $ newgirl['Laura'].Lmote = "confused"
                    call LauraFace
                "Closed":
                    $ newgirl['Laura'].Lmote = "closed"
                    call LauraFace
                "Down":
                    $ newgirl['Laura'].Lmote = "down"
                    call LauraFace
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ newgirl['Laura'].Lmote = "sadside"
                    call LauraFace
                "Startled":
                    $ newgirl['Laura'].Lmote = "startled"
                    call LauraFace
                "Perplexed":
                    $ newgirl['Laura'].Lmote = "perplexed"
                    call LauraFace
                "Sly":
                    $ newgirl['Laura'].Lmote = "sly"
                    call LauraFace
        "Toggle Mouth Spunk":
            if "mouth" in newgirl['Laura'].Spunk:
                $ newgirl['Laura'].Spunk.remove("mouth")
            else:
                $ newgirl['Laura'].Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in newgirl['Laura'].Spunk:
                $ newgirl['Laura'].Spunk.remove("hand")
            else:
                $ newgirl['Laura'].Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in newgirl['Laura'].Spunk and "hair" not in newgirl['Laura'].Spunk:
                $ newgirl['Laura'].Spunk.append("hair")
            elif "facial" in newgirl['Laura'].Spunk:
                $ newgirl['Laura'].Spunk.remove("facial")                
                $ newgirl['Laura'].Spunk.remove("hair")
            else:
                $ newgirl['Laura'].Spunk.append("facial")
            
        "Blush":
            if newgirl['Laura'].Blush == 2:
                $ newgirl['Laura'].Blush = 0
            elif newgirl['Laura'].Blush:
                $ newgirl['Laura'].Blush = 2
            else:
                $ newgirl['Laura'].Blush = 1  
        "Exit.":
            return
    jump LauraEmotionEditor
return