# Basic character Sprites
image Rogue:
    LiveComposite(
        (480,960),
        (0,0), ConditionSwitch(                                                                         #Overhsirt backing
            "R_Over == 'mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh1.png",
            "R_Over == 'mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_mesh2.png",
            "R_Over == 'white mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_whitemesh1.png",
            "R_Over == 'white mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_whitemesh2.png",
            "R_Over == 'blue mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_bluemesh2.png",
            "R_Over == 'red mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_redmesh1.png",
            "R_Over == 'red mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_redmesh2.png",
            "R_Over == 'yellow mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_yellowmesh1.png",
            "R_Over == 'yellow mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_yellowmesh2.png",
            "R_Over == 'black mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_blackmesh1.png",
            "R_Over == 'black mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_blackmesh2.png",  
            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
            "R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodieB.png",
            "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodieB.png",
            "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodieB.png",
            "R_Over == 'black hoodie'", "images/RogueSprite/Rogue_over_dhoodieB.png",
            "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodieB.png",
            "R_Over == 'SR7 mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh_SR7_1.png",
            "R_Over == 'SR7 mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_mesh_SR7_2.png",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(                                                                         #body 
            "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1body_bare.png",
            "R_Tan == 'tan'", "images/RogueSprite/Rogue_tbody_bare.png",
            "True", "images/RogueSprite/Rogue_body_bare.png",         
            ),  
        (0,0), ConditionSwitch(                                                                         #body 
            "R_Pubes and (R_HairColor == 'black' or R_HairColor == 'blackwhite')", "images/RogueSprite/Rogue_bodyhaired_pubesblack.png",
            "R_Pubes and (R_HairColor == 'blonde' or R_HairColor == 'blondewhite')", "images/RogueSprite/Rogue_bodyhaired_pubesblonde.png",
            #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            #"R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
            #"R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
            "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_pubes.png",   
            "True", Null(),         
            ),  
        (0,0), ConditionSwitch(                                                                         #body 
            #"R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_piercing_ring.png",            
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_piercing_barbell.png",
            #"R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", Null(),         
            ),   
        #(0,0), ConditionSwitch(                                                                         #body 
        #    "R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
        #    "R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
        #    "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
        #    "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
        #    "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
        #    "True", "images/RogueSprite/Rogue_body_bare.png",         
        #    ),              
        (0,0), ConditionSwitch(                                                                         #head 
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Tan and R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_thead_evowet.png",
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_Tan and R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2.png",
            "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_Tan and R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_thead_evo_blush.png",
            "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_Tan and R_Hair == 'evo'", "images/RogueSprite/Rogue_thead_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "R_Tan", "images/RogueSprite/Rogue_thead_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #pants backing/hose    
            "R_Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
            "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #Panties            
            "not R_Panties", Null(),
            # "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", Null(),
            "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",             
            "R_Panties == 'shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
            "R_Panties == 'red shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_down_wet.png",
            "R_Panties == 'blue shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_down_wet.png",
            "R_Panties == 'shorts' and R_PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",
            "R_Panties == 'red shorts' and R_PantiesDown", "images/RogueSprite/Rogue_ryshorts_down.png",
            "R_Panties == 'blue shorts' and R_PantiesDown", "images/RogueSprite/Rogue_byshorts_down.png",  
            "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",
            "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_wet.png",
            "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_wet.png",          
            "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
            "R_Panties == 'red shorts'", "images/RogueSprite/Rogue_ryshorts.png",
            "R_Panties == 'blue shorts'", "images/RogueSprite/Rogue_byshorts.png",
            "R_Panties == 'green panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
            "R_Panties == 'green panties' and R_PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
            "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
            "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
            "R_Panties == 'black large panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_down_wet.png",
            "R_Panties == 'black large panties' and R_PantiesDown", "images/RogueSprite/Rogue_undiesBlack_down.png",  
            "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_wet.png",          
            "R_Panties == 'black large panties'", "images/RogueSprite/Rogue_undiesBlack.png",
            "R_Panties == 'lace panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            "R_Panties == 'black panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
            "True", "images/RogueSprite/Rogue_panties.png",            
            ),
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "R_Tan and Rogue_Arms == 1 and R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms1a_gloved.png",       #Gloves and collar 
            "Rogue_Arms == 1 and R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",       #Gloves and collar 
            "R_Tan and Rogue_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_tarms1b_gloved.png",                                     #Gloves, no collar
            "Rogue_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "R_Tan and Rogue_Arms == 1 and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms1a_bare.png",                                #No Gloves, collar 
            "Rogue_Arms == 1 and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_bare.png",                                #No Gloves, collar 
            "R_Tan and Rogue_Arms == 1", "images/RogueSprite/Rogue_tarms1b_bare.png",                                                              #No gloves, no collar
            "Rogue_Arms == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "R_Tan and R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_gloved.png",                           #Gloves and collar 
            "R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",                           #Gloves and collar 
            "R_Tan and R_Arms == 'gloved'", "images/RogueSprite/Rogue_tarms2b_gloved.png",                                                         #Gloved, no collar
            "R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved.png",                                                         #Gloved, no collar
            "R_Tan and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_bare.png",                                                    #No gloves, collar
            "R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare.png",                                                    #No gloves, collar
            "R_Tan", "images/RogueSprite/Rogue_tarms2b_bare.png",                                                                         #No gloves, no collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",                                                                         #No gloves, no collar
#            "Rogue_Arms == 1 and R_Arms == 'collargloved'", "images/RogueSprite/Rogue_arms1a_gloved.png",  
#            "Rogue_Arms == 1 and R_Arms == 'collarbare'", "images/RogueSprite/Rogue_arms1a_bare.png", 
#            "Rogue_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                   
#            "Rogue_Arms == 1", "images/RogueSprite/Rogue_arms1b_bare.png",
#            "R_Arms == 'collargloved'", "images/RogueSprite/Rogue_arms2a_gloved.png", 
#            "R_Arms == 'collarbare'", "images/RogueSprite/Rogue_arms2a_bare.png", 
#            "R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved.png",
#            "True", "images/RogueSprite/Rogue_arms2b_bare.png",          
            ), 
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "Rogue_Arms == 1 and R_Arms == 'classic gloves'", "images/RogueSprite/Rogue_Sprite_XGloves1.png",                                     #Gloves, no collar
            "R_Arms == 'classic gloves'", "images/RogueSprite/Rogue_Sprite_XGloves2.png",                                                         #Gloved, no collar
            "True", Null(),                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(                                                                         #chest layer
            "R_Tan == 'tan1' and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_t1chest_barbell.png",            
            "R_Tan == 'tan' and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_tchest_barbell.png",            
            "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            "R_Tan == 'tan1' and R_Pierce == 'ring'", "images/RogueSprite/Rogue_t1chest_rings.png",      
            "R_Tan == 'tan' and R_Pierce == 'ring'", "images/RogueSprite/Rogue_tchest_rings.png",      
            "R_Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1chest_bare.png",     
            "R_Tan == 'tan'", "images/RogueSprite/Rogue_tchest_bare.png",     
            "True", "images/RogueSprite/Rogue_chest_bare.png",     
            ),   
        (0,0), ConditionSwitch(                                                                         #chest clothes layer
            "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
            "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
            "R_Chest == 'blue sports bra'", "images/RogueSprite/Rogue_chest_bysportsbra.png",
            "R_Chest == 'red sports bra'", "images/RogueSprite/Rogue_chest_rysportsbra.png",
            "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
            "R_Chest == 'SR7 tank short'", "images/RogueSprite/Rogue_chest_tankshort_SR7.png",
            "R_Chest == 'tank short'", "images/RogueSprite/Rogue_chest_tankshort.png",
            "R_Chest == 'slut tank short'", "images/RogueSprite/Rogue_chest_tankshort_slut.png",
            "R_Chest == 'tape'", "images/RogueSprite/Rogue_chest_tape.png",
            "R_BodySuit and not R_BodySuitOff", Null(),
            "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            "Rogue_Arms == 1 and R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            "R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            "Rogue_Arms == 1 and R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            "R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            "R_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(  
            "R_Chest == 'swimsuit1' or R_Panties == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1.png",
            "R_Chest == 'swimsuit2' or R_Panties == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(  
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),
            "R_BodySuit == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1.png",
            "R_BodySuit == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2.png",
            "Rogue_Arms == 1 and R_BodySuit == 'classic uniform' and R_Wet", "images/RogueSprite/Rogue_Sprite_XCatsuit1_wet.png",
            "Rogue_Arms == 1 and R_BodySuit == 'classic uniform'", "images/RogueSprite/Rogue_Sprite_XCatsuit1.png",
            "R_BodySuit == 'classic uniform' and R_Wet", "images/RogueSprite/Rogue_Sprite_XCatsuit2_wet.png",
            "R_BodySuit == 'classic uniform'", "images/RogueSprite/Rogue_Sprite_XCatsuit2.png",
            "Rogue_Arms == 1 and R_BodySuit == 'classic uniform damaged'", "images/RogueSprite/Rogue_Sprite_XCatsuit1_Dmg.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSprite/Rogue_Sprite_XCatsuit2_Dmg.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                         #chest clothes layer
            "not R_BodySuit or R_BodySuitOff", Null(),
            "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            "Rogue_Arms == 1 and R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            "R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            "Rogue_Arms == 1 and R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            "R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            #"R_Chest == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1_Top.png",
            #"R_Chest == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2_Top.png",
            "R_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                         #full hose/tights              
            "R_PantiesDown", Null(), 
            "R_Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",                  
            "R_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            "R_Hose == 'SR7 hose'", "images/RogueSprite/Rogue_hose_SR7.png",       
            "R_Hose == 'fishnet'", "images/RogueSprite/Rogue_hose_fishnet.png",       
            "R_Hose == 'tights' and R_Wet", "images/RogueSprite/Rogue_tights_wet.png",
            "R_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "R_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #Personal Wetness            
            "not R_Wet", Null(),
            "R_Legs and R_Wet <= 1", Null(),
            "R_Legs", "images/RogueSprite/Rogue_wet.png",
            "R_Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",       #R_Wet >1
            ),              
        (0,0), ConditionSwitch(                                                                         #brows
            "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "R_Brows == 'normal'", "images/RogueSprite/Rogue_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueSprite/Rogue_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueSprite/Rogue_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueSprite/Rogue_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueSprite/Rogue_brows_confused.png",
            "True", "images/RogueSprite/Rogue_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(                                                                         #Blush
#            "R_Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), ConditionSwitch(  
            "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",                                                                       #Mouths        
            "R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                       #Mouths        
            "R_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                       #Mouths        
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue_w.png",
            "R_Tan and 'mouth' in R_Spunk", "images/RogueSprite/Rogue_tmouth_lipbite_w.png",
            "'mouth' in R_Spunk", "images/RogueSprite/Rogue_mouth_lipbite_w.png",
            "R_Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "R_Tan and R_Mouth == 'lipbite'", "images/RogueSprite/Rogue_tmouth_lipbite.png",
            "R_Mouth == 'lipbite'", "images/RogueSprite/Rogue_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking.png",            
            "R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_surprised.png",            
            "R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue.png",                
            "R_Mouth == 'grimace'", "images/RogueSprite/Rogue_mouth_grimace.png",           
            "True", "images/RogueSprite/Rogue_mouth_normal.png",
            ),            
        (0,0), "Rogue Blink",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ), 
        (0,0), ConditionSwitch(                                                                      
            "R_Headband", "images/RogueSprite/Rogue_Sprite_XHeadband.png",   
            "True", Null(),
            ),                                                                           
            
        (0,0), ConditionSwitch(                                                                         #Pants and Skirts
            "R_Boots == 'boots' and R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_boots_down.png", 
            "R_Boots == 'boots' and R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants_boots.png", 
            "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            "R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            "R_Legs == 'skirt' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "R_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            "R_Legs == 'skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_up.png",
            "R_Legs == 'skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort.png", 
            "R_Legs == 'SR7 skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_SR7_up.png",
            "R_Legs == 'SR7 skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort_SR7.png",  
            #"R_Legs == 'skirtshort'", AlphaMask("images/RogueSprite/Rogue_legs_skirtshort.png", "images/RogueSprite/Rogue_legs_skirtshort_alphamask.png"),
            "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Up.png",
            "R_Legs == 'cheerleader skirt'", "images/RogueSprite/Rogue_Cheerleader_Skirt.png",
            "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short_Up.png",            
            "R_Legs == 'cheerleader skirtshort'", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short.png",
            "True", Null(),   
            ),
        (0,0), ConditionSwitch(                                                                         
            "R_Boots == 'boots'", "images/RogueSprite/Rogue_Highshoes.png",
            "R_Boots == 'classic boots'", "images/RogueSprite/Rogue_Sprite_XShoes.png",
            "True", Null(),  
            ), 

        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "Rogue_Arms == 1", Null(),                                                              #No gloves, no collar
            "R_Tan and R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_gloved_.png",                           #Gloves and collar 
            "R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved_.png",                           #Gloves and collar 
            "R_Tan and R_Arms == 'gloved'", "images/RogueSprite/Rogue_tarms2b_gloved_.png",                                                         #Gloved, no collar
            "R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved_.png",                                                         #Gloved, no collar
            "R_Tan and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_tarms2a_bare_.png",                                                    #No gloves, collar
            "R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare_.png",                                                    #No gloves, collar
            "R_Tan", "images/RogueSprite/Rogue_tarms2b_bare_.png",                                                                         #No gloves, no collar
            "True", "images/RogueSprite/Rogue_arms2b_bare_.png",  
            ), 
        
        (0,0), ConditionSwitch(                                                                         #Arms and gloves
            "Rogue_Arms == 1", Null(),                                                             
            "R_BodySuitOff", Null(),
            "R_BodySuit == 'classic uniform' or R_BodySuit == 'classic uniform damaged'", "images/RogueSprite/Rogue_Sprite_XCatsuit2_.png",
            "True", Null(),
            ),                 
        (0,0), ConditionSwitch(                                                                         #water
            "R_Water and Rogue_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "R_Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         #soap
            "R_Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),                 
            ),
        (0,0), ConditionSwitch(                                                                         #accessories
            "R_Accessory == 'classic belt' and Rogue_Arms == 1", "images/RogueSprite/Rogue_Sprite_Over_XBelt1.png",
            "R_Accessory == 'classic belt'", "images/RogueSprite/Rogue_Sprite_Over_XBelt2.png",
            "True", Null(),
            ),  
        
        (0,0), ConditionSwitch(                                                                         #Overshirt layer
            "Rogue_Arms == 1 and R_Over == 'SR7 mesh top'", "images/RogueSprite/Rogue_over_mesh_SR7_1.png",
            "Rogue_Arms == 1 and R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",
            "Rogue_Arms == 1 and R_Over == 'white mesh top'", "images/RogueSprite/Rogue_over_whitemesh1.png",
            "Rogue_Arms == 1 and R_Over == 'blue mesh top'", "images/RogueSprite/Rogue_over_bluemesh1.png",
            "Rogue_Arms == 1 and R_Over == 'red mesh top'", "images/RogueSprite/Rogue_over_redmesh1.png",
            "Rogue_Arms == 1 and R_Over == 'yellow mesh top'", "images/RogueSprite/Rogue_over_yellowmesh1.png",
            "Rogue_Arms == 1 and R_Over == 'black mesh top'", "images/RogueSprite/Rogue_over_blackmesh1.png",           
            "Rogue_Arms == 1 and R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
            "Rogue_Arms == 1 and R_Over == 'red top'", "images/RogueSprite/Rogue_over_red1.png",
            "Rogue_Arms == 1 and R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
            "Rogue_Arms == 1 and R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
            "Rogue_Arms == 1 and R_Over == 'classic jacket'", "images/RogueSprite/Rogue_Sprite_Over_XJacket1.png",
            "Rogue_Arms == 1 and R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
            "Rogue_Arms == 1 and R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodie1.png",
            "Rogue_Arms == 1 and R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie1.png",
            "Rogue_Arms == 1 and R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie1.png",
            "Rogue_Arms == 1 and R_Over == 'black hoodie'", "images/RogueSprite/Rogue_over_dhoodie1.png",
            "Rogue_Arms == 1 and R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie1.png",
            "Rogue_Arms == 1 and R_Over == 'red dress' and R_Upskirt", "images/RogueSprite/Rogue_reddress_up_1.png",
            "Rogue_Arms == 1 and R_Over == 'red dress'", "images/RogueSprite/Rogue_reddress_1.png",
            "Rogue_Arms == 1 and R_Over == 'blue dress' and R_Upskirt", "images/RogueSprite/Rogue_bluedress_up_1.png",
            "Rogue_Arms == 1 and R_Over == 'blue dress'", "images/RogueSprite/Rogue_bluedress_1.png",
            "R_Over == 'SR7 mesh top'", "images/RogueSprite/Rogue_over_mesh_SR7_2.png",
            "R_Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png",
            "R_Over == 'white mesh top'", "images/RogueSprite/Rogue_over_whitemesh2.png",
            "R_Over == 'blue mesh top'", "images/RogueSprite/Rogue_over_bluemesh2.png",
            "R_Over == 'red mesh top'", "images/RogueSprite/Rogue_over_redmesh2.png",
            "R_Over == 'yellow mesh top'", "images/RogueSprite/Rogue_over_yellowmesh2.png",
            "R_Over == 'black mesh top'", "images/RogueSprite/Rogue_over_blackmesh2.png", 
            "R_Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
            "R_Over == 'red top'", "images/RogueSprite/Rogue_over_red2.png",
            "R_Over == 'classic jacket'", "images/RogueSprite/Rogue_Sprite_Over_XJacket2.png",
            "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
            "R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodie2.png",
            "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie2.png",
            "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie2.png",
            "R_Over == 'black hoodie'", "images/RogueSprite/Rogue_over_dhoodie2.png",
            "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie2.png",
            "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
            "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",  
            "R_Over == 'red dress' and R_Upskirt", "images/RogueSprite/Rogue_reddress_up_2.png",
            "R_Over == 'red dress'", "images/RogueSprite/Rogue_reddress_2.png",
            "R_Over == 'blue dress' and R_Upskirt", "images/RogueSprite/Rogue_bluedress_up_2.png",            
            "R_Over == 'blue dress'", "images/RogueSprite/Rogue_bluedress_2.png",            
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(                                                                         #accessories
            "not R_Over", Null(),
            "R_Over != 'red dress' and R_Over != 'blue dress'", Null(),
            "R_Accessory == 'classic belt' and Rogue_Arms == 1", "images/RogueSprite/Rogue_Sprite_Over_XBelt1.png",
            "R_Accessory == 'classic belt'", "images/RogueSprite/Rogue_Sprite_Over_XBelt2.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo.png",
            "True", Null(), 
            ),                           
        (0,0), ConditionSwitch(                                                                         #hand spunk
            "not R_Spunk", Null(), 
            "'hand' in R_Spunk and Rogue_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                         #face spunk
            "not R_Spunk", Null(), 
            "'facial' in R_Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                         #belly spunk
            "'belly' in R_Spunk", "images/RogueSprite/Rogue_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(                                                                         #Props
            "not R_Held or Rogue_Arms != 2", Null(), 
            "Rogue_Arms == 2 and R_Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "Rogue_Arms == 2 and R_Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
            "Rogue_Arms == 2 and R_Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "Rogue_Arms == 2 and R_Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(), 
            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Rogue'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",  
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Rogue'", Null(), 
            #this doesn't activate unless Rogue is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                          
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Rogue'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy",
            "Trigger == 'fondle pussy'", "GropePussy",
            "Trigger == 'lick pussy'", "Lickpussy",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Rogue'", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",        
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",            
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",       
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),                                              
            #When both triggers are the same, do nothing  
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",  
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy",
            "Trigger2 == 'lick pussy'", "Lickpussy",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Kitty's hand on her)
            "not Trigger4 or Ch_Focus != 'Rogue'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger4 == 'lick pussy'", "Lickpussy",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger4 == 'suck breasts'", "LickRightBreast",          
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(  
            #UI tool for Trigger3(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Trigger3 or Ch_Focus == 'Rogue'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and R_Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",            
            "Trigger3 == 'lick pussy'", "Lickpussy",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast", 
            "Trigger3 == 'suck breasts'", "LickRightBreast",          
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right  
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",                 
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),            
        )                 
    anchor (0.6, 0.0)               
    zoom .75             
    
image Rogue Blink:
    ConditionSwitch(
    "R_Eyes == 'sexy'", "images/RogueSprite/Rogue_eyes_sexy.png",
    "R_Eyes == 'side'", "images/RogueSprite/Rogue_eyes_side.png",
    "R_Eyes == 'surprised'", "images/RogueSprite/Rogue_eyes_surprised.png",
    "R_Eyes == 'normal'", "images/RogueSprite/Rogue_eyes_normal.png",    
    "R_Eyes == 'stunned'", "images/RogueSprite/Rogue_eyes_stunned.png",
    "R_Eyes == 'down'", "images/RogueSprite/Rogue_eyes_down.png",
    "R_Eyes == 'closed'", "images/RogueSprite/Rogue_eyes_closed.png",
    "R_Eyes == 'manic'", "images/RogueSprite/Rogue_eyes_manic.png",
    "R_Eyes == 'squint'", "Rogue_Squint",
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

image Rogue_Squint:
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

image Rogue_Selfie:
    
        contains:
            "images/KittySelfie/Kitty_selfie_floor.png",
            pos (300, 200)
            zoom .5


        contains:
            ConditionSwitch(
                "R_HairColor == 'black' or R_HairColor == 'blackwhite'", "images/RogueSelfie/Rogue_selfie_hairBlack_back.png",
                "R_HairColor == 'blonde' or R_HairColor == 'blondewhite'", "images/RogueSelfie/Rogue_selfie_hairBlonde_back.png",
                "True", "images/RogueSelfie/Rogue_selfie_hair_back.png",
                ),

            pos (370, 90)
            zoom .4
        contains:
            ConditionSwitch(
                "R_Tan == 'tan1'", "images/RogueSelfie/Rogue_t1selfie_base.png",
                "R_Tan == 'tan'", "images/RogueSelfie/Rogue_tselfie_base.png",
                "True", "images/RogueSelfie/Rogue_selfie_base.png",
                ),
            pos (320, 320)
            zoom .4
        contains:
            ConditionSwitch(
                "R_BodySuit == 'classic uniform'", "images/RogueSelfie/Rogue_Selfie_XCatsuit.png",
                "R_BodySuit == 'classic uniform damaged'", "images/RogueSelfie/Rogue_Selfie_XCatsuit_Dmg.png",
                "True", Null(),
                ),
            pos (320, 320)
            zoom .4

        contains:
            ConditionSwitch(
                "R_Pierce == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_barbell_only.png",
                "R_Pierce == 'ring'", "images/RogueBJFace/Rogue_tj_tits_ring_only.png",
                "True", Null(),
                ),
            pos (320, 320)
            zoom .4

        #contains:
        #    "images/RogueBJFace/Rogue_tj_tits.png"
        #    pos (320, 320)
        #    zoom .4

        contains:
            "Rogue_SelfieChin"
            pos (370, 90)
            zoom .4

        contains:
            ConditionSwitch(
                "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueSelfie/Rogue_selfie_hairBlackwhite.png",
                "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSelfie/Rogue_selfie_hairBlack.png",
                "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueSelfie/Rogue_selfie_hairBlondewhite.png",
                "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSelfie/Rogue_selfie_hairBlonde.png",
                "R_Hair == 'evo'", "images/RogueSelfie/Rogue_selfie_hair.png",
                "True", "images/RogueSelfie/Rogue_selfie_hair.png",
                ), 
            pos (370, 90)
            zoom .4
        #contains:
        #    "Rogue_BJFace" 
        #    pos (150, -560)
        #    zoom .95
        #    pos (-60, 200)

        #LiveComposite(    
        #(787,913),    
        contains:
            ConditionSwitch(
                "R_SelfieOverlay","images/Selfie/Selfie_overlay_01.png",
                "True", Null(),
                ),
            pos (320, 320)
            zoom .4

        contains:
            "images/KittySelfie/Kitty_selfie_cellphone.png",
            pos (300, 200)
            zoom .5
        pos (0,0)
#        )
#    zoom .5 
    #offset (-300,-200)
#image Rogue_Selfie = im.Crop(Rogue_Selfie2, (0, 0, 100, 307))
#Xavier Sprite Compositing
image Professor:
    LiveComposite(
        (429,521),
        (0,0), "images/NPC/Xavier_body.png",
        (0,0), ConditionSwitch(
            "X_Brows == 'concentrate'", "images/NPC/Xavier_brows_concentrate.png",
            "X_Brows == 'happy'", "images/NPC/Xavier_brows_happy.png",
            "X_Brows == 'shocked'", "images/NPC/Xavier_brows_shocked.png",
            "X_Brows == 'neutral'", "images/NPC/Xavier_brows_neutral.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "X_Mouth == 'concentrate'", "images/NPC/Xavier_mouth_stern.png",            
            "X_Mouth == 'happy'", "images/NPC/Xavier_mouth_smile.png",
            "X_Mouth == 'neutral'", "images/NPC/Xavier_mouth_neutral.png",
            "True", Null(),
            ),
        (0,0), "Xavier Blink",
        (0,0), ConditionSwitch(
            "X_Psychic == 1", "images/NPC/Xavier_psychic.png",        
            "True", Null(),
            ),
        )           
    anchor (0.5, 0.0)
    offset (0,150)#200)
    zoom 1.1
        
image Xavier Blink:
    ConditionSwitch(
    "X_Eyes == 'concentrate'", "images/NPC/Xavier_eyes_closed.png",  
    "X_Eyes == 'hypno'", "images/NPC/Xavier_eyes_hypno.png",        
    "X_Eyes == 'shocked'", "images/NPC/Xavier_eyes_shocked.png",
    "True", "images/NPC/Xavier_eyes_happy.png",  
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/NPC/Xavier_eyes_closed.png"
    .25
    repeat     

image Mystique_Picture:
    "images/NPC/Xavier_Picture2.png"
    xalign 0.5 
    yalign 0.5
    zoom 0.7


screen Mystique_Pic:
    add "images/NPC/Xavier_Picture2.png" xalign 0.5 yalign 0.5 zoom 0.7
    key "mouseup_1" action Hide("Mystique_Pic")
    #timer 10.0 action Hide("Mystique_Pic")


#Night composite
image setting = LiveComposite(
    (1024,768),
    (0, 0), ConditionSwitch(        
        "Current_Time == 'Evening'", "images/sky_sunset.jpg",
        "Current_Time == 'Night'", "images/sky_night.jpg",        
        "True", "images/sky_day.jpg",        
        ),
    (0, 0), ConditionSwitch(           
        "bg_current == 'bg study'", "images/study.jpg",
        "bg_current == 'bg player'", "images/playerroom.png",            
        "bg_current == 'bg dangerroom'", "images/dangerroom.jpg",        
        "bg_current == 'bg showerroom'", "images/Shower.jpg",
        "bg_current == 'bg rogue'", "images/Rogueroom.png",
        "bg_current == 'bg movies'", "images/Movies.jpg",               
        "bg_current == 'bg restaurant'", "images/Restaurant.jpg",
        "bg_current == 'bg kitty'", "images/kittyroom.png",          
        "bg_current == 'bg emma'", "images/emmaroom.png",            
#        "bg_current == 'bg classroom'", "images/ClassroomLit.jpg",        
        # if bg_current == 'bg campus' or anything else        
        "Current_Time == 'Evening'",    "images/Crossroads_Evening.jpg",
        "Current_Time == 'Night'",      "images/Crossroads_Night.jpg",    
        "True",                         "images/Crossroads_Day.jpg",  
        ),     
    )
        
label Display_Background(Entry = 0): 
        # call Display_Background(1)              
        #Displays the current background
        if Entry:     
                                scene bg_entry onlayer backdrop   
        elif bg_current == "bg player":        
                                scene bg_player onlayer backdrop         
        elif bg_current == "bg rogue":        
                                scene bg_rogue onlayer backdrop   
        elif bg_current == "bg kitty":        
                                scene bg_kitty onlayer backdrop 
        elif bg_current == "bg emma":        
                                scene bg_emma onlayer backdrop  
        elif bg_current == "bg classroom":        
                                scene bg_class onlayer backdrop 
        elif bg_current == "bg dangerroom":        
                                scene bg_danger onlayer backdrop
        elif bg_current == "bg pool":  
                            if Current_Time == "Evening":
                                scene bg_pool_e onlayer backdrop 
                            elif Current_Time == "Night":
                                scene bg_pool_n onlayer backdrop 
                            else:
                                scene bg_pool_d onlayer backdrop 
        elif bg_current == "bg field":        
                                scene bg_field onlayer backdrop  
        elif bg_current == "bg Mystique":        
                                scene bg_mystique onlayer backdrop            
        elif bg_current == "bg showerroom":        
                                scene bg_shower onlayer backdrop  
        elif bg_current == "bg study":        
                                scene bg_study onlayer backdrop    
        elif bg_current == "bg movies":        
                                scene bg_movies onlayer backdrop          
        elif bg_current == "bg restaurant":        
                                scene bg_rest onlayer backdrop   
        else: # if 'bg campus' or anything else        
                                scene bg_campus onlayer backdrop   
        return

image bg_entry = "images/Door.jpg"        
image bg_player:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/playerroom.png"
image bg_rogue:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains:
                "images/Rogueroom.png"        
image bg_kitty:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/kittyroom.png"

image bg_emma:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'", "images/sky_sunset.jpg",
                "Current_Time == 'Night'", "images/sky_night.jpg",        
                "True", "images/sky_day.jpg",
                )   
        contains: 
                "images/emmaroom.png"
                
image bg_campus:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Current_Time == 'Evening'",    "images/Crossroads_Evening.jpg",
                "Current_Time == 'Night'",      "images/Crossroads_Night.jpg",    
                "True",                         "images/Crossroads_Day.jpg",
                )       
        
image bg_class:
        contains:
            "images/Classroom.jpg"
        contains:
            ConditionSwitch(        
                "newgirl['Mystique'].Loc == 'bg teacher'", "Mystique_At_Podium",
                "E_Loc == 'bg teacher'", "Emma_At_Podium",
                "E_Loc == 'bg desk'", "Emma_At_Desk",
                "True", Null(),
                )
        contains:
            #The overlay Podium
            "images/ClassroomFront.png"
        contains:
            ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),
                "True", "images/ClassroomPupils.png",
                )

#image bg_classlit = "images/ClassroomLit.jpg"
#image bg_classnight = "images/ClassroomNight.jpg"
image bg_danger = "images/dangerroom.jpg"
image bg_pool = "images/pool.jpg"
image bg_pool_d = "images/pool_day.png"
image bg_pool_e = "images/pool_evening.png"
image bg_pool_n = "images/pool_night.png"
image bg_field = "images/Football_Field.png"       
image bg_mystique = "images/mystiqueroom.png"       
image bg_shower = "images/Shower.jpg"
image bg_study = "images/study.jpg"
image bg_movies = "images/Movies.jpg"     
image bg_rest = "images/Restaurant.jpg"







# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
image Rogue_Doggy:
    LiveComposite(                                                                                 #Base body
        (420,750),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Rogue_Doggy_Fuck3_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Rogue_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Rogue_Doggy_Fuck_Top",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Doggy_Anal_Head_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Rogue_Doggy_Fuck2_Top",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Rogue_Doggy_Fuck_Top",
            "True", "Rogue_Doggy_Body",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Rogue_Doggy_Fuck3_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Rogue_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Rogue_Doggy_Fuck_Ass",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Doggy_Anal_Head_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Rogue_Doggy_Fuck2_Ass",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Rogue_Doggy_Fuck_Ass",
            "True", "Rogue_Doggy_Ass",            
            ),
        )
    align (0.6,0.0)
    
            
image Rogue_Doggy_Body = LiveComposite(                                                                                         #Upper body
        (420,750),
        (0,0), ConditionSwitch(                                                                                 #Hair underlayer
            "R_Water", Null(), 
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueDoggy/Rogue_Doggy_HairBlackwhiteB.png",   
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackB.png",   
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueDoggy/Rogue_Doggy_HairBlondewhiteB.png",   
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeB.png",   
            "R_Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairB.png",   
            "True", Null(),                   
            ),   
        (0,0), ConditionSwitch(  
            "R_Tan and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_tDoggy_BallGag.png", 
            "R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGag.png",
            "True", Null(), #Rogue_Doggy_BallGag
            ),
        (0,0), ConditionSwitch(  
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Body.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Body.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Body.png",
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "R_Tan and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_tDoggy_BallGagTop.png",
            "R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BallGagTop.png",
            "R_Tan and 'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_tDoggy_Mouth_BlowW.png",
            "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            "R_Tan and R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Blow.png",
            "R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'lipbite'", "images/RogueDoggy/Rogue_tDoggy_Mouth_LipbiteW.png",
            "'mouth' in R_Spunk and R_Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_LipbiteW.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueDoggy/Rogue_tDoggy_Mouth_SurprisedW.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_SurprisedW.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueDoggy/Rogue_tDoggy_Mouth_BlowW.png",
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueDoggy/Rogue_tDoggy_Mouth_SadW.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_SadW.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueDoggy/Rogue_tDoggy_Mouth_SmileW.png",   
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_SmileW.png",   
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueDoggy/Rogue_tDoggy_Mouth_TongueW.png",  
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_TongueW.png",  
            "R_Tan and 'mouth' in R_Spunk", "images/RogueDoggy/Rogue_tDoggy_Mouth_NormalW.png",   
            "'mouth' in R_Spunk", "images/RogueDoggy/Rogue_Doggy_Mouth_NormalW.png",   
            "R_Tan and R_Mouth == 'normal'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Normal.png",
            "R_Mouth == 'normal'", "images/RogueDoggy/Rogue_Doggy_Mouth_Normal.png",
            "R_Tan and R_Mouth == 'lipbite'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Lipbite.png",
            "R_Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_Lipbite.png",
            "R_Tan and R_Mouth == 'sucking'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Blow.png",            
            "R_Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",            
            "R_Tan and R_Mouth == 'kiss'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Surprised.png",
            "R_Mouth == 'kiss'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "R_Tan and R_Mouth == 'sad'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Sad.png",
            "R_Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_Sad.png",
            "R_Tan and R_Mouth == 'smile'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Smile.png",
            "R_Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "R_Tan and R_Mouth == 'grimace'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Smile.png",
            "R_Mouth == 'grimace'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "R_Tan and R_Mouth == 'surprised'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Surprised.png",       
            "R_Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",       
            "R_Tan and R_Mouth == 'tongue'", "images/RogueDoggy/Rogue_tDoggy_Mouth_Tongue.png", 
            "R_Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_Tongue.png", 
            "R_Tan", "images/RogueDoggy/Rogue_tDoggy_Mouth_Smile.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png", 
            ),
                                                              #Body base
        (0,0), ConditionSwitch(                                                                                 #Blush
            "R_Tan and R_Blush and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_tDoggy_BlushEvoBallGag.png",
            "R_Blush and R_Gag == 'ballgag'", "images/RogueDoggy/Rogue_Doggy_BlushEvoBallGag.png",
            "R_Tan and R_Blush", "images/RogueDoggy/Rogue_tDoggy_BlushEvo.png",
            "R_Blush", "images/RogueDoggy/Rogue_Doggy_BlushEvo.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                                 #Mouth
            "R_Gag == 'ringgag'", "images/RogueDoggy/Rogue_Doggy_RingGag.png",
            "True", Null(), #Rogue_Doggy_RingGag
            ),
        (0,0), ConditionSwitch(                                                                                 #Brows
            "R_Brows == 'normal'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "R_Brows == 'angry'", "images/RogueDoggy/Rogue_Doggy_Brows_Angry.png",
            "R_Brows == 'sad'", "images/RogueDoggy/Rogue_Doggy_Brows_Sad.png",
            "R_Brows == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Brows_Surprised.png",        
            "R_Brows == 'confused'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            ),     
        (0,0), "Rogue Doggy Blink",                                                                             #Eyes
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Glasses", "images/RogueDoggy/Rogue_Doggy_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not R_Chest", Null(), 
            "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit.png",  
            "R_Chest == 'bra'", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
            "R_Chest == 'sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png",
            "R_Chest == 'blue sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_BYSportsBra.png",
            "R_Chest == 'red sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_RYSportsBra.png",
            "R_Chest == 'lace bra'", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
            "R_Chest == 'SR7 tank short'", "images/RogueDoggy/Rogue_Doggy_Chest_TankShort_SR7.png",
            "R_Chest == 'tank short'", "images/RogueDoggy/Rogue_Doggy_Chest_TankShort.png",
            "R_Chest == 'slut tank short'", "images/RogueDoggy/Rogue_Doggy_Chest_TankShort.png",
            "R_BodySuit and not R_BodySuitOff", Null(),
            "R_Chest == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
            "R_Chest == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
            "R_Chest == 'green crop top'", "images/RogueDoggy/Rogue_Doggy_Green_Crop_Top.png",
            "R_Chest == 'black crop top'", "images/RogueDoggy/Rogue_Doggy_Black_Crop_Top.png",
            "R_Chest == 'cheerleader'", "images/RogueDoggy/Rouge_Doggy_Cheerleader_Outfit.png",
            "True", Null(),            
            ), 
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),
            "R_BodySuit == 'classic uniform'", "images/RogueDoggy/Rogue_Doggy_XCatsuit_top.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueDoggy/Rogue_Doggy_XCatsuit_Dmg_top.png",
            "R_BodySuit == 'swimsuit1' or R_BodySuit == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit.png",
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not R_Chest", Null(), 
            "R_Chest == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
            "R_Chest == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
            "R_Chest == 'green crop top'", "images/RogueDoggy/Rogue_Doggy_Green_Crop_Top.png",
            "R_Chest == 'black crop top'", "images/RogueDoggy/Rogue_Doggy_Black_Crop_Top.png",
            "R_Chest == 'cheerleader'", "images/RogueDoggy/Rouge_Doggy_Cheerleader_Outfit.png",
            "True", Null(),            
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                                                                         #accessories
            "R_Accessory == 'classic belt'", "images/RogueDoggy/Rogue_Doggy_Over_XBelt.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not R_Over", Null(),
            "R_Over == 'SR7 mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh_SR7.png",
            "R_Over == 'mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png",
            "R_Over == 'white mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_WhiteMesh.png",
            "R_Over == 'blue mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_BlueMesh.png",
            "R_Over == 'red mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_RedMesh.png",
            "R_Over == 'yellow mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_YellowMesh.png",
            "R_Over == 'black mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_BlackMesh.png",           
            "R_Over == 'pink top'", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png",
            "R_Over == 'red top'", "images/RogueDoggy/Rogue_Doggy_Over_Red.png",             
            "R_Over == 'classic jacket'", "images/RogueDoggy/Rogue_Doggy_Over_XJacket.png",
            "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png",
            "R_Over == 'blue hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_BHoodie.png",
            "R_Over == 'red hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_RHoodie.png",
            "R_Over == 'yellow hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_YHoodie.png",
            "R_Over == 'black hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_DHoodie.png",
            "R_Over == 'white hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_WHoodie.png",           
            "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png",         
            "R_Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelTop.png",
            "R_Over == 'red dress'", "images/RogueDoggy/Rogue_reddress_top.png",
            "R_Over == 'blue dress'", "images/RogueDoggy/Rogue_bluedress_rear_top.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(                                                                                 #Hair
            "R_Water and R_HairColor == 'blackwhite'", "images/RogueDoggy/Rogue_Doggy_HairBlackwhiteWet.png",   
            "R_Water and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackWet.png",   
            "R_Water and R_HairColor == 'blondewhite'", "images/RogueDoggy/Rogue_Doggy_HairBlondewhiteWet.png",   
            "R_Water and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeWet.png",   
            "R_Water", "images/RogueDoggy/Rogue_Doggy_HairWet.png",   
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueDoggy/Rogue_Doggy_HairBlackwhiteF.png",   
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackF.png",   
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueDoggy/Rogue_Doggy_HairBlondewhiteF.png",   
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeF.png",   
            "R_Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairF.png",   
            "True and R_HairColor == 'blackwhite'", "images/RogueDoggy/Rogue_Doggy_HairBlackwhiteF.png",                     
            "True and R_HairColor == 'black'", "images/RogueDoggy/Rogue_Doggy_HairBlackF.png",                     
            "True and R_HairColor == 'blondewhite'", "images/RogueDoggy/Rogue_Doggy_HairBlondewhiteF.png",                     
            "True and R_HairColor == 'blonde'", "images/RogueDoggy/Rogue_Doggy_HairBlondeF.png",                     
            "True", "images/RogueDoggy/Rogue_Doggy_HairF.png",                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #face spunk
            "not R_Spunk", Null(),
            "'facial' in R_Spunk", "images/RogueDoggy/Rogue_Doggy_Facial.png",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hair            
            "R_Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png",
            "R_Over == 'blue hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_BHood.png",
            "R_Over == 'red hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_RHood.png",
            "R_Over == 'yellow hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_YHood.png",
            "R_Over == 'black hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_DHood.png",
            "R_Over == 'white hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_WHood.png", 
            "True", Null(),                     
            ),  
        )

image Rogue_Doggy_Ass = LiveComposite(                                                                                          #Lower body
        (420,750), #(210,375), #(419,750), 
        (0,0), ConditionSwitch(                                                                                 #Panties back
            "not R_PantiesDown or (R_Legs == 'pants' and not R_Upskirt) or R_BodySuit == 'classic uniform damaged'", Null(),  
            "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",    
            "R_Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Back.png",   
            "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Back.png",   
            "R_Panties == 'lace panties' or R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",  
            #"R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Ass.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Ass.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Ass.png", 
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "not P_Sprite or (P_Cock != 'in' and P_Cock != 'anal' and P_Cock != 'plug')", Null(),
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),
            "R_BodySuit == 'classic uniform damaged'", "images/RogueDoggy/Rogue_Doggy_XCatsuit_bottom_Dmg_botpart.png",
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Hose
            "R_Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
            "R_Hose == 'SR7 hose'", "images/RogueDoggy/Rogue_Doggy_Hose_SR7.png",
            "True", Null(),
            ),             
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "not R_PantiesDown or (R_Legs == 'pants' and not R_Upskirt) or R_BodySuit == 'classic uniform damaged'", Null(),
            "R_Panties == 'shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png",
            "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down_Wet.png",
            "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down_Wet.png", #fix turn this on when graphics fixed
            "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png",
            "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts_Down.png",
            "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts_Down.png", 
            "R_Panties == 'green panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "R_Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Down.png", 
            "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Down_Wet.png",
            "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Down.png",  
            "R_Panties == 'lace panties' or R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",  
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(                                                                                 #Pussy Composite           
            "P_Sprite and P_Cock == 'in' and Speed > 2", "Rogue_Pussy_Fucking3",
            "P_Sprite and P_Cock == 'in' and Speed > 1", "Rogue_Pussy_Fucking2",
            "P_Sprite and P_Cock == 'in' and Speed", "Rogue_Pussy_Moving",
            "P_Sprite and P_Cock == 'in'", "Rogue_Pussy",    
            "Trigger == 'lick pussy'", "images/RogueDoggy/Rogue_Doggy_Pussy_Open.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png", 
            ),   
#        (0,0), ConditionSwitch(                                                                                 #spunkpussy Layer
#            "R_Spunk == 'in' and P_Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_SpunkPussyOpen.png",  #fix for R_Spunk is used later
#            "R_Spunk == 'in'", "images/RogueDoggy/Rogue_Doggy_SpunkPussyClosed.png", 
#            "R_Wet and P_Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png", 
#            "R_Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png", 
#            "True", Null(),                    
#            ),   
        (0,0), ConditionSwitch(                                                                                 #pubes              
            "not R_Pubes", Null(),         
            "P_Sprite and P_Cock == 'in'", Null(),
            "(R_Legs == 'pants' or (R_BodySuit and R_BodySuit != 'classic uniform damaged' and not R_BodySuitOff)) and not R_Upskirt and (R_HairColor == 'black' or R_HairColor == 'blackwhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlack_Panties.png",   
            "(R_Legs == 'pants' or (R_BodySuit and R_BodySuit != 'classic uniform damaged' and not R_BodySuitOff)) and not R_Upskirt and (R_HairColor == 'blonde' or R_HairColor == 'blondewhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlonde_Panties.png",   
            "(R_Legs == 'pants' or (R_BodySuit and R_BodySuit != 'classic uniform damaged' and not R_BodySuitOff)) and not R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
            "R_PantiesDown and (R_HairColor == 'black' or R_HairColor == 'blackwhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlack.png",  
            "R_PantiesDown and (R_HairColor == 'blonde' or R_HairColor == 'blondewhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlonde.png",  
            "R_PantiesDown", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
            "R_Panties and (R_HairColor == 'black' or R_HairColor == 'blackwhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlack_Panties.png",
            "R_Panties and (R_HairColor == 'blonde' or R_HairColor == 'blondewhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlonde_Panties.png",
            "R_Panties", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "R_Hose and R_Hose != 'stockings' and (R_HairColor == 'black' or R_HairColor == 'blackwhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlack_Panties.png",   
            "R_Hose and R_Hose != 'stockings' and (R_HairColor == 'blonde' or R_HairColor == 'blondewhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlonde_Panties.png",   
            "R_Hose and R_Hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",   
            "True and (R_HairColor == 'black' or R_HairColor == 'blackwhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlack.png",  
            "True and (R_HairColor == 'blonde' or R_HairColor == 'blondewhite')", "images/RogueDoggy/Rogue_Doggy_PubesBlonde.png",  
            "True", "images/RogueDoggy/Rogue_Doggy_Pubes.png",  
            ),  
        (0,0), ConditionSwitch(                                                                                 #Pussy Piercings          
            "P_Sprite", Null(),             
            "R_Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",            
            "R_Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "True", Null(),  
            ),   
        (0,0), ConditionSwitch(                                                                                 #Anus Composite            
            "P_Sprite and P_Cock == 'anal' and Speed > 3", "Rogue_Anal_Fucking3",         
            "P_Sprite and P_Cock == 'anal' and Speed > 2", "Rogue_Anal_Fucking2",         
            "P_Sprite and P_Cock == 'anal' and Speed > 1", "Rogue_Anal_Fucking",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Rogue_Anal",  
            "P_Sprite and P_Cock == 'plug' and Speed", "Rogue_Anal_Plug_Heading",
            "P_Sprite and P_Cock == 'plug' and R_Plugged", "images/RogueDoggy/Rogue_Doggy_Plugged.png",  
            "P_Sprite and P_Cock == 'plug'", "Rogue_Anal_Plug",  
#            "Action == 'plug'", "Rogue_Anal_Plug",  
#            "Action == 'plug'", "test_case",
            "R_Plugged", "images/RogueDoggy/Rogue_Doggy_Plugged.png",   
            "R_Loose", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",   
            "True", "images/RogueDoggy/Rogue_Doggy_Asshole_Tight.png", 
            ),
        (0,0), ConditionSwitch(                                                                                 #Hose
            #"R_Spank == 0", "images/RogueDoggy/Rogue_Doggy_Spank0.png",
            "R_Spank >= 1 and R_Spank <= 4 and R_Plugged", "images/RogueDoggy/Rogue_Doggy_SpankPlugged1.png",
            "R_Spank >= 1 and R_Spank <= 4 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/RogueDoggy/Rogue_Doggy_SpankAnal1.png",
            "R_Spank >= 1 and R_Spank <= 4", "images/RogueDoggy/Rogue_Doggy_Spank1.png",
            "R_Spank >= 5 and R_Spank <= 10 and R_Plugged", "images/RogueDoggy/Rogue_Doggy_SpankPlugged2.png",
            "R_Spank >= 5 and R_Spank <= 10 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/RogueDoggy/Rogue_Doggy_SpankAnal2.png",
            "R_Spank >= 5 and R_Spank <= 10", "images/RogueDoggy/Rogue_Doggy_Spank2.png",
            "R_Spank >= 11 and R_Plugged", "images/RogueDoggy/Rogue_Doggy_SpankPlugged3.png",
            "R_Spank >= 11 and (P_Cock == 'anal' or P_Cock == 'plug')", "images/RogueDoggy/Rogue_Doggy_SpankAnal3.png",
            "R_Spank >= 11", "images/RogueDoggy/Rogue_Doggy_Spank3.png",
            "True", Null(),
            ),           
#        (0,0), "test_case",
        (0,0), ConditionSwitch(                                                                                 #spunkanal Layer
            "'anal' in R_Spunk and P_Sprite", Null(),   
            "'anal' in R_Spunk and P_Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",  
            "'anal' in R_Spunk and R_Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "'anal' in R_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png", 
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "R_PantiesDown", Null(),     
            "R_Panties == 'shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",
            "R_Panties == 'red shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_RYShorts_Wet.png",
            "R_Panties == 'blue shorts' and R_Wet", "images/RogueDoggy/Rogue_Doggy_BYShorts_Wet.png",          
            "R_Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
            "R_Panties == 'red shorts'", "images/RogueDoggy/Rogue_Doggy_RYShorts.png",
            "R_Panties == 'blue shorts'", "images/RogueDoggy/Rogue_Doggy_BYShorts.png",
            "R_Panties == 'green panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",          
            "R_Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies.png", 
            "R_Panties == 'black large panties' and R_Wet", "images/RogueDoggy/Rogue_Doggy_UndiesBlack_Wet.png",          
            "R_Panties == 'black large panties'", "images/RogueDoggy/Rogue_Doggy_UndiesBlack.png",          
            "R_Panties == 'lace panties'", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png",                      
            "R_Panties == 'black panties'", "images/RogueDoggy/Rogue_Doggy_Panties.png", 
            "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit_bottom.png",  
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(   
            "P_Sprite and (P_Cock == 'in' or P_Cock == 'anal' or P_Cock == 'plug')", Null(),
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),
            "R_BodySuit == 'classic uniform damaged'", "images/RogueDoggy/Rogue_Doggy_XCatsuit_bottom_Dmg_botpart.png",
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                                 #Panties if Down
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),
            "R_BodySuit == 'classic uniform' and R_Wet", "images/RogueDoggy/Rogue_Doggy_XCatsuit_bottom_Wet.png",
            "R_BodySuit == 'classic uniform'", "images/RogueDoggy/Rogue_Doggy_XCatsuit_bottom.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueDoggy/Rogue_Doggy_XCatsuit_bottom_Dmg_toppart.png",
            "R_BodySuit == 'swimsuit1' or R_BodySuit == 'swimsuit2'", "images/RogueDoggy/Rogue_Doggy_Swimsuit_bottom.png",
            "True", Null(),                     
            ),  
        (0,0), ConditionSwitch(                                                                         #full hose/tights  
            "P_Sprite and (P_Cock == 'in' or P_Cock == 'anal')", Null(), #fix this at some point, currently it clips tights
            "R_PantiesDown", Null(), 
            "R_Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",    
            "R_Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",    
            "R_Hose == 'tights' and R_Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
            "R_Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
            "R_Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",   
            "R_Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png", 
            "R_Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",            
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "R_Legs == 'pants' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png",            
            "R_Legs == 'pants' and R_Wet > 1", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png",
            "R_Legs == 'pants'", "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png",
            "R_Legs == 'skirt' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png",   
            "R_Legs == 'skirt' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png",   
            "R_Legs == 'skirt'", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png", 
            "R_Legs == 'SR7 skirtshort' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Legs_SkirtShort_SR7_UpAnal.png",   
            "R_Legs == 'SR7 skirtshort' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_SkirtShort_SR7_Up.png",   
            "R_Legs == 'SR7 skirtshort'", "images/RogueDoggy/Rogue_Doggy_Legs_SkirtShort_SR7.png", 
            "R_Legs == 'skirtshort' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Legs_SkirtShort_UpAnal.png",   
            "R_Legs == 'skirtshort' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_SkirtShort_Up.png",   
            "R_Legs == 'skirtshort'", "images/RogueDoggy/Rogue_Doggy_Legs_SkirtShort.png", 
            "R_Legs == 'cheerleader skirt' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Cheerleader_Skirt_UpAnal.png",   
            "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Cheerleader_Skirt_Up.png",   
            "R_Legs == 'cheerleader skirt'", "images/RogueDoggy/Rogue_Doggy_Cheerleader_Skirt.png", 
            "R_Legs == 'cheerleader skirtshort' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Cheerleader_SkirtShort_UpAnal.png",   
            "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Cheerleader_SkirtShort_Up.png",   
            "R_Legs == 'cheerleader skirtshort'", "images/RogueDoggy/Rogue_Doggy_Cheerleader_SkirtShort.png", 
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "R_Over == 'nighty' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",            
            "R_Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            "R_Over == 'towel' and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png",            
            "R_Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss.png",
            "R_Over == 'blue dress' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_bluedress_rear_bottom_up_anal.png",   
            "R_Over == 'blue dress' and R_Upskirt", "images/RogueDoggy/Rogue_bluedress_rear_bottom_up.png",   
            "R_Over == 'blue dress'", "images/RogueDoggy/Rogue_bluedress_rear_bottom.png", 
            "R_Over == 'red dress' and R_Upskirt and P_Sprite and P_Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_reddress_rear_bottom_up_anal.png",   
            "R_Over == 'red dress' and R_Upskirt", "images/RogueDoggy/Rogue_reddress_rear_bottom_up.png",   
            "R_Over == 'red dress'", "images/RogueDoggy/Rogue_reddress_rear_bottom.png", 
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #spunkass Layer
            "'back' in R_Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",  
            "True", Null(),                    
            ),   
        (0,0), ConditionSwitch(                                                                                 #Hotdogging underlayer
            "not P_Sprite or P_Cock != 'out'", Null(),   
            "(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",  
            "(R_Legs == 'skirtshort' or R_Legs == 'SR7 skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png", 
            ),    
        (0,0), ConditionSwitch(                                                                                 #Hotdogging Cock w/ alpha
            "not P_Sprite or P_Cock != 'out'", Null(),            
            "(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(R_Legs == 'skirt' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(R_Over == 'blue dress' or R_Over == 'red dress') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(R_Over == 'blue dress' or R_Over == 'red dress') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(R_Legs == 'skirtshort' or R_Legs == 'SR7 skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(R_Legs == 'skirtshort' or R_Legs == 'SR7 skirtshort' or R_Legs == 'cheerleader skirt') and R_Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
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

image Slap_Thy_Ass:
    (0,0), ConditionSwitch(                                                                                 #UI tool layer
            #"not UI_Tool", Null(),   
            #"UI_Tool", "Slap_Ass",  
            "not UI_Tool", "Slap_Ass2",  
            "True", Null(),   
            ),  
        
image Rogue Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(          
    "R_Eyes == 'sexy'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "R_Eyes == 'side'", "images/RogueDoggy/Rogue_Doggy_Eyes_Side.png",
    "R_Eyes == 'normal'", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    "R_Eyes == 'closed'", "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png",
    "R_Eyes == 'manic'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "R_Eyes == 'down'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",           
    "R_Eyes == 'stunned'", "images/RogueDoggy/Rogue_Doggy_Eyes_Stunned.png",
    "R_Eyes == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "R_Eyes == 'squint'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "True", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    ),
#    choice:
#        3.5
#    choice:
#        3.25
#    choice:
#        3
    3
    # This randomizes the time between blinking.
    "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png"
    .25
    repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Hotdogging animations
image Zero_Doggy_Up:                                                                                    #Cock when out (hotdog)
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png", 
            ),
        #"Cock__U"  
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null(), 
            ),
    # ConditionSwitch(    
    #     "P_CockVisible", alpha 1,
    #     "not P_CockVisible", alpha 0.4,
    #     "True", Null(), 
    #     ),
    #alpha P_CockVisible
    alpha 1

image Zero_Doggy_Up_alpha0_5:                                                                                    #Cock when out (hotdog)
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png", 
            ), 
        #"Cock__U"  
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null(), 
            ),
    # ConditionSwitch(    
    #     "P_CockVisible", alpha 1,
    #     "not P_CockVisible", alpha 0.4,
    #     "True", Null(), 
    #     ),
    #alpha P_CockVisible
    alpha 0.5

image Zero_Doggy_Up_alpha0:                                                                                    #Cock when out (hotdog)
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png", 
            ), 
        #"Cock__U"  
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null(), 
            ),
    # ConditionSwitch(    
    #     "P_CockVisible", alpha 1,
    #     "not P_CockVisible", alpha 0.4,
    #     "True", Null(), 
    #     ),
    #alpha P_CockVisible
    alpha 0

image Zero_Hotdog_Static:
    contains:
        ConditionSwitch(    
            "P_CockVisible == 1", "Zero_Doggy_Up",
            "P_CockVisible == 0.5", "Zero_Doggy_Up_alpha0_5",
            "P_CockVisible == 0", "Zero_Doggy_Up_alpha0",
            "True", "Zero_Doggy_Up", 
            ),        
        # "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Hotdog_Moving:
    contains:
        ConditionSwitch(    
            "P_CockVisible == 1", "Zero_Doggy_Up",
            "P_CockVisible == 0.5", "Zero_Doggy_Up_alpha0_5",
            "P_CockVisible == 0", "Zero_Doggy_Up_alpha0",
            "True", "Zero_Doggy_Up", 
            ),
        pos (175, 370) 
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                  #Insert cock animations
image Zero_Doggy_Insert_alpha1:                                                                                #Insert cock
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png", 
            ),
        #"Cock__In" 
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",           
            "True", Null(),
            ), 
    contains:
        ConditionSwitch(    
            "P_Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",           
            "True", Null(),
            ), 
    alpha 1

image Zero_Doggy_Insert_alpha0_5:                                                                                #Insert cock
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png", 
            ), 
        #"Cock__In" 
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",           
            "True", Null(),
            ), 
    contains:
        ConditionSwitch(    
            "P_Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",           
            "True", Null(),
            ), 
    alpha 0.5

image Zero_Doggy_Insert_alpha0:                                                                                #Insert cock
    contains:
        ConditionSwitch(    
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png", 
            ),
        #"Cock__In"  
    contains:
        ConditionSwitch(    
            "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",           
            "True", Null(),
            ), 
    contains:
        ConditionSwitch(    
            "P_Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",           
            "True", Null(),
            ), 
    alpha 0

image Cock__In:                                                                                #Insert cock
    contains:
        ConditionSwitch(   
            "P_CockTorso", Null(), 
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png", 
            ),
    # contains:
    #     ConditionSwitch(    
    #         "not P_CockTorso", Null(), 
    #         "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Torso_In_P.png",
    #         "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Torso_In_B.png",             
    #         "True", "images/RogueDoggy/Rogue_Doggy_Torso_In_G.png", 
    #         ),
    #     xpos -132

image Cock__U:                                                                                #Insert cock
    contains:
        ConditionSwitch(   
            "P_CockTorso", Null(), 
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",             
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png", 
            ),
    # contains:
    #     ConditionSwitch(    
    #         "not P_CockTorso", Null(), 
    #         "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Torso_U_P.png",
    #         "P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Torso_U_B.png",             
    #         "True", "images/RogueDoggy/Rogue_Doggy_Torso_U_G.png", 
    #         ),
    #     xpos -139
    #     ypos 4 #-50

image Zero_Doggy_Insert:                                                                                #Insert cock
    ConditionSwitch(    
            "P_CockVisible == 1", "Zero_Doggy_Insert_alpha1",
            "P_CockVisible == 0.5", "Zero_Doggy_Insert_alpha0_5",
            "P_CockVisible == 0", "Zero_Doggy_Insert_alpha0",
            "True", "Zero_Doggy_Insert_alpha1", 
            ), 

image Plug_Doggy_Insert:                                                                                #Insert cock
    contains:
        ConditionSwitch(    
            #"P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            #"P_Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",             
            "P_Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Plug_In.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Plug_In.png", 
            ), 
    #contains:
    #    ConditionSwitch(    
    #        "P_Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",           
    #        "True", Null(),
    #        ), 
    #contains:
    #    ConditionSwitch(    
    #        "P_Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",           
    #        "True", Null(),
    #        ), 
            
image Zero_Doggy_Heading:
    contains:
        subpixel True
        "Zero_Doggy_Insert"    
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500                    #in stroke
            pause 1
            ease 3 xpos 171 ypos 545                    #out stroke
            repeat

image Zero_Doggy_Fucking2:
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat
            
image Zero_Doggy_Fucking3:
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat
            
image Rogue_Pussy_Mask:                 #AlphaMask used to prevent the cock from moving past the pussy
    contains:                                                                                   #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"    
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              #Pussy fucking animations    
image Rogue_Pussy:                                                                                              #Full Animation for speed 0    
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Pussy_FBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Pussy_FBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png", 
            ),    
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (169,460) #Out stroke
    contains:                                                                                   #Mask
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Pussy_FMask.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Pussy_FMask.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_FMask.png", 
            ),
        

image Rogue_Pussy_Moving:                                                                                       #Full Animation for speed 1
    subpixel True
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Pussy_FBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Pussy_FBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png", 
            ),    
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518) 
        xzoom 1
    contains:                                                                                   #Base
        #"images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png" 
        "Rogue_Doggy_Pussy_FHole"   
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
        
        
image Rogue_Pussy_Hole_Mask: # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Moving"
    contains:                                                                                   #Base
        #AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        AlphaMask("Rogue_Doggy_Pussy_FHole", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518) 
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat 
            
image Rogue_Pussy_Heading: #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Moving"
    contains:                                                                                   #Mask
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Rogue_Pussy_Fucking2:                                                                                      #Full Animation for speed 2
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Pussy_FBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Pussy_FBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png", 
            ),    
    contains:                                                                                   #Base
        #"images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"  
        "Rogue_Doggy_Pussy_FHole"
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        

image Rogue_Pussy_Fucking3:                                                                                      #Full Animation for speed 3
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Pussy_FBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Pussy_FBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png", 
            ),  
    contains:                                                                                   #Base
        #"images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"  
        "Rogue_Doggy_Pussy_FHole"
    contains:                                                                                   #Cock        
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        
image Rogue_Doggy_Pussy_FHole:
    ConditionSwitch(                                                                                 #Pussy Composite           
        "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Pussy_FHole.png", 
        "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Pussy_FHole.png", 
        "True", "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", 
        ),         
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
image Rogue_Anal2:                                                                                               #Anal static
    contains:     
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png", 
            ),                                                                               #Base
    contains:
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullHole.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullHole.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png", 
            ),                                                 #Hole
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)
    contains:                                                                                   #Mask
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullMask.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullMask.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png", 
            ),
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5    
    contains:                                                                                   #Cheeks
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullCheeks.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullCheeks.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png", 
            ), 


image Rogue_Anal:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"   
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:                                                                                   #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Rogue_Anal_Plug:                                                                                               #Anal static Loose
    contains:                                                                                   #Base
        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"   
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:                                                                                   #Cock
        "Plug_Doggy_Insert"
        pos (172,500)
        #anchor (0.50,0.69)
        #pos (208,500)
        #zoom 1.25

        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png", 
            ),        
    contains:
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullHole.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullHole.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png", 
            ),                                       #Hole
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
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullMask.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullMask.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png", 
            ),
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat             
    contains:                                                                                   #Cheeks
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullCheeks.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullCheeks.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png", 
            ), 

image Rogue_Anal_Plug_Heading:                                                                                       #Animation for speed 1
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png", 
            ),       
        #"images/RogueDoggy/Rogue_Doggy_Anal_HeadingBase.png"    
    contains:
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullHole.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullHole.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png", 
            ),                                       #Hole
        #"images/RogueDoggy/Rogue_Doggy_Anal_HeadingBase.png"                                       #Hole
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
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullMask_Plug.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullMask_Plug.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullMask_Plug.png", 
            ), 
        #"images/RogueDoggy/Rogue_Doggy_Anal_HeadingMask_Plug.png"
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
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullCheeks.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullCheeks.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png", 
            ), 



image Rogue_Doggy_Anal_Head_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 0
        block:     
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
            
image Rogue_Doggy_Anal_Head_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
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
            
image Rogue_Anal_Fucking:                                                                                       #Animation for speed 2 Ass
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png", 
            ),        
    contains:                                                                                   #Hole
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullHole.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullHole.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png", 
            ),  
    # contains:
    #     "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_AnalMask.png")
    contains:                                                                                   #Mask
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullMask.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullMask.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png", 
            ),
    contains:                                                                                   #Cheeks
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullCheeks.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullCheeks.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png", 
            ), 


image Rogue_Doggy_Fuck_Top:                #animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 15#28
        pause .4
        block: 
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28 
            repeat
            
image Rogue_Doggy_Fuck_Ass:                #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
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


        #"Zero_Doggy_Insert"
        #pos (172,460)
        #block:
        #    ease .2 ypos 395
        #    pause .1
        #    ease .6 ypos 465
        #    repeat

        #anal1
        #"Zero_Doggy_Insert"
        #pos (172,460)
        #block:
        #    ease .5 ypos 395
        #    pause .25
        #    ease 1.75 ypos 460
        #    repeat
                      
image Rogue_Anal_Fucking2:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png", 
            ),       
    contains:                                                                                   #Hole
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullHole.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullHole.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png", 
            ),  
    # contains:
    #     "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullMask.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullMask.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png", 
            ),
    contains:                                                                                   #Cheeks
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullCheeks.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullCheeks.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png", 
            ), 

image Rogue_Anal_Fucking3:                                                                                      #Animation for speed 3 Ass
    contains:                                                                                   #Base
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullBase.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullBase.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png", 
            ),      
    contains:                                                                                   #Hole
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullHole.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullHole.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png", 
            ),  
    # contains:
    #     "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
    contains:                                                                                   #Cock
        AlphaMask("Zero_Doggy_Anal3", "images/RogueDoggy/Rogue_Doggy_AnalMask.png")       
    contains:                                                                                   #Mask
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullMask3.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullMask3.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullMask3.png", 
            ), 
    contains:                                                                                   #Cheeks
        ConditionSwitch(                                                                                 #Pussy Composite           
            "R_Tan == 'tan1'", "images/RogueDoggy/Rogue_t1Doggy_Anal_FullCheeks.png", 
            "R_Tan == 'tan'", "images/RogueDoggy/Rogue_tDoggy_Anal_FullCheeks.png", 
            "True", "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png", 
            ), 


image Rogue_Doggy_Fuck3_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .2 ypos 20             
            pause .05
            repeat
            
image Rogue_Doggy_Fuck3_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 5
        block:     
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .1 ypos 5 
            pause .05
            repeat #.90


image Rogue_Doggy_Fuck2_Top:                #animation for anal fucking2 top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"         
        ypos 20
        block: 
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20             
            pause .05
            repeat
            
image Rogue_Doggy_Fuck2_Ass:                #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
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

#image Slap_Ass:    
#    contains:
#        "SlapHand"
#        pause 1.2
#        Null()

image Slap_Ass:
    contains:
        "UI_Hand"    
        subpixel True        
        zoom 1        
        alpha 0.5
        anchor (0.5,0.5)
        pos (600,380)         
        rotate 40 
        block:
            parallel:
                ease .5 xpos 300 rotate 80                
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9        
            
image NotSlap_Ass:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 1
        pos (600,380) #follow through  point r-60
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            pos (600,380)            
            rotate 40
            parallel:
                ease .5 xpos 300 rotate 80                
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9
            repeat

image Slap_Ass2:
    contains:
        "UI_Hand"    
        subpixel True        
        zoom 1        
        alpha 0.5
        anchor (0.5,0.5)
        pos (800,350)         
        rotate 40 
        block:
            parallel:
                ease .1 xpos 670 #rotate 80                
                #ease .1 xpos 610 #rotate 80
                pause .3
            parallel:
                ease .1 ypos 550
                pause .3  
        alpha 0

            
#pos (100,450) #follow through  point r-60
#        pos (500,380) #high point r-40        
#        pos (310,520) #impact point r-60
#        block: 
#            ease 1 rotate 60
#            ease 1 rotate 90
#            repeat



# Kitty Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Rogue_SexSprite:            
    LiveComposite(                                                                                 #Base body
        (1120,840),  
        (0,0), ConditionSwitch(                                                         #Shows different upper body motion depending on events  
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Rogue_Sex_Body_Anim3",  
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Rogue_Sex_Body_Anim2",#akiparcero
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Rogue_Sex_Body_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Rogue_Sex_Body_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Rogue_Sex_Body_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Rogue_Hotdog_Body_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Rogue_Sex_Body_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Rogue_Sex_Body_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Rogue_Sex_Body_FootAnimStatic",
            
            "True", "Rogue_Sex_Body_Static",           
            ),  
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "Rogue_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "Rogue_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'in' and Speed >= 3", "Rogue_Sex_Legs_Anim3",
            "P_Sprite and P_Cock == 'in' and Speed >= 2", "Rogue_Sex_Legs_Anim2",
            "P_Sprite and P_Cock == 'in' and Speed", "Rogue_Sex_Legs_Anim1",
            "P_Sprite and P_Cock == 'out' and Speed >= 2","Rogue_Hotdog_Legs_Anim2",
            
            "P_Sprite and P_Cock == 'foot' and Speed >= 2", "Rogue_Sex_Legs_FootAnim2",
            "P_Sprite and P_Cock == 'foot' and Speed", "Rogue_Sex_Legs_FootAnim1",
            "P_Sprite and P_Cock == 'foot'", "Rogue_Sex_Legs_FootAnimStatic",
            
#            "P_Sprite and P_Cock == 'foot' and Speed >= 2", At("Rogue_Sex_Legs", Rogue_Sex_Legs_FootAnim2A()),
#            "P_Sprite and P_Cock == 'foot' and Speed", At("Rogue_Sex_Legs", Rogue_Sex_Legs_FootAnim1A()), 
#            "P_Sprite and P_Cock == 'foot'", At("Rogue_Sex_Legs", Rogue_Sex_Legs_FootAnimStaticA()), 
            
            "True", "Rogue_Sex_Legs_Static",            
            ),        
        ) 
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

#image Rogue_Sex_Legs = LiveComposite(  
image Rogue_Sex_Legs:
    LiveComposite(  
        #the legs used in the sex pose, referenced by Rogue_SexSprite
        (1120,840), 
        (0,0), ConditionSwitch(
            "R_Tan == 'tan1' and R_LegsUp", "images/RogueSex/Rogue_t1Sex_Legs_LegsUp.png",
            "R_Tan == 'tan' and R_LegsUp", "images/RogueSex/Rogue_tSex_Legs_LegsUp.png",
            "R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Legs.png",                                              #Legs Base                                                      #Legs Base
            "R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Legs.png",                                              #Legs Base                                                      #Legs Base
            #"R_Tan == 'tan2' and R_LegsUp", "images/RogueSex/Rogue_Sex_T2Legs_LegsUp.png",
            #"R_Tan == 'tan2'", "images/RogueSex/Rogue_Sex_T2Legs.png",                                            #Legs Base                                                      #Legs Base
            #"R_Tan == 'tan3' and R_LegsUp", "images/RogueSex/Rogue_Sex_T3Legs_LegsUp.png",
            #"R_Tan == 'tan3'", "images/RogueSex/Rogue_Sex_T3Legs.png",
            "R_LegsUp", "images/RogueSex/Rogue_Sex_Legs_LegsUp.png",
            "True", "images/RogueSex/Rogue_Sex_Legs.png",
            ),
            
        (0,0), ConditionSwitch( 
            "R_LegsUp", Null(),
            "R_Water", "images/RogueSex/Rogue_Sex_Water_Legs.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(
            "R_PantiesDown", Null(),
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "R_LegsUp", Null(),   
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_Dmg.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(
            "R_PantiesDown", Null(),
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "not R_LegsUp", Null(),   
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_LegsUp_Dmg.png",
            "True", Null(),                     
            ), 
        (0,0), "Rogue_Sex_Anus",                                                                          #Anus Composite 

        (0,0), "Rogue_Sex_Pussy",  
                                                                               #Pussy Composite

        (0,0), ConditionSwitch(
            "R_PantiesDown", Null(),     
            #"R_Panties == 'green panties' and R_Wet", "images/RogueSex/Rogue_Sex_Panties_Green_Wet.png",          
            #"R_Panties == 'green panties'", "images/RogueSex/Rogue_Sex_Panties_Green.png",  
            #"R_Panties == 'white panties' and R_Wet", "images/RogueSex/Rogue_Sex_Panties_White_Wet.png",          
            #"R_Panties == 'white panties'", "images/RogueSex/Rogue_Sex_Panties_White.png",  
            #"R_Panties == 'purple bikini panties' and R_Wet", "images/RogueSex/Rogue_Sex_Panties_Bikini1_Wet.png",          
            #"R_Panties == 'purple bikini panties'", "images/RogueSex/Rogue_Sex_Panties_Bikini1.png",  
            #"R_Panties == 'lace panties' and R_Wet", "images/RogueSex/Rogue_Sex_Panties_Lace_Wet.png",       
            #"R_Panties == 'lace panties'", "images/RogueSex/Rogue_Sex_Panties_Lace.png",   
            #"R_Panties == 'darker lace panties' and R_Wet", "images/RogueSex/Rogue_Sex_Panties_DarkerLace_Wet.png",       
            #"R_Panties == 'darker lace panties'", "images/RogueSex/Rogue_Sex_Panties_DarkerLace.png",   
            #"R_Panties == 'swimsuit3'", "images/RogueSex/Rogue_Sex_Swimsuit3_Bottom.png",
            #"R_Panties == 'zipper panties'", "images/RogueSex/RogueSexBDPantyClosed.png",
            #"R_Panties == 'zipper panties open'", "images/RogueSex/RogueSexBDPantyOpen.png",
            "R_Panties == 'black panties' and R_Wet", "images/RogueSex/Rogue_Sex_Panties_Wet.png",
            "R_Panties == 'black panties'", "images/RogueSex/Rogue_Sex_Panties.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "R_LegsUp", Null(),   
            "R_BodySuit == 'classic uniform' and R_Wet", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_Wet.png",
            "R_BodySuit == 'classic uniform'", "images/RogueSex/Rogue_Sex_XCatsuit_Legs.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_Dmg.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "not R_LegsUp", Null(),   
            "R_BodySuit == 'classic uniform' and R_Wet", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_LegsUp_Wet.png",
            "R_BodySuit == 'classic uniform'", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_LegsUp.png",
            "R_BodySuit == 'classic uniform damaged' and not R_PantiesDown", "images/RogueSex/Rogue_Sex_XCatsuit_Legs_LegsUp_Dmg.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(        
            "R_LegsUp", Null(),                                                                         #Legs Layer
            "R_Hose == 'SR7 hose'", "images/RogueSex/Rogue_Sex_SR7_Hose_Legs.png",
            #"R_Hose == 'stockings'", "images/RogueSex/Rogue_Sex_Stockings_Legs.png",
            #"R_Hose == 'white socks'", "images/RogueSex/Rogue_Sex_WSocks_Thigh_Legs.png",
            #"R_Hose == 'black socks'", "images/RogueSex/Rogue_Sex_BSocks_Thigh_Legs.png",
            #"R_Hose == 'pink socks'", "images/RogueSex/Rogue_Sex_PSocks_Thigh_Legs.png",
            "True", Null(),                      
            ), 
        (0,0), ConditionSwitch(
            "R_LegsUp", Null(),   
            "R_Boots == 'classic boots'", "images/RogueSex/Rogue_Sex_XShoes_Legs.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            #"R_Upskirt", Null(),  
            "R_Legs == 'SR7 skirtshort'", "images/RogueSex/Rogue_Sex_SR7_Skirt_Short.png",
            #"R_Legs == 'shorts' and R_Wet > 1", "images/RogueSex/Rogue_Sex_Shorts_Wet.png",
            #"R_Legs == 'shorts'", "images/RogueSex/Rogue_Sex_Shorts.png",
            #"R_Legs == 'blue shorts' and R_Wet > 1", "images/RogueSex/Rogue_Sex_BlueShorts_Wet.png",
            #"R_Legs == 'blue shorts'", "images/RogueSex/Rogue_Sex_BlueShorts.png",
            #"R_Legs == 'white shorts' and R_Wet > 1", "images/RogueSex/Rogue_Sex_WhiteShorts_Wet.png",
            #"R_Legs == 'white shorts'", "images/RogueSex/Rogue_Sex_WhiteShorts.png",                             
            #"R_LegsUp", Null(),
            #"R_Legs == 'capris' and R_Wet > 1", "images/RogueSex/Rogue_Sex_Pants_Blue_Wet.png",
            #"R_Legs == 'capris'", "images/RogueSex/Rogue_Sex_Pants_Blue.png",
            #"R_Legs == 'black jeans' and R_Wet > 1", "images/RogueSex/Rogue_Sex_Pants_Black_Wet.png",
            #"R_Legs == 'black jeans'", "images/RogueSex/Rogue_Sex_Pants_Black.png",
            #"R_Legs == 'yoga pants' and R_Wet > 1", "images/RogueSex/Rogue_Sex_Pants_Yoga_Wet.png",
            "True", Null(),                      
            ),   
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            #"R_Over == 'towel'", "images/RogueSex/Rogue_Sex_Towel_Legs.png",
            "True", Null(),                    
            ),   
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Pelvis.png",   
            "True", Null(),  
            ),  
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer  
            "not P_Sprite or P_Cock != 'out'", Null(),                    
            "Speed >= 2", "Rogue_Hotdog_Zero_Anim2",
            "Speed", "Rogue_Hotdog_Zero_Anim1",
            "True", "Rogue_Hotdog_Zero_Anim0",   
            ), 
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer  
            "not P_Sprite or P_Cock != 'foot'", Null(),                    
            "Speed >= 2", "Rogue_Footcock_Zero_Anim2",
            "Speed", "Rogue_Footcock_Zero_Anim1",
            "True", "Rogue_Footcock_Static",   
            ),
   
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not Speed", "Rogue_Sex_Feet",  
            "R_LegsUp and (P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out')", "Rogue_Sex_Feet", 
            "P_Cock == 'anal' or P_Cock == 'in' or P_Cock == 'out'", AlphaMask("Rogue_Sex_Feet", "images/RogueSex/Rogue_Sex_FeetMask.png"), 
            "True", "Rogue_Sex_Feet",            
            ),
        )
    
image Rogue_Sex_Feet = LiveComposite(                                                                                          
        #the lower legs used in the sex pose, referenced by Rogue_Sex_Legs
        (1120,840), 
        (0,0), ConditionSwitch(
            #"R_LegsUp", Null(),
            "R_Tan and R_LegsUp", "images/RogueSex/Rogue_tSex_Feet_LegsUp.png",
            "R_LegsUp", "images/RogueSex/Rogue_Sex_Feet_LegsUp.png",
            "R_Tan", "images/RogueSex/Rogue_tSex_Feet.png",                                                         #Legs Base
            "True", "images/RogueSex/Rogue_Sex_Feet.png",
            ),
        (0,0), ConditionSwitch(
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "not R_LegsUp", Null(),   
            "R_BodySuit == 'classic uniform'", "images/RogueSex/Rogue_Sex_XCatsuit_LegsUp.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_LegsUp_Dmg.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "R_LegsUp", Null(),   
            "R_BodySuit == 'classic uniform'", "images/RogueSex/Rogue_Sex_XCatsuit_Feet.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_Feet.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(
            "R_LegsUp", Null(),
            "R_Hose == 'SR7 hose'", "images/RogueSex/Rogue_Sex_SR7_Hose_Feet.png",  
            #"R_Hose == 'stockings'", "images/RogueSex/Rogue_Sex_Stockings_Feet.png",  
            #"R_Hose == 'white socks'", "images/RogueSex/Rogue_Sex_WSocks_Thigh_Feet.png",
            #"R_Hose == 'black socks'", "images/RogueSex/Rogue_Sex_BSocks_Thigh_Feet.png",
            #"R_Hose == 'pink socks'", "images/RogueSex/Rogue_Sex_PSocks_Thigh_Feet.png",                                                       #Legs Base
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "not R_LegsUp", Null(),
            "R_Hose == 'SR7 hose'", "images/RogueSex/Rogue_Sex_SR7_Hose_LegsUp.png", 
            # "R_Hose == 'stockings'", "images/RogueSex/Rogue_Sex_Stockings_Thigh_LegsUp_.png",  
            # "R_Hose == 'white socks'", "images/RogueSex/Rogue_Sex_WSocks_Thigh_LegsUp_.png",
            # "R_Hose == 'black socks'", "images/RogueSex/Rogue_Sex_BSocks_Thigh_LegsUp_.png",
            # "R_Hose == 'pink socks'", "images/RogueSex/Rogue_Sex_PSocks_Thigh_LegsUp_.png",                                                       #Legs Base
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "not R_LegsUp", Null(),   
            "R_Boots == 'classic boots'", "images/RogueSex/Rogue_Sex_XShoes_LegsUp.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(
            "R_LegsUp", Null(),   
            "R_Boots == 'classic boots'", "images/RogueSex/Rogue_Sex_XShoes_Feet.png",
            "True", Null(),                     
            ), 
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueSex/Rogue_Sex_Water_Feet.png",   
            "True", Null(),              
            ),  
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            #"R_LegsUp", Null(),
            #"R_Upskirt", Null(),                               
            #"R_Legs == 'capris'", "images/RogueSex/Rogue_Sex_Feet_Blue.png",
            #"R_Legs == 'black jeans'", "images/RogueSex/Rogue_Sex_Feet_Black.png",
            #"R_Legs == 'yoga pants'", "images/RogueSex/Rogue_Sex_Feet_Yoga.png",
            "True", Null(),                      
            ),   
        )


image Rogue_Sex_Pussy:            
    # This is the visual for her pussy during the Speed 0 mode (static).     
    contains:
            # The background plate of her pussy            
            ConditionSwitch(
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2 and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "P_Sprite and P_Cock == 'in' and Speed and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "P_Sprite and P_Cock == 'in' and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Closed.png",
                "P_Sprite and P_Cock == 'in' and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Closed.png",
                "P_Sprite and P_Cock == 'in'", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                "Trigger == 'lick pussy' and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Open.png",
                "Trigger == 'lick pussy' and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "True and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Pussy_Closed.png",
                "True and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Pussy_Closed.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                )    
    contains:
            # The background plate of her pussy            
            ConditionSwitch(    
                "not R_Wet", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_WetPussy_F.png",
                "True", "images/RogueSex/Rogue_Sex_WetPussy_C.png",
                )
    contains: 
            #ring piercing
            ConditionSwitch(  
                "R_Pierce != 'ring'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                ) 
    contains: 
            #barbell piercing
            ConditionSwitch(  
                "R_Pierce != 'barbell'", Null(),
                "not P_Sprite or P_Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )  
    #contains:
    #        ConditionSwitch(
    #        "R_PantiesDown and P_Cock != 'anal' and R_Panties == 'swimsuit3'", "images/RogueSex/Rogue_Sex_Swimsuit3_BottomPush.png",
    #        "True", Null(), 
    #        ),  

    contains:
            # pubes
            ConditionSwitch(    
                "not R_Pubes", Null(),         
                # "R_BodySuit and R_BodySuit != 'classic uniform damaged' and not R_BodySuitOff", Null(),
                #"P_Sprite and P_Cock == 'in' and Speed >= 2 and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Fucking.png",
                #"P_Sprite and P_Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                #"P_Sprite and P_Cock == 'in' and Speed and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Open.png",
                #"P_Sprite and P_Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                #"P_Sprite and P_Cock == 'in' and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Closed.png", 
                #"P_Sprite and P_Cock == 'in'", "images/RogueSex/Rogue_Sex_Pubes_Closed.png", 
                #"Trigger == 'lick pussy' and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Open.png", 
                #"Trigger == 'lick pussy'", "images/RogueSex/Rogue_Sex_Pubes_Open.png", 
                #"True and R_HairColor == 'black'", "images/RogueSex/Rogue_Sex_PubesBlack_Closed.png",
                #"True", "images/RogueSex/Rogue_Sex_Pubes_Closed.png",
                "R_HairColor == 'blonde' or R_HairColor == 'blondewhite'", "images/RogueSex/Rogue_Sex_Pubes_Blonde.png",
                "R_HairColor == 'black' or R_HairColor == 'blackwhite'", "images/RogueSex/Rogue_Sex_Pubes_Black.png",
                "True", "images/RogueSex/Rogue_Sex_Pubes.png",
                )
    #contains:
    #        ConditionSwitch(
    #        "R_PantiesDown and R_Panties == 'zipper panties'", "images/RogueSex/RogueSexBDPantyOpenTop.png",
    #        "R_PantiesDown and R_Panties == 'zipper panties open'", "images/RogueSex/RogueSexBDPantyOpenTop.png",
    #        "True", Null(), 
    #        ),

    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'in' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Puss_Under.png",   
                "True", Null(),  
                )  
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(    
                "not P_Sprite", Null(),  
                "P_Sprite and P_Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "P_Sprite and P_Cock == 'in' and Speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "P_Sprite and P_Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),  
                "True", Null(),  
                )  
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'in' not in R_Spunk or not P_Sprite or P_Cock != 'in' or not Speed", Null(), 
                "Speed <= 1", "Kitty_Pussy_Spunk_Heading",   
                "True", "images/RogueSex/Rogue_Sex_Spunk_Puss_Over.png",  
                )  
            
    #End Rogue Pussy composite


#Start Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Rogue_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(                                                                                             
            "P_Sprite and P_Cock == 'anal' and Speed >= 3", "images/RogueSex/Rogue_Sex_Hole_Open.png",         
            "P_Sprite and P_Cock == 'anal' and Speed >= 2", "images/RogueSex/Rogue_Sex_Hole_Open.png",
            "P_Sprite and P_Cock == 'anal' and Speed", "Rogue_Sex_Anal_Heading",
            "P_Sprite and P_Cock == 'anal'", "Rogue_Anal_Tip", 
            "R_Loose", "images/RogueSex/Rogue_Sex_Hole_Loose.png",   
            "True", "images/RogueSex/Rogue_Sex_Hole_Tight.png", 
            )    
    contains:
            #Spunk under penis
            ConditionSwitch(    
                "'anal' not in R_Spunk", Null(),  
                "P_Sprite and P_Cock != 'anal' and Speed >= 1", "images/RogueSex/Rogue_Sex_Spunk_Anal_Under.png",  
                "P_Sprite and P_Cock != 'anal' and Speed == 1", "Rogue_Anal_Spunk_Heading_Under",
                "True", "images/RogueSex/Rogue_Sex_Spunk_Anal_Closed.png",  
                )  
#    contains:
#            ConditionSwitch(
#            "R_PantiesDown and P_Cock == 'anal' and R_Panties == 'swimsuit3'", "images/RogueSex/Rogue_Sex_Swimsuit3_BottomPush.png",
#            "R_PantiesDown and P_Cock == 'anal' and R_Panties == 'zipper panties'", "images/RogueSex/RogueSexBDPantyOpenAss.png",
#            "R_PantiesDown and P_Cock == 'anal' and R_Panties == 'zipper panties open'", "images/RogueSex/RogueSexBDPantyOpenAss.png",
#            "True", Null(), 
#            ),
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(               
            "not P_Sprite or P_Cock != 'anal'", Null(),                                                                                    
            "Speed >= 3",  AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Anal_Fucking_Mask"),        
            "Speed >= 2", AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask"),
            "True", AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask"), 
            )    
    contains:
            #Spunk over penis
            ConditionSwitch(    
                "'anal' not in R_Spunk or not P_Sprite or P_Cock != 'anal' or not Speed", Null(),  
                "Speed == 1", "Rogue_Anal_Spunk_Heading_Over",
                "True", "images/RogueSex/Rogue_Sex_Spunk_Anal_Over.png",  
                )  
            
                
image Rogue_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static). 
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask") 
            
image Rogue_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading). 
    contains:
            # The background plate of her pussy
            "Rogue_Sex_Anal_Heading"
#            "images/RogueSex/Rogue_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask") 

    
image Rogue_Anal_Fucking_Mask:
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Hole_Mask.png"               

image Rogue_Anal_Open_Mask:            
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Hole_Mask.png"  
            yoffset 3

image Rogue_Sex_Anal_Heading:                
    "images/RogueSex/Rogue_Sex_Hole_Open.png"
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

image Rogue_Anal_Spunk_Heading_Over:                
    "images/RogueSex/Rogue_Sex_Spunk_Anal_Over.png"
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
image Rogue_Anal_Spunk_Heading_Under:                
    "images/RogueSex/Rogue_Sex_Spunk_Anal_Under.png"
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

image Rogue_Anal_Tip:                
    "images/RogueSex/Rogue_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
            
#End Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Anal_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Rogue_Anal_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
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
            
image Rogue_Anal_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
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
            
image Rogue_Anal_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
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
image Rogue_Hotdog_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4
            
image Rogue_Hotdog_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
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

image Rogue_Hotdog_Zero_Anim2:
        #this is Rogue's sex animation, Speed 3 (fast)
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
                
image Rogue_Hotdog_Legs_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat 

image Rogue_Footcock:   
    contains:
            subpixel True
            "Blowcock"
            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Rogue_Footcock_Static:    
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
    pos (750,230)
                
image Rogue_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Rogue_Footcock"
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
              
image Rogue_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Rogue_Footcock"
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

image Rogue_Sex_Legs_FootAnim1:            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
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
                
image Rogue_Sex_Legs_FootAnim2:            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
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
                
image Rogue_Sex_Legs_FootAnimStatic:            
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)
                


#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4
            
image Rogue_Sex_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
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
            
image Rogue_Sex_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
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
            
image Rogue_Sex_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
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

#Start Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Legs_Anim1:
        #this is the animation for Rogue's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Rogue_Sex_Legs_Anim2:            
        #this is the animation for Rogue's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat 
            
image Rogue_Sex_Legs_Anim3:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,0)
                repeat 
#End Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Rogue_Sex_Body_Static:
    contains:
            "Rogue_Sex_Body"
    pos (650,230)

image Rogue_Sex_Legs_Static:
    contains:
            "Rogue_Sex_Legs"
    pos (650,230)

image Rogue_Sex_Body_Anim1:
        #this is the animation for Rogue's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat 

image Rogue_Sex_Body_Anim2:            
        #this is the animation for Rogue's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat 

image Rogue_Sex_Body_Anim3:
        #this is the animation for Rogue's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15) 
                pause .20
                ease 1.4 pos (0,10)
                repeat 

image Rogue_Hotdog_Body_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds   
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat 

image Rogue_Sex_Body_FootAnim1:            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
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

image Rogue_Sex_Body_FootAnim2:            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
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

image Rogue_Sex_Body_FootAnimStatic:            
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)

image Rogue_Sex_Body = LiveComposite(                                                                                
        #the torso/head used in the sex pose, referenced by Rogue_SexSprite
        (1120,840),
#        (0,0), ConditionSwitch(                                                                                 #Hair underlayer, delete once this is working
#            "K_Water", Null(), 
#            "K_Hair == 'evo'", "images/RogueSex/Rogue_Sex_HairB.png",   
#            "True", Null(),                   
#            ),   
        (140,-240), "Rogue_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(                                                                                 #Body Base
            #"R_Pierce == 'barbell' and R_Tan == 'tan2'", "images/RogueSex/Rogue_Sex_T2Body_Barbell.png",
            #"R_Pierce == 'barbell' and R_Tan == 'tan3'", "images/RogueSex/Rogue_Sex_T3Body_Barbell.png",
            
            #"R_Pierce == 'barbell' and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Body_Barbell.png",   
            #"R_Pierce == 'barbell' and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Body_Barbell.png",   
            #"R_Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Barbell.png",   
            
            #"R_Pierce == 'ring' and R_Tan == 'tan2'", "images/RogueSex/Rogue_Sex_T2Body_Ring.png",
            #"R_Pierce == 'ring' and R_Tan == 'tan3'", "images/RogueSex/Rogue_Sex_T3Body_Ring.png",
            
            #"R_Pierce == 'ring' and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Body_Ring.png",   
            #"R_Pierce == 'ring' and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Body_Ring.png",   
            #"R_Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_Ring.png",   
            
            #"True and R_Tan == 'tan2'", "images/RogueSex/Rogue_Sex_T2Body.png",
            #"True and R_Tan == 'tan3'", "images/RogueSex/Rogue_Sex_T3Body.png",
            "R_Over == 'bondage'", "images/RogueSex/Rogue_Sex_Body_BinderTop.png",             
            "R_Over == 'bondage cuffs'", "images/RogueSex/Rogue_Sex_Body_ArmCuffs.png",             
            "True and R_Tan == 'tan1' and R_Over == 'armbinder'", "images/RogueSex/Rogue_t1Sex_Body_Armbinder.png",             
            "True and R_Tan == 'tan1'", "images/RogueSex/Rogue_t1Sex_Body.png",             
            "True and R_Tan == 'tan' and R_Over == 'armbinder'", "images/RogueSex/Rogue_tSex_Body_Armbinder.png",             
            "True and R_Tan == 'tan'", "images/RogueSex/Rogue_tSex_Body.png",             
            "R_Over == 'armbinder'", "images/RogueSex/Rogue_Sex_Body_Armbinder.png",             
            "True", "images/RogueSex/Rogue_Sex_Body.png",             
            ), 
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "not R_Pierce", Null(),
            "R_Over == 'bondage' or R_Over == 'bondage cuffs'", Null(),
            "R_Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Tits_Barbell.png",   
            "R_Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_Tits_Ring.png",   
            "True", Null(),             
            ),  
        (0,0), ConditionSwitch(                                                                                 #Body Base
            "not R_Pierce", Null(),
            "R_Over != 'bondage' and R_Over != 'bondage cuffs'", Null(),
            "R_Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_ArmCuffs_BarbellPierce.png",   
            "R_Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_ArmCuffs_RingPierce.png",   
            "True", Null(),             
            ),            
        (0,0), ConditionSwitch(                                                                                 #necklace
            #"R_Neck == 'gold necklace'", "images/RogueSex/Rogue_Sex_NecR_Gold.png",
            #"R_Neck == 'star necklace'", "images/RogueSex/Rogue_Sex_NecR_Star.png",
            #"R_Chest == 'orange top'", "images/RogueSex/Rogue_Sex_NecR_Orange.png",
            #"R_Chest == 'black top'", "images/RogueSex/Rogue_Sex_NecR_Black.png",
            #"R_Chest == 'leather top'", "images/RogueSex/Rogue_Sex_NecR_Leather.png",
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                                 #tanktop
            "not R_Chest", Null(),        
            #"R_Chest == 'cami'", "images/RogueSex/Rogue_Sex_Under_Cami.png",
            #"R_Chest == 'white cami'", "images/RogueSex/Rogue_Sex_Under_WhiteCami.png",
            #"R_Chest == 'sports bra'", "images/RogueSex/Rogue_Sex_Under_SportsBra.png",
            #"R_Chest == 'purple bikini bra'", "images/RogueSex/Rogue_Sex_Under_Bikini1.png",
            "R_Chest == 'SR7 tank short'", "images/RogueSex/Rogue_Sex_SR7_Tank_Short.png",
            "R_Chest == 'bra'", "images/RogueSex/Rogue_Sex_Under_Bra.png",
            #"R_Chest == 'lace bra'", "images/RogueSex/Rogue_Sex_Under_LaceBra.png",
            #"R_Chest == 'darker lace bra'", "images/RogueSex/Rogue_Sex_Under_DarkerLaceBra.png",
            #"R_Chest == 'orange top'", "images/RogueSex/Rogue_Sex_Under_Orange.png",
            #"R_Chest == 'black top'", "images/RogueSex/Rogue_Sex_Under_Black.png",
            #"R_Chest == 'leather top'", "images/RogueSex/Rogue_Sex_Under_Leather.png",
            #"R_Chest == 'swimsuit3'", "images/RogueSex/Rogue_Sex_Swimsuit3_Top.png",
            #"R_Chest == 'bustier bra' and R_PantiesDown", "images/RogueSex/RogueSexBustierBraOpen.png",
            #"R_Chest == 'bustier bra'", "images/RogueSex/RogueSexBustierBraClosed.png",
            #"R_Chest == 'bustier bra open'", "images/RogueSex/RogueSexBustierBraOpen.png",
            "True", Null(),            
            ), 
        (0,0), ConditionSwitch(
            "R_BodySuitOff and R_BodySuit != 'classic uniform damaged'", Null(),  
            "R_BodySuit == 'classic uniform'", "images/RogueSex/Rogue_Sex_XCatsuit_Top.png",
            "R_BodySuit == 'classic uniform damaged'", "images/RogueSex/Rogue_Sex_XCatsuit_Top_Dmg.png",
            "True", Null(),                     
            ),
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "R_Water", "images/RogueSex/Rogue_Sex_Water_Body.png",   
            "True", Null(),              
            ), 
#        (0,0), ConditionSwitch(                                                                                 #Wet look
#            "R_Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Barbell.png",   
#            "R_Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_Ring.png",   
#            "True", Null(),              
#            ), 
        (0,0), ConditionSwitch(                                                                         #accessories
            "R_Accessory == 'classic belt'", "images/RogueSex/Rogue_Sex_Over_XBelt.png",
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                                 #Overshirt
            "not R_Over", Null(),
            "R_Over == 'armbinder'", "images/RogueSex/RogueSexArmbinderOvershirt.png",
            "R_Over == 'classic jacket'", "images/RogueSex/Rogue_Sex_Over_XJacket.png",           
            "R_Over == 'SR7 mesh top'", "images/RogueSex/Rogue_Sex_Over_SR7_Mesh_Top.png",           
            "R_Over == 'blue dress'", "images/RogueSex/Rogue_Sex_Bluedress.png",           
            "R_Over == 'red dress'", "images/RogueSex/Rogue_Sex_Reddress.png",           
            #"R_Over == 'pink top'", "images/RogueSex/Rogue_Sex_Over_PinkShirt.png",           
            #"R_Over == 'purple shirt'", "images/RogueSex/Rogue_Sex_Over_purpleShirt.png",   
            #"R_Over == 'red shirt'", "images/RogueSex/Rogue_Sex_Over_RedShirt.png",   
            #"R_Over == 'towel'", "images/RogueSex/Rogue_Sex_Over_Towel.png",       
            #"R_Over == 'armbinder'", "images/RogueSex/RogueSexArmbinderOvershirt.png",       
            "True", Null(), 
            ),  
        (140,-240), "Rogue_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in R_Spunk", "images/RogueSex/Rogue_Sex_Spunk_Body.png",   
            "True", Null(),  
            ),  
        )

image Rogue_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Rogue_Sex_Body            
    "Rogue_HairBack"
    zoom 1.4
    anchor (0.5,0.5)   
    #rotate -10  


image Rogue_HairBack:
    LiveComposite(
        (416,610),    
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo.png",
            "True", Null(), 
            ),    
        )
#    anchor (0.6, 0.0)
#    zoom .5



image Rogue_Head_Sex:
    # The head used for the sex pose, referenced by Rogue_Sex_Body
    "Rogue_Head"
    zoom 1.4
    anchor (0.5,0.5)
    #rotate -10

image Rogue_Head:               
    LiveComposite(
        (416,610),    
#        (0,0), ConditionSwitch(
#            "K_Water", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
#            "K_Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
#            "True", Null(),
#            ),    
        (0,0), ConditionSwitch(                                                                         #head 
            #"renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Tan and R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_thead_evowet.png",
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            "R_Tan and R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_thead_evo_blush2.png",
            "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            "R_Tan and R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_thead_evo_blush.png",
            "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            "R_Tan and R_Hair == 'evo'", "images/RogueSprite/Rogue_thead_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "R_Tan", "images/RogueSprite/Rogue_thead_evo.png",
            "True", "images/RogueSprite/Rogue_head_evo.png",
            ),  
        (0,0), ConditionSwitch(                                                                         #brows
            "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "R_Brows == 'normal'", "images/RogueSprite/Rogue_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueSprite/Rogue_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueSprite/Rogue_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueSprite/Rogue_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueSprite/Rogue_brows_confused.png",
            "True", "images/RogueSprite/Rogue_brows_normal.png",
            ),
        (0,0), ConditionSwitch(  
            "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",                                                                       #Mouths        
            "R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                       #Mouths        
            "R_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                       #Mouths        
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_sucking_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_sad_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile_w.png",
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue_w.png",
            "R_Tan and 'mouth' in R_Spunk", "images/RogueSprite/Rogue_tmouth_lipbite_w.png",
            "'mouth' in R_Spunk", "images/RogueSprite/Rogue_mouth_lipbite_w.png",
            "R_Mouth == 'normal'", "images/RogueSprite/Rogue_mouth_normal.png",
            "R_Tan and R_Mouth == 'lipbite'", "images/RogueSprite/Rogue_tmouth_lipbite.png",
            "R_Mouth == 'lipbite'", "images/RogueSprite/Rogue_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueSprite/Rogue_mouth_sucking.png",            
            "R_Mouth == 'kiss'", "images/RogueSprite/Rogue_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueSprite/Rogue_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueSprite/Rogue_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueSprite/Rogue_mouth_surprised.png",            
            "R_Mouth == 'tongue'", "images/RogueSprite/Rogue_mouth_tongue.png",                
            "R_Mouth == 'grimace'", "images/RogueSprite/Rogue_mouth_grimace.png",           
            "True", "images/RogueSprite/Rogue_mouth_normal.png",
            ),            
        (0,0), "Rogue Blink",  
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),                                                                           #Eyes
        (0,0), ConditionSwitch(                                                                      
            "R_Headband", "images/RogueSprite/Rogue_Sprite_XHeadband.png",   
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                         #Hair
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_wet.png",
            "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueSprite/Rogue_hairBlackwhite_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueSprite/Rogue_hairBlondewhite_evo.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "R_Hair == 'evo'", "images/RogueSprite/Rogue_hair_evo.png",
            "True", Null(), 
            ),                           
        (0,0), ConditionSwitch(                                                                         #face spunk
            "not R_Spunk", Null(), 
            "'facial' in R_Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),
        )
#    anchor (0.6, 0.0)
#    zoom .5

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Doggy Launch/Reset
label Rogue_Doggy_Launch(Line = "massage"): 
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
    if renpy.showing("Rogue_Doggy"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Rogue  
    show Rogue_Doggy at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return
    
label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_Doggy") and not renpy.showing("Rogue_SexSprite"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ Rogue_Arms = 2      
    $ R_SpriteVer = 0
    if renpy.showing("Rogue_Doggy"):
        hide Rogue_Doggy
    else:
        hide Rogue_SexSprite
    #if R_Gag == "ballgag":
    #    $ R_Gag = 0
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    $ Speed = 0
    return




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Rogue_Sex_Launch(Line = "solo"): 
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
    if renpy.showing("Rogue_SexSprite"):
        return     
    $ P_Sprite = 1
    $ Speed = 0
    hide Rogue  
    show Rogue_SexSprite zorder 150        
#    show Rogue_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return
    
label Rogue_Sex_Reset:
    if not renpy.showing("Rogue_SexSprite"):
        return
    $ Rogue_Arms = 2     
    $ R_SpriteVer = 0
    hide Rogue_SexSprite
    if R_Over == "armbinder" or R_Over == "bondage" or R_Over == "bondage cuffs":
        "You help her remove the armbinder"
        $ R_Over = 0
#    call Set_The_Scene(Dress = 0)    
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
    
# End Rogue Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    
        
    
               
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue BJ element
#Rogue BJ Over Sprite Compositing


image Rogue_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (787,913),             
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0", At("BJ_HairBack", BJ_Starting()),                         
            "Speed == 1", At("BJ_HairBack", BJ_Licking()),                         
            "Speed == 2", At("BJ_HairBack", BJ_Heading()),                        
            "Speed == 3", At("BJ_HairBack", BJ_Sucking()),
            "Speed == 4", At("BJ_HairBack", BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # body, everything below the chin
            "Speed == 0", At("BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # her head
            "Speed == 0", At("BJ_Head", BJ_Starting()),                       
            "Speed == 1", At("BJ_Head", BJ_Licking()),                       
            "Speed == 2", At("BJ_Head", BJ_Heading()),                     
            "Speed == 3", At("BJ_Head", BJ_Sucking()),
            "Speed == 4", At("BJ_Head", BJ_Deep()), 
            "True", Null(),
            ),   
#        (0,0), Transform("images/RogueBJFace/Rogue_bj_markercard.png", alpha=(.2)),
        (0,0), ConditionSwitch(                                                                 # cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), BJ_Sucking()),
            "Speed == 4", At(AlphaMask("BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), BJ_Deep()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("BJ_Head", "BJ_MaskHeadingComposite"), BJ_Heading()),
            "True", Null(),
            ),    
        )
    zoom .55
    anchor (.5,.5)
    
image BJ_HairBack:
    ConditionSwitch(                                                                            #Hair underlay
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueBJFace/Rogue_bj_hairBlackwhite_back_wet.png",
            "R_Water and R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_back_wet.png",
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueBJFace/Rogue_bj_hairBlondewhite_back_wet.png",
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_back_wet.png",
            "R_Water and R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_back_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueBJFace/Rogue_bj_hairBlackwhite_back.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_back.png",
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueBJFace/Rogue_bj_hairBlondewhite_back.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_back.png",
            "R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_back.png",
            "True", Null(),
            ),
    
image BJ_Backdrop:                                                                        #Her Body under the head
    "Rogue"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)
    
image BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(    
        (787,913),     
        (0,0), ConditionSwitch(                                                                 #Hair back
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blackwhite'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlackwhite_back_wet.png", "BJ_Backdrop"),
            "R_Water and R_Hair == 'evo' and R_HairColor == 'black'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlack_back_wet.png", "BJ_Backdrop"),
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blondewhite'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlondewhite_back_wet.png", "BJ_Backdrop"),
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blonde'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlonde_back_wet.png", "BJ_Backdrop"),
            "R_Water and R_Hair == 'evo'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back_wet.png", "BJ_Backdrop"),
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlackwhite_back.png", "BJ_Backdrop"),
            "R_Hair == 'evo' and R_HairColor == 'black'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlack_back.png", "BJ_Backdrop"),
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlondewhite_back.png", "BJ_Backdrop"),
            "R_Hair == 'evo' and R_HairColor == 'blonde'", AlphaMask("images/RogueBJFace/Rogue_bj_hairBlonde_back.png", "BJ_Backdrop"),
            "R_Hair == 'evo'", AlphaMask("images/RogueBJFace/Rogue_bj_hair_back.png", "BJ_Backdrop"),
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                     
            "R_Tan and not Speed", "images/RogueBJFace/Rogue_tbj_face_base.png",    
            "not Speed", "images/RogueBJFace/Rogue_bj_face_base.png",    
            "R_Tan", "images/RogueBJFace/Rogue_tbj_face_base_s.png",
            "True", "images/RogueBJFace/Rogue_bj_face_base_s.png",
            ),   
        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_lickingS_ring.png", #sucking
            "Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            #"Speed == 1 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_licking_ring.png", #sucking
            "Speed == 1 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ring.png", #sucking
            "R_Tan and Speed == 2 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_tbj_mouth_licking_ring.png", #sucking
            "Speed == 2 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_licking_ring.png", #sucking
            "R_Tan and Speed == 3 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_tbj_mouth_sucking_ring.png", #sucking
            "Speed == 3 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_sucking_ring.png", #sucking
            "R_Tan and Speed == 4 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_tbj_mouth_sucking_ring.png", #deepthroat  
            "Speed == 4 and Trigger == 'blow' and R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_sucking_ring.png", #deepthroat  
            "R_Gag == 'ringgag' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            #"R_Gag == 'ringgag' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS_ring.png", #sucking
            "R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ring.png", 
            #"R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_licking_ring.png", #sucking
            "Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "R_Tan and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png", #sucking
            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
            "R_Tan and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png", #deepthroat         
            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat         
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueBJFace/Rogue_tbj_mouth_lipbiteS.png",              
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "R_Tan and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_tbj_mouth_lipbiteS.png",
            "'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
            "R_Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            "R_Tan and R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_tbj_mouth_lipbite.png",
            "R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
            "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
            "R_Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
            "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            ),       
        (316,590), ConditionSwitch(      #600               
            "Speed == 2 and not R_Gag", At("BJ_MouthHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(                                                                                 #cum for under layer
            "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png",
            "not R_Spunk or Trigger != 'blow' or 'mouth' not in R_Spunk", Null(),
#            "Speed == 2", "images/RogueBJFace/Rogue_bj_face_under_heading_cum.png", 
            "R_Tan and Speed == 3", "images/RogueBJFace/Rogue_tbj_face_under_sucking_cum.png",
            "Speed == 3", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
            "R_Tan and Speed == 4", "images/RogueBJFace/Rogue_tbj_face_under_sucking_cum.png",  
            "Speed == 4", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #cum for under layer
            #"'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png",
            #"not R_Spunk or Trigger != 'blow' or 'mouth' not in R_Spunk", Null(),
#            "Speed == 2", "images/RogueBJFace/Rogue_bj_face_under_heading_cum.png", 
            #"Speed == 3", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
            #"Speed == 4", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(                                                                 #Brows
            "R_Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "BJ Blink",                                                                #Eyes
        (0,0), ConditionSwitch(                                                                 #cum on the face
                "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png",
                "not R_Spunk or Trigger != 'blow' or 'mouth' not in R_Spunk", Null(),
#                "Speed == 2", "images/RogueBJFace/Rogue_bj_face_over_heading_cum.png", 
                "Speed == 3", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "Speed == 4", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Glasses", "images/RogueBJFace/Rogue_BJFace_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                      
            "R_Headband", "images/RogueBJFace/Rogue_BjFace_XHeadband.png",   
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(                                                                 #Hair overlay
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueBJFace/Rogue_bj_hairBlackwhite_wet.png",
            "R_Water and R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_wet.png",
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueBJFace/Rogue_bj_hairBlondewhite_wet.png",
            "R_Water and R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_wet.png",
            "R_Water and R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueBJFace/Rogue_bj_hairBlackwhite.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack.png",
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueBJFace/Rogue_bj_hairBlondewhite.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde.png",
            "R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hands overlay
            "not P_Hands", Null(),
            "(R_Water or R_Hair == 'wet') and P_Color == 'pink'", "images/RogueBJFace/Rogue_bj_Wet_HeadHands_P.png",
            "(R_Water or R_Hair == 'wet') and P_Color == 'green'", "images/RogueBJFace/Rogue_bj_Wet_HeadHands_G.png",
            "(R_Water or R_Hair == 'wet') and P_Color == 'brown'", "images/RogueBJFace/Rogue_bj_Wet_HeadHands_B.png",
            "P_Color == 'pink'", "images/RogueBJFace/Rogue_bj_HeadHands_P.png",
            "P_Color == 'green'", "images/RogueBJFace/Rogue_bj_HeadHands_G.png",
            "P_Color == 'brown'", "images/RogueBJFace/Rogue_bj_HeadHands_B.png",
            "True", Null(),
            ), 
        )


image BJ Blink:                                                                           #eyeblinks
    ConditionSwitch(
        "R_Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "R_Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "R_Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "R_Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "R_Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "R_Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "R_Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_squint.png",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    .25
    repeat

image BJ_MouthHeading:                                          #the mouth used for the heading animations
    contains:
        ConditionSwitch(
            "R_Tan", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png",
            "True", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
        ),
        anchor (0.40,0.65) 
        
image BJ_MaskHeading:                                           #the mask used for the heading image 
    contains:
        "images/RogueBJFace/Rogue_bj_facemask.png"
        anchor (0.4,0.65)    

image BJ_MaskHeadingComposite:                                  #The composite for the heading mask that goes over the face
    LiveComposite(    
        (787,913),  
        (316,590), ConditionSwitch(      #600               
            "Speed == 2", At("BJ_MaskHeading", BJ_MouthAnim()),     
            "True", Null(),
            ),  
        )
    
transform BJ_MouthAnim():                                       #The animation for the heading mouth
        subpixel True
        zoom 0.90     #small 
        block: #total time 10 down, 15 back up
            pause .40            
            easein .40 zoom 0.87
            linear .10 zoom 0.9
            easeout .45 zoom 0.70 
            pause .15                       
            easein .25 zoom 0.9
            linear .10 zoom 0.87
            easeout .30 zoom 0.9   
            pause .35
            
#            pause .15                
#            easein .4 zoom 0.87
#            linear .1 zoom 0.9
#            easeout .45 zoom 0.70 
#            pause .50                        
#            easein .25 zoom 0.9
#            linear .1 zoom 0.87
#            easeout .3 zoom 0.9  
#            pause .25
            repeat
            
image Blowcock:
    contains:
        ConditionSwitch(        
            "P_Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "P_Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",             
            "P_Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png", 
            "True", Null(),
            ),   
    contains:
        ConditionSwitch(                 
            "P_Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
            "True", Null(),
            ),       
    contains:
        ConditionSwitch(    
            "P_Spunk", "images/RogueBJFace/Zero_Cock_S.png", 
            "True", Null(),
            ),  
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)#(-175,450)
    
transform Cock_BJ_Starting():                            #The static animation for the cock
    anchor (.5,.5)
    rotate -10

transform Cock_BJ_Licking():                            #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat
        
transform Cock_BJ_Straight():                            #The static animation for the cock
    anchor (.5,.5)
    rotate 0
    
transform BJ_Licking():                                 #The licking animation for her face
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform BJ_LickingBody():                             #The licking animation for her body
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
        
transform BJ_Heading():                                 #The heading animation for her face
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 35           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat

transform BJ_HeadingBody():                             #The heading animation for her body
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 15           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
        
transform BJ_Sucking():                                 #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat
    
transform BJ_SuckingBody():                             #The sucking animation for her body
    subpixel True 
    ease 0.5 offset (0,50)  
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat
    
transform BJ_Deep():                                    #The deep animation for her face
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat
        
transform BJ_DeepBody():                                #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100   
        repeat    

transform BJ_Static():                                  #The static animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
    repeat

transform BJ_StaticBody():                              #The static animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
                                         
transform BJ_Starting():                                #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
    
transform BJ_StartingBody():                            #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Rogue_BJ_Launch(Line = 0):    # The sequence to launch the Rogue BJ animations  
    if renpy.showing("Rogue_BJ_Animation"):
        return
    
    call Rogue_Hide from _call_Rogue_Hide_2
    if Line == "L" or Line == "cum":
        show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80) 
        with dissolve
    else:
        show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140) 
        with dissolve
        
#    show Rogue:
#        pos (715,50)
#        alpha 1
#        zoom 2.5 offset (-90,140) 
#    with dissolve
        
    if Taboo and Line == "L": # Rogue gets started. . .
        if not R_Blow:
            "Rogue looks around to see if anyone can see her."
            "Rogue hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Rogue hesitantly looks around to see if anyone notices what she's doing, but then bends down and puts her lips around you,"
    elif Line == "L":    
        if not R_Blow:
            "Rogue hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Rogue bends down and begins to suck on your cock."    
            
    $ Speed = 0
    
    if Line != "cum":
        $ Trigger = "blow"
    
    show Rogue zorder RogueLayer:
        alpha 0
    show Rogue_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Rogue_BJ_Reset: # The sequence to the Rogue animations from BJ to default
    if not renpy.showing("Rogue_BJ_Animation"):
        return
    hide Rogue_BJ_Animation
    $ Speed = 0
    
#    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
#        alpha 1
#        zoom 2 offset (70,140)
#    with dissolve
    show Rogue SpriteLoc(R_SpriteLoc) zorder RogueLayer:        
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)     
    call RogueFace("sexy") from _call_RogueFace_781        
    return  
    
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


#       Face currently used for titfucking. Remove once titfucking uses new facial system


image Rogue_BJFace:
    LiveComposite(    
        (787,912),     
        (0,0), ConditionSwitch(
            "R_Tan and R_Blush and Trigger != 'blow'", "images/RogueBJFace/Rogue_tbj_face_over_blush.png",
            "R_Blush and Trigger != 'blow'", "images/RogueBJFace/Rogue_bj_face_over_blush.png",
            "Trigger != 'blow'", Null(),
            "R_Tan and Speed == 3 and R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_suckingB.png",
            "Speed == 3 and R_Blush", "images/RogueBJFace/Rogue_bj_face_over_suckingB.png",
            "R_Tan and Speed == 3 and not R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_sucking.png",
            "Speed == 3 and not R_Blush", "images/RogueBJFace/Rogue_bj_face_over_sucking.png",
            "R_Tan and Speed == 2 and R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_headingB.png",
            "Speed == 2 and R_Blush", "images/RogueBJFace/Rogue_bj_face_over_headingB.png",
            "R_Tan and Speed == 2 and not R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_heading.png",
            "Speed == 2 and not R_Blush", "images/RogueBJFace/Rogue_bj_face_over_heading.png",
            "R_Tan and Speed == 4 and R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_suckingB.png",
            "Speed == 4 and R_Blush", "images/RogueBJFace/Rogue_bj_face_over_suckingB.png",
            "R_Tan and Speed == 4 and not R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_sucking.png",
            "Speed == 4 and not R_Blush", "images/RogueBJFace/Rogue_bj_face_over_sucking.png",
            "R_Tan and R_Blush", "images/RogueBJFace/Rogue_tbj_face_over_blush.png",
            "R_Blush", "images/RogueBJFace/Rogue_bj_face_over_blush.png",
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(
            "R_Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "Rogue_BJ Blink",
        (0,0), ConditionSwitch(  
            "R_Gag == 'ringgag' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            "R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ring.png", 
            "R_Gag == 'ballgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ball.png", 
            "True", Null(),
            #"R_Gag == 'ringgag' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking  
            ),
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Glasses", "images/RogueBJFace/Rogue_BJFace_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                      
            "R_Headband", "images/RogueBJFace/Rogue_BjFace_XHeadband.png",   
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'mouth' in R_Spunk and Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_heading_cum.png", 
                "'mouth' in R_Spunk and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "'mouth' in R_Spunk and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_over.png", 
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
            "R_Hair == 'evo' and R_HairColor == 'blackwhite'", "images/RogueBJFace/Rogue_bj_hairBlackwhite.png",
            "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack.png",
            "R_Hair == 'evo' and R_HairColor == 'blondewhite'", "images/RogueBJFace/Rogue_bj_hairBlondewhite.png",
            "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde.png",
            "R_Hair == 'evo'", "images/RogueBJFace/Rogue_bj_hair.png",
            "True", Null(),
            ),              
        )

#Rogue BJ Under Sprite Compositing
image Rogue_BJChin:
    LiveComposite(
        (787,912),     
        (0,0), ConditionSwitch(
            "R_Tan", "images/RogueBJFace/Rogue_tbj_face_under.png",
            "True", "images/RogueBJFace/Rogue_bj_face_under.png",
            ),   
        (0,0), ConditionSwitch(  
            "R_Gag", Null(),
            "R_Gag == 'ringgag' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            "R_Gag == 'ringgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ring.png", 
            #"R_Gag == 'ringgag' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_tjS_ring.png", #sucking
            "R_Gag == 'ballgag'", "images/RogueBJFace/Rogue_bj_mouth_tj_ball.png", 
            "Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",
            "Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_heading.png", 
            "R_Tan == 'tan1' and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png",
            "Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
            "R_Tan == 'tan1' and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_tbj_mouth_sucking.png",           
            "Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",           
            "'mouth' in R_Spunk and R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in R_Spunk and R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprisedS.png",
            "'mouth' in R_Spunk and R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "'mouth' in R_Spunk and R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_sadS.png",
            "R_Tan and 'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueBJFace/Rogue_tbj_mouth_lipbiteS.png",              
            "'mouth' in R_Spunk and R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",              
            "'mouth' in R_Spunk and R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "R_Tan and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_tbj_mouth_lipbiteS.png",
            "'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lipbiteS.png",
            "R_Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            "R_Tan and R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_tbj_mouth_lipbite.png",
            "R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
            "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
            "R_Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
            "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            ),       
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'mouth' in R_Spunk and Speed == 2 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_heading_cum..png", 
                "'mouth' in R_Spunk and Speed == 3 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",
                "'mouth' in R_Spunk and Speed == 4 and Trigger == 'blow'", "images/RogueBJFace/Rogue_bj_face_under_sucking_cum.png",  
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                "not R_Spunk", Null(),
                "'facial' in R_Spunk", "images/RogueBJFace/Rogue_bj_facial_under.png", 
                "True", Null(),
                ),
        )

image Rogue_SelfieChin:
    LiveComposite(
        (787,912),     
        (0,0), ConditionSwitch(    
            "R_Tan", "images/RogueSelfie/Rogue_tselfie_face_under.png",
            "True", "images/RogueSelfie/Rogue_selfie_face_under.png",
            ),
        (0,0), ConditionSwitch(    
            "R_Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            "R_Tan and R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_tbj_mouth_lipbite.png",
            "R_Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
            "R_Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",            
            "R_Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
            "R_Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
            "R_Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",            
            "R_Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
            "R_Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",          
            "R_Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",    
            "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
            ),
        (0,0), ConditionSwitch(
            "R_Brows == 'normal'", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            "R_Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "R_Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "R_Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",        
            "R_Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),   
        (0,0), ConditionSwitch(
            "R_Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
            "R_Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
            "R_Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
            "R_Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
            "R_Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
            "R_Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
            "R_Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
            "R_Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
            "R_Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
            "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
            ), 
        (0,0), ConditionSwitch(                                                                                 #Collar
            "R_Glasses", "images/RogueBJFace/Rogue_BJFace_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(                                                                      
            "R_Headband", "images/RogueBJFace/Rogue_BjFace_XHeadband.png",   
            "True", Null(),
            ), 
        )

image Rogue_BJ Blink:
    ConditionSwitch(
        "R_Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        "R_Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",  
        "R_Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "R_Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "R_Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "R_Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "R_Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "R_Eyes == 'squint'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",  
        ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    .25
    repeat
    
transform Zero_BJ_Static():                            #The static animation for the cock
    anchor (.5,.5)
#    pos (180,560) #(125,300)
    rotate -10
#    pos (-25,0)

transform Zero_BJ_Sucking():                            #The sucking animation for the cock
    anchor (.5,.5)
    rotate 0

    
transform Zero_BJ_Licking():                            #The licking animation for the cock
    subpixel True
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat

image Zero_Blowcock:
    LiveComposite(                            #The compositived BJ cock
        (175,946),             
        (0,0), ConditionSwitch(        
            "P_Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "P_Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",             
            "P_Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png", 
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                 
            "P_Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
            "True", Null(),
            ),       
        (0,0), ConditionSwitch(    
            "P_Spunk", "images/RogueBJFace/Zero_Cock_Spunk.png", 
            "True", Null(),
            ),       
        )
    anchor (0.5,0.5)
    zoom 1.2
    xoffset 5

   
# and R_HairColor = 'black'
# Core Rogue Titfucking element //////////////////////////////////////////////////////////////////////                                         Core Rogue TJ element

image Rogue_TJ_Under: 
    contains:
        ConditionSwitch(
            "R_HairColor == 'blackwhite'", "images/RogueBJFace/Rogue_bj_hairBlackwhite_back.png",
            "R_HairColor == 'black'", "images/RogueBJFace/Rogue_bj_hairBlack_back.png",
            "R_HairColor == 'blondewhite'", "images/RogueBJFace/Rogue_bj_hairBlondewhite_back.png",
            "R_HairColor == 'blonde'", "images/RogueBJFace/Rogue_bj_hairBlonde_back.png",
            "True", "images/RogueBJFace/Rogue_bj_hair_back.png",
            ),

        pos (150, -560)
        zoom .95
    contains:
        ConditionSwitch(
            "R_Tan == 'tan1' and R_Over == 'bondage'", "images/RogueBJFace/Rogue_t1tj_base_Binder.png",
            "R_Tan == 'tan' and R_Over == 'bondage'", "images/RogueBJFace/Rogue_ttj_base_Binder.png",
            "R_Over == 'bondage'", "images/RogueBJFace/Rogue_tj_base_Binder.png",
            "R_Tan == 'tan1' and R_Over == 'bondage cuffs'", "images/RogueBJFace/Rogue_t1tj_base_ArmCuffs.png",
            "R_Tan == 'tan' and R_Over == 'bondage cuffs'", "images/RogueBJFace/Rogue_ttj_base_ArmCuffs.png",
            "R_Over == 'bondage cuffs'", "images/RogueBJFace/Rogue_tj_base_ArmCuffs.png",
            "R_Tan == 'tan1'", "images/RogueBJFace/Rogue_t1tj_base.png",
            "R_Tan == 'tan'", "images/RogueBJFace/Rogue_ttj_base.png",
            "True", "images/RogueBJFace/Rogue_tj_base.png",
            ),
    contains:
        ConditionSwitch( 
            "'tits' in R_Spunk", "images/RogueBJFace/Rogue_tj_spunkU.png",
            "True", Null(),
            ),
    contains:
        "Rogue_BJChin"
        pos (150, -560)
        zoom .95
    contains:
        "Rogue_BJFace" 
        pos (150, -560)
        zoom .95
    pos (-60, 200)

image Rogue_TJ_Over:     
    contains:
        ConditionSwitch( 
            "R_Tan == 'tan1' and R_Pierce == 'barbell' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_t1tj_tits_b_Binder.png", 
            "R_Tan == 'tan' and R_Pierce == 'barbell' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_ttj_tits_b_Binder.png", 
            "R_Pierce == 'barbell' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_tj_tits_b_Binder.png", 
            "R_Tan == 'tan1' and R_Pierce == 'barbell'", "images/RogueBJFace/Rogue_t1tj_tits_b.png", 
            "R_Tan == 'tan' and R_Pierce == 'barbell'", "images/RogueBJFace/Rogue_ttj_tits_b.png", 
            "R_Pierce == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_b.png", 
            "R_Tan == 'tan1' and R_Pierce == 'ring' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_t1tj_tits_r_Binder.png",
            "R_Tan == 'tan' and R_Pierce == 'ring' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_ttj_tits_r_Binder.png",
            "R_Pierce == 'ring' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_tj_tits_r_Binder.png",
            "R_Tan == 'tan1' and R_Pierce == 'ring'", "images/RogueBJFace/Rogue_t1tj_tits_r.png",
            "R_Tan == 'tan' and R_Pierce == 'ring'", "images/RogueBJFace/Rogue_ttj_tits_r.png",
            "R_Pierce == 'ring'", "images/RogueBJFace/Rogue_tj_tits_r.png",
            "R_Tan == 'tan1' and R_Pierce != 'barbell' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_t1tj_tits_Binder.png",
            "R_Tan == 'tan' and R_Pierce != 'barbell' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_ttj_tits_Binder.png",
            "R_Pierce != 'barbell' and (R_Over == 'bondage cuffs' or R_Over == 'bondage')", "images/RogueBJFace/Rogue_tj_tits_Binder.png",
            "R_Tan == 'tan1' and R_Pierce != 'barbell'", "images/RogueBJFace/Rogue_t1tj_tits.png",
            "R_Tan == 'tan' and R_Pierce != 'barbell'", "images/RogueBJFace/Rogue_ttj_tits.png",
            "R_Pierce != 'barbell'", "images/RogueBJFace/Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch( 
            "'tits' in R_Spunk", "images/RogueBJFace/Rogue_tj_spunk.png",
            "True", Null(),
            ),
    pos (-60, 200)


transform Rogue_TJ_Under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout .2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_TJ_Over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout .1 ypos 300
        easein 1.2 ypos 120
        repeat
        
transform Rogue_TJ_Under_2():
    ypos 200
    subpixel True
    block:
        ease .25 ypos 200
        ease .4 ypos 120
        ease .1 ypos 125
        repeat

transform Rogue_TJ_Over_2():
    ypos 200
    subpixel True
    block:
        ease .3 ypos 200
        ease .35 ypos 120
        ease .1 ypos 125          #high point
        repeat
        
        
transform Zero_TJ_Cock():                            #The sucking animation for the cock
    anchor (.5,.5)
    pos (440,1020) #220,1000 #(180,560)
    rotate 0
    
transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout .2 ypos 1060
        easein 1.3 ypos 1020
        repeat
        
transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease .35 ypos 1030
        ease .4 ypos 1020
#        pause .1
        repeat



image Rogue_TJ_Animation:                                                                                               #core TJ animation
    contains:
        ConditionSwitch(                                                                          # Zero cock sucking
            "not Speed", Transform("Rogue_TJ_Under"), 
            "Speed == 1", At("Rogue_TJ_Under", Rogue_TJ_Under_1()),
            "Speed >= 2", At("Rogue_TJ_Under", Rogue_TJ_Under_2()),
            "Speed", Null(),
            ),  
    
    contains:
        ConditionSwitch(                                                                          # Zero cock sucking
            "not Speed", At("Zero_Blowcock", Zero_TJ_Cock()),
            "Speed == 1", At("Zero_Blowcock", Zero_TJ_Cock_1()),
            "Speed >= 2", At("Zero_Blowcock", Zero_TJ_Cock_2()),
            "Speed", Null(),
            ),  
        
    contains:
        ConditionSwitch(                                                                          # Zero cock sucking
            "not Speed", Transform("Rogue_TJ_Over"), 
            "Speed == 1", At("Rogue_TJ_Over", Rogue_TJ_Over_1()),
            "Speed >= 2", At("Rogue_TJ_Over", Rogue_TJ_Over_2()), 
            "Speed", Null(),
            ),     
    anchor (0.6, 0.0)
    offset (-75, 250)
    zoom .55
        
label Rogue_TJ_Launch(Line = 0):    # The sequence to launch the Rogue Titfuck animations   
    if renpy.showing("Rogue_TJ_Animation"):
        return
    call Rogue_Hide from _call_Rogue_Hide_3
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50 #offset (-100,50) 
    if Taboo: # Rogue gets started. . .
         "Rogue looks around to see if anyone can see her."
    
    if R_Chest and R_Over:
        "She throws off her [R_Over] and her [R_Chest]."                
    elif R_Over:
        "She throws off her [R_Over], baring her breasts underneath."
    elif R_Chest:
        "She tugs off her [R_Chest] and throws it aside."
    $ R_Over = 0
    $ R_Chest = 0
    $ R_Arms = 0
    
    call Rogue_First_Topless from _call_Rogue_First_Topless_16                
    
    if not R_Tit and Line == "L": #first time
        if not R_Chest and not R_Over:
            "As you pull out your cock, Rogue hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and not R_Over:
            "As you pull out your cock, Rogue hesitantly places it under her [R_Chest], between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and R_Over:
            "As you pull out your cock, Rogue hesitantly places it under her [R_Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, Rogue hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L": #any other time
        if not R_Chest and not R_Over:
            "As you pull out your cock, Rogue places it between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and not R_Over:
            "As you pull out your cock, Rogue places it under her [R_Chest], between her breasts and starts to rub them up and down the shaft."
        elif R_Chest and R_Over:
            "As you pull out your cock, Rogue places it under her [R_Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, Rogue places it under her clothes, between her breasts and starts to rub them up and down the shaft."    
    else:
        "Rogue wraps her tits around your cock."
#    hide Rogue    
    show blackscreen onlayer black with dissolve
    show Rogue zorder RogueLayer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Rogue_TJ_Animation at SpriteLoc(StageRight) zorder 150 
    hide blackscreen onlayer black with dissolve
    return
    
label Rogue_TJ_Reset: # The sequence to the Rogue animations from Titfuck to default
    if not renpy.showing("Rogue_TJ_Animation"):
        return
    hide Rogue_TJ_Animation

    if R_Over == "bondage" or R_Over == "bondage cuffs":
            "You help her remove the bondage suit"
            $ R_Over = 0
    
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Rogue zorder RogueLayer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos R_SpriteLoc yoffset 0
        
    "Rogue pulls back"
    return
    

# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element

image Zero_Handcock:
    contains:
        ConditionSwitch(    # Zero cock sucking
            "P_Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "P_Color == 'brown'", "images/RogueBJFace/handcock_B.png",             
            "P_Color == 'green'", "images/RogueBJFace/handcock_G.png", 
            "P_Color != 'pink'", Null(),
            ),  
    anchor (0.5,1.0)  #1.0
    pos (200,400)#(200,400)
        
image Rogue_Hand_Under:
    ConditionSwitch(
        "R_Tan", "images/RogueBJFace/thand2.png",
        "True", "images/RogueBJFace/hand2.png",
    ),
    anchor (0.5,0.5)
    pos (0,0)
    
    
image Rogue_Hand_Over:
    ConditionSwitch(
        "R_Tan", "images/RogueBJFace/thand1.png",
        "True", "images/RogueBJFace/hand1.png",
    ),   
    anchor (0.5,0.5)
    pos (0,0)

transform Handcock_1():
    subpixel True
    rotate_pad False
    ease .5 ypos 450 rotate -2 #450
    pause 0.25
    ease 1.0 ypos 400 rotate 0 #400
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease .2 ypos 430 rotate -3 #410
    ease .5 ypos 400 rotate 0
    pause 0.1
    repeat
    
transform Rogue_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3   
    pause 0.1
    ease 0.4 ypos -100 rotate -3 
    pause 0.1
    repeat

image Rogue_HJ_Animation:  
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Rogue_Hand_Under"), 
            "Speed == 1", At("Rogue_Hand_Under", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Under", Rogue_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Rogue_Hand_Over"), 
            "Speed == 1", At("Rogue_Hand_Over", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Over", Rogue_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6
        
label Rogue_HJ_Launch(Line = 0): 
    if renpy.showing("Rogue_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Rogue_Hide from _call_Rogue_Hide_4
    $ R_Arms = 0
    $ Rogue_Arms = 1
    if Line == "L":      
        show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200 #offset (-50,200)
    else:     
        show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
        with dissolve
   
    if Taboo and Line == "L": # Rogue gets started. . .
        if not R_Hand:
            "Rogue looks around to see if anyone can see her."
            "As you pull out your cock, Rogue pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "Rogue hesitantly looks around to see if anyone notices what she's doing, but then leans over and grabs your cock,"
    elif Line == "L":    
        if not R_Hand:
            "As you pull out your cock, Rogue pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "Rogue bends down and grabs your cock."
    else:
        "Rogue bends down and grabs your cock."
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    show Rogue_HJ_Animation at SpriteLoc(R_SpriteLoc) zorder 150 with easeinbottom
    return
    
label Rogue_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Rogue_HJ_Animation"):
        return    
    $ Speed = 0
    hide Rogue_HJ_Animation
    with fade    
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        alpha 1
        zoom 1.7  xpos 700 yoffset 200
    show Rogue zorder RogueLayer:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos R_SpriteLoc yoffset 0           
    return
    
# All Reset ////////////////////////////////////////////////////////////////////////////////////
label AllReset(chr = "Rogue"): 
    if chr == "Rogue":
        if renpy.showing("Rogue_SexSprite"): 
            call Rogue_Sex_Reset from _call_Rogue_Sex_Reset
        elif renpy.showing("Rogue_Doggy"): 
            call Rogue_Doggy_Reset from _call_Rogue_Doggy_Reset_6
        elif renpy.showing("Rogue_HJ_Animation"): 
            call Rogue_HJ_Reset from _call_Rogue_HJ_Reset_3
        elif renpy.showing("Rogue_BJ_Animation"):   
            call Rogue_BJ_Reset from _call_Rogue_BJ_Reset_5
        elif renpy.showing("Rogue_TJ_Animation"):   
            call Rogue_TJ_Reset from _call_Rogue_TJ_Reset
        elif R_Loc == bg_current:
            show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
                ease .5 zoom 1 offset (0,0) anchor (0.6, 0.0)
        else:
            hide Rogue
    elif chr == "Kitty":
        if renpy.showing("Kitty_SexSprite"): 
            call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_22
        elif renpy.showing("Kitty_Doggy"): 
            call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset
        elif renpy.showing("Kitty_HJ_Animation"): 
            call Kitty_HJ_Reset from _call_Kitty_HJ_Reset_3
        elif renpy.showing("Kitty_BJ_Animation"):   
            call Kitty_BJ_Reset from _call_Kitty_BJ_Reset_2
        elif renpy.showing("Kitty_TJ_Animation"):   
            call Kitty_TJ_Reset from _call_Kitty_TJ_Reset
        elif K_Loc == bg_current:
            show Kitty_Sprite at SpriteLoc(K_SpriteLoc) zorder KittyLayer:
                ease .5 zoom 1 offset (0,0) anchor (0.5, 0.0)
        else:
            hide Kitty_Sprite
    elif chr == "Emma":
        if renpy.showing("Emma_SexSprite"): 
            call Emma_Sex_Reset from _call_Emma_Sex_Reset_30
        elif renpy.showing("Emma_Doggy"): 
            call Emma_Doggy_Reset from _call_Emma_Doggy_Reset
        elif renpy.showing("Emma_HJ_Animation"): 
            call Emma_HJ_Reset from _call_Emma_HJ_Reset_7
        elif renpy.showing("Emma_BJ_Animation"):   
            call Emma_BJ_Reset from _call_Emma_BJ_Reset_6
        elif renpy.showing("Emma_TJ_Animation"):   
            call Emma_TJ_Reset from _call_Emma_TJ_Reset_6
        elif E_Loc == bg_current:
            show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
                ease .5 zoom 1 offset (0,0) anchor (0.5, 0.0)
        else:
            hide Emma_Sprite
    return
            
            
# Interface items //////////////////////////////////////////////////////////////////////////////

transform Vibrate():
    subpixel True
    block:
        linear .5 xoffset 2
        linear .5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(                                                                                 #Base body
        (224,224),  
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA", 
            "Vibration", At("UI_VibB", Vibrate()),
            ),  
        )        

image GropeLeftBreast:    
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block: 
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.7
        xzoom -0.7
        pos (180,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block: 
            ease 1 rotate -30
            ease 1 rotate -60 
            repeat

#image GropeBreast:
image LickRightBreast:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -45 pos (150,370)            
            pause .5
            ease 1.5 rotate 30 pos (160,400)
            repeat

image LickLeftBreast:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)#(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -45 pos (260,380)#(150,370)            
            pause .5
            ease 1.5 rotate 30 pos (280,410)#(160,400)
            repeat

image GropeThigh: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
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

image GropePussy: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (220,620)
                ease .75 rotate 170 pos (220,635)   
            choice: 
                ease .5 rotate 190 pos (220,620)
                pause .25
                ease 1 rotate 170 pos (220,635)             
            repeat

image FingerPussy: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.7
        pos (230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)   
            choice:                          
                ease .5 rotate 40 pos (240,685)
                pause .5
                ease 1.75 rotate 50 pos (230,720)  
            choice:                          
                ease 2 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)  
            choice:                          
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720) 
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
            repeat
            
image Lickpussy:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.5
        xzoom -0.5
        pos (250,670)#(0.5,0.5)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easein .5 rotate -50 pos (230,650)  
            linear .5 rotate -60 pos (220,660)
            easeout 1 rotate 10 pos (250,670)
            repeat

image VibratorRightBreast: 
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

image VibratorLeftBreast: 
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
            
image VibratorPussy: 
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

image VibratorAnal: 
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
            
image VibratorPussyInsert: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        
image TestUIAnimation: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665           
            pause .25
            repeat

#Lesbian action animations.
image GirlGropeLeftBreast:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6#.7
        pos (300,400)#(300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block: 
            ease 1 rotate -40 pos (280,390)
            ease 1 rotate -20 pos (300,400)
            repeat

image GirlGropeRightBreast:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (160,380) #(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat

image GirlGropeThigh: 
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

image GirlGropePussy: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (230,615)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (225,620)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
            choice: #Fast stroke
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
            repeat

image GirlFingerPussy: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (230,630)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (230,635)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
            choice: #Fast stroke
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
            repeat
        
# ////   Etc.   ////////////////////////////////////////////////

image Zero_Chibicock:
    LiveComposite(                            #The compositived Chibi UI cock
        (225,350),             
        (0,0), ConditionSwitch(        
            "P_Color == 'pink'", "images/Chibi_Cock_P.png",
            "P_Color == 'brown'", "images/Chibi_Cock_B.png",             
            "P_Color == 'green'", "images/Chibi_Cock_G.png", 
            "True", Null(),
            ),   
#        (0,0), ConditionSwitch(                 
#            "P_Wet", "images/RogueBJFace/Zero_Cock_Wet.png", 
#            "True", Null(),
#            ),       
#        (0,0), ConditionSwitch(    
#            "P_Spunk", "images/RogueBJFace/Zero_Cock_Spunk.png", 
#            "True", Null(),
#            ),       
        )
    anchor (0.5,0.5)

image Chibi_Null: 
    #The Blank Chibi-cock
    contains:
        "Zero_Chibicock"  
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0 
        xzoom 1 
    pos (75,675)
    zoom 0.5
    
image Chibi_Jackin: 
    #the jackin it chibi cock
    contains:
        "Zero_Chibicock"   
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1 
    contains:
        subpixel True
        "images/Chibi_Hand_M.png"   
        pos (-10,-80)
        anchor (0.5,0.5)
        rotate 20
        block:
                ease .3 rotate -10 pos (0,50)
                ease .7 rotate 20 pos (-10,-80)
                repeat
    pos (75,675)
    zoom 0.5
            
image Chibi_Handy: 
    #the girl handy chibicock
    contains:
        "Zero_Chibicock"  
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0    
        xzoom 1 
    contains:
        subpixel True
        "images/Chibi_Hand_G.png"   
        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
                ease .3 rotate 0 pos (10,10)
                ease .7 rotate -10 pos (0,-130)
                repeat
    pos (75,675)
    zoom 0.5

image Chibi_Mouth_Mask:
    "images/Chibi_Mouth_Mask.png"
    anchor (0.5,0.5)
   
image Chibi_Mouth_Emma:
    "images/Chibi_Mouth_E.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Rogue:
    "images/Chibi_Mouth_R.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Kitty:
    "images/Chibi_Mouth_K.png"
    anchor (0.5,0.5)

image Chibi_Sucking:
    # The core sucking image
    contains:
        "Chibi_SuckingB" 
    pos (75,675)
    
image Chibi_SuckingB:
    #The composited Chibi UI cock
    LiveComposite(
        (225,350),             
        (0,0), ConditionSwitch(        
            "Partner == 'Rogue'", "Chibi_Mouth_Rogue",             
            "Partner == 'Kitty'", "Chibi_Mouth_Kitty", 
            "Partner == 'Emma'", "Chibi_Mouth_Emma",
            "True", "Chibi_Mouth_Kitty"
            ),   
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_Mouth_Mask") 
        )      
    subpixel True
    pos (7,0) #top
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout .25 rotate 0 pos (2,48) xzoom 1 #middle
        easein .25 rotate 0 pos (6,92) xzoom 1 #bottom
        easeout .5 rotate 0 pos (2,48) xzoom 1 #middle
        easein .5 rotate 0 pos (5,0) xzoom 0.71 #top
        repeat

image Chibi_Sucking_Cock:
    #The animation for the cock used in the sucking cock animation
    contains:
        subpixel True
        "Zero_Chibicock"     
        pos (100,175) #top
        xzoom 1.5
        anchor (0.5,0.5)
#        alpha 0.5
        rotate 0
        block:
            easeout .25 rotate 0 pos (110,80) xzoom 1 #middle
            easein .25 rotate 0 pos (100,-10) xzoom 1 #bottom
            easeout .5 rotate 0 pos (110,80) xzoom 1 #middle
            easein .5 rotate 0 pos (100,175) xzoom 1.5 #top
            repeat


#>>>>>>>>>>

image Chibi_UI:
    # The basic chibi-UI image that is called 
    contains:
        ConditionSwitch(      
            "Trigger2 == 'jackin'", "Chibi_Jackin",
            "Trigger3 == 'hand' or Trigger5 == 'hand'", "Chibi_Handy",             
            "Trigger5 == 'blow'", "Chibi_Sucking", 
            "True", "Chibi_Null", 
            )
#    anchor (0.5,0.5)
#    pos (75,675)

label R_Kissing_Launch(T = Trigger):    
    call Rogue_Hide from _call_Rogue_Hide_5
    $ Trigger = T
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer
    show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
        ease 0.5  zoom 2
    return

label R_Kissing_Smooch:   
    call RogueFace("kiss") from _call_RogueFace_782  
    show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
        ease 0.5 xpos StageCenter zoom 2
        pause 1
        ease 0.5 xpos R_SpriteLoc zoom 1        
    call RogueFace("sexy") from _call_RogueFace_783  
    return
    
label R_Breasts_Launch(T = Trigger):    
    call Rogue_Hide from _call_Rogue_Hide_6
    $ Trigger = T
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        ease 0.5 pos (700,-50) zoom 2 #offset (-100,-200)
    return
        
label R_Pussy_Launch(T = Trigger):
    call Rogue_Hide from _call_Rogue_Hide_7    
    $ Trigger = T
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        ease 0.5 pos (700,-400) zoom 2 #ease 0.5 offset (-100,-550) zoom 2
    return
        
label R_Pos_Reset(Pose = 0):
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        ease .5 offset (0,0) anchor (0.6, 0.0) zoom 1   
    show Rogue at SpriteLoc(R_SpriteLoc) zorder RogueLayer:
        offset (0,0) 
        anchor (0.6, 0.0)
        zoom 1  
    $ Trigger = Pose
    return
    
label Rogue_Hide:
    if renpy.showing("Rogue_Doggy") or renpy.showing("Rogue_SexSprite"):
        call Rogue_Doggy_Reset from _call_Rogue_Doggy_Reset_7
    hide Rogue_Doggy       
    hide Rogue_HJ_Animation
    hide Rogue_BJ_Animation
    hide Rogue_TJ_Animation 
    return
    
image Cellphone:
    "images/Cellphone.png"
    xoffset 0 #-250
    yoffset 100
