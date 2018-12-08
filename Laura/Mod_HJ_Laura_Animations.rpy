# Basic character Sprites


# Start Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Sex element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element



# Start Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Handjob element //////////////////////////////////////////////////////////////////////                                         Core Emma HJ element

image Laura_Hand_Under:
    "images/EmmaSprite/handemma2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    
    
image Laura_Hand_Over:
    "images/EmmaSprite/handemma1.png"    
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
     
transform Handcock_1E():
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

transform Handcock_2E():
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
            "not Speed", Transform("Emma_Hand_Under"), 
            "Speed == 1", At("Emma_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Under", Kitty_Hand_2()),
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
            "not Speed", Transform("Emma_Hand_Over"), 
            "Speed == 1", At("Emma_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Over", Kitty_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Laura_HJ_Launch(Line = 0): 
    if renpy.showing("Laura_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Laura_Hide
    if Line == "L":      
        show Laura_Sprite at SpriteLoc(StageRight) zorder newgirl["Laura"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
    else:     
        show Laura_Sprite at SpriteLoc(StageRight) zorder newgirl["Laura"].GirlLayer:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
        with dissolve
   
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ newgirl["Laura"].Girl_Arms = 2
    show Laura_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (100,250)#(100,250)
    return
    
label Laura_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Laura_HJ_Animation"):
        return    
    $ Speed = 0            
    $ newgirl["Laura"].Girl_Arms = 1
    hide Laura_HJ_Animation with easeoutbottom
    call Laura_Hide 
    show Laura_Sprite at SpriteLoc(E_SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Laura_Sprite at SpriteLoc(E_SpriteLoc) zorder newgirl["Laura"].GirlLayer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    return
    
# End Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    
    




