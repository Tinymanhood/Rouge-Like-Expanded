
#=======================================FUTURE?=====================================================================
# image Laura_Sprite_BG:
#     LiveComposite(        
#         (402,965),
#         (0,0), ConditionSwitch(
#             #hair back 
#             "not newgirl['Laura'].Hair", Null(),
#             "renpy.showing('Laura_BJ_Animation')", Null(), 
#             "newgirl['Laura'].Hair", "Laura_Sprite_HairBack",   
#             "True", Null(),        
#             ),   
#         (0,0), ConditionSwitch(            
#             #panties down back 
#             "not newgirl['Laura'].Panties or not newgirl['Laura'].PantiesDown or (newgirl['Laura'].Legs == 'pants' and not newgirl['Laura'].Upskirt)", Null(), 
#             "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",   
#             "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",   
#             ), 
#         (0,0), ConditionSwitch(
#             #backside of arms
#             "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",   
#             "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png", #if newgirl['Laura'].Arms == 1 
#             ),     
#         #body
#         (0,0), "images/LauraSprite/Laura_Sprite_Body.png",
#         (0,0), ConditionSwitch(
#             #pubes 
#             "newgirl['Laura'].Pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",   
#             "True", Null(),        
#             ),      
#         (0,0), ConditionSwitch(
#             #stockings    
#             "newgirl['Laura'].Hose == 'stockings' or newgirl['Laura'].Hose == 'stockings and garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
#             "True", Null(),
#             ),     
#         (0,0), ConditionSwitch(
#             #garterbelt    
#             "newgirl['Laura'].Hose == 'stockings and garterbelt' or newgirl['Laura'].Hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
#             "True", Null(),
#             ),              
#         (0,0), ConditionSwitch(
#             #panties    
#             "not newgirl['Laura'].Panties", Null(),
#             "newgirl['Laura'].PantiesDown", ConditionSwitch(                   
#                     #if the panties are down
#                     "not newgirl['Laura'].Legs or newgirl['Laura'].Upskirt or newgirl['Laura'].Legs == 'skirt'", ConditionSwitch(                   
#                             #if she's wearing a skirt or nothing else                    
#                             "newgirl['Laura'].Panties == 'wolvie panties' and newgirl['Laura'].Wet", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png", 
#                             "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",                             
#                             "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", 
#                             "newgirl['Laura'].Panties == 'black panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", #fix
#                             "True", Null(),
#                             ),         
#                     "True", Null(),
#                     ),                    
#             "True", ConditionSwitch(                
#                     #if she's got panties and they are not down
#                     "newgirl['Laura'].Wet", ConditionSwitch(   
#                         #if she's  wet                            
#                         "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
#                         "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
#                         "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
#                         ),
#                     "True", ConditionSwitch(   
#                         #if she's not wet                            
#                         "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
#                         "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
#                         "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
#                         ),                    
#                     ),    
#             ),            
#         (0,0), ConditionSwitch(
#             #pants    
#             "not newgirl['Laura'].Legs", Null(),
#             "newgirl['Laura'].Upskirt", ConditionSwitch(                
#                         #if the skirt's up or pants down 
#                         "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png", 
#                         "True", Null(),                       
#                         ),                    
#             "True", ConditionSwitch(                
#                     #if it's the ring pericings
#                     "newgirl['Laura'].Wet", ConditionSwitch(   
#                         #if she's not wet
#                         "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
#                         "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
#                         "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
#                         "True", Null(),
#                         ),                    
#                     "True", ConditionSwitch(   
#                         #if she's wet
#                         "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
#                         "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
#                         "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
#                         "True", Null(),
#                         ),                    
#                     ),                  
#             ),    
        
#         (0,0), ConditionSwitch(
#             #arms midlayer
#             "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
#             "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png", #if newgirl['Laura'].Arms == 1   # Crossed        
#             ),  
#         (0,0), ConditionSwitch(
#             #arms wristband
#             "newgirl['Laura'].Arms == 'wrists' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png", # one hand up
#             "newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png", # one hand up
#             "True", Null(),     
#             ), 
        
#         (0,0), ConditionSwitch(
#             #L Over under
#             "newgirl['Laura'].Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png", # one hand up
#             "True", Null(),     
#             ), 
#         # tits
#         (0,0), "images/LauraSprite/Laura_Sprite_Tits.png", 

        
#         (0,0), ConditionSwitch(                          
#             #neck
#             "newgirl['Laura'].Neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
#             "True", Null(), 
#             ),  
#         (0,0), ConditionSwitch(                                                                        
#             #Chest layer
#             "newgirl['Laura'].Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
#             "newgirl['Laura'].Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",   
#             "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Bra_Sports.png",   
#             "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",   
#             "True", Null(),              
#             ),            

#         (0,0), ConditionSwitch(
#             #L Over
#             "newgirl['Laura'].Over == 'jacket' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png", # one hand up
#             "newgirl['Laura'].Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png", # one hand up
#             "newgirl['Laura'].Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
#             "True", Null(),     
#             ), 
        
#         #Head
#         (0,0), ConditionSwitch(
#             # head
#             "renpy.showing('Laura_BJ_Animation')", Null(),  
#             "True", "Laura_Sprite_Head_BG",   
#             ),         
#         (0,0), ConditionSwitch(
#             #arms toplayer
#             "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
#             "True", Null(),     
#             ), 
#         (0,0), ConditionSwitch(
#             #arms wristband
#             "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
#             "True", Null(),     
#             ), 
#         (0,0), ConditionSwitch(
#             #jacket arm toplayer
#             "newgirl['Laura'].Over == 'jacket' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png", # one hand up
#             "True", Null(),     
#             ), 
#         (0,0), ConditionSwitch(
#             #claws
#             "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Claws", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
#             "True", Null(),     
#             ), 
#         )           
#     anchor (0.6, 0.0)                
#     yoffset 15
#     zoom .75                

    
# image Laura_Sprite_Head_BG:            
#     LiveComposite(
#         (806,806),         
#         (0,0), ConditionSwitch(
#                 # Face background plate
#                 "newgirl['Laura'].Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
#                 "newgirl['Laura'].Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
#                 "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
#                 ),        
#         (0,0), ConditionSwitch(#Mouths 
#             "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
#             "newgirl['Laura'].Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
#             "newgirl['Laura'].Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
#             "newgirl['Laura'].Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
#             "newgirl['Laura'].Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
#             "newgirl['Laura'].Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
#             "newgirl['Laura'].Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
#             "newgirl['Laura'].Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
#             "newgirl['Laura'].Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
#             "newgirl['Laura'].Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
#             "newgirl['Laura'].Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
#             "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
#             ),         
#         (0,0), ConditionSwitch(#Mouth spunk 
#             "'mouth' not in newgirl['Laura'].Spunk", Null(),
#             "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png", #and Speed >= 2
#             "newgirl['Laura'].Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
#             "newgirl['Laura'].Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
#             "newgirl['Laura'].Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",            
#             "newgirl['Laura'].Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
#             "newgirl['Laura'].Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
#             "newgirl['Laura'].Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
#             "newgirl['Laura'].Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",            
#             "newgirl['Laura'].Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",                
#             "newgirl['Laura'].Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",              
#             "newgirl['Laura'].Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",      
#             "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
#             ),                                                        
#         (0,0), ConditionSwitch(                                                                       
#             #brows
#             "newgirl['Laura'].Blush >= 2", ConditionSwitch(
#                     "newgirl['Laura'].Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
#                     "newgirl['Laura'].Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
#                     "newgirl['Laura'].Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
#                     "newgirl['Laura'].Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
#                     "newgirl['Laura'].Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
#                     "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
#                     ),
#             "True", ConditionSwitch(
#                     "newgirl['Laura'].Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
#                     "newgirl['Laura'].Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
#                     "newgirl['Laura'].Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
#                     "newgirl['Laura'].Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
#                     "newgirl['Laura'].Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
#                     "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
#                     ),
#             ),        
#         (0,0), "Laura Blink_BG",     #Eyes    
#         (0,0), ConditionSwitch(                
#             #Hair mid
#             "newgirl['Laura'].Over == 'jacket'", Null(),
#             "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
#             "True", Null(),
#             ),       
#         (0,0), ConditionSwitch(                                                                         
#             #Hair over
#             "not newgirl['Laura'].Hair", Null(),
#             "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
#             "True", Null(),
#             ),        
#         (0,0), ConditionSwitch(
#             #Hair Water
#             "not newgirl['Laura'].Water", Null(),
#             "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#             ),
#         (0,0), ConditionSwitch(
#             #facial spunk               
#             "'hair' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",  
#             "'facial' in newgirl['Laura'].Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",            
#             "True", Null(),
#             ),  
#         )                
#     anchor (0.6, 0.0)                
#     zoom .5               

# image Laura Blink_BG:            
#     ConditionSwitch(
#     "newgirl['Laura'].Eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
#     "newgirl['Laura'].Eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
#     "newgirl['Laura'].Eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
#     "newgirl['Laura'].Eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",    
#     "newgirl['Laura'].Eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
#     "newgirl['Laura'].Eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
#     "newgirl['Laura'].Eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
#     "newgirl['Laura'].Eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
#     "newgirl['Laura'].Eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
#     "newgirl['Laura'].Eyes == 'squint'", "Laura_Squint_BG",
#     "True", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png", 
#     ),
#     choice:
#         3.5
#     choice:
#         3.25
#     choice:
#         3    
#     "images/LauraSprite/Laura_Sprite_Eyes_Closed.png"
#     .25
#     repeat                

# image Laura_Squint_BG:       
#     "images/LauraSprite/Laura_Sprite_Eyes_Normal.png"
#     choice:
#         3.5
#     choice:
#         3.25
#     choice:
#         3    
#     "images/LauraSprite/Laura_Sprite_Eyes_Squint.png"
#     .25
#     repeat   

#=======================================FUTURE?=====================================================================
image Laura_Sprite_BG:
    LiveComposite(        
        (402,965),
        (0,0), ConditionSwitch(
            #hair back 
            "not newgirl['Laura'].Hair", Null(),
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
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",   
            # "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png", #if newgirl['Laura'].Arms == 1 
            ),     
        #body
        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",
        (0,0), ConditionSwitch(
            #pubes 
            # "newgirl['Laura'].Pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",   
            # "True", Null(),        
            "True", "images/LauraSprite/Laura_Sprite_Pubes.png",        
            ),      
        # (0,0), ConditionSwitch(
        #     #stockings    
        #     "newgirl['Laura'].Hose == 'stockings' or newgirl['Laura'].Hose == 'stockings and garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
        #     "True", Null(),
        #     ),     
        # (0,0), ConditionSwitch(
        #     #garterbelt    
        #     "newgirl['Laura'].Hose == 'stockings and garterbelt' or newgirl['Laura'].Hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
        #     "True", Null(),
        #     ),              
        (0,0), ConditionSwitch(
            #panties    
            # "not newgirl['Laura'].Panties", Null(),
            # "newgirl['Laura'].PantiesDown", ConditionSwitch(                   
            #         #if the panties are down
            #         "not newgirl['Laura'].Legs or newgirl['Laura'].Upskirt or newgirl['Laura'].Legs == 'skirt'", ConditionSwitch(                   
            #                 #if she's wearing a skirt or nothing else                    
            #                 "newgirl['Laura'].Panties == 'wolvie panties' and newgirl['Laura'].Wet", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png", 
            #                 "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",                             
            #                 "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", 
            #                 "newgirl['Laura'].Panties == 'black panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", #fix
            #                 "True", Null(),
            #                 ),         
            #         "True", Null(),
            #         ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
                    # "newgirl['Laura'].Wet", ConditionSwitch(   
                    #     #if she's  wet                            
                    #     "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                    #     "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                    #     "True", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                    #     ),
                    "True", ConditionSwitch(   
                        #if she's not wet                            
                        # "newgirl['Laura'].Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        # "newgirl['Laura'].Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        ),                    
                    ),    
            ),            
        (0,0), ConditionSwitch(
            #pants    
            # "not newgirl['Laura'].Legs", Null(),
            # "newgirl['Laura'].Upskirt", ConditionSwitch(                
            #             #if the skirt's up or pants down 
            #             "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png", 
            #             "True", Null(),                       
            #             ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    # "newgirl['Laura'].Wet", ConditionSwitch(   
                    #     #if she's not wet
                    #     "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
                    #     "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
                    #     "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                    #     "True", Null(),
                    #     ),                    
                    "True", ConditionSwitch(   
                        #if she's wet
                        # "newgirl['Laura'].Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
                        # "newgirl['Laura'].Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
                        # "newgirl['Laura'].Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",
                        ),                    
                    ),                  
            ),    
        
        (0,0), ConditionSwitch(
            #arms midlayer
            # "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
            # "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png", #if newgirl['Laura'].Arms == 1   # Crossed        
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
            ),  
        (0,0), ConditionSwitch(
            #arms wristband
            # "newgirl['Laura'].Arms == 'wrists' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png", # one hand up
            # "newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png", # one hand up
            # "True", Null(),     
            "True", "images/LauraSprite/Laura_Sprite_Wrist2.png",     
            ), 
        
        # (0,0), ConditionSwitch(
        #     #L Over under
        #     "newgirl['Laura'].Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png", # one hand up
        #     "True", Null(),     
        #     ), 
        # tits
        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png", 

        
        (0,0), ConditionSwitch(                          
            #neck
            # "newgirl['Laura'].Neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
            "True", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
            # "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                        
            #Chest layer
            # "newgirl['Laura'].Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
            # "newgirl['Laura'].Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",   
            # "newgirl['Laura'].Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Bra_Sports.png",   
            # "newgirl['Laura'].Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",   
            # "True", Null(),              
            "True", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
            ),            

        # (0,0), ConditionSwitch(
        #     #L Over
        #     "newgirl['Laura'].Over == 'jacket' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png", # one hand up
        #     "newgirl['Laura'].Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png", # one hand up
        #     "newgirl['Laura'].Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
        #     "True", Null(),     
        #     ), 
        
        #Head
        (0,0), ConditionSwitch(
            # head
            "renpy.showing('Laura_BJ_Animation')", Null(),  
            "True", "Laura_Sprite_Head_BG",   
            ),         
        (0,0), ConditionSwitch(
            #arms toplayer
            # "newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
            # "True", Null(),     
            "True", "images/LauraSprite/Laura_Sprite_Arm_Left2.png",     
            ), 
        (0,0), ConditionSwitch(
            #arms wristband
            # "newgirl['Laura'].Girl_Arms == 2 and newgirl['Laura'].Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
            # "True", Null(),     
            "True", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png",     
            ), 
        # (0,0), ConditionSwitch(
        #     #jacket arm toplayer
        #     "newgirl['Laura'].Over == 'jacket' and newgirl['Laura'].Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png", # one hand up
        #     "True", Null(),     
        #     ), 
        (0,0), ConditionSwitch(
            #claws
            "True", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
            # "True", Null(),     
            ), 
        )           
    anchor (0.6, 0.0)                
    yoffset 15
    zoom .75                

    
image Laura_Sprite_Head_BG:            
    LiveComposite(
        (806,806),         
        (0,0), ConditionSwitch(
                # Face background plate
                "newgirl['Laura'].Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "newgirl['Laura'].Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
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
        (0,0), "Laura Blink_BG",     #Eyes    
        (0,0), ConditionSwitch(                
            #Hair mid
            "newgirl['Laura'].Over == 'jacket'", Null(),
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not newgirl['Laura'].Hair", Null(),
            "newgirl['Laura'].Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not newgirl['Laura'].Water", Null(),
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

image Laura Blink_BG:            
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
    "newgirl['Laura'].Eyes == 'squint'", "Laura_Squint_BG",
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

image Laura_Squint_BG:       
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

label Laura_BG_Launch(T = Trigger):
    call Laura_Hide    
    $ Trigger = T
    show Laura_Sprite_BG at SpriteLoc(newgirl["Laura"].SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        ease 0.5 pos (800,-100) offset (0,0) zoom 1.5 alpha 1
    return                      
# End Laura Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Rogue Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_BG:
    LiveComposite(
        (480,960),
        (0,0), ConditionSwitch(                                                                         #Overhsirt backing
            "R_BG_Over == 'mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh1.png",
            "R_BG_Over == 'white mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_whitemesh1.png",
            "R_BG_Over == 'red mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_redmesh1.png",
            "R_BG_Over == 'yellow mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_yellowmesh1.png",
            "R_BG_Over == 'black mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_blackmesh1.png",
            "R_BG_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
            "R_BG_Over == 'jacket'", "images/RogueSprite/Rogue_JacketB.png",
            "R_BG_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
            "R_BG_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodieB.png",
            "R_BG_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodieB.png",
            "R_BG_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodieB.png",
            "R_BG_Over == 'black hoodie'", "images/RogueSprite/Rogue_over_dhoodieB.png",
            "R_BG_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodieB.png",
            "R_BG_Over == 'SR7 mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh_SR7_1.png",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(                                                                         #body 
            "R_BG_Tan == 'tan1'", "images/RogueSprite/Rogue_t1body_bare.png",
            "R_BG_Tan == 'tan'", "images/RogueSprite/Rogue_tbody_bare.png",
            "True", "images/RogueSprite/Rogue_body_bare.png",         
            ),  
        (0,0), ConditionSwitch(                                                                         #body 
            "R_BG_Pubes and (R_BG_HairColor == 'black' or R_BG_HairColor == 'blackwhite')", "images/RogueSprite/Rogue_bodyhaired_pubesblack.png",
            "R_BG_Pubes and (R_BG_HairColor == 'blonde' or R_BG_HairColor == 'blondewhite')", "images/RogueSprite/Rogue_bodyhaired_pubesblonde.png",
            "R_BG_Pubes", "images/RogueSprite/Rogue_bodyhaired_pubes.png",   
            "True", Null(),         
            ),  
        (0,0), ConditionSwitch(                                                                         #body 
            "R_BG_Pierce == 'ring'", "images/RogueSprite/Rogue_body_piercing_ring.png",            
            "R_BG_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_piercing_barbell.png",
            "True", Null(),         
            ),   
        #(0,0), ConditionSwitch(                                                                         #body 
        #    "R_BG_Pubes and R_BG_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
        #    "R_BG_Pubes and R_BG_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
        #    "R_BG_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
        #    "R_BG_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
        #    "R_BG_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
        #    "True", "images/RogueSprite/Rogue_body_bare.png",         
        #    ),              
        (0,0), ConditionSwitch(                                                                         #head 
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_BG_Tan and R_BG_Hair == 'evo' and R_BG_Water", "images/RogueSprite/Rogue_thead_evowet.png",
            "R_BG_Hair == 'evo' and R_BG_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_BG_Tan and R_BG_Hair == 'evo' and R_BG_Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2.png",
            # "R_BG_Hair == 'evo' and R_BG_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_BG_Tan and R_BG_Hair == 'evo' and R_BG_Blush", "images/RogueSprite/Rogue_thead_evo_blush.png",
            # "R_BG_Hair == 'evo' and R_BG_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_BG_Tan and R_BG_Hair == 'evo'", "images/RogueSprite/Rogue_thead_evo.png",
            "R_BG_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",

            "R_BG_Tan and R_BG_Hair == 'newhair' and R_BG_Water", "images/RogueSprite/Rogue_thead_evowet_newhair.png",
            "R_BG_Hair == 'newhair' and R_BG_Water", "images/RogueSprite/Rogue_head_evowet_newhair.png",
            # "R_BG_Tan and R_BG_Hair == 'newhair' and R_BG_Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2_newhair.png",
            # "R_BG_Hair == 'newhair' and R_BG_Blush == 2", "images/RogueSprite/Rogue_hair_evo_blush2_newhair.png",
            # "R_BG_Tan and R_BG_Hair == 'newhair' and R_BG_Blush", "images/RogueSprite/Rogue_thead_evo_blush_newhair.png",
            # "R_BG_Hair == 'newhair' and R_BG_Blush", "images/RogueSprite/Rogue_hair_evo_blush_newhair.png",
            "R_BG_Tan and R_BG_Hair == 'newhair'", "images/RogueSprite/Rogue_thead_evo_newhair.png",
            "R_BG_Hair == 'newhair'", "images/RogueSprite/Rogue_head_evo_newhair.png",

            "R_BG_Tan", "images/RogueSprite/Rogue_thead_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #pants backing/hose    
            "R_BG_Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
            "R_BG_Legs == 'pants' and R_BG_Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #Panties            
            "not R_BG_Panties", Null(),
            # "R_BG_Panties == 'swimsuit1' or R_BG_Panties == 'swimsuit2'", Null(),
            # "R_BG_Legs == 'pants' and not R_BG_Upskirt", "images/RogueSprite/Rogue_panties.png",             
            "R_BG_Panties == 'swimsuit1' or R_BG_Panties == 'swimsuit2'", Null(),
            # "PantsNum('Rogue') == 10 and not R_BG_Upskirt", "images/RogueSprite/Rogue_panties.png",             
            "R_BG_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
            "R_BG_Panties == 'red shorts'", "images/RogueSprite/Rogue_ryshorts.png",
            "R_BG_Panties == 'blue shorts'", "images/RogueSprite/Rogue_byshorts.png",
            "R_BG_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
            "R_BG_Panties == 'black large panties'", "images/RogueSprite/Rogue_undiesBlack.png",
            "R_BG_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
            "True", "images/RogueSprite/Rogue_panties.png",            
            ),
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "R_BG_Tan and Rogue_Arms == 1 and R_BG_Arms == 'gloved' and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms1a_gloved.png",       #Gloves and collar 
            "Rogue_Arms == 1 and R_BG_Arms == 'gloved' and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",       #Gloves and collar 
            "R_BG_Tan and Rogue_Arms == 1 and R_BG_Arms == 'gloved'", "images/RogueSprite/Rogue_tarms1b_gloved.png",                                     #Gloves, no collar
            "Rogue_Arms == 1 and R_BG_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "R_BG_Tan and Rogue_Arms == 1 and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms1a_bare.png",                                #No Gloves, collar 
            "Rogue_Arms == 1 and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_bare.png",                                #No Gloves, collar 
            "R_BG_Tan and Rogue_Arms == 1", "images/RogueSprite/Rogue_tarms1b_bare.png",                                                              #No gloves, no collar
            "Rogue_Arms == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "R_BG_Tan and R_BG_Arms == 'gloved' and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_gloved.png",                           #Gloves and collar 
            "R_BG_Arms == 'gloved' and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",                           #Gloves and collar 
            "R_BG_Tan and R_BG_Arms == 'gloved'", "images/RogueSprite/Rogue_tarms2b_gloved.png",                                                         #Gloved, no collar
            "R_BG_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved.png",                                                         #Gloved, no collar
            "R_BG_Tan and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_bare.png",                                                    #No gloves, collar
            "R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare.png",                                                    #No gloves, collar
            "R_BG_Tan", "images/RogueSprite/Rogue_tarms2b_bare.png",                                                                         #No gloves, no collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "Rogue_Arms == 1 and R_BG_Arms == 'classic gloves'", "images/RogueSprite/Rogue_Sprite_XGloves1.png",                                     #Gloves, no collar
            "R_BG_Arms == 'classic gloves'", "images/RogueSprite/Rogue_Sprite_XGloves2.png",                                                         #Gloved, no collar
            "True", Null(),                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(                                                                         #chest layer
            "R_BG_Tan == 'tan1' and R_BG_Pierce == 'barbell'", "images/RogueSprite/Rogue_t1chest_barbell.png",            
            "R_BG_Tan == 'tan' and R_BG_Pierce == 'barbell'", "images/RogueSprite/Rogue_tchest_barbell.png",            
            "R_BG_Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            "R_BG_Tan == 'tan1' and R_BG_Pierce == 'ring'", "images/RogueSprite/Rogue_t1chest_rings.png",      
            "R_BG_Tan == 'tan' and R_BG_Pierce == 'ring'", "images/RogueSprite/Rogue_tchest_rings.png",      
            "R_BG_Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "R_BG_Tan == 'tan1'", "images/RogueSprite/Rogue_t1chest_bare.png",     
            "R_BG_Tan == 'tan'", "images/RogueSprite/Rogue_tchest_bare.png",     
            "True", "images/RogueSprite/Rogue_chest_bare.png",     
            ),   
        (0,0), ConditionSwitch(                                                                         #chest clothes layer
            "R_BG_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
            "R_BG_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
            "R_BG_Chest == 'blue sports bra'", "images/RogueSprite/Rogue_chest_bysportsbra.png",
            "R_BG_Chest == 'red sports bra'", "images/RogueSprite/Rogue_chest_rysportsbra.png",
            "R_BG_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
            "R_BG_Chest == 'green top'", "images/RogueSprite/Rogue_GrnTop.png",
            "R_BG_Chest == 'SR7 tank short'", "images/RogueSprite/Rogue_chest_tankshort_SR7.png",
            "R_BG_Chest == 'tank short'", "images/RogueSprite/Rogue_chest_tankshort.png",
            "R_BG_Chest == 'slut tank short'", "images/RogueSprite/Rogue_chest_tankshort_slut.png",
            "R_BG_Chest == 'tape'", "images/RogueSprite/Rogue_chest_tape.png",
            "R_BG_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            "Rogue_Arms == 1 and R_BG_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            "R_BG_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            "Rogue_Arms == 1 and R_BG_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            "R_BG_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            "R_BG_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            "R_BG_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(  
            "R_BG_Chest == 'swimsuit1' or R_BG_Panties == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1.png",
            "R_BG_Chest == 'swimsuit2' or R_BG_Panties == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(  
            "R_BG_BodySuit == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1.png",
            "R_BG_BodySuit == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2.png",
            "Rogue_Arms == 1 and R_BG_BodySuit == 'classic uniform'", "images/RogueSprite/Rogue_Sprite_XCatsuit1.png",
            "R_BG_BodySuit == 'classic uniform'", "images/RogueSprite/Rogue_Sprite_XCatsuit2.png",
            "Rogue_Arms == 1 and R_BG_BodySuit == 'classic uniform damaged'", "images/RogueSprite/Rogue_Sprite_XCatsuit1_Dmg.png",
            "R_BG_BodySuit == 'classic uniform damaged'", "images/RogueSprite/Rogue_Sprite_XCatsuit2_Dmg.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                         #chest clothes layer
            "R_BG_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            "Rogue_Arms == 1 and R_BG_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            "R_BG_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            "Rogue_Arms == 1 and R_BG_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            "R_BG_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            "R_BG_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            #"R_BG_Chest == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1_Top.png",
            #"R_BG_Chest == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2_Top.png",
            "R_BG_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                         #full hose/tights              
            "R_BG_Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",                  
            "R_BG_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            "R_BG_Hose == 'SR7 hose'", "images/RogueSprite/Rogue_hose_SR7.png",       
            "R_BG_Hose == 'fishnet'", "images/RogueSprite/Rogue_hose_fishnet.png",       
            "R_BG_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "R_BG_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            "R_BG_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #brows
            # "R_BG_Brows == 'normal' and R_BG_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            # "R_BG_Brows == 'angry' and R_BG_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            # "R_BG_Brows == 'sad' and R_BG_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            # "R_BG_Brows == 'surprised' and R_BG_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            # "R_BG_Brows == 'confused' and R_BG_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "R_BG_Brows == 'normal'", "images/RogueSprite/Rogue_brows_normal.png",
            "R_BG_Brows == 'angry'", "images/RogueSprite/Rogue_brows_angry.png",
            "R_BG_Brows == 'sad'", "images/RogueSprite/Rogue_brows_sad.png",
            "R_BG_Brows == 'surprised'", "images/RogueSprite/Rogue_brows_surprised.png",        
            "R_BG_Brows == 'confused'", "images/RogueSprite/Rogue_brows_confused.png",
            "True", "images/RogueSprite/Rogue_brows_normal.png",
            ),
        (0,0), ConditionSwitch(  
            "R_BG_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                       #Mouths        
            "R_BG_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                       #Mouths        
            "R_BG_Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "R_BG_Tan and R_BG_Mouth == 'lipbite'", "images/RogueSprite/Rogue_tmouth_lipbite.png",
            "R_BG_Mouth == 'lipbite'", "images/RogueSprite/Rogue_mouth_lipbite.png",
            "R_BG_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking.png",            
            "R_BG_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_kiss.png",
            "R_BG_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad.png",
            "R_BG_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile.png",
            "R_BG_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_surprised.png",            
            "R_BG_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue.png",                
            "R_BG_Mouth == 'grimace'", "images/RogueSprite/Rogue_mouth_grimace.png",           
            "True", "images/RogueSprite/Rogue_mouth_normal.png",
            ),            
        (0,0), "Rogue Blink_BG",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_BG_Glasses == 'glasses'", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "R_BG_Glasses == 'sunglasses'", "images/RogueSprite/Rogue_Sprite_Glasses_black.png",   
            "True", Null(),                #R_BG_Arms == 'gloved' or not R_BG_Arms
            ), 
        (0,0), ConditionSwitch(                                                                      
            "R_BG_Headband", "images/RogueSprite/Rogue_Sprite_XHeadband.png",   
            "True", Null(),
            ),                                                                           
            
        (0,0), ConditionSwitch(                                                                         #Pants and Skirts
            "R_BG_Boots == 'boots' and R_BG_Legs == 'pants' and R_BG_Upskirt", "images/RogueSprite/Rogue_legs_pants_boots_down.png", 
            "R_BG_Boots == 'boots' and R_BG_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants_boots.png", 
            "R_BG_Legs == 'leather pants' and R_BG_Upskirt", "images/RogueSprite/Rogue_LeatherPants_Down.png", 
            "R_BG_Legs == 'leather pants'", "images/RogueSprite/Rogue_LeatherPants.png", 
            "R_BG_Legs == 'pants' and R_BG_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            "R_BG_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            "R_BG_Legs == 'shorts' and R_BG_Upskirt", "images/RogueSprite/Rogue_shorts_down.png",
            "R_BG_Legs == 'red shorts' and R_BG_Upskirt", "images/RogueSprite/Rogue_ryshorts_down.png",
            "R_BG_Legs == 'blue shorts' and R_BG_Upskirt", "images/RogueSprite/Rogue_byshorts_down.png",  
            "R_BG_Legs == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
            "R_BG_Legs == 'red shorts'", "images/RogueSprite/Rogue_ryshorts.png",
            "R_BG_Legs == 'blue shorts'", "images/RogueSprite/Rogue_byshorts.png",
            "R_BG_Legs == 'skirt' and R_BG_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "R_BG_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            "R_BG_Legs == 'skirtshort' and R_BG_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_up.png",
            "R_BG_Legs == 'skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort.png", 
            "R_BG_Legs == 'SR7 skirtshort' and R_BG_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_SR7_up.png",
            "R_BG_Legs == 'SR7 skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort_SR7.png",  
            #"R_BG_Legs == 'skirtshort'", AlphaMask("images/RogueSprite/Rogue_legs_skirtshort.png", "images/RogueSprite/Rogue_legs_skirtshort_alphamask.png"),
            "R_BG_Legs == 'cheerleader skirt' and R_BG_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Up.png",
            "R_BG_Legs == 'cheerleader skirt'", "images/RogueSprite/Rogue_Cheerleader_Skirt.png",
            "R_BG_Legs == 'cheerleader skirtshort' and R_BG_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short_Up.png",            
            "R_BG_Legs == 'cheerleader skirtshort'", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short.png",
            "True", Null(),   
            ),
        (0,0), ConditionSwitch(                                                                         
            "R_BG_Boots == 'boots'", "images/RogueSprite/Rogue_Highshoes.png",
            "R_BG_Boots == 'classic boots'", "images/RogueSprite/Rogue_Sprite_XShoes.png",
            "True", Null(),  
            ), 

        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "Rogue_Arms == 1", Null(),                                                              #No gloves, no collar
            "R_BG_Tan and R_BG_Arms == 'gloved' and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_gloved_.png",                           #Gloves and collar 
            "R_BG_Arms == 'gloved' and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved_.png",                           #Gloves and collar 
            "R_BG_Tan and R_BG_Arms == 'gloved'", "images/RogueSprite/Rogue_tarms2b_gloved_.png",                                                         #Gloved, no collar
            "R_BG_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved_.png",                                                         #Gloved, no collar
            "R_BG_Tan and R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_bare_.png",                                                    #No gloves, collar
            "R_BG_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare_.png",                                                    #No gloves, collar
            "R_BG_Tan", "images/RogueSprite/Rogue_tarms2b_bare_.png",                                                                         #No gloves, no collar
            "True", "images/RogueSprite/Rogue_arms2b_bare_.png",  
            ), 
        
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "Rogue_Arms == 1", Null(),                                                             
            "R_BG_BodySuit == 'classic uniform' or R_BG_BodySuit == 'classic uniform damaged'", "images/RogueSprite/Rogue_Sprite_XCatsuit2_.png",
            "True", Null(),
            ),                 
        (0,0), ConditionSwitch(                                                                         #water
            "R_BG_Water and Rogue_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "R_BG_Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         #soap
            "R_BG_Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         #accessories
            "R_BG_Accessory == 'classic belt' and Rogue_Arms == 1", "images/RogueSprite/Rogue_Sprite_Over_XBelt1.png",
            "R_BG_Accessory == 'classic belt'", "images/RogueSprite/Rogue_Sprite_Over_XBelt2.png",
            "True", Null(),
            ),  
        
        (0,0), ConditionSwitch(                                                                         #Overshirt layer
            "Rogue_Arms == 1 and R_BG_Over == 'SR7 mesh top'", "images/RogueSprite/Rogue_over_mesh_SR7_1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'white mesh top'", "images/RogueSprite/Rogue_over_whitemesh1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'blue mesh top'", "images/RogueSprite/Rogue_over_bluemesh1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'red mesh top'", "images/RogueSprite/Rogue_over_redmesh1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'yellow mesh top'", "images/RogueSprite/Rogue_over_yellowmesh1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'black mesh top'", "images/RogueSprite/Rogue_over_blackmesh1.png",           
            "Rogue_Arms == 1 and R_BG_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'red top'", "images/RogueSprite/Rogue_over_red1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'classic jacket'", "images/RogueSprite/Rogue_Sprite_Over_XJacket1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'jacket'", "images/RogueSprite/Rogue_Jacket1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodie1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'black hoodie'", "images/RogueSprite/Rogue_over_dhoodie1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'red dress' and R_BG_Upskirt", "images/RogueSprite/Rogue_reddress_up_1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'red dress'", "images/RogueSprite/Rogue_reddress_1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'blue dress' and R_BG_Upskirt", "images/RogueSprite/Rogue_bluedress_up_1.png",
            "Rogue_Arms == 1 and R_BG_Over == 'blue dress'", "images/RogueSprite/Rogue_bluedress_1.png",
            "R_BG_Over == 'SR7 mesh top'", "images/RogueSprite/Rogue_over_mesh_SR7_2.png",
            "R_BG_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png",
            "R_BG_Over == 'white mesh top'", "images/RogueSprite/Rogue_over_whitemesh2.png",
            "R_BG_Over == 'blue mesh top'", "images/RogueSprite/Rogue_over_bluemesh2.png",
            "R_BG_Over == 'red mesh top'", "images/RogueSprite/Rogue_over_redmesh2.png",
            "R_BG_Over == 'yellow mesh top'", "images/RogueSprite/Rogue_over_yellowmesh2.png",
            "R_BG_Over == 'black mesh top'", "images/RogueSprite/Rogue_over_blackmesh2.png", 
            "R_BG_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
            "R_BG_Over == 'red top'", "images/RogueSprite/Rogue_over_red2.png",
            "R_BG_Over == 'classic jacket'", "images/RogueSprite/Rogue_Sprite_Over_XJacket2.png",
            "R_BG_Over == 'jacket'", "images/RogueSprite/Rogue_Jacket2.png",
            "R_BG_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
            "R_BG_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodie2.png",
            "R_BG_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie2.png",
            "R_BG_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie2.png",
            "R_BG_Over == 'black hoodie'", "images/RogueSprite/Rogue_over_dhoodie2.png",
            "R_BG_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie2.png",
            "R_BG_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
            "R_BG_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",  
            "R_BG_Over == 'red dress' and R_BG_Upskirt", "images/RogueSprite/Rogue_reddress_up_2.png",
            "R_BG_Over == 'red dress'", "images/RogueSprite/Rogue_reddress_2.png",
            "R_BG_Over == 'blue dress' and R_BG_Upskirt", "images/RogueSprite/Rogue_bluedress_up_2.png",            
            "R_BG_Over == 'blue dress'", "images/RogueSprite/Rogue_bluedress_2.png",            
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         #accessories
            "not R_BG_Over", Null(),
            "R_BG_Over != 'red dress' and R_BG_Over != 'blue dress'", Null(),
            "R_BG_Accessory == 'classic belt' and Rogue_Arms == 1", "images/RogueSprite/Rogue_Sprite_Over_XBelt1.png",
            "R_BG_Accessory == 'classic belt'", "images/RogueSprite/Rogue_Sprite_Over_XBelt2.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_BG_Hair == 'evo' and R_BG_Water and R_BG_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_wet.png",
            "R_BG_Hair == 'evo' and R_BG_Water and R_BG_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            "R_BG_Hair == 'evo' and R_BG_Water and R_BG_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_wet.png",
            "R_BG_Hair == 'evo' and R_BG_Water and R_BG_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            "R_BG_Hair == 'evo' and R_BG_Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_BG_Hair == 'evo' and R_BG_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_evo.png",
            "R_BG_Hair == 'evo' and R_BG_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            "R_BG_Hair == 'evo' and R_BG_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_evo.png",
            "R_BG_Hair == 'evo' and R_BG_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "R_BG_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo.png",
            "R_BG_Hair == 'newhair' and R_BG_Water", "images/RogueSprite/Rogue_hair_wet_newhair.png",
            "R_BG_Hair == 'newhair'", "images/RogueSprite/Rogue_hair_evo_newhair.png",
            "True", Null(), 
            ),                           
        )                 
    anchor (0.6, 0.0)               
    zoom .75             
    
image Rogue Blink_BG:
    ConditionSwitch(
    "R_BG_Eyes == 'sexy'", "images/RogueSprite/Rogue_eyes_sexy.png",
    "R_BG_Eyes == 'side'", "images/RogueSprite/Rogue_eyes_side.png",
    "R_BG_Eyes == 'surprised'", "images/RogueSprite/Rogue_eyes_surprised.png",
    "R_BG_Eyes == 'normal'", "images/RogueSprite/Rogue_eyes_normal.png",    
    "R_BG_Eyes == 'stunned'", "images/RogueSprite/Rogue_eyes_stunned.png",
    "R_BG_Eyes == 'down'", "images/RogueSprite/Rogue_eyes_down.png",
    "R_BG_Eyes == 'closed'", "images/RogueSprite/Rogue_eyes_closed.png",
    "R_BG_Eyes == 'manic'", "images/RogueSprite/Rogue_eyes_manic.png",
    "R_BG_Eyes == 'squint'", "Rogue_Squint_BG",
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

image Rogue_Squint_BG:
    "images/RogueSprite/Rogue_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueSprite/Rogue_eyes_squint.png"
    .25
    repeat 
# End Rogue Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Define_Outfit_BG:
    default L_BG_Arms = "wrists"                  #her gloves
    default L_BG_Legs = "mesh pants"
    default L_BG_Over = 0    
    default L_BG_Chest = "leather bra"    
    default L_BG_Neck = "leash choker"
    default L_BG_Hair = "long"
    default L_BG_Panties = "lace panties"
    default L_BG_Boots = 0
    default L_BG_Pubes = 1
    default L_BG_Pierce = 0
    default L_BG_Hose = 0
    default L_BG_Glasses = 0
    default L_BG_HeadBand = 0
    default L_BG_Tan = 0
    default L_BG_Gloves = 0
    default L_BG_DynamicTan = [0,0,0,0,0]

    default R_BG_Arms = 0                  #her gloves
    default R_BG_Neck = "spiked collar"
    default R_BG_Legs = "skirtshort"
    default R_BG_Over = "SR7 mesh top"    
    default R_BG_Chest = "SR7 tank short"    
    default R_BG_Hair = "evo"
    default R_BG_Pubes = 1
    default R_BG_Pierce = 0
    default R_BG_HairColor = "blondewhite"
    default R_BG_Panties = "black panties"
    default R_BG_Boots = 0
    default R_BG_Hose = "SR7 hose"
    default R_BG_Glasses = "glasses"
    default R_BG_Headband = "classic headband"
    default R_BG_Tan = 0
    default R_BG_Water = 0
    default R_BG_Gloves = 0
    default R_BG_DynamicTan = [0,0,0,0,0]
    default R_BG_BodySuit = 0
    default R_BG_Upskirt = 0
    default R_BG_Brows = 0
    default R_BG_Eyes = 0
    default R_BG_Mouth = 0
    default R_BG_Gag = 0
    default R_BG_Accessory = 0

    default K_BG_Arms = 1                  #arm pose
    default K_BG_Neck = 0
    default K_BG_Legs = 0
    default K_BG_Over = 0    
    default K_BG_Chest = "purple bikini bra"    
    default K_BG_Hair = "long"
    default K_BG_Pubes = 1
    default K_BG_Pierce = 0
    default K_BG_HairColor = "black"
    default K_BG_Panties = "kitty lingerie panties"
    default K_BG_Boots = 0
    default K_BG_Hose = "stockings"
    default K_BG_Glasses = 0
    default K_BG_HeadBand = "pink"
    default K_BG_Tan = "tan"
    default K_BG_Gloves = "black gloves"
    default K_BG_DynamicTan = [0,0,0,0,0]

    default E_BG_Arms = "black gloves"                  #her gloves
    default E_BG_Neck = "NewX black"
    default E_BG_Legs = 0
    default E_BG_Over = "black cape"    
    default E_BG_Chest = "black corset"    
    default E_BG_Hair = "wet"
    default E_BG_Pubes = 1
    default E_BG_Pierce = 0
    default E_BG_HairColor = "blonde"
    default E_BG_Panties = "black panties"
    default E_BG_Boots = 0
    default E_BG_Hose = "black thigh high"
    default E_BG_Glasses = 0
    default E_BG_HeadBand = 0
    default E_BG_Tan = 0
    # default E_BG_Gloves = "black gloves"
    default E_BG_DynamicTan = [0,0,0,0,0]
