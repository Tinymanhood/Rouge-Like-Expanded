# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

    
##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False, CountWords = 0): #CountWords is just a counter used with the gag

    # Decide if we want to use the one-window or two-window variant.
    
    
    if not two_window:
        # The one window variant. Used for caption boxes
        window:
#            xpos 0.0
#            xanchor 0.0

            pos (0.0,0.1) #(0.3,0.1)
            anchor (0.0,0.0)
            
            style "textbox" 
            
            id "textbox"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what" color "#000000" font "CRIMFBRG.ttf"
            #text what id "what" 
    else:
        # The two window variant. Used for character dialog
        # start gag code
        if who == "Rogue" and R_Gag: 
            $ CountWords = 1
        elif who == "Kitty" and K_Gag: 
            $ CountWords = 1
        elif who == "Emma" and E_Gag: 
            $ CountWords = 1
        elif who in ModdedGirls and newgirl[who].Gag: 
            $ CountWords = 1
        if CountWords == 1:
            $ CountWords = what.count(" ") if what.count(" ") <= 10 else 10
            $ CountWords = CountWords - what.count(".")
            $ what = ""
            python: 
                while CountWords >= 0:
                    CountWords -= 1
                    what = what + renpy.random.choice(["Mrph", 
                                                    "Hrgaph",    
                                                    "Rhgn",                       
                                                    "Phar",                       
                                                    "Geghs",
                                                    "Paha",
                                                    "Grde",
                                                    "Phraph",
                                                    "Ugh"]) 
                    if CountWords:
                        what = what + " "
                    else:
                        what = what + "."
        # End gag code
        
        vbox:
            #Main chat text window
            pos (0.0,0.1) #(0.7,0.1)
            anchor (0.0,0.0)#(1.0,0.0)
            
            style "say_two_window_vbox"
             
            window:   
                style "say_balloon" 

                has vbox:
                    style "say_balloon"                  
                text what id "what" color "#000000" font "CRIMFBRG.ttf" text_align 0.5
              
            if who == "Rogue":
                    if R_SpriteLoc == StageRight or R_SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85                        
                    elif R_SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    else: #R_SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8                        
            elif who == "Kitty": 
                    if K_SpriteLoc == StageRight or K_SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85                        
                    elif K_SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    else: #K_SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8   
            elif who == "Emma": 
                    if E_SpriteLoc == StageRight or E_SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85                        
                    elif E_SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    else: #E_SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8   
            elif who == EmmaName: 
                    if E_SpriteLoc == StageRight or E_SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85                        
                    elif E_SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    else: #E_SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8   
            elif who in ModdedGirls: 
                    if newgirl[who].SpriteLoc == StageRight or newgirl[who].SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85                        
                    elif newgirl[who].SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    else: #E_SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8        
            elif who == Playername:
                    pass
            elif who == "Professor X":                     
                    add "arrow" xalign 0.8 
            elif who:
                    add "arrow" xalign 0.8 
                
        if who:
            # this block is the name tag
            window:         
                    pos (0.1,0.07) #(0.65,0.07)
                    anchor (0.5,0)#(0.5,0.5)
                    style "say_who_window"

                    text who:
                        size 15
                        id "who" 
                        font "CRIMFBRG.ttf" 
         
    # Use the quick menu.
    use quick_menu
    
    
image side arrow = "arrow"

image arrow:
    "images/Arrow.png"
    ypos -17
    xalign 0.5 #0.9  
    zoom 1
    rotate 0
    
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    


    window:
        style "menu_window"
        #xpos 20
        #ypos 0.3
        #yanchor 0

        fixed pos (20,0.43) xysize (310,530):
            viewport:
                yinitial 0
                #scrollbars "vertical"
                arrowkeys True
                mousewheel True
                draggable True
        
                side_yfill True
    
                vbox:
                    style "menu"
                    spacing 2
        
                    for caption, action, chosen in items:
        
                        if action:
                            if " (locked)" in caption:
                                $ caption = caption.replace(" (locked)", "")
                                button:
                                    action None
                                    style "menu_choice_button"
                                    background "#424242"                           
                                    text caption style "menu_choice" color "#6E6E6E"
                                        
        
                                   
                            else:               #to fix, just make this the default of "if action"
                                button:
                                    action action
                                    style "menu_choice_button"
        
                                    text caption style "menu_choice" 
        
                        else:
                            text caption style "menu_caption"
    
        



init -2:
    $ config.narrator_menu = True
    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.30) #* 0.45)
        xmaximum int(config.screen_width * 0.30)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt" color "#000000" size 20
        input id "input" style "input_text" color "#6E6E6E" size 25

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"        
    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start() 
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Disclaimer") action Show("Disclaimer_screen") #ui.callsinnewcontext("Disclaimer_screen_label")        
        textbutton _("Patreon") action OpenURL("http://www.patreon.com/OniArtist")       
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


##############################################################################
# My Bullshit
#
# This is the random crap I've added
# 

#begin Roguebutton
screen roguebutton:
#    if True: #"Rogue" in Party or R_Loc == bg_current:
    imagebutton:
        auto "images/Button_Rogue_%s.png" 
        action ui.callsinnewcontext("RogueWardrobe") 
        xpos 690 
        ypos 5
        focus_mask True
   
#end roguebutton

#begin Statbutton
screen statbutton:
#    if True: #"Rogue" in Party or R_Loc == bg_current:
    imagebutton:
        auto "images/Button_Rogue_%s.png" 
        action ui.callsinnewcontext("RogueStats") #works
#            action ui.callsinnewcontext("R_Wardrobe_screen_label")
        xpos 730 
        ypos 5
        focus_mask True
   
#end statbutton

#begin Statbutton
screen Inventorybutton:
    imagebutton:
        auto "images/UI_Backpack_%s.png" 
        action Show("P_Inventory_screen") 
        xpos 780 
        ypos 5
        focus_mask True
   
#end statbutton

#Begin Status screen:
        
screen R_Status_screen:
    
    default tt = Tooltip(" ")
    
    #Rogue's Stats
    if Ch_Focus == "Rogue":
        add "images/BarBackdrop_R.png"
        frame:  
            style_group "stat_bar" 
            xminimum 130       
            background None
            has vbox     
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [R_Love]")
                bar range 100 value VariableValue("R_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [R_Lust]")
                bar range 100 value VariableValue("R_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 130    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [R_Obed]") #action NullAction("none")?
                bar range 100 value VariableValue("R_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [R_Addict]")
                bar range 100 value VariableValue("R_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [R_Inbt]")
                bar range 100 value VariableValue("R_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [R_Addictionrate]")
                bar range 100 value VariableValue("R_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
        showif not Trigger:
            imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("Shift_Focus", "Kitty") xpos 690 ypos 5 focus_mask True
        showif config.developer:
            imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("RogueStats") xpos 730 ypos 5 focus

        
    #Kitty's stats
    elif Ch_Focus == "Kitty":
        add "images/BarBackdrop_K.png"        
        frame:  
            style_group "stat_bar" 
            xminimum 130       
            background None
            has vbox     
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [K_Love]")
                bar range 100 value VariableValue("K_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [K_Lust]")
                bar range 100 value VariableValue("K_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 130    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [K_Obed]")
                bar range 100 value VariableValue("K_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [K_Addict]")
                bar range 100 value VariableValue("K_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [K_Inbt]")
                bar range 100 value VariableValue("K_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiciton Rate: [K_Addictionrate]")
                bar range 100 value VariableValue("K_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        showif not Trigger:
            imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("Shift_Focus", "Emma") xpos 690 ypos 5 focus_mask True
        showif config.developer:
            imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("KittyStats") xpos 730 ypos 5 focus
    #Emma's Stats
    elif Ch_Focus == "Emma":
        add "images/BarBackdrop_E.png"
        frame:  
            style_group "stat_bar" 
            xminimum 130       
            background None
            has vbox     
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: [E_Love]")
                bar range 100 value VariableValue("E_Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: [E_Lust]")
                bar range 100 value VariableValue("E_Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 130    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: [E_Obed]") #action NullAction("none")?
                bar range 100 value VariableValue("E_Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: [E_Addict]")
                bar range 100 value VariableValue("E_Addict", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: [E_Inbt]")
                bar range 100 value VariableValue("E_Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiction Rate: [E_Addictionrate]")
                bar range 100 value VariableValue("E_Addictionrate", 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
        showif not Trigger:
            imagebutton auto "images/Button_Mystique_%s.png" action ui.callsinnewcontext("Shift_Focus", "Mystique") xpos 690 ypos 5 focus_mask True
        showif config.developer:
            imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("EmmaStats") xpos 730 ypos 5 focus
                            
    elif Ch_Focus == "Mystique":
        add "images/BarBackdrop_M.png"
        frame:  
            style_group "stat_bar" 
            xminimum 130       
            background None
            has vbox     
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: " + str(newgirl["Mystique"].Love))
                bar range 100 value VariableValue2("Love", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: " + str(newgirl["Mystique"].Lust))
                bar range 100 value VariableValue2("Lust", Ch_Focus, 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

        frame:
            xminimum 130
            xpos 130    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: " + str(newgirl["Mystique"].Obed))
                bar range 100 value VariableValue2("Obed", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: " + str(newgirl["Mystique"].Addict))
                bar range 100 value VariableValue2("Addict", Ch_Focus, 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: " + str(newgirl["Mystique"].Inbt))
                bar range 100 value VariableValue2("Inbt", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiciton Rate: " + str(newgirl["Mystique"].Addictionrate))
                bar range 100 value VariableValue2("Addictionrate", Ch_Focus, 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
        showif not Trigger:
            imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("Shift_Focus", "Laura") xpos 690 ypos 5 focus_mask True
        showif config.developer: #nothing here
            imagebutton auto "images/Button_Mystique_%s.png" action ui.callsinnewcontext("EmmaStats") xpos 730 ypos 5 focus

    elif Ch_Focus == "Laura":
        add "images/BarBackdrop_L.png"
        frame:  
            style_group "stat_bar" 
            xminimum 130       
            background None
            has vbox     
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Love: " + str(newgirl["Laura"].Love))
                bar range 100 value VariableValue2("Love", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Lust: " + str(newgirl["Laura"].Lust))
                bar range 100 value VariableValue2("Lust", Ch_Focus, 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

        frame:
            xminimum 130
            xpos 130    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Obedience: " + str(newgirl["Laura"].Obed))
                bar range 100 value VariableValue2("Obed", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Addiction: " + str(newgirl["Laura"].Addict))
                bar range 100 value VariableValue2("Addict", Ch_Focus, 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260    
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Inhibitions: " + str(newgirl["Laura"].Inbt))
                bar range 100 value VariableValue2("Inbt", Ch_Focus, 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Addiciton Rate: " + str(newgirl["Laura"].Addictionrate))
                bar range 100 value VariableValue2("Addictionrate", Ch_Focus, 10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0        
        showif not Trigger:
            imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("Shift_Focus", "Rogue") xpos 690 ypos 5 focus_mask True
        showif config.developer: #nothing here
            imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("EmmaStats") xpos 730 ypos 5 focus
                            
    frame:
        #Focus meter (dick)
        xminimum 130
        xpos 390    
        background None
        has vbox
        hbox:            
            bar range 100 value VariableValue("P_Focus", 100) xmaximum 100 left_bar "images/barfullP.png" right_bar "images/baremptyP.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0 
        hbox:
            bar range 100 value VariableValue("P_Semen", 5) xmaximum 100 left_bar "images/barfullS.png" right_bar "images/baremptyS.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("EmmaStats") xpos 730 ypos 5 focus

    frame:
        # Money and level
        xminimum 75
        xpos 500 
        ypos -5   
        background None
        has vbox
        hbox:            
            text "Money: $[P_Cash]" size 12
        hbox:
            text "Level: [P_Lvl]" size 12 
        if Ch_Focus == 'Emma':
            hbox:
                text "Actions Left: [E_Action]" size 12
            hbox:
                text "Forced: [E_ForcedCount]" size 12
        elif Ch_Focus == 'Kitty':
            hbox:
                text "Actions Left: [K_Action]" size 12
            hbox:
                text "Forced: [K_ForcedCount]" size 12
        elif Ch_Focus == 'Rogue':
            hbox:
                text "Actions Left: [R_Action]" size 12
            hbox:
                text "Forced: [R_ForcedCount]" size 12
        elif Ch_Focus == 'Mystique':
            hbox:
                text "Actions Left: [newgirl[Mystique].Action]" size 12
            hbox:
                text "Forced: [newgirl[Mystique].ForcedCount]" size 12
        elif Ch_Focus == 'Laura':
            hbox:
                text "Actions Left: [newgirl[Laura].Action]" size 12
            hbox:
                text "Forced: [newgirl[Laura].ForcedCount]" size 12
        # this block is the name tag
        window:         
            pos (90,-40)#(-15,-8)
            anchor (0,0)
            style "say_who_window"
            if Ch_Focus == "Mystique":
                text "Raven" size 12 font "CRIMFBRG.ttf" color "#000000" #id "Ch_Focus"  
            elif Ch_Focus == "Laura":
                text newgirl[Ch_Focus].GirlName size 12 font "CRIMFBRG.ttf" color "#000000" #id "Ch_Focus"            
            else:
                text "[Ch_Focus]" size 12 font "CRIMFBRG.ttf" color "#000000" #id "Ch_Focus"            
            
#    frame:
#        xpos 900  
#        ypos 20
#        background None
#        imagebutton idle "CircleTest" hover "CircleTest" action NullAction() hovered tt.Action("Time Left: [Round]%")
        
        
    frame:
        #Clock test.
        xpos 900  
        ypos 20
        background None

        add "images/Clockbase.png":
            anchor (0.5,0.5)
            yzoom -1
            subpixel True

        if Round < 50:
            add "images/Clockred.png" at rotate_red(Round):
                anchor (0.5,0.5)
                subpixel True
        else:
            add "images/Clockwhite.png" at rotate_white(Round):
                anchor (0.5,0.5)
                subpixel True

#        add "images/Clockface.png":
#            anchor (0.5,0.5)
        imagebutton idle "images/Clockface.png" hover "images/Clockface.png" action NullAction() hovered tt.Action("Time Left: [Round]%") anchor (0.5,0.5)
            
    frame:
        # Date and time
        xminimum 130
        xpos 920    
        background None
        has vbox
        hbox:            
            text "Day: [Day] [DayofWeek]" size 12
        hbox:            
            text "Time: [Current_Time]" size 12
    
    if tt.value != " ":
        # Pop-up mouse-over labels
        frame :
            xpos 500 ypos 60
            has vbox:
                text tt.value 

transform rotate_white(x):
    rotate -(int(x *3.6))

transform rotate_red(x):
    rotate -(int(x *3.6-180))

# Bar styling
#init -1 python: 
#    Styling for the bar sliders:
#        style.stat_frame.background = None
#        style.stat_bar.left_bar = "barfull.png"
#        style.stat_bar.right_bar = "barempty.png"
#        style.stat_bar.thumb = None
#        style.stat_slider.xmaximum = 100
#        style.stat_slider.ymaximum = 20 
    
    
#Begin Wardobe screen:

#screen R_Wardrobe_screen:
#    frame:
#        xpos 10
#        ypos 10
#        has hbox
#        textbutton "Toggle Arms" action [ui.callsinnewcontext("RogueWardrobe"),Return()]
# #       textbutton "Toggle Arms" action [ui.callsinnewcontext("Screen_ToggleArms"),Return()] #Works
##            action [Jump(Screen_ToggleArms), SensitiveIf(Rogue_Arms == 1)]
##        text "[R_Love]" size 20

##        showif Rogue_Arms == 2:
##            textbutton "Arms 1" action SetVariable(Rogue_Arms, 1)
##        showif Rogue_Arms == 1:    
##            textbutton "Arms 2" action SetVariable(Rogue_Arms, "2")
#    frame:
#        xpos 10
#        ypos 50
#        has hbox
#        textbutton "Return" action Return()

#label R_Wardrobe_screen_label:
#    call screen R_Wardrobe_screen
#    return

#label Screen_ToggleArms:    
#    if Rogue_Arms == 1:
#        $ Rogue_Arms = 2
#    else:
#        $ Rogue_Arms = 1
#    return
  
#end wardrobe



screen P_Inventory_screen: 
    frame:
        xminimum 200
        xpos 700
        ypos 75
        has vbox
        
#        hbox:    
        text "Inventory:" size 20
        if CheatsEnabled:
            textbutton "Disable Cheats" text_size 15 action [ SetVariable("CheatsEnabled", 0)]
        else:
            textbutton "Enable Cheats" text_size 15 action [ SetVariable("CheatsEnabled", 1)]
        if OniBJ:
            textbutton "Use Mod EmmaBJ" text_size 15 action [ SetVariable("OniBJ", 0)]
        else:
            textbutton "Use ONI EmmaBJ" text_size 15 action [ SetVariable("OniBJ", 1)]
        if CheatsEnabled:
            textbutton "+ $1000" text_size 15 action SetVariable("P_Cash", P_Cash + 1000)
        if P_Lvl < 10 and CheatsEnabled:
            textbutton "Player Max Level" text_size 15 action [ SetVariable("P_Lvl", 10), SetVariable("P_XP", 3330), SetVariable("P_StatPoints", 9) ]
        if R_Lvl < 10 and CheatsEnabled:
            textbutton "Rogue Max Level" text_size 15 action [ SetVariable("R_Lvl", 10), SetVariable("R_XP", 3330), SetVariable("R_StatPoints", 9) ]
        if K_Lvl < 10 and CheatsEnabled:
            textbutton "Kitty Max Level" text_size 15 action [ SetVariable("K_Lvl", 10), SetVariable("K_XP", 3330), SetVariable("K_StatPoints", 9) ]
        if E_Lvl < 10 and CheatsEnabled:
            textbutton "Emma Max Level" text_size 15 action [ SetVariable("E_Lvl", 10), SetVariable("E_XP", 3330), SetVariable("E_StatPoints", 9) ]
        if R_ForcedCount and CheatsEnabled:
            textbutton "Rogue Forced 0" text_size 15 action [ SetVariable("R_ForcedCount", 0)]
        if K_ForcedCount and CheatsEnabled:
            textbutton "Kitty Forced 0" text_size 15 action [ SetVariable("K_ForcedCount", 0)]
        if E_ForcedCount and CheatsEnabled:
            textbutton "Emma Forced 0" text_size 15 action [ SetVariable("E_ForcedCount", 0)]
        if not R_Action and CheatsEnabled:
            textbutton "10 Rogue actions" text_size 15 action [ SetVariable("R_Action", 10)]
        if not K_Action and CheatsEnabled:
            textbutton "10 Kitty actions" text_size 15 action [ SetVariable("K_Action", 10)]
        if not E_Action and CheatsEnabled:
            textbutton "10 Emma actions" text_size 15 action [ SetVariable("E_Action", 10)]
        if not newgirl["Mystique"].Action and CheatsEnabled:
            textbutton "10 Mystique actions" text_size 15 action [ SetField(newgirl["Mystique"], "Action", 10)]
        textbutton "Dick Opacity 0" text_size 15 action [ SetVariable("P_CockVisible", 0)]
        textbutton "Dick Opacity 0_5" text_size 15 action [ SetVariable("P_CockVisible", 0.5)]
        textbutton "Dick Opacity 1" text_size 15 action [ SetVariable("P_CockVisible", 1)]
        if "Xavier's photo" in P_Inventory:
            textbutton "Mystique Picture" text_size 15 action Show("Mystique_Pic",transition=Pause(1))
            if renpy.get_screen("Mystique_Pic"):
                textbutton "Hide Picture" text_size 15 action Hide("Mystique_Pic",transition=Pause(1))
        if R_Rules and CheatsEnabled:
            textbutton "X stop bothering Rogue" text_size 15 action [ SetVariable("R_Rules", 0)]
        if K_Rules and CheatsEnabled:
            textbutton "X stop bothering Kitty" text_size 15 action [ SetVariable("K_Rules", 0)]
        if E_Rules and CheatsEnabled:
            textbutton "X stop bothering Emma" text_size 15 action [ SetVariable("E_Rules", 0)]
        showif "dildo" in P_Inventory:
            $ Inventory_Count = Inventory_Check("dildo")
            text "Dildos: [Inventory_Count]" size 15        
        showif "vibrator" in P_Inventory:
            $ Inventory_Count = Inventory_Check("vibrator")
            text "Vibrators: [Inventory_Count]" size 15
        showif "Dazzler and Longshot" in P_Inventory:
            text "Dazzler and Longshot" size 15
        showif "256 Shades of Grey" in P_Inventory:
            text "256 Shades of Grey" size 15
        showif "Avengers Tower Penthouse" in P_Inventory:
            text "Avengers Tower Penthouse" size 15
        showif "Xavier's photo" in P_Inventory:
            text "Xavier's Photo" size 15    
        showif "lace bra" in P_Inventory:
            text "Lace Bra" size 15          
        showif "lace panties" in P_Inventory:
            text "Lace Panties" size 15    
        showif "nighty" in P_Inventory:
            text "Green Nighty" size 15    
        showif "Mandrill Cologne" in P_Inventory:
            $ Inventory_Count = Inventory_Check("Mandrill Cologne")
            textbutton "Mandrill Cologne: [Inventory_Count] doses" action ui.callsinnewcontext("MandrillScreen") text_size 15
        showif "Purple Rain Cologne" in P_Inventory:
            $ Inventory_Count = Inventory_Check("Purple Rain Cologne")
            textbutton "Purple Rain Cologne: [Inventory_Count] doses" action ui.callsinnewcontext("PurpleRainScreen") text_size 15
        showif "Corruption Cologne" in P_Inventory:
            $ Inventory_Count = Inventory_Check("Corruption Cologne")
            textbutton "Corruption Cologne: [Inventory_Count] doses" action ui.callsinnewcontext("CorruptionScreen") text_size 15
        showif "Xavier" in Keys:
            text "Xavier's Key" size 15    
        showif "Rogue" in Keys:
            text "Rogue's Key" size 15    
        showif "Kitty" in Keys:
            text "Kitty's Key" size 15    
            
        
    imagebutton:
        auto "images/UI_Backpack_%s.png" 
        action Hide("P_Inventory_screen") 
        xpos 780 
        ypos 5
        focus_mask True

   
label MandrillScreen:    
    if "mandrill" in P_Traits:
        "You already have this on."
        return                
    if "purple" in P_Traits or "corruption" in P_Traits:
        "You'll confuse the scent you already have on."
        return
    $ Inventory_Count = Inventory_Check("Mandrill Cologne")
    "This cologne is guaranteed to make women love you more [[+Love]]. You have [Inventory_Count] doses left."
    "Product warning, any love gained while under the effects may be lost when this wears off, if the limits are reached."
    menu:
        "Use it now?"
        "Yes":
            $ P_Traits.append("mandrill")
            $ P_Inventory.remove("Mandrill Cologne")     
        "No":
            pass
             
    return   
   
label PurpleRainScreen:   
    if "purple" in P_Traits:
        "You already have this on."
        return                
    if "mandrill" in P_Traits or "corruption" in P_Traits:
        "You'll confuse the scent you already have on."
        return
    $ Inventory_Count = Inventory_Check("Purple Rain Cologne")
    "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]]. You have [Inventory_Count] doses left."
    "Product warning, any obedience gained whie under the effects may be lost when this wears off, if the limits are reached."
    menu:
        "Use it now?"
        "Yes":
            $ P_Traits.append("purple")
            $ P_Inventory.remove("Purple Rain Cologne") 
        "No":
            pass
    return
    
label CorruptionScreen: 
    if "corruption" in P_Traits:
        "You already have this on."
        return                
    if "purple" in P_Traits or "mandrill" in P_Traits:
        "You'll confuse the scent you already have on."
        return
    $ Inventory_Count = Inventory_Check("Corruption Cologne")
    "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]]. You have [Inventory_Count] doses left."
    "Product warning, any Inhibition lost whie under the effects may be regained when this wears off, if the limits are reached."
    menu:
        "Use it now?"
        "Yes":            
            $ P_Traits.append("corruption")
            $ P_Inventory.remove("Corruption Cologne")                      
        "No":
            pass  
    return                            
#Begin Disclaimer screen:

screen Disclaimer_screen:
    window:
        style "gm_root"
    frame:
        xalign .5
        ypos 100
        xmaximum 800
        has vbox
        text "This is a work of parody fiction. It is intended to be distributed through Hentai United and Oniartist's Patreon page, please do not redistribute through other sources." 
        text " "
        text "As is noted in the game, this story takes place several years after the last episode of the TV series it is based on, and all characters involved are over the age of 18. The game references events of the TV series, but is not beholden to the canon of the series, and characters will behave differently or have different backstories." 
        text " "
        text "I would like to thank Akabur for his help getting started with all this (definitely check out his games too), and the various documentation on the Renpy site for pointing me in the right directions. I've had a lot of fun coding this game, and look forward to continually improving on it. If you'd like to support my efforts, please sign up under my name at Hentai United, or join on to my Patreon page. I have some huge ambitions for where this project will end up." 
        text " "
        text "{a=http://oni.hentaiunited.com/}http://oni.hentaiunited.com{/a}"
        text "{a=http://www.patreon.com/OniArtist}http://www.patreon.com/OniArtist{/a}"

    frame:
        xalign 0.5
        yalign 0.95
        has hbox
        #textbutton "Return" action Return()
        textbutton "Return" action Hide("Disclaimer_screen")

#label Disclaimer_screen_label:    
#    call screen Disclaimer_screen
#    return
#end Disclaimer  

