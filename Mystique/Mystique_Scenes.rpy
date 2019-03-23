# start MystiqueMeet //////////////////////////////////////////////////////////
# Check  #Mystique_Update   to see what needs fixing still
label MystiqueMeet:    
    $ bg_current = "bg classroom"   
    $ newgirl["Mystique"].Outfit = "teacher"
    call CleartheRoom("Mystique",0,1)
    $ newgirl["Mystique"].Loc = "bg Mystique"  
    $ newgirl["Mystique"].Love = 0        
    $ newgirl["Mystique"].Obed = 0            
    $ newgirl["Mystique"].Inbt = 0 
    call Shift_Focus("Mystique")    
    call Set_The_Scene
    $ Mystique_SpriteLoc = StageRight
    #call LastNamer   
    $ newgirl["Mystique"].GirlName = "Ms. Darkholme"
    #$ newgirl["Mystique"].Petnames.append(_return)
    #$ newgirl["Mystique"].Petname = _return
        
    "You enter the classroom and take a seat." 
    "The bell rings to class, but Professor McCoy seems to be late."
    "A woman enters the room and heads to the podium with a smile."
    call NewGirl_Face("Mystique","normal")
    show Mystique_Sprite at SpriteLoc(Mystique_SpriteLoc) with easeinright     
    $ newgirl["Mystique"].Loc = "bg classroom" 
    $ newgirl["Mystique"].Girl_Arms = 1
    ch_u "Good morning, students. My name is Raven Darkholme, and I will be filling in for Professor McCoy in his absence."
    #ch_m "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect." 
    "Her eyes scans the room, passing over each student."    
    call NewGirl_Face("Mystique","surprised")
    pause 1
    call NewGirl_Face("Mystique","sly")
    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)     
    $ newgirl["Mystique"].Lust += 5
    "As her eyes pass over you, they briefly widen and then narrow."
    #call NewGirl_Face("Mystique","sly")
    ch_m "Very well, let's begin."
    call NewGirl_Face("Mystique","normal") 
    "The class is pretty basic today, mostly a lecture on her areas of expertise, history."
    $ newgirl["Mystique"].Lust += 5
    "She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."
    $ newgirl["Mystique"].Lust += 5
    call Wait 
    call CleartheRoom("Mystique",0,1)
    $ newgirl["Mystique"].Loc = "bg classroom" 
    call Set_The_Scene
    ch_m "All right students, you may leave."
    ch_m "[newgirl[Mystique].Petname], could you stay a moment, I have something to ask of you before your next class starts."    
    menu:
        extend ""
        "Yes?":
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10) 
                call NewGirl_Face("Mystique","normal")  
        "I've got places to be.":
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -15) 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                call NewGirl_Face("Mystique","angry") 
                ch_m "MR. [Playername], do not take that attitude with me."
                "She places herself in the doorway, preventing you from leaving."
        "For such a hot teacher? Sure i've got some time.":
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                call NewGirl_Face("Mystique","angry",1, Mouth="smirk") 
                ch_m "That's rather. . . inappropriate."
                call NewGirl_Face("Mystique","bemused", Mouth="smile") 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 20) 
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 25, 15)  
                ch_m "But also true, so I can't criticize you too harshly."
    
    ch_m "Professor Xavier and others told me about you." 
    
    if P_Rep <= 200:
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 15) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
        call MystiqueFace("angry", Brows="confused") 
        ch_m "You seem to be a bit of a scoundrel. . ."        
    elif P_Rep < 600:
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 5) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
        call MystiqueFace("sly") 
        ch_m "You have quite a reputation around campus. . ."
    else:
        call MystiqueFace("smile") 
        ch_m "You have managed a reasonble reputation. . ."
        
    if R_SEXP >= 60 and K_SEXP >= 60:
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
        call MystiqueFace("sly") 
        ch_m "and a number of conquests to your name. . ."
    elif R_SEXP >= 60 or K_SEXP >= 60:
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 2) 
        call MystiqueFace("smile") 
        ch_m "and are not without some romantic entanglements. . ."
    else:
        call MystiqueFace("smile", Brows="confused") 
        ch_m "though I haven't heard of much of a romantic life. . ."
        
    if P_Lvl >= 7:
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
        call MystiqueFace("smile") 
        ch_m "but your grades are excellent."
    elif P_Lvl >= 3:
        call MystiqueFace("normal", Brows="confused") 
        ch_m "but your grades are marginal at best."
    else:
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 10, -5, 1)  
        call MystiqueFace("normal", Brows="sad") 
        ch_m "but you haven't been living up to your potential in class."
    
    call MystiqueFace("normal", Eyes="side") 
    ch_m "My particular interest in your case, however. . ."
    call MystiqueFace("sly") 
    ch_m "is how dangerous you can be."
    call MystiqueFace("sly", Mouth="normal") 
    ch_m "Even Xavier, the most powerful telepath there is, becomes a mere human in front of you. . ."
    call MystiqueFace("sly") 
    ch_m "quite. . . impressive"
    # menu:
    #     extend ""
    #     "I imagine it would.":
    #             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
    #             $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
    #             call MystiqueFace("normal") 
    #             ch_m "Hmm, yes."
    #     "Huh.":
    #             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -1) 
    #             $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -1)
    #             call MystiqueFace("confused", Mouth="normal") 
    #             ch_m ". . . yes."
    #             call MystiqueFace("normal") 
    #     "So you can't see what I'm picturing right now?":
    #             $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
    #             call MystiqueFace("bemused") 
    #             pause 0.5
    #             call MystiqueFace("bemused", Eyes="down") 
    #             "She glances downward."
    #             call MystiqueFace("sly") 
    #             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10) 
    #             $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10) 
    #             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 15) 
    #             ch_m "I can't read your mind, but I'm not blind, [newgirl[Mystique].Petname]."
    ch_m "Anyway, I think we should set aside some time to talk."
    ch_m "I'd like to make you a personal project, so I can see how and if your powers can develop."
    menu:
        extend ""
        "I'd be ok with that.": 
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
                call MystiqueFace("smile") 
                ch_m "Excellent, I look forward to it."
        "I don't know if i would like to be part of some strange experiments!":
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
                call MystiqueFace("normal", Mouth="sad") 
                ch_m "There's nothing for you to fear."
                call MystiqueFace("sly") 
                ch_m "I'll be. . . gentle."
        "If it means to be near you more often. . .":
                if ApprovalCheck("Mystique", 295, "L"):
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
                    call MystiqueFace("sly") 
                    ch_m "Oh, I believe we'll be spending a lot of time together. . ."
                else:
                    call MystiqueFace("angry") 
                    ch_m "Much as it may pain me, it would. . ."
                    call MystiqueFace("normal") 
        "What's in there for me?":
                if not ApprovalCheck("Mystique", 290, "L"):
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
                    call MystiqueFace("angry") 
                    ch_m "You'll stand some chance of passing this class, [newgirl[Mystique].Petname]."
                    call MystiqueFace("normal") 
                    ch_m "And you might get even more powerful."
                else:
                    if newgirl["Mystique"].Obed > 0:
                        call MystiqueFace("confused", Mouth="smirk") 
                        ch_m "What would you {i}like{/i} to \"get out of it?\""
                        menu:
                            extend ""
                            "I guess if it helps your \"research.\" . .":
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10) 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -5)
                                    call MystiqueFace("smile") 
                                    ch_m "I'm glad to see that you can be reasonable."
                            "Spending more time with you would be plenty. . .":
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 20, 5) 
                                    call MystiqueFace("sly") 
                                    ch_m "It certainly should be."
                            "A kiss?":
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                                    call MystiqueFace("surprised",1, Mouth="surprised") 
                                    ch_m "[newgirl[Mystique].Petname], that is incredibly inappropriate!"
                                    call MystiqueFace("sadside",0,Brows="angry") 
                                    ch_m "I would {i}never{/i} consider such a thing with a student."
                                    if ApprovalCheck("Mystique", 220, "I"):
                                        call MystiqueFace("sly",1) 
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
                                        ch_m ". . .never. . ."
                            "I think you know what I'd want. . .":
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
                                    call MystiqueFace("sly",Brows="angry") 
                                    ch_m "Yes, I imagine that I do. . ."
                                    if ApprovalCheck("Mystique", 220, "I"):
                                        call MystiqueFace("sly",1) 
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) 
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10) 
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
                                        ch_m "And we may be able to come to some sort of \"mutually beneficial\" arrangement."
                                    else:
                                        call MystiqueFace("bemused",0) 
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5) 
                                        ch_m "But figuring out whether I'm correct is the entire point here."
                    else: #if 0 Obedience
                        call MystiqueFace("normal") 
                        ch_m "The satisfaction of helping my. . . studies."
                        if ApprovalCheck("Mystique", 300, "L"):
                            call MystiqueFace("sly") 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 5) 
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5) 
                            ch_m "-and maybe if you're good. . ."
                        else:
                            ch_m "-and nothing more."
     
    call MystiqueFace("normal",0) 
    ch_m "That said, class is finished for the day and I have some things to attend to, so I'll see you. . ."   
    ch_m ". . . later. . ."
    hide Mystique_Sprite with easeoutright 
    "She walkes out of the room and down the hall."
    $ newgirl["Mystique"].Loc = "bg Mystique"         
    $ newgirl["Mystique"].History.append("met")          
    $ Round -= 10      
    return
            
#end MystiqueMeet //////////////////////////////////////////////////////////  

# start MystiqueMeetGym //////////////////////////////////////////////////////////
# Check  #Mystique_Update   to see what needs fixing still
label MystiqueMeetGym:    
    $ bg_current = "bg dangerroom"   
    call CleartheRoom("Mystique",0,1)
    $ newgirl["Mystique"].Loc = "bg Mystique"  
    $ newgirl["Mystique"].Gym = [2,0,"workout pants","workout jacket",0,"workout top","black panties",0,0,0,0]
    #$ newgirl["Mystique"].Gym = [2,0,0,"workout jacket",0,"workout top","black panties","workout pants",0,0,0]  
    $ newgirl["Mystique"].Over = "workout jacket"
    $ newgirl["Mystique"].Chest = "workout top"
    $ newgirl["Mystique"].Legs = "workout pants"
    $ newgirl["Mystique"].Panties = "black panties"
    $ newgirl["Mystique"].Neck = 0      
    $ newgirl["Mystique"].Glasses = 0      
    $ newgirl["Mystique"].Outfit = "gym"
    #$ newgirl["Mystique"].Love = 300        
    #$ newgirl["Mystique"].Obed = 0            
    #$ newgirl["Mystique"].Inbt = 200 
    call Shift_Focus("Mystique")    
    call Set_The_Scene
    $ MSpriteLoc = StageCenter
    #call LastNamer                         
    #$ newgirl["Mystique"].Petnames.append(_return)
    #$ newgirl["Mystique"].Petname = _return

    "You enter the danger room." 
    show Mystique_Sprite at SpriteLoc(MSpriteLoc)
    #"The bell to class rings, but Professor McCoy seems to be late."
label MystiqueMeetGym_Waited:
    "You see Raven working out."
    call MystiqueFace("normal")
    #$ newgirl["Mystique"].Loc = "bg classroom" 
    $ newgirl["Mystique"].Girl_Arms = 1
    "At some point she notices you're kind of close to her"
    call MystiqueFace("surprised")
    "She ends up losing focus on the training and gets knocked down on the floor."
    "You run towards her. As soon as you touch her to help her stand, something happens to her body"
    #turns back into mystique
    $ newgirl["Mystique"].LooksLike = "Mystique"
    call NewGirl_RemoveClothes("Mystique")
    call Mystique_First_Topless(1)
    call Mystique_First_Bottomless(1)
    ch_p "Wha... what's going on?"
    ch_m "You've never seen a naked woman, [newgirl[Mystique].Petname]?"
    ch_p "You're Mystique!!!"
    call MystiqueFace("angry")
    ch_m "Shut up! Do you want everyone in this mansion to hear it?"
    ch_p "I have to tell the teachers and professor Xavier"
    "You try to make a run for it but she quickly jumps between you and the door."
    ch_m "I'd rather you didn't. How about we make a deal, there must be something you want."
    "You look down at her body with a smile"
    ch_p "Yeah, I guess we can make a deal."
    ch_m "Or I could just kill you..."
    $ newgirl["Mystique"].Over = "workout jacket"
    $ newgirl["Mystique"].Chest = "workout top"
    $ newgirl["Mystique"].Legs = "workout pants"
    $ newgirl["Mystique"].Panties = "black panties"
    ch_p "Wait wait, if you do that everyone'll be with their guards up, that wouldn't be good for you, right?"
    call NewGirl_Face("Mystique", "confused") 
    ch_m "You may be right..."
    $ newgirl["Mystique"].Eyes = "closed"
    ch_m "Fine"
    call NewGirl_Face("Mystique", "sly") 
    ch_m "Meet me at my room."
    $ newgirl["Mystique"].LooksLike = "Raven"
    #call Wait 
    
    #call CleartheRoom("Mystique",0,1)
    #$ newgirl["Mystique"].Loc = "bg dangerroom" 
    #call Set_The_Scene

    #ch_m "In any case, I think we should set aside some time to talk."
    #ch_m "I'd like to make you a personal project, so I can see how you tick."

     
    #call MystiqueFace("normal",0) 
    #ch_m "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."   
    ch_m ". . . later. . ."
    hide Mystique_Sprite with easeoutright 
    "She walks out of the room and down the hall."
    $ newgirl["Mystique"].Loc = "bg Mystique"         
    $ newgirl["Mystique"].History.append("metgym")          
    #$ Round -= 10      
    #$ newgirl["Mystique"].OutfitDay = "teacher"

    return
            
#end MystiqueMeetGym //////////////////////////////////////////////////////////            
           

# Event Mystique_Teacher_Caught /////////////////////////////////////////////////////         
# label Mystique_Teacher_Caught(Girl = "That girl"):
#     #add this scene for when Mystique is a teacher, and catches one of the girls fucking around in class.
#     ch_m "[Playername]? [Girl]? Could you stop what you're doing immediately?" 
#     call Checkout(1)
#     if Girl == "Rogue":
#             call RogueFace("bemused", 2, Eyes="side")            
#             call AllReset("Rogue")
#             $ renpy.pop_call()        
#             $ renpy.pop_call()
#             if ApprovalCheck("Rogue", 700, "I"): 
#                     call RogueFace("bemused", 1)  
#                     "Rogue shrugs and returns to her seat."
#                     $ R_LikeNewGirl["Mystique"] += 2
#             else: 
#                     "Rogue jumps and dashes out of the room."
#                     $ R_LikeNewGirl["Mystique"] -= 2
#                     $ R_Loc = "bg rogue"
#                     hide Rogue
#                     if "Rogue" in Party:
#                         $ Party.remove("Rogue")
#             $ R_Rep -= 1
#             $ newgirl["Mystique"].LikeRogue += 2
#     elif Girl == "Kitty":
#             call KittyFace("bemused", 2, Eyes="side")  
#             call AllReset("Kitty")
#             $ renpy.pop_call()        
#             $ renpy.pop_call()
#             if ApprovalCheck("Kitty", 700, "I"): 
#                     call KittyFace("bemused", 1) 
#                     "Kitty shrugs and returns to her seat."
#                     $ K_LikeNewGirl["Mystique"] += 2
#             else: 
#                     "Kitty jumps and dashes out of the room."
#                     $ K_LikeNewGirl["Mystique"] -= 2
#                     $ K_Loc = "bg kitty"
#                     hide Kitty_Sprite
#                     if "Kitty" in Party:
#                         $ Party.remove("Kitty")
#             $ K_Rep -= 1
#             $ newgirl["Mystique"].LikeKitty += 2
#     $ P_Rep -= 1             
#     ch_m "Thank you."
#     ch_m "And [Playername], see me after class for detention. . ."
#     $ P_Traits.append("detention")
#     jump Class_Room
    
# end Mystique_Teacher_Caught //////////////////////////////////////////////////////////            
           
# Event Mystique Sleepover /////////////////////////////////////////////////////  
label Mystique_Sleepover(sleepover = 0):  #Mystique_Update   
            #This event gets called from the Location menus when time passes in the Night timeframe.
            call Shift_Focus("Mystique")
            if R_Loc == bg_current and newgirl["Mystique"].LikeRogue < 800:                
                    call CleartheRoom("Mystique",1)
            if K_Loc == bg_current and newgirl["Mystique"].LikeKitty < 800:              
                    call CleartheRoom("Mystique",1)
                    
            if bg_current == "bg Mystique":
                    if Weekday < 4 or Weekday > 5:
                            #ch_m "I'm afraid I have class tommorrow. . ."
                            ch_m "I need to get some sleep. . ."
                    else:
                            ch_m "I need to get some sleep. . ."
            else:
                    ch_m "It's getting late, I should retire for the evening. . ."  
            if Day <= 14:        
                ch_m "It's been a pleasant evening, but it wouldn't be appropriate to stay after hours like this. . ."  
                #jump Return_Player    
                
            call MystiqueFace("sexy", 1)
            if (newgirl["Mystique"].Sleep >= 3 and ApprovalCheck("Mystique", 800)) or ApprovalCheck("Mystique", 1100, "LI"):                                 
                    #You've slept over several times and she still likes you
                    if bg_current == "bg Mystique":
                            ch_m "Are you spending the night?"
                    else:
                            ch_m "Would you like me to stay?"
                    $ sleepover = 1                    
            elif newgirl["Mystique"].Sleep < 3 or not ApprovalCheck("Mystique", 600):                            
                    #She doesn't especially want you there.  
                    if bg_current == "bg Mystique":
                        ch_m "I think you should probably get going." 
                    else:
                        ch_m "I should head back to my room."                    
            else: #If she's uninterested
                    if bg_current == "bg Mystique":
                        ch_m "You should leave, [newgirl[Mystique].Petname]." 
                    else:
                        ch_m "I hope to see you in class [newgirl[Mystique].Petname]."
            if sleepover:            
                if R_Loc == bg_current:
                    ch_m "And of course you as well, Rogue."   
                if K_Loc == bg_current:
                    ch_m "And of course you as well, Kitty."
                                          
            menu:
                extend ""
                "Sure." if sleepover:
                        if newgirl["Mystique"].Sleep <= 5:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5) if newgirl["Mystique"].Love >= 500 else newgirl["Mystique"].Love
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 25)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 25, 25) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                        ch_m "Great! I'll get changed."
                    
                "No, sorry." if sleepover:                  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 6)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 4)
                        $ newgirl["Mystique"].Brows = "sad"
                        ch_m "Alright. . . see you tomorrow. . ."
                        $ sleepover = 0
                        
                "Ok, I'll head out. Good night." if not sleepover and bg_current == "bg Mystique":                        
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 25, 2)            
                        call MystiqueFace("smile")
                        ch_m "Ok, good night. . ."
                "Ok, see you later then. Good night." if not sleepover and bg_current != "bg Mystique":                        
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 25, 2)            
                        call MystiqueFace("smile")
                        ch_m "Yeah, night, [newgirl[Mystique].Petname] . ."
                    
                "Are you sure I can't stay the night? . ." if not sleepover and not newgirl["Mystique"].Sleep and bg_current == "bg Mystique": 
                        if ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 700, "L") or ApprovalCheck("Mystique", 500, "O"):
                            call MystiqueFace("bemused", 1)                   
                            ch_m "Well, Maybe. . ."
                            $ sleepover = 1 
                        else:                    
                            call MystiqueFace("smile")
                            $ newgirl["Mystique"].Brows = "confused"
                            ch_m "No, not tonight, [newgirl[Mystique].Petname] Sorry."
                "Are you sure you can't stay? . ." if not sleepover and not newgirl["Mystique"].Sleep and bg_current != "bg Mystique": 
                        if ApprovalCheck("Mystique", 1000) or ApprovalCheck("Mystique", 700, "L") or ApprovalCheck("Mystique", 500, "O"):
                            call MystiqueFace("bemused", 1)                   
                            ch_m "Well, Maybe. . ."
                            $ sleepover = 1 
                        else:                    
                            call MystiqueFace("smile")
                            $ newgirl["Mystique"].Brows = "confused"
                            ch_m "No, not tonight, [newgirl[Mystique].Petname] Sorry." 
                            
                "That was not a problem for you the other night . ." if not sleepover and newgirl["Mystique"].Sleep: #if she wants you gone  
                        if ApprovalCheck("Mystique", 900)or ApprovalCheck("Mystique", 700, "L") or ApprovalCheck("Mystique", 500, "O"):
                            call MystiqueFace("bemused", 1)                  
                            ch_m "and that was pretty nice. . ."
                            $ sleepover = 1
                        else:                    
                            call MystiqueFace("smile")
                            $ newgirl["Mystique"].Brows = "confused"
                            if bg_current == "bg Mystique":
                                ch_m "Um, no, sorry." 
                            else:                        
                                ch_m "Um, no, sorry. I'll see you." 
                    
            if sleepover: #If she agreed
                    if R_Loc == bg_current:
                        if R_LikeNewGirl["Mystique"] >= 800:                                
                                ch_r "I'll get ready for bed then."   
                        else:        
                                ch_r "I'm actually going to head out. . ."           
                                call CleartheRoom("Mystique",1) 
                    if K_Loc == bg_current:
                        if K_LikeNewGirl["Mystique"] >= 800:                                
                                ch_k "I'll get cleaned up."   
                        else:        
                                ch_k "I'll[K_like]take a raincheck on that. . ."           
                                call CleartheRoom("Mystique",1) 
                    if newgirl["Mystique"].SEXP < 10 and not ApprovalCheck("Mystique", 600, "I") and not ApprovalCheck("Mystique", 600, "O"):
                            ch_m "Just don't do anything funny. . ."        
                    jump Mystique_Morning
            jump Return_Player    
    
label Mystique_Morning:
            #This label is jumped too from Mystique Sleepover if you successfully stay the night
            call Shift_Focus("Mystique")
            call MystiqueOutfit("sleep")
            "Mystique changes into her sleepwear."
            ch_m "Ah, that's better."
            ch_m "Night, [newgirl[Mystique].Petname]"                                               #fix add sex option here
            show blackscreen onlayer black    
            pause 2
            call Wait(Lights = 0) 
            $ newgirl["Mystique"].Loc = bg_current
            call MystiqueOutfit("sleep")
            
            $ D20 = renpy.random.randint(40, 70)                                #This element sends player to the Morningwood event        
            if "hungry" in newgirl["Mystique"].Traits and D20 > 50:
                    $ Cnt = 1
            elif D20 >= newgirl["Mystique"].Lust:
                    $ Cnt = 0     
            elif newgirl["Mystique"].SEXP <= 15:
                    $ Cnt = 0         
            elif newgirl["Mystique"].Blow >= 5 or ApprovalCheck("Mystique", 900, "I"):
                    $ Cnt = 1
            elif newgirl["Mystique"].Blow and ApprovalCheck("Mystique", 900):
                    $ Cnt = 1
            elif ApprovalCheck("Mystique", 1400): # Trinity < 1400
                    $ Cnt = 1
            else:
                    $ Cnt = 0 
                 
            if Cnt:   
                    call Mystique_SexAct("morningwood") #mystique wip
                    ch_m "Hmmm. . ."
                                    
            call MystiqueFace("smile")
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            ch_m "Good morning . . ."
            menu:
                extend ""
                "It's always nice sleeping with you." if newgirl["Mystique"].Sleep: 
                        if newgirl["Mystique"].Sleep < 5:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 8)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 8)    
                        $ newgirl["Mystique"].Blush = 1
                        ch_m "And that's always nice to hear."
                        ch_m "We'll have to keep this up."
                "I loved sleeping next to you." if not newgirl["Mystique"].Sleep:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)            
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 12)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 12)  
                        $ newgirl["Mystique"].Blush = 2
                        ch_m "Yeah, I. .  I had fun too."
                        $ newgirl["Mystique"].Blush = 1
                        ch_m "I wouldn't mind doing it again."   
                        $ newgirl["Mystique"].Blush = 2
                        ch_m "You know, some other time. . . "
                        $ newgirl["Mystique"].Blush = 1
                "It was fun.":
                        if not newgirl["Mystique"].Sleep:                    
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)            
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 8)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 15)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15) 
                        elif newgirl["Mystique"].Sleep < 5:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 8)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 35, 8)             
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 8)
                        if newgirl["Mystique"].Love >= 800:
                            call MystiqueFace("bemused")
                        else:
                            call MystiqueFace("confused")
                        ch_m "Yeah, I mean I guess it was. . ."
                "You were constantly tossing around.":            
                        $ newgirl["Mystique"].Blush = 1
                        if ApprovalCheck("Mystique", 800, "L"):
                            call MystiqueFace("bemused")
                        else:
                            call MystiqueFace("angry")
                        if newgirl["Mystique"].Sleep < 5:
                            ch_m "!"
                            ch_m "I don't make a habit out of it. . ."                       
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -8)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 22)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 22)  
                        else:
                            ch_m "Yeah, well. . . you should be used to that!"
                "You need to learn to stick to your side.":  
                        if newgirl["Mystique"].Sleep < 5:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -8) 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 40)  
                        if ApprovalCheck("Mystique", 500, "O"):
                            call MystiqueFace("normal")
                            ch_m "Fine, whatever."
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 8) if newgirl["Mystique"].Sleep < 5 else newgirl["Mystique"].Obed
                        else:
                            call MystiqueFace("angry")
                            ch_m "That's not how you get me to come back." 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 35, 20) if newgirl["Mystique"].Sleep < 5 else newgirl["Mystique"].Inbt  
                        
            #fix add sex option here
            $ newgirl["Mystique"].Blush = 0
            $ newgirl["Mystique"].Sleep += 1    
            call Mystique_Schedule
            call RogueFace("normal")
            if newgirl["Mystique"].Outfit != "sleep":
                "Mystique changes out of her sleepwear."
            call MystiqueOutfit(Changed=1)
            call Girls_Location
            return
    
# end Event Sleepover /////////////////////////////////////////////////////
# start Event Morning Wood /////////////////////////////////////////////////////

label Mystique_MorningWood: #Mystique_Update   
            # this label is called from the Mystique_SexAct("morningwood"), 
            # which was called from Mystique_Sleepover, which was called from a Location.
            call Shift_Focus("Mystique")
            $ P_Focus = 30
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 5)
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5) 
            $ newgirl["Mystique"].RecentActions.append("blanket")           
            call Mystique_BJ_Launch
            "You feel a pleasant sensation. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 5)
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
            "It's somewhere below your waist. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 10)
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
            $ Trigger = "blow"
            $ newgirl["Mystique"].Eyes = "down"
            "You open your eyes. . ."
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            $ Speed = 3
            $ Count = 3
            $ Line = 0
            call Mystique_First_Peen(1)
            while Count > 0:
                    #Looping portion
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 10)
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                    menu:
                        extend ""
                        "Stay Quiet":
                            if Count >2:
                                "You just let her do her thing and pretend to still be asleep."
                            elif Count:
                                "It does feel real good. . ."
                            elif not Count:
                                "You wouldn't want her to stop. . ."
                            ch_m "\"Slurp, slurp, slurp.\""
                        "Um, [newgirl[Mystique].Pet]? What're you doing?":
                            $ Line = "question"
                            $ Count = 1
                        "That feels soo great, keep going. . .":
                            $ Line = "praise"
                            $ Count = 1
                        "Hey, quit that!":
                            $ Line = "no"
                            $ Count = 1
                    $ Count -= 1
            $ Speed = 1
            $ newgirl["Mystique"].Blush = 1
            "She pulls back with a pop."
            if Line == "question":
                    call MystiqueFace("smile")
                    ch_m "I wasn't being subtle about it, [newgirl[Mystique].Petname]." 
            elif Line == "praise":
                    call MystiqueFace("smile")
                    ch_m "Mmm, hehe."
            elif Line == "no":
                    $ Speed = 0
                    call MystiqueFace("angry")
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "{i}That's{/i} the thanks I get?!"
            else:
                    ch_m "You can stop pretending it, [newgirl[Mystique].Petname]. . ."
                    ch_m "This cock of your's telling me you're awake now."
                
            menu:
                extend ""
                "So, um, you want to go on?":
                        if Line != "no":
                            call MystiqueFace("smile")
                            ch_m "Hehe, mmmm. . ."
                        elif Line == "no" and ApprovalCheck("Mystique", 1750):
                            call MystiqueFace("bemused")
                            ch_m "Wha? Well. . . I guess. . ."
                            $ Line = "maybe"
                        else:
                            call MystiqueFace("angry")
                            ch_m "You can't walk that one back!"
                            ch_m "You can take care of that yourself."
                "Were you more interested in something else?":
                        if Line != "no":
                            call MystiqueFace("sexy")
                            ch_m "Depends. . . like what?"
                            $ Line = "sex"
                        elif Line == "no" and ApprovalCheck("Mystique", 1650):
                            call MystiqueFace("bemused")
                            ch_m "Oh, so you want to do something {i}else{/i} with me. . ."
                            ch_m "Like what?"
                            $ Line = "sex"
                        else:
                            call MystiqueFace("angry")
                            ch_m "Well not anymore!"   
                            ch_m "You can take care of that yourself."
                "Sorry, sorry, please continue." if Line == "no":
                        if (newgirl["Mystique"].Love + newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt) >= 1450:
                            call MystiqueFace("bemused")
                            ch_m "I guess I can forgive you. . ."
                            $ Line = "maybe"
                        else:
                            call MystiqueFace("angry")
                            ch_m "As if."
                "Sorry, but we could do something else." if Line == "no":
                        if ApprovalCheck("Mystique", 1350):
                            call MystiqueFace("sexy")
                            ch_m "I guess, maybe. . ."
                            ch_m "Like what?"
                            $ Line = "sex"
                        else:
                            call MystiqueFace("angry")
                            ch_m "As if."
                "Not when I'm just waking up.":
                        call MystiqueFace("angry")
                        ch_m "Aw. . ."
                        $ newgirl["Mystique"].Eyes = "side"
                        ch_m "Last time I do you a favor. . ."
                        $ Line = "no"
                        
            $ newgirl["Mystique"].RecentActions.remove("blanket") 
            if Line == "no":
                    call Mystique_BJ_Reset
                    if bg_current == "bg player":  
                        ch_m "I'm out of here."
                    else:
                        ch_m "Get out of my face."
                    call MystiqueOutfit
                    $ renpy.pop_call()
                    jump Return_Player
            elif Line == "sex":
                    call Mystique_BJ_Reset
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



# Event Mystique_Caught_Masturbating  /////////////////////////////////////////////////////  

label Mystique_Caught_Masturbating: #Mystique_Update   
            #This label is called from a Location
            call Shift_Focus("Mystique")
            "You hear some odd noises coming from Mystique's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call MystiqueOutfit(Changed=1)    
            $ newgirl["Mystique"].Upskirt = 1
            $ newgirl["Mystique"].PantiesDown = 1
            call Set_The_Scene
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Eyes = "closed"
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ newgirl["Mystique"].DailyActions.append("unseen")
            $ newgirl["Mystique"].RecentActions.append("unseen")    
            call Mystique_SexAct("masturbate")
            if "angry" in newgirl["Mystique"].RecentActions:
                return
        
            #After caught masturbating. . .
            $ newgirl["Mystique"].Eyes = "sexy"
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "smile"
            if newgirl["Mystique"].Mast == 1:        
                    $ newgirl["Mystique"].Mouth = "kiss"
                    ch_m "I wasn't expecting visitors. . ."
                    $ newgirl["Mystique"].Eyes = "side"
                    $ newgirl["Mystique"].Mouth = "lipbite"        
                    ch_m "although for you I could make an exception. . ."
                    $ newgirl["Mystique"].Eyes = "sexy"
                    $ newgirl["Mystique"].Brows = "normal"         
                    $ newgirl["Mystique"].Mouth = "smile"
                    ch_m "Perhaps next time you could knock?" 
            else:
                    ch_m "I notice you make a habit of dropping in."           
            $ newgirl["Mystique"].Girl_Arms = 1  
            call MystiqueOutfit    
            return
    
# end Mystique_Caught_Masturbating/////////////////////////////////////////////////////




# Event Mystique_Caught_Classroom  /////////////////////////////////////////////////////  

label Mystique_Caught_Classroom:  
            #This label is called from a Location
            call Shift_Focus("Mystique")
            "As you walk down the halls, you hear some odd noises coming from the classroom."                           #fix this scene, pants option    
            show blackscreen onlayer black
            $ bg_current = "bg classroom"            
            call CleartheRoom("Mystique",0,1)
            call MystiqueOutfit(Changed=1)     
            $ newgirl["Mystique"].Loc = 0
            call Set_The_Scene
            $ newgirl["Mystique"].Loc = "bg desk"
            $ Taboo = 0
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Eyes = "closed"
            $ newgirl["Mystique"].Girl_Arms = 1
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ Trigger3 = "fondle pussy"
            $ Trigger5 = "fondle breasts"
            $ newgirl["Mystique"].RecentActions.append("classcaught") 
            $ newgirl["Mystique"].DailyActions.append("unseen")
            $ newgirl["Mystique"].RecentActions.append("unseen")    
            $ Line = 0
            call DrainWord("Mystique","no masturbation")
            $ newgirl["Mystique"].RecentActions.append("masturbation")                      
            $ newgirl["Mystique"].DailyActions.append("masturbation") 
            "You see Ms Darkholme leaning back against her desk, her hands tracing slow paths across her body."
            call MystiqueM_Cycle
            if "angry" in newgirl["Mystique"].RecentActions:
                return
        
        #After caught masturbating. . .
            $ newgirl["Mystique"].Eyes = "sexy"
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "normal"             
            $ newgirl["Mystique"].Girl_Arms = 1  
            call MystiqueOutfit    
            $ bg_current = "bg classroom"  
            call Display_Mystique 
            if "classcaught" in newgirl["Mystique"].History: 
                    ch_m "I notice you make a habit of dropping in."  
                    call MystiqueOutfit      
            else:
                    # First time caught
                    $ newgirl["Mystique"].History.append("classcaught") 
                    ch_m "Well."
                    call MystiqueFace("angry", Eyes="side")
                    ch_m "It seems that you've caught me in a somewhat. . . compromising position. . ."
                    menu:
                        extend ""
                        "You say!":
                                call MystiqueFace("perplexed", Mouth="normal")         
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, -5)
                                ch_m "Er, well. . ."
                        "Are you supposed to be rubbing it in class?":
                                call MystiqueFace("angry", Eyes="side")
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                ch_m "Hrm."
                                call MystiqueFace("sly", Brows="angry")
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 3)
                                ch_m "Well, i shouldn't, but you know how it can be,"
                                $ newgirl["Mystique"].Brows = "normal"
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "-surrounded by so many attractive students all day long. . ."
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "you included. . ."
                        "I think it was really hot.":
                                call MystiqueFace("sly")
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 10) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "Hmm, well I suppose I can't blame you for that. . ."
                        "What do you mean?":
                                call MystiqueFace("angry")
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -10)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -5)
                                ch_m "I mean how I was. . ."
                                call MystiqueFace("surprised")
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 15)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 15)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                ch_m "Oh!"
                                call MystiqueFace("perplexed")
                                ch_m "Yes, obviously it was nothing, just getting some. . ."
                                $ newgirl["Mystique"].Eyes = "side"
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "paperwork done. . ."
                                call MystiqueFace("sly")
                                $ Line = 1
                    ch_m "So how did you want to handle this. . . situation?"
                    menu:
                        extend ""
                        "I think I can forget all about it.":
                                call MystiqueFace("smile")
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 10)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15) 
                                ch_m "Thank you, [newgirl[Mystique].Petname]. I appreciate your discretion."
                                call MystiqueFace("sly")
                                ch_m "Are you {i}certain{/i} there's nothing I could do to thank you?"
                        "What do you you have in mind?":
                                call MystiqueFace("sly")
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 15)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "Oh, I'm sure I could make it worth your while. . ."
                        "What situation?":
                                if Line != 1:
                                        call MystiqueFace("confused")
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -5)
                                        ch_m "I mean how I was. . ."
                                        call MystiqueFace("surprised")
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 15)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 15)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                        ch_m "Oh!"
                                        call MystiqueFace("perplexed")
                                        ch_m "Yes, obviously it was nothing, just getting some. . ."
                                        $ newgirl["Mystique"].Eyes = "side"
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        ch_m "paperwork done. . ."
                                        call MystiqueFace("sly")
                                else:
                                        call MystiqueFace("angry")
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                        ch_m "I do wonder if you're just being dense. . ."
                                        call MystiqueFace("sly")
                                        ch_m "Still. . ."
                    $ Line = 0
                    $ MultiAction = 0
                    menu:
                        extend ""
                        "Could you strip?":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15) 
                                ch_m "So you wanted a better view of your teacher?"
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "I suppose I could accomodate that. . ."
                                ch_m "to a point. . ."
                                "Ms Darkholme walks to the door and locks it behind her."
                                $ Tempmod = 50
                                call Mystique_Strip
                        "Could you just keep going?":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 15)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15) 
                                ch_m "Oh, you wanted to watch me some more?"
                                ch_m "I can't exactly blame you."    
                                $ newgirl["Mystique"].Eyes = "down"
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "Will you going to show me something as well?"
                                menu:
                                    "Yeah!":
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 10) 
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        ch_m "Excellent."
                                        if "cockout" not in P_RecentActions:
                                            call Mystique_First_Peen
                                        "You begin to stroke your cock."
                                        $ Trigger2 = "jackin"
                                    "No, you go ahead.":
                                        call MystiqueFace("sad")
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                        ch_m "Pity."
                                call MystiqueFace("sly")
                                "Ms Darkholme walks to the door and locks it behind her."
                                $ Taboo = 0
                                $Trigger = "masturbation"
                                $Trigger3 = "fondle breasts"
                                "Ms Darkholme leans back and runs her fingertips along her breasts."
                                $ Tempmod = 50
                                call MystiqueM_Cycle
                        "Could I feel you up?":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 10) 
                                ch_m "Hmm, I could use some help . . .around the office. . . "
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "perhaps you have some suggestions?"
                                "Ms Darkholme walks to the door and locks it behind her."
                                $ Taboo = 0
                                $ Tempmod = 50
                                call Mystique_FB_Prep
                        "Could you give me a hand? [[point to your cock]":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                                $ newgirl["Mystique"].Brows = "surprised"
                                ch_m "I appreciate boldness, [newgirl[Mystique].Petname], but be a bit more realistic." 
                                $ newgirl["Mystique"].Brows = "normal"
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "Perhaps instead I could just offer a little. . . token of my appreciation."
                                "Ms Darkholme walks to the door and locks it behind her."
                                $ Tempmod = 50
                                call Mystique_Strip
                        "I should just get going then.":
                                call MystiqueFace("surprised")
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                                ch_m "Oh."
                                call MystiqueFace("confused")
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -5) 
                                ch_m "Well, I suppose. . ."
                                call MystiqueFace("perplexed")
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "I'll see you. . . in class then. . ."
                    call MystiqueOutfit     
                    "Afterwards, Ms Darkholme collects her things and walkes toward the door."
                    "She turns back with her hand on the door."
                    call MystiqueFace("sly")
                    ch_m "Oh, and [newgirl[Mystique].Petname]?"
                    ch_m "You can just call me \"Raven.\""
                    $ newgirl["Mystique"].GirlName = "Raven"
                    $ newgirl["Mystique"].Loc = "bg Mystique"
                    hide Mystique_Sprite with easeoutleft
                    $ Round = 20 if Round > 20 else Round
                    $ MultiAction = 1
            return
    
# end Mystique_Caught_Classroom/////////////////////////////////////////////////////


# Event Mystique_Detention  /////////////////////////////////////////////////////  

label Mystique_Detention:  
            #This label is called from a Location
            call Shift_Focus("Mystique")
            call CleartheRoom("Mystique",0,1)
            if "traveling" in P_RecentActions:
                "You enter the room and see Mystique waiting for you at the back of the room."
            else:
                "After class, the students file out, and you wait a few minutes until they're all gone."
                "Once the last student leaves, Mystique approaches you."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ newgirl["Mystique"].Loc = "bg classroom"
            call MystiqueOutfit    
            call Set_The_Scene     
            call MystiqueFace("sly")
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Count = 0  
            call CleartheRoom("Mystique",0,1)
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in P_DailyActions:
                ch_m "I'm glad you take your. . . education seriously."
            else:
                #if you skipped detention
                call MystiqueFace("surprised")  
                ch_m "Oh, [newgirl[Mystique].Petname], you really shouldn't skip your detention like that. . ."            
            $ P_Traits.remove("detention") 
            $ newgirl["Mystique"].RecentActions.append("detention") 
            $ newgirl["Mystique"].DailyActions.append("detention") 
            call MystiqueFace("sly")  
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 3)
            ch_m "You've been such a naughty student. . ."
            $ newgirl["Mystique"].Girl_Arms = 1
            call MystiqueFace("sadside", Brows="normal")  
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
            ch_m "Chasing after those young girls. . ."            
            call MystiqueFace("sly")  
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 3)
            if "detention" in newgirl["Mystique"].History:
                ch_m "What will we do with you this time?"
            else:
                #first time
                ch_m "What am I to do with you. . ."
                $ newgirl["Mystique"].History.append("detention") 
            
            "Mystique walks to the door and locks it behind her."
            $ Taboo = 0
            menu:
                extend ""
                "I guess I should focus on my studies.":  
                        if ApprovalCheck("Mystique", 900) and "classcaught" in newgirl["Mystique"].History:
                                call MystiqueFace("perplexed")   
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -3) 
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                ch_m "Oh. Really? I was thinking of a more. . . physical punishment."
                                menu:
                                    extend ""
                                    "Kidding, of course, what should we do? [[sex stuff]":
                                        call MystiqueFace("sly")  
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                        ch_m "Why do I put up with you?"
                                        call Mystique_SexMenu
                                    "No, you're right, I take my education too lightly.":
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1) 
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -2) 
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        ch_m "Oh. Ok. Um. . ."
                                        call MystiqueFace("sad")  
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        ch_m "I guess we could go over some of the topics from today's class then. . ."
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        $ P_XP += 10
                        else:
                                        #She's not into you yet.
                                        call MystiqueFace("sad", Mouth="normal")  
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 5) 
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 5) 
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        ch_m "Yes. . . Exactly. . ."
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        ch_m "I guess we could go over some of the topics from today's class then. . ."
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                        $ P_XP += 10
                "I could think of a few things. . . [[sex stuff]":
                        if ApprovalCheck("Mystique", 900) and "classcaught" in newgirl["Mystique"].History:
                                call MystiqueFace("sly")  
                                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                                ch_m "I know you can. . ."
                                call Mystique_SexMenu
                        else:
                            #She's not into you yet.
                            call MystiqueFace("sad", Mouth="smirk")  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 5) 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                            ch_m "I'm sure you could. . . but unfortunately this isn't the time for it."
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5) 
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                            ch_m "We'll just have to settle for going over some of the topics from today's class. . ."
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5) 
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)
                            $ P_XP += 10                            
            $ Round = 20 if Round > 20 else Round 
            ch_m "Ok, I think that's plenty for now. . ."
            ch_m "You wouldn't want to make this a habit. . ."
            call MystiqueOutfit  
            return            
    
# end Mystique_Detention/////////////////////////////////////////////////////


# Event Mystique_Key /////////////////////////////////////////////////////  

#Not updated

label Mystique_Key: #Mystique_Update   
            call Shift_Focus("Mystique")
            call Set_The_Scene
            call MystiqueFace("bemused")
            $ newgirl["Mystique"].Girl_Arms = 2
            ch_m "So you've been coming by a lot lately, I think you might want a key. . ."
            ch_p "Thanks."
            $ newgirl["Mystique"].Girl_Arms = 1    
            $ Keys.append("Mystique")
            $ newgirl["Mystique"].Event[0] = 1
            return
# end Event Mystique_Key /////////////////////////////////////////////////////


# Event Mystique_Caught /////////////////////////////////////////////////////  

label Mystique_Caught: #Mystique_Update   
    call Shift_Focus("Mystique")
    call Checkout
    ch_m "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call MystiqueOutfit
    $ bg_current = "bg study"  
    $ newgirl["Mystique"].Loc = "bg study"
    call Set_The_Scene(0)

    show Professor at SpriteLoc(StageLeft)    
    show Mystique_Sprite at SpriteLoc(StageRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease

    # show Professor at center
    # with fade
    call XavierFace("shocked")
    call MystiqueFace("sad")
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
    
    if newgirl["Mystique"].Shame >= 40:
        ch_x "Mystique, my dear, you're practically naked! At least throw a towel on!"
        "He throws Mystique the towel."
        show blackscreen onlayer black 
        $ newgirl["Mystique"].Over = "towel"         
        hide blackscreen onlayer black
    elif newgirl["Mystique"].Shame >= 20:
        ch_x "Mystique, my dear, that attire is positively scandalous."
    
    if newgirl["Mystique"].Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2)
        ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1)
        $ R_Eyes = "side"
        
    $ Count = newgirl["Mystique"].Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if newgirl["Mystique"].Caught < 5:
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, -25)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -10) 
            call XavierFace("happy")  
            if newgirl["Mystique"].Caught:
                ch_x "But you know you've done this before. . . at least [newgirl[Mystique].Caught] times. . ." 
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
            
        "Just having a little fun, right [newgirl[Mystique].Pet]?":
            call Mystique_Namecheck
            call MystiqueFace("bemused")         
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 10)   
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10) 
            call XavierFace("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, -20)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Mystique, plan Mu" if "Xavier's photo" in P_Inventory and P_Lvl >= 5:
            if ApprovalCheck("Mystique", 1500, TabM=1, Loc="No"):                   
                    jump Plan_Mu
            elif ApprovalCheck("Mystique", 1000, TabM=1, Loc="No"):
                    call MystiqueFace("perplexed") 
                    $ newgirl["Mystique"].Brows = "sad"
                    ch_m "You know. . . I really don't think that's a good idea. . ."
                    menu:
                        "Dammit Mystique. . .":
                                call MystiqueFace("angry")
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5) 
                        "Yeah, I guess you're right. . .":
                                call MystiqueFace("bemused") 
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5) 
            else:
                    call MystiqueFace("confused") 
                    ch_m "Wait, Plan what??"
                    ch_p "Plan {i}Mu!{/i} . . you know. . ."
                    ch_m "I have no {i}idea{/i} what you're talking about."
                    ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                    call MystiqueFace("bemused") 
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, -10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -5)   
            ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 25)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 40)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!" 
            if newgirl["Mystique"].Inbt > 50:
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 15)             
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, -20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -10)    
            ch_x "Now get out of my sight."
            
    $ PunishmentX += Count            
    $ newgirl["Mystique"].Caught += 1
    $ newgirl["Mystique"].RecentActions.append("caught")
    $ newgirl["Mystique"].DailyActions.append("caught")     
    if "Mystique" in Party:
        $ Party.remove("Mystique")     
    if "Rogue" in Party:
        $ Party.remove("Rogue")
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Mu: #Mystique_Update   
    call MystiqueFace("sly")         
    "As you say this, a sly grin crosses Mystique's face."
    #$ newgirl["Mystique"].Arms = 0
    $ newgirl["Mystique"].Girl_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."    
    $ newgirl["Mystique"].Girl_Arms = 2
    show Mystique_Sprite at SpriteLoc(650,150) with ease 
    $ MSpriteLoc = StageLeft
    "Mystique moves in sits on his lap, pinning his arms to the chair."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised")      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly")
    call XavierFace("angry")
    
    if "Kappa" in P_Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
    else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the photo you found earlier in his study."
            ch_p "I have here a rather. . . compromising photo of you and Mystique."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "Mystique here's set it to distribute to every computer in school, every day."
            ch_p "And only I know the password." 
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ." 
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 40)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 30)
    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_m "Well, [newgirl[Mystique].Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if newgirl["Mystique"].Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ newgirl["Mystique"].Rules = 0
            "You know, it's kinda fun dodging you, catch us if you can." if not newgirl["Mystique"].Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ newgirl["Mystique"].Rules = 1
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
                    
                    "Give me the key to Mystique's room." if "Mystique" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."  
                            $ Keys.append("Mystique")
                    "Give me the key to Mystique's room.[[Owned] (locked)" if "Mystique" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_x "Very well, that should conlude our business. Please leave." 
    if "Psi" not in P_Traits:
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 10)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 10)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
        $ P_Traits.append("Psi")
    $ newgirl["Mystique"].Girl_Arms = 1
    "You return to your room"
    jump Player_Room
                              
# end Mystique_Caught/////////////////////////////////////////////////////

# start Mystique_BF//////////////////////////////////////////////////////////

label Mystique_BF: #Mystique_Update   
    call Shift_Focus("Mystique")
    
    if newgirl["Mystique"].Loc != bg_current and "Mystique" not in Party:
        "Mystique approaches you and asks if the two of you can talk."
        "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."    
                
    $ newgirl["Mystique"].Loc = bg_current
    call Set_The_Scene 
    call Taboo_Level
    call CleartheRoom("Mystique")
    $ newgirl["Mystique"].DailyActions.append("relationship")
    call MystiqueFace("bemused", 1)
    ch_m "So, [newgirl[Mystique].Petname], we've been hanging for a while, right?"
    ch_m ". . ."
    $ newgirl["Mystique"].Eyes = "sexy"
    menu:
        ch_m "Right?"
        "Yeah. And it's been amazing.":
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
        "Yeah, I guess":
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 10)
        "Uhm. . .maybe?":
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
    if newgirl["Mystique"].SEXP >= 10:
        ch_m "I mean, I've gone further with you than I've ever been with anybody before. . ."
    if newgirl["Mystique"].SEXP >= 15:
        ch_m "You know . . .in the {i}bedroom{/i}. . ."
    if "dating" in R_Traits and "dating?" in newgirl["Mystique"].Traits:    
        ch_m "I know you're kinda Rogue's boyfriend and all. . . but she and I were talking and . . ."
    elif "dating" in newgirl["Mystique"].Traits:
        ch_m "I know you're kinda Rogue's boyfriend and all. . ."
    if not newgirl["Mystique"].Event[5]:
        ch_m "So, uhm. . ."
        ch_m "It’s not like I haven’t gone out with young guys before."
        ch_m "I just ..wow, this is so awkward.  I really like you a lot and. . ."
        ch_m "I think. . . do you want be my boyfriend?"
        ch_m " well we could make it official?"
    elif "dating?" in newgirl["Mystique"].Traits: 
        ch_m "Rogue said it’d totally be cool if we were dating, too." 
    elif "dating" in R_Traits: 
        ch_m "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:        
        ch_m "I wish you weren’t such a jerk sometimes, but still. . . I’m totally serious about this."
        ch_m "I wanna be your girlfriend officially."
    $ newgirl["Mystique"].Event[5] += 1
    menu: 
        extend ""
        "Are you kidding?  I'd love to!":
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30)
            $ newgirl["Mystique"].Petnames.append("boyfriend")
            $ newgirl["Mystique"].Traits.append("dating")
            "Mystique wraps her arms around you and starts kissing you passionately."
            call MystiqueFace("kiss") 
            $ newgirl["Mystique"].Kissed += 1
        "Uhm okay.":
            $ newgirl["Mystique"].Petnames.append("boyfriend")
            $ newgirl["Mystique"].Traits.append("dating")
            $ newgirl["Mystique"].Brows = "confused"
            "Mystique seems a little put off by how casually you’re taking all this."
            "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."    
        "I'm with Rogue now." if "dating" in R_Traits:             
            call MystiqueFace("sad",1)    
            ch_m "I know.  I just . . . I thought maybe you could go out with me, too, by any chance?"
            menu:
                extend ""
                "Yes.  Absolutely.":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30)
                    $ newgirl["Mystique"].Petnames.append("boyfriend")
                    $ newgirl["Mystique"].Traits.append("dating")
                    "Mystique wraps her arms around you and starts kissing you passionately."
                    call MystiqueFace("kiss") 
                    $ newgirl["Mystique"].Kissed += 1
                "I'm sorry, but. .  .no.":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                    ch_m "Well. . . okay. I get it." 
                "No way.":
                    jump Mystique_BF_Jerk
        "Not really.":
            jump Mystique_BF_Jerk
    call MystiqueFace("sexy")    
    ch_m "Now. . . boyfriend. . . how about you and I celebrate a little, huh?"
    $ Tempmod = 10
    call Mystique_SexMenu
    $ Tempmod = 0
    return
    
label Mystique_BF_Jerk:
    call MystiqueFace("angry", 1)
    ch_m "Fine! . . .be that way!" 
    $ Count = (20* newgirl["Mystique"].Event[5])
    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 40)
    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, Count)
    if newgirl["Mystique"].Event[5] >= 3:
        call MystiqueFace("sad")
        ch_m "Yeah?  Well. . . I don’t care what you want!  We’re dating!  Deal."   
        $ newgirl["Mystique"].Petnames.append("boyfriend")
        $ newgirl["Mystique"].Traits.append("dating")
        $ Achievements.append("I am not your Boyfriend!")
        ch_m "I. . .uhm. . .think I need to be alone for a little while."
        $ bg_current = "bg player"   
        call Set_The_Scene
        return        
    if newgirl["Mystique"].Event[5] > 1:
        ch_m "It was such a mistake asking you again.  You’re still such an Asshole!"          
    $ Count = (50* newgirl["Mystique"].Event[5])                                  #fix test to see if negatives can work here.
    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -Count)
    ch_m "Get out, you big Asshole!"
    $ newgirl["Mystique"].Loc = "bg Mystique"
    $ bg_current = "bg player"   
    call Set_The_Scene
    $ renpy.pop_call()
    jump Player_Room
    
## end Mystique_BF//////////////////////////////////////////////////////////

## start Mystique_Love//////////////////////////////////////////////////////////
label Mystique_Love: #Mystique_Update   
    call Shift_Focus("Mystique")  
    if newgirl["Mystique"].Event[6]:
            #on repeat attempts
            "Mystique seems kind of shy and shuffles up to you, as if working up her nerve."
    elif bg_current != "bg Mystique":
        if newgirl["Mystique"].Loc == bg_current or "Mystique" in Party:
            "Suddenly, Mystique says she wants to talk to you in her room and drags you over there."
        else:
            "Mystique shows up, hurridly says she wants to talk to you in her room and drags you over there."
        $ bg_current = "bg Mystique"
    else:
            "Mystique suddenly stares at you very intently."
        
    $ newgirl["Mystique"].Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Mystique")
    call Taboo_Level
    $ newgirl["Mystique"].DailyActions.append("relationship")
    call MystiqueFace("bemused", 1)
    $ newgirl["Mystique"].Eyes = "side"    
    $ Line = 0
    $ newgirl["Mystique"].Event[6] += 1
    if newgirl["Mystique"].Event[6] == 1:
            if "dating" in newgirl["Mystique"].Traits:
                ch_m "We've been together for a while now, and I've been thinking. . ."
            else:
                ch_m "We've know each other for a while now, and I've been thinking. . ."
            ch_m "It's been kinda hard for me to really get invested in anyone. . ."
            $ newgirl["Mystique"].Eyes = "down"
            ch_m ". . . to be comfortable with who they are and be myself. . ."
            $ newgirl["Mystique"].Eyes = "sly"
            ch_m "I just feel like sometimes you. . ."
            $ newgirl["Mystique"].Eyes = "side"
            ch_m "and me  . ."
            call MystiqueFace("perplexed", 2)
            $ newgirl["Mystique"].Eyes = "surprised"
            ch_m "Never mind!"
            "Mystique dashes off and runs through the nearest Door."
            hide Mystique_Sprite with easeoutright
            call Remove_Girl("Mystique")
            return
    if newgirl["Mystique"].Event[6] == 2:
        ch_m "Sorry about before, I don't think I was ready maybe. . ."
        ch_m ". . . but I was kind of thinking-"   
    elif newgirl["Mystique"].Event[6] >= 5:
        ch_m "Um. . ."
        $ newgirl["Mystique"].Eyes = "sly"
        ch_m "You know, it's time to stop running. I think I love you."
        $ newgirl["Mystique"].Eyes = "side"
        ch_m "You don't have to say it back, but I do."
        $ newgirl["Mystique"].Petnames.append("lover")
        ch_m "Um, that's all."
    else:
        ch_m "Um. . ."
    if "lover" not in newgirl["Mystique"].Petnames: 
            menu:
                "She turns and makes a break for the nearest Door."
                "Catch her":
                    call MystiqueFace("perplexed", 2)
                    $ newgirl["Mystique"].Eyes = "surprised"
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 10) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 15) 
                    "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
                "Let her go":
                    "She dashes through the nearest doorway and vanishes from view."
                    jump Mystique_Love_End    
            $ newgirl["Mystique"].Blush = 1
            menu:
                extend ""
                "Pull her close":
                    call MystiqueFace("smile", 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 20) 
                    "You draw her into an embrace, arms wrapped tightly around her waist."
                    $ Line = "hug"
                "Stay like this":
                    $ newgirl["Mystique"].Eyes = "down"
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 10) 
                    "You keep hold of her wrist."
                    $ Line = "wrist"
                "Let her go":
                    if 1 < newgirl["Mystique"].Event[6] < 4:
                        "You immediately release her wrist."
                        $ newgirl["Mystique"].Eyes = "down"
                        "She dashes through the nearest doorway and vanishes from view."
                        jump Mystique_Love_End
                    else:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 10) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 20)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)  
                        "You release her wrist and she takes a step back."
                        
            ch_m "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in newgirl["Mystique"].Petnames:        
            # If she hasn't confessed yet
            ch_m "I thought maybe if I let myself get too close. . ."
            ch_m "I'd fall. . ."
            menu:
                extend ""
                "I'll never let go." if Line:
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 20) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)  
                    "She melts into your arms."
                "I'd always catch you.":
                    call MystiqueFace("smile")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 20) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 15)
                    "She smiles and shifts a bit uncomfortably."
                "Yeah, you should watch out for that.":
                    call MystiqueFace("angry", 1)
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)  
                    "She shoves you away and then stomps through the nearest door."                        
                    jump Mystique_Love_End
                    
                "So get going. [[Give her a shove]":
                    call MystiqueFace("surprised", 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -50) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)  
                    "You shove her through the nearest door and then continue on you way."
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    hide Mystique_Sprite with easeoutbottom
                    jump Mystique_Love_End
                    
    if "lover" in newgirl["Mystique"].Petnames: 
        #if she made the first move
        menu:
            extend "" #"I love you."
            "I love you too.":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 40) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 50)  
                        call MystiqueFace("smile")
            "You love me?":
                call MystiqueFace("confused", 2)
                menu:
                    ch_m "But you don't love me?"
                    "Yeah, of course I do!":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 60)  
                        call MystiqueFace("smile")
                    "I mean, a little?": 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 20)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -10)  
                        ch_m "That's not a \"yes.\" . ."
                        $ Line = "awkward"
                    "Not really.":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 30)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -30)  
                        call MystiqueFace("angry", 2)
                        ch_m "Huh?!"
                        $ Line = "awkward"
            "Huh.":
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -20)  
                menu:
                    ch_m "Huh?!"
                    "I mean, I love you too!":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)  
                        call MystiqueFace("smile")
                        ch_m "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 30)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -20)  
                        call MystiqueFace("angry", 2)
                        $ Line = "awkward"
            "Well that's awkward.":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 40)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -20)  
                        call MystiqueFace("perplexed", 2)
                        $ Line = "awkward"
    else:
        menu:
            extend ""
            "I love you, Mystique.":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 50) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 30)  
                        call MystiqueFace("smile")
                        $ Line = "love"
            "I think you're pretty great.":
                call MystiqueFace("confused")
                menu:
                    ch_m "But you don't love me?"
                    "Yeah, of course I do!":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 30) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)  
                        call MystiqueFace("smile")
                    "I mean, a little?":
                        if ApprovalCheck("Mystique", 1200, "OI"):
                            call MystiqueFace("sad")
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 20)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)  
                            ch_m "But not \"nothing\". . ."
                        else:
                            $ Line = "awkward"
                    "Not really.":     
                        call MystiqueFace("sad")                   
                        if ApprovalCheck("Mystique", 1500, "OI"):
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 30)
                            ch_m "Ouch. . ."
                        else:
                            $ Line = "awkward"
            "I was thinking something more casual. . .":
                        call MystiqueFace("sad")
                        if ApprovalCheck("Mystique", 1200, "OI") or ApprovalCheck("Mystique", 700, "I"):
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 20)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 30)  
                            ch_m "Close enough."
                        else:  
                            $ Line = "awkward"
                            
    if Line == "awkward":   
        if ApprovalCheck("Mystique", 700, "O"):   
            ch_m "Fine, this doesn't have to be love."
        elif ApprovalCheck("Mystique", 700, "I"):
            ch_m "Fine, just sex it is."            
        elif ApprovalCheck("Mystique", 1200, "OI"):
            ch_m "Fine, I can work with that."
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -50) 
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 95, 50)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -50)  
            ch_m "Oh, well I mean if you don't love me-"
            ch_m "You don't have to love me, that's ok."
            ch_m "I'll, um. . . never mind."
            $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].Event[6] = 20 #this means it shuts down future attempts
    else:
        if Line:
            # If you're holding her
            "She squeezes you even tighter and makes a little whimper."
        else:
            "She dives into your arms with a little squeek."
        if "lover" not in newgirl["Mystique"].Petnames:
            ch_m "I love you too. . ."
            ch_m "I think I have for a while now."
            $ newgirl["Mystique"].Petnames.append("lover")
    
label Mystique_Love_End:    
    if Line == "awkward" or "lover" not in newgirl["Mystique"].Petnames:
            hide Mystique_Sprite with easeoutright
            call Remove_Girl("Mystique")
            return
    if not newgirl["Mystique"].Sex:
        ch_m "So I was thinking. . . did you want to . . ."
        if bg_current != "bg player" and bg_current != "bg Mystique":
                ch_m "Wait, let's take this someplace more private. . ."
                $ bg_current = "bg Mystique"
                $ newgirl["Mystique"].Loc = bg_current
                call Set_The_Scene
                call CleartheRoom("Mystique")
                call Taboo_Level
                ch_m "Ok, so like I was saying. . ."
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
        menu:
            extend ""
            "Yeah, let's do this. . . [[have sex]":      
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "E_Inbt", newgirl["Mystique"].Inbt, 30, 30) 
                ch_m "Hmm. . ."  
                call Mystique_SexAct("sex")
            "I have something else in mind. . .[[choose another activity]":
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
                ch_m "Something like. . ."    
                $ Tempmod = 20
                call Mystique_SexMenu     
    return
    
label Mystique_Love_Redux:
    #this is for if you rejected her but want a second chance
    $ Line = 0
    $ newgirl["Mystique"].DailyActions.append("relationship")
    if newgirl["Mystique"].Event[6] >= 25:
            #if this is the second time through
            ch_p "I hope you've forgeven me, I still love you."
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 10) 
            if ApprovalCheck("Mystique", 950, "L"):
                $ Line = "love"
            else:
                call MystiqueFace("sad")   
                ch_m "You've dug too deep a hole, [newgirl[Mystique].Petname]."
                ch_m "Keep trying though." 
    else:
            ch_p "Remember when I told you that I didn't love you?"
            call MystiqueFace("perplexed",1)   
            ch_m "Um, YEAH?!"
            menu:
                "I'm sorry, I didn't mean it.":
                    $ newgirl["Mystique"].Eyes = "surprised"
                    ch_m "Well, if you. . . so wait, you {i}do{/i} love me?"
                    ch_p "Yeah. I mean, yes, I love you, Mystique."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 10) 
                    if ApprovalCheck("Mystique", 950, "L"):
                        $ Line = "love"
                    else:
                        call MystiqueFace("sadside")   
                        ch_m "Well, I don't know how I feel at this point. . ."                        
                "I've changed my mind, so. . .":
                    if ApprovalCheck("Mystique", 950, "L"):
                        $ Line = "love"
                        $ newgirl["Mystique"].Eyes = "surprised"
                        ch_m "Really?!"
                    else:
                        $ newgirl["Mystique"].Mouth = "sad"
                        ch_m "Oh, you've changed your mind. Wonderful."
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 10) 
                        call MystiqueFace("sadside")    
                        ch_m "Maybe I have too. . ."
                "Um, never mind.":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)  
                    call MystiqueFace("angry")   
                    ch_m "Seriously?"
                    $ newgirl["Mystique"].RecentActions.append("angry")
    if Line == "love":
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 40) 
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 10) 
            call MystiqueFace("smile")    
            ch_m "I love you too!"
            if newgirl["Mystique"].Event[6] < 25:             
                call MystiqueFace("sly")   
                "She slugs you in the arm"
                ch_m "Took you long enough."
            $ newgirl["Mystique"].Petnames.append("lover")                
    $ newgirl["Mystique"].Event[6] = 25
    return
## end Mystique_Love//////////////////////////////////////////////////////////


# start Mystique_Sub//////////////////////////////////////////////////////////

label Mystique_Sub:     #Mystique_Update   
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Loc != bg_current and "Mystique" not in Party:
        "Suddenly, Mystique shows up and says she needs to talk to you."
    
    $ newgirl["Mystique"].Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Mystique")
    call Taboo_Level
    $ newgirl["Mystique"].DailyActions.append("relationship")
    call MystiqueFace("bemused", 1)
    
    $ Line = 0
    ch_m "So, uhm. . .you've really kinda taken control in our relationship lately."
    menu:    
        extend ""        
        "I guess. That's just kind of what comes naturally for me.":   
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
        "Sorry. I didn't mean to come off like that.":
                call MystiqueFace("startled", 2)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 5)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -5)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -5)
                ch_m "No!  Don't get the wrong idea!  I just. . ." 
        "Yup. Deal with it.": 
                if ApprovalCheck("Mystique", 1000, "LO"):
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 20)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                        ch_m "Um, yeah. . ."
                else:
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                        call MystiqueFace("angry")
                        ch_m "I {i}was{/i} going to tell you I kinda liked it.  But I didn't think you'd be a {i}jerk{/i} about it!" #(Loss of points)
                        menu:        
                            extend ""
                            "Guess you don't know me so well, huh?":
                                    ch_m "I guess not."
                                    $ Line = "rude"
                            "Sorry.  I kind of thought you were getting into me being like that.": 
                                    call MystiqueFace("sexy", 2)
                                    $ newgirl["Mystique"].Eyes = "side"
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                                    ". . ."
     
    $ newgirl["Mystique"].Blush = 1       
    if not Line:
            # She's advancing to the next stage            
            ch_m "Well, I've, uhm. . . never had a guy be like that with me before. . ."
            call MystiqueFace("sly", 2)
            ch_m "I think I kinda like it."
            call MystiqueFace("smile", 1)
            menu:
                extend ""
                "Good. If you wanna be with me, that's how it'll be.":
                        if ApprovalCheck("Mystique", 1000, "LO"):
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 15)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                            ch_m "I guess I walked into that one. . ."                        
                        else:
                            call MystiqueFace("sadside", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)                      
                            ch_m "You don't have to do it {i}all{/i} the time.  You could still be nice once in a while."
                            menu:      
                                extend ""
                                "Whatever.  That's how it is.  Take it or leave it.":
                                        call MystiqueFace("angry")
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                                        ch_m "Y'know, you're such an ass, [Playername]!" 
                                        $ Line = "rude"
                                "I think I could maybe do that." : 
                                        call MystiqueFace("bemused", 2)
                                        $ newgirl["Mystique"].Eyes = "side"
                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 5)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 3)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                                        ch_m "Well. . .yeah.  It's . . kinda hot."
                                
                "Yeah?  You think it's sexy?":
                            call MystiqueFace("bemused", 2)
                            $ newgirl["Mystique"].Eyes = "side"
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                            ch_m "Well. . .yeah.  It's . . kinda hot."
                        
                "You sure you don't want me to back off a little?":  
                        call MystiqueFace("startled", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -5)
                        menu:
                            ch_m "Only if you think it might be weird. But I think it's kinda hot."
                            "Only if you're okay with it.":
                                call MystiqueFace("bemused", 2)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 10)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                                $ Line = 0
                            "Well. . .yeah.  I {i}do{/i} think it's weird.  Sorry.":                                
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -5)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -10)
                                $ Line = "embarrassed"
                        
                "I don't really care what you like.  I do what I want.":
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 15)
                            call MystiqueFace("angry")
                            ch_m "Y'know, you're such an ass, [Playername]!" 
                            $ Line = "rude"
                                        
    if not Line:
        call MystiqueFace("bemused", 1)
        $ newgirl["Mystique"].Eyes = "down"
        ch_m "Cool.  So. . .just so you know. . .I don't mind you being in control."
        if "256 Shades of Grey" in newgirl["Mystique"].Inventory:
                ch_m "Like in that '256 Shades of Grey' book."
        menu Mystique_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -15)
                    $ Line = "embarrassed"
            "I think I could get used to that kinda thing.":
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                    call MystiqueFace("smile", 1)
                    $ Line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in newgirl["Mystique"].Inventory and Line != "grey":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 5)
                    call MystiqueFace("sly", 1)
                    ch_m "You think I wouldn't read something you bought me?  I think you {i}maybe{/i} don't realize how much I like you."
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                    ch_m "Well, I {i}did{/i} read it.  And. . .it turns out it kinda . . {i}really{/i} turned me on."
                    ch_m "So. . .what d'you think?  Think maybe you'd like that?"
                    $ Line = "grey"
                    jump Mystique_Sub_Choice

    if not Line:
        call MystiqueFace("smile", 1)
        ch_m "Awesome.  So. . .if you wanted me to, I could call you {i}sir{/i} or something."
        call MystiqueFace("sly", 2)
        ch_m "Think you'd like that?"        
        $ newgirl["Mystique"].Blush = 1  
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 95, 5)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 15)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                    ch_m "Okay, then. . .{i}sir{/i}."              
                    $ newgirl["Mystique"].Petname = "sir"
            "I think I'd rather stick with what we've got going.":
                call MystiqueFace("startled", 2)
                ch_m "Oh!"
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -5)
                call MystiqueFace("sadside", 1)
                menu:
                    ch_m ". . . Well. . . maybe you can still kinda be in control, anyway?"
                    "I like that idea.":
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                            call MystiqueFace("smile", 1)
                            ch_m "You're so awesome, [newgirl[Mystique].Petname]."
                    "This is getting really weird.":
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -50)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -15)
                            $Line = "embarrassed"
        
    #Mystique_Sub_Bad_End:
    $ newgirl["Mystique"].History.append("sir")
    if not Line:
            $ newgirl["Mystique"].Blush = 1  
            "She gives you a piece of paper with the password for her cellphone calender."
            "Apparently, whatever you enter into it, she intends to do. . . within reason."
            $ newgirl["Mystique"].Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":        
            hide Mystique_Sprite with easeoutbottom                     
            call Remove_Girl("Mystique")
            $ renpy.pop_call()
            "Mystique walks through the door in a huff, leaving you alone."
    elif Line == "embarrassed":
            call MystiqueFace("sadside", 2)
            ch_m "Oh!  Uhm, yeah!  I mean. . .."
            $ newgirl["Mystique"].Mouth = "smile"
            ch_m "I was just kidding.  I . . yeah.  That's kinda weird."
            ch_m "I should go.  I think I hear Professor McCoy calling me."
            $ newgirl["Mystique"].Blush = 1            
            hide Mystique_Sprite with easeoutbottom                     
            call Remove_Girl("Mystique")
            $ renpy.pop_call()
            "Mystique walks through the door, leaving you alone. It didn't look like she could get away fast enough."
    return

label Mystique_Sub_Asked: #Mystique_Update   
    $ Line = 0
    call MystiqueFace("sadside", 1)
    ch_m "Yeah.  And I also remember what an {i}asshole{/i} you were to me about it."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 850, "O"): 
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck("Mystique", 550, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500 
                        pass
                else: #if it failed both those things,    
                        ch_m "Well maybe {i}I'm{/i} over that. . ." #Failed again. :(       
                        $ Line = "rude"
                        
                if Line != "rude":    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
                        call MystiqueFace("sly", 1)
                        ch_m "Well. . .okay.  I {i}did{/i} think that was pretty hot.  Also, you're so cute when you apologize." 
                        #Blushing expression.  Mystique kisses player and big addition of points
                        ch_m "Okay.  We can try again." 

        "Listen. . .I know it's what you want.  Do you want to try again, or not?":
                call MystiqueFace("bemused", 1)
                if "sir" in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 850, "O"): 
                        ch_m "Ok, fine."
                elif ApprovalCheck("Mystique", 600, "O"): 
                        ch_m "Um, ok."
                else: 
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        call MystiqueFace("sadside", 1) 
                        ch_m "You're totally impossible."
                        $ newgirl["Mystique"].Eyes = "squint"
                        ch_m "Maybe you're right.  But I still think you should  apologize for being an ass to me."
                        menu:
                            extend ""
                            "Okay, I'm sorry I was mean about it.":
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                                    call MystiqueFace("bemused", 1)
                                    $ newgirl["Mystique"].Eyes = "side"
                                    ch_m "That's all you had to say."
                            "Not gonna happen.":
                                    if "sir" in newgirl["Mystique"].Petnames and ApprovalCheck("Mystique", 900, "O"): 
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                                            ch_m ". . ."
                                    elif ApprovalCheck("Mystique",650, "O"):  
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                                            ch_m "I, um. . ."    
                                    else: #if it failed both those things,     
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, -10)
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -10)
                                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -15)                       
                                            "Mystique sighs and rolls her eyes."
                                            call MystiqueFace("angry", 1)
                                            $ newgirl["Mystique"].Eyes = "side"
                                            ch_m "You really don't learn, do you?"    
                                            $ Line = "rude"
                            "Ok, never mind then.":    
                                    call MystiqueFace("angry", 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, -10)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -10)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -15)
                                    ch_m "Y'know, if you're gonna throw that in my face, forget it."
                                    ch_m "I should've expected you'd be like that."
                                    $ Line = "rude"
    
    $ newgirl["Mystique"].RecentActions.append("asked sub")   
    $ newgirl["Mystique"].DailyActions.append("asked sub")     
    if Line == "rude":            
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Mystique_Sprite with easeoutbottom                     
            call Remove_Girl("Mystique")
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ renpy.pop_call()
            "Mystique goes through the door, leaving you alone.  She looked pretty upset."
    elif "sir" in newgirl["Mystique"].Petnames:
            #it didn't fail and "sir" was covered
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 50)
            $ newgirl["Mystique"].Petnames.append("master")  
            $ newgirl["Mystique"].Petname = "master"
            $ newgirl["Mystique"].Eyes = "sly"
            ch_m ". . . master. . ."
    else:
            #it didn't fail
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 30)
            $ newgirl["Mystique"].Petnames.append("sir")  
            $ newgirl["Mystique"].Petname = "sir"
            $ newgirl["Mystique"].Eyes = "sly"
            ch_m ". . . sir."
    return

# end Mystique_Sub//////////////////////////////////////////////////////////


# start Mystique_Master//////////////////////////////////////////////////////////

label Mystique_Master:  #Mystique_Update   
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Loc != bg_current and "Mystique" not in Party:
        "Suddenly, Mystique shows up and says she needs to talk to you."
    
    $ newgirl["Mystique"].Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Mystique")
    $ newgirl["Mystique"].DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    call MystiqueFace("bemused", 1)
    ch_m "[newgirl[Mystique].Petname], if you don't mind me saying so. . ."
    ch_m "I think having you be in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
                call MystiqueFace("sly", 1)
                ch_m "Cool.  Maybe we could kick it up a notch?"
                menu:
                    extend ""
                    "Nah.  This is just about perfect.":
                            call MystiqueFace("sad", 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -15)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                            ch_m "Oh.  Well, okay, I guess."     
                            $ Line = "fail"                      
                    "What'd you have in mind?":
                            $ newgirl["Mystique"].Eyes = "side"
                            ch_m "I dunno. I was thinking maybe I could start calling you. . . {i}master{/i}?"
                            $ newgirl["Mystique"].Eyes = "squint"
                            ch_m "Would you like that?  I think that'd be kinda hot."
                            menu:
                                extend ""
                                "Oh, yeah.  I'd like that.":
                                        ch_m "Cool. . ."
                                "Uhm. . .nah.  That's too much.":
                                        call MystiqueFace("sad", 1)
                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -15)
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                                        ch_m "Oh.  Well, okay, I guess."
                                        $ Line = "fail"

                    "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":
                            call MystiqueFace("sly", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 15)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -10)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)
                            ch_m "Aw, I guess I can't get mad about that. . ."
                            $ Line = "fail"
                            
                    "Actually, let's stop that. It's creeping me out.":
                            call MystiqueFace("perplexed", 2)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -50)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -15)
                            ch_m "Oh.  Sorry.  I guess I got carried away with it."
                            $ newgirl["Mystique"].Blush = 1
                            $ Line = "embarrassed"
                            
        "As if I care what you think, slut.":
                call MystiqueFace("sad", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -10)
                menu:
                    extend ""
                    "Sorry. I just don't care what you want.":
                            if ApprovalCheck("Mystique", 1400, "LO"): 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                                    ch_m "That's so. . ." 
                                    call MystiqueFace("sly", 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 20)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 15)
                                    ch_m ". . .{i}mean!{/i}" 
                            else:
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -10)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                                    call MystiqueFace("angry", 1)
                                    ch_m "!!!"
                                    $ Line = "rude"

                    "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 10)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 10)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)
                            ch_m "Oh, okay.  Just. . .try not to be so mean about it, Okay?" 

        "Not me.  It's kind of creepy.":
                    call MystiqueFace("sad", 2)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, -20)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -25)
                    ch_m "Oh.  Uhm. . .never mind, then."
                    $ Line = "embarrassed"
    
    $ newgirl["Mystique"].History.append("master")
    if Line == "rude":
            $ newgirl["Mystique"].RecentActions.append("angry")
            hide Mystique_Sprite with easeoutbottom                     
            call Remove_Girl("Mystique")
            $ renpy.pop_call()
            "Mystique runs through the door in a huff.  She might have been crying."
    elif Line == "embarrassed":    
            hide Mystique_Sprite with easeoutbottom                     
            call Remove_Girl("Mystique")
            $ renpy.pop_call()
            "Mystique walks through the door, leaving you alone.  She looked really embarrassed."
    elif Line != "fail":
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 50)
            $ newgirl["Mystique"].Petnames.append("master")
            $ newgirl["Mystique"].Petname = "master"
            ch_m ". . .master."
    return

# end Mystique_Master//////////////////////////////////////////////////////////


# start Mystique_Sexfriend//////////////////////////////////////////////////////////

label Mystique_Sexfriend:   #Mystique_Update   
    $ newgirl["Mystique"].Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Mystique")
    $ newgirl["Mystique"].DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    call MystiqueFace("bemused", 1)
    ch_m "So, [newgirl[Mystique].Petname]. . .you got a second?" #blushing expression
    menu:
            extend ""
            "Not really.":
                call MystiqueFace("angry", 1)
                ch_m "You're such an ass, [Playername]!" #Angry expression.  Loss of points                
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20) 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)           
                $ Line = "rude"

            "This doesn't sound good.":
                call MystiqueFace("perplexed", 1)
                ch_m "I promise.  It's nothing bad." 
                    
            "Yeah.  What's up?":
                pass
                
    if not Line: #all this gets skipped if the "rude" response was procced above
            if ApprovalCheck("Mystique", 850, "L"):                  
                    call MystiqueFace("bemused", 1)
                    ch_m "Well. . . I really like you.  You know that, right?" #Sexy expression.  This is Mystique's "High Like" response
                    menu:
                        extend ""
                        "I was kinda hoping.":
                            call MystiqueFace("sexy", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 10) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5)    
                            ch_m "I was {i}really{/i} hoping you'd say that [newgirl[Mystique].Petname]." #Blushing expression
                
                        "Really?":
                            ch_m "Uhm. . .  yeah.  I really do." #Blushing expression

                        "Ugh.  Gross":
                            call MystiqueFace("angry", 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -5)   
                            ch_m "Y'know, you're such an ass, [Playername]!" #Angry expression.  Big loss of points
                            $ Line = "rude"
                            
            elif ApprovalCheck("Mystique", 1000, "LI"): 
                    call MystiqueFace("sexy", 1)
                    ch_m "I just wanted to tell you. . .I think you're kinda cute." 
                    menu:
                        extend ""
                        "That's really nice of you to say.":
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 5) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5)   
                            ch_m "Well, I really mean it." #Blushing expression

                        "Me?  You really think so?":
                            ch_m "Yeah.  I {i}really{/i} do." #Blushing expression
                
                        "Are you going somewhere with this?":
                            call MystiqueFace("angry")
                            ch_m "Well not anymore, I'm not!" #Angry expression.  Loss of points
                            $ Line = "rude"
                            
            else: #if it reaches this block, it's because it failed the "like" check above.                    
                    $ newgirl["Mystique"].Mouth = "smile"
                    $ newgirl["Mystique"].Brows = "sad"
                    $ newgirl["Mystique"].Eyes = "side"
                    ch_m "This is gonna sound really weird."
                    menu:
                        extend ""
                        "Well, you've got me intrigued.  Now you {i}have{/i} to tell me.":
                            ch_m "Promise you won't think {i}badly{/i}of me?"  #Nervous expression
                            menu:
                                extend ""
                                "Mystique. . . I really like you.  I promise.":
                                    call MystiqueFace("smile")
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 10) 
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5)    
                                    ch_m "Well. . . okay."  #Blushing expression.  Gain of points.

                                "Uhm. . . okay?":
                                    ch_m "Well. .  ." #Nervous expression

                                "No promises.":
                                    call MystiqueFace("perplexed",2)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -5)  
                                    ch_m "Uhm. . . never mind, then."  #Embarrassed expression.  Minor loss of points
                                    $ Line = "embarrassed"

                        "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                            call MystiqueFace("angry",1)
                            ch_m "Fine.  whatever."
                            $ Line = "rude"
                                
    if not Line: #again, if the Line has been changed to "rude" or "embarrassed" then it skips past here.                          
            ch_m "Anyway. . . I was kinda thinking. . . we get along pretty well, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        call MystiqueFace("perplexed",2)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -10)  
                        ch_m "Sorry.  I knew this was a mistake." #Embarrassed expression.  Minor loss of points
                        $ Line = "embarrassed"
                    
    if not Line:                
            ch_m "And we've known each other for a little while, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        call MystiqueFace("perplexed",2)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -10)  
                        ch_m "Sorry.  I knew this was a mistake." 
                        $ Line = "embarrassed"
    if not Line:            
            ch_m "Well. . . I was just kinda thinking. . .  we could take our relationship a little further, if you wanted to."
            menu:
                extend ""
                "You mean. . . like, being {i}friends with benefits{/i}?":
                        ch_m "Yeah.  Whaddya think?" #Blushing expression
                        menu:
                            extend ""
                            "Sounds amazing!  Count me in.":
                                    call MystiqueFace("smile",1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 10) 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 50)             
                                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                                    "Mystique leans in and gives you a gentle kiss on the cheek."
                                    ch_m "I can't wait to get started, [newgirl[Mystique].Petname]."

                            "That may be the sluttiest thing I've ever heard in my life.":
                                    call MystiqueFace("angry",1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -30) 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 10)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -40)  
                                    ch_m "You are the biggest asshole ever, [newgirl[Mystique].Petname]!" #Angry expression.  HUGE loss of points
                                    $ Line = "rude"

                "Uhm, to be honest, I'd rather not.":
                        call MystiqueFace("sadside",2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 15)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -15)  
                        ch_m "Oh.  Okay."  #Sad expression
                        ch_m "I think I should go now.  I've got stuff to do."
                        $ Line = "sad"

    if Line == "rude":    
            call MystiqueFace("angry",1)
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20) 
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -10) 
            hide Mystique_Sprite with easeoutleft   
            $ newgirl["Mystique"].RecentActions.append("angry")
            "Mystique storms off in a huff.  She seemed pretty mad at you."
    elif Line == "embarrassed":
            call MystiqueFace("perplexed",1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, -20)   
            hide Mystique_Sprite with easeoutbottom
            "Mystique walks through the door leaving you alone.  That was very strange."
    elif Line == "sad":    
            hide Mystique_Sprite with easeoutbottom
            "Mystique runs through the door leaving you alone.  You think you may have hurt her feelings."
    else: #if you kept Line unused throughout, then you passed all the checks, so. . .
            $ newgirl["Mystique"].Petnames.append("sex friend")             
            call MystiqueFace("sly",2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10)             
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 10)   
            "Mystique leans in and passes her hand across your body."
            "As she does so, she shoves her hand in your jeans, so her fingers slide along your bare skin."
            $ newgirl["Mystique"].Blush = 1
            ch_m "I'll definitely be seeing {i}you{/i} later, [newgirl[Mystique].Petname]."  
            hide Mystique_Sprite with easeoutright
            "She passes through a nearby door. "            
    call Remove_Girl("Mystique")
    return
    
# end Mystique_Sexfriend//////////////////////////////////////////////////////////


# start Mystique_Fuckbuddy//////////////////////////////////////////////////////////

label Mystique_Fuckbuddy:   #Mystique_Update   
    $ newgirl["Mystique"].DailyActions.append("relationship")
    "Out of nowhere, you feel a hand stroking across your cock."
    "Even though you're fully dressed, it definitely feels like soft skin touching your own."
    "You glance down and see a slender arm snaked around your waist, before vanishing into your pants."
    "As you try to control your rising erection, a voice whispers into your ear,"
    ch_m "Any time, just let me know. . ."
    "-and suddenly the pressure is gone." 
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on Mystique later. . ."
    $ newgirl["Mystique"].Petnames.append("fuck buddy")  
    $ newgirl["Mystique"].Event[10] += 1
    return
# end Mystique_Fuckbuddy//////////////////////////////////////////////////////////

# start Mystique_Daddy//////////////////////////////////////////////////////////

#Not updated

label Mystique_Daddy:       #Mystique_Update   
    $ newgirl["Mystique"].DailyActions.append("relationship")
    call Shift_Focus("Mystique")
    ch_m ". . ."
    if "dating" in newgirl["Mystique"].Traits:
        ch_m "You know, even though we've been dating,"  
    else:    
        ch_m "Even though we've been hanging out," 
    if newgirl["Mystique"].Love > newgirl["Mystique"].Obed and newgirl["Mystique"].Love > newgirl["Mystique"].Inbt:
        ch_m "and you're really sweet to me. . ."
    elif newgirl["Mystique"].Obed > newgirl["Mystique"].Inbt:
        ch_m "and you know what I need. . ."
    else:
        ch_m "and I've really been spreading my wings. . ."        
    ch_m "So I was thinking, could I call you \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
            call MystiqueFace("smile") 
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)          
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 10)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 30) 
            ch_m "Squee!"            
        "What do you mean by that?": 
            call MystiqueFace("bemused") 
            ch_m "I just sort of get turned on by it, you know, being your baby girl. . ."
            ch_m "I'd like to call you that."
            menu:
                extend ""
                "Sounds interesting, fine by me.":     
                    call MystiqueFace("smile") 
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)          
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 20)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 25) 
                    ch_m "Great! . . daddy."  
                "Could you not, please?":             
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 40)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)  
                    call MystiqueFace("sad") 
                    ch_m "   . . .   "
                    ch_m "Well, ok."
                "No, that creeps me out.":    
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)          
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 45)            
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 5)  
                    call MystiqueFace("angry") 
                    ch_m "Hrmph." 
        "No, that creeps me out.":
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)          
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 40)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 10) 
            call MystiqueFace("angry") 
            ch_m "Hrmph."  
    $ newgirl["Mystique"].Petnames.append("daddy")
    return

# end Mystique_Daddy//////////////////////////////////////////////////////////

# Start MystiqueBreakup //////////////////////////////////////////////////////////  
 #Mystique_Update   
label Mystique_Cheated(Other = "Rogue", Resolution = 0, B = 0):  #Other is the other girl, Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
    #Scene for if Mystique catches you with Rogue and confronts you about it. 
    $ newgirl["Mystique"].DailyActions.append("relationship")
    $ Line = 0
    call MystiqueFace("angry")
    
    if Other == "Rogue":
        if newgirl["Mystique"].LikeRogue >= 900:
            $ Resolution += 2
        elif newgirl["Mystique"].LikeRogue >= 800:
            $ Resolution += 1
        $ B = int((newgirl["Mystique"].LikeRogue - 500)/2)
    
    $ Resolution -= newgirl["Mystique"].Cheated if newgirl["Mystique"].Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating
    
    if newgirl["Mystique"].Cheated:
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -50) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -25)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -50)   
    else:
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -120) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -30)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, -20)  
        
    "Mystique stomps up to you and stares you down for a moment."
    ch_m "Well?!" 
    ch_m "Wanna tell me what that was all about?"
    menu:
        extend ""
        "Uhm. . .sorry?":
                ch_m "Is that {i}really{/i} all you have to say for yourself?"
                ch_p "I don't know? It would kinda help if I knew what you were upset about."
                if ApprovalCheck("Mystique", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Line = "angry"
        "I have no idea what you're talking about.":
                ch_m "I can't believe you just said that. I gave you a lot more credit than that."
                ch_p "[newgirl[Mystique].Pet], I'm being serious. Why're you so upset?"
                if ApprovalCheck("Mystique", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Resolution -= 2
                    $ Line = "angry"
        "Could you chill out and tell me what you mean?":
                call MystiqueFace("sad",2)                
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 5, 1) 
                ch_m "I didn't like what happened already. How much worse can it get?"
                ch_p "You'd better start making some sense, or you're gonna find out."
                if ApprovalCheck("Mystique", 500, "O"):
                    $ Resolution += 1  
                elif ApprovalCheck("Mystique", 1200, "LO"):
                    $ Resolution -= 1    
                else:
                    $ Resolution -= 3
                    $ Line = "angry"
                    
    if not Line:
            #this section only triggers if you didn't trigger the "angry" response in the previous section
            call MystiqueFace("angry",2)
            if Other == "Rogue":
                ch_m "I {i}saw{/i} you and Rogue! I can't believe you'd do that, [newgirl[Mystique].Petname]."
            else:
                ch_m "I {i}saw{/i} you with her! I can't believe you'd do that, [newgirl[Mystique].Petname]."
            ch_m "I thought we had something. . .  {i}special{/i} going on."
            menu:
                extend ""
                "I'm sorry. . . ":
                        $ Resolution += 1                        
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5) 
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)  
                        if not ApprovalCheck("Mystique", 900, "L"):
                                #if love is less than 900
                                $ Line = "sad"
                        else:
                                call MystiqueFace("sad")
                                ch_m "Me too. I thought you. . . "
                                call MystiqueFace("sadside")
                                ch_m ". . . I thought you maybe loved me."
                                menu:
                                    extend ""
                                    "You weren't wrong, [newgirl[Mystique].Pet].":
                                            $ Resolution += 1                                            
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 5) 
                                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)   
                                            call MystiqueFace("embarrassed")
                                            ch_m " . . . really?"
                                            menu:
                                                extend ""
                                                " really.":
                                                        call MystiqueFace("embarrassed")
                                                        if Other == "Rogue":
                                                            ch_m "Then. . . why did you do that with {i}Rogue?{/i} You had to know that would hurt me."
                                                        else:
                                                            ch_m "Then. . . why did you do that with {i}her?{/i} You had to know that would hurt me."                                                        
                                                        menu:
                                                            extend ""
                                                            "It was a mistake. And I promise I'll never do it again.":
                                                                    $ Resolution += 2                                                                    
                                                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, 5)
                                                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)   
                                                                    call MystiqueFace("happy",2)
                                                                    ch_m "Okay. I understand. Just. . . remember how much I care about you, Okay?"
                                                                    ch_m "I can forgive you this time."
                                                                    ch_m "Because I'm in love with you, too."
                                                                    call Mystique_Kissing_Launch("kissing")
                                                                    call Mystique_Pos_Reset
                                                            "I was trying to maybe include her in what we have going.":
                                                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                                                    $ Line = "maybe"
                                                            "I don't know, seemed fun at the time.":
                                                                    $ Resolution -= 1
                                                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                                                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, -5)
                                                                    $ Line = "angry"          
                                                "Had you going, there, didn't I? {i}Hell{/i}, no, I don't!":
                                                        $ Resolution -= 3
                                                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20) 
                                                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)   
                                                        $ Line = "angry"                                                                   
                                    "Yeah, well. .  . I don't.":
                                            $ Resolution -= 1
                                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)   
                                            $ Line = "sad"  
                        #end "sorry."
                "Whatever.":
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 5)   
                        if ApprovalCheck("Mystique", 900, "L") and not ApprovalCheck("Mystique", 500, "O"):
                                $ Resolution -= 2
                                $ Line = "angry"
                        else:
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10) 
                                $ Resolution -= 1
                                $ Line = "sad"
                "We do. And now, it can be even {b}more{/b} special.":
                                $ Resolution += 1
                                $ Line = "maybe"
            #end "questioning", for long blocks like this, it helps to put a comment at the end to explain what was going on, so I don't get lost. ;)
            
    if Line == "maybe":
            # Maybe threesome?            
            if ApprovalCheck("Mystique", 1250):
                    call MystiqueFace("confused")
                    ch_m "What're you even {i}talking{/i} about?"
                    if Other == "Rogue":
                        ch_p "Look. . .be totally honest with me for a second. Rogue is your adopted Daughter, right?"
                    else:
                        ch_p "Look. . .be totally honest with me for a second. She's kinda hot, right?"
                    ch_m "Yeah. . ."
                    ch_p "Right. And when you saw us together. . . you have to admit, you thought it was pretty hot on some level, right?"
                    call MystiqueFace("angry")
                    ch_m "No. It pissed me off is what it did."
                    ch_p "C'mon, [newgirl[Mystique].Pet]. Haven't you ever thought about it?"
                    call MystiqueFace("confused")
                    ch_m "Thought about what?"
                    if Other == "Rogue":
                        ch_p "Thought about what it might be like if we invited Rogue into what we have together."
                    else:
                        ch_p "Thought about what it might be like if we invited her into what we have together."                    
                    if ApprovalCheck("Mystique", 1500) and Resolution >= 3:
                            call MystiqueFace("embarrassed")
                            ch_m "You mean . . .a {i}threesome{/i}?"
                            call MystiqueFace("sly")
                            ch_m "I can't believe I'm saying this but. . . I'm vaguely intrigued."
                            if Other == "Rogue":
                                ch_m "Assuming I'm interested. . . how're you going to convince Rogue?"
                            else:
                                ch_m "Assuming I'm interested. . . how're you going to convince her?"
                            ch_p "If you see us together again, just play it cool."
                            ch_p "Make sure she notices that you're watching us, but don't give her the impression it puts you off."
                            call MystiqueFace("sly",1)
                            ch_m ". . . which should make her wonder what's up."
                            ch_p "Right. Eventually, she'll ask me what our arrangement is."
                            ch_m "By then, with any luck, she'll be comfortable enough with me that I can ask her how she feels about it."
                            call MystiqueFace("sly",2)
                            ch_m "Gotta admit, [newgirl[Mystique].Petname]. . . you're pretty smooth."
                            ch_m "Consider me on board with that plan."
                            ch_m "Just be sure to be careful with her. She's still my Daughter."
                            #have Mystique kiss the Player here.
                            ch_m "And remember, you're still {i}my{/i} guy."                            
                            $ newgirl["Mystique"].Traits.append("poly rogue")
                            $ newgirl["Mystique"].Traits.append("ask rogue")
                            $ Line = 0
            if Line:
                    #this section will only trigger if the "maybe" line above triggered BUT both of the stat checks above failed. 
                    #If you don't even ask about a threesome then this check gets skipped, and if you ask, but succeed both checks,
                    #then this section gets skipped. 
                    call MystiqueFace("angry")
                    if Other == "Rogue":
                        ch_m "So, you're telling me you being with Rogue like that was your way of seeing if I'd be up for a threesome?"
                    else:
                        ch_m "So, you're telling me you being with her like that was your way of seeing if I'd be up for a threesome?"
                    ch_p "Pretty much. I. . .take it you're not down with that?"
                    $ Line = "angry"
            # End "maybe threesome?"
    
    elif Resolution >= 4:
        if Other == "Rogue" and newgirl["Mystique"].LikeRogue >= 800:
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 25)   
                ch_m "Well, maybe Rogue and I can work something out. . ."                            
                $ newgirl["Mystique"].Traits.append("poly rogue")
                $ newgirl["Mystique"].Traits.append("ask rogue")                
        
    $ newgirl["Mystique"].Cheated += 1
    if "saw with rogue" in newgirl["Mystique"].Traits: 
            #Clean up the trait for this event
            $ newgirl["Mystique"].Traits.remove("saw with rogue")
            if "poly rogue" not in newgirl["Mystique"].Traits:
                $ newgirl["Mystique"].LikeRogue -= 50
            
    if not Line:
            #a neutral ending if you wrap things up without really effecting much
            pass                
    elif Line == "angry":
            #Angry ending
            call MystiqueFace("angry",2)
            ch_m "You are {b}SUCH{/b} an asshole, [newgirl[Mystique].Petname]!"
            ch_m "I never wanna see you again, as long as I live!"
            "Mystique walkes through the door leaving you standing alone."
            "Whatever you once had is over now, for sure."     
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].Break[0] = 7 + newgirl["Mystique"].Break[1] + newgirl["Mystique"].Cheated
            $ newgirl["Mystique"].Traits.remove("dating")
            $ newgirl["Mystique"].Traits.append("ex")         
    elif Line == "sad":
            # Sad ending
            call MystiqueFace("sad",2)
            "Mystique walks through the door leaving you standing alone."
            "You're pretty sure she was crying as she left."
            "You're also pretty sure you seriously damaged your relationship with her."
            if Resolution <= 3:
                $ newgirl["Mystique"].Break[0] = 5 + newgirl["Mystique"].Break[1] + newgirl["Mystique"].Cheated
                $ newgirl["Mystique"].Traits.remove("dating")
                $ newgirl["Mystique"].Traits.append("ex")                
    return

# end MystiqueBreakup //////////////////////////////////////////////////////////    
