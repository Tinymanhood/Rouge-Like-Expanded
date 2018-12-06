# Basic character Sprites
image Mystique_Blue_Sprite:
    LiveComposite(
        (480,960),
        #  (0,0), ConditionSwitch(
            ## Overhsirt backing
        # #     "R_Over == 'mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_mesh1.png",
        # #     "R_Over == 'mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_mesh2.png",
        # #     "R_Over == 'white mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_whitemesh1.png",
        # #     "R_Over == 'white mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_whitemesh2.png",
        # #     "R_Over == 'blue mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_bluemesh1.png",
        # #     "R_Over == 'blue mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_bluemesh2.png",
        # #     "R_Over == 'red mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_redmesh1.png",
        # #     "R_Over == 'red mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_redmesh2.png",
        # #     "R_Over == 'yellow mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_yellowmesh1.png",
        # #     "R_Over == 'yellow mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_yellowmesh2.png",
        # #     "R_Over == 'black mesh top' and Rogue_Arms == 1", "images/RogueSprite/Rogue_under_blackmesh1.png",
        # #     "R_Over == 'black mesh top' and Rogue_Arms == 2", "images/RogueSprite/Rogue_under_blackmesh2.png",  
        # #     "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
        # #     "R_Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
        # #     "R_Over == 'blue hoodie'", "images/RogueSprite/Rogue_over_bhoodieB.png",
        # #     "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodieB.png",
        # #     "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodieB.png",
        #     "newgirl['Mystique'].Over == 'black hoodie'", "images/MystiqueSprite/Mystique_over_dhoodieB.png",
        # #     "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodieB.png",
        #     "True", Null(), 
        #     ),     
        (0,0), ConditionSwitch(
            ## Body 
            # "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1body_bare.png",
            # "R_Tan == 'tan'", "images/RogueSprite/Rogue_tbody_bare.png",
            "True", "images/MystiqueSprite/Mystique_body_bare.png",         
            ),  
        # (0,0), ConditionSwitch(
            ## Body 
        #     "R_Pubes and R_HairColor == 'black'", "images/RogueSprite/Rogue_bodyhaired_pubesblack.png",
        #     "R_Pubes and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_bodyhaired_pubesblonde.png",
        #     #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
        #     #"R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
        #     #"R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
        #     "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_pubes.png",   
        #     "True", Null(),         
        #     ),  
        (0,0), ConditionSwitch(    
         ## Body     
            #"R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",   
            #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",  
            # "newgirl['Mystique'].Pierce == 'ring'", "images/RogueSprite/Rogue_body_piercing_ring.png",            
            # "newgirl['Mystique'].Pierce == 'barbell'", "images/RogueSprite/Rogue_body_piercing_barbell.png",
            #"R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", Null(),         
            ),   
        #(0,0), ConditionSwitch(
            ## Body 
        #    "R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
        #    "R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
        #    "R_Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",            
        #    "R_Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
        #    "R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
        #    "True", "images/RogueSprite/Rogue_body_bare.png",         
        #    ),              
        # (0,0), ConditionSwitch(
            #pants backing/hose    
        #     "R_Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",     
        #     "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_pantsback.png", 
        #     "True", Null(), 
        #     ),
        (0,0), ConditionSwitch(
            ## Panties            
            "not newgirl['Mystique'].Panties", Null(),
            "newgirl['Mystique'].PantiesDown", Null(),      
            # "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", Null(),
            # "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",             
            # "R_Panties == 'shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
            # "R_Panties == 'red shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_down_wet.png",
            # "R_Panties == 'blue shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_down_wet.png",
            # "R_Panties == 'shorts' and R_PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",
            # "R_Panties == 'red shorts' and R_PantiesDown", "images/RogueSprite/Rogue_ryshorts_down.png",
            # "R_Panties == 'blue shorts' and R_PantiesDown", "images/RogueSprite/Rogue_byshorts_down.png",  
            # "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",
            # "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_wet.png",
            # "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_wet.png",          
            # "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
            # "R_Panties == 'red shorts'", "images/RogueSprite/Rogue_ryshorts.png",
            # "R_Panties == 'blue shorts'", "images/RogueSprite/Rogue_byshorts.png",
            # "R_Panties == 'green panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
            # "R_Panties == 'green panties' and R_PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
            # "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
            # "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
            # "R_Panties == 'black large panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_down_wet.png",
            # "R_Panties == 'black large panties' and R_PantiesDown", "images/RogueSprite/Rogue_undiesBlack_down.png",  
            # "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_wet.png",          
            # "R_Panties == 'black large panties'", "images/RogueSprite/Rogue_undiesBlack.png",
            # "R_Panties == 'lace panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            # "R_Panties == 'black panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            # "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
            "newgirl['Mystique'].Panties == 'yellow bikini'", "images/MystiqueSprite/Mystique_Panty_BikiniYellow.png",      
            "newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueSprite/Mystique_Panty_LacedPantiesBlack.png",      
            "newgirl['Mystique'].Panties == 'black lingerie'", "images/MystiqueSprite/Mystique_Panty_LacedPantiesBlack.png",      
            "True", "images/MystiqueSprite/Mystique_Panty_LacedPantiesBlack.png",            
            ),
        (0,0), ConditionSwitch(
            ## Full hose/tights              
            #"R_PantiesDown", Null(), 
            "newgirl['Mystique'].Hose == 'stockings'", "images/MystiqueSprite/Mystique_Legs_LacedStockingsBlack.png",                  
            # "R_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            # "R_Hose == 'fishnet'", "images/RogueSprite/Rogue_hose_fishnet.png",       
            # "R_Hose == 'tights' and R_Wet", "images/RogueSprite/Rogue_tights_wet.png",
            # "R_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            # "R_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            # "R_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
            ## Panties            
            "not newgirl['Mystique'].Panties", Null(),
            "newgirl['Mystique'].Panties == 'black lingerie'", "images/MystiqueSprite/Mystique_Waist_LacedBeltBlack.png",      
            "True", Null(),            
            ),
        (0,0), ConditionSwitch(
            ## Arms and gloves
            #"newgirl['Mystique'].Girl_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "newgirl['Mystique'].Girl_Arms == 1", "images/MystiqueSprite/Mystique_arms1b_bare.png",                                                              #No gloves, no collar
            #"R_Arms == 'gloved'", "images/MystiqueSprite/Mystique_arms2b_gloved.png",                                                         #Gloved, no collar
            "True", "images/MystiqueSprite/Mystique_arms1b_bare.png",                                                                         #No gloves, no collar
            #"True", "images/MystiqueSprite/Mystique_arms2b_bare.png",                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(
            # Chest layer
            #"newgirl['Mystique'].Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            #"newgirl['Mystique'].Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "True", "images/MystiqueSprite/Mystique_chest_bare.png",     
            ),   
        (0,0), ConditionSwitch(
            # Chest clothes layer
            # "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            # "R_Chest == 'tank short'", "images/RogueSprite/Rogue_chest_tankshort.png",
            # "R_Chest == 'slut tank short'", "images/RogueSprite/Rogue_chest_tankshort_slut.png",
            # "Rogue_Arms == 1 and R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            # "R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            # "Rogue_Arms == 1 and R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            # "R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            # "R_Chest == 'tape'", "images/RogueSprite/Rogue_chest_tape.png",
            # "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            # "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
            # "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
            # "R_Chest == 'blue sports bra'", "images/RogueSprite/Rogue_chest_bysportsbra.png",
            # "R_Chest == 'red sports bra'", "images/RogueSprite/Rogue_chest_rysportsbra.png",
            # "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
            # "R_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            #"newgirl['Mystique'].Chest == 'slut short top'", "images/MystiqueSprite/Mystique_chest_tankshort_slut.png",
            #"newgirl['Mystique'].Chest == 'short top'", "images/MystiqueSprite/Mystique_chest_tankshort.png",
            "newgirl['Mystique'].Chest == 'workout top'", "images/MystiqueSprite/Mystique_Legs_WorkoutTopTeal.png",
            "newgirl['Mystique'].Chest == 'bra'", "images/MystiqueSprite/Mystique_Chest_LacedBraBlack.png",
            "newgirl['Mystique'].Chest == 'black bra'", "images/MystiqueSprite/Mystique_Chest_LacedBraBlack.png",
            "newgirl['Mystique'].Chest == 'yellow bikini'", "images/MystiqueSprite/Mystique_Chest_BikiniYellow.png",
            "newgirl['Mystique'].Chest == 'top'", "images/MystiqueSprite/Mystique_Chest_TopBlack.png",
            "True", Null(),               
            ), 
        
        # (0,0), ConditionSwitch(  
        #     "R_Chest == 'swimsuit1' or R_Panties == 'swimsuit1'", "images/RogueSprite/Rogue_Swimsuit1.png",
        #     "R_Chest == 'swimsuit2' or R_Panties == 'swimsuit2'", "images/RogueSprite/Rogue_Swimsuit2.png",
        #     "True", Null(),
        #     ),
        (0,0), ConditionSwitch(
            ## Personal Wetness            
            "not newgirl['Mystique'].Wet", Null(),
            "newgirl['Mystique'].Legs and newgirl['Mystique'].Wet <= 1", Null(),
            "newgirl['Mystique'].Legs", "images/MystiqueSprite/Mystique_wet.png",
            "newgirl['Mystique'].Wet == 1", "images/MystiqueSprite/Mystique_wet.png",
            "True", "images/MystiqueSprite/Mystique_wet2.png",       #R_Wet >1
            ),  
        (0,0), ConditionSwitch(
            ## Pants and Skirts
            "newgirl['Mystique'].Upskirt", Null(),
            # "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            # "R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            # "R_Legs == 'skirt' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            # "R_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            # "R_Legs == 'skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_up.png",
            # "R_Legs == 'skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort.png",  
            # "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Up.png",
            # "R_Legs == 'cheerleader skirt'", "images/RogueSprite/Rogue_Cheerleader_Skirt.png",
            # "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short.png",
            # "R_Legs == 'cheerleader skirtshort'", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short_Up.png",            
            "newgirl['Mystique'].Legs == 'workout pants'", "images/MystiqueSprite/Mystique_Legs_WorkoutPantsTeal.png",
            "newgirl['Mystique'].Legs == 'black skirt'", "images/MystiqueSprite/Mystique_Legs_TeacherSkirtBlack.png",
            "newgirl['Mystique'].Legs == 'black skirt'", "images/MystiqueSprite/Mystique_Legs_TeacherSkirtGrey.png",
            "newgirl['Mystique'].Legs == 'split skirt'", "images/MystiqueSprite/Mystique_Legs_SplitSkirtBlack.png",
            "True", Null(),   
            ),

        # (0,0), ConditionSwitch(
            ## Arms and gloves
        #     "newgirl['Mystique'].Girl_Arms == 1", Null(),                                                              #No gloves, no collar
        #     #"R_Arms == 'gloved' and R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved_.png",                           #Gloves and collar 
        #     #"R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms2b_gloved_.png",                                                         #Gloved, no collar
        #     #"R_Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare_.png",                                                    #No gloves, collar
        #     "True", "images/MystiqueSprite/Mystique_arms2b_bare_.png",  
        #     ), 
                          
        # (0,0), ConditionSwitch(
            ## Water
        #     "R_Water and Rogue_Arms == 1", "images/RogueSprite/Rogue_body_wet1.png",
        #     "R_Water", "images/RogueSprite/Rogue_body_wet2.png",
        #     "True", Null(),                 
        #     ),
        # (0,0), ConditionSwitch(
            ## Soap
        #     "R_Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
        #     "True", Null(),                 
        #     ),
        (0,0), ConditionSwitch(
            ## Overshirt layer
        #     "Rogue_Arms == 1 and R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie1.png",
        #     "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie2.png",
        #     "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie2.png",
            "newgirl['Mystique'].Over == 'workout jacket'", "images/MystiqueSprite/Mystique_Over_WorkoutJacket.png",
            "newgirl['Mystique'].Over == 'lavender shirt'", "images/MystiqueSprite/Mystique_Chest_ShirtLavender.png",
            "newgirl['Mystique'].Over == 'red shirt'", "images/MystiqueSprite/Mystique_Chest_ShirtRed.png",
        #     "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie2.png",
        #     "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
        #     "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",              
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
            ## Head 
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/MystiqueSprite/Mystique_head_base.png",
            ),             
        (0,0), ConditionSwitch(
            ## Brows
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
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
        (0,0), ConditionSwitch(
            ## Mouths
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",
            # "R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",
            # "R_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",
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
        (0,0), "Mystique Blink",  
        (0,0), ConditionSwitch(
            ## Collar
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            "newgirl['Mystique'].Glasses", "images/MystiqueSprite/Mystique_head_glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),     
        (0,0), ConditionSwitch(
            ## Hair
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSprite/Mystique_hair_basic.png",
            "True", Null(), 
            ), 
        (0,0), ConditionSwitch(
            ## Hair
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSprite/Mystique_Head_HairGem.png",
            "True", Null(), 
            ),                           
        (0,0), ConditionSwitch(
            ## Hand spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'hand' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Girl_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
            ## Face spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            ## Belly spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),               
        (0,0), ConditionSwitch(
            ## Props
            "not newgirl['Mystique'].Held or newgirl['Mystique'].Girl_Arms != 2", Null(), 
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(), 
            ),        
        (0,0), ConditionSwitch(
            ## UI tool for When Mystique is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_M",
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
            ## UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Mystique'", Null(), 
            ## This doesn't activate unless Mystique is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_M",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                          
            ## UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_M",
            "Trigger == 'fondle pussy'", "GropePussy_M",
            "Trigger == 'lick pussy'", "Lickpussy_M",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
            ## UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",        
            ## When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",            
            ## When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",       
            ## When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),                                              
            ## When both triggers are the same, do nothing  
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",  
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy_M",
            "Trigger2 == 'lick pussy'", "Lickpussy_M",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
            ## UI tool for Trigger4(Threesome) actions (ie Kitty's hand on her)
            "not Trigger4 or Ch_Focus != 'Mystique'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_M",            
            "Trigger4 == 'lick pussy'", "Lickpussy_M",
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
            ## UI tool for Trigger3(lesbian) actions (ie Kitty's hand on her when Mystique is secondary)
            "not Trigger3 or Ch_Focus == 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_M",            
            "Trigger3 == 'lick pussy'", "Lickpussy_M",
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
    
image Mystique Blink:
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", "images/MystiqueSprite/Mystique_eyes_sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/MystiqueSprite/Mystique_eyes_side.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/MystiqueSprite/Mystique_eyes_surprised.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/MystiqueSprite/Mystique_eyes_normal.png",    
    "newgirl['Mystique'].Eyes == 'stunned'", "images/MystiqueSprite/Mystique_eyes_stunned.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/MystiqueSprite/Mystique_eyes_down.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/MystiqueSprite/Mystique_eyes_closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/MystiqueSprite/Mystique_eyes_manic.png",
    "newgirl['Mystique'].Eyes == 'squint'", "Mystique_Squint",
    "True", "images/MystiqueSprite/Mystique_eyes_normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/MystiqueSprite/Mystique_eyes_closed.png"
    .25
    repeat                

image Mystique_Squint:
    "images/MystiqueSprite/Mystique_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/MystiqueSprite/Mystique_eyes_squint.png"
    .25
    repeat  
           
# Basic character Sprites
image Mystique_Raven_Sprite:
    LiveComposite(
        (480,960),    
        (0,0), ConditionSwitch(
         ## Body 
            # "R_Tan == 'tan1'", "images/RogueSprite/Rogue_t1body_bare.png",
            # "R_Tan == 'tan'", "images/RogueSprite/Rogue_tbody_bare.png",
            "True", "images/RavenSprite/Raven_Sprite_body_bare.png",         
            ),   
        (0,0), ConditionSwitch(
         ## Body 
            #"R_Pubes and R_Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            #"R_Pubes and R_Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            # "newgirl['Mystique'].Pierce == 'ring'", "images/RogueSprite/Rogue_body_piercing_ring.png",            
            # "newgirl['Mystique'].Pierce == 'barbell'", "images/RogueSprite/Rogue_body_piercing_barbell.png",
            #"R_Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",   
            "True", Null(),         
            ),   
        (0,0), ConditionSwitch(
         ## Panties            
            "not newgirl['Mystique'].Panties", Null(),
            "newgirl['Mystique'].PantiesDown", Null(),      
            # "R_Panties == 'swimsuit1' or R_Panties == 'swimsuit2'", Null(),
            # "R_Legs == 'pants' and not R_Upskirt", "images/RogueSprite/Rogue_panties.png",             
            # "R_Panties == 'shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_shorts_down_wet.png",
            # "R_Panties == 'red shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_down_wet.png",
            # "R_Panties == 'blue shorts' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_down_wet.png",
            # "R_Panties == 'shorts' and R_PantiesDown", "images/RogueSprite/Rogue_shorts_down.png",
            # "R_Panties == 'red shorts' and R_PantiesDown", "images/RogueSprite/Rogue_ryshorts_down.png",
            # "R_Panties == 'blue shorts' and R_PantiesDown", "images/RogueSprite/Rogue_byshorts_down.png",  
            # "R_Panties == 'shorts' and R_Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",
            # "R_Panties == 'red shorts' and R_Wet > 1", "images/RogueSprite/Rogue_ryshorts_wet.png",
            # "R_Panties == 'blue shorts' and R_Wet > 1", "images/RogueSprite/Rogue_byshorts_wet.png",          
            # "R_Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
            # "R_Panties == 'red shorts'", "images/RogueSprite/Rogue_ryshorts.png",
            # "R_Panties == 'blue shorts'", "images/RogueSprite/Rogue_byshorts.png",
            # "R_Panties == 'green panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undies_down_wet.png",
            # "R_Panties == 'green panties' and R_PantiesDown", "images/RogueSprite/Rogue_undies_down.png",  
            # "R_Panties == 'green panties' and R_Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",          
            # "R_Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
            # "R_Panties == 'black large panties' and R_PantiesDown and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_down_wet.png",
            # "R_Panties == 'black large panties' and R_PantiesDown", "images/RogueSprite/Rogue_undiesBlack_down.png",  
            # "R_Panties == 'black large panties' and R_Wet > 1", "images/RogueSprite/Rogue_undiesBlack_wet.png",          
            # "R_Panties == 'black large panties'", "images/RogueSprite/Rogue_undiesBlack.png",
            # "R_Panties == 'lace panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            # "R_Panties == 'black panties' and R_PantiesDown", "images/RogueSprite/Rogue_panties_down.png",      
            # "R_Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",         
            "newgirl['Mystique'].Panties == 'yellow bikini'", "images/MystiqueSprite/Mystique_Panty_BikiniYellow.png",      
            "newgirl['Mystique'].Panties == 'black panties'", "images/MystiqueSprite/Mystique_Panty_LacedPantiesBlack.png",      
            "newgirl['Mystique'].Panties == 'black lingerie'", "images/MystiqueSprite/Mystique_Panty_LacedPantiesBlack.png",      
            "True", "images/MystiqueSprite/Mystique_Panty_LacedPantiesBlack.png",            
            ),
        (0,0), ConditionSwitch(
         ## Full hose/tights              
            #"R_PantiesDown", Null(), 
            "newgirl['Mystique'].Hose == 'stockings'", "images/MystiqueSprite/Mystique_Legs_LacedStockingsBlack.png",                  
            # "R_Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",       
            # "R_Hose == 'fishnet'", "images/RogueSprite/Rogue_hose_fishnet.png",       
            # "R_Hose == 'tights' and R_Wet", "images/RogueSprite/Rogue_tights_wet.png",
            # "R_Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            # "R_Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png", 
            # "R_Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",   
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
         ## Panties            
            "not newgirl['Mystique'].Panties", Null(),
            "newgirl['Mystique'].Panties == 'black lingerie'", "images/MystiqueSprite/Mystique_Waist_LacedBeltBlack.png",      
            "True", Null(),            
            ),
        (0,0), ConditionSwitch(
         ## Arms and gloves
            #"newgirl['Mystique'].Girl_Arms == 1 and R_Arms == 'gloved'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "newgirl['Mystique'].Girl_Arms == 1", "images/RavenSprite/Raven_Sprite_Arms_Arms1.png",                                                              #No gloves, no collar
            #"R_Arms == 'gloved'", "images/RavenSprite/Raven_arms2b_gloved.png",                                                         #Gloved, no collar
            "True", "images/RavenSprite/Raven_Sprite_Arms_Arms1.png",                                                                         #No gloves, no collar
            #"True", "images/MystiqueSprite/Mystique_arms2b_bare.png",                                                                         #No gloves, no collar
            ), 
        (0,0), ConditionSwitch(
         ## Chest layer
            #"newgirl['Mystique'].Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",            
            #"newgirl['Mystique'].Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",      
            "True", "images/RavenSprite/Raven_Sprite_Chest_Bare.png",     
            ),   
        (0,0), ConditionSwitch(
         ## Chest clothes layer
            # "R_Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
            # "R_Chest == 'tank short'", "images/RogueSprite/Rogue_chest_tankshort.png",
            # "R_Chest == 'slut tank short'", "images/RogueSprite/Rogue_chest_tankshort_slut.png",
            # "Rogue_Arms == 1 and R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms1.png",
            # "R_Chest == 'green crop top'", "images/RogueSprite/Rogue_Sprite_Green_Crop_Top_Arms2.png",
            # "Rogue_Arms == 1 and R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms1.png",
            # "R_Chest == 'black crop top'", "images/RogueSprite/Rogue_Sprite_Black_Crop_Top_Arms2.png",
            # "R_Chest == 'tape'", "images/RogueSprite/Rogue_chest_tape.png",
            # "R_Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",            
            # "R_Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",                         
            # "R_Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
            # "R_Chest == 'blue sports bra'", "images/RogueSprite/Rogue_chest_bysportsbra.png",
            # "R_Chest == 'red sports bra'", "images/RogueSprite/Rogue_chest_rysportsbra.png",
            # "R_Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",  
            # "R_Chest == 'cheerleader'", "images/RogueSprite/Rogue_Cheerleader_Outfit.png",
            #"newgirl['Mystique'].Chest == 'slut short top'", "images/MystiqueSprite/Mystique_chest_tankshort_slut.png",
            #"newgirl['Mystique'].Chest == 'short top'", "images/MystiqueSprite/Mystique_chest_tankshort.png",
            "newgirl['Mystique'].Chest == 'workout top'", "images/MystiqueSprite/Mystique_Legs_WorkoutTopTeal.png",
            "newgirl['Mystique'].Chest == 'bra'", "images/MystiqueSprite/Mystique_Chest_LacedBraBlack.png",
            "newgirl['Mystique'].Chest == 'black bra'", "images/MystiqueSprite/Mystique_Chest_LacedBraBlack.png",
            "newgirl['Mystique'].Chest == 'yellow bikini'", "images/MystiqueSprite/Mystique_Chest_BikiniYellow.png",
            "newgirl['Mystique'].Chest == 'top'", "images/MystiqueSprite/Mystique_Chest_TopBlack.png",
            "True", Null(),               
            ), 
        (0,0), ConditionSwitch(                                                                         #Personal Wetness            
            "not newgirl['Mystique'].Wet", Null(),
            "newgirl['Mystique'].Legs and newgirl['Mystique'].Wet <= 1", Null(),
            "newgirl['Mystique'].Legs", "images/MystiqueSprite/Mystique_wet.png",
            "newgirl['Mystique'].Wet == 1", "images/MystiqueSprite/Mystique_wet.png",
            "True", "images/MystiqueSprite/Mystique_wet2.png",       #R_Wet >1
            ),  
        (0,0), ConditionSwitch(                                                                         #Pants and Skirts
            "newgirl['Mystique'].Upskirt", Null(),
            # "R_Legs == 'pants' and R_Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png", 
            # "R_Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",          
            # "R_Legs == 'skirt' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            # "R_Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            # "R_Legs == 'skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_legs_skirtshort_up.png",
            # "R_Legs == 'skirtshort'", "images/RogueSprite/Rogue_legs_skirtshort.png",  
            # "R_Legs == 'cheerleader skirt' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Up.png",
            # "R_Legs == 'cheerleader skirt'", "images/RogueSprite/Rogue_Cheerleader_Skirt.png",
            # "R_Legs == 'cheerleader skirtshort' and R_Upskirt", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short.png",
            # "R_Legs == 'cheerleader skirtshort'", "images/RogueSprite/Rogue_Cheerleader_Skirt_Short_Up.png",            
            "newgirl['Mystique'].Legs == 'workout pants'", "images/MystiqueSprite/Mystique_Legs_WorkoutPantsTeal.png",
            "newgirl['Mystique'].Legs == 'black skirt'", "images/MystiqueSprite/Mystique_Legs_TeacherSkirtBlack.png",
            "newgirl['Mystique'].Legs == 'black skirt'", "images/MystiqueSprite/Mystique_Legs_TeacherSkirtGrey.png",
            "newgirl['Mystique'].Legs == 'split skirt'", "images/MystiqueSprite/Mystique_Legs_SplitSkirtBlack.png",
            "True", Null(),   
            ),
        (0,0), ConditionSwitch(
         ## Overshirt layer
        #     "Rogue_Arms == 1 and R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie1.png",
        #     "Rogue_Arms == 1 and R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie1.png",
        #     "R_Over == 'red hoodie'", "images/RogueSprite/Rogue_over_rhoodie2.png",
        #     "R_Over == 'yellow hoodie'", "images/RogueSprite/Rogue_over_yhoodie2.png",
            "newgirl['Mystique'].Over == 'workout jacket'", "images/MystiqueSprite/Mystique_Over_WorkoutJacket.png",
            "newgirl['Mystique'].Over == 'lavender shirt'", "images/MystiqueSprite/Mystique_Chest_ShirtLavender.png",
            "newgirl['Mystique'].Over == 'red shirt'", "images/MystiqueSprite/Mystique_Chest_ShirtRed.png",
        #     "R_Over == 'white hoodie'", "images/RogueSprite/Rogue_over_whoodie2.png",
        #     "R_Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
        #     "R_Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",              
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
         ## Head 
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/RavenSprite/Raven_Sprite_Head.png",
            ),             
        (0,0), ConditionSwitch(
         ## Brows
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            # "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            # "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            # "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            # "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/RavenSprite/Raven_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/RavenSprite/Raven_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/RavenSprite/Raven_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/RavenSprite/Raven_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/RavenSprite/Raven_brows_confused.png",
            "True", "images/RavenSprite/Raven_brows_normal.png",
            ),
        (0,0), ConditionSwitch(
         ## Mouths
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "'mouth' in R_Spunk and R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag_w.png",                                                                         
            # "R_Gag == 'ringgag'", "images/RogueSprite/Rogue_mouth_ringgag.png",                                                                              
            # "R_Gag == 'ballgag'", "images/RogueSprite/Rogue_mouth_Ballgag.png",                                                                              
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/RavenSprite/Raven_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/RavenSprite/Raven_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/RavenSprite/Raven_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/RavenSprite/Raven_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/RavenSprite/Raven_mouth_smile_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/RavenSprite/Raven_mouth_tongue_w.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/RavenSprite/Raven_mouth_lipbite_w.png",
            "newgirl['Mystique'].Mouth == 'normal'", "images/RavenSprite/Raven_mouth_normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/RavenSprite/Raven_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/RavenSprite/Raven_mouth_sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/RavenSprite/Raven_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/RavenSprite/Raven_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/RavenSprite/Raven_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/RavenSprite/Raven_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/RavenSprite/Raven_mouth_tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/RavenSprite/Raven_mouth_grimace.png",           
            "True", "images/RavenSprite/Raven_mouth_normal.png",
            ),            
        (0,0), "Raven Blink",  
        (0,0), ConditionSwitch(
         ## Collar
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            "newgirl['Mystique'].Glasses", "images/MystiqueSprite/Mystique_head_glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),     
        (0,0), ConditionSwitch(
         ## Hair
            "renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/RavenSprite/Raven_Sprite_Hair.png",
            "True", Null(), 
            ),                          
        (0,0), ConditionSwitch(
         ## Hand spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'hand' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Girl_Arms == 2", "images/RogueSprite/Rogue_spunkhand.png",                
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(
         ## Face spunk
            "not newgirl['Mystique'].Spunk", Null(), 
            "'facial' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_facial.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
         ## Belly spunk
            "'belly' in newgirl['Mystique'].Spunk", "images/RogueSprite/Rogue_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),               
        # (0,0), ConditionSwitch(
           ## Props
        #     "not newgirl['Mystique'].Held or newgirl['Mystique'].Girl_Arms != 2", Null(), 
        #     "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
        #     "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",            
        #     "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
        #     "newgirl['Mystique'].Girl_Arms == 2 and newgirl['Mystique'].Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
        #     "True", Null(), 
        #     ),        
        (0,0), ConditionSwitch(
         ## UI tool for When Mystique is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_M",
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
         ## UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == 'Mystique'", Null(), 
            # This doesn't activate unless Mystique is not primary, and is actively masturbating
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_M",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(                                                                          
         ## UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_M",
            "Trigger == 'fondle pussy'", "GropePussy_M",
            "Trigger == 'lick pussy'", "Lickpussy_M",
            "True", Null(), 
            ),
        (0,0), ConditionSwitch(                                                                        
         ## UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != 'Mystique'", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",        
            # When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",            
            # When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",       
            # When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),                                              
            # When both triggers are the same, do nothing  
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",  
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy_M",
            "Trigger2 == 'lick pussy'", "Lickpussy_M",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null(), 
            ),     
        (0,0), ConditionSwitch(  
         ## UI tool for Trigger4(Threesome) actions (ie Kitty's hand on her)
            "not Trigger4 or Ch_Focus != 'Mystique'", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_M",            
            "Trigger4 == 'lick pussy'", "Lickpussy_M",
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
         ## UI tool for Trigger3(lesbian) actions (ie Kitty's hand on her when Mystique is secondary)
            "not Trigger3 or Ch_Focus == 'Mystique'", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and newgirl['Mystique'].Lust >= 70", "GirlFingerPussy_M",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_M",            
            "Trigger3 == 'lick pussy'", "Lickpussy_M",
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
    
image Raven Blink:
    ConditionSwitch(
    "newgirl['Mystique'].Eyes == 'sexy'", "images/RavenSprite/Raven_eyes_sexy.png",
    "newgirl['Mystique'].Eyes == 'side'", "images/RavenSprite/Raven_eyes_side.png",
    "newgirl['Mystique'].Eyes == 'surprised'", "images/RavenSprite/Raven_eyes_surprised.png",
    "newgirl['Mystique'].Eyes == 'normal'", "images/RavenSprite/Raven_eyes_normal.png",    
    "newgirl['Mystique'].Eyes == 'stunned'", "images/RavenSprite/Raven_eyes_stunned.png",
    "newgirl['Mystique'].Eyes == 'down'", "images/RavenSprite/Raven_eyes_down.png",
    "newgirl['Mystique'].Eyes == 'closed'", "images/RavenSprite/Raven_eyes_closed.png",
    "newgirl['Mystique'].Eyes == 'manic'", "images/RavenSprite/Raven_eyes_manic.png",
    "newgirl['Mystique'].Eyes == 'squint'", "Raven_Squint",
    "True", "images/RavenSprite/Raven_eyes_normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RavenSprite/Raven_eyes_closed.png"
    .25
    repeat                

image Raven_Squint:
    "images/RavenSprite/Raven_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/RavenSprite/Raven_eyes_squint.png"
    .25
    repeat  
           


image Test_Object:                 #this is the yellow rectangle
    contains:
        Solid("#d5f623", xysize=(1024, 678))
    anchor (0,0)
    alpha .8
    
image Mystique_At_DeskB:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)
    contains:        
#        AlphaMask("Test_Object", "images/ClassroomFront.png")
        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
    contains:
        ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
                "True", "images/ClassroomPupils.png",                
                )      

image Mystique_At_PodiumB:
    contains:
        subpixel True
        "Mystique_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)
    contains:        
#        AlphaMask("Test_Object", "images/ClassroomFront.png")
        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
    contains:
        ConditionSwitch(        
                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),                
                "True", "images/ClassroomPupils.png",                
                )                     
        
image Mystique_At_Desk:
    contains:
        subpixel True
        "Mystique_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)

image Mystique_At_Podium:
    contains:
        subpixel True
        "Mystique_Sprite"
        zoom 0.29
        pos (630,180) #(500,200)




# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Mystique BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Mystique BJ element
#Mystique BJ Over Sprite Compositing


image Mystique_Blue_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (787,913),             
        # (0,0), ConditionSwitch(
           ## Back of the hair, which needs to go behind the body
        #     "Speed == 0", At("Emma_BJ_HairBack", BJ_Starting()),                         
        #     "Speed == 1", At("Emma_BJ_HairBack", BJ_Licking()),                         
        #     "Speed == 2", At("Emma_BJ_HairBack", BJ_Heading()),                        
        #     "Speed == 3", At("Emma_BJ_HairBack", BJ_Sucking()),
        #     "Speed == 4", At("Emma_BJ_HairBack", BJ_Deep()), 
        #     "True", Null(),
        #     ),    
        (0,0), ConditionSwitch(
         ## Body, everything below the chin
            "Speed == 0", At("Mystique_BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("Mystique_BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("Mystique_BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("Mystique_BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("Mystique_BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(
         ## Her head
            "Speed == 0", At("Mystique_BJ_Head_2", BJ_Starting()),                       
            #"Speed == 1", At("BJ_Head", BJ_Licking()),                       
            "Speed == 1", At("Mystique_BJ_Head_2", BJ_Licking()),                       
            "Speed == 2", At("Mystique_BJ_Head_2", BJ_Heading()),                     
            "Speed == 3", At("Mystique_BJ_Head_2", BJ_Sucking()),
            "Speed == 4", At("Mystique_BJ_Head_2", BJ_Deep()), 
            "True", Null(),
            ),   
#        (0,0), Transform("images/RogueBJFace/Rogue_bj_markercard.png", alpha=(.2)),
        (0,0), ConditionSwitch(
         ## Cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
         (0,0), ConditionSwitch(
          ## The masked overlay for when her head overlaps the cock
             "Speed < 3", Null(), 
             #"Speed == 2", At("Emma_BJ_Head_3", BJ_Heading()),
             "Speed == 3", At("Mystique_BJ_Head_3", BJ_Sucking()),
             "Speed == 4", At("Mystique_BJ_Head_3", BJ_Deep()), 
             #"Speed == 3", At(AlphaMask("Mystique_BJ_Head_2", "Emma_BJ_Mask"), BJ_Sucking()),
             #"Speed == 4", At(AlphaMask("Mystique_BJ_Head_2", "images/EmmaSprite/Emma_bj_facemask.png"), BJ_Deep()), 
             "True", Null(),
             ),    
         (0,0), ConditionSwitch(
          ## Same as above, but for the heading animation
             #"Speed == 2", At("E_BJ_MaskHeadingComposite", BJ_Heading()),
             #"Speed == 2", At("Emma_BJ_Head_4", BJ_Heading()),
             "True", Null(),
             ),    
        )
    zoom .55
    anchor (.5,.5)
    
image Mystique_BJ_Backdrop:
## Her Body under the head
    "Mystique_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125) #-325, -125

image Mystique_BJ_Head_3:
    #"images/MystiqueSprite/Mystique_bj_facemask.png"
    AlphaMask("Mystique_BJ_Head", "Mystique_BJ_Mask")    #zoom .75
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Mystique_BJ_Head_4:
    AlphaMask("Mystique_BJ_Head_2", "E_BJ_MaskHeadingComposite")    #zoom .75
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Mystique_BJ_Head_2:
    "Mystique_BJ_Head"
    # #zoom .75
    # zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Mystique_BJ_Mask:
    "images/MystiqueSprite/Mystique_bj_facemask2.png"
    # anchor (0.6, 0.0)                
    # zoom 2.025  
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125

    # zoom 4.5
    # pos (175,-110)
    # offset (-615, -125)
    anchor (0.6, 0.0)                
    zoom .75 


image Mystique_BJ_Head:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(
         ## Head 
            #"renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/MystiqueSprite/Mystique_head_base.png",
            ),  
        (0,0), ConditionSwitch(
         ## Brows
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
        (0,0), "Mystique Blink",  
        (0,0), ConditionSwitch(
         ## Collar
            "newgirl['Mystique'].Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(
         ## Hair
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/MystiqueSprite/Mystique_hair_basic.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
         ## Mouth for under layer
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
        # (0,0), ConditionSwitch(
           ## Mouth spunk               
        #     "'mouth' not in E_Spunk", Null(),
        #     "E_Mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",            
        #     "E_Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",            
        #     "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",  
        #     ), 
        (0,0), ConditionSwitch(
         ## Facial spunk               
            "'facial' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ), 
        (0,0), ConditionSwitch(
         ## Hair spunk               
            "'hair' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .75


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Raven BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Raven BJ element
#Raven BJ Over Sprite Compositing


image Mystique_Raven_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (787,913),             
        # (0,0), ConditionSwitch(
           ## Back of the hair, which needs to go behind the body
        #     "Speed == 0", At("Emma_BJ_HairBack", BJ_Starting()),                         
        #     "Speed == 1", At("Emma_BJ_HairBack", BJ_Licking()),                         
        #     "Speed == 2", At("Emma_BJ_HairBack", BJ_Heading()),                        
        #     "Speed == 3", At("Emma_BJ_HairBack", BJ_Sucking()),
        #     "Speed == 4", At("Emma_BJ_HairBack", BJ_Deep()), 
        #     "True", Null(),
        #     ),    
        (0,0), ConditionSwitch(
         ## Body, everything below the chin
            "Speed == 0", At("Raven_BJ_Backdrop", BJ_StartingBody()),                       
            "Speed == 1", At("Raven_BJ_Backdrop", BJ_LickingBody()),                        
            "Speed == 2", At("Raven_BJ_Backdrop", BJ_HeadingBody()),                 
            "Speed == 3", At("Raven_BJ_Backdrop", BJ_SuckingBody()),
            "Speed == 4", At("Raven_BJ_Backdrop", BJ_DeepBody()), 
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(
         ## Her head
            "Speed == 0", At("Raven_BJ_Head_2", BJ_Starting()),                       
            #"Speed == 1", At("BJ_Head", BJ_Licking()),                       
            "Speed == 1", At("Raven_BJ_Head_2", BJ_Licking()),                       
            "Speed == 2", At("Raven_BJ_Head_2", BJ_Heading()),                     
            "Speed == 3", At("Raven_BJ_Head_2", BJ_Sucking()),
            "Speed == 4", At("Raven_BJ_Head_2", BJ_Deep()), 
            "True", Null(),
            ),   
#        (0,0), Transform("images/RogueBJFace/Rogue_bj_markercard.png", alpha=(.2)),
        (0,0), ConditionSwitch(
         ## Cock
            "Speed == 0", At("Blowcock", Cock_BJ_Starting()),   
            "Speed == 1", At("Blowcock", Cock_BJ_Licking()),                                  
            "Speed == 2", At("Blowcock", Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Cock_BJ_Straight()),                          
            "Speed == 4", At("Blowcock", Cock_BJ_Straight()), 
            "True", Null(),
            ),    
         (0,0), ConditionSwitch(
          ## The masked overlay for when her head overlaps the cock
             "Speed < 3", Null(), 
             #"Speed == 2", At("Emma_BJ_Head_3", BJ_Heading()),
             "Speed == 3", At("Raven_BJ_Head_3", BJ_Sucking()),
             "Speed == 4", At("Raven_BJ_Head_3", BJ_Deep()), 
             #"Speed == 3", At(AlphaMask("Raven_BJ_Head_2", "Emma_BJ_Mask"), BJ_Sucking()),
             #"Speed == 4", At(AlphaMask("Raven_BJ_Head_2", "images/EmmaSprite/Emma_bj_facemask.png"), BJ_Deep()), 
             "True", Null(),
             ),    
         (0,0), ConditionSwitch(
          ## Same as above, but for the heading animation
             #"Speed == 2", At("E_BJ_MaskHeadingComposite", BJ_Heading()),
             #"Speed == 2", At("Emma_BJ_Head_4", BJ_Heading()),
             "True", Null(),
             ),    
        )
    zoom .55
    anchor (.5,.5)
    
image Raven_BJ_Backdrop:
# #Her Body under the head
    "Mystique_Raven_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125) #-325, -125

image Raven_BJ_Head_3:
    #"images/RavenSprite/Raven_bj_facemask.png"
    AlphaMask("Raven_BJ_Head", "Raven_BJ_Mask")    #zoom .75
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Raven_BJ_Head_4:
    AlphaMask("Raven_BJ_Head_2", "E_BJ_MaskHeadingComposite")    #zoom .75
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Raven_BJ_Head_2:
    "Raven_BJ_Head"
    # #zoom .75
    # zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Raven_BJ_Mask:
    "images/RavenSprite/Raven_bj_facemask2.png"
    # anchor (0.6, 0.0)                
    # zoom 2.025  
    # #zoom 4.05
    # pos (275,-110)
    # offset (-240, -200) #-140 - 125

    # zoom 4.5
    # pos (175,-110)
    # offset (-615, -125)
    anchor (0.6, 0.0)                
    zoom .75 


image Raven_BJ_Head:
    LiveComposite(
        (555,673), 
        (0,0), ConditionSwitch(
         ## Head 
            #"renpy.showing('Mystique_BJ_Animation') or renpy.showing('BJ_NewTest') or renpy.showing('Mystique_TJ_Animation')", Null(),
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_head_evowet.png",
            # "R_Hair == 'evo' and R_Blush == 2", "images/RogueSprite/Rogue_head_evo_blush2.png",
            # "R_Hair == 'evo' and R_Blush", "images/RogueSprite/Rogue_head_evo_blush.png",
            # "R_Hair == 'evo'", "images/RogueSprite/Rogue_head_evo.png",
            "True", "images/RavenSprite/Raven_Sprite_Head.png",
            ),  
        (0,0), ConditionSwitch(
         ## Brows
            # "R_Brows == 'normal' and R_Blush == 2", "images/RogueSprite/Rogue_brows_normal_b.png",
            # "R_Brows == 'angry' and R_Blush == 2", "images/RogueSprite/Rogue_brows_angry_b.png",
            # "R_Brows == 'sad' and R_Blush == 2", "images/RogueSprite/Rogue_brows_sad_b.png",
            # "R_Brows == 'surprised' and R_Blush == 2", "images/RogueSprite/Rogue_brows_surprised_b.png",        
            # "R_Brows == 'confused' and R_Blush == 2", "images/RogueSprite/Rogue_brows_confused_b.png",
            "newgirl['Mystique'].Brows == 'normal'", "images/RavenSprite/Raven_brows_normal.png",
            "newgirl['Mystique'].Brows == 'angry'", "images/RavenSprite/Raven_brows_angry.png",
            "newgirl['Mystique'].Brows == 'sad'", "images/RavenSprite/Raven_brows_sad.png",
            "newgirl['Mystique'].Brows == 'surprised'", "images/RavenSprite/Raven_brows_surprised.png",        
            "newgirl['Mystique'].Brows == 'confused'", "images/RavenSprite/Raven_brows_confused.png",
            "True", "images/RavenSprite/Raven_brows_normal.png",
            ),
#        (0,0), ConditionSwitch(
          ## Blush
#            "R_Blush", "images/RogueSprite/Rogue_blush.png",
#            "True", Null(), 
#            ),
        (0,0), "Raven Blink",  
        (0,0), ConditionSwitch(
         ## Collar
            "newgirl['Mystique'].Glasses", "images/RogueSprite/Rogue_Sprite_Glasses.png",   
            "True", Null(),                #R_Arms == 'gloved' or not R_Arms
            ),  
        (0,0), ConditionSwitch(
         ## Hair
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_wet.png",
            # "R_Hair == 'evo' and R_Water and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_wet.png",
            # "R_Hair == 'evo' and R_Water", "images/RogueSprite/Rogue_hair_wet.png",
            # "R_Hair == 'evo' and R_HairColor == 'black'", "images/RogueSprite/Rogue_hairBlack_evo.png",
            # "R_Hair == 'evo' and R_HairColor == 'blonde'", "images/RogueSprite/Rogue_hairBlonde_evo.png",
            "newgirl['Mystique'].Hair", "images/RavenSprite/Raven_Sprite_Hair.png",
            "True", Null(), 
            ),   
        (0,0), ConditionSwitch(
         ## Mouth for under layer
            #"Speed == 1 and Trigger == 'blow' and 'mouth' in R_Spunk", "images/RogueBJFace/Rogue_bj_mouth_lickingS.png",
            "Speed == 1 and Trigger == 'blow'", "images/RavenSprite/Raven_mouth_tongue.png", #licking
            "Speed == 2 and Trigger == 'blow'", Null(),                                #heading Rogue_BJ_HeadingMouth()
            "Speed == 3 and Trigger == 'blow'", "images/RavenSprite/Raven_bj_mouth2.png", #sucking
            "Speed == 4 and Trigger == 'blow'", "images/RavenSprite/Raven_bj_mouth2.png", #deepthroat   
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sucking'", "images/RavenSprite/Raven_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'surprised'", "images/RavenSprite/Raven_mouth_sucking_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'sad'", "images/RavenSprite/Raven_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'kiss'", "images/RavenSprite/Raven_mouth_sad_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'smile'", "images/RavenSprite/Raven_mouth_smile_w.png",
            "'mouth' in newgirl['Mystique'].Spunk and newgirl['Mystique'].Mouth == 'tongue'", "images/RavenSprite/Raven_mouth_tongue_w.png",
            "'mouth' in newgirl['Mystique'].Spunk", "images/RavenSprite/Raven_mouth_lipbite_w.png",      
            "newgirl['Mystique'].Mouth == 'normal'", "images/RavenSprite/Raven_mouth_normal.png",
            "newgirl['Mystique'].Mouth == 'lipbite'", "images/RavenSprite/Raven_mouth_lipbite.png",
            "newgirl['Mystique'].Mouth == 'sucking'", "images/RavenSprite/Raven_mouth_sucking.png",            
            "newgirl['Mystique'].Mouth == 'kiss'", "images/RavenSprite/Raven_mouth_kiss.png",
            "newgirl['Mystique'].Mouth == 'sad'", "images/RavenSprite/Raven_mouth_sad.png",
            "newgirl['Mystique'].Mouth == 'smile'", "images/RavenSprite/Raven_mouth_smile.png",
            "newgirl['Mystique'].Mouth == 'surprised'", "images/RavenSprite/Raven_mouth_surprised.png",            
            "newgirl['Mystique'].Mouth == 'tongue'", "images/RavenSprite/Raven_mouth_tongue.png",                
            "newgirl['Mystique'].Mouth == 'grimace'", "images/RavenSprite/Raven_mouth_grimace.png",          
            "True", "images/RavenSprite/Raven_mouth_normal.png",
            ),
        (0,0), ConditionSwitch(
         ## Facial spunk               
            "'facial' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",             
            "True", Null(),
            ),  
        (0,0), ConditionSwitch(
         ## Hair spunk               
            "'hair' in newgirl['Mystique'].Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",              
            "True", Null(),
            ),  
        )                
    anchor (0.6, 0.0)                
    zoom .75 


label Mystique_BJ_Launch(Line = 0):    # The sequence to launch the Emma BJ animations  
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    if renpy.showing("Mystique_BJ_Animation"):
        return

    call Mystique_Hide from _call_Mystique_Hide_2
    if Line == "L" or Line == "cum":
        show Mystique_Sprite at SpriteLoc(StageCenter) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80) 
        with dissolve
    else:
        show Mystique_Sprite at SpriteLoc(StageCenter) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140) 
        with dissolve
        
#    show Mystique:
#        pos (715,50)
#        alpha 1
#        zoom 2.5 offset (-90,140) 
#    with dissolve
        
    if Taboo and Line == "L": # Mystique gets started. . .
        if not newgirl["Mystique"].Blow:
            "Mystique looks around to see if anyone can see her."
            "Mystique hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Mystique hesitantly looks around to see if anyone notices what she's doing, but then bends down and puts her lips around you,"
    elif Line == "L":    
        if not newgirl["Mystique"].Blow:
            "Mystique hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "Mystique bends down and begins to suck on your cock."    
            
    $ Speed = 0
    
    #if Line != "cum":
    $ Trigger = "blow"
    
    show Mystique_Sprite zorder newgirl["Mystique"].GirlLayer:
        alpha 0
    show Mystique_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Mystique_BJ_Reset: # The sequence to the Mystique animations from BJ to default
    if not renpy.showing("Mystique_BJ_Animation"):
        return
    hide Mystique_BJ_Animation
    $ Speed = 0
    
    show Mystique_Sprite SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:        
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)     
    call NewGirl_Face("Mystique","sexy") from _call_NewGirl_Face_340        
    return  
    
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////

image Mystique_Hand_Under:
    ConditionSwitch(
        "newgirl['Mystique'].LooksLike == 'Mystique'", "images/MystiqueSprite/hand2.png",
        "newgirl['Mystique'].LooksLike == 'Raven'", "images/RavenSprite/hand2.png",
        "True", "images/MystiqueSprite/hand2.png",
        ),
    anchor (0.5,0.5)
    pos (0,0)
    
    
image Mystique_Hand_Over:
    ConditionSwitch(
        "newgirl['Mystique'].LooksLike == 'Mystique'", "images/MystiqueSprite/hand1.png",
        "newgirl['Mystique'].LooksLike == 'Raven'", "images/RavenSprite/hand1.png",
        "True", "images/MystiqueSprite/hand1.png",
        ),
    anchor (0.5,0.5)
    pos (0,0)



image Mystique_Blue_HJ_Animation:  
    contains:
        ConditionSwitch(
        ## Backside of the hand
            "not Speed", Transform("Mystique_Hand_Under"), 
            "Speed == 1", At("Mystique_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Mystique_Hand_Under", Kitty_Hand_2()),
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(
        ## Cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(
        ## Fingers of the hand
            "not Speed", Transform("Mystique_Hand_Over"), 
            "Speed == 1", At("Mystique_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Mystique_Hand_Over", Kitty_Hand_2()), 
            "Speed", Null(),
            ),   
    #anchor (0.51, -1.3)
    #zoom 0.4#0.6
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6
        


label Mystique_HJ_Launch(Line = 0): 
    $ newgirl["Mystique"].Girl_Arms = 1
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    if renpy.showing("Mystique_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Mystique_Hide from _call_Mystique_Hide_3
    if Line == "L":      
        show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
    else:     
        show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
        with dissolve
   
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    if newgirl["Mystique"].LooksLike == "Mystique" or newgirl["Mystique"].LooksLike == "Raven":
        show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
            #xoffset 150
            #offset (100,250)#(75,250)
    elif newgirl["Mystique"].LooksLike == "Emma" or newgirl["Mystique"].LooksLike == "Kitty":
        show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
            offset (100,250)#(75,250)
    else:
        show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
            #xoffset 150
            #offset (100,250)#(75,250)
    return

label Mystique_HJ_FixPos(Line = 0): 
    $ newgirl["Mystique"].Girl_Arms = 1
    if Trigger2 == "jackin":
        $ Trigger2 = 0
    # if renpy.showing("Mystique_HJ_Animation"):        
    #     $ Trigger = "hand"
    #     return
    call Mystique_Hide from _call_Mystique_Hide_4
    if Line == "L":      
        show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
    else:     
        show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 xpos 700 yoffset 200
        with dissolve
   
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    if newgirl["Mystique"].LooksLike == "Mystique" or newgirl["Mystique"].LooksLike == "Raven":
        show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
            #xoffset 150
            #offset (100,250)#(75,250)
    elif newgirl["Mystique"].LooksLike == "Emma" or newgirl["Mystique"].LooksLike == "Kitty":
        show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
            offset (100,250)#(75,250)
    else:
        show Mystique_HJ_Animation at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder 150 with easeinbottom:
            #xoffset 150
            #offset (100,250)#(75,250)
    return
    
label Mystique_HJ_Reset: # The sequence to the Emma animations from handjob to default
    if not renpy.showing("Mystique_HJ_Animation"):
        return    
    $ Speed = 0
    hide Mystique_HJ_Animation with easeoutbottom
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    return
        
label Mystique_Kissing_Launch(T = Trigger):    
    call Mystique_Hide from _call_Mystique_Hide_5
    $ Trigger = T
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer
    show Mystique_Sprite at SpriteLoc(StageCenter) zorder newgirl["Mystique"].GirlLayer:
        ease 0.5 zoom 2
    return
    
label Mystique_Kissing_Smooch:   
    call MystiqueFace("kiss") from _call_MystiqueFace_838  
    show Mystique_Sprite at SpriteLoc(StageCenter) zorder newgirl["Mystique"].GirlLayer:
        ease 0.5 xpos StageCenter zoom 2
        pause 1
        ease 0.5 xpos newgirl["Mystique"].SpriteLoc zoom 1        
    call MystiqueFace("sexy") from _call_MystiqueFace_839  
    return
            
label Mystique_Breasts_Launch(T = Trigger):    
    call Mystique_Hide from _call_Mystique_Hide_6
    $ Trigger = T
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) zoom 2
    return
        
label Mystique_Pussy_Launch(T = Trigger):
    call Mystique_Hide from _call_Mystique_Hide_7    
    $ Trigger = T
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        ease 0.5 pos (700,-400) zoom 2
    return
        
label Mystique_Pos_Reset(Pose = 0):
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1   
    show Mystique_Sprite at SpriteLoc(newgirl["Mystique"].SpriteLoc) zorder newgirl["Mystique"].GirlLayer:
        offset (0,0) 
        anchor (0.5, 0.0)
        zoom 1  
        alpha 1
    $ Trigger = Pose
    return
    
label Mystique_Hide:
        if renpy.showing("Mystique_SexSprite") or renpy.showing("Mystique_Doggy"):
            call Mystique_Sex_Reset from _call_Mystique_Sex_Reset_30
        hide Mystique_SexSprite
        if renpy.showing("Mystique_Doggy"):
            if newgirl["Mystique"].Gag == "ballgag":
                $ newgirl["Mystique"].Gag = 0
        hide Mystique_Doggy
        hide Mystique_HJ_Animation
        hide Mystique_BJ_Animation
    #    hide Emma_TJ_Animation 
        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_E:    
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

image GropeRightBreast_E:    
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
image LickRightBreast_E:   
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
            
image LickLeftBreast_E:   
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

image GropeThigh_E: 
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

image GropePussy_M: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (255,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (255,620)
                ease .75 rotate 170 pos (255,635)   
            choice: 
                ease .5 rotate 190 pos (255,620)
                pause .25
                ease 1 rotate 170 pos (255,635)             
            repeat

image FingerPussy_M: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.7
        pos (265,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (275,685)
                pause .5
                ease 1 rotate 50 pos (265,720)   
            choice:                          
                ease .5 rotate 40 pos (275,685)
                pause .5
                ease 1.75 rotate 50 pos (265,720)  
            choice:                          
                ease 2 rotate 40 pos (275,685)
                pause .5
                ease 1 rotate 50 pos (265,720)  
            choice:                          
                ease .25 rotate 40 pos (275,685)
                ease .25 rotate 50 pos (265,720) 
                ease .25 rotate 40 pos (275,685)
                ease .25 rotate 50 pos (265,720)
            repeat
            
image Lickpussy_M:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.5
        xzoom -0.5
        pos (285,670)#(0.5,0.5)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easein .5 rotate -50 pos (265,650)  
            linear .5 rotate -60 pos (255,660)
            easeout 1 rotate 10 pos (285,670)
            repeat

image VibratorRightBreast_E: 
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

image VibratorLeftBreast_E: 
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
            
image VibratorPussy_E: 
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

image VibratorAnal_E: 
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
            
image VibratorPussyInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_E: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_E: 
    contains:
        "GirlGropeLeftBreast_E"
    contains:
        "GirlGropeRightBreast_E"
    
image GirlGropeLeftBreast_E:  
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

image GirlGropeRightBreast_E:    
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

image GirlGropeThigh_E: 
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

image GirlGropePussy_ESelf:
    contains:
        "GirlGropePussy_E"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)
    
image GirlGropePussy_M: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (235,575)#(210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (240,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (240,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (240,590)
                ease .75 rotate 200 pos (240,595)
                ease .5 rotate 205 pos (240,590)
                ease .75 rotate 200 pos (240,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (240,590)
                ease .3 rotate 200 pos (240,600)
                ease .3 rotate 205 pos (240,590)
                ease .3 rotate 200 pos (240,600)
            repeat

image GirlFingerPussy_M: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (265,630)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (265,635)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (265,635)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (265,635)
                ease .75 rotate 200 pos (265,640)
                ease .5 rotate 205 pos (265,635)
                ease .75 rotate 200 pos (265,640)
            choice: #Fast stroke
                ease .3 rotate 205 pos (265,635)
                ease .3 rotate 200 pos (265,645)
                ease .3 rotate 205 pos (265,635)
                ease .3 rotate 200 pos (265,645)
            repeat

# Start Emma Faces / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label MystiqueFace(Emote = newgirl["Mystique"].Emote, B = newgirl["Mystique"].Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
        if (newgirl["Mystique"].Forced or "angry" in newgirl["Mystique"].RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"     
        elif newgirl["Mystique"].ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
            
        if Emote == "normal":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "angry"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl["Mystique"].Mouth = "tongue"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "surprised"
                $ newgirl["Mystique"].Blush = 1
        elif Emote == "sad":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl["Mystique"].Mouth = "lipbite"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl["Mystique"].Mouth = "sucking"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl["Mystique"].Mouth = "smirk"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "grimace":
                $ newgirl["Mystique"].Mouth = "grimace"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint" 
        elif Emote == "laugh":
                $ newgirl["Mystique"].Mouth = "grimace"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"
            
        if M:
                $ newgirl["Mystique"].Eyes = "surprised"        
        if B > 1:
                $ newgirl["Mystique"].Blush = 2
        elif B:
                $ newgirl["Mystique"].Blush = 1
        else:
                $ newgirl["Mystique"].Blush = 0
        
        if Mouth:
                $ newgirl["Mystique"].Mouth = Mouth
        if Eyes:
                $ newgirl["Mystique"].Eyes = Eyes
        if Brows:
                $ newgirl["Mystique"].Brows = Brows
        
        return


label MystiqueFaceSpecial(Emote = newgirl["Mystique"].Emote, B = newgirl["Mystique"].Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):

        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state 
            
        if Emote == "normal":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "angry":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "angry"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "bemused":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "closed":
                $ newgirl["Mystique"].Mouth = "normal"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"  
        elif Emote == "confused":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "kiss":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "tongue":
                $ newgirl["Mystique"].Mouth = "tongue"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "stunned" #"stunned"
        elif Emote == "manic":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "surprised"
                $ newgirl["Mystique"].Blush = 1
        elif Emote == "sad":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "sexy"
        elif Emote == "sadside":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "side"
        elif Emote == "sexy":
                $ newgirl["Mystique"].Mouth = "lipbite"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "smile":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sucking":
                $ newgirl["Mystique"].Mouth = "sucking"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "closed"
        elif Emote == "surprised":
                $ newgirl["Mystique"].Mouth = "kiss"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "startled":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "surprised"
                $ newgirl["Mystique"].Eyes = "surprised"
        elif Emote == "down":
                $ newgirl["Mystique"].Mouth = "sad"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "down"  
        elif Emote == "perplexed":
                $ newgirl["Mystique"].Mouth = "smile"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "normal"
        elif Emote == "sly":
                $ newgirl["Mystique"].Mouth = "smirk"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "grimace":
                $ newgirl["Mystique"].Mouth = "grimace"
                $ newgirl["Mystique"].Brows = "normal"
                $ newgirl["Mystique"].Eyes = "squint"
        elif Emote == "laugh":
                $ newgirl["Mystique"].Mouth = "grimace"
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Eyes = "closed"
            
        if M:
                $ newgirl["Mystique"].Eyes = "surprised"        
        if B > 1:
                $ newgirl["Mystique"].Blush = 2
        elif B:
                $ newgirl["Mystique"].Blush = 1
        else:
                $ newgirl["Mystique"].Blush = 0
        
        if Mouth:
                $ newgirl["Mystique"].Mouth = Mouth
        if Eyes:
                $ newgirl["Mystique"].Eyes = Eyes
        if Brows:
                $ newgirl["Mystique"].Brows = Brows
        
        return
        
        
# Emma's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label MystiqueWardrobe:
    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call E_Pos_Reset from _call_E_Pos_Reset_56
                    "Face":
                        call E_Kissing_Launch(0) from _call_E_Kissing_Launch_2
                    "Body":
                        call E_Pussy_Launch(0) from _call_E_Pussy_Launch_17
                    "Back":
                        jump EmmaWardrobe 
        # Outfits
        "Nude":
            $ E_Over = 0
            $ E_Chest = 0
            $ E_Legs = 0
            $ E_Panties = 0
            $ E_Gloves = 0
            $ E_Neck = 0
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [E_Over]" if E_Over:
                        $ E_Over = 0
                    "Add Jacket":
                        $ E_Over = "jacket"   
                        $ E_Arms = 0
                    "Add Towel":
                        $ E_Over = "towel"   
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe                
        "Tops":            
            while True:
                menu:
                    # Tops    
                    "Remove [E_Chest]" if E_Chest:
                        $ E_Chest = 0
                    "Add corset":
                        $ E_Chest = "corset"
                    "Back":
                        jump EmmaWardrobe             
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if E_Legs:     
                        $ E_Legs = 0
                    "Add pants":
                        $ E_Legs = "pants"
                        $ E_Upskirt = 0
                    "Toggle upskirt":
                        if E_Upskirt:
                            $ E_Upskirt = 0
                        else:
                            $ E_Upskirt = 1
                    "Back":
                        jump EmmaWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
                    "Remove panties" if E_Panties:     
                        $ E_Panties = 0     
                    "Add black panties":
                        $ E_Panties = "white panties"
                    "pull down-up panties":
                        if E_PantiesDown:
                            $ E_PantiesDown = 0
                        else:
                            $ E_PantiesDown = 1
                    "Back":
                        jump EmmaWardrobe    
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call EmmaEmotionEditor from _call_EmmaEmotionEditor_1
                    "Toggle Arms":
                        if Emma_Arms == 1:
                            $ Emma_Arms = 2
                        else:
                            $ Emma_Arms = 1
                    "Toggle Wetness":
                        if not E_Wet:
                            $ E_Wet = 1
                        elif E_Wet == 1:
                            $ E_Wet = 2
                        else:
                            $ E_Wet  = 0
                    "Toggle wet look":
                        if not E_Water:
                            $ E_Water = 1
                        elif E_Water == 1:
                            $ E_Water = 3
                        else:
                            $ E_Water  = 0
                    "Toggle pubes":
                        if not E_Pubes:
                            $ E_Pubes = 1
                        else:
                            $ E_Pubes = 0
                    "Toggle Pussy Spunk":
                        if "pussy" in E_Spunk:
                            $ E_Spunk.remove("pussy")
                        else:
                            $ E_Spunk.append("pussy")

                    "Add choker" if not E_Neck:
                        $ E_Neck = "choker"
                    "Remove choker" if E_Neck:
                        $ E_Neck = 0
                        
                    "Add Gloves" if not E_Arms:
                        $ E_Arms = "white gloves"
                    "Remove Gloves" if E_Arms:
                        $ E_Arms = 0
                    "Back":
                        jump EmmaWardrobe               
        "Nothing":
            return
    jump EmmaWardrobe
return

label MystiqueEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ E_Emote = "normal"
                    call EmmaFace from _call_EmmaFace_1525
                "Angry":
                    $ E_Emote = "angry"
                    call EmmaFace from _call_EmmaFace_1526
                "Smiling":
                    $ E_Emote = "smile"
                    call EmmaFace from _call_EmmaFace_1527
                "Sexy":
                    $ E_Emote = "sexy"
                    call EmmaFace from _call_EmmaFace_1528
                "Suprised":
                    $ E_Emote = "surprised"
                    call EmmaFace from _call_EmmaFace_1529
                "Bemused":
                    $ E_Emote = "bemused"
                    call EmmaFace from _call_EmmaFace_1530
                "Manic":
                    $ E_Emote = "manic"
                    call EmmaFace from _call_EmmaFace_1531
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ E_Emote = "sad"
                    call EmmaFace from _call_EmmaFace_1532
                "Sucking":
                    $ E_Emote = "sucking"
                    call EmmaFace from _call_EmmaFace_1533
                "kiss":
                    $ E_Emote = "kiss"
                    call EmmaFace from _call_EmmaFace_1534
                "Tongue":
                    $ E_Emote = "tongue"
                    call EmmaFace from _call_EmmaFace_1535
                "confused":
                    $ E_Emote = "confused"
                    call EmmaFace from _call_EmmaFace_1536
                "Closed":
                    $ E_Emote = "closed"
                    call EmmaFace from _call_EmmaFace_1537
                "Down":
                    $ E_Emote = "down"
                    call EmmaFace from _call_EmmaFace_1538
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ E_Emote = "sadside"
                    call EmmaFace from _call_EmmaFace_1539
                "Startled":
                    $ E_Emote = "startled"
                    call EmmaFace from _call_EmmaFace_1540
                "Perplexed":
                    $ E_Emote = "perplexed"
                    call EmmaFace from _call_EmmaFace_1541
                "Sly":
                    $ E_Emote = "sly"
                    call EmmaFace from _call_EmmaFace_1542
        "Toggle Mouth Spunk":
            if "mouth" in E_Spunk:
                $ E_Spunk.remove("mouth")
            else:
                $ E_Spunk.append("mouth")
        "Toggle hand Spunk":
            if "hand" in E_Spunk:
                $ E_Spunk.remove("hand")
            else:
                $ E_Spunk.append("hand")
                
        "Toggle Facial Spunk":
            if "facial" in E_Spunk and "hair" not in E_Spunk:
                $ E_Spunk.append("hair")
            elif "facial" in E_Spunk:
                $ E_Spunk.remove("facial")                
                $ E_Spunk.remove("hair")
            else:
                $ E_Spunk.append("facial")
            
        "Blush":
            if E_Blush == 2:
                $ E_Blush = 1
            elif E_Blush:
                $ E_Blush = 0
            else:
                $ E_Blush = 2  
        "Exit.":
            return
    jump EmmaEmotionEditor
return
