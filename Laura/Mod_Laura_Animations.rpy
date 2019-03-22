# Basic character Sprites

image Laura_Sprite:
    LiveComposite(        
        (402,965),
#        (55,0), ConditionSwitch(                                                                         #hair back temporary
#            "not newgirl['Laura'].Hair", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Head_HairBackWet.png",
#            "True", Null(),        
#            ),        
        (0,0), ConditionSwitch(
            #hair back 
            "not newgirl['Laura'].Hair", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_HairbackWet.png",
            "renpy.showing('Laura_BJ_Animation')", Null(), 
            "newgirl['Laura'].Hair", "Laura_Sprite_HairBack",   
            "True", Null(),        
            ),   
        (0,0), ConditionSwitch(            
            #panties down back 
            "not newgirl['Laura'].Panties or not newgirl['Laura'].PantiesDown or (newgirl['Laura'].Legs == 'pants' and not newgirl['Laura'].Upskirt)", Null(), 
            "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",   
            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",   
            ), 
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
            #stockings    
            "newgirl['Laura'].Hose == 'stockings' or newgirl['Laura'].Hose == 'stockings and garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            #garterbelt    
            "newgirl['Laura'].Hose == 'stockings and garterbelt' or newgirl['Laura'].Hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
            "True", Null(),
            ),              
        (0,0), ConditionSwitch(
            #panties    
            "not newgirl['Laura'].Panties", Null(),
            "newgirl['Laura'].PantiesDown", ConditionSwitch(                   
                    #if the panties are down
                    "not newgirl['Laura'].Legs or newgirl['Laura'].Upskirt or newgirl['Laura'].Legs == 'skirt'", ConditionSwitch(                   
                            #if she's wearing a skirt or nothing else                    
                            "newgirl['Laura'].Panties == 'wolvie panties' and newgirl['Laura'].Wet", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png", 
                            "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",                             
                            "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", 
                            "newgirl['Laura'].Panties == 'black panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", #fix
                            "True", Null(),
                            ),         
                    "True", Null(),
                    ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
                    "newgirl['Laura'].Wet", ConditionSwitch(   
                        #if she's  wet                            
                        "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                        "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),
                    "True", ConditionSwitch(   
                        #if she's not wet                            
                        "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),                    
                    ),    
            ),            
        (0,0), ConditionSwitch(
            #pants    
            "not newgirl['Laura'].Legs", Null(),
            "newgirl['Laura'].Upskirt", ConditionSwitch(                
                        #if the skirt's up or pants down 
                        "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png", 
                        "True", Null(),                       
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "newgirl['Laura'].Wet", ConditionSwitch(   
                        #if she's not wet
                        "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
                        "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
#                        "newgirl['Laura'].Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_YogaWet.png",       
                        "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    "True", ConditionSwitch(   
                        #if she's wet
                        "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
                        "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
#                        "newgirl['Laura'].Legs == 'yoga pants'", "images/LauraSprite/Laura_Sprite_Pants_Yoga.png",       
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
        
        (0,0), ConditionSwitch(
            #L Over under
            "newgirl['Laura'].Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png", # one hand up
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
            "newgirl['Laura'].Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",   
            "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Bra_Sports.png",   
            "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",   
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

        (0,0), ConditionSwitch(
            #L Over
            "newgirl['Laura'].Over == 'jacket' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png", # one hand up
            "newgirl['Laura'].Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png", # one hand up
            "newgirl['Laura'].Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
            "True", Null(),     
            ), 
        
        #Head
#        (0,0), "Laura_Sprite_Head", #(55,0)
        (0,0), ConditionSwitch(
            # head
            "renpy.showing('Laura_BJ_Animation')", Null(),  
            "True", "Laura_Sprite_Head",   
            ),         
        (0,0), ConditionSwitch(
            #arms toplayer
            "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #arms wristband
            "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #jacket arm toplayer
            "newgirl['Laura'].Over == 'jacket' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png", # one hand up
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
            #Laura is primary and a sex trigger is active
            "not Trigger or Ch_Focus != 'Laura'", Null(),            
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
            "not Trigger4 or Ch_Focus != 'Laura'", Null(),
            
            # There is a threesome trigger set and Laura is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Laura'].Lust >= 70", "GirlFingerPussy_L",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_L",            
            "Trigger4 == 'lick pussy'", "Lickpussy_L",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_L", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_L",      
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_L", #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_L",  #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_L", #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_L",#else, fondle right
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
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in newgirl['Laura'].Spunk", Null(),
            "renpy.showing('Laura_BJ_Animation') and Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),    
        (0,0), ConditionSwitch(#Mouths 
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
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
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in newgirl['Laura'].Spunk", Null(),
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png", #and Speed >= 2
            "newgirl['Laura'].Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "newgirl['Laura'].Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "newgirl['Laura'].Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
            "newgirl['Laura'].Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "newgirl['Laura'].Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "newgirl['Laura'].Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "newgirl['Laura'].Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
            "newgirl['Laura'].Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
            "newgirl['Laura'].Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
            "newgirl['Laura'].Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),                                                        
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
        (0,0), ConditionSwitch(                
            #Hair mid
            "newgirl['Laura'].Over == 'jacket'", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Head_HairWet.png",
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not newgirl['Laura'].Hair", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Head_HairWet.png",
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not newgirl['Laura'].Water", Null(),
#            "newgirl['Laura'].Hair == 'wet'", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
            "'facial' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
            "True", Null(),
            ),  
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




# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                 
# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                 

              
image Laura_BJ_Animation:                
    #core blowjob animation   
    contains:
        ConditionSwitch(
            # Laura's upper body
#            "P_Sprite", ConditionSwitch(                                                               
#                    # If during sex
            "Speed == 1", "Laura_BJ_Body_1",#Licking
            "Speed == 2", "Laura_BJ_Body_2",#Heading
            "Speed == 3", "Laura_BJ_Body_3",#Sucking
            "Speed == 4", "Laura_BJ_Body_4",#Deepthroat
            "Speed == 5", "Laura_BJ_Body_5",#Cumming high
            "Speed == 6", "Laura_BJ_Body_6",#Cumming deep
#                    "True",     "Laura_BJ_Body_0",#Static
#                    ),
            "True","Laura_BJ_Body_0",#Static
            )   
    zoom 1.35            
    anchor (.5,.5)                 
    pos (600,605)            
                 

#  BJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

                
#image Laura_Sprite_BJ_SuckingMask:
#    contains:
#            "images/LauraSprite/Laura_Sprite_SuckingMask.png"
##            pos (200,50)
#    contains:
#            "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png"
#    pos (100,150)
#    alpha .8
            
image Laura_Sprite_BJ_HairBack:          
    #This is the version of the hair back used in the BJ pose
    "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png"      
                    
image Laura_Sprite_BJ_Head:
    #This is the version of the head used in the BJ pose
    LiveComposite(
        (806,806),         
        (0,0), ConditionSwitch(
                # Face background plate
                "newgirl['Laura'].Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "newgirl['Laura'].Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in newgirl['Laura'].Spunk", Null(),
            "Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),    
        (0,0), ConditionSwitch(#Mouths 
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png",   #sucking       
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",     #licking 
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
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in newgirl['Laura'].Spunk", Null(),
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png",   #sucking       
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",     #licking             
            "newgirl['Laura'].Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "newgirl['Laura'].Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "newgirl['Laura'].Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
            "newgirl['Laura'].Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "newgirl['Laura'].Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "newgirl['Laura'].Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "newgirl['Laura'].Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
            "newgirl['Laura'].Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
            "newgirl['Laura'].Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
            "newgirl['Laura'].Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),     
        (0,0), ConditionSwitch(#Mouth spunk over 
            "Speed >= 2 and 'mouth' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png",   #sucking  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(#wet tongue
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Wet_Tongue.png",     #licking   
            "True", Null(),
            ),                                                              
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
        (0,0), ConditionSwitch(                
            #Hair mid
            "newgirl['Laura'].Over == 'jacket'", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Head_HairWet.png",
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not newgirl['Laura'].Hair", Null(),
#            "newgirl['Laura'].Hair == 'wet' or newgirl['Laura'].Water", "images/LauraSprite/Laura_Sprite_Head_HairWet.png",
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not newgirl['Laura'].Water", Null(),
#            "newgirl['Laura'].Hair == 'wet'", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
            "'facial' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
            "True", Null(),
            ),  
        )                
#    anchor (0.6, 0.0)                
#    zoom .5      
        
image Laura_BlowCock_Mask:   
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat                    


#image Laura_BlowCock_Mask_3:   
#    This is a mask used by the blockcock during the Speed 4 deep throat animation
#    it is a block moving in and out to prevent the cock sticking out the back. 
#    contains:
#        Solid("#159457", xysize=(190,950))
#        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   

image Laura_BJ_Body_0:                                                                        
    #Her Body in the BJ pose, static
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat           
    contains:       
            #base body
            "Laura_Sprite"   
            subpixel True   
            pos (650,800)#(673,740) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            parallel:
                pause 0.1
                ease 1.1 ypos 810 #bottom
                pause 0.2
                ease 1.1 ypos 800 #top
                pause 0.1
                repeat    
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30    
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
#                easeout .1 rotate 1 #bottom .6
                ease .15 rotate -5 #bottom
                pause 0.4
                ease 1.95 rotate 10 #top
                repeat
            parallel:
                pause 0.1
#                easeout .1 pos (407,262) #bottom(637,168)
                ease .15 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.95 pos (420,292) #top 412
                repeat
    #End BJ animation Speed 0
    

image Laura_BJ_Body_1:                                                                        
    #Her Body in the BJ pose, licking
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481 
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat            
    contains:       
            #base body
            "Laura_Sprite"      
            pos (673,740)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.25 rotate -40 #bottom
                pause 0.45
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15
                easeout .9 xpos 740 #bottom
                easein .35 xpos 740 #bottom 481 
                pause 0.5
                easeout .65 xpos 710 #top
                easein .65 xpos 673 #top
                repeat   
            parallel:
                pause 0.15
                ease 1.25 ypos 830 #bottom
                pause 0.45
                ease 1.35 ypos 740 #top
                repeat    
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481 
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
                easeout 1.2 rotate 1 #bottom
                easein .3 rotate -1 #bottom
                pause 0.4
                ease 1.2 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 pos (407,262) #bottom(637,168)
                easein .3 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.2 pos (412,292) #top
                repeat
    #End BJ animation Speed 1
    
image Laura_BJ_Body_2:                                                                        
    #Her Body in the BJ pose, heading
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30            
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat   
    contains:       
            #base body
            "Laura_Sprite"      
            pos (680,755)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -30 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15   
                ease 1.35 xpos 730 #bottom 760
                pause 0.25
                ease 1.45 xpos 680 #top                    
                repeat   
            parallel:
                pause 0.15
                ease 1.55 ypos 780 #bottom
                pause 0.15
                ease 1.35 ypos 755 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 1.3
                ease .4 rotate 8 #bottom
                pause .2
                ease 1 rotate 10 #top
                pause .3
                repeat
            parallel:
                pause 1.3
                ease .4 pos (410,285) #bottom(407,262)
                pause .2
                ease 1 pos (412,292) #top
                pause .3
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat   
    #End BJ animation Speed 2
    


image Laura_BlowCock_Mask_3:   
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   

image Laura_BJ_Body_3:                                                                        
    #Her Body in the BJ pose, sucking
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat                  
    contains:       
            #base body
            "Laura_Sprite"      
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
#                pause 0.15
                ease .7 rotate -40 #bottom
#                pause 0.15
                ease 1.0 rotate -20 #top
                repeat 
            parallel:
#                pause 0.15   
                easeout .3 xpos 710 #bottom
                easein .4 xpos 760 #bottom
#                pause 0.15
                easeout .55 xpos 710 #top
                easein .45 xpos 673 #top                    
                repeat   
            parallel:
#                pause 0.15
                ease .7 ypos 780 #bottom 830
#                pause 0.15
                ease 1.0 ypos 780 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_3")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
#                pause 0.2
                ease .7 rotate 0 #bottom
#                pause 0.1
                ease 1 rotate 10 #top
                repeat
            parallel:
#                pause 0.2
                ease .7 pos (407,262) #bottom(637,168)
#                pause 0.1
                ease 1 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")   
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat   
    #End BJ animation Speed 3
    
    
image Laura_BlowCock_Mask_4:   
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
        block:
                pause 0.1
                ease 1.6 offset (0,300)# bottom
                pause 0.1
                ease 1.4 offset (0,0)# top
                repeat   

image Laura_BJ_Body_4:                                                                        
    #Her Body in the BJ pose, deep throat
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat                
    contains:       
            #base body
            "Laura_Sprite"      
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -40 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15   
                easeout .65 xpos 710 #bottom
                easein .9 xpos 760 #bottom
                pause 0.15
                easeout .70 xpos 710 #top
                easein .65 xpos 673 #top                    
                repeat   
            parallel:
                pause 0.15
                ease 1.55 ypos 830 #bottom
                pause 0.15
                ease 1.35 ypos 780 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_4")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
                ease 1.6 rotate 0 #bottom
                pause 0.1
                ease 1.4 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 pos (407,262) #bottom(637,168)
                pause 0.1
                ease 1.4 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat  
    #End BJ animation Speed 4
    
    
image Laura_BJ_Body_5:                                                                        
    #Her Body in the BJ pose, high cumming
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat              
    contains:       
            #base body
            "Laura_Sprite"      
            subpixel True
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -30
            pos (730,760)#(680,755) #bottom                
            parallel:
                pause 1
                ease .3 rotate -26 #top
                easeout .3 rotate -28 #bottom
                easein .5 rotate -30 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 710 #top 680
                easeout .3 xpos 720 #bottom
                easein .5 xpos 730 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 750 #top 755
                easeout .3 ypos 755 #bottom
                easein .5 ypos 760 #bottom
                pause .5
                repeat                  
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat                   
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (410,292) #bottom
            zoom 0.4  
            alpha 1
            rotate 12    
            parallel:
                pause 1
                ease .3 rotate 10 #top
                ease .3 rotate 12 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (412,285) #top
                ease .3 pos (410,292) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat   
    #End BJ animation Speed 5
    
image Laura_BlowCock_Mask_6:   
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   
                
image Laura_BJ_Body_6:                                                                        
    #Her Body in the BJ pose, deep throat cumming
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat                 
    contains:       
            #base body
            "Laura_Sprite"      
            subpixel True
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -40
            pos (760,830)#(680,755) #bottom                
            parallel:
                pause 1
                ease .3 rotate -38 #top
                easeout .3 rotate -39 #bottom
                easein .5 rotate -40 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 750 #top
                easeout .3 xpos 756 #bottom
                easein .5 xpos 760 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 835 #top
                easeout .3 ypos 830 #bottom
                easein .5 ypos 830 #bottom
                pause .5
                repeat  
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat   
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "P_Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_6")
            subpixel True
            pos (407,262) #bottom
            zoom 0.4  
            alpha 1
            rotate 0    
            parallel:
                pause 1
                ease .3 rotate 2 #top
                ease .3 rotate 0 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (409,268) #top
                ease .3 pos (407,262) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat  
    #End BJ animation Speed 6
#Head and Body Animations for Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Laura_BJ_Launch(Line = 0):    # The sequence to launch the Laura BJ animations  
    if renpy.showing("Laura_BJ_Animation"):
        return
    
    call Laura_Hide from _call_Laura_Hide
    if Line == "L" or Line == "cum":
        show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl["Laura"].GirlLayer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl["Laura"].GirlLayer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    $ Speed = 0
    if Taboo and Line == "L": # Laura gets started. . .
            if R_Loc == bg_current:
                "Laura looks back at Rogue to see if she's watching."
            elif K_Loc == bg_current:
                "Laura looks back at Kitty to see if she's watching."
            else:
                "Laura casually glaces around to see if anyone notices what she's doing"
            "She then bends down and puts your cock to her mouth."
    elif Line == "L":    
            "Laura smoothly bends down and places your cock against her cheek."    
            
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Laura_Sprite zorder newgirl["Laura"].GirlLayer:
        alpha 0
    show Laura_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Laura_BJ_Reset: # The sequence to the Laura animations from BJ to default
    if not renpy.showing("Laura_BJ_Animation"):
        return
#    hide Laura_BJ_Animation
    call Laura_Hide from _call_Laura_Hide_1 
    $ Speed = 0
    
    show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Laura_Sprite zorder newgirl["Laura"].GirlLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        zoom 1 offset (0,0)    
    return  

# End Laura Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Handjob element //////////////////////////////////////////////////////////////////////                                         Core Emma HJ element

image Laura_Hand_Under:
    "images/LauraSprite/handlaura2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    
    
image Laura_Hand_Over:
    "images/LauraSprite/handlaura1.png"    
    anchor (0.5,0.5)
    pos (-10,0)
    
transform Laura_Hand_1():
    subpixel True
    pos (-20,-100) 
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Laura_Hand_2():
    subpixel True    
    pos (-15,-120) 
    rotate 10 
    block:
        ease 0.2 pos (-15,0) rotate 0   
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10 
        pause 0.1
        repeat

transform Handcock_3():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_4():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat
     
transform Handcock_1L():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_2L():
    subpixel True
    rotate_pad False
    ypos 400 
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat
    
image Laura_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Laura_Hand_Under"), 
            "Speed == 1", At("Laura_Hand_Under", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Under", Laura_Hand_2()),            
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1L()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2L()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Laura_Hand_Over"), 
            "Speed == 1", At("Laura_Hand_Over", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Over", Laura_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Laura_HJ_Launch(Line = 0): 
    if renpy.showing("Laura_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Laura_Hide from _call_Laura_Hide_2
    if Line == "L":      
        show Laura_Sprite at SpriteLoc(StageRight) zorder newgirl["Laura"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:     
        show Laura_Sprite at SpriteLoc(StageRight) zorder newgirl["Laura"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
        with dissolve
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ newgirl["Laura"].Girl_Arms = 1
    show Laura_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)
    return
    
label Laura_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Laura_HJ_Animation"):
        return    
    $ Speed = 0            
    $ newgirl["Laura"].Girl_Arms = 1
    hide Laura_HJ_Animation with easeoutbottom
    call Laura_Hide from _call_Laura_Hide_3 
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0) 
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        zoom 1 offset (0,0)     
    return
    
# End Laura Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    

# Laura Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
       
        
        
label Laura_Kissing_Launch(T = Trigger):    
    call Laura_Hide from _call_Laura_Hide_4
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer
    show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl["Laura"].GirlLayer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label Laura_Kissing_Smooch:   
    call LauraFace("kiss") from _call_LauraFace_183  
    show Laura_Sprite at SpriteLoc(StageCenter) zorder newgirl["Laura"].GirlLayer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos newgirl["Laura"].SpriteLoc zoom 1      
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        zoom 1
    call LauraFace("sexy") from _call_LauraFace_184  
    return
            
label Laura_Breasts_Launch(T = Trigger):    
    call Laura_Hide from _call_Laura_Hide_5
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
        
label Laura_Pussy_Launch(T = Trigger):
    call Laura_Hide from _call_Laura_Hide_6    
    $ Trigger = T
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label Laura_Pos_Reset(Pose = 0):    
    call Laura_Hide from _call_Laura_Hide_7 
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1
    show Laura_Sprite zorder newgirl["Laura"].GirlLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1  
        alpha 1
        pos (newgirl["Laura"].SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Laura_Hide:
        if renpy.showing("Laura_SexSprite"):
            call Laura_Sex_Reset from _call_Laura_Sex_Reset_3
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
        pos (195,380)#(215,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block: 
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_L:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,380)#(120,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block: 
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60 
            repeat

#image GropeBreast:
image LickRightBreast_L:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (95,355)#(105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (75,330)#(85,345)  top         
            pause .5
            ease 1.5 rotate 30 pos (95,355)#(105,375) bottom
            repeat
            
image LickLeftBreast_L:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (195,360) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (190,340)#(190,380)            
            pause .5
            ease 1.5 rotate 30 pos (195,360)#(200,410)
            repeat

image GropeThigh_L: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (115,690)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (105,780) #(150,750) bottom
            ease 1 rotate 100 pos (115,690)   
            repeat

image GropePussy_L: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (120,620)#(200,600) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (120,605) #(200,585)
                ease .75 rotate 170 pos (120,620)   
            choice: 
                ease .5 rotate 190 pos (120,605)
                pause .25
                ease 1 rotate 170 pos (120,620)             
            repeat

image FingerPussy_L: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (140,700)#(210,665)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (150,665)#(220,640)
                pause .5
                ease 1 rotate 50 pos (140,700)  #(210,665)     
            choice:                          
                ease .5 rotate 40 pos (150,665)
                pause .5
                ease 1.75 rotate 50 pos (140,700)  
            choice:                          
                ease 2 rotate 40 pos (150,665)
                pause .5
                ease 1 rotate 50 pos (140,700) 
            choice:                          
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
            repeat
            
image Lickpussy_L:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (155,650)#(230,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easeout .5 rotate -50 pos (145,630) #(210,605)
            linear .5 rotate -60 pos (135,640) #(200,615)
            easein 1 rotate 10 pos (155,650) #(230,625)
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
        pos (220,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block: 
            ease 1 rotate 10 pos (220,380)#(280,390)
            ease 1 rotate -10 pos (220,370)
            repeat

image GirlGropeRightBreast_L:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,370) #(90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -40 pos (90,380)#(90,410)
            ease 1 rotate -10 pos (90,370)
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
        pos (100,500) #(120,530)
    
image GirlGropePussy_L: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (130,595) #(205,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (130,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (130,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (130,590) #(205,590)
                ease .75 rotate 200 pos (130,595) #(205,595)
                ease .5 rotate 205 pos (130,590)
                ease .75 rotate 200 pos (130,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
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
label LauraFace(Emote = newgirl["Laura"].Emote, B = newgirl["Laura"].Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state
        # M is whether the character is in a  manic state                 
        $ Emote = newgirl["Laura"].Emote if Emote == 5 else Emote
        $ B = newgirl["Laura"].Blush if B == 5 else B
        
        if (newgirl["Laura"].Forced or "angry" in newgirl["Laura"].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl["Laura"].ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl["Laura"].Mouth = "normal"
                $ newgirl["Laura"].Brows = "normal"
                $ newgirl["Laura"].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl["Laura"].Mouth = "kiss"
                $ newgirl["Laura"].Brows = "angry"
                $ newgirl["Laura"].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl["Laura"].Mouth = "lipbite"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl["Laura"].Mouth = "normal"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl["Laura"].Mouth = "kiss"
                $ newgirl["Laura"].Brows = "confused"
                $ newgirl["Laura"].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl["Laura"].Mouth = "kiss"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl["Laura"].Mouth = "tongue"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl["Laura"].Mouth = "lipbite"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "surprised"
                $ newgirl["Laura"].Blush = 1
        elif Emote == "sad":
                $ newgirl["Laura"].Mouth = "sad"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl["Laura"].Mouth = "sad"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl["Laura"].Mouth = "lipbite"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "squint"
        elif Emote == "smile":
                if newgirl["Laura"].Love >= 700:
                    $ newgirl["Laura"].Mouth = "smile"
                else:
                    $ newgirl["Laura"].Mouth = "smirk"                
                $ newgirl["Laura"].Brows = "normal"
                $ newgirl["Laura"].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl["Laura"].Mouth = "sucking"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl["Laura"].Mouth = "kiss"
                $ newgirl["Laura"].Brows = "surprised"
                $ newgirl["Laura"].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl["Laura"].Mouth = "smile"
                $ newgirl["Laura"].Brows = "surprised"
                $ newgirl["Laura"].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl["Laura"].Mouth = "sad"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl["Laura"].Mouth = "smile"
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Eyes = "surprised"
        elif Emote == "sly":
                if newgirl["Laura"].Love >= 700:
                    $ newgirl["Laura"].Mouth = "smile"
                else:
                    $ newgirl["Laura"].Mouth = "smirk" 
                $ newgirl["Laura"].Brows = "confused"
                $ newgirl["Laura"].Eyes = "squint"
            
        if M:
                $ newgirl["Laura"].Eyes = "surprised"        
        if B > 1:
                $ newgirl["Laura"].Blush = 2
        elif B:
                $ newgirl["Laura"].Blush = 1
        else:
                $ newgirl["Laura"].Blush = 0
        
        if Mouth:
                $ newgirl["Laura"].Mouth = Mouth
        if Eyes:
                $ newgirl["Laura"].Eyes = Eyes
        if Brows:
                $ newgirl["Laura"].Brows = Brows
        
        return
        
        
# Laura's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label LauraWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call Laura_Pos_Reset from _call_Laura_Pos_Reset
                    "Face":
                        call Laura_Kissing_Launch(0) from _call_Laura_Kissing_Launch
                    "Body":
                        call Laura_Pussy_Launch(0) from _call_Laura_Pussy_Launch
                    "Back":
                        jump LauraWardrobe 
        # Outfits
#        "Teacher outfit":
#            $ newgirl["Laura"].Outfit = "teacher"
#            call LauraOutfit
#        "Super outfit":
#            $ newgirl["Laura"].Outfit = "costume"
#            call LauraOutfit
        "Nude":
            $ newgirl["Laura"].Over = 0
            $ newgirl["Laura"].Chest = 0
            $ newgirl["Laura"].Legs = 0
            $ newgirl["Laura"].Panties = 0
            $ newgirl["Laura"].Gloves = 0
            $ newgirl["Laura"].Neck = 0
#            $ newgirl["Laura"].Outfit = "nude"
#            call LauraOutfit
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [newgirl[Laura].Over]" if newgirl["Laura"].Over:
                        $ newgirl["Laura"].Over = 0
                    "Add Jacket":
                        $ newgirl["Laura"].Over = "jacket"  
                    "Add Towel":
                        $ newgirl["Laura"].Over = "towel" 
                    "Add nighty":
                        $ newgirl["Laura"].Over = "nighty"   
                    "Back":
                        jump LauraWardrobe                
        "Chests":            
            while True:
                menu:
                    # Tops    
                    "Remove [newgirl[Laura].Chest]" if newgirl["Laura"].Chest:
                        $ newgirl["Laura"].Chest = 0
                    "Add leather bra":
                        $ newgirl["Laura"].Chest = "leather bra"
                    "Add wolvie top":
                        $ newgirl["Laura"].Chest = "wolvie top"
                    "Add corset":
                        $ newgirl["Laura"].Chest = "corset"
#                    "Add buttoned tank top" if newgirl["Laura"].Over != "mesh top":
#                        $ newgirl["Laura"].Chest = "buttoned tank"
                    "Add lace bra":
                        $ newgirl["Laura"].Chest = "lace bra"
#                    "Add bra":
#                        $ newgirl["Laura"].Chest = "bra"                            
#                    "Toggle Piercings":
#                        if newgirl["Laura"].Pierce == "ring":
#                            $ newgirl["Laura"].Pierce = "barbell"
#                        elif newgirl["Laura"].Pierce == "barbell":
#                            $ newgirl["Laura"].Pierce = 0
#                        else:
#                            $ newgirl["Laura"].Pierce = "ring"
                    "Back":
                        jump LauraWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if newgirl["Laura"].Legs:     
                        $ newgirl["Laura"].Legs = 0
                    "Add leather pants":
                        $ newgirl["Laura"].Legs = "leather pants"
                        $ newgirl["Laura"].Upskirt = 0
                    "Add mesh pants":
                        $ newgirl["Laura"].Legs = "mesh pants"
                        $ newgirl["Laura"].Upskirt = 0
                    "Add skirt":
                        $ newgirl["Laura"].Legs = "skirt"
                    "Toggle upskirt":
                        if newgirl["Laura"].Upskirt:
                            $ newgirl["Laura"].Upskirt = 0
                        else:
                            $ newgirl["Laura"].Upskirt = 1
                    "Back":
                        jump LauraWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
                    "Hose":
                        menu:
                            "Add hose":     
                                $ newgirl["Laura"].Hose = "stockings"  
                            "Add garter":     
                                $ newgirl["Laura"].Hose = "garterbelt"  
                            "Add stockings and garter":     
                                $ newgirl["Laura"].Hose = "stockings and garterbelt"  
#                            "Add pantyhose":     
#                                $ newgirl["Laura"].Hose = "pantyhose"   
#                            "Add tights":     
#                                $ newgirl["Laura"].Hose = "tights"   
#                            "Add ripped hose":     
#                                $ newgirl["Laura"].Hose = "ripped pantyhose"   
#                            "Add ripped tights":     
#                                $ newgirl["Laura"].Hose = "ripped tights"   
#                            "Add tights":     
#                                $ newgirl["Laura"].Hose = "tights"    
                            "Remove hose" if newgirl["Laura"].Hose:     
                                $ newgirl["Laura"].Hose = 0  

#                    "toggle boots":    
#                        if not newgirl["Laura"].Boots:
#                            $ newgirl["Laura"].Boots = "thigh boots"   
#                        else:
#                            $ newgirl["Laura"].Boots = 0     
                        
                    "Remove panties" if newgirl["Laura"].Panties:     
                        $ newgirl["Laura"].Panties = 0     
                    "Add black panties":
                        $ newgirl["Laura"].Panties = "black panties"
#                    "Add shorts":
#                        $ newgirl["Laura"].Panties = "shorts"
                    "Add wolvie panties":
                        $ newgirl["Laura"].Panties = "wolvie panties"  
                    "Add lace panties":
                        $ newgirl["Laura"].Panties = "lace panties"    
                    "pull down-up panties":
                        if newgirl["Laura"].PantiesDown:
                            $ newgirl["Laura"].PantiesDown = 0
                        else:
                            $ newgirl["Laura"].PantiesDown = 1
                    "Back":
                        jump LauraWardrobe    
        "Face":
            while True:
                menu: 
                    "Brows=[newgirl[Laura].Brows], Eyes=[newgirl[Laura].Eyes], Mouth=[newgirl[Laura].Mouth]"
                    "Emotions":
                            call LauraEmotionEditor from _call_LauraEmotionEditor
                    "Toggle Brows":
                            if newgirl["Laura"].Brows == "normal":
                                $ newgirl["Laura"].Brows = "angry"
                            elif newgirl["Laura"].Brows == "angry":
                                $ newgirl["Laura"].Brows = "confused"
                            elif newgirl["Laura"].Brows == "confused":
                                $ newgirl["Laura"].Brows = "sad"
                            elif newgirl["Laura"].Brows == "sad":
                                $ newgirl["Laura"].Brows = "surprised"
                            else:
                                $ newgirl["Laura"].Brows = "normal"
                    "Toggle Eyes Emotions":
                            if newgirl["Laura"].Eyes == "normal":                          
                                $ newgirl["Laura"].Eyes = "surprised"
                            elif newgirl["Laura"].Eyes == "surprised":
                                $ newgirl["Laura"].Eyes = "sexy"
                            elif newgirl["Laura"].Eyes == "sexy":
                                $ newgirl["Laura"].Eyes = "squint"
                            elif newgirl["Laura"].Eyes == "squint":
                                $ newgirl["Laura"].Eyes = "closed"
                            else:
                                $ newgirl["Laura"].Eyes = "normal"
                    "Toggle Eyes Directions":
                            if newgirl["Laura"].Eyes == "normal":
                                $ newgirl["Laura"].Eyes = "side"
                            elif newgirl["Laura"].Eyes == "side":
                                $ newgirl["Laura"].Eyes = "down"
                            elif newgirl["Laura"].Eyes == "down":
                                $ newgirl["Laura"].Eyes = "leftside"
                            elif newgirl["Laura"].Eyes == "leftside":
                                $ newgirl["Laura"].Eyes = "stunned"
                            else:
                                $ newgirl["Laura"].Eyes = "normal"  
                    "Toggle Mouth Normal":
                            if newgirl["Laura"].Mouth  == "normal":
                                $ newgirl["Laura"].Mouth = "sad"
                            elif newgirl["Laura"].Mouth == "sad":
                                $ newgirl["Laura"].Mouth = "smile"
                            elif newgirl["Laura"].Mouth == "smile":
                                $ newgirl["Laura"].Mouth = "surprised"
                            else:
                                $ newgirl["Laura"].Mouth = "normal"  
                    "Toggle Mouth Sexy":
                            if newgirl["Laura"].Mouth  == "normal":
                                $ newgirl["Laura"].Mouth = "kiss"
                            elif newgirl["Laura"].Mouth == "kiss":
                                $ newgirl["Laura"].Mouth = "sucking"
                            elif newgirl["Laura"].Mouth == "sucking":
                                $ newgirl["Laura"].Mouth = "tongue"
                            elif newgirl["Laura"].Mouth == "tongue":
                                $ newgirl["Laura"].Mouth = "lipbite"
                            else:
                                $ newgirl["Laura"].Mouth = "normal"  
                    "Toggle Blush":
                        if newgirl["Laura"].Blush == 1:
                            $ newgirl["Laura"].Blush = 2
                        elif newgirl["Laura"].Blush:
                            $ newgirl["Laura"].Blush = 0
                        else:
                            $ newgirl["Laura"].Blush = 1
                            
                    "Back":
                            jump LauraWardrobe    
        "Misc":
            while True:
                menu: 
                    "Toggle Arm pose":
                        if newgirl["Laura"].Girl_Arms == 1:
                            $ newgirl["Laura"].Girl_Arms = 2
                        else:
                            $ newgirl["Laura"].Girl_Arms = 1
                    "Toggle Claws":
                        if newgirl["Laura"].Claws:
                            $ newgirl["Laura"].Claws = 0
                        else:
                            $ newgirl["Laura"].Claws = 1
                    "Toggle Wetness" if True:
                        if not newgirl["Laura"].Wet:
                            $ newgirl["Laura"].Wet = 1
                        elif newgirl["Laura"].Wet == 1:
                            $ newgirl["Laura"].Wet = 2
                        else:
                            $ newgirl["Laura"].Wet  = 0
                    "Toggle wet look" if True:
                        if not newgirl["Laura"].Water:
                            $ newgirl["Laura"].Water = 1
                        elif newgirl["Laura"].Water == 1:
                            $ newgirl["Laura"].Water = 3
                        else:
                            $ newgirl["Laura"].Water  = 0
                    "Toggle pubes":
                        if not newgirl["Laura"].Pubes:
                            $ newgirl["Laura"].Pubes = 1
                        else:
                            $ newgirl["Laura"].Pubes = 0
                    "Toggle Pussy Spunk" if True:
                        if "pussy" in newgirl["Laura"].Spunk:
                            $ newgirl["Laura"].Spunk.remove("pussy")
                        else:
                            $ newgirl["Laura"].Spunk.append("pussy")
                    "Toggle Piercings":
                        if newgirl["Laura"].Pierce == "ring":
                            $ newgirl["Laura"].Pierce = "barbell"
                        elif newgirl["Laura"].Pierce == "barbell":
                            $ newgirl["Laura"].Pierce = 0
                        else:
                            $ newgirl["Laura"].Pierce = "ring"
                    "Add leash choker" if not newgirl["Laura"].Neck:
                        $ newgirl["Laura"].Neck = "leash choker"
                    "Remove choker" if newgirl["Laura"].Neck:
                        $ newgirl["Laura"].Neck = 0
                        
                    "Add wristbands" if not newgirl["Laura"].Arms:
                        $ newgirl["Laura"].Arms = "wrists"
                    "Remove Gloves" if newgirl["Laura"].Arms:
                        $ newgirl["Laura"].Arms = 0
                    "Back":
                        jump LauraWardrobe               
#        "Set Custom Outfit #1.":
#            $ newgirl["Laura"].Custom[0] = 1
#            $ newgirl["Laura"].Custom[1] = newgirl["Laura"].Arms
#            $ newgirl["Laura"].Custom[2] = newgirl["Laura"].Legs
#            $ newgirl["Laura"].Custom[3] = newgirl["Laura"].Over
#            $ newgirl["Laura"].Custom[4] = newgirl["Laura"].Under #fix, this can be changed to something else, no longer necessary
#            $ newgirl["Laura"].Custom[5] = newgirl["Laura"].Chest
#            $ newgirl["Laura"].Custom[6] = newgirl["Laura"].Panties 
#            $ newgirl["Laura"].Custom[7] = newgirl["Laura"].Pubes 
#            $ newgirl["Laura"].Custom[8] = newgirl["Laura"].Hair
#            $ newgirl["Laura"].Custom[9] = newgirl["Laura"].Hose
#        "Wear Custom Outfit #[newgirl[Laura].Custom[0]]." if newgirl["Laura"].Custom[0]:
#            $ Line = newgirl["Laura"].Outfit
#            $ newgirl["Laura"].Outfit = "custom1"
#            call RogueOutfit
#            $ newgirl["Laura"].Outfit = Line
        "Nothing":
            return
    jump LauraWardrobe
return

label LauraEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ newgirl["Laura"].Emote = "normal"
                    call LauraFace from _call_LauraFace_185
                "Angry":
                    $ newgirl["Laura"].Emote = "angry"
                    call LauraFace from _call_LauraFace_186
                "Smiling":
                    $ newgirl["Laura"].Emote = "smile"
                    call LauraFace from _call_LauraFace_187
                "Sexy":
                    $ newgirl["Laura"].Emote = "sexy"
                    call LauraFace from _call_LauraFace_188
                "Suprised":
                    $ newgirl["Laura"].Emote = "surprised"
                    call LauraFace from _call_LauraFace_189
                "Bemused":
                    $ newgirl["Laura"].Emote = "bemused"
                    call LauraFace from _call_LauraFace_190
                "Manic":
                    $ newgirl["Laura"].Emote = "manic"
                    call LauraFace from _call_LauraFace_191
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ newgirl["Laura"].Emote = "sad"
                    call LauraFace from _call_LauraFace_192
                "Sucking":
                    $ newgirl["Laura"].Emote = "sucking"
                    call LauraFace from _call_LauraFace_193
                "kiss":
                    $ newgirl["Laura"].Emote = "kiss"
                    call LauraFace from _call_LauraFace_194
                "Tongue":
                    $ newgirl["Laura"].Emote = "tongue"
                    call LauraFace from _call_LauraFace_195
                "confused":
                    $ newgirl["Laura"].Emote = "confused"
                    call LauraFace from _call_LauraFace_196
                "Closed":
                    $ newgirl["Laura"].Emote = "closed"
                    call LauraFace from _call_LauraFace_197
                "Down":
                    $ newgirl["Laura"].Emote = "down"
                    call LauraFace from _call_LauraFace_198
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ newgirl["Laura"].Emote = "sadside"
                    call LauraFace from _call_LauraFace_199
                "Startled":
                    $ newgirl["Laura"].Emote = "startled"
                    call LauraFace from _call_LauraFace_200
                "Perplexed":
                    $ newgirl["Laura"].Emote = "perplexed"
                    call LauraFace from _call_LauraFace_201
                "Sly":
                    $ newgirl["Laura"].Emote = "sly"
                    call LauraFace from _call_LauraFace_202
        "Toggle Mouth Spunk":
            if "mouth" in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.remove("mouth")
            else:
                $ newgirl["Laura"].Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.remove("hand")
            else:
                $ newgirl["Laura"].Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in newgirl["Laura"].Spunk and "hair" not in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.append("hair")
            elif "facial" in newgirl["Laura"].Spunk:
                $ newgirl["Laura"].Spunk.remove("facial")                
                $ newgirl["Laura"].Spunk.remove("hair")
            else:
                $ newgirl["Laura"].Spunk.append("facial")
            
        "Blush":
            if newgirl["Laura"].Blush == 2:
                $ newgirl["Laura"].Blush = 0
            elif newgirl["Laura"].Blush:
                $ newgirl["Laura"].Blush = 2
            else:
                $ newgirl["Laura"].Blush = 1  
        "Exit.":
            return
    jump LauraEmotionEditor
return