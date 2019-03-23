
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

