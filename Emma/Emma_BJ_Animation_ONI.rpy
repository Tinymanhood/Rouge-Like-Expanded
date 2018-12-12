image Emma_BJ_Animation:
    ConditionSwitch(
        "OniBJ", "Emma_BJ_Animation_ONI",
        "True", "Emma_BJ_Animation_Mod",
        ),

image TempHairBack:
    "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png"         
    anchor (0.6, 0.0)                
    zoom .5       

image Emma_BJ_ONI_Blink:
    ConditionSwitch(
    "E_Eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
    "E_Eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
    "E_Eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_Eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",    
    "E_Eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
    "E_Eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
    "E_Eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
    "E_Eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
    "E_Eyes == 'squint'", "Emma_BJ_ONI_Squint",
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

image Emma_BJ_ONI_Squint:
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




# Start Emma Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element
#Emma BJ Over Sprite Compositing


image Emma_BJ_Animation_ONI:#BJ_NewTest:                                                                #core BJ animation   
    LiveComposite(    
        (858,928),  
        (-270,-160), ConditionSwitch( #-270,-160                                                                
            # Emma's hair backside 
            "Speed == 0", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_0()),               #Static
            "Speed == 1", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_1()),               #Licking
            "Speed == 2", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_2()),               #Heading
            "Speed == 3", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_3()),               #Sucking
            "Speed == 4", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_4()),               #Deepthroat
            "Speed == 5", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_5()),               #Cumming High
            "Speed == 6", At("Emma_BJ_ONI_HairBack", Emma_BJ_ONI_Head_6()),               #Cumming Deep
            "True", Null(),
            ),  
        (-20,270), ConditionSwitch(                                                                 
            # Emma's body, everything below the chin
            "Speed == 0", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_0()),           #Static
            "Speed == 1", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_1()),           #Licking
            "Speed == 2", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_2()),           #Heading
            "Speed == 3", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_3()),           #Sucking
            "Speed == 4", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_4()),           #Deepthroat
            "Speed == 5", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_5()),           #Cumming High
            "Speed == 6", At("Emma_BJ_ONI_Backdrop", Emma_BJ_ONI_Body_6()),           #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # Emma's head Underlay
            "Speed == 0", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_0()),               #Static
            "Speed == 1", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_1()),               #Licking
            "Speed == 2", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_2()),               #Heading
            "Speed == 3", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_3()),               #Sucking
            "Speed == 4", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_4()),               #Deepthroat
            "Speed == 5", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_5()),               #Cumming High
            "Speed == 6", At("Emma_BJ_ONI_Head", Emma_BJ_ONI_Head_6()),               #Cumming Deep
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(                                                                 
            # Cock
            "Speed == 0", At("Blowcock", Emma_BJ_ONI_Cock_0()),                    #Static
            "Speed == 1", At("Blowcock", Emma_BJ_ONI_Cock_1()),                    #Licking                        
            "Speed >= 2", At("Blowcock", Emma_BJ_ONI_Cock_2()),                    #Heading+                        
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(), 
            "Speed == 3", At(AlphaMask("Emma_BJ_ONI_Head", "Emma_BJ_ONI_MouthSuckingMask"), Emma_BJ_ONI_Head_3()), #Sucking
            "Speed == 4", At(AlphaMask("Emma_BJ_ONI_Head", "Emma_BJ_ONI_MouthSuckingMask"), Emma_BJ_ONI_Head_4()), #Deepthroat
            "Speed == 6", At(AlphaMask("Emma_BJ_ONI_Head", "Emma_BJ_ONI_MouthSuckingMask"), Emma_BJ_ONI_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (-270,-160), ConditionSwitch(                                                                 
            # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Emma_BJ_ONI_Head", "Emma_BJ_ONI_MaskHeadingComposite"), Emma_BJ_ONI_Head_2()), #Heading
            "Speed == 5", At(AlphaMask("Emma_BJ_ONI_Head", "Emma_BJ_ONI_MaskHeadingComposite"), Emma_BJ_ONI_Head_5()), #Cumming High
            "True", Null(),
            ),            
        (325,490), ConditionSwitch(                                                                
            # the over part of spunk
            "Speed < 3 or 'mouth' not in E_Spunk", Null(),
            "Speed == 3", At("Emma_BJ_ONI_SuckingSpunk", Emma_BJ_ONI_Head_3()), #Sucking
            "Speed == 4", At("Emma_BJ_ONI_SuckingSpunk", Emma_BJ_ONI_Head_4()), #Deepthroat
            "Speed == 6", At("Emma_BJ_ONI_SuckingSpunk", Emma_BJ_ONI_Head_6()), #Cumming Deep
            "True", Null(),
            ),    
        (325,490), ConditionSwitch(         #(325,490)                                                        
            # same as above, but for the heading animation
            "Speed == 2 and 'mouth' in E_Spunk", At("Emma_BJ_ONI_MaskHeadingSpunk", Emma_BJ_ONI_Head_2()), #Heading
            "True", Null(),
            ),   
        )
    zoom .55
    anchor (.5,.5)
    
image Emma_BJ_ONI_HairBack:
    #Hair underlay
    ConditionSwitch(                                                                            
            "E_Hair", "images/EmmaBJFaceONI/Emma_BJ_Hair_Wave_Back.png",            
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    
    
image Emma_BJ_ONI_Backdrop: 
    #add body here

image Emma_BJ_ONI_Backdrop:                                                                        
    #Her Body under the head
    LiveComposite(    
        (858,928),  
        (-375,250), ConditionSwitch(                                                                         
            #blanket
            "'blanket' in E_RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),  
        (0,0),"images/EmmaBJFaceONI/Emma_TJ_Body.png",                                                   
            #body
        (0,0), ConditionSwitch(                                                                         
            #tits
            "renpy.showing('Emma_TJ_Animation')", "images/EmmaBJFaceONI/Emma_TJ_Tits.png", #Titjob animation 
            "E_Chest == 'corset'", "images/EmmaBJFaceONI/Emma_TJ_Tits_Up.png",   # E_TitsUp = 1
            "E_Chest == 'sports bra' or E_Chest == 'lace bra'", "images/EmmaBJFaceONI/Emma_TJ_Tits_Up.png",   # E_TitsUp = 1
            "True", "images/EmmaBJFaceONI/Emma_TJ_Tits_Down.png",   # E_TitsUp = 0
            ), 
            
        )
    zoom 1.5 
    offset (-300,-200)
    
    
image Emma_BJ_ONI_Head:                                                                            #These are all the details of the face
    LiveComposite(    
        (858,928), 
         (0,0), ConditionSwitch(                                                                 
            #Hair behind face above body
            "E_Hair", "images/EmmaBJFaceONI/Emma_BJ_Hair_Wave_Mid.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Emma_BJ_Animation_ONI')", ConditionSwitch( 
                    # If the animation isn't sucking, or if not in BJ pose
                    "E_Blush", "images/EmmaBJFaceONI/Emma_BJ_FaceClosed_Blush.png",              
                    "True", "images/EmmaBJFaceONI/Emma_BJ_FaceClosed.png",
                    ),  
            "E_Blush", "images/EmmaBJFaceONI/Emma_BJ_FaceOpen_Blush.png",              
            "True", "images/EmmaBJFaceONI/Emma_BJ_FaceOpen.png"
            ),           
        (0,0), ConditionSwitch(                                                                         
            #Mouth
            "Speed and renpy.showing('Emma_BJ_Animation_ONI')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Sucking.png", #sucking
                    "Speed == 4", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Sucking.png", #deepthroat     
                    "Speed == 6", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Sucking.png", #cumming    
                    ),  
            "E_Mouth == 'normal'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Smile.png",
            "E_Mouth == 'lipbite'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Lipbite.png",
            "E_Mouth == 'sucking'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Sucking.png",            
            "E_Mouth == 'kiss'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Smile.png",  
            "E_Mouth == 'smirk'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Smirk.png",           
            "E_Mouth == 'grimace'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Smile.png",
            "E_Mouth == 'surprised'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Surprised.png",          
            "E_Mouth == 'tongue'", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Tongue.png",    
            "True", "images/EmmaBJFaceONI/Emma_BJ_Mouth_Smile.png",
            ),       
        (428,605), ConditionSwitch(   
            # Heading Mouth
            "not renpy.showing('Emma_BJ_Animation_ONI')", Null(),
            "Speed == 2", At("Emma_BJ_ONI_MouthHeading", Emma_BJ_ONI_MouthAnim()),  #heading 
            "Speed == 5", At("Emma_BJ_ONI_MouthHeading", Emma_BJ_ONI_MouthAnimC()), #cumming high    
            "True", Null(),
            ),  
        
        (0,0), ConditionSwitch(                                                                         
            #Spunk layer
            "'mouth' not in E_Spunk", Null(), 
            "Speed and renpy.showing('Emma_BJ_Animation_ONI')", ConditionSwitch( 
                    # If in sucking position
                    "Speed == 1", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/EmmaBJFaceONI/Emma_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/EmmaBJFaceONI/Emma_BJ_Spunk_SuckingUnder.png", #deepthroat     
                    "Speed == 6", "images/EmmaBJFaceONI/Emma_BJ_Spunk_SuckingUnder.png", #cumming    
                    ),  
            "E_Mouth == 'normal'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Smile.png",
            "E_Mouth == 'lipbite'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Lipbite.png",
            "E_Mouth == 'kiss'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Kiss.png",
            "E_Mouth == 'sad'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Sad.png",
            "E_Mouth == 'smile'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Smile.png", 
            "E_Mouth == 'smirk'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Smirk.png",
            "E_Mouth == 'surprised'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Surprised.png",
            "E_Mouth == 'tongue'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Tongue.png",
            "E_Mouth == 'sucking'", "images/EmmaBJFaceONI/Emma_BJ_Spunk_SuckingUnder.png",
            "True", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Smile.png",
            ),       
        (0,0), ConditionSwitch(                                                                         
            #Brows
            "E_Brows == 'normal'", "images/EmmaBJFaceONI/Emma_BJ_Brows_Normal.png",
            "E_Brows == 'angry'", "images/EmmaBJFaceONI/Emma_BJ_Brows_Angry.png",
            "E_Brows == 'sad'", "images/EmmaBJFaceONI/Emma_BJ_Brows_Sad.png",
            "E_Brows == 'surprised'", "images/EmmaBJFaceONI/Emma_BJ_Brows_Surprised.png",        
            "E_Brows == 'confused'", "images/EmmaBJFaceONI/Emma_BJ_Brows_Confused.png",
            "True", "images/EmmaBJFaceONI/Emma_BJ_Brows_Normal.png",
            ),
        (0,0), "Emma_BJ_ONI_Blink",                                                                
            #Eyes
        (0,0), ConditionSwitch(                                                                 
            #cum on the face
            "'facial' in E_Spunk", "images/EmmaBJFaceONI/Emma_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 
            #Hair overlay
            "E_Hair", "images/EmmaBJFaceONI/Emma_BJ_Hair_Wave_Top.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Emma_BJ_ONI_Blink:                                                                           
        #eyeblinks
        ConditionSwitch(
            "E_Eyes == 'normal'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Sexy.png",  
            "E_Eyes == 'sexy'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Sexy.png",  
            "E_Eyes == 'closed'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Closed.png",
            "E_Eyes == 'surprised'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Surprised.png",
            "E_Eyes == 'side'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Side.png",
            "E_Eyes == 'stunned'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Surprised.png",
            "E_Eyes == 'down'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Down.png",
            "E_Eyes == 'manic'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Surprised.png",
            "E_Eyes == 'squint'", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Squint.png",
            "True", "images/EmmaBJFaceONI/Emma_BJ_Eyes_Sexy.png",  
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3    
        "images/EmmaBJFaceONI/Emma_BJ_Eyes_Closed.png"
        .25
        repeat

image Emma_BJ_ONI_MouthHeading:                                          
    #the mouth used for the heading animations
    contains:
        "images/EmmaBJFaceONI/Emma_BJ_Mouth_Sucking.png"        
        zoom 1.4
        anchor (0.50,0.65)  #(0.50,0.65) 
        
image Emma_BJ_ONI_MouthSuckingMask:                                          
    #the mask used for sucking animations
    contains:
        "images/EmmaBJFaceONI/Emma_BJ_Mouth_SuckingMask.png"
        zoom 1.4
        
image Emma_BJ_ONI_MaskHeading:                                           
    #the mask used for the heading image 
    contains:
        "images/EmmaBJFaceONI/Emma_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Emma_BJ_ONI_MaskHeadingComposite:                                  
    #The composite for the heading mask that goes over the face
    LiveComposite(    
        (858,928),
        (300,462), ConditionSwitch(            
            "Speed == 2", At("Emma_BJ_ONI_MaskHeading", Emma_BJ_ONI_MouthAnim()),   
            "Speed == 5", At("Emma_BJ_ONI_MaskHeading", Emma_BJ_ONI_MouthAnimC()),      
            "True", Null(),
            ),  
        )
    zoom 1.8
    
image Emma_BJ_ONI_MaskHeadingSpunk:                                  
    #The composite for the heading mask that goes over the face
    contains:
            "images/EmmaBJFaceONI/Emma_BJ_Spunk_SuckingOver.png"
            subpixel True
            anchor (0.5, 0.65)
            zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base      
            block: #total time 1.0 down, 1.5 back up 2.5 total
                pause .20
                easein .15 zoom 0.66
                linear .15 zoom 0.60
                easeout .25 zoom 0.68 
                pause .25                           
                #1.0s to this point
                pause .40            
                easein .40 zoom 0.60
                linear .10 zoom 0.66
                easeout .30 zoom 0.58 
                pause .30                           
                #1.5s to this point            
                repeat
    zoom 2.5 #1.8
    yoffset 210#130
            
image Emma_BJ_ONI_SuckingSpunk:
    contains:
        "images/EmmaBJFaceONI/Emma_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)

            
transform Emma_BJ_ONI_MouthAnim():                                       
        #The animation for the heading mouth
        subpixel True
        zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base      
        block: #total time 1.0 down, 1.5 back up 2.5 total
            pause .20
            easein .15 zoom 0.66
            linear .15 zoom 0.60
            easeout .25 zoom 0.68 
            pause .25                           
            #1.0s to this point
            pause .40            
            easein .40 zoom 0.60
            linear .10 zoom 0.66
            easeout .30 zoom 0.58 
            pause .30                           
            #1.5s to this point            
            repeat


   
transform Emma_BJ_ONI_Head_2():                                 
    #The heading animation for her face
    subpixel True 
    offset (0,-40)     #top (0,-40), -20 is crown, 0 is mid
    block:
        ease 1 yoffset 40           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat



transform Emma_BJ_ONI_MouthAnimC():                                       
        #The animation for the heading mouth
        subpixel True
        zoom 0.7 #0.90      
        block: #total time 10 down, 15 back up
            pause .20            
            ease .50 zoom 0.65 #0.87
            pause .60                
            ease .30 zoom 0.7#0.9  
            pause .10                
            ease .30 zoom 0.65#0.9   
            pause .20 
            ease .30 zoom 0.7#0.9  
            repeat


#Cock Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Emma_BJ_ONI_Cock_0():                            
    #The angled static animation for the cock for starting
    anchor (.5,.5)
    rotate -10
transform Emma_BJ_ONI_Cock_1():                            
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat        
transform Emma_BJ_ONI_Cock_2():                            
    #The vertical static animation for the cock used in most sucking
    anchor (.5,.5)
    rotate 0
    alpha 1
#End Cock Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Head and Body Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /               
transform Emma_BJ_ONI_Head_0():                                
    #The starting animation for her face
    subpixel True 
    ease 1.5 offset (0,0)    
transform Emma_BJ_ONI_Body_0():                            
    #The starting animation for her body
    subpixel True 
    ease 1.5 offset (0,0)
    

transform Emma_BJ_ONI_Head_1():                                
    #The licking animation for her face
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
transform Emma_BJ_ONI_Body_1():                             
    #The licking animation for her body
    subpixel True 
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
        
            
transform Emma_BJ_ONI_Body_2():                            
    #The heading animation for her body
    subpixel True 
    offset (0,-40)     #top 
    block:
        ease 1 yoffset 15           #bottom         
        ease 1.5 offset (0,-40)     #top  
        repeat
        
transform Emma_BJ_ONI_Head_3():                                
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50) 
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50) 
        repeat    
transform Emma_BJ_ONI_Body_3():                            
    #The sucking animation for her body
    subpixel True 
    ease 0.5 offset (0,50)  
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat
    
transform Emma_BJ_ONI_Head_4():                                   
    #The deep animation for her face
    ease .5 offset (0,100) 
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100  
        repeat        
transform Emma_BJ_ONI_Body_4():                               
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100   
        repeat    

transform Emma_BJ_ONI_Head_5():                                 
    #The heading cumming animation for her face
    subpixel True 
    offset (0,-30)     #top 
    block:
        ease 1 yoffset -20           #bottom         
        ease 1.5 offset (0,-30)     #top  
        repeat
transform Emma_BJ_ONI_Body_5():                            
    #The heading cumming animation for her body
    subpixel True 
    offset (0,-30)     #top 
    block:
        ease 1 yoffset -20           #bottom         
        ease 1.5 offset (0,-30)     #top  
        repeat        
        
transform Emma_BJ_ONI_Head_6():                                   
    #The deep cumming animation for her face
    ease .5 offset (0,230) 
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230  
        repeat        
transform Emma_BJ_ONI_Body_6():                               
    #The deep cumming animation for her body
    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190   
        repeat    
        
                          
    
#Head and Body Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
