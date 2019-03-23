
image Laura_Sprite_BG:
    LiveComposite(        
        (402,965),
        (0,0), ConditionSwitch(
            #hair back 
            "not L_BG_Hair", Null(),
            "renpy.showing('Laura_BJ_Animation')", Null(), 
            "L_BG_Hair", "Laura_Sprite_HairBack",   
            "True", Null(),        
            ),   
        (0,0), ConditionSwitch(            
            #panties down back 
            "not L_BG_Panties or not L_BG_PantiesDown or (L_BG_Legs == 'pants' and not L_BG_Upskirt)", Null(), 
            "L_BG_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",   
            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",   
            ), 
        (0,0), ConditionSwitch(
            #backside of arms
            "L_BG_Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",   
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png", #if L_BG_Arms == 1 
            ),     
        #body
        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",
        (0,0), ConditionSwitch(
            #pubes 
            "L_BG_Pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(
            #stockings    
            "L_BG_Hose == 'stockings' or L_BG_Hose == 'stockings and garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            #garterbelt    
            "L_BG_Hose == 'stockings and garterbelt' or L_BG_Hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
            "True", Null(),
            ),              
        (0,0), ConditionSwitch(
            #panties    
            "not L_BG_Panties", Null(),
            "L_BG_PantiesDown", ConditionSwitch(                   
                    #if the panties are down
                    "not L_BG_Legs or L_BG_Upskirt or L_BG_Legs == 'skirt'", ConditionSwitch(                   
                            #if she's wearing a skirt or nothing else                    
                            "L_BG_Panties == 'wolvie panties' and L_BG_Wet", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png", 
                            "L_BG_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",                             
                            "L_BG_Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", 
                            "L_BG_Panties == 'black panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png", #fix
                            "True", Null(),
                            ),         
                    "True", Null(),
                    ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
                    "L_BG_Wet", ConditionSwitch(   
                        #if she's  wet                            
                        "L_BG_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                        "L_BG_Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),
                    "True", ConditionSwitch(   
                        #if she's not wet                            
                        "L_BG_Panties == 'wolvie panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        "L_BG_Panties == 'lace panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png", 
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png", 
                        ),                    
                    ),    
            ),            
        (0,0), ConditionSwitch(
            #pants    
            "not L_BG_Legs", Null(),
            "L_BG_Upskirt", ConditionSwitch(                
                        #if the skirt's up or pants down 
                        "L_BG_Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png", 
                        "True", Null(),                       
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "L_BG_Wet", ConditionSwitch(   
                        #if she's not wet
                        "L_BG_Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",  
                        "L_BG_Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",   
                        "L_BG_Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    "True", ConditionSwitch(   
                        #if she's wet
                        "L_BG_Legs == 'leather pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",   
                        "L_BG_Legs == 'mesh pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",  
                        "L_BG_Legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),                  
            ),    
        
        (0,0), ConditionSwitch(
            #arms midlayer
            "L_BG_Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",         # one hand up
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png", #if L_BG_Arms == 1   # Crossed        
            ),  
        (0,0), ConditionSwitch(
            #arms wristband
            "L_BG_Arms == 'wrists' and L_BG_Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png", # one hand up
            "L_BG_Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png", # one hand up
            "True", Null(),     
            ), 
        
        (0,0), ConditionSwitch(
            #L Over under
            "L_BG_Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png", # one hand up
            "True", Null(),     
            ), 
        # tits
        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png", 

        
        (0,0), ConditionSwitch(                          
            #neck
            "L_BG_Neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",       
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                        
            #Chest layer
            "L_BG_Chest == 'leather bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png", 
            "L_BG_Chest == 'wolvie top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",   
            "L_BG_Chest == 'sports bra'", "images/LauraSprite/Laura_Sprite_Bra_Sports.png",   
            "L_BG_Chest == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",   
            "True", Null(),              
            ),            

        (0,0), ConditionSwitch(
            #L Over
            "L_BG_Over == 'jacket' and L_BG_Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png", # one hand up
            "L_BG_Over == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png", # one hand up
            "L_BG_Over == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
            "True", Null(),     
            ), 
        
        #Head
        (0,0), ConditionSwitch(
            # head
            "renpy.showing('Laura_BJ_Animation')", Null(),  
            "True", "Laura_Sprite_Head_BG",   
            ),         
        (0,0), ConditionSwitch(
            #arms toplayer
            "L_BG_Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #arms wristband
            "L_BG_Girl_Arms == 2 and L_BG_Arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #jacket arm toplayer
            "L_BG_Over == 'jacket' and L_BG_Girl_Arms == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png", # one hand up
            "True", Null(),     
            ), 
        (0,0), ConditionSwitch(
            #claws
            "L_BG_Girl_Arms == 2 and L_BG_Claws", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
            "True", Null(),     
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
                "L_BG_Blush == 2", "images/LauraSprite/Laura_Sprite_Head_Blush2.png", 
                "L_BG_Blush", "images/LauraSprite/Laura_Sprite_Head_Blush.png",  
                "True", "images/LauraSprite/Laura_Sprite_Head.png",                        
                ),        
        # (0,0), ConditionSwitch(#Mouths 
        #     "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
        #     "L_BG_Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
        #     "L_BG_Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
        #     "L_BG_Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
        #     "L_BG_Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
        #     "L_BG_Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
        #     "L_BG_Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
        #     "L_BG_Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
        #     "L_BG_Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
        #     "L_BG_Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
        #     "L_BG_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
        #     "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
        #     ),   
        (0,0), "Laura Mouth_BG",     #Mouth    

        (0,0), ConditionSwitch(                                                                       
            #brows
            "L_BG_Blush >= 2", ConditionSwitch(
                    "L_BG_Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "L_BG_Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "L_BG_Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "L_BG_Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",        
                    "L_BG_Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "L_BG_Brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "L_BG_Brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "L_BG_Brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "L_BG_Brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",        
                    "L_BG_Brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Laura Blink_BG",     #Eyes    
        (0,0), ConditionSwitch(                
            #Hair mid
            "L_BG_Over == 'jacket'", Null(),
            "L_BG_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not L_BG_Hair", Null(),
            "L_BG_Hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not L_BG_Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
            ),
        )                
    anchor (0.6, 0.0)                
    zoom .5               

image Laura Blink_BG:            
    ConditionSwitch(
    "L_BG_Eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
    "L_BG_Eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
    "L_BG_Eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
    "L_BG_Eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",    
    "L_BG_Eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
    "L_BG_Eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
    "L_BG_Eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
    "L_BG_Eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
    "L_BG_Eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "L_BG_Eyes == 'squint'", "Laura_Squint_BG",
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

image Laura Mouth_BG:            
    ConditionSwitch(
    "L_BG_Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
    "L_BG_Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
    "L_BG_Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",            
    "L_BG_Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
    "L_BG_Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
    "L_BG_Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
    "L_BG_Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",            
    "L_BG_Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",                
    "L_BG_Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",              
    "L_BG_Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",                    
    "True", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3 
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

# Start Kitty Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sprite_BG:        
    LiveComposite(
        (480,960),                                                                    
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_HairBack_BG",   
            ),         
        (0,0), ConditionSwitch(   
            "K_BG_Tan == 'tan' and K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_TArms_Armbinder.png",                                                                      #Arms1               
            "K_BG_Tan == 'tan2' and K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_T2Arms_Armbinder.png",                                                                      #Arms1               
            "K_BG_Tan == 'tan3' and K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_T3Arms_Armbinder.png",                                                                      #Arms1               
            "K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_Arms_Armbinder.png",                                                                      #Arms1               
            "not K_BG_Arms and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TArms1.png",
            "not K_BG_Arms and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Arms1.png",
            "not K_BG_Arms and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Arms1.png",
            "not K_BG_Arms", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),               
            ), 

        (0,0), ConditionSwitch(   
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'darker lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_DarkerLace.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'purple bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'red bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini2.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'white cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_WhiteCami1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'kitty lingerie top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'orange top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Orange1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'black top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Black1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'leather top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Leather1.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'swimsuit3'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Swimsuit3.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra' and K_BG_PantiesDown", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_Bustier.png"),
            "not K_BG_Arms and K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra open'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms1.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                         #piercings bottom
            "K_BG_Over == 'armbinder'", Null(),                                                                      #Arms1               
            "not K_BG_Arms and K_BG_Gloves == 'black gloves'", "images/KittySprite/Kitty_Sprite_BlackLongGloves_1.png",      
            "True", Null(),   
            ),  
        (0,0), ConditionSwitch(                                                                         #back of the shirt
            "K_BG_Over == 'dark top' and K_BG_Arms", "images/KittySprite/Kitty_Sprite_Under_dark2.png",       #2
            "K_BG_Over == 'dark top'", "images/KittySprite/Kitty_Sprite_Under_dark1.png",                  #1
            "K_BG_Over == 'pink top' and K_BG_Arms", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",       #2
            "K_BG_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",                  #1
            "K_BG_Over == 'black dress'", "images/KittySprite/Kitty_Sprite_Dress.png",                  #1
            "True", Null(),               
            ),
        (0,0), ConditionSwitch(                                                                     #body
            "K_BG_Tan == 'tan' and K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_TBody_Bare1.png",                                                                      #Arms1               
            "K_BG_Tan == 'tan2' and K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_T2Body_Bare1.png",                                                                      #Arms1               
            "K_BG_Tan == 'tan3' and K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_T3Body_Bare1.png",                                                                      #Arms1               
            "K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",                                                                      #Arms1               
            "K_BG_Arms and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TBody_Bare2.png",               
            "K_BG_Arms and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Body_Bare2.png",
            "K_BG_Arms and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",
            "K_BG_Arms", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TBody_Bare1.png",    
            "True and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Body_Bare1.png",
            "True and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Body_Bare1.png",
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",    
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'white cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_WhiteCami1.png"),
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'orange top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Orange1.png"),
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'kitty lingerie top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top1.png"),
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'black top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Black1.png"),
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'leather top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Leather1.png"),
            "K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'swimsuit3'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Swimsuit3.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'darker lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bra_DarkerLace.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'purple bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'red bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Cami2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'white cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_WhiteCami2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'kitty lingerie top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'orange top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Orange2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'black top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Black2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'leather top'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Leather2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'swimsuit3'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Swimsuit3_2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra' and K_BG_PantiesDown", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_Bustier.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra open'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare2.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'green panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Green.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'white panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_White.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'lace panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Lace.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'kitty lingerie panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_KittyLingerie_Panties.png"), 
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'darker lace panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_DarkerLace.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'purple bikini panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Panties_Bikini1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'zipper panties'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_BDPanty.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[4] == 'zipper panties open'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_BDPantyOpen.png"),
            "True", Null(),             
            ),

        (0,0), ConditionSwitch(                                                                     #body
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'capris'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Blue.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'black jeans'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Black.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'black blue pants'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_BlackBluePants.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'leather pants'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Leather.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'orange skirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Orange.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'black skirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_OBlack.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'white skirt'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_OWhite.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'yoga pants'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png"),  
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'shorts'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_Shorts.png"),            
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'blue shorts'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_BlueShorts.png"),            
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[2] == 'white shorts'", AlphaMask("images/KittySprite/Kitty_Sprite_Body_Bare1.png", "images/KittySprite/Kitty_Sprite_WhiteShorts.png"),  
            "True", Null(),             
            ),


        (0,0), ConditionSwitch(                                                                         #body
   
            "K_BG_Pubes and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_Body_Hair_PubesBlack.png",               
            "K_BG_Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair_Pubes.png",               
            "K_BG_Arms and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TBody_Bare2.png",               
            "K_BG_Arms and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Body_Bare2.png",               
            "K_BG_Arms and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Body_Bare2.png",               
            "K_BG_Arms", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",               
            "True", Null(),  
            ),
        
        

        (0,0), ConditionSwitch(                                                                         #piercings bottom
            "not K_BG_Pierce or (K_BG_Panties and not K_BG_PantiesDown)", Null(),                       
            "K_BG_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",   
            ),    
        
        (0,0), ConditionSwitch(                                                                         #panties
            "not K_BG_Panties", Null(),
            "K_BG_PantiesDown and (not K_BG_Legs or K_BG_Upskirt)", Null(), #If panties are down, and pants are either off or down, skip this
            "K_BG_Wet and K_BG_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'white panties'", "images/KittySprite/Kitty_Sprite_Panties_White_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'purple bikini panties'", "images/KittySprite/Kitty_Sprite_Panties_Bikini1_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",            
            "K_BG_Wet and K_BG_Panties == 'kitty lingerie panties'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Panties_Wet.png",            
            "K_BG_Wet and K_BG_Panties == 'darker lace panties'", "images/KittySprite/Kitty_Sprite_Panties_DarkerLace_Wet.png",            
            "K_BG_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
            "K_BG_Panties == 'white panties'", "images/KittySprite/Kitty_Sprite_Panties_White.png",
            "K_BG_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
            "K_BG_Panties == 'kitty lingerie panties'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Panties.png",            
            "K_BG_Panties == 'darker lace panties'", "images/KittySprite/Kitty_Sprite_Panties_DarkerLace.png",
            "K_BG_Panties == 'purple bikini panties'", "images/KittySprite/Kitty_Sprite_Panties_Bikini1.png",
            "K_BG_Panties == 'zipper panties'", "images/KittySprite/Kitty_Sprite_BDPanty.png",
            "K_BG_Panties == 'zipper panties open'", "images/KittySprite/Kitty_Sprite_BDPantyOpen.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #panties down
            "not K_BG_Panties", Null(),
            "not K_BG_PantiesDown or (K_BG_Legs and not K_BG_Upskirt)", Null(), #If panties are not down or if  pants are on and up, skip this
            "K_BG_Wet and K_BG_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'white panties'", "images/KittySprite/Kitty_Sprite_Panties_White_Down_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'purple bikini panties'", "images/KittySprite/Kitty_Sprite_Panties_Bikini1_Down_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
            "K_BG_Wet and K_BG_Panties == 'kitty lingerie panties'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Panties_Wet.png",            
            "K_BG_Wet and K_BG_Panties == 'darker lace panties'", "images/KittySprite/Kitty_Sprite_Panties_DarkerLace_Down_Wet.png",
            "K_BG_Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
            "K_BG_Panties == 'white panties'", "images/KittySprite/Kitty_Sprite_Panties_White_Down.png",
            "K_BG_Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
            "K_BG_Panties == 'kitty lingerie panties'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Panties_Down.png",            
            "K_BG_Panties == 'darker lace panties'", "images/KittySprite/Kitty_Sprite_Panties_DarkerLace_Down.png",
            "K_BG_Panties == 'purple bikini panties'", "images/KittySprite/Kitty_Sprite_Panties_Bikini1_Down.png",
            "K_BG_Panties == 'zipper panties'", "images/KittySprite/Kitty_Sprite_BDPantyOpen.png",
            "K_BG_Panties == 'zipper panties open'", "images/KittySprite/Kitty_Sprite_BDPantyOpen.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #wetness                    
            "K_BG_Legs or not K_BG_Wet", Null(),             
            "K_BG_Panties and not K_BG_PantiesDown and K_BG_Wet < 2", Null(),
            "K_BG_Panties and not K_BG_PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "K_BG_Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),  
        
        (0,0), ConditionSwitch(                                                                         #Arms2               
            "K_BG_Over == 'armbinder'", Null(),                                                                                  
            "K_BG_Arms and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_TArms2.png",
            "K_BG_Arms and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2Arms2.png",
            "K_BG_Arms and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3Arms2.png",
            "K_BG_Arms", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),               
            ), 

        (0,0), ConditionSwitch(                                                                         #Arms2               
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Cami2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'white cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_WhiteCami2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'orange top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Orange2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'kitty lingerie top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'black top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Black2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'leather top'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Leather2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'swimsuit3'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Swimsuit3_2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'darker lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bra_DarkerLace.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'purple bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini1.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'red bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini2.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'bustier bra' and K_BG_PantiesDown", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'bustier bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_Bustier.png"),
            "K_BG_Arms and K_BG_DynamicTan[0] and K_BG_Arms and K_BG_DynamicTan[3] == 'bustier bra open'", AlphaMask("images/KittySprite/Kitty_Sprite_Arms2.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                         #piercings bottom
            "K_BG_Over == 'armbinder'", Null(),                                                                      #Arms1               
            "K_BG_Arms and K_BG_Gloves == 'black gloves'", "images/KittySprite/Kitty_Sprite_BlackLongGloves_2.png",      
            "True", Null(),   
            ), 
        (0,0), ConditionSwitch(                                                                         #chest
            "not K_BG_Chest and not K_BG_Over and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_Tchest_bare.png",
            "not K_BG_Chest and not K_BG_Over and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2chest_bare.png",
            "not K_BG_Chest and not K_BG_Over and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3chest_bare.png",
            "not K_BG_Chest and not K_BG_Over", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
            "True and K_BG_Tan == 'tan'", "images/KittySprite/Kitty_Sprite_Tchest_bare.png",
            "True and K_BG_Tan == 'tan2'", "images/KittySprite/Kitty_Sprite_T2chest_bare.png",
            "True and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_T3chest_bare.png",
            "True", "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
            ),  
        (0,0), ConditionSwitch(                                                                     #body
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'darker lace bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bra_DarkerLace.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'sports bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'purple bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'red bikini bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bra_Bikini2.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Cami1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'white cami'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_WhiteCami1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'kitty lingerie top'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'orange top'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Orange1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'black top'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Black1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'leather top'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Leather1.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'swimsuit3'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Swimsuit3.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra' and K_BG_PantiesDown", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_Bustier.png"),
            "K_BG_DynamicTan[0] and K_BG_DynamicTan[3] == 'bustier bra open'", AlphaMask("images/KittySprite/Kitty_Sprite_Chest_Bare.png", "images/KittySprite/Kitty_Sprite_BustierOpen.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                         #piercings top
            "not K_BG_Pierce", Null(),                       
            "K_BG_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",   
            ),    
        (0,0), ConditionSwitch(                                                                         #Bra
            "not K_BG_Chest", Null(),
            "K_BG_Arms and K_BG_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
            "K_BG_Arms and K_BG_Chest == 'white cami'", "images/KittySprite/Kitty_Sprite_WhiteCami2.png",
            "K_BG_Arms and K_BG_Chest == 'orange top'", "images/KittySprite/Kitty_Sprite_Orange2.png",
            "K_BG_Arms and K_BG_Chest == 'kitty lingerie top'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top2.png",
            "K_BG_Arms and K_BG_Chest == 'black top'", "images/KittySprite/Kitty_Sprite_Black2.png",
            "K_BG_Arms and K_BG_Chest == 'leather top'", "images/KittySprite/Kitty_Sprite_Leather2.png",
            "K_BG_Arms and K_BG_Chest == 'swimsuit3'", "images/KittySprite/Kitty_Sprite_Swimsuit3_2.png",
            "K_BG_Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
            "K_BG_Chest == 'darker lace bra'", "images/KittySprite/Kitty_Sprite_Bra_DarkerLace.png",
            "K_BG_Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
            "K_BG_Chest == 'purple bikini bra'", "images/KittySprite/Kitty_Sprite_Bra_Bikini1.png",
            "K_BG_Chest == 'red bikini bra'", "images/KittySprite/Kitty_Sprite_Bra_Bikini2.png",
            "K_BG_Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
            "K_BG_Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
            "K_BG_Chest == 'white cami'", "images/KittySprite/Kitty_Sprite_WhiteCami1.png",
            "K_BG_Chest == 'kitty lingerie top'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Top1.png",
            "K_BG_Chest == 'orange top'", "images/KittySprite/Kitty_Sprite_Orange1.png",
            "K_BG_Chest == 'black top'", "images/KittySprite/Kitty_Sprite_Black1.png",
            "K_BG_Chest == 'leather top'", "images/KittySprite/Kitty_Sprite_Leather1.png",
            "K_BG_Chest == 'swimsuit3'", "images/KittySprite/Kitty_Sprite_Swimsuit3.png",
            "K_BG_Chest == 'bustier bra' and K_BG_PantiesDown", "images/KittySprite/Kitty_Sprite_BustierOpen.png",
            "K_BG_Chest == 'bustier bra'", "images/KittySprite/Kitty_Sprite_Bustier.png",
            "K_BG_Chest == 'bustier bra open'", "images/KittySprite/Kitty_Sprite_BustierOpen.png",
            "K_BG_Chest == 0 and (K_BG_Over == 'pink top' or K_BG_Over == 'dark top')", Null(),   #use for when bra and top clash  
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(                                                                         #pants         
            "K_BG_Hose == 'kitty lingerie socks'", "images/KittySprite/Kitty_Sprite_KittyLingerie_Socks_Thigh.png",            
            "K_BG_Hose == 'pink socks'", "images/KittySprite/Kitty_PSocks_Thigh.png",            
            "K_BG_Hose == 'white socks'", "images/KittySprite/Kitty_WSocks_Thigh.png",            
            "K_BG_Hose == 'black socks'", "images/KittySprite/Kitty_BSocks_Thigh.png",            
            "K_BG_Hose == 'stockings'", "images/KittySprite/Kitty_Stockings.png",            
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                         #pants         
            "K_BG_Legs == 'shorts' and K_BG_Upskirt", "images/KittySprite/Kitty_Sprite_Shorts_Down.png",            
            "K_BG_Legs == 'blue shorts' and K_BG_Upskirt", "images/KittySprite/Kitty_Sprite_BlueShorts_Down.png",            
            "K_BG_Legs == 'white shorts' and K_BG_Upskirt", "images/KittySprite/Kitty_Sprite_WhiteShorts_Down.png",            
            "not K_BG_Legs or K_BG_Upskirt", Null(),
            "K_BG_Legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "K_BG_Legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "K_BG_Legs == 'black blue pants'", "images/KittySprite/Kitty_Sprite_BlackBluePants.png",
            "K_BG_Legs == 'leather pants'", "images/KittySprite/Kitty_Sprite_Pants_Leather.png",
            "K_BG_Legs == 'orange skirt'", "images/KittySprite/Kitty_Sprite_Pants_Orange.png",
            "K_BG_Legs == 'black skirt'", "images/KittySprite/Kitty_Sprite_Pants_OBlack.png",
            "K_BG_Legs == 'white skirt'", "images/KittySprite/Kitty_Sprite_Pants_OWhite.png",
            "K_BG_Wet and K_BG_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",   
            "K_BG_Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",  
            "K_BG_Wet and K_BG_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",    
            "K_BG_Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",            
            "K_BG_Wet and K_BG_Legs == 'blue shorts'", "images/KittySprite/Kitty_Sprite_BlueShorts_Wet.png",    
            "K_BG_Legs == 'blue shorts'", "images/KittySprite/Kitty_Sprite_BlueShorts.png",            
            "K_BG_Wet and K_BG_Legs == 'white shorts'", "images/KittySprite/Kitty_Sprite_WhiteShorts_Wet.png",    
            "K_BG_Legs == 'white shorts'", "images/KittySprite/Kitty_Sprite_WhiteShorts.png",            
            "True", Null(),
            ),    
        
        (0,0), ConditionSwitch(                                                                         #piercings over shirt
            "not K_BG_Pierce or not K_BG_Chest", Null(),                       
            "K_BG_Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",      
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",   
            ),    
        
        (0,0), ConditionSwitch(                                                                         #necklace
            "K_BG_Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "K_BG_Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "True", Null(),
            ),          
        
        (0,0), ConditionSwitch(                                                                         #wet look
            "K_BG_Water and K_BG_Arms", "images/KittySprite/Kitty_Sprite_Water2.png",
            "K_BG_Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),  
        
        (0,0), ConditionSwitch(                                                                         #shirt
            "not K_BG_Over", Null(),
            "K_BG_Arms and K_BG_Over == 'dark top'", "images/KittySprite/Kitty_Sprite_Over_dark2.png",
            "K_BG_Arms and K_BG_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
            "K_BG_Arms and K_BG_Over == 'purple shirt'", "images/KittySprite/Kitty_Sprite_Over_CrewPurple2.png",
            "K_BG_Arms and K_BG_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
            "K_BG_Arms and K_BG_Over == 'violet shirt scarfless'", "images/KittySprite/Kitty_Sprite_Over_VioletShirt1_2.png",
            "K_BG_Arms and K_BG_Over == 'violet shirt scarf'", "images/KittySprite/Kitty_Sprite_Over_VioletShirt2_2.png",
            "K_BG_Arms and K_BG_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
            "K_BG_Over == 'dark top'", "images/KittySprite/Kitty_Sprite_Over_dark1.png",
            "K_BG_Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
            "K_BG_Over == 'purple shirt'", "images/KittySprite/Kitty_Sprite_Over_CrewPurple1.png",
            "K_BG_Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
            "K_BG_Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
            "K_BG_Over == 'black dress'", "images/KittySprite/Kitty_Sprite_Dress.png",
            "K_BG_Over == 'armbinder'", "images/KittySprite/Kitty_Sprite_Overshirt_Armbinder.png",   
            "K_BG_Over == 'violet shirt scarfless'", "images/KittySprite/Kitty_Sprite_Over_VioletShirt1_1.png",
            "K_BG_Over == 'violet shirt scarf'", "images/KittySprite/Kitty_Sprite_Over_VioletShirt2_1.png",                                                                  #Arms1               
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                         #necklace
            "K_BG_Neck == 'scarf'", "images/KittySprite/Kitty_Sprite_Shawl.png",
            "True", Null(),
            ),      
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head_BG",   
            ), 
        )
    anchor (0.6, 0.0)
    zoom .75                      

image Kitty_Head_BG:               
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "K_BG_Water and K_BG_Tan and K_BG_Blush == 1", "images/KittySprite/Kitty_Sprite_THead_Wet_Blush1.png",
            "K_BG_Water and K_BG_Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush1.png",
            "K_BG_Water and K_BG_Tan and K_BG_Blush == 2", "images/KittySprite/Kitty_Sprite_THead_Wet_Blush2.png",
            "K_BG_Water and K_BG_Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush2.png",
            "K_BG_Water and K_BG_Tan", "images/KittySprite/Kitty_Sprite_THead_Wet_Base.png",
            "K_BG_Water", "images/KittySprite/Kitty_Sprite_Head_Wet_Base.png",
            "K_BG_Blush == 1 and K_BG_Tan", "images/KittySprite/Kitty_Sprite_THead_Evo_Blush1.png",
            "K_BG_Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush1.png",
            "K_BG_Blush == 2 and K_BG_Tan", "images/KittySprite/Kitty_Sprite_THead_Evo_Blush2.png",
            "K_BG_Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush2.png",
            "True and K_BG_Tan", "images/KittySprite/Kitty_Sprite_THead_Evo_Base.png",
            "True", "images/KittySprite/Kitty_Sprite_Head_Evo_Base.png",
            ),     
        (0,0), ConditionSwitch(
            "K_BG_Brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "K_BG_Brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "K_BG_Brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "K_BG_Brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "K_BG_Brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "K_BG_Mouth == 'normal' and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Normal.png",
            "K_BG_Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "K_BG_Mouth == 'lipbite' and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Lipbite.png",
            "K_BG_Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Mouth_Lipbite.png",
            "K_BG_Mouth == 'kiss' and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Kiss.png",
            "K_BG_Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Mouth_Kiss.png",
            "K_BG_Mouth == 'sad' and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Sad.png",
            "K_BG_Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Mouth_Sad.png",
            "K_BG_Mouth == 'smile' and K_BG_Tan == 'tan3'", "images/KittySprite/Kitty_Sprite_TMouth_Smile.png",
            "K_BG_Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Mouth_Smile.png",
            "K_BG_Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Mouth_Surprised.png",
            "K_BG_Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "K_BG_Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png", #fix add
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            ),      
        (0,0), "Kitty Blink_BG",
        (0,0), ConditionSwitch(
            "K_BG_Blindfold", "images/KittySprite/Kitty_Sprite_Blindfold.png",  
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "K_BG_Water and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Wet.png",
            "K_BG_Water and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Wet.png",
            "K_BG_Water and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Wet.png",
            "K_BG_Water", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "K_BG_Hair == 'evo' and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Evo.png",
            "K_BG_Hair == 'evo' and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Evo.png",
            "K_BG_Hair == 'evo' and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Evo.png",
            "K_BG_Hair == 'evo'", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            "K_BG_Hair == 'long' and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Long.png",
            "K_BG_Hair == 'long' and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Long.png",
            "K_BG_Hair == 'long' and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Long.png",
            "K_BG_Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long.png",
            "K_BG_Hair == 'wet' and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Wet.png",
            "K_BG_Hair == 'wet' and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Wet.png",
            "K_BG_Hair == 'wet' and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Wet.png",
            "K_BG_Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "True and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Evo.png",
            "True and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Evo.png",
            "True and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Evo.png",
            "True", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            ),   
        (0,0), ConditionSwitch(
            "K_BG_Headband == 'pink'", "images/KittySprite/Kitty_Catband_Pink.png",
            "K_BG_Headband == 'black'", "images/KittySprite/Kitty_Catband_Black.png",
            "True", Null(),
            ),     
        (0,0), ConditionSwitch(
            "K_BG_Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),     
        )
    zoom .5

image Kitty_HairBack_BG:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(
            "(K_BG_Water or K_BG_Hair == 'wet') and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Wet_Back.png",
            "(K_BG_Water or K_BG_Hair == 'wet') and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Wet_Back.png",
            "(K_BG_Water or K_BG_Hair == 'wet') and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Wet_Back.png",
            "K_BG_Water or K_BG_Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
            "K_BG_Hair == 'long' and K_BG_HairColor == 'red'", "images/KittySprite/Kitty_Sprite_HairRed_Long_Back.png",
            "K_BG_Hair == 'long' and K_BG_HairColor == 'blonde'", "images/KittySprite/Kitty_Sprite_HairBlonde_Long_Back.png",
            "K_BG_Hair == 'long' and K_BG_HairColor == 'black'", "images/KittySprite/Kitty_Sprite_HairBlack_Long_Back.png",
            "K_BG_Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
            "True", Null(),
            ),    
        )
    zoom .5
    
image Kitty Blink_BG:
    ConditionSwitch( 
    "K_BG_Eyes == 'sexy'", "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png", 
    "K_BG_Eyes == 'side'", "images/KittySprite/Kitty_Sprite_Eyes_Side.png",  
    "K_BG_Eyes == 'surprised'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "K_BG_Eyes == 'manic'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",  
    "K_BG_Eyes == 'normal'", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",  
    "K_BG_Eyes == 'down'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "K_BG_Eyes == 'stunned'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",  
    "K_BG_Eyes == 'squint'", "Kitty_Squint_BG",  
    "K_BG_Eyes == 'closed'", "images/KittySprite/Kitty_Sprite_Eyes_Closed.png",    
    "True", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/KittySprite/Kitty_Sprite_Eyes_Closed.png"
    .25
    repeat 
    
image Kitty_Squint_BG:
    "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/KittySprite/Kitty_Sprite_Eyes_Squint.png"
    .25
    repeat  
# End Kitty Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Emma Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sprite_BG:
    LiveComposite(
        (402,965), 
        (0,0), ConditionSwitch(
            #hair back
            "renpy.showing('Emma_BJ_Animation') or not E_BG_Hair", Null(),
            "(E_BG_Hair == 'wet' or E_BG_Water) and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_HairbackWet_Red.png",
            "(E_BG_Hair == 'wet' or E_BG_Water) and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_HairbackWet_White.png",
            "(E_BG_Hair == 'wet' or E_BG_Water) and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_HairBlackbackWet.png",
            "E_BG_Hair == 'wet' or E_BG_Water", "images/EmmaSprite/EmmaSprite_HairbackWet.png",
            "E_BG_Hair and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Hairback_Red.png",   
            "E_BG_Hair and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Hairback_White.png",   
            "E_BG_Hair and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_HairBlackback.png",   
            "E_BG_Hair", "images/EmmaSprite/EmmaSprite_Hairback.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(
            #nighty underlayer 
            "E_BG_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png", 
            "E_BG_Over == 'black cape'", "images/EmmaSprite/EmmaSprite_LongCape_Back_Black.png",   
            "E_BG_Over == 'cape'", "images/EmmaSprite/EmmaSprite_LongCape_Back.png",   
            "True", Null(),        
            ),
        (0,0), ConditionSwitch(
            #panties down back
            "not E_BG_Panties or not E_BG_PantiesDown or (E_BG_Legs == 'pants' and not E_BG_Upskirt)", Null(),
            "E_BG_Panties == 'black panties'", "images/EmmaSprite/EmmaSprite_Panties_DownBack_Black.png",   
            "E_BG_Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownBack.png",   
            "E_BG_Panties == 'white panties'", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png",   
            "E_BG_Panties == 'bikini'", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(
            #legs/torso
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Legs_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Legs_Arms1.png", #if E_BG_Arms == 1         
            ),     
        (0,0), ConditionSwitch(
            #pubes 
            "E_BG_Pubes", "images/EmmaSprite/EmmaSprite_Pubes.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(
            #nude lower piercings        
            "not E_BG_Pierce", Null(),  
            "E_BG_Panties and not E_BG_PantiesDown", Null(), 
            "E_BG_Legs != 'skirt' and E_BG_Legs and not E_BG_Upskirt", Null(), #skirt if wearing a skirt
            "E_BG_Pierce == 'ring'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Ring.png",   
            "E_BG_Pierce == 'barbell'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Barbell.png",   
            "True", Null(),        
            ),     
        (0,0), ConditionSwitch(
            #Water effect 
            "E_BG_Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",   
            "True", Null(),        
            ),  
        (0,0), ConditionSwitch(
            #boots
            "not E_BG_Hose", Null(),
            "E_BG_Hose == 'boots'", "images/EmmaSprite/EmmaSprite_Boots.png", 
            "E_BG_Hose == 'white thigh high'", "images/EmmaSprite/Emma_Sprite_ThighHighsWhite.png", 
            "E_BG_Hose == 'black thigh high'", "images/EmmaSprite/Emma_Sprite_ThighHighsBlack.png", 
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(
            #panties down if not wearing pants
            "not E_BG_Panties or not E_BG_PantiesDown or (E_BG_Legs == 'pants' and not E_BG_Upskirt)", Null(), 
            "E_BG_Panties == 'black panties'", "images/EmmaSprite/EmmaSprite_Panties_Down_Black.png",  
            "E_BG_Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_Down.png",  
            "E_BG_Panties == 'white panties'", "images/EmmaSprite/EmmaSprite_Panties_Down.png",
            "E_BG_Panties == 'lace panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace_Down.png",
            "E_BG_Panties == 'bikini'", "images/EmmaSprite/EmmaSprite_Panties_Down.png",
            "True", Null(),        
            ),   
        (0,0), ConditionSwitch(
            #panties up
            "E_BG_PantiesDown or not E_BG_Panties", Null(),  
            "E_BG_Panties == 'black panties'", "images/EmmaSprite/EmmaSprite_Panties_Black.png",  
            "E_BG_Panties == 'sports panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports.png",  
            "E_BG_Panties == 'white panties'", "images/EmmaSprite/EmmaSprite_Panties.png",
            "E_BG_Panties == 'lace panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace.png",
            "E_BG_Panties == 'bikini'", "images/EmmaSprite/EmmaSprite_BikiniBottom.png",  
            "True", Null(),        
            ),
        (0,0), ConditionSwitch(
            #pants    
            "not E_BG_Legs", Null(),
            "E_BG_Upskirt", ConditionSwitch(                   
                    #if the skirt's up or pants down 
                    "E_BG_Legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png",
                    "E_BG_Legs == 'NewX'", "images/EmmaSprite/EmmaSprite_Pants_NewX_unzip.png", 
                    "E_BG_Legs == 'NewX black'", "images/EmmaSprite/EmmaSprite_Pants_NewXBlack_unzip.png",
                    "True", Null(),
                    ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "E_BG_Wet", ConditionSwitch(   
                        #if she's not wet
                        "E_BG_Legs == 'pants' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants.png",
                        "E_BG_Legs == 'black pants' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_Black.png",
                        "E_BG_Legs == 'yoga pants' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_Yoga.png",
                        "E_BG_Legs == 'red sports shorts' and not E_BG_Upskirt", "images/EmmaSprite/Emma_Sprite_ShortsRed.png",
                        "E_BG_Legs == 'white sports shorts' and not E_BG_Upskirt", "images/EmmaSprite/Emma_Sprite_ShortsWhite.png",
                        "E_BG_Legs == 'NewX' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_NewX.png", 
                        "E_BG_Legs == 'NewX black' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_NewXBlack.png", 
                        "E_BG_Legs == 'skirt' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Skirt.png", 
                        ),
                    "True", ConditionSwitch(   
                        #if she's wet
                        "E_BG_Legs == 'pants' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_PantsWet.png",
                        "E_BG_Legs == 'black pants' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_BlackWet.png",
                        "E_BG_Legs == 'yoga pants' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_YogaWet.png",
                        "E_BG_Legs == 'red sports shorts' and not E_BG_Upskirt", "images/EmmaSprite/Emma_Sprite_ShortsRedWet.png",
                        "E_BG_Legs == 'white sports shorts' and not E_BG_Upskirt", "images/EmmaSprite/Emma_Sprite_ShortsWhiteWet.png",
                        "E_BG_Legs == 'NewX' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_NewXWet.png", 
                        "E_BG_Legs == 'NewX black' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Pants_NewXBlackWet.png", 
                        "E_BG_Legs == 'skirt' and not E_BG_Upskirt", "images/EmmaSprite/EmmaSprite_Skirt.png",
                        ),                    
                    ),    
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness            
            "E_BG_Legs or not E_BG_Wet", Null(),
            #"E_BG_Panties == 'naked pool'", Null(),
            "E_BG_Panties and E_BG_Panties != 'naked pool' and not E_BG_PantiesDown and E_BG_Wet < 2", Null(),
            "E_BG_Panties and E_BG_Panties != 'naked pool' and not E_BG_PantiesDown", "images/EmmaSprite/EmmaSprite_Wet1.png",
            "E_BG_Wet == 2", "images/EmmaSprite/EmmaSprite_Wet2.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet1.png",
            ),     
        (0,0), ConditionSwitch(
            #Chest underlayer
            "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_CorsetUnder_Black.png",   
            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetUnder.png",   
            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports_Under.png",   
            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Under.png", 
            "E_BG_Chest == 'NewX'", "images/EmmaSprite/EmmaSprite_CorsetUnder_NewX.png",   
            "E_BG_Chest == 'NewX black'", "images/EmmaSprite/EmmaSprite_CorsetUnder_NewXBlack.png",   
            "True", Null(),              
            ), 
        (0,0), ConditionSwitch(
            #Towel underlayer
            "E_BG_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png", 
            "E_BG_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Under.png",   
            "True", Null(),              
            ),
        (0,0), ConditionSwitch(
            #arms 
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Arms2.png",         # one hand up
            "True", "images/EmmaSprite/EmmaSprite_Arms1.png", #if E_BG_Arms == 1   # Crossed        
            ),  
        (0,0), ConditionSwitch(
            #Water effect on arms
            "not E_BG_Water", Null(),             
            "Emma_Arms == 2", "images/EmmaSprite/EmmaSprite_Water_Arms2.png",   
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms1.png", #if E_BG_Arms == 1      
            ), 
        (0,0), ConditionSwitch(
            #gloves 
            "not E_BG_Arms", Null(),  
            "Emma_Arms == 2 and E_BG_Arms == 'black gloves'", "images/EmmaSprite/EmmaSprite_Gloves_Arms2_Black.png",   
            "E_BG_Arms == 'black gloves'", "images/EmmaSprite/EmmaSprite_Gloves_Arms1_Black.png", #if E_BG_Arms == 1         
            "Emma_Arms == 2 and E_BG_Arms == 'white gloves'", "images/EmmaSprite/EmmaSprite_Gloves_Arms2.png",   
            "E_BG_Arms == 'white gloves'", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png",   
            "True", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png", #if E_BG_Arms == 1         
            ),   
        (0,0), ConditionSwitch(
            #tits      
            "Emma_Arms == 1 or E_BG_Chest == 'corset' or E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_BG_TitsUp = 1
            "E_BG_Chest == 'sports bra' or E_BG_Chest == 'red sports bra' or E_BG_Chest == 'white sports bra' or E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_TitsUp.png",   # E_BG_TitsUp = 1
            "True", "images/EmmaSprite/EmmaSprite_TitsDown.png",   # E_BG_TitsUp = 0
            ), 
        (0,0), ConditionSwitch(
            #nude peircings      
            #something about this entry makes all subsequent entries mis-aligned
            "not E_BG_Pierce", Null(),  
            "E_BG_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",                     
                    "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Barbell.png",        
                    ),                        
            "E_BG_Pierce == 'ring'", ConditionSwitch(                      
                    #if it's the ring pericings                                 
                    "Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png", 
                    "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Ring.png", 
                    ),       
            "True", Null(),  
            ),
        (0,0), ConditionSwitch(
            #Water effect 
            "not E_BG_Water", Null(),             
            "Emma_Arms == 1 or E_BG_Chest == 'corset' or E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",  
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png", #if E_BG_Arms == 1      
            ), 
        (0,0), ConditionSwitch(
            #Chest layer
            "not E_BG_Chest", Null(),
            "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/Emma_Sprite_Sportsbra_Red.png",   
            "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/Emma_Sprite_Sportsbra_White.png",   
            "E_BG_Chest == 'black corset' and E_BG_Over", "images/EmmaSprite/EmmaSprite_CorsetTitsX_Black.png",   
            "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_CorsetTits_Black.png",   
            "E_BG_Chest == 'corset' and E_BG_Over", "images/EmmaSprite/EmmaSprite_CorsetTitsX.png",   
            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits.png",  
            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports.png",   
            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace.png",   
            "E_BG_Chest == 'NewX' and Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_CorsetTits_NewX_Up.png",   
            "E_BG_Chest == 'NewX black' and Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_CorsetTits_NewXBlack_Up.png",   
            "E_BG_Chest == 'bikini' and Emma_Arms == 1", "images/EmmaSprite/EmmaSprite_BikiniTits_Up.png",   
            "E_BG_Chest == 'NewX' and Emma_Arms > 1", "images/EmmaSprite/EmmaSprite_CorsetTits_NewX_Down.png",   
            "E_BG_Chest == 'NewX black' and Emma_Arms > 1", "images/EmmaSprite/EmmaSprite_CorsetTits_NewXBlack_Down.png",   
            "E_BG_Chest == 'bikini' and Emma_Arms > 1", "images/EmmaSprite/EmmaSprite_BikiniTits_Down.png",   
            "True", Null(),              
            ),
        (0,0), ConditionSwitch(
            #cape layer       
            "E_BG_Over or (E_BG_Chest != 'corset' and E_BG_Chest != 'black corset')", Null(),  
            "Emma_Arms == 2 and E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Cape2.png",              
            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Cape1.png", 
            "Emma_Arms == 2 and E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_Cape2_Black.png",              
            "True", "images/EmmaSprite/EmmaSprite_Cape1_Black.png",
            ), 
        (0,0), ConditionSwitch(
            #neck
            "E_BG_Neck == 'black choker'", "images/EmmaSprite/EmmaSprite_Neck_Choker_Black.png",       
            "E_BG_Neck == 'choker'", "images/EmmaSprite/EmmaSprite_Neck_Choker.png",       
            "E_BG_Neck == 'NewX'", "images/EmmaSprite/EmmaSprite_Neck_NewX.png",       
            "E_BG_Neck == 'NewX black'", "images/EmmaSprite/EmmaSprite_Neck_NewXBlack.png",       
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #Overshirt layer
            "not E_BG_Over", Null(),
            "Emma_Arms == 2", ConditionSwitch(
                    #if her arms are down, allowing her breasts to sink
                    "E_BG_Over == 'jacket'", ConditionSwitch(
                            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'NewX'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'NewX black'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",    
                            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'bikini'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "True", "images/EmmaSprite/EmmaSprite_Jacket_2Down.png",
                            ),
                    "E_BG_Over == 'black jacket'", ConditionSwitch(
                            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Black.png",
                            "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Black.png",
                            "E_BG_Chest == 'NewX'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Black.png",
                            "E_BG_Chest == 'NewX black'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Black.png",
                            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",    
                            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "E_BG_Chest == 'bikini'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "True", "images/EmmaSprite/EmmaSprite_Jacket_2Down_Black.png",
                            ),
                    "E_BG_Over == 'cape'", ConditionSwitch(
                            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'NewX'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'NewX black'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",    
                            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "E_BG_Chest == 'bikini'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
                            "True", "images/EmmaSprite/EmmaSprite_LongCape_TitsDown.png",
                            ),
                    "E_BG_Over == 'black cape'", ConditionSwitch(
                            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'black corset'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'NewX'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'NewX black'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",    
                            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'white sports bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'red sports bra'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "E_BG_Chest == 'bikini'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
                            "True", "images/EmmaSprite/EmmaSprite_LongCape_TitsDown_Black.png",
                            ),
                    "E_BG_Over == 'nighty'", ConditionSwitch(
                            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png",
                            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png",    
                            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png",  
                            "True", "images/EmmaSprite/EmmaSprite_Nighty_2Down.png",
                            ),
                    "E_BG_Over == 'towel'", ConditionSwitch(
                            "E_BG_Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",
                            "E_BG_Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",
                            "E_BG_Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",
                            "True", "images/EmmaSprite/EmmaSprite_Towel_Down2.png",
                            ),
                    "True", Null(),
                    ),
            #if her arms are up, preventng her breasts from sinking
            "E_BG_Over == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up.png",
            "E_BG_Over == 'black jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up_Black.png",
            "E_BG_Over == 'cape'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp.png",
            "E_BG_Over == 'black cape'", "images/EmmaSprite/EmmaSprite_LongCape_TitsUp_Black.png",
            "E_BG_Over == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_1Up.png",      
            "E_BG_Over == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up1.png",               
            "True", Null(), 
            ),
        (55,0), "EmmaSprite_Head_BG",  #Head
        )
    anchor (0.6, 0.0)                
    zoom .75                

image EmmaSprite_Head_BG:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(
            #Face no blush not wet
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Blush or E_BG_Hair == 'wet' or E_BG_Water", Null(),        
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",     
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png", #E_BG_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(
            #Face blush 1 not wet
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Blush != 1 or E_BG_Hair == 'wet' or E_BG_Water", Null(),        
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",   
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png", #E_BG_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(
            #Face blush 2 not wet
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Blush != 2 or E_BG_Hair == 'wet' or E_BG_Water", Null(),        
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",    
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png", 
            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png", #E_BG_Brows == 'normal'
            ),
        
         (0,0), ConditionSwitch(
            #Face no blush wet
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Blush or (E_BG_Hair != 'wet' and not E_BG_Water)", Null(),        
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",    
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",  
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png", #E_BG_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(
            #Face blush 1 wet
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Blush != 1 or (E_BG_Hair != 'wet' and not E_BG_Water)", Null(),        
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",    
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png", #E_BG_Brows == 'normal'
            ),
        (0,0), ConditionSwitch(
            #Face blush 2 wet
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Blush != 2 or (E_BG_Hair != 'wet' and not E_BG_Water)", Null(),        
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",    
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",    
            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png", #E_BG_Brows == 'normal'
            ),
        
        (0,0), ConditionSwitch(
            #Mouths        
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "E_BG_Mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "E_BG_Mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "E_BG_Mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_BG_Mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "E_BG_Mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "E_BG_Mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "E_BG_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",            
            "E_BG_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",                
            "E_BG_Mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",                 
            "E_BG_Mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",         
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),   
        (0,0), "Emma Blink_BG", #Eyes        
        (0,0), ConditionSwitch(                                                                         #brows
            "renpy.showing('Emma_BJ_Animation')", Null(),
            #"E_BG_Brows == 'normal' and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"E_BG_Brows == 'normal' and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "E_BG_Brows == 'normal' and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "E_BG_Brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            #"E_BG_Brows == 'angry' and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_White.png",
            #"E_BG_Brows == 'angry' and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry_Red.png",
            "E_BG_Brows == 'angry' and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Angry.png",
            "E_BG_Brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            #"E_BG_Brows == 'sad' and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_White.png",
            #"E_BG_Brows == 'sad' and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad_Red.png",
            "E_BG_Brows == 'sad' and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Sad.png",
            "E_BG_Brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            #"E_BG_Brows == 'surprised' and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_White.png",        
            #"E_BG_Brows == 'surprised' and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised_Red.png",        
            "E_BG_Brows == 'surprised' and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Surprised.png",        
            "E_BG_Brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",        
            #"E_BG_Brows == 'confused' and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_White.png",
            #"E_BG_Brows == 'confused' and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused_Red.png",
            "E_BG_Brows == 'confused' and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Confused.png",
            "E_BG_Brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            #"True and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_White.png",
            #"True and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal_Red.png",
            "True and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_BrowsBlack_Normal.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),         
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "not E_BG_Hair", Null(),
            "(E_BG_Hair == 'wet' or E_BG_Water) and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_HairWet_White.png",
            "(E_BG_Hair == 'wet' or E_BG_Water) and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_HairWet_Red.png",
            "(E_BG_Hair == 'wet' or E_BG_Water) and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlackWet.png",
            "E_BG_Hair == 'wet' or E_BG_Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "E_BG_Hair and E_BG_HairColor == 'white'", "images/EmmaSprite/EmmaSprite_Head_Hair_White.png",
            "E_BG_Hair and E_BG_HairColor == 'red'", "images/EmmaSprite/EmmaSprite_Head_Hair_Red.png",
            "E_BG_Hair and E_BG_HairColor == 'black'", "images/EmmaSprite/EmmaSprite_Head_HairBlack.png",
            "E_BG_Hair", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(                                                                         #Hair Water
            "renpy.showing('Emma_BJ_Animation')", Null(),
            "not E_BG_Water", Null(),
            "E_BG_Hair == 'wet'", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            ),
        )
    anchor (0.6, 0.0)                
    zoom .5   

image Emma Blink_BG:
    ConditionSwitch(
    "E_BG_Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
    "E_BG_Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
    "E_BG_Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_BG_Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
    "E_BG_Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
    "E_BG_Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
    "E_BG_Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
    "E_BG_Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_BG_Eyes == 'squint'", "Emma_Squint_BG",
    "True", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png"
    .25
    repeat                

image Emma_Squint_BG:
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Squint.png"
    .25
    repeat 
# End Emma Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


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
    default L_BG_PantiesDown = 0
    default L_BG_Upskirt = 0
    default L_BG_Claws = 1

    default L_BG_Girl_Arms = 2
    default L_BG_Wet = 0
    default L_BG_Blush = 1
    default L_BG_Brows = 0
    default L_BG_Eyes = 0
    default L_BG_Mouth = 0
    default L_BG_Water = 0


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
    default K_BG_Headband = "pink"
    default K_BG_Tan = "tan"
    default K_BG_Gloves = "black gloves"
    default K_BG_DynamicTan = [0,0,0,0,0]
    default K_BG_BodySuit = 0
    default K_BG_Upskirt = 0
    default K_BG_PantiesDown = 0
    default K_BG_Brows = 0
    default K_BG_Eyes = 0
    default K_BG_Mouth = 0
    default K_BG_Gag = 0
    default K_BG_Blindfold = 0

    default K_BG_Girl_Arms = 2
    default K_BG_Wet = 0
    default K_BG_Blush = 1
    default K_BG_Water = 0

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
    default E_BG_BodySuit = 0
    default E_BG_Upskirt = 0
    default E_BG_PantiesDown = 0
    default E_BG_Brows = 0
    default E_BG_Eyes = 0
    default E_BG_Mouth = 0
    default E_BG_Gag = 0
    default E_BG_Blindfold = 0

    default E_BG_Girl_Arms = 2
    default E_BG_Wet = 0
    default E_BG_Blush = 1
    default E_BG_Water = 0
