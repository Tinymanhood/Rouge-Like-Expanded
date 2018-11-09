image Emma_Cowgirl:
    #core sex animation   
    contains:
        ConditionSwitch(                                                               
            # Emma's lower body
            "P_Sprite and P_Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_Cowgirl_Legs_S1",#heading
                    "Speed == 2", "Emma_Cowgirl_Legs_S2",#slow
                    "Speed == 3", "Emma_Cowgirl_Legs_S3",#fast
                    "Speed >= 4", "Emma_Cowgirl_Legs_S4",#cumming
                    "True", "Emma_Cowgirl_Legs_S0",#Static
                    ),
            "P_Sprite and P_Cock == 'anal'", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Emma_Cowgirl_Legs_A1",#heading
                    "Speed == 2", "Emma_Cowgirl_Legs_A2",#slow
                    "Speed == 3", "Emma_Cowgirl_Legs_A3",#fast
                    "Speed >= 4", "Emma_Cowgirl_Legs_A4",#cumming
                    "True", "Emma_Cowgirl_Legs_A0",#Static
                    ),
            "True", ConditionSwitch(                                                               
                    # If neither
                    "Speed == 1", "Emma_Cowgirl_Legs_H1",#heading
                    "Speed == 4", "Emma_Cowgirl_Legs_H4",#cumming
                    "Speed >= 2", "Emma_Cowgirl_Legs_H2",#slow
                    "True", "Emma_Cowgirl_Legs_H0",#Static
                    ),
            ) 
    contains:
        ConditionSwitch(                                                              
            # Emma's upper body
            "P_Sprite and P_Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Emma_Cowgirl_Body_S1",#heading
                    "Speed == 2", "Emma_Cowgirl_Body_S2",#slow
                    "Speed == 3", "Emma_Cowgirl_Body_S3",#fast
                    "Speed >= 4", "Emma_Cowgirl_Body_S4",#cumming
                    "True",       "Emma_Cowgirl_Body_S0",#Static
                    ),
            "P_Sprite and P_Cock == 'anal'", ConditionSwitch(                                                              
#                    # If during Anal
                    "Speed == 1", "Emma_Cowgirl_Body_A1",#heading
                    "Speed == 2", "Emma_Cowgirl_Body_A2",#slow
                    "Speed == 3", "Emma_Cowgirl_Body_A3",#fast
                    "Speed >= 4", "Emma_Cowgirl_Body_A4",#cumming
                    "True",       "Emma_Cowgirl_Body_A0",#Static
                    ),
            "True", ConditionSwitch(                                                              
                    # If neither
                    "Speed == 1", "Emma_Cowgirl_Body_H1",#heading
                    "Speed == 4", "Emma_Cowgirl_Body_H4",#cumming
                    "Speed >= 2", "Emma_Cowgirl_Body_H2",#slow
                    "True",       "Emma_Cowgirl_Body_H0",#Static
                    ),
            )
    zoom 0.8
    anchor (.5,.5)
    
image Emma_Cowgirl_HairBack:
    #Hair underlay
    ConditionSwitch(                                                                            
            "E_Hair", "images/EmmaBJFaceONI/Emma_BJ_Hair_Wave_Back.png",            
            "True", Null(),
            ),
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)
  
image Emma_Cowgirl_Head:
    #Hair underlay
    "Emma_BJ_ONI_Head"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)
                    
                    
# Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /

image Emma_Cowgirl_Tits:
    #the tits used in the sex pose
    contains:
            # tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "E_Chest == 'corset'", "images/EmmaCowgirl/Emma_Cowgirl_Tits_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra' or E_Chest == 'lace bra'", "images/EmmaCowgirl/Emma_Cowgirl_Tits_Up.png",   # E_TitsUp = 1
            "True", "images/EmmaCowgirl/Emma_Cowgirl_Tits_Down.png",   # E_TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "not E_Pierce or E_Chest", Null(),
#            "E_Over == 'nighty'", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaCowgirl/Emma_Pierce_Barbell_Tits_D.png", 
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaCowgirl/Emma_Pierce_Ring_Tits_D.png", 
                    ),                    
            "True", Null(), 
            )
            
image Emma_Cowgirl_Torso:                                                                        
    #Her torso for the sex, BJ, and TJ poses
    contains:
            # body
            "images/EmmaCowgirl/Emma_Cowgirl_Body.png"
    contains:
            # tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "E_Chest == 'corset'", "images/EmmaCowgirl/Emma_Cowgirl_Tits_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra' or E_Chest == 'lace bra'", "images/EmmaCowgirl/Emma_Cowgirl_Tits_Up.png",   # E_TitsUp = 1
            "True", "images/EmmaCowgirl/Emma_Cowgirl_Tits_Down.png",   # E_TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(   
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "not E_Pierce or E_Over or E_Chest", Null(),
            "E_Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaCowgirl/Emma_Pierce_Barbell_Tits_D.png", 
                    ),    
            "E_Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings   
                    "E_Chest in ('corset', 'lace bra', 'sports bra')", Null(),  
                    "True", "images/EmmaCowgirl/Emma_Pierce_Ring_Tits_D.png", 
                    ),                    
            "True", Null(), 
            )
#    contains:
#            # tits
#        ConditionSwitch(   
#            "renpy.showing('Emma_TJ_Animation')", Null(),
#            "True", "Emma_Cowgirl_Tits",
#            )
    contains:
            #chest clothing under layer for TJs
            ConditionSwitch(    
                "not renpy.showing('Emma_TJ_Animation')", Null(),   # E_TitsUp = 0
                "E_Chest == 'sports bra'", "images/EmmaCowgirl/Emma_Cowgirl_Bra_Sports_TJU.png",
                "True", Null(),
                ) 
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "not E_Chest or renpy.showing('Emma_TJ_Animation')", Null(),   # E_TitsUp = 0
            "E_Chest == 'corset'", "images/EmmaCowgirl/Emma_Cowgirl_Bra_Corset_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra'", "images/EmmaCowgirl/Emma_Cowgirl_Bra_Sports_Up.png",   # E_TitsUp = 1
            "E_Chest == 'lace bra'", "images/EmmaCowgirl/Emma_Cowgirl_Bra_Lace_Up.png",   # E_TitsUp = 1
            "True", Null(),   # E_TitsUp = 0
            )
    contains:
            # Over clothing layer
        ConditionSwitch(   
            "E_Over == 'jacket'", ConditionSwitch(   
                    #if it's the ring pericings                       
                    "renpy.showing('Emma_TJ_Animation')", Null(),
#                    "renpy.showing('Emma_TJ_Animation')", "images/EmmaCowgirl/Emma_Cowgirl_Jacket_Down.png",
                    "E_Chest == 'corset'", "images/EmmaCowgirl/Emma_Cowgirl_Jacket_Up.png",   # E_TitsUp = 1
                    "E_Chest == 'sports bra'", "images/EmmaCowgirl/Emma_Cowgirl_Jacket_Up.png",   # E_TitsUp = 1
                    "E_Chest == 'lace bra'", "images/EmmaCowgirl/Emma_Cowgirl_Jacket_Up.png",   # E_TitsUp = 1
                    "True", "images/EmmaCowgirl/Emma_Cowgirl_Jacket_Down.png",   # E_TitsUp = 0
                    ),    
            "True", Null(), 
            )
    contains:
            # spunk on tits
            ConditionSwitch(    
                "'tits' not in E_Spunk", Null(),
                "renpy.showing('Emma_TJ_Animation')", "images/EmmaCowgirl/Emma_Spunk_Titjob_Under.png",
                "True", "images/EmmaCowgirl/Emma_Spunk_Tits.png",
                ) 
    zoom 1 
                
image Emma_Cowgirl_Body:                                                                        
    #Her Body in the sex pose
    contains:
            "Emma_Cowgirl_HairBack"
    contains:
            # body
            "Emma_Cowgirl_Torso"
    contains:
            # Arms
        ConditionSwitch(    
            "Emma_Arms == 3", Null(),   # Neither arms
            "Emma_Arms == 4", AlphaMask("Emma_Arms", "images/EmmaCowgirl/Emma_Cowgirl_ArmsMask_R.png"),   # Right arm only
            "Emma_Arms == 5", AlphaMask("Emma_Arms", "images/EmmaCowgirl/Emma_Cowgirl_ArmsMask_L.png"),   # Left arm only
            "True", AlphaMask("Emma_Arms", "images/EmmaCowgirl/Emma_Cowgirl_ArmsMask.png"),  # Both Arms
            )
    contains:
            "Emma_Cowgirl_Head"
    zoom 1 
#    offset (0,0)
# end Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /


image Emma_Arms:
    contains:
            # Base Arms
        ConditionSwitch(    
            "E_Over == 'jacket'", Null(),
            "E_Chest == 'corset'", "images/EmmaCowgirl/Emma_Cowgirl_Arms_U.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra'", "images/EmmaCowgirl/Emma_Cowgirl_Arms_U.png",   # E_TitsUp = 1
            "E_Chest == 'lace bra'", "images/EmmaCowgirl/Emma_Cowgirl_Arms_U.png",   # E_TitsUp = 1
            "True", "images/EmmaCowgirl/Emma_Cowgirl_Arms_D.png",   # E_TitsUp = 0
            )
    contains:
            # Arm clothing
        ConditionSwitch(    
            "E_Over == 'jacket'", Null(),
            "E_Chest == 'sports bra'", "images/EmmaCowgirl/Emma_Cowgirl_Bra_Sports_Arms.png",   # E_TitsUp = 1
            "True", Null(),
            )
    contains:
            # Arm clothing Over
        ConditionSwitch(    
            "E_Over == 'jacket'", "images/EmmaCowgirl/Emma_Cowgirl_Arms_Jacket.png",   # E_TitsUp = 1
            "True", Null(),
            )



# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /
image Emma_Cowgirl_Legs_S:                                                                        
    #Her Legs during sex
    contains:
            # spunk
        ConditionSwitch(    
            "'anal' in E_Spunk or 'in' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Sex.png", 
            "True", Null(),
            )
    contains:
            # Legs base
        ConditionSwitch(    
            "Trigger == 'hotdog'", "images/EmmaCowgirl/Emma_Cowgirl_Legs_Hotdog.png", 
            "True", "images/EmmaCowgirl/Emma_Cowgirl_Legs_Sex.png", 
            )
    contains:
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaCowgirl/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaCowgirl/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            )
    contains:
            # pubes
        ConditionSwitch(    
            "E_Pubes", "images/EmmaCowgirl/Emma_Pubes_Sex.png", 
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Belly.png", 
            "True", Null(),
            )
    zoom 1 
#    offset (0,0)

image Emma_Cowgirl_Legs_A:                        
    #Her Legs during anal
    contains:
            # anal spunk
        ConditionSwitch(    
            "'anal' in E_Spunk and not Speed", "images/EmmaCowgirl/Emma_Spunk_Anal_Closed.png", 
            "True", Null(),
            )
    contains:
            # Legs Base
            "images/EmmaCowgirl/Emma_Cowgirl_Legs_Anal.png"
    contains:
            #Anus
        ConditionSwitch(  
            "P_Sprite and P_Cock == 'anal' and Speed", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Emma_Cowgirl_Anus_A1",#heading
                    "True", "Emma_Cowgirl_Anus_A2",#faster
                    ),
            "True", "Emma_Cowgirl_Anus_A0",
            ) 
    contains:
            # pubes
        ConditionSwitch(    
            "E_Pubes", "images/EmmaCowgirl/Emma_Pubes_Anal.png", 
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaCowgirl/Emma_Pierce_Barbell_Pussy_A.png", 
            "E_Pierce == 'ring'", "images/EmmaCowgirl/Emma_Pierce_Ring_Pussy_A.png",
            "True", Null(), 
            )
    contains:
            # pussy spunk
        ConditionSwitch(    
            "'in' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Pussy.png", 
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Belly.png", 
            "True", Null(),
            )
        ypos -40
    zoom 1 
#    offset (0,0)

image Emma_Cowgirl_Pussy_Mask:
    contains:
            "images/EmmaCowgirl/Emma_Cowgirl_Pussy_Mask.png"
    contains:       
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaCowgirl/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaCowgirl/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            ) 

image Emma_Cowgirl_Hotdog_Mask:
    contains:
            "images/EmmaCowgirl/Emma_Cowgirl_Legs_HotdogMask.png"
#            yoffset 3
    contains:       
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaCowgirl/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaCowgirl/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            ) 
    contains:
            # piercings
        ConditionSwitch(    
            "E_Panties and not E_PantiesDown", Null(), 
            "E_Legs and not E_Upskirt", Null(), 
            "E_Pierce == 'barbell'", "images/EmmaCowgirl/Emma_Pierce_Barbell_Pussy_S.png", 
            "E_Pierce == 'ring'", "images/EmmaCowgirl/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(), 
            )
            
# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /



#  Sex animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Cowgirl_Body_H0:                                                                        
    #Her Body in the hotdog pose, idle
    contains:
        "Emma_Cowgirl_Body"   
        subpixel True          
        pos (0,-10) #top
        block:
            ease 2 pos (0,0) #bottom
            ease 2 pos (0,-10) #top
            repeat

image Emma_Cowgirl_Body_H1:                                                                        
    #Her Body in the hotdog pose, slow
    contains:
        "Emma_Cowgirl_Body"     
        subpixel True        
        pos (0,-10) #top
        block:
            ease 1.5 pos (0,0) #bottom
            ease 1.5 pos (0,-10) #top
            repeat

image Emma_Cowgirl_Body_H2:                                                                        
    #Her Body in the hotdog pose, fast
    contains:
        "Emma_Cowgirl_Body" 
        subpixel True            
        pos (0,-10) #top
        block:
            ease .6 pos (0,10) #bottom
            ease .4 pos (0,-10) #top
            repeat

image Emma_Cowgirl_Body_H4:                                                                        
    #Her Body in the hotdog pose, cumming
    contains:
        "Emma_Cowgirl_Body"   
        subpixel True          
        pos (0,-80) #top
        block:
            ease 1.5 pos (0,-70) #bottom
            ease 2 pos (0,-80) #top
            pause .5
            repeat
            
image Emma_Cowgirl_Body_S0:                                                                        
    #Her Body in the sex pose, idle
    contains:
        "Emma_Cowgirl_Body"      
        subpixel True       
        pos (0,-60) #top (0,-10)
        block:
            ease 1 pos (0,-50) #bottom (0,0)
            ease 1 pos (0,-60) #top
            repeat

image Emma_Cowgirl_Body_S1:                                                                        
    #Her Body in the sex pose, slow
    contains:
        "Emma_Cowgirl_Body"  
        subpixel True           
        pos (0,-20) #top
        block:
            ease .75 pos (0,0) #bottom
            ease 1.5 pos (0,-20) #top
            pause 0.75
            repeat
            
image Emma_Cowgirl_Body_S2:                                                                        
    #Her Body in the sex pose, fast
    contains:
        "Emma_Cowgirl_Body"   
        subpixel True          
        pos (0,-50) #top
        block:
            ease 0.5 pos (0,20) #bottom
            ease 1.5 pos (0,-50) #top
#            pause 0.5
            repeat

image Emma_Cowgirl_Body_S3:                                                                        
    #Her Body in the sex pose, superfast
    contains:
        "Emma_Cowgirl_Body" 
        subpixel True            
        pos (0,-50) #top
        block:
            ease 0.25 pos (0,0) #bottom
            ease 0.5 pos (0,-50) #top
            repeat

image Emma_Cowgirl_Body_S4:                                                                        
    #Her Body in the sex pose, cumming
    contains:
        "Emma_Cowgirl_Body"      
        subpixel True       
        pos (0,-20) #top
        block:
            ease 0.5 pos (0,0) #bottom
            ease 1 pos (0,-20) #top
            repeat
            
image Emma_Cowgirl_Body_A0:                                                                       
    #Her Body in the anal pose, idle
    contains:
        "Emma_Cowgirl_Body"    
        subpixel True         
        pos (0,-115) #top (0,-20)
        block:
            ease 1 pos (0,-95) #bottom (0,-10)
            ease 1 pos (0,-115) #top
            repeat

image Emma_Cowgirl_Body_A1:                                                                        
    #Her Body in the anal pose, slow
    contains:
        "Emma_Cowgirl_Body"  
        subpixel True   
        pos (0,-80) #top (0,-40)
        block:
            easein 1 pos (0,-60) #bottom   (0,-20)
            easeout 2 pos (0,-40) #bottom  (0,0)
            pause 1
            easein 1 pos (0,-60) #top (0,-20)
            easeout 2 pos (0,-80) #top
            pause 1
            repeat
            
image Emma_Cowgirl_Body_A2:                                                                       
    #Her Body in the anal pose, fast
    contains:
        "Emma_Cowgirl_Body"  
        subpixel True           
        pos (0,-10) #top
        block:
            ease .30 pos (0,10) #mid   
            ease .50 pos (0,50) #bottom  
            pause .3
            ease .80 pos (0,-10) #top
            pause .1
            repeat

image Emma_Cowgirl_Body_A3:                                                                       
    #Her Body in the anal pose, very fast
    contains:
        "Emma_Cowgirl_Body"  
        subpixel True      
        pos (0,-10) #top
        block:  
            ease .40 pos (0,50) #bottom  
            ease .60 pos (0,-10) #top
            repeat

image Emma_Cowgirl_Body_A4:                                                                       
    #Her Body in the anal pose, cumming
    contains:
        "Emma_Cowgirl_Body"    
        subpixel True         
        pos (0,20) #top (0,-20)
        block:
            ease 1 pos (0,40) #bottom (0,-10)
            ease 1 pos (0,20) #top
            repeat
            
# Leg animations / / / / / / Legs / / / / / / Legs / / / / / / Legs / / / / / / Legs / / / / / /
image Emma_Cowgirl_Legs_H0:
    # Her Legs in the Hotdog pose, idle
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95   
            parallel:
                ease 2 zoom .98 #bottom
                ease 2 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease 2 ypos 360 #bottom
                ease 2 ypos 340 #top
#                pause .3
                repeat    
    contains:
            #Cock
            ConditionSwitch(  
                "P_Sprite", "Zero_Doggy_Insert", 
                "True", Null(),
                )          
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Hotdog_Mask")#"images/EmmaCowgirl/Emma_Cowgirl_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95    
            parallel:
                ease 2 zoom .98 #bottom
                ease 2 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease 2 ypos 360 #bottom
                ease 2 ypos 340 #top
#                pause .3
                repeat     
    # End Legs Hotdog Idle

image Emma_Cowgirl_Legs_H1:
    # Her Legs in the Hotdog pose, slow
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,300) #top (528,300)
            zoom .9   
            parallel:
                ease 1.5 zoom 1 #bottom
                ease 1.5 zoom .9 #top
                pause .3
                repeat
            parallel:
                ease 1.5 ypos 390 #bottom
                ease 1.5 ypos 300 #top
                pause .3
                repeat    
    contains:
            #Cock
            ConditionSwitch(  
                "P_Sprite", "Zero_Doggy_Insert", 
                "True", Null(),
                )          
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Hotdog_Mask")#"images/EmmaCowgirl/Emma_Cowgirl_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,300) #top(515,300) 
            zoom .9   
            parallel:
                ease 1.5 zoom 1 #bottom
                ease 1.5 zoom .9 #top
                pause .3
                repeat
            parallel:
                ease 1.5 ypos 390 #bottom
                ease 1.5 ypos 300 #top
                pause .3
                repeat    
    # End Legs Hotdog slow

image Emma_Cowgirl_Legs_H2:
    # Her Legs in the Hotdog pose, fast
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95   
            parallel:
                ease .6 zoom 1 #bottom
                ease .4 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease .6 ypos 390 #bottom
                ease .4 ypos 340 #top
#                pause .3
                repeat    
    contains:
            #Cock
            ConditionSwitch(  
                "P_Sprite", "Zero_Doggy_Insert", 
                "True", Null(),
                )          
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Hotdog_Mask")#"images/EmmaCowgirl/Emma_Cowgirl_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95   
            parallel:
                ease .6 zoom 1 #bottom
                ease .4 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease .6 ypos 390 #bottom
                ease .4 ypos 340 #top
#                pause .3
                repeat    
    # End Legs Hotdog fast
  
image Emma_Cowgirl_Legs_H4:
    # Her Legs in the Hotdog pose, cumming
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
#            anchor (.515,.5)
            pos (0,-80) #top
            parallel:
                ease 2 ypos -70 #bottom
                ease 2 ypos -80 #top
                repeat
                
    contains:
            #Cock
            "Blowcock" 
            alpha 0.9
            zoom 0.5
            pos (680,440)   
#    contains:
#            #Cock
#            ConditionSwitch(  
#                "P_Sprite", "Zero_Doggy_Insert", 
#                "True", Null(),
#                )          
#            alpha 1
#            zoom 1.2
#            pos (450,590)
#    contains:
#            #Overlay
#            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Hotdog_Mask")#"images/EmmaCowgirl/Emma_Cowgirl_Legs_HotdogMask.png")
#            subpixel True
#            anchor (.515,.5)
#            pos (528,340) #top (528,300)
#            zoom .95    
#            parallel:
#                ease 2 zoom .98 #bottom
#                ease 2 zoom .95 #top
##                pause .3
#                repeat
#            parallel:
#                ease 2 ypos 360 #bottom
#                ease 2 ypos 340 #top
##                pause .3
#                repeat     
    # End Legs Hotdog Idle
                
# Emma's sex legs animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Cowgirl_Legs_S0:
    # Her Legs in the Sex pose, idle
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            pos (0,-140) #top
            parallel:
                ease 1 ypos -135 #bottom
                ease 1 ypos -140 #top
                repeat
            parallel:
                ease 2 xpos -8 #bottom
                ease 2 xpos 8 #top
                repeat
    contains:
            #Cock
            "Blowcock" 
            alpha 0.9
            zoom 0.5
            pos (680,400)         
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Pussy_Mask")#"images/EmmaCowgirl/Emma_Cowgirl_Pussy_Mask.png")
            subpixel True
            pos (0,-140) #top
            parallel:
                ease 1 ypos -135 #bottom
                ease 1 ypos -140 #top
                repeat
            parallel:
                ease 2 xpos -8 #bottom
                ease 2 xpos 8 #top
                repeat
    # End Legs Sex Idle

image Emma_Cowgirl_Legs_S1:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.75 ypos -50 #bottom
                pause 0.75
                ease 1.5 ypos -120 #top
                repeat
    contains:
            #Cock
            "Blowcock"      
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (680,400)
            block:
                ease 0.8 ypos 410
                pause 1
                ease 1.2 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Pussy_Mask")
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.75 ypos -50  #bottom
                pause 0.75
                ease 1.5 ypos -120 #top
                repeat
    # End Legs Sex slow
    
image Emma_Cowgirl_Legs_S2:
    # Her Legs in the Sex pose, fast
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            pos (0,-150) #top
            block:
                ease 0.5 ypos 0 #bottom
                pause 0.5
                ease 1 ypos -150 #top
                repeat
    contains:
            #Cock
            "Blowcock"     
            subpixel True 
            alpha 0.9
            zoom 0.5
            pos (680,400)
            block:
                ease 0.4 ypos 430
                pause 1
                ease 0.6 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Pussy_Mask")
            subpixel True
            pos (0,-150) #top
            block:
                ease 0.5 ypos 0 #bottom
                pause 0.5
                ease 1 ypos -150 #top
                repeat
    # End Legs Sex fast

image Emma_Cowgirl_Legs_S3:
    # Her Legs in the Sex pose, very fast
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.25 ypos 10 #bottom
                ease 0.5 ypos -120 #top
                repeat
    contains:
            #Cock
            "Blowcock"      
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (680,400)
            block:
                ease 0.2 ypos 430
                ease 0.55 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Pussy_Mask")
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.25 ypos 10 #bottom
                ease 0.5 ypos -120 #top
                repeat
    # End Legs Sex very fast

image Emma_Cowgirl_Legs_S4:
    # Her Legs in the Sex pose, cumming
    contains:
            #Body
            "Emma_Cowgirl_Legs_S"
            subpixel True
            pos (0,0) #top
            block:
                ease 0.5 ypos 10 #bottom
                ease 1 ypos 0 #top
                repeat
    contains:
            #Cock
            "Blowcock"      
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (680,430)
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_S", "Emma_Cowgirl_Pussy_Mask")
            subpixel True
            pos (0,0) #top
            block:
                ease 0.5 ypos 10 #bottom
                ease 1 ypos 0 #top
                repeat
    # End Legs Sex cumming
# Anal / / / / / / Anal / / / / / / Anal / / / / / / Anal / / / / / / Anal / / / / / /    
image Emma_Cowgirl_Legs_A0:
    # Her Legs in the anal pose, idle
    contains:
            #Base Legs
            "Emma_Cowgirl_Legs_A"   
            subpixel True
            pos (0,-138) #top
            block:
                ease 1 ypos -134 #bottom
                ease 1 ypos -138 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            alpha 0.9
            zoom 0.5
            pos (681,420)
    # End Sex Legs Anal Idle

image Emma_Cowgirl_Legs_A1:
    # Her Legs in the anal pose, slow
    contains:
            #Base Legs
            "Emma_Cowgirl_Legs_A"   
            subpixel True
            pos (0,-130) #top
            block:
                ease 4 ypos -80 #bottom
                ease 4 ypos -130 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            alpha 0.9
            zoom 0.5
            pos (681,420)
    contains:
            #Overlay
            AlphaMask("Emma_Cowgirl_Legs_A", "Emma_Cowgirl_Anus_Mask_A1")  
            subpixel True
            pos (0,-130) #top
            block:
                ease 4 ypos -80 #bottom
                ease 4 ypos -130 #top
                repeat          
    # End Sex Legs Anal slow
 
image Emma_Cowgirl_Anus_Mask_A1:
    #mask for the slow anal pose
    contains:        
        contains:
            "images/EmmaCowgirl/Emma_Cowgirl_Anus_Mask.png" 
        contains:
                # spunk
            ConditionSwitch(    
                "'anal' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Open.png",
                "True", Null(),
                )
        subpixel True
        xzoom 0.5
        xpos  250 
        parallel:
            #8 total
            pause .2
            ease 2.2 xzoom 0.9 #bottom
            ease 0.6 xzoom 0.85 #bottom
            
            ease 0.75 xzoom 0.9 #bottom
            pause 0.5            
            ease 0.75 xzoom 0.85 #bottom
            
            ease 0.6 xzoom 0.9 #bottom
            ease 2.2 xzoom 0.5 #top
            pause .2
            repeat  
        parallel:
            pause .2  
            ease 2.2 xpos 50 #bottom
            ease 0.6 xpos 75 #bottom 125=75%
            
            ease 0.75 xpos 50 #bottom
            pause 0.5
            ease 0.75 xpos 75 #bottom
            
            ease 0.6 xpos 50 #bottom
            ease 2.2 xpos 250 #top
            pause .2
            repeat
    #end animation for mask in slow anal

image Emma_Cowgirl_Legs_A2:
    # Her Legs in the anal pose, fast
    contains:
            #Base Legs
            "Emma_Cowgirl_Legs_A"   
            pos (0,-80) #top
            subpixel True
            block:
                ease 1 ypos 0 #bottom
                ease 1 ypos -80 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (681,420)
            block:
                ease 1 ypos 430
                ease 1 ypos 400
                repeat
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Cowgirl_Legs_A", "images/EmmaCowgirl/Emma_Cowgirl_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(    
                    "'anal' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )   
            subpixel True  
            pos (0,-80) #top
            block:
                ease 1 ypos 0 #bottom
                ease 1 ypos -80 #top
                repeat    
    # End Sex Legs Anal fast
    
image Emma_Cowgirl_Legs_A3:
    # Her Legs in the anal pose, very fast
    contains:
            #Base Legs
            "Emma_Cowgirl_Legs_A"   
            subpixel True
            pos (0,-80) #top
            block:
                ease 0.5 ypos 20 #bottom
                ease 0.5 ypos -80 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (681,420)
            block:
                ease 0.5 ypos 430
                ease 0.5 ypos 400
                repeat
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Cowgirl_Legs_A", "images/EmmaCowgirl/Emma_Cowgirl_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(    
                    "'anal' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )     
            subpixel True
            pos (0,-80) #top
            block:
                ease 0.5 ypos 20 #bottom
                ease 0.5 ypos -80 #top
                repeat 
    # End Sex Legs Anal very fast

image Emma_Cowgirl_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Base Legs
            "Emma_Cowgirl_Legs_A"   
            subpixel True
            pos (0,15) #top
            block:
                ease 1 ypos 20 #bottom
                ease 1 ypos 15 #top
                repeat
    contains:
            #Cock
            "Blowcock"
            subpixel True
            alpha 0.9
            zoom 0.5
            pos (681,430)
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Cowgirl_Legs_A", "images/EmmaCowgirl/Emma_Cowgirl_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(    
                    "'anal' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )     
            subpixel True
            pos (0,15) #top
            block:
                ease 1 ypos 20 #bottom
                ease 1 ypos 15 #top
                repeat 
    # End Sex Legs Anal cumming
    
image Emma_Cowgirl_Anus_A0:
        #this is the animated stretched anus 
        "images/EmmaCowgirl/Emma_Cowgirl_Anus_Tight.png"
        xpos  0 
        
image Emma_Cowgirl_Anus_A1:                    
        #this is the animated stretched anus 
        contains:
            "images/EmmaCowgirl/Emma_Cowgirl_Anus_Open.png"          
        contains:
                # spunk
            ConditionSwitch(    
                "'anal' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        subpixel True
        xzoom 0.5
        xpos  250 
        parallel:
            #8 total
            pause .2
            ease 2.2 xzoom 0.9 #bottom
            ease 0.6 xzoom 0.85 #bottom
            
            ease 0.75 xzoom 0.9 #bottom
            pause 0.5            
            ease 0.75 xzoom 0.85 #bottom
            
            ease 0.6 xzoom 0.9 #bottom
            ease 2.2 xzoom 0.5 #top
            pause .2
            repeat  
        parallel:
            pause .2  
            ease 2.2 xpos 50 #bottom
            ease 0.6 xpos 75 #bottom 125=75%
            
            ease 0.75 xpos 50 #bottom
            pause 0.5
            ease 0.75 xpos 75 #bottom
            
            ease 0.6 xpos 50 #bottom
            ease 2.2 xpos 250 #top
            pause .2
            repeat
        #end animation for anus in slow animation
            
image Emma_Cowgirl_Anus_A2:
        #this is the animated stretched anus 
        contains:
            "images/EmmaCowgirl/Emma_Cowgirl_Anus_Open.png"  
        contains:
                # spunk
            ConditionSwitch(    
                "'anal' in E_Spunk", "images/EmmaCowgirl/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        xpos  0 
      
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Cowgirl_Launch(Line = "solo"): 
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
    if renpy.showing("Emma_Cowgirl"):
        return 
    $ P_Sprite = 1
    $ Speed = 0
    hide Emma_Sprite      
    if renpy.showing("Emma_BJ_Animation"):
        hide Emma_BJ_Animation
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation
    if renpy.showing("Emma_TJ_Animation"):
        hide Emma_TJ_Animation
    
    if E_Legs:          #temporary, change or remove when other clothing options are available
        $ E_Upskirt = 1
    if E_Panties:       #temporary, change or remove when other clothing options are available
        $ E_PantiesDown = 1
                
    show Emma_Cowgirl zorder 150:
        pos (575,470)
    with dissolve
    return
    
label Emma_Gowgirl_Reset:
    if not renpy.showing("Emma_Cowgirl"):
        return
    $ Emma_Arms = 2     
    hide Emma_Cowgirl  
    call Emma_Hide 
    show Emma_Sprite at SpriteLoc(E_SpriteLoc) zorder EmmaLayer:
        alpha 1
        zoom 1 offset (0,0) 
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /