# start EmmaMeet //////////////////////////////////////////////////////////
# Check  #Emma_Update   to see what needs fixing still
label EmmaMeet:    
    $ bg_current = "bg classroom"   
    call CleartheRoom("Emma",0,1) from _call_CleartheRoom_30
    $ E_Loc = "bg emma"  
    $ E_Love = 300        
    $ E_Obed = 0            
    $ E_Inbt = 200 
    call Shift_Focus("Emma") from _call_Shift_Focus_157    
    call Set_The_Scene from _call_Set_The_Scene_137
    $ ESpriteLoc = StageRight
    call LastNamer from _call_LastNamer_3                         
    $ E_Petnames.append(_return)
    $ E_Petname = _return
        
    "You enter the classroom and have a seat." 
    "The bell to class rings, but Professor McCoy seems to be late."
    "A strange woman enters the room and heads to the podium with a regal stride."
    call EmmaFace("normal") from _call_EmmaFace_874
    show Emma_Sprite at SpriteLoc(ESpriteLoc) with easeinright     
    $ E_Loc = "bg classroom" 
    $ Emma_Arms = 1
    ch_u "Hello students. My name is Emma Frost, and I have been invited to conduct this class."
    ch_e "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect." 
    "She scans her eyes over the room, passing over each student."    
    call EmmaFace("surprised") from _call_EmmaFace_875
    pause 1
    call EmmaFace("sly",Mouth="sad") from _call_EmmaFace_876
    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)     
    $ E_Lust += 5
    "As her eyes pass over you, they briefly widen and then narrow."
    call EmmaFace("sly") from _call_EmmaFace_877
    ch_e "Very well, let us begin, class."
    call EmmaFace("normal") from _call_EmmaFace_878 
    "The class is pretty basic today, mostly a lecture on her areas of expertise, psychology and literature."
    $ E_Lust += 5
    "She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."
    $ E_Lust += 5
    call Wait from _call_Wait_34 
    call CleartheRoom("Emma",0,1) from _call_CleartheRoom_31
    $ E_Loc = "bg classroom" 
    call Set_The_Scene from _call_Set_The_Scene_138
    ch_e "All right students, class dismissed."
    ch_e "[E_Petname], could you wait a moment, I have something to discuss with you."    
    menu:
        extend ""
        "Yes?":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10) 
                call EmmaFace("normal") from _call_EmmaFace_879  
        "I've got places to be.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -15) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                call EmmaFace("angry") from _call_EmmaFace_880 
                ch_e "MR. [Playername], do not take that attitude with me."
                "She places herself in the doorway, preventing you from leaving."
        "For such a sexy teacher? I've got some time.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                call EmmaFace("angry",1, Mouth="smirk") from _call_EmmaFace_881 
                ch_e "That's rather. . . inappropriate."
                call EmmaFace("bemused", Mouth="smile") from _call_EmmaFace_882 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 20) 
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 25, 15)  
                ch_e "But also obvious, so I can't criticize you too harshly."
    
    ch_e "I've heard about you from Professor Xavier and. . . others." 
    
    if P_Rep <= 200:
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 15) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
        call EmmaFace("angry", Brows="confused") from _call_EmmaFace_883 
        ch_e "You seem to be a bit of a scoundrel. . ."        
    elif P_Rep < 600:
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 5) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
        call EmmaFace("sly") from _call_EmmaFace_884 
        ch_e "You have quite a reputation around campus. . ."
    else:
        call EmmaFace("smile") from _call_EmmaFace_885 
        ch_e "You have managed a reasonble reputation. . ."
        
    if R_SEXP >= 60 and K_SEXP >= 60:
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
        call EmmaFace("sly") from _call_EmmaFace_886 
        ch_e "and a number of conquests to your name. . ."
    elif R_SEXP >= 60 or K_SEXP >= 60:
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 2) 
        call EmmaFace("smile") from _call_EmmaFace_887 
        ch_e "and are not without some romantic entanglements. . ."
    else:
        call EmmaFace("smile", Brows="confused") from _call_EmmaFace_888 
        ch_e "though I haven't heard of much of a romantic life. . ."
        
    if P_Lvl >= 7:
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
        call EmmaFace("smile") from _call_EmmaFace_889 
        ch_e "but your grades have been excellent."
    elif P_Lvl >= 3:
        call EmmaFace("normal", Brows="confused") from _call_EmmaFace_890 
        ch_e "but your grades been marginal at best."
    else:
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 10, -5, 1)  
        call EmmaFace("normal", Brows="sad") from _call_EmmaFace_891 
        ch_e "but you haven't been living up to your potential in class."
    
    call EmmaFace("normal", Eyes="side") from _call_EmmaFace_892 
    ch_e "My particular interest in this case, however. . ."
    call EmmaFace("sly") from _call_EmmaFace_893 
    ch_e "is that I cannot get a \"read\" on you."
    call EmmaFace("sly", Mouth="normal") from _call_EmmaFace_894 
    ch_e "My mutant power is telepathy, the same as Professor Xavier's."
    ch_e "I've grown accustomed to knowing what those around me are thinking."
    call EmmaFace("bemused", Eyes="side") from _call_EmmaFace_895 
    ch_e "With you. . . I cannot do that, which presents an interesting. . ."
    call EmmaFace("sly") from _call_EmmaFace_896 
    ch_e "challenge. . ."
    menu:
        extend ""
        "I imagine it would.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                call EmmaFace("normal") from _call_EmmaFace_897 
                ch_e "Hmm, yes."
        "Huh.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -1) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, -1)
                call EmmaFace("confused", Mouth="normal") from _call_EmmaFace_898 
                ch_e ". . . yes."
                call EmmaFace("normal") from _call_EmmaFace_899 
        "So you can't see what I'm picturing right now?":
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                call EmmaFace("bemused") from _call_EmmaFace_900 
                pause 0.5
                call EmmaFace("bemused", Eyes="down") from _call_EmmaFace_901 
                "She glances downward."
                call EmmaFace("sly") from _call_EmmaFace_902 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10) 
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 15) 
                ch_e "I can't read your mind, but I'm not blind, [E_Petname]."
    ch_e "In any case, I think we should set aside some time to talk."
    ch_e "I'd like to make you a personal project, so I can see how you tick."
    menu:
        extend ""
        "I'd be ok with that.": 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                call EmmaFace("smile") from _call_EmmaFace_903 
                ch_e "Excellent, I look forward to it."
        "I don't know if you should experiment on your students.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
                call EmmaFace("normal", Mouth="sad") from _call_EmmaFace_904 
                ch_e "There's nothing for you to worry about."
                call EmmaFace("sly") from _call_EmmaFace_905 
                ch_e "I'll be. . . gentle."
        "If it means spending more time with you. . .":
                if ApprovalCheck("Emma", 295, "L"):
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
                    call EmmaFace("sly") from _call_EmmaFace_906 
                    ch_e "Oh, I believe we'll be spending a good deal of time together. . ."
                else:
                    call EmmaFace("angry") from _call_EmmaFace_907 
                    ch_e "Much as it may pain me, it would. . ."
                    call EmmaFace("normal") from _call_EmmaFace_908 
        "What do I get out of it?":
                if not ApprovalCheck("Emma", 290, "L"):
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                    call EmmaFace("angry") from _call_EmmaFace_909 
                    ch_e "You'll stand some chance of passing this class, [E_Petname]."
                    call EmmaFace("normal") from _call_EmmaFace_910 
                else:
                    if E_Obed > 0:
                        call EmmaFace("confused", Mouth="smirk") from _call_EmmaFace_911 
                        ch_e "What would you {i}like{/i} to \"get out of it?\""
                        menu:
                            extend ""
                            "I guess if it helps your \"research.\" . .":
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10) 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, -5)
                                    call EmmaFace("smile") from _call_EmmaFace_912 
                                    ch_e "I'm glad to see that you can be reasonable."
                            "Spending more time with you would be plenty. . .":
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 20, 5) 
                                    call EmmaFace("sly") from _call_EmmaFace_913 
                                    ch_e "It certainly should be."
                            "A kiss?":
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                                    call EmmaFace("surprised",1, Mouth="surprised") from _call_EmmaFace_914 
                                    ch_e "[E_Petname], that is incredibly inappropriate!"
                                    call EmmaFace("sadside",0,Brows="angry") from _call_EmmaFace_915 
                                    ch_e "I would {i}never{/i} consider such a thing with a student."
                                    if ApprovalCheck("Emma", 220, "I"):
                                        call EmmaFace("sly",1) from _call_EmmaFace_916 
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
                                        ch_e ". . .never. . ."
                            "I think you know what I'd want. . .":
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
                                    call EmmaFace("sly",Brows="angry") from _call_EmmaFace_917 
                                    ch_e "Yes, I imagine that I do. . ."
                                    if ApprovalCheck("Emma", 220, "I"):
                                        call EmmaFace("sly",1) from _call_EmmaFace_918 
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10) 
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
                                        ch_e "And we may be able to come to some sort of \"mutually beneficial\" arrangement."
                                    else:
                                        call EmmaFace("bemused",0) from _call_EmmaFace_919 
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
                                        ch_e "But figuring out whether I'm correct is the entire point here."
                    else: #if 0 Obedience
                        call EmmaFace("normal") from _call_EmmaFace_920 
                        ch_e "The satisfaction of helping my. . . studies."
                        if ApprovalCheck("Emma", 300, "L"):
                            call EmmaFace("sly") from _call_EmmaFace_921 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5) 
                            ch_e "-and maybe if you're good. . ."
                        else:
                            ch_e "-and nothing more."
     
    call EmmaFace("normal",0) from _call_EmmaFace_922 
    ch_e "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."   
    ch_e ". . . later. . ."
    hide Emma_Sprite with easeoutright 
    "She strides out of the room and down the hall."
    $ E_Loc = "bg emma"         
    $ E_History.append("met")          
    $ Round -= 10      
    return
            
# end EmmaMeet //////////////////////////////////////////////////////////  

# start EmmaMeet //////////////////////////////////////////////////////////
# Check  #Emma_Update   to see what needs fixing still
label EmmaMeetGym:    
    $ bg_current = "bg dangerroom"   
    call CleartheRoom("Emma",0,1) from _call_CleartheRoom_32
    $ E_Loc = "bg emma"  
    $ E_Gym = [2,0,0,"cape","NewX","corset","white panties",0,0,"white thigh high",0]  
    $ E_Over = "cape"
    $ E_Legs = 0
    $ E_Panties = "white panties"
    $ E_Neck = "NewX"      
    $ E_Hose = "white thigh high"
    $ E_Outfit = "gym"
    #$ E_Love = 300        
    #$ E_Obed = 0            
    #$ E_Inbt = 200 
    call Shift_Focus("Emma") from _call_Shift_Focus_158    
    call Set_The_Scene from _call_Set_The_Scene_139
    $ ESpriteLoc = StageCenter
    #call LastNamer                         
    #$ E_Petnames.append(_return)
    #$ E_Petname = _return

    "You enter the danger room." 
    show Emma_Sprite at SpriteLoc(ESpriteLoc)
    #"The bell to class rings, but Professor McCoy seems to be late."
label EmmaMeetGym_Waited:
    "You see Emma Frost's in a different outfit."
    call EmmaFace("normal") from _call_EmmaFace_923
    #$ E_Loc = "bg classroom" 
    $ Emma_Arms = 1
    ch_e "Hello students. My name is Emma Frost, and for now on, I'll be supervising some of the evening trainings."
    ch_e "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect." 
    "She scans her eyes over the room, passing over each student."    
    #call EmmaFace("surprised")
    #pause 1
    call EmmaFace("sly",Mouth="sad") from _call_EmmaFace_924
    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)     
    $ E_Lust += 5
    "As her eyes pass over you, they stop for a moment and then keep going."
    call EmmaFace("sly") from _call_EmmaFace_925
    ch_e "Very well, we will begin in a few moments."
    call EmmaFace("normal") from _call_EmmaFace_926 
    "You can't take your eyes off her bottom, she is wearing a very small underwear, barely covering her pussy lips"
    "She notices your looks and aproach you."
    $ E_Lust += 5
    ch_e "Is something wrong [E_Petname]?"
    #"She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."
    $ E_Lust += 5

    menu:
        extend ""
        "You're. . . not wearing much.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 5) 
                call EmmaFace("confused", Mouth="normal") from _call_EmmaFace_927 
                ch_e "Hmm, yes, it makes easier to move around, very useful in combat."
                call EmmaFace("normal") from _call_EmmaFace_928 
        "Huh, nothing, nothing wrong.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -1) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, -1)
                call EmmaFace("confused", Mouth="normal") from _call_EmmaFace_929 
                ch_e ". . . ok."
                call EmmaFace("normal") from _call_EmmaFace_930 
        "I'm lucky you can't see what I'm picturing right now.":
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                call EmmaFace("bemused") from _call_EmmaFace_931 
                pause 0.5
                call EmmaFace("bemused", Eyes="down") from _call_EmmaFace_932 
                "She glances downward."
                call EmmaFace("sly") from _call_EmmaFace_933 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10) 
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 15) 
                ch_e "I can't read your mind, but I'm not blind, [E_Petname]."

    ch_e "In any case, let's stop talking and start the training session."

    "The training session starts but you can't focus on the training, you can't take your eyes of Emma's body"
    "At some moments you swear you were able to see her pussy escape the tight underwear"
    $ E_OutfitDay = "gym"
    call Wait from _call_Wait_35 
    #call CleartheRoom("Emma",0,1)
    #$ E_Loc = "bg dangerroom" 
    #call Set_The_Scene
    ch_e "All right students, class dismissed."

    #ch_e "In any case, I think we should set aside some time to talk."
    #ch_e "I'd like to make you a personal project, so I can see how you tick."

     
    #call EmmaFace("normal",0) 
    "She looks at you and move her mouth without making a sound:"
    call EmmaFace("sly") from _call_EmmaFace_934
    #ch_e "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."   
    ch_e ". . . later. . ."
    hide Emma_Sprite with easeoutright 
    "She strides out of the room and down the hall."
    $ E_Loc = "bg emma"         
    $ E_History.append("metgym")          
    $ Round -= 10      
    $ E_OutfitDay = "teacher"

    return
            
# end EmmaMeetGym //////////////////////////////////////////////////////////            
           

# Event Emma_Teacher_Caught /////////////////////////////////////////////////////         
label Emma_Teacher_Caught(Girl = "That girl"):
    #add this scene for when Emma is a teacher, and catches one of the girls fucking around in class.
    ch_e "[Playername]? [Girl]? Could you stop what you're doing immediately?" 
    call Checkout(1) from _call_Checkout_66
    if Girl == "Rogue":
            call RogueFace("bemused", 2, Eyes="side") from _call_RogueFace_850            
            call AllReset("Rogue") from _call_AllReset_3
            $ renpy.pop_call()        
            $ renpy.pop_call()
            if ApprovalCheck("Rogue", 700, "I"): 
                    call RogueFace("bemused", 1) from _call_RogueFace_851  
                    "Rogue shrugs and returns to her seat."
                    $ R_LikeEmma += 2
            else: 
                    "Rogue jumps and dashes out of the room."
                    $ R_LikeEmma -= 2
                    $ R_Loc = "bg rogue"
                    hide Rogue
                    if "Rogue" in Party:
                        $ Party.remove("Rogue")
            $ R_Rep -= 1
            $ E_LikeRogue += 2
    elif Girl == "Kitty":
            call KittyFace("bemused", 2, Eyes="side") from _call_KittyFace_624  
            call AllReset("Kitty") from _call_AllReset_4
            $ renpy.pop_call()        
            $ renpy.pop_call()
            if ApprovalCheck("Kitty", 700, "I"): 
                    call KittyFace("bemused", 1) from _call_KittyFace_625 
                    "Kitty shrugs and returns to her seat."
                    $ K_LikeEmma += 2
            else: 
                    "Kitty jumps and dashes out of the room."
                    $ K_LikeEmma -= 2
                    $ K_Loc = "bg kitty"
                    hide Kitty_Sprite
                    if "Kitty" in Party:
                        $ Party.remove("Kitty")
            $ K_Rep -= 1
            $ E_LikeKitty += 2
    $ P_Rep -= 1             
    ch_e "Thank you."
    ch_e "And [Playername], see me after class for detention. . ."
    $ P_Traits.append("detention")
    jump Class_Room
    
# end Emma_Teacher_Caught //////////////////////////////////////////////////////////            
           
# Event Emma Sleepover /////////////////////////////////////////////////////  
label Emma_Sleepover(sleepover = 0):  #Emma_Update   
            #This event gets called from the Location menus when time passes in the Night timeframe.
            call Shift_Focus("Emma") from _call_Shift_Focus_159
            if R_Loc == bg_current and E_LikeRogue < 800:                
                    call CleartheRoom("Emma",1) from _call_CleartheRoom_33
            if K_Loc == bg_current and E_LikeKitty < 800:              
                    call CleartheRoom("Emma",1) from _call_CleartheRoom_34
                    
            if bg_current == "bg emma":
                    if Weekday < 4 or Weekday > 5:
                            ch_e "I'm afraid I have class tommorrow. . ."
                    else:
                            ch_e "I'm need to get some sleep in. . ."
            else:
                    ch_e "It's getting late, I should retire for the evening. . ."  
            if Day <= 14:        
                ch_e "It's been a pleasant evening, but it wouldn't be appropriate to stay after hours like this. . ."  
                #jump Return_Player    
                
            call EmmaFace("sexy", 1) from _call_EmmaFace_935
            if (E_Sleep >= 3 and ApprovalCheck("Emma", 800)) or ApprovalCheck("Emma", 1100, "LI"):                                 
                    #You've slept over several times and she still likes you
                    if bg_current == "bg emma":
                            ch_e "Are you spending the night?"
                    else:
                            ch_e "Would you like me to stay?"
                    $ sleepover = 1                    
            elif E_Sleep < 3 or not ApprovalCheck("Emma", 600):                            
                    #She doesn't especially want you there.  
                    if bg_current == "bg emma":
                        ch_e "I think you should probably get going." 
                    else:
                        ch_e "I should head back to my room."                    
            else: #If she's uninterested
                    if bg_current == "bg emma":
                        ch_e "You should leave, [E_Petname]." 
                    else:
                        ch_e "I hope to see you in class,[E_Petname]."
            if sleepover:            
                if R_Loc == bg_current:
                    ch_e "And of course you as well, Rogue."   
                if K_Loc == bg_current:
                    ch_e "And of course you as well, Kitten."
                                          
            menu:
                extend ""
                "Sure." if sleepover:
                        if E_Sleep <= 5:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5) if E_Love >= 500 else E_Love
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 25)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 25, 25) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                        ch_e "Great! I'll get changed."
                    
                "No, sorry." if sleepover:                  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 6)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 4)
                        $ E_Brows = "sad"
                        ch_e "Alright. . . see you tomorrow. . ."
                        $ sleepover = 0
                        
                "Ok, I'll head out. Good night." if not sleepover and bg_current == "bg emma":                        
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 25, 2)            
                        call EmmaFace("smile") from _call_EmmaFace_936
                        ch_e "Ok, good night. . ."
                "Ok, see you later then. Good night." if not sleepover and bg_current != "bg emma":                        
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 25, 2)            
                        call EmmaFace("smile") from _call_EmmaFace_937
                        ch_e "Yeah, 'night, [E_Petname]. . ."
                    
                "Are you sure I can't stay the night? . ." if not sleepover and not E_Sleep and bg_current == "bg emma": 
                        if ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 700, "L") or ApprovalCheck("Emma", 500, "O"):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_938                   
                            ch_e "Well, Maaaybeee. . ."
                            $ sleepover = 1 
                        else:                    
                            call EmmaFace("smile") from _call_EmmaFace_939
                            $ E_Brows = "confused"
                            ch_e "Ehhhh. . . no, not tonight, [E_Petname]. Sorry." 
                "Are you sure you can't stay? . ." if not sleepover and not E_Sleep and bg_current != "bg emma": 
                        if ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 700, "L") or ApprovalCheck("Emma", 500, "O"):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_940                   
                            ch_e "Well, Maaaybeee. . ."
                            $ sleepover = 1 
                        else:                    
                            call EmmaFace("smile") from _call_EmmaFace_941
                            $ E_Brows = "confused"
                            ch_e "Ehhhh. . . no, not tonight, [E_Petname]. Sorry." 
                            
                "That's not what you said the other night . ." if not sleepover and E_Sleep: #if she wants you gone  
                        if ApprovalCheck("Emma", 900)or ApprovalCheck("Emma", 700, "L") or ApprovalCheck("Emma", 500, "O"):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_942                  
                            ch_e "and that went pretty well. . ."
                            $ sleepover = 1
                        else:                    
                            call EmmaFace("smile") from _call_EmmaFace_943
                            $ E_Brows = "confused"
                            if bg_current == "bg emma":
                                ch_e "Um, no, 'fraid not. Scoot." 
                            else:                        
                                ch_e "Um, no, 'fraid not. I'll see ya." 
                    
            if sleepover: #If she agreed
                    if R_Loc == bg_current:
                        if R_LikeEmma >= 800:                                
                                ch_r "I'll get ready for bed then."   
                        else:        
                                ch_r "I'm actually going to head out. . ."           
                                call CleartheRoom("Emma",1) from _call_CleartheRoom_35 
                    if K_Loc == bg_current:
                        if K_LikeEmma >= 800:                                
                                ch_k "I'll get cleaned up."   
                        else:        
                                ch_k "I'll[K_like]take a raincheck on that. . ."           
                                call CleartheRoom("Emma",1) from _call_CleartheRoom_36 
                    if E_SEXP < 10 and not ApprovalCheck("Emma", 600, "I") and not ApprovalCheck("Emma", 600, "O"):
                            ch_e "Just keep your hands to yourself. . ."        
                    jump Emma_Morning
            jump Return_Player    
    
label Emma_Morning:
            #This label is jumped too from Emma Sleepover if you successfully stay the night
            call Shift_Focus("Emma") from _call_Shift_Focus_160
            call EmmaOutfit("sleep") from _call_EmmaOutfit_48
            "Emma changes into her sleepwear."
            ch_e "Ah, that's better."
            ch_e "Night, [E_Petname]"                                               #fix add sex option here
            show blackscreen onlayer black    
            pause 2
            call Wait(Lights = 0) from _call_Wait_36 
            $ E_Loc = bg_current
            call EmmaOutfit("sleep") from _call_EmmaOutfit_49
            
            $ D20 = renpy.random.randint(40, 70)                                #This element sends player to the Morningwood event        
            if "hungry" in E_Traits and D20 > 50:
                    $ Cnt = 1
            elif D20 >= E_Lust:
                    $ Cnt = 0     
            elif E_SEXP <= 15:
                    $ Cnt = 0         
            elif E_Blow >= 5 or ApprovalCheck("Emma", 900, "I"):
                    $ Cnt = 1
            elif E_Blow and ApprovalCheck("Emma", 900):
                    $ Cnt = 1
            elif ApprovalCheck("Emma", 1400): # Trinity < 1400
                    $ Cnt = 1
            else:
                    $ Cnt = 0 
                 
            if Cnt:   
                    call Emma_SexAct("morningwood") from _call_Emma_SexAct_7 
                    ch_e "Hmmm. . ."
                                    
            call EmmaFace("smile") from _call_EmmaFace_944
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            ch_e "G'morning . . ."
            menu:
                extend ""
                "It's always nice sleeping with you." if E_Sleep: 
                        if E_Sleep < 5:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 8)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 8)    
                        $ E_Blush = 1
                        ch_e "And that's always nice to hear."
                        ch_e "We'll have to keep this up."
                "I loved sleeping next to you." if not E_Sleep:
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 15)            
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 12)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 12)  
                        $ E_Blush = 2
                        ch_e "Yeah, I. .  I had fun too."
                        $ E_Blush = 1
                        ch_e "I wouldn't mind doing it again."   
                        $ E_Blush = 2
                        ch_e "You know, some other time. . . "
                        $ E_Blush = 1
                "It was fun.":
                        if not E_Sleep:                    
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)            
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 8)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 15)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15) 
                        elif E_Sleep < 5:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 8)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 35, 8)             
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 8)
                        if E_Love >= 800:
                            call EmmaFace("bemused") from _call_EmmaFace_945
                        else:
                            call EmmaFace("confused") from _call_EmmaFace_946
                        ch_e "Yeah, I mean I guess it was. . ."
                "You were constantly tossing around.":            
                        $ E_Blush = 1
                        if ApprovalCheck("Emma", 800, "L"):
                            call EmmaFace("bemused") from _call_EmmaFace_947
                        else:
                            call EmmaFace("angry") from _call_EmmaFace_948
                        if E_Sleep < 5:
                            ch_e "!"
                            ch_e "I don't make a habit out of it. . ."                       
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 60, -8)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 22)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 22)  
                        else:
                            ch_e "Yeah, well. . . you should be used to that!"
                "You need to learn to stick to your side.":  
                        if E_Sleep < 5:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -8) 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 40)  
                        if ApprovalCheck("Emma", 500, "O"):
                            call EmmaFace("normal") from _call_EmmaFace_949
                            ch_e "Fine, whatever."
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 8) if E_Sleep < 5 else E_Obed
                        else:
                            call EmmaFace("angry") from _call_EmmaFace_950
                            ch_e "That's not how you get me to come back." 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 35, 20) if E_Sleep < 5 else E_Inbt  
                        
            #fix add sex option here
            $ E_Blush = 0
            $ E_Sleep += 1    
            call Emma_Schedule from _call_Emma_Schedule_4
            call RogueFace("normal") from _call_RogueFace_852
            if E_Outfit != "sleep":
                "Emma changes out of her sleepwear."
            call EmmaOutfit(Changed=1) from _call_EmmaOutfit_50
            call Girls_Location from _call_Girls_Location_35
            return
    
# end Event Sleepover /////////////////////////////////////////////////////
# start Event Morning Wood /////////////////////////////////////////////////////

label Emma_MorningWood: #Emma_Update   
            # this label is called from the Emma_SexAct("morningwood"), 
            # which was called from Emma_Sleepover, which was called from a Location.
            call Shift_Focus("Emma") from _call_Shift_Focus_161
            $ P_Focus = 30
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 5)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5) 
            $ E_RecentActions.append("blanket")           
            call Emma_BJ_Launch from _call_Emma_BJ_Launch_13
            "You feel a pleasant sensation. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 5)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
            "It's somewhere below your waist. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 10)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
            $ Trigger = "blow"
            $ E_Eyes = "down"
            "You open your eyes. . ."
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            $ Speed = 3
            $ Count = 3
            $ Line = 0
            call Emma_First_Peen(1) from _call_Emma_First_Peen_1
            while Count > 0:
                    #Looping portion
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 10)
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                    menu:
                        extend ""
                        "Stay Quiet":
                            if Count >2:
                                "You just let her do her thing and pretend to still be asleep."
                            elif Count:
                                "It does feel nice. . ."
                            elif not Count:
                                "You wouldn't want to disturb her. . ."
                            ch_e "\"Slurp, slurp, slurp.\""
                        "Um, [E_Pet]? What're you doing?":
                            $ Line = "question"
                            $ Count = 1
                        "That feels great, keep going. . .":
                            $ Line = "praise"
                            $ Count = 1
                        "Hey, quit that!":
                            $ Line = "no"
                            $ Count = 1
                    $ Count -= 1
            $ Speed = 1
            $ E_Blush = 1
            "She pulls back with a pop."
            if Line == "question":
                    call EmmaFace("smile") from _call_EmmaFace_951
                    ch_e "I wasn't being subtle about it, [E_Petname]." 
            elif Line == "praise":
                    call EmmaFace("smile") from _call_EmmaFace_952
                    ch_e "Mmm, hehe."
            elif Line == "no":
                    $ Speed = 0
                    call EmmaFace("angry") from _call_EmmaFace_953
                    $E_Brows = "confused"
                    ch_e "{i}That's{/i} the thanks I get?!"
            else:
                    ch_e "You can stop faking it, [E_Petname]. . ."
                    ch_e "This guy's telling me you're awake now."
                
            menu:
                extend ""
                "So, um, you want to get back to it?":
                        if Line != "no":
                            call EmmaFace("smile") from _call_EmmaFace_954
                            ch_e "Hehe, mmmm. . ."
                        elif Line == "no" and ApprovalCheck("Emma", 1750):
                            call EmmaFace("bemused") from _call_EmmaFace_955
                            ch_e "Wha? Well. . . I guess. . ."
                            $ Line = "maybe"
                        else:
                            call EmmaFace("angry") from _call_EmmaFace_956
                            ch_e "You can't walk that one back!"
                            ch_e "You can take care of that yourself."
                "Were you more interested in something else?":
                        if Line != "no":
                            call EmmaFace("sexy") from _call_EmmaFace_957
                            ch_e "Maaaybee. . . like what?"
                            $ Line = "sex"
                        elif Line == "no" and ApprovalCheck("Emma", 1650):
                            call EmmaFace("bemused") from _call_EmmaFace_958
                            ch_e "Oh, so you had something {i}else{/i} in mind. . ."
                            ch_e "Like what?"
                            $ Line = "sex"
                        else:
                            call EmmaFace("angry") from _call_EmmaFace_959
                            ch_e "Well not anymore!"   
                            ch_e "You can take care of that yourself."
                "Sorry, sorry, please continue." if Line == "no":
                        if (E_Love + E_Obed + E_Inbt) >= 1450:
                            call EmmaFace("bemused") from _call_EmmaFace_960
                            ch_e "I guess I can forgive you. . ."
                            $ Line = "maybe"
                        else:
                            call EmmaFace("angry") from _call_EmmaFace_961
                            ch_e "As if."
                "Sorry, but we could do something else." if Line == "no":
                        if ApprovalCheck("Emma", 1350):
                            call EmmaFace("sexy") from _call_EmmaFace_962
                            ch_e "I guess, maybe. . ."
                            ch_e "Like what?"
                            $ Line = "sex"
                        else:
                            call EmmaFace("angry") from _call_EmmaFace_963
                            ch_e "As if."
                "Not when I'm just waking up.":
                        call EmmaFace("angry") from _call_EmmaFace_964
                        ch_e "Aw. . ."
                        $E_Eyes = "side"
                        ch_e "Last time I do you a favor. . ."
                        $ Line = "no"
                        
            $ E_RecentActions.remove("blanket") 
            if Line == "no":
                    call Emma_BJ_Reset from _call_Emma_BJ_Reset_7
                    if bg_current == "bg player":  
                        ch_e "I'm out of here."
                    else:
                        ch_e "Get out of my face."
                    call EmmaOutfit from _call_EmmaOutfit_51
                    $ renpy.pop_call()
                    jump Return_Player
            elif Line == "sex":
                    call Emma_BJ_Reset from _call_Emma_BJ_Reset_8
                    $ Situation = "shift"
                    return
            else:
                    $ Line = 0
                    $ Speed = 1
                    $ Situation = "blow"
                    return 
            $ renpy.pop_call()
            return
    
# end Event Morning Wood /////////////////////////////////////////////////////    



# Event Emma_Caught_Masturbating  /////////////////////////////////////////////////////  

label Emma_Caught_Masturbating: #Emma_Update   
            #This label is called from a Location
            call Shift_Focus("Emma") from _call_Shift_Focus_162
            "You hear some odd noises coming from Emma's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call EmmaOutfit(Changed=1) from _call_EmmaOutfit_52    
            $ E_Upskirt = 1
            $ E_PantiesDown = 1
            call Set_The_Scene from _call_Set_The_Scene_140
            call EmmaFace("sexy") from _call_EmmaFace_965
            $ E_Eyes = "closed"
            $ Emma_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ E_DailyActions.append("unseen")
            $ E_RecentActions.append("unseen")    
            call Emma_SexAct("masturbate") from _call_Emma_SexAct_8
            if "angry" in E_RecentActions:
                return
        
#After caught masturbating. . .
            $ E_Eyes = "sexy"
            $ E_Brows = "confused"
            $ E_Mouth = "smile"
            if E_Mast == 1:        
                    $ E_Mouth = "kiss"
                    ch_e "I wasn't expecting visitors. . ."
                    $ E_Eyes = "side"
                    $ E_Mouth = "lipbite"        
                    ch_e "although for you I could make an exception. . ."
                    $ E_Eyes = "sexy"
                    $ E_Brows = "normal"         
                    $ E_Mouth = "smile"
                    ch_e "Perhaps next time you could knock?" 
            else:
                    ch_e "I notice you make a habit of dropping in."           
            $ Emma_Arms = 1  
            call EmmaOutfit from _call_EmmaOutfit_53    
            return
    
# end Emma_Caught_Masturbating/////////////////////////////////////////////////////




# Event Emma_Caught_Classroom  /////////////////////////////////////////////////////  

label Emma_Caught_Classroom:  
            #This label is called from a Location
            call Shift_Focus("Emma") from _call_Shift_Focus_163
            "As you walk down the halls, you hear some odd noises coming from the classroom."                           #fix this scene, pants option    
            show blackscreen onlayer black
            $ bg_current = "bg classroom"            
            call CleartheRoom("Emma",0,1) from _call_CleartheRoom_37
            call EmmaOutfit(Changed=1) from _call_EmmaOutfit_54     
            $ E_Loc = 0
            call Set_The_Scene from _call_Set_The_Scene_141
            $ E_Loc = "bg desk"
            $ Taboo = 0
            call EmmaFace("sexy") from _call_EmmaFace_966
            $ E_Eyes = "closed"
            $ Emma_Arms = 1
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ Trigger3 = "fondle pussy"
            $ Trigger5 = "fondle breasts"
            $ E_RecentActions.append("classcaught") 
            $ E_DailyActions.append("unseen")
            $ E_RecentActions.append("unseen")    
            $ Line = 0
            call DrainWord("Emma","no masturbation") from _call_DrainWord_137
            $ E_RecentActions.append("masturbation")                      
            $ E_DailyActions.append("masturbation") 
            "You see Ms Frost leaning back against her desk, her hands tracing slow paths across her body."
            call EM_Cycle from _call_EM_Cycle
            if "angry" in E_RecentActions:
                return
        
#After caught masturbating. . .
            $ E_Eyes = "sexy"
            $ E_Brows = "confused"
            $ E_Mouth = "normal"             
            $ Emma_Arms = 1  
            call EmmaOutfit from _call_EmmaOutfit_55    
            $ bg_current = "bg classroom"  
            call Display_Emma from _call_Display_Emma_5 
            if "classcaught" in E_History: 
                    ch_e "I notice you make a habit of dropping in."  
                    call EmmaOutfit from _call_EmmaOutfit_56      
            else:
                    # First time caught
                    $ E_History.append("classcaught") 
                    ch_e "Well."
                    call EmmaFace("angry", Eyes="side") from _call_EmmaFace_967
                    ch_e "It appears that you've caught me in a somewhat. . . compromising position. . ."
                    menu:
                        extend ""
                        "Yup.":
                                call EmmaFace("perplexed", Mouth="normal") from _call_EmmaFace_968         
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, -5)
                                ch_e "Er, well. . ."
                        "Are you supposed to be shlicking it in class?":
                                call EmmaFace("angry", Eyes="side") from _call_EmmaFace_969
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                ch_e "Hrm."
                                call EmmaFace("sly", Brows="angry") from _call_EmmaFace_970
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 3)
                                ch_e "I imagine I shouldn't, but you know how it can be,"
                                $ E_Brows = "normal"
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "-surrounded by attractive co-eds all day long. . ."
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "yourself included. . ."
                        "I think it was pretty hot.":
                                call EmmaFace("sly") from _call_EmmaFace_971
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 10) 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "Hmm, well I suppose I can't blame you for that. . ."
                        "What do you mean?":
                                call EmmaFace("angry") from _call_EmmaFace_972
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -10)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -5)
                                ch_e "I mean how I was. . ."
                                call EmmaFace("surprised") from _call_EmmaFace_973
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 15)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 15)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                ch_e "Oh!"
                                call EmmaFace("perplexed") from _call_EmmaFace_974
                                ch_e "Yes, obviously it was nothing, just getting some. . ."
                                $ E_Eyes = "side"
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "paperwork done. . ."
                                call EmmaFace("sly") from _call_EmmaFace_975
                                $ Line = 1
                    ch_e "So how did you want to handle this. . . situation?"
                    menu:
                        extend ""
                        "I think I can forget all about it.":
                                call EmmaFace("smile") from _call_EmmaFace_976
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 10)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15) 
                                ch_e "Thank you, [E_Petname]. I appreciate your discretion."
                                call EmmaFace("sly") from _call_EmmaFace_977
                                ch_e "Are you {i}certain{/i} there's nothing I could do to thank you?"
                        "What solution did you have in mind?":
                                call EmmaFace("sly") from _call_EmmaFace_978
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 15)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15) 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "Oh, I'm sure I could make it worth your while. . ."
                        "What situation?":
                                if Line != 1:
                                        call EmmaFace("confused") from _call_EmmaFace_979
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -10)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -5)
                                        ch_e "I mean how I was. . ."
                                        call EmmaFace("surprised") from _call_EmmaFace_980
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 15)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 15)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                        ch_e "Oh!"
                                        call EmmaFace("perplexed") from _call_EmmaFace_981
                                        ch_e "Yes, obviously it was nothing, just getting some. . ."
                                        $ E_Eyes = "side"
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        ch_e "paperwork done. . ."
                                        call EmmaFace("sly") from _call_EmmaFace_982
                                else:
                                        call EmmaFace("angry") from _call_EmmaFace_983
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                        ch_e "I do wonder if you're just being dense. . ."
                                        call EmmaFace("sly") from _call_EmmaFace_984
                                        ch_e "Still. . ."
                    $ Line = 0
                    $ MultiAction = 0
                    menu:
                        extend ""
                        "Could you strip?":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15) 
                                ch_e "So you wanted a better view of the action?"
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "I suppose I could accomodate that. . ."
                                ch_e "to a point. . ."
                                "Ms Frost walks to the door and locks it behind her."
                                $ Tempmod = 50
                                call E_Strip from _call_E_Strip
                        "Could you just keep going?":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 15)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15) 
                                ch_e "Oh, you wanted to watch some more?"
                                ch_e "I can't exactly blame you."    
                                $ E_Eyes = "down"
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "Were you going to put on a show as well?"
                                menu:
                                    "Yeah!":
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 10) 
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        ch_e "Excellent."
                                        if "cockout" not in P_RecentActions:
                                            call Emma_First_Peen from _call_Emma_First_Peen_2
                                        "You begin to stroke your cock."
                                        $ Trigger2 = "jackin"
                                    "No, you go ahead.":
                                        call EmmaFace("sad") from _call_EmmaFace_985
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -10)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                        ch_e "Pity."
                                call EmmaFace("sly") from _call_EmmaFace_986
                                "Ms Frost walks to the door and locks it behind her."
                                $ Taboo = 0
                                $Trigger = "masturbation"
                                $Trigger3 = "fondle breasts"
                                "Ms Frost leans back and runs her fingertips along her breasts."
                                $ Tempmod = 50
                                call EM_Cycle from _call_EM_Cycle_1
                        "Could I feel you up?":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 10) 
                                ch_e "Hmm, I could use some help . . .around the office. . . "
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "perhaps you have some suggestions?"
                                "Ms Frost walks to the door and locks it behind her."
                                $ Taboo = 0
                                $ Tempmod = 50
                                call E_FB_Prep from _call_E_FB_Prep
                        "Could you give me a hand? [[point to your cock]":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                                $ E_Brows = "surprised"
                                ch_e "I appreciate boldness, [E_Petname], but be a bit more realistic." 
                                $ E_Brows = "normal"
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "Perhaps instead I could just offer a little. . . token of my appreciation."
                                "Ms Frost walks to the door and locks it behind her."
                                $ Tempmod = 50
                                call E_Strip from _call_E_Strip_1
                        "I should just get going then.":
                                call EmmaFace("surprised") from _call_EmmaFace_987
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                                ch_e "Oh."
                                call EmmaFace("confused") from _call_EmmaFace_988
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -5) 
                                ch_e "Well, I suppose. . ."
                                call EmmaFace("perplexed") from _call_EmmaFace_989
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "I'll see you. . . in class then. . ."
                    call EmmaOutfit from _call_EmmaOutfit_57     
                    "Afterwards, Ms Frost collects her things and strides toward the door."
                    "She turns back with her hand on the door."
                    call EmmaFace("sly") from _call_EmmaFace_990
                    ch_e "Oh, and [E_Petname]?"
                    ch_e "You can just call me \"Emma.\""
                    $ EmmaName = "Emma"
                    $ E_Loc = "bg emma"
                    hide Emma_Sprite with easeoutleft
                    $ Round = 20 if Round > 20 else Round
                    $ MultiAction = 1
            return
    
# end Emma_Caught_Classroom/////////////////////////////////////////////////////


# Event Emma_Detention  /////////////////////////////////////////////////////  

label Emma_Detention:  
            #This label is called from a Location
            call Shift_Focus("Emma") from _call_Shift_Focus_164
            call CleartheRoom("Emma",0,1) from _call_CleartheRoom_38
            if "traveling" in P_RecentActions:
                "You enter the room and see [EmmaName] waiting for you at the back of the room."
            else:
                "After class, the students file out, and you wait a few minutes until they're all gone."
                "Once the last student leaves, [EmmaName] approaches you."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ E_Loc = "bg classroom"
            call EmmaOutfit from _call_EmmaOutfit_58    
            call Set_The_Scene from _call_Set_The_Scene_142     
            call EmmaFace("sly") from _call_EmmaFace_991
            $ Emma_Arms = 2
            $ Count = 0  
            call CleartheRoom("Emma",0,1) from _call_CleartheRoom_39
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in P_DailyActions:
                ch_e "I'm glad you take your. . . education seriously."
            else:
                #if you skipped detention
                call EmmaFace("surprised") from _call_EmmaFace_992  
                ch_e "Oh, [E_Petname], you really shouldn't skip your detention like that. . ."            
            $ P_Traits.remove("detention") 
            $ E_RecentActions.append("detention") 
            $ E_DailyActions.append("detention") 
            call EmmaFace("sly") from _call_EmmaFace_993  
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 3)
            ch_e "You've been such a naughty pupil. . ."
            $ Emma_Arms = 1
            call EmmaFace("sadside", Brows="normal") from _call_EmmaFace_994  
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
            ch_e "Chasing after those young girls. . ."            
            call EmmaFace("sly") from _call_EmmaFace_995  
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 3)
            if "detention" in E_History:
                ch_e "How will we deal with it this time?"
            else:
                #first time
                ch_e "What am I to do with you. . ."
                $ E_History.append("detention") 
            
            "[EmmaName] walks to the door and locks it behind her."
            $ Taboo = 0
            menu:
                extend ""
                "I guess I should focus on my studies.":  
                        if ApprovalCheck("Emma", 900) and "classcaught" in E_History:
                                call EmmaFace("perplexed") from _call_EmmaFace_996   
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -3) 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                ch_e "Oh. Really? I was thinking of a more. . . recreational punishment."
                                menu:
                                    extend ""
                                    "Kidding, of course, what should we do? [[sex stuff]":
                                        call EmmaFace("sly") from _call_EmmaFace_997  
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                        ch_e "Why do I put up with you?"
                                        call Emma_SexMenu from _call_Emma_SexMenu_4
                                    "No, you're right, I take my education too lightly.":
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1) 
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -2) 
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        ch_e "Oh. Ok. Um. . ."
                                        call EmmaFace("sad") from _call_EmmaFace_998  
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        $ P_XP += 10
                        else:
                                        #She's not into you yet.
                                        call EmmaFace("sad", Mouth="normal") from _call_EmmaFace_999  
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 5) 
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 5) 
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        ch_e "Yes. . . Exactly. . ."
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                        $ P_XP += 10
                "I could think of a few things. . . [[sex stuff]":
                        if ApprovalCheck("Emma", 900) and "classcaught" in E_History:
                                call EmmaFace("sly") from _call_EmmaFace_1000  
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                                ch_e "I just bet you can. . ."
                                call Emma_SexMenu from _call_Emma_SexMenu_5
                        else:
                            #She's not into you yet.
                            call EmmaFace("sad", Mouth="smirk") from _call_EmmaFace_1001  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 5) 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                            ch_e "I'm sure you could. . . but unfortunately this isn't the time for it."
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5) 
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                            ch_e "We'll just have to settle for going over some of the topics from today's class. . ."
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                            $ P_XP += 10                            
            $ Round = 20 if Round > 20 else Round 
            ch_e "Ok, I think that's plenty for now. . ."
            ch_e "You wouldn't want to make this a habit. . ."
            call EmmaOutfit from _call_EmmaOutfit_59  
            return            
    
# end Emma_Detention/////////////////////////////////////////////////////


# Event Emma_Key /////////////////////////////////////////////////////  

#Not updated

label Emma_Key: #Emma_Update   
            call Shift_Focus("Emma") from _call_Shift_Focus_165
            call Set_The_Scene from _call_Set_The_Scene_143
            call EmmaFace("bemused") from _call_EmmaFace_1002
            $ Emma_Arms = 2
            ch_e "So you've been dropping by a lot lately, I figured you might want a key. . ."
            ch_p "Thanks."
            $ Emma_Arms = 1    
            $ Keys.append("Emma")
            $ E_Event[0] = 1
            return
# end Event Emma_Key /////////////////////////////////////////////////////


# Event Emma_Caught /////////////////////////////////////////////////////  

label Emma_Caught: #Emma_Update   
    call Shift_Focus("Emma") from _call_Shift_Focus_166
    call Checkout from _call_Checkout_67
    ch_e "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call EmmaOutfit from _call_EmmaOutfit_60
    $ bg_current = "bg study"  
    $ E_Loc = "bg study"
    call Set_The_Scene(0) from _call_Set_The_Scene_144

    show Professor at SpriteLoc(StageLeft)    
    show Emma_Sprite at SpriteLoc(StageRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease

    # show Professor at center
    # with fade
    call XavierFace("shocked") from _call_XavierFace_7
    call EmmaFace("sad") from _call_EmmaFace_1003
    ch_x "I'm very disappointed in your behavior, the both of you."
    
    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "lick pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blow":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"
    
    if E_Shame >= 40:
        ch_x "Emma, my dear, you're practically naked! At least throw a towel on!"
        "He throws Emma the towel."
        show blackscreen onlayer black 
        $ E_Over = "towel"         
        hide blackscreen onlayer black
    elif E_Shame >= 20:
        ch_x "Emma, my dear, that attire is positively scandalous."
    
    if E_Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2) from _call_RogueFace_853
        ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1) from _call_RogueFace_854
        $ R_Eyes = "side"
        
    $ Count = E_Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if E_Caught < 5:
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, -25)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -10) 
            call XavierFace("happy") from _call_XavierFace_8  
            if E_Caught:
                ch_x "But you know you've done this before. . . at least [E_Caught] times. . ." 
            elif R_Caught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [R_Caught] times. . ." 
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
            
        "Just having a little fun, right [E_Pet]?":
            call Emma_Namecheck from _call_Emma_Namecheck_20
            call EmmaFace("bemused") from _call_EmmaFace_1004         
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 5)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 10)   
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10) 
            call XavierFace("angry") from _call_XavierFace_9
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, -20)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Psi, Emma!" if "Xavier's photo" in P_Inventory and P_Lvl >= 5:
            if ApprovalCheck("Emma", 1500, TabM=1, Loc="No"):                   
                    jump Plan_Psi
            elif ApprovalCheck("Emma", 1000, TabM=1, Loc="No"):
                    call EmmaFace("perplexed") from _call_EmmaFace_1005 
                    $ E_Brows = "sad"
                    ch_e "You know. . . I really don't think that's a good idea. . ."
                    menu:
                        "Dammit Emma. . .":
                                call EmmaFace("angry") from _call_EmmaFace_1006
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5) 
                        "Yeah, I guess you're right. . .":
                                call EmmaFace("bemused") from _call_EmmaFace_1007 
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5) 
            else:
                    call EmmaFace("confused") from _call_EmmaFace_1008 
                    ch_e "Wait, Plan what??"
                    ch_p "Plan {i}Psi!{/i} . . you know. . ."
                    ch_e "I have no {i}idea{/i} what you're talking about."
                    ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                    call EmmaFace("bemused") from _call_EmmaFace_1009 
            call XavierFace("angry") from _call_XavierFace_10
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, -10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -5)   
            ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call EmmaFace("surprised") from _call_EmmaFace_1010
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 25)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 40)  
            call XavierFace("angry") from _call_XavierFace_11
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!" 
            if E_Inbt > 50:
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 15)             
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, -20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -10)    
            ch_x "Now get out of my sight."
            
    $ PunishmentX += Count            
    $ E_Caught += 1
    $ E_RecentActions.append("caught")
    $ E_DailyActions.append("caught")     
    if "Emma" in Party:
        $ Party.remove("Emma")     
    if "Rogue" in Party:
        $ Party.remove("Rogue")
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Psi: #Emma_Update   
    call EmmaFace("sly") from _call_EmmaFace_1011         
    "As you say this, a sly grin crosses Emma's face."
    #$ E_Arms = 0
    $ Emma_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic") from _call_XavierFace_12
    ch_x ". . ."
    call XavierFace("shocked") from _call_XavierFace_13
    "Xavier realizes with a shock that with your powers, his telepathy is useless."    
    $ Emma_Arms = 2
    show Emma_Sprite at SpriteLoc(650,150) with ease 
    $ ESpriteLoc = StageLeft
    "Emma moves in sits on his lap, pinning his arms to the chair."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised") from _call_RogueFace_855      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly") from _call_RogueFace_856
    call XavierFace("angry") from _call_XavierFace_14
    
    if "Kappa" in P_Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
    else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the photo you found earlier in his study."
            ch_p "I have here a rather. . . compromising photo of you and Mystique."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "Emma here's set it to distribute to every computer in school, every day."
            ch_p "And only I know the password." 
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ." 
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 40)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 30)
    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_e "Well, [E_Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if E_Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ E_Rules = 0
            "You know, it's kinda fun dodging you, catch us if you can." if not E_Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ E_Rules = 1
            "Raise my stipend." if P_Income < 30 and "Psi" not in P_Traits:    
                    ch_x "Very well. . . but I can only raise it by so much. . ."        
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Psi" in P_Traits:           
                    pass
            "I was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, although you don't seem to need it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room.[[Owned] (locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Emma's room." if "Emma" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."  
                            $ Keys.append("Emma")
                    "Give me the key to Emma's room.[[Owned] (locked)" if "Emma" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_x "Very well, that should conlude our business. Please leave." 
    if "Psi" not in P_Traits:
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 10)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 10)
        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
        $ P_Traits.append("Psi")
    $ Emma_Arms = 1
    "You return to your room"
    jump Player_Room
                              
# end Emma_Caught/////////////////////////////////////////////////////

# start Emma_BF//////////////////////////////////////////////////////////

label Emma_BF: #Emma_Update   
    call Shift_Focus("Emma") from _call_Shift_Focus_167
    
    if E_Loc != bg_current and "Emma" not in Party:
        "Emma approaches you and asks if the two of you can talk."
        "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."    
                
    $ E_Loc = bg_current
    call Set_The_Scene from _call_Set_The_Scene_145 
    call Taboo_Level from _call_Taboo_Level_34
    call CleartheRoom("Emma") from _call_CleartheRoom_40
    $ E_DailyActions.append("relationship")
    call EmmaFace("bemused", 1) from _call_EmmaFace_1012
    ch_e "So, [E_Petname], we've been hanging for a while, right?"
    ch_e ". . ."
    $ E_Eyes = "sexy"
    menu:
        ch_e "Right?"
        "Yeah. And it's been amazing.":
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
        "Yeah, I guess":
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 10)
        "Uhm. . .maybe?":
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
    if E_SEXP >= 10:
        ch_e "I mean, I've gone further with you than I've ever been with anybody before. . ."
    if E_SEXP >= 15:
        ch_e "You know . . .with a {i}student{/i}. . ."
    if "dating" in R_Traits and "dating?" in E_Traits:    
        ch_e "I know you're kinda Rogue's boyfriend and all. . . but she and I were talking and . . ."
    elif "dating" in E_Traits:
        ch_e "I know you're kinda Rogue's boyfriend and all. . ."
    if not E_Event[5]:
        ch_e "So, uhm. . ."
        ch_e "It’s not like I haven’t gone out with students before."
        ch_e "I just ..wow, this is so awkward.  I really like you a lot and. . ."
        ch_e "I mean. . . do you wanna be my boyfriend?"
        ch_e " maybe we could make it official?"
    elif "dating?" in E_Traits: 
        ch_e "Rogue said it’d totally be cool if we were dating, too." 
    elif "dating" in R_Traits: 
        ch_e "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:        
        ch_e "I wish you weren’t such a jerk sometimes, but still. . . I’m totally serious about this."
        ch_e "I wanna be your girlfriend officially."
    $ E_Event[5] += 1
    menu: 
        extend ""
        "Are you kidding?  I'd love to!":
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30)
            $ E_Petnames.append("boyfriend")
            $ E_Traits.append("dating")
            "Emma wraps her arms around you and starts kissing you passionately."
            call EmmaFace("kiss") from _call_EmmaFace_1013 
            $ E_Kissed += 1
        "Uhm okay.":
            $ E_Petnames.append("boyfriend")
            $ E_Traits.append("dating")
            $E_Brows = "confused"
            "Emma seems a little put off by how casually you’re taking all this."
            "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."    
        "I'm with Rogue now." if "dating" in R_Traits:             
            call EmmaFace("sad",1) from _call_EmmaFace_1014    
            ch_e "I know.  I just . . . I thought maybe you could go out with me, too, maybe?"
            menu:
                extend ""
                "Yes.  Absolutely.":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30)
                    $ E_Petnames.append("boyfriend")
                    $ E_Traits.append("dating")
                    "Emma wraps her arms around you and starts kissing you passionately."
                    call EmmaFace("kiss") from _call_EmmaFace_1015 
                    $ E_Kissed += 1
                "I'm sorry, but. .  .no.":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                    ch_e "Well. . . okay. I get it." 
                "No way.":
                    jump Emma_BF_Jerk
        "Not really.":
            jump Emma_BF_Jerk
    call EmmaFace("sexy") from _call_EmmaFace_1016    
    ch_e "Now. . . boyfriend. . . how about you and I celebrate, darling?"
    $ Tempmod = 10
    call Emma_SexMenu from _call_Emma_SexMenu_6
    $ Tempmod = 0
    return
    
label Emma_BF_Jerk:
    call EmmaFace("angry", 1) from _call_EmmaFace_1017
    ch_e "Fine! . . .be that way!" 
    $ Count = (20* E_Event[5])
    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 40)
    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, Count)
    if E_Event[5] >= 3:
        call EmmaFace("sad") from _call_EmmaFace_1018
        ch_e "Yeah?  Well. . . I don’t care what you want!  We’re dating!  Deal."   
        $ E_Petnames.append("boyfriend")
        $ E_Traits.append("dating")
        $ Achievements.append("I am not your Boyfriend!")
        ch_e "I. . .uhm. . .think I need to be alone for a little while."
        $ bg_current = "bg player"   
        call Set_The_Scene from _call_Set_The_Scene_146
        return        
    if E_Event[5] > 1:
        ch_e "It was such a mistake asking you again.  You’re still such a jerk!"          
    $ Count = (50* E_Event[5])                                  #fix test to see if negatives can work here.
    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -Count)
    ch_e "Get out, you big jerk!"
    $ E_Loc = "bg emma"
    $ bg_current = "bg player"   
    call Set_The_Scene from _call_Set_The_Scene_147
    $ renpy.pop_call()
    jump Player_Room
    
## end Emma_BF//////////////////////////////////////////////////////////

## start Emma_Love//////////////////////////////////////////////////////////
label Emma_Love: #Emma_Update   
    call Shift_Focus("Emma") from _call_Shift_Focus_168  
    if E_Event[6]:
            #on repeat attempts
            "Emma seems kind of shy and shuffles up to you, as if working up her nerve."
    elif bg_current != "bg emma":
        if E_Loc == bg_current or "Emma" in Party:
            "Suddenly, Emma says she wants to talk to you in her room and drags you over there."
        else:
            "Emma shows up, hurriedly says she wants to talk to you in her room and drags you over there."
        $ bg_current = "bg emma"
    else:
            "Emma suddenly stares at you very intently."
        
    $ E_Loc = bg_current
    call Set_The_Scene from _call_Set_The_Scene_148
    call CleartheRoom("Emma") from _call_CleartheRoom_41
    call Taboo_Level from _call_Taboo_Level_35
    $ E_DailyActions.append("relationship")
    call EmmaFace("bemused", 1) from _call_EmmaFace_1019
    $ E_Eyes = "side"    
    $ Line = 0
    $ E_Event[6] += 1
    if E_Event[6] == 1:
            if "dating" in E_Traits:
                ch_e "We've been together for a while now, and I've been thinking. . ."
            else:
                ch_e "We've know each other for a while now, and I've been thinking. . ."
            ch_e "It's been kinda hard for me to really get invested in anyone. . ."
            $ E_Eyes = "down"
            ch_e ". . . to be comfortable with who they are and be myself. . ."
            $ E_Eyes = "sly"
            ch_e "I just feel like sometimes you. . ."
            $ E_Eyes = "side"
            ch_e "and me  . ."
            call EmmaFace("perplexed", 2) from _call_EmmaFace_1020
            $ E_Eyes = "surprised"
            ch_e "Never mind!"
            "Emma dashes off and disappears behind the nearest door."
            hide Emma_Sprite with easeoutright
            call Remove_Girl("Emma") from _call_Remove_Girl_69
            return
    if E_Event[6] == 2:
        ch_e "Sorry about before, I don't think I was ready maybe. . ."
        ch_e ". . . but I was kind of thinking-"   
    elif E_Event[6] >= 5:
        ch_e "Um. . ."
        $ E_Eyes = "sly"
        ch_e "You know, it's time to stop running. I think I love you."
        $ E_Eyes = "side"
        ch_e "You don't have to say it back, but I do."
        $ E_Petnames.append("lover")
        ch_e "Um, that's all."
    else:
        ch_e "Um. . ."
    if "lover" not in E_Petnames: 
            menu:
                "She turns and makes a break for the nearest door."
                "Catch her":
                    call EmmaFace("perplexed", 2) from _call_EmmaFace_1021
                    $ E_Eyes = "surprised"
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 10) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 15) 
                    "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
                "Let her go":
                    "She dashes through the nearest door and vanishes from view."
                    jump Emma_Love_End    
            $ E_Blush = 1
            menu:
                extend ""
                "Pull her close":
                    call EmmaFace("smile", 1) from _call_EmmaFace_1022
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 20) 
                    "You draw her into an embrace, arms wrapped tightly around her waist."
                    $ Line = "hug"
                "Stay like this":
                    $ E_Eyes = "down"
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 10) 
                    "You keep hold of her wrist."
                    $ Line = "wrist"
                "Let her go":
                    if 1 < E_Event[6] < 4:
                        "You immediately release her wrist."
                        $ E_Eyes = "down"
                        "She dashes through the nearest door and vanishes from view."
                        jump Emma_Love_End
                    else:
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 10) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 20)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)  
                        "You release her wrist and she takes a step back."
                        
            ch_e "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in E_Petnames:        
            # If she hasn't confessed yet
            ch_e "I thought maybe if I let myself get too close. . ."
            ch_e "I'd fall. . ."
            menu:
                extend ""
                "I'll never let go." if Line:
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 20) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)  
                    "She melts into your arms."
                "I'd always catch you.":
                    call EmmaFace("smile") from _call_EmmaFace_1023
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 20) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 15)
                    "She smiles and shifts a bit uncomfortably."
                "Yeah, you should watch out for that.":
                    call EmmaFace("angry", 1) from _call_EmmaFace_1024
                    $ E_RecentActions.append("angry")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)  
                    "She shoves you away and then stomps through the nearest door."                        
                    jump Emma_Love_End
                    
                "So get going. [[Give her a shove]":
                    call EmmaFace("surprised", 1) from _call_EmmaFace_1025
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -50) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)  
                    "You shove her through the nearest door and then continue on you way."
                    $ E_RecentActions.append("angry")
                    hide Emma_Sprite with easeoutbottom
                    jump Emma_Love_End
                    
    if "lover" in E_Petnames: 
        #if she made the first move
        menu:
            extend "" #"I love you."
            "I love you too.":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 40) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 50)  
                        call EmmaFace("smile") from _call_EmmaFace_1026
            "You love me?":
                call EmmaFace("confused", 2) from _call_EmmaFace_1027
                menu:
                    ch_e "But you don't love me?"
                    "Yeah, of course I do!":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 60)  
                        call EmmaFace("smile") from _call_EmmaFace_1028
                    "I mean, a little?": 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 20)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -10)  
                        ch_e "That's not a \"yes.\" . ."
                        $ Line = "awkward"
                    "Not really.":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 30)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -30)  
                        call EmmaFace("angry", 2) from _call_EmmaFace_1029
                        ch_e "Huh?!"
                        $ Line = "awkward"
            "Huh.":
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -20)  
                menu:
                    ch_e "Huh?!"
                    "I mean, I love you too!":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)  
                        call EmmaFace("smile") from _call_EmmaFace_1030
                        ch_e "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 30)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -20)  
                        call EmmaFace("angry", 2) from _call_EmmaFace_1031
                        $ Line = "awkward"
            "Well that's awkward.":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 40)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -20)  
                        call EmmaFace("perplexed", 2) from _call_EmmaFace_1032
                        $ Line = "awkward"
    else:
        menu:
            extend ""
            "I love you, Emma.":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 50) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 30)  
                        call EmmaFace("smile") from _call_EmmaFace_1033
                        $ Line = "love"
            "I think you're pretty great.":
                call EmmaFace("confused") from _call_EmmaFace_1034
                menu:
                    ch_e "But you don't love me?"
                    "Yeah, of course I do!":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)  
                        call EmmaFace("smile") from _call_EmmaFace_1035
                    "I mean, a little?":
                        if ApprovalCheck("Emma", 1200, "OI"):
                            call EmmaFace("sad") from _call_EmmaFace_1036
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 20)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)  
                            ch_e "But not \"nothing\". . ."
                        else:
                            $ Line = "awkward"
                    "Not really.":     
                        call EmmaFace("sad") from _call_EmmaFace_1037                   
                        if ApprovalCheck("Emma", 1500, "OI"):
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 30)
                            ch_e "Ouch. . ."
                        else:
                            $ Line = "awkward"
            "I was thinking something more casual. . .":
                        call EmmaFace("sad") from _call_EmmaFace_1038
                        if ApprovalCheck("Emma", 1200, "OI") or ApprovalCheck("Emma", 700, "I"):
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 20)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 30)  
                            ch_e "Close enough."
                        else:  
                            $ Line = "awkward"
                            
    if Line == "awkward":   
        if ApprovalCheck("Emma", 700, "O"):   
            ch_e "Fine, this doesn't have to be love."
        elif ApprovalCheck("Emma", 700, "I"):
            ch_e "Fine, just sex it is."            
        elif ApprovalCheck("Emma", 1200, "OI"):
            ch_e "Fine, I can work with that."
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -50) 
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 50)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -50)  
            ch_e "Oh, well I mean if you don't love me-"
            ch_e "You don't have to love me, that's ok."
            ch_e "I'll, um. . . never mind."
            $ E_RecentActions.append("angry")
        $ E_Event[6] = 20 #this means it shuts down future attempts
    else:
        if Line:
            # If you're holding her
            "She squeezes you even tighter and makes a little whimper."
        else:
            "She dives into your arms with a little squeak."
        if "lover" not in E_Petnames:
            ch_e "I love you too. . ."
            ch_e "I think I have for a while now."
            $ E_Petnames.append("lover")
    
label Emma_Love_End:    
    if Line == "awkward" or "lover" not in E_Petnames:
            hide Emma_Sprite with easeoutright
            call Remove_Girl("Emma") from _call_Remove_Girl_70
            return
    if not E_Sex:
        ch_e "So I was thinking. . . did you want to . . ."
        if bg_current != "bg player" and bg_current != "bg emma":
                ch_e "Wait, let's take this someplace more private. . ."
                $ bg_current = "bg emma"
                $ E_Loc = bg_current
                call Set_The_Scene from _call_Set_The_Scene_149
                call CleartheRoom("Emma") from _call_CleartheRoom_42
                call Taboo_Level from _call_Taboo_Level_36
                ch_e "Ok, so like I was saying. . ."
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
        menu:
            extend ""
            "Yeah, let's do this. . . [[have sex]":      
                $ E_Inbt = Statupdate("Emma", "E_Inbt", E_Inbt, 30, 30) 
                ch_e "Hmm. . ."  
                call Emma_SexAct("sex") from _call_Emma_SexAct_9
            "I have something else in mind. . .[[choose another activity]":
                $ E_Brows = "confused"
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
                ch_e "Something like. . ."    
                $ Tempmod = 20
                call Emma_SexMenu from _call_Emma_SexMenu_7     
    return
    
label Emma_Love_Redux:
    #this is for if you rejected her but want a second chance
    $ Line = 0
    $ E_DailyActions.append("relationship")
    if E_Event[6] >= 25:
            #if this is the second time through
            ch_p "I hope you've forgiven me, I still love you."
            $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 10) 
            if ApprovalCheck("Emma", 950, "L"):
                $ Line = "love"
            else:
                call EmmaFace("sad") from _call_EmmaFace_1039   
                ch_e "You've dug too deep a hole, [E_Petname]."
                ch_e "Keep trying though." 
    else:
            ch_p "Remember when I told you that I didn't love you?"
            call EmmaFace("perplexed",1) from _call_EmmaFace_1040   
            ch_e "Um, YEAH?!"
            menu:
                "I'm sorry, I didn't mean it.":
                    $ E_Eyes = "surprised"
                    ch_e "Well, if you. . . so wait, you {i}do{/i} love me?"
                    ch_p "Yeah. I mean, yes, I love you, Emma."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 10) 
                    if ApprovalCheck("Emma", 950, "L"):
                        $ Line = "love"
                    else:
                        call EmmaFace("sadside") from _call_EmmaFace_1041   
                        ch_e "Well, I don't know how I feel at this point. . ."                        
                "I've changed my mind, so. . .":
                    if ApprovalCheck("Emma", 950, "L"):
                        $ Line = "love"
                        $ E_Eyes = "surprised"
                        ch_e "Really?!"
                    else:
                        $ E_Mouth = "sad"
                        ch_e "Oh, you've changed your mind. Wonderful."
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 10) 
                        call EmmaFace("sadside") from _call_EmmaFace_1042    
                        ch_e "Maybe I have too. . ."
                "Um, never mind.":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)  
                    call EmmaFace("angry") from _call_EmmaFace_1043   
                    ch_e "Seriously?"
                    $ E_RecentActions.append("angry")
    if Line == "love":
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 40) 
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 10) 
            call EmmaFace("smile") from _call_EmmaFace_1044    
            ch_e "I love you too!"
            if E_Event[6] < 25:             
                call EmmaFace("sly") from _call_EmmaFace_1045   
                "She slugs you in the arm"
                ch_e "Took you long enough."
            $ E_Petnames.append("lover")                
    $ E_Event[6] = 25
    return
## end Emma_Love//////////////////////////////////////////////////////////


# start Emma_Sub//////////////////////////////////////////////////////////

label Emma_Sub:     #Emma_Update   
    call Shift_Focus("Emma") from _call_Shift_Focus_169
    if E_Loc != bg_current and "Emma" not in Party:
        "Suddenly, Emma shows up and says she needs to talk to you."
    
    $ E_Loc = bg_current
    call Set_The_Scene from _call_Set_The_Scene_150
    call CleartheRoom("Emma") from _call_CleartheRoom_43
    call Taboo_Level from _call_Taboo_Level_37
    $ E_DailyActions.append("relationship")
    call EmmaFace("bemused", 1) from _call_EmmaFace_1046
    
    $ Line = 0
    ch_e "So, uhm. . .you've really kinda taken control in our relationship lately."
    menu:    
        extend ""        
        "I guess. That's just kind of what comes naturally for me.":   
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
        "Sorry. I didn't mean to come off like that.":
                call EmmaFace("startled", 2) from _call_EmmaFace_1047
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 5)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -5)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -5)
                ch_e "No!  Don't get the wrong idea!  I just. . ." 
        "Yup. Deal with it.": 
                if ApprovalCheck("Emma", 1000, "LO"):
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 20)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                        ch_e "Um, yeah. . ."
                else:
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                        call EmmaFace("angry") from _call_EmmaFace_1048
                        ch_e "I {i}was{/i} going to tell you I kinda liked it.  But I didn't think you'd be a {i}jerk{/i} about it!" #(Loss of points)
                        menu:        
                            extend ""
                            "Guess you don't know me so well, huh?":
                                    ch_e "I guess not."
                                    $ Line = "rude"
                            "Sorry.  I kind of thought you were getting into me being like that.": 
                                    call EmmaFace("sexy", 2) from _call_EmmaFace_1049
                                    $ E_Eyes = "side"
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                                    ". . ."
     
    $ E_Blush = 1       
    if not Line:
            # She's advancing to the next stage            
            ch_e "Well, I've, uhm. . . never had a student be like that with me before. . ."
            call EmmaFace("sly", 2) from _call_EmmaFace_1050
            ch_e "I think I kinda like it."
            call EmmaFace("smile", 1) from _call_EmmaFace_1051
            menu:
                extend ""
                "Good. If you wanna be with me, that's how it'll be.":
                        if ApprovalCheck("Emma", 1000, "LO"):
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 15)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                            ch_e "I guess I walked into that one. . ."                        
                        else:
                            call EmmaFace("sadside", 1) from _call_EmmaFace_1052
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)                      
                            ch_e "You don't have to do it {i}all{/i} the time.  You could still be nice once in a while."
                            menu:      
                                extend ""
                                "Whatever.  That's how it is.  Take it or leave it.":
                                        call EmmaFace("angry") from _call_EmmaFace_1053
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                                        ch_e "Y'know, you're such a jerk, [Playername]!" 
                                        $ Line = "rude"
                                "I think I could maybe do that." : 
                                        call EmmaFace("bemused", 2) from _call_EmmaFace_1054
                                        $ E_Eyes = "side"
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 5)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 3)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                                        ch_e "Uhm. . .yeah.  It's . . kinda hot."
                                
                "Yeah?  You think it's sexy?":
                            call EmmaFace("bemused", 2) from _call_EmmaFace_1055
                            $ E_Eyes = "side"
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                            ch_e "Uhm. . .yeah.  It's . . kinda hot."
                        
                "You sure you don't want me to back off a little?":  
                        call EmmaFace("startled", 1) from _call_EmmaFace_1056
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -5)
                        menu:
                            ch_e "Only if you think it might be weird. But I think it's kinda hot."
                            "Only if you're okay with it.":
                                call EmmaFace("bemused", 2) from _call_EmmaFace_1057
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 10)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                                $ Line = 0
                            "Uhm. . .yeah.  I {i}do{/i} think it's weird.  Sorry.":                                
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -5)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -10)
                                $ Line = "embarrassed"
                        
                "I don't really care what you like.  I do what I want.":
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 15)
                            call EmmaFace("angry") from _call_EmmaFace_1058
                            ch_e "Y'know, you're such a jerk, [Playername]!" 
                            $ Line = "rude"
                                        
    if not Line:
        call EmmaFace("bemused", 1) from _call_EmmaFace_1059
        $ E_Eyes = "down"
        ch_e "Cool.  So. . .just so you know. . .I don't mind you being in control."
        if "256 Shades of Grey" in E_Inventory:
                ch_e "Like in that '256 Shades of Grey' book."
        menu Emma_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -15)
                    $ Line = "embarrassed"
            "I think I could get used to that kinda thing.":
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                    call EmmaFace("smile", 1) from _call_EmmaFace_1060
                    $ Line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in E_Inventory and Line != "grey":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 5)
                    call EmmaFace("sly", 1) from _call_EmmaFace_1061
                    ch_e "You think I wouldn't read something you bought me?  I think you {i}maybe{/i} don't realize how much I like you."
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                    ch_e "Well, I {i}did{/i} read it.  And. . .it turns out it kinda . . {i}really{/i} turned me on."
                    ch_e "So. . .what d'you think?  Think maybe you'd like that?"
                    $ Line = "grey"
                    jump Emma_Sub_Choice

    if not Line:
        call EmmaFace("smile", 1) from _call_EmmaFace_1062
        ch_e "Awesome.  So. . .if you wanted me to, I could call you {i}sir{/i} or something."
        call EmmaFace("sly", 2) from _call_EmmaFace_1063
        ch_e "Think you'd like that?"        
        $ E_Blush = 1  
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 5)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 15)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                    ch_e "Okay, then. . .{i}sir{/i}."              
                    $ E_Petname = "sir"
            "I think I'd rather stick with what we've got going.":
                call EmmaFace("startled", 2) from _call_EmmaFace_1064
                ch_e "Oh!"
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -5)
                call EmmaFace("sadside", 1) from _call_EmmaFace_1065
                menu:
                    ch_e ". . . Well. . . maybe you can still kinda be in control, anyway?"
                    "I like that idea.":
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                            call EmmaFace("smile", 1) from _call_EmmaFace_1066
                            ch_e "You're so awesome, [E_Petname]."
                    "This is getting really weird.":
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -50)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -15)
                            $Line = "embarrassed"
        
#Emma_Sub_Bad_End:
    $ E_History.append("sir")
    if not Line:
            $ E_Blush = 1  
            "She gives you a piece of paper with the password for her cellphone calender."
            "Apparently, whatever you enter into it, she intends to do. . . within reason."
            $ E_Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":        
            hide Emma_Sprite with easeoutbottom                     
            call Remove_Girl("Emma") from _call_Remove_Girl_71
            $ renpy.pop_call()
            "Emma runs through the door in a huff, leaving you alone."
    elif Line == "embarrassed":
            call EmmaFace("sadside", 2) from _call_EmmaFace_1067
            ch_e "Oh!  Uhm, yeah!  I mean. . .."
            $ E_Mouth = "smile"
            ch_e "I was just kidding.  I . . yeah.  That's kinda weird."
            ch_e "I should go.  I think I hear Professor Xavier calling me."
            $ E_Blush = 1            
            hide Emma_Sprite with easeoutbottom                     
            call Remove_Girl("Emma") from _call_Remove_Girl_72
            $ renpy.pop_call()
            "Emma leaves through the door, leaving you alone. It didn't look like she could get away fast enough."
    return

label Emma_Sub_Asked: #Emma_Update   
    $ Line = 0
    call EmmaFace("sadside", 1) from _call_EmmaFace_1068
    ch_e "Yeah.  And I also remember what a {i}jerk{/i} you were to me about it."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in E_Petnames and ApprovalCheck("Emma", 850, "O"): 
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck("Emma", 550, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500 
                        pass
                else: #if it failed both those things,    
                        ch_e "Well maybe {i}I'm{/i} over that. . ." #Failed again. :(       
                        $ Line = "rude"
                        
                if Line != "rude":    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
                        call EmmaFace("sly", 1) from _call_EmmaFace_1069
                        ch_e "Well. . .okay.  I {i}did{/i} think that was pretty hot.  Also, you're super-cute when you apologize." 
                        #Blushing expression.  Emma kisses player and big addition of points
                        ch_e "Okay.  We can try again." 

        "Listen. . .I know it's what you want.  Do you want to try again, or not?":
                call EmmaFace("bemused", 1) from _call_EmmaFace_1070
                if "sir" in E_Petnames and ApprovalCheck("Emma", 850, "O"): 
                        ch_e "Ok, fine."
                elif ApprovalCheck("Emma", 600, "O"): 
                        ch_e "Um, ok."
                else: 
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        call EmmaFace("sadside", 1) from _call_EmmaFace_1071 
                        ch_e "You're totally impossible."
                        $ E_Eyes = "squint"
                        ch_e "Maybe you're right.  But I still think you should  apologize for being a jerk to me."
                        menu:
                            extend ""
                            "Okay, I'm sorry I was mean about it.":
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 15)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                                    call EmmaFace("bemused", 1) from _call_EmmaFace_1072
                                    $ E_Eyes = "side"
                                    ch_e "That's all you had to say."
                            "Not gonna happen.":
                                    if "sir" in E_Petnames and ApprovalCheck("Emma", 900, "O"): 
                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                                            ch_e ". . ."
                                    elif ApprovalCheck("Emma",650, "O"):  
                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                                            ch_e "I, um. . ."    
                                    else: #if it failed both those things,     
                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, -10)
                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -10)
                                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -15)                       
                                            "Emma sighs and rolls her eyes."
                                            call EmmaFace("angry", 1) from _call_EmmaFace_1073
                                            $ E_Eyes = "side"
                                            ch_e "You really don't learn, do you?"    
                                            $ Line = "rude"
                            "Ok, never mind then.":    
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1074
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, -10)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -10)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -15)
                                    ch_e "Y'know, if you're gonna throw that in my face, forget it."
                                    ch_e "I should've expected you'd be like that."
                                    $ Line = "rude"
    
    $ E_RecentActions.append("asked sub")   
    $ E_DailyActions.append("asked sub")     
    if Line == "rude":            
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Emma_Sprite with easeoutbottom                     
            call Remove_Girl("Emma") from _call_Remove_Girl_73
            $ E_RecentActions.append("angry")
            $ renpy.pop_call()
            "Emma hurries through the door, leaving you alone.  She looked pretty upset."
    elif "sir" in E_Petnames:
            #it didn't fail and "sir" was covered
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 50)
            $ E_Petnames.append("master")  
            $ E_Petname = "master"
            $ E_Eyes = "sly"
            ch_e ". . . master. . ."
    else:
            #it didn't fail
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
            $ E_Petnames.append("sir")  
            $ E_Petname = "sir"
            $ E_Eyes = "sly"
            ch_e ". . . sir."
    return

# end Emma_Sub//////////////////////////////////////////////////////////


# start Emma_Master//////////////////////////////////////////////////////////

label Emma_Master:  #Emma_Update   
    call Shift_Focus("Emma") from _call_Shift_Focus_170
    if E_Loc != bg_current and "Emma" not in Party:
        "Suddenly, Emma shows up and says she needs to talk to you."
    
    $ E_Loc = bg_current
    call Set_The_Scene from _call_Set_The_Scene_151
    call CleartheRoom("Emma") from _call_CleartheRoom_44
    $ E_DailyActions.append("relationship")
    call Taboo_Level from _call_Taboo_Level_38
    $ Line = 0
    call EmmaFace("bemused", 1) from _call_EmmaFace_1075
    ch_e "[E_Petname], if you don't mind me saying so. . ."
    ch_e "I think having you be in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
                call EmmaFace("sly", 1) from _call_EmmaFace_1076
                ch_e "Cool.  Maybe we could kick it up a notch?"
                menu:
                    extend ""
                    "Nah.  This is just about perfect.":
                            call EmmaFace("sad", 1) from _call_EmmaFace_1077
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -15)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                            ch_e "Oh.  Well, okay, I guess."     
                            $ Line = "fail"                      
                    "What'd you have in mind?":
                            $ E_Eyes = "side"
                            ch_e "I dunno. I was thinking maybe I could start calling you. . . {i}master{/i}?"
                            $ E_Eyes = "squint"
                            ch_e "Would you like that?  I think that'd be kinda hot."
                            menu:
                                extend ""
                                "Oh, yeah.  I'd like that.":
                                        ch_e "Cool. . ."
                                "Uhm. . .nah.  That's too much.":
                                        call EmmaFace("sad", 1) from _call_EmmaFace_1078
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -15)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                                        ch_e "Oh.  Well, okay, I guess."
                                        $ Line = "fail"

                    "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":
                            call EmmaFace("sly", 1) from _call_EmmaFace_1079
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 15)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -10)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)
                            ch_e "Aw, I guess I can't get mad about that. . ."
                            $ Line = "fail"
                            
                    "Actually, let's stop that. It's creeping me out.":
                            call EmmaFace("perplexed", 2) from _call_EmmaFace_1080
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -50)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -15)
                            ch_e "Oh.  Sorry.  I guess I got carried away with it."
                            $ E_Blush = 1
                            $ Line = "embarrassed"
                            
        "As if I care what you think, slut.":
                call EmmaFace("sad", 1) from _call_EmmaFace_1081
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -10)
                menu:
                    extend ""
                    "Sorry. I just don't care what you want.":
                            if ApprovalCheck("Emma", 1400, "LO"): 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                                    ch_e "That's so. . ." 
                                    call EmmaFace("sly", 1) from _call_EmmaFace_1082
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 15)
                                    ch_e ". . .{i}mean!{/i}" 
                            else:
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -10)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1083
                                    ch_e "!!!"
                                    $ Line = "rude"

                    "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 10)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                            ch_e "Oh, okay.  Just. . .try not to be so mean about it, Okay?" 

        "Not me.  It's kind of creepy.":
                    call EmmaFace("sad", 2) from _call_EmmaFace_1084
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, -20)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -25)
                    ch_e "Oh.  Uhm. . .never mind, then."
                    $ Line = "embarrassed"
    
    $ E_History.append("master")
    if Line == "rude":
            $ E_RecentActions.append("angry")
            hide Emma_Sprite with easeoutbottom                     
            call Remove_Girl("Emma") from _call_Remove_Girl_74
            $ renpy.pop_call()
            "Emma hurries through the door in a huff.  She might have been crying."
    elif Line == "embarrassed":    
            hide Emma_Sprite with easeoutbottom                     
            call Remove_Girl("Emma") from _call_Remove_Girl_75
            $ renpy.pop_call()
            "Emma hurries through the door, leaving you alone.  She looked really embarrassed."
    elif Line != "fail":
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 50)
            $ E_Petnames.append("master")
            $ E_Petname = "master"
            ch_e ". . .master."
    return

# end Emma_Master//////////////////////////////////////////////////////////


# start Emma_Sexfriend//////////////////////////////////////////////////////////

label Emma_Sexfriend:   #Emma_Update   
    $ E_Loc = bg_current
    call Set_The_Scene from _call_Set_The_Scene_152
    call CleartheRoom("Emma") from _call_CleartheRoom_45
    $ E_DailyActions.append("relationship")
    call Taboo_Level from _call_Taboo_Level_39
    $ Line = 0
    call EmmaFace("bemused", 1) from _call_EmmaFace_1085
    ch_e "So, [E_Petname]. . .you got a second?" #blushing expression
    menu:
            extend ""
            "Not really.":
                call EmmaFace("angry", 1) from _call_EmmaFace_1086
                ch_e "You're such a jerk, [Playername]!" #Angry expression.  Loss of points                
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)           
                $ Line = "rude"

            "This doesn't sound good.":
                call EmmaFace("perplexed", 1) from _call_EmmaFace_1087
                ch_e "I promise.  It's nothing bad." 
                    
            "Yeah.  What's up?":
                pass
                
    if not Line: #all this gets skipped if the "rude" response was procced above
            if ApprovalCheck("Emma", 850, "L"):                  
                    call EmmaFace("bemused", 1) from _call_EmmaFace_1088
                    ch_e "Well. . . I really like you.  You know that, right?" #Sexy expression.  This is Emma's "High Like" response
                    menu:
                        extend ""
                        "I was kinda hoping.":
                            call EmmaFace("sexy", 1) from _call_EmmaFace_1089
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 10) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5)    
                            ch_e "I was {i}really{/i} hoping you'd say that [E_Petname]." #Blushing expression
                
                        "Really?":
                            ch_e "Uhm. . .  yeah.  I really do." #Blushing expression

                        "Ugh.  Gross":
                            call EmmaFace("angry", 1) from _call_EmmaFace_1090
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -5)   
                            ch_e "Y'know, you're such an ass, [Playername]!" #Angry expression.  Big loss of points
                            $ Line = "rude"
                            
            elif ApprovalCheck("Emma", 1000, "LI"): 
                    call EmmaFace("sexy", 1) from _call_EmmaFace_1091
                    ch_e "I just wanted to tell you. . .I think you're kinda cute, for a student." 
                    menu:
                        extend ""
                        "That's really nice of you to say.":
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 5) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5)   
                            ch_e "Well, I really mean it." #Blushing expression

                        "Me?  You really think so?":
                            ch_e "Yeah.  I {i}really{/i} do." #Blushing expression
                
                        "Are you going somewhere with this?":
                            call EmmaFace("angry") from _call_EmmaFace_1092
                            ch_e "Well not anymore, I'm not!" #Angry expression.  Loss of points
                            $ Line = "rude"
                            
            else: #if it reaches this block, it's because it failed the "like" check above.                    
                    $ E_Mouth = "smile"
                    $ E_Brows = "sad"
                    $ E_Eyes = "side"
                    ch_e "This is gonna sound really weird."
                    menu:
                        extend ""
                        "Well, you've got me intrigued.  Now you {i}have{/i} to tell me.":
                            ch_e "Promise you won't think {i}badly{/i}of me?"  #Nervous expression
                            menu:
                                extend ""
                                "Emma. . . I really like you.  I promise.":
                                    call EmmaFace("smile") from _call_EmmaFace_1093
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 10) 
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5)    
                                    ch_e "Well. . . okay."  #Blushing expression.  Gain of points.

                                "Uhm. . . okay?":
                                    ch_e "Well. .  ." #Nervous expression

                                "No promises.":
                                    call EmmaFace("perplexed",2) from _call_EmmaFace_1094
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -5)  
                                    ch_e "Uhm. . . never mind, then."  #Embarrassed expression.  Minor loss of points
                                    $ Line = "embarrassed"

                        "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                            call EmmaFace("angry",1) from _call_EmmaFace_1095
                            ch_e "Fine.  whatever."
                            $ Line = "rude"
                                
    if not Line: #again, if the Line has been changed to "rude" or "embarrassed" then it skips past here.                          
            ch_e "Anyway. . . I was kinda thinking. . . we get along pretty well, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        call EmmaFace("perplexed",2) from _call_EmmaFace_1096
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -10)  
                        ch_e "Sorry.  I knew this was a mistake." #Embarrassed expression.  Minor loss of points
                        $ Line = "embarrassed"
                    
    if not Line:                
            ch_e "And we've known each other for a little while, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        call EmmaFace("perplexed",2) from _call_EmmaFace_1097
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -10)  
                        ch_e "Sorry.  I knew this was a mistake." 
                        $ Line = "embarrassed"
    if not Line:            
            ch_e "Well. . . I was just kinda thinking. . .  we could take our relationship a little further, if you wanted to."
            menu:
                extend ""
                "You mean. . . like, being {i}friends with benefits{/i}?":
                        ch_e "Kind of, yes.  What do you think?" #Blushing expression
                        menu:
                            extend ""
                            "Sounds amazing!  Count me in.":
                                    call EmmaFace("smile",1) from _call_EmmaFace_1098
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 10) 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 50)             
                                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                                    "Emma leans in and gives you a gentle kiss on the cheek."
                                    ch_e "I can't wait to get started, [E_Petname]."

                            "That may be the sluttiest thing I've ever heard in my life.":
                                    call EmmaFace("angry",1) from _call_EmmaFace_1099
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -30) 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -40)  
                                    ch_e "You're the biggest asshole ever, [E_Petname]!" #Angry expression.  HUGE loss of points
                                    $ Line = "rude"

                "Uhm, to be honest, I'd rather not.":
                        call EmmaFace("sadside",2) from _call_EmmaFace_1100
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 15)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -15)  
                        ch_e "Oh.  Okay."  #Sad expression
                        ch_e "I think I should go now.  I've got stuff to do."
                        $ Line = "sad"

    if Line == "rude":    
            call EmmaFace("angry",1) from _call_EmmaFace_1101
            $ E_RecentActions.append("angry")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20) 
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -10) 
            hide Emma_Sprite with easeoutleft   
            $ E_RecentActions.append("angry")
            "Emma storms off in a huff.  She seemed pretty mad at you."
    elif Line == "embarrassed":
            call EmmaFace("perplexed",1) from _call_EmmaFace_1102
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, -20)   
            hide Emma_Sprite with easeoutbottom
            "Emma runs through the door leaving you alone.  That was very strange."
    elif Line == "sad":    
            hide Emma_Sprite with easeoutbottom
            "Emma leaves through the door leaving you alone.  You think you may have hurt her feelings."
    else: #if you kept Line unused throughout, then you passed all the checks, so. . .
            $ E_Petnames.append("sex friend")             
            call EmmaFace("sly",2) from _call_EmmaFace_1103
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)             
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10)   
            "Emma leans in and passes her hand across body."
            "As she does so, she sticks her hand in your jeans, so her fingers slide along your bare skin."
            $ E_Blush = 1
            ch_e "I'll definitely be seeing {i}you{/i} later, [E_Petname]."  
            hide Emma_Sprite with easeoutright
            "She leaves through a nearby door. "            
    call Remove_Girl("Emma") from _call_Remove_Girl_76
    return
    
# end Emma_Sexfriend//////////////////////////////////////////////////////////


# start Emma_Fuckbuddy//////////////////////////////////////////////////////////

label Emma_Fuckbuddy:   #Emma_Update   
    $ E_DailyActions.append("relationship")
    "Out of nowhere, you feel a hand stroking across your cock."
    "Even though you're fully dressed, it definitely feels like soft skin touching your own."
    "You glance down and see a slender arm snaked around your waist, before vanishing into your pants."
    "As you try to control your rising erection, a voice whispers into your ear,"
    ch_e "Any time, just let me know. . ."
    "-and suddenly the pressure is gone." 
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on Emma later. . ."
    $ E_Petnames.append("fuck buddy")  
    $ E_Event[10] += 1
    return
# end Emma_Fuckbuddy//////////////////////////////////////////////////////////

# start Emma_Daddy//////////////////////////////////////////////////////////

#Not updated

label Emma_Daddy:       #Emma_Update   
    $ E_DailyActions.append("relationship")
    call Shift_Focus("Emma") from _call_Shift_Focus_171
    ch_e ". . ."
    if "dating" in E_Traits:
        ch_e "You know, even though we've been dating,"  
    else:    
        ch_e "Even though we've been hanging out," 
    if E_Love > E_Obed and E_Love > E_Inbt:
        ch_e "and you're really sweet to me. . ."
    elif E_Obed > E_Inbt:
        ch_e "and you know what I need. . ."
    else:
        ch_e "and I've really been spreading my wings. . ."        
    ch_e "So I was thinking, could I call you \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
            call EmmaFace("smile") from _call_EmmaFace_1104 
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)          
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 30) 
            ch_e "Squee!"            
        "What do you mean by that?": 
            call EmmaFace("bemused") from _call_EmmaFace_1105 
            ch_e "I just sort of get turned on by it, you know, being your baby girl. . ."
            ch_e "I'd like to call you that."
            menu:
                extend ""
                "Sounds interesting, fine by me.":     
                    call EmmaFace("smile") from _call_EmmaFace_1106 
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 15)          
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 20)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 25) 
                    ch_e "Great! . . daddy."  
                "Could you not, please?":             
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 40)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)  
                    call EmmaFace("sad") from _call_EmmaFace_1107 
                    ch_e "   . . .   "
                    ch_e "Well, ok."
                "No, that creeps me out.":    
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)          
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 45)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 5)  
                    call EmmaFace("angry") from _call_EmmaFace_1108 
                    ch_e "Hrmph." 
        "No, that creeps me out.":
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 40)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 10) 
            call EmmaFace("angry") from _call_EmmaFace_1109 
            ch_e "Hrmph."  
    $ E_Petnames.append("daddy")
    return

# end Emma_Daddy//////////////////////////////////////////////////////////

# Start EmmaBreakup //////////////////////////////////////////////////////////  
 #Emma_Update   
label Emma_Cheated(Other = "Rogue", Resolution = 0, B = 0):  #Other is the other girl, Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
    #Scene for if Emma catches you with Rogue and confronts you about it. 
    $ E_DailyActions.append("relationship")
    $ Line = 0
    call EmmaFace("angry") from _call_EmmaFace_1110
    
    if Other == "Rogue":
        if E_LikeRogue >= 900:
            $ Resolution += 2
        elif E_LikeRogue >= 800:
            $ Resolution += 1
        $ B = int((E_LikeRogue - 500)/2)
    
    $ Resolution -= E_Cheated if E_Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating
    
    if E_Cheated:
        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -50) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, -25)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -50)   
    else:
        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -120) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, -30)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -20)  
        
    "Emma stomps up to you and stares you down for a moment."
    ch_e "Well?!" 
    ch_e "Wanna tell me what that was all about?"
    menu:
        extend ""
        "Uhm. . .sorry?":
                ch_e "Is that {i}really{/i} all you have to say for yourself?"
                ch_p "I don't know? It would kinda help if I knew what you were upset about."
                if ApprovalCheck("Emma", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Line = "angry"
        "I have no idea what you're talking about.":
                ch_e "I can't believe you just said that. I gave you a lot more credit than that."
                ch_p "[E_Pet], I'm being serious. Why're you so upset?"
                if ApprovalCheck("Emma", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Resolution -= 2
                    $ Line = "angry"
        "Could you chill out and tell me what you mean?":
                call EmmaFace("sad",2) from _call_EmmaFace_1111                
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 5, 1) 
                ch_e "I didn't like what happened already. How much worse can it get?"
                ch_p "You'd better start making some sense, or you're gonna find out."
                if ApprovalCheck("Emma", 500, "O"):
                    $ Resolution += 1  
                elif ApprovalCheck("Emma", 1200, "LO"):
                    $ Resolution -= 1    
                else:
                    $ Resolution -= 3
                    $ Line = "angry"
                    
    if not Line:
            #this section only triggers if you didn't trigger the "angry" response in the previous section
            call EmmaFace("angry",2) from _call_EmmaFace_1112
            if Other == "Rogue":
                ch_e "I {i}saw{/i} you and Rogue! I can't believe you'd do that, [E_Petname]."
            else:
                ch_e "I {i}saw{/i} you with her! I can't believe you'd do that, [E_Petname]."
            ch_e "I thought we had something. . .  {i}special{/i} going on."
            menu:
                extend ""
                "I'm sorry. . . ":
                        $ Resolution += 1                        
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5) 
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)  
                        if not ApprovalCheck("Emma", 900, "L"):
                                #if love is less than 900
                                $ Line = "sad"
                        else:
                                call EmmaFace("sad") from _call_EmmaFace_1113
                                ch_e "Me too. I thought you. . . "
                                call EmmaFace("sadside") from _call_EmmaFace_1114
                                ch_e ". . . I thought you maybe loved me."
                                menu:
                                    extend ""
                                    "You weren't wrong, [E_Pet].":
                                            $ Resolution += 1                                            
                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 5) 
                                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)   
                                            call EmmaFace("embarrassed") from _call_EmmaFace_1115
                                            ch_e " . . . really?"
                                            menu:
                                                extend ""
                                                " really.":
                                                        call EmmaFace("embarrassed") from _call_EmmaFace_1116
                                                        if Other == "Rogue":
                                                            ch_e "Then. . . why did you do that with {i}Rogue?{/i} You had to know that would hurt me."
                                                        else:
                                                            ch_e "Then. . . why did you do that with {i}her?{/i} You had to know that would hurt me."                                                        
                                                        menu:
                                                            extend ""
                                                            "It was a mistake. And I promise I'll never do it again.":
                                                                    $ Resolution += 2                                                                    
                                                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 5)
                                                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)   
                                                                    call EmmaFace("happy",2) from _call_EmmaFace_1117
                                                                    ch_e "Okay. I understand. Just. . . remember how much I care about you, 'kay?"
                                                                    ch_e "I can forgive you this time."
                                                                    ch_e "Because I'm in love with you, too."
                                                                    call E_Kissing_Launch("kissing") from _call_E_Kissing_Launch_1
                                                                    call E_Pos_Reset from _call_E_Pos_Reset_15
                                                            "I was trying to maybe include her in what we have going.":
                                                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                                                    $ Line = "maybe"
                                                            "I don't know, seemed fun at the time.":
                                                                    $ Resolution -= 1
                                                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                                                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, -5)
                                                                    $ Line = "angry"          
                                                "Had you going, there, didn't I? {i}Hell{/i}, no, I don't!":
                                                        $ Resolution -= 3
                                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20) 
                                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)   
                                                        $ Line = "angry"                                                                   
                                    "Yeah, well. .  . I don't.":
                                            $ Resolution -= 1
                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)   
                                            $ Line = "sad"  
                        #end "sorry."
                "Whatever.":
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)   
                        if ApprovalCheck("Emma", 900, "L") and not ApprovalCheck("Emma", 500, "O"):
                                $ Resolution -= 2
                                $ Line = "angry"
                        else:
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10) 
                                $ Resolution -= 1
                                $ Line = "sad"
                "We do. And now, it can be even {b}more{/b} special.":
                                $ Resolution += 1
                                $ Line = "maybe"
            #end "questioning", for long blocks like this, it helps to put a comment at the end to explain what was going on, so I don't get lost. ;)
            
    if Line == "maybe":
            # Maybe threesome?            
            if ApprovalCheck("Emma", 1250):
                    call EmmaFace("confused") from _call_EmmaFace_1118
                    ch_e "What're you even {i}talking{/i} about?"
                    if Other == "Rogue":
                        ch_p "Look. . .be totally honest with me for a second. Rogue's your best friend, right?"
                    else:
                        ch_p "Look. . .be totally honest with me for a second. She's kinda hot, right?"
                    ch_e "Yeah. . ."
                    ch_p "Right. And when you saw us together. . . you have to admit, you thought it was pretty hot on some level, right?"
                    call EmmaFace("angry") from _call_EmmaFace_1119
                    ch_e "No. It pissed me off is what it did."
                    ch_p "C'mon, [E_Pet]. Haven't you ever thought about it?"
                    call EmmaFace("confused") from _call_EmmaFace_1120
                    ch_e "Thought about what?"
                    if Other == "Rogue":
                        ch_p "Thought about what it might be like if we invited Rogue into what we have together."
                    else:
                        ch_p "Thought about what it might be like if we invited her into what we have together."                    
                    if ApprovalCheck("Emma", 1500) and Resolution >= 3:
                            call EmmaFace("embarrassed") from _call_EmmaFace_1121
                            ch_e "You mean . . .a {i}threesome{/i}?"
                            call EmmaFace("sly") from _call_EmmaFace_1122
                            ch_e "I can't believe I'm saying this but. . . I'm vaguely intrigued."
                            if Other == "Rogue":
                                ch_e "Assuming I'm interested. . . how're you going to convince Rogue?"
                            else:
                                ch_e "Assuming I'm interested. . . how're you going to convince her?"
                            ch_p "If you see us together again, just play it cool."
                            ch_p "Make sure she notices that you're watching us, but don't give her the impression it puts you off."
                            call EmmaFace("sly",1) from _call_EmmaFace_1123
                            ch_e ". . . which should make her wonder what's up."
                            ch_p "Right. Eventually, she'll ask me what our arrangement is."
                            ch_e "By then, with any luck, she'll be comfortable enough with me that I can ask her how she feels about it."
                            call EmmaFace("sly",2) from _call_EmmaFace_1124
                            ch_e "Gotta admit, [E_Petname]. . . you're pretty smooth."
                            ch_e "Consider me on board with that plan."
                            ch_e "Just be sure to be careful with her. She's still my friend."
                            #have Emma kiss the Player here.
                            ch_e "And remember, you're still {i}my{/i} guy."                            
                            $ E_Traits.append("poly rogue")
                            $ E_Traits.append("ask rogue")
                            $ Line = 0
            if Line:
                    #this section will only trigger if the "maybe" line above triggered BUT both of the stat checks above failed. 
                    #If you don't even ask about a threesome then this check gets skipped, and if you ask, but succeed both checks,
                    #then this section gets skipped. 
                    call EmmaFace("angry") from _call_EmmaFace_1125
                    if Other == "Rogue":
                        ch_e "So, you're telling me you being with Rogue like that was your way of seeing if I'd be up for a threesome?"
                    else:
                        ch_e "So, you're telling me you being with her like that was your way of seeing if I'd be up for a threesome?"
                    ch_p "Pretty much. I. . .take it you're not down with that?"
                    $ Line = "angry"
            # End "maybe threesome?"
    
    elif Resolution >= 4:
        if Other == "Rogue" and E_LikeRogue >= 800:
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 25)   
                ch_e "Well, maybe Rogue and I can work something out. . ."                            
                $ E_Traits.append("poly rogue")
                $ E_Traits.append("ask rogue")                
        
    $ E_Cheated += 1
    if "saw with rogue" in E_Traits: 
            #Clean up the trait for this event
            $ E_Traits.remove("saw with rogue")
            if "poly rogue" not in E_Traits:
                $ E_LikeRogue -= 50
            
    if not Line:
            #a neutral ending if you wrap things up without really effecting much
            pass                
    elif Line == "angry":
            #Angry ending
            call EmmaFace("angry",2) from _call_EmmaFace_1126
            ch_e "You are {b}SUCH{/b} an asshole, [E_Petname]!"
            ch_e "I never wanna see you again, as long as I live!"
            "Emma disappears through the doorway leaving you standing alone."
            "Whatever you once had is over now, for sure."     
            $ E_RecentActions.append("angry")
            $ E_Break[0] = 7 + E_Break[1] + E_Cheated
            $ E_Traits.remove("dating")
            $ E_Traits.append("ex")         
    elif Line == "sad":
            # Sad ending
            call EmmaFace("sad",2) from _call_EmmaFace_1127
            "Emma leaves through the door leaving you standing alone."
            "You're pretty sure she was crying as she left."
            "You're also pretty sure you seriously damaged your relationship with her."
            if Resolution <= 3:
                $ E_Break[0] = 5 + E_Break[1] + E_Cheated
                $ E_Traits.remove("dating")
                $ E_Traits.append("ex")                
    return

# end EmmaBreakup //////////////////////////////////////////////////////////    
