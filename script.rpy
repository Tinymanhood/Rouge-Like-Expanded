#This is the core game code


image title card = "images/titleimage_new.jpg"
image NightMask = "images/nightmask.png"

image Crossroads_E = "images/Crossroads_Evening.jpg"
image Crossroads_N = "images/Crossroads_Night.jpg"  
image Crossroads_D = "images/Crossroads_Day.jpg"

image UI_Backpack = "images/UI_Backpack_idle.png"
image UI_Dildo = "images/UI_Dildo.png"
image UI_VibA = "images/UI_VibA.png"
image UI_VibB = "images/UI_VibB.png"
image UI_Tongue = "images/UI_Tongue.png"
image UI_Finger = "images/UI_Finger.png"
image UI_Hand = "images/UI_Hand.png"
image UI_GirlFinger = "images/UI_GirlFinger.png" 
image UI_GirlHand = "images/UI_GirlHand.png" 
#image UI_GirlFinger:
#    "images/UI_GirlFinger.png" 
#    zoom .8
#image UI_GirlHand:
#    "images/UI_GirlHand.png" 
#    zoom .8


image blackscreen:
    Solid("#000000")
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

define ch_r = Character('Rogue', color="#85bb65", image = "arrow", show_two_window=True)
define ch_m = Character('[newgirl[Mystique].GirlName]', color="#646dbb", image = "arrow", show_two_window=True)
define ch_p = Character('[Playername]', color="#87CEEB", show_two_window=True)
define ch_x = Character('Professor X', color="#a09400", image = "arrow", show_two_window=True)
define ch_k = Character('Kitty', color="#F5A9D0", image = "arrow", show_two_window=True)
define ch_e = Character('[EmmaName]', color="#98bee7", image = "arrow", show_two_window=True)
define ch_b = Character('Dr. McCoy', color="#1033b2", image = "arrow", show_two_window=True)
define ch_u = Character('???', color="#85bb65", image = "arrow", show_two_window=True)
define ch_usher = Character('Usher', color="#DF0174", show_two_window=True)
#define e = Character("Eileen", what_color="#c8ffc8") #this sets the chat text color, handy

define ch_l = Character('[newgirl[Laura].GirlName]', color="#646dbb", image = "arrow", show_two_window=True)


label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show image "images/Onirating.jpg"
        show text "This title is for ages 18 and up." with dissolve
        with Pause(2)
        
        show text "This is a very rough beta version of the game. It has limited function and has not been thoroughly tested. Please report any bugs you find." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return
    

init -1:  

    #default Mystique = NewGirl("Mystique", 51, "pants")

    #default newgirl = Girlnew("Mystique")
    default ModdedGirls = ["Mystique", "Laura"] #List with all modded girls
    #default ModdedGirls = ["Mystique", "Jean"] #List with all modded girls
    default MystiqueName = "Mystique"
    default LauraName = "Mystique"
    default newgirl = {"Mystique" : Girlnew("Mystique"),    #The LikeOtherGirl attribute should be set for each new girl
                       "Laura" : Girlnew("Laura")
                        }
    
    #default newgirl["Jean"] = Girlnew("Jean")
    #default newgirl.update({"Jean" : Girlnew("Jean")})
    default M_Love = 300
    default M_Obed = 0
    default M_Inbt = 200
    default M_Lust = 10
    default M_Addict = 0
    default M_Addictionrate = 0

    #$ newgirl["Mystique"].Love = 300
    #girlnew.add_othergirls()
    default OniBJ = 0
    default CheatsEnabled = 1
#World Stats
    default SaveVersion = 978
    default Day = 1
    default Cheat = 0
    default Time_Options = ["Morning", "Midday", "Evening", "Night"]
    default Time_Count = 2
    default Current_Time = Time_Options[(Time_Count)]     
    default Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default Weekday = 6
    default DayofWeek = Week[Weekday]
    default bg_current = "bg study"
    default Party = []
    default Taboo = 0
    default Rules = 1
    default R_Rules = 1
    default K_Rules = 1
    default E_Rules = 1
    default Line = 0
    default Situation = 0               #Whether Auto/Shift
    default MultiAction = 1             #0 if the action cannot continue, 1 if it can
    default Trigger = 0                 #Mainhand
    default Trigger2 = 0                #Offhand
    default Trigger3 = 0                #Girl's offhand    
    default Trigger4 = 0                #this is the 4th sexual act performed by the second girl 
    default Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating
    default Adjacent = 0                #this is the girl you're sitting next to in class
    default Present = []                #This list tracks which girls are in this scene
#    default LesFlag = 0                #This is triggered if a lesbian action is occurring
    default Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
    default Events = []  
    default Tempmod = 0
    default Approval = 0                #for approval checks
    default Count = 0                   #For within an event
    default Count2 = 0                  #For between several events
    default Round = 100                 #Tracks time within a turn
    default Stealth = 0                 #How careful you're being
    default Cnt = 0                     #a mini Count variable for discrete operations
    default Speed = 0
    default CountStore = 0              #Stores values for after an event ends
    default Achievements = []
    default Options = []
    default Vibration = 0
    default UI_Tool = 0
    default UI_Girl = "Rogue"           #girl used in UI elements
    default Ch_Focus = "Rogue"
    default TravelMode = 0              #used for wandering around, if 0, you use the worldmap
    default StageFarRight = 900         #these are values for location points on the screen
    default StageRight = 715        
    default StageCenter = 550
    default StageLeft = 350
    default StageFarLeft = 150
#Player Stats
    default Playername = "Zero"
    default P_Male = 1
    default R_Petname = "sugar"       #What Rogue calls the player
    default R_Petnames = ["sugar"]
    default R_Pet = "Rogue"           #What you call Rogue
    default R_Pets = ["Rogue"]
    default K_Petname = "sweetie"       #What Kitty calls the player
    default K_Petnames = ["sweetie"]
    default K_Pet = "Kitty"           #What you call Kitty
    default K_Pets = ["Kitty"]
    default E_Petname = "young man"       #What Emma calls the player
    default E_Petnames = ["young man"]
    default E_Pet = "Ms. Frost"           #What you call Emma
    default E_Pets = ["Ms. Frost"]
    default P_CockVisible = 1
    default P_CockTorso = 0
    default P_Semen = 2
    default P_Semen_Max = 3
    default P_Focus = 0
    default P_FocusX = 0
    default P_XP = 0
    default P_StatPoints = 0    
    default P_XPgoal = 100
    default P_Lvl = 1
    default P_Traits = []
    default P_Rep = 600
    default P_RecentActions = []
    default P_DailyActions = []
# Player Inventory Variables 
    default P_Income = 12               #how much you make each day
    default P_Cash = 20
    default P_Hands = 0
    default P_Inventory = []
    default Inventory_Count = 0
    default Digits = []
    default Keys = [] 
    default PunishmentX = 0
# Player Sprite
    default P_Sprite = 0
    default P_Color = "green"
    default P_Cock = "out"
    default P_Spunk = 0
    default P_Wet = 0
#Rogue Stats   
    default R_Loc = "bg rogue"
    default R_Love = 500
    default R_Inbt = 0
    default R_Obed = 0
    default R_Lust = 10
    default R_LikeKitty = 600
    default R_LikeEmma = 500
    default R_LikeNewGirl = {"Mystique" : 200,
                             "Laura" : 500,
                            }
    default R_Addict = 0                #how addicted she is
    default R_Addictionrate = 0         #How faster her addiciton rises
    default R_AddictStore = 0           #stores her base addiction level
    default R_Resistance = 0            #how fast her rate falls
    default R_OCount = 0                #Orgasm counter
    default R_Loose = 0
    default R_Inventory = []
    default R_XP = 0
    default R_ShameLevel = 0
    default R_Cheated = 0               #number of times you've cheated on her    
    default R_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default R_StatPoints = 0    
    default R_XPgoal = 100
    default R_Lvl = 0
    default R_Traits = []
    default R_Rep = 800
    default R_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
    default R_Shame = 0                 #The amount of shame Rogue generates with her current clothing/action
    default R_Taboo = 0                 #The taboo level of the location Rogue is at when not with you
    default R_Chat = [0,0,0,0,0,0]
    default R_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default R_Todo = []
    default R_PubeC = 0
  # Sexual Encounters
    default R_History = []
    default R_RecentActions = []
    default R_DailyActions = []
    default R_Action = 3
    default R_MaxAction = 3
    default R_Caught = 0
    default R_Kissed = 0              #How many times they've kissed
    default R_Hand = 0
    default R_Foot = 0
    default R_Slap = 0
    default R_Spank = 0
    default R_Strip = 0
    default R_Tit = 0
    default R_Sex = 0
    default R_Anal = 0
    default R_Hotdog = 0
    default R_Mast = 0
    default R_Org = 0
    default R_FondleB = 0
    default R_FondleT = 0
    default R_FondleP = 0
    default R_FondleA = 0
    default R_DildoP = 0
    default R_DildoA = 0
    default R_Vib = 0
    default R_Vibrator = 0
    default R_Plug = 0
    default R_Plugged = 0
    default R_SuckB = 0
    default R_InsertP = 0
    default R_InsertA = 0
    default R_LickP = 0    
    default R_LickA = 0
    default R_Blow = 0
    default R_Swallow = 0
    default R_CreamP = 0
    default R_CreamA = 0
    default R_Les = 0                           #how many times she's done lesbian stuff
    default R_LesWatch = 0
    default R_SexKitty = 0                      #how many times she's had sex involving Kitty
    default R_SEXP = 0
    default R_PlayerFav = 0                     #The player's favorite activity with her
    default R_Favorite = 0                      #her favorite activity
    default R_SeenChest = 0
    default R_SeenPanties = 0
    default R_SeenPussy = 0
    default R_SeenPeen = 0                      #How many times she's seen your cock
    default R_Sleep = 0 
    default R_Personality = "normal"
    default R_Date = 0 
    default R_Forced = 0                        #This is a toggle for if she's being coerced
    default R_ForcedCount = 0                   #This is a counter for each time she's been coerced lately
#Rogue Sprite Variables
    default R_Outfit = "evo_green"
    default R_OutfitDay = "evo_green"
    default Rogue_Arms = 1
    default R_Emote = "normal"
#    default R_EmoteDefault = "normal"
    default R_Arms = "gloved"
    default R_Legs = "skirt"
    default R_Over = "mesh top"
    default R_Under = 0
    default R_Chest = "tank"
    default R_BodySuit = 0
    default R_Pierce = 0
    default R_Panties = "black panties"
    default R_Neck = "spiked collar"
    default R_Hose = "stockings"
    default Temp_R_Hose = 0
    default Temp_R_Legs = 0
    default R_Mouth = "normal"
    default R_Brows = "normal"
    default R_Eyes = "normal"
    default R_Hair = "evo"
    default R_Gag = 0    
    default R_Gagx = 0   
    default R_Boots = 0    
    default R_Bondage = 0  
    default R_Glasses = 0    
    default R_Headband = 0    
    default R_Accessory = 0    
    default R_Blush = 0
    default R_Spunk = []
    default R_Sperm = []
    default R_Pubes = 1
    default R_Nudes = 1
    default R_SelfieOverlay = 0
    default R_Tan = 0
    default R_LegsUp = 0
    default R_Wet = 0
    default R_Water = 0
    default R_Upskirt = 0
    default R_BodySuitOff = 0
    default R_PantiesDown = 0
    default R_Uptop = 0
    default R_Held = 0
    default R_Custom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    default R_Custom4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    default R_Custom5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    default R_Custom6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    default R_Custom7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    default R_Gym = [2,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0,0,0,0,0,0,0]
    default R_Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,0,0,0,0,0,0]
    default R_Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
    default R_SpriteVer = 0
    default RogueLayer = 50
    default R_SpriteLoc = StageRight                        #Sets Rogue to default to the right side  
#Kitty Stats   
    default K_Loc = "bg kitty"
    default K_Love = 400
    default K_Obed = 100
    default K_Inbt = 0
    default K_Lust = 10
    default K_LikeRogue = 700
    default K_LikeEmma = 400
    default K_LikeNewGirl = {"Mystique" : 200,
                             "Laura" : 500,
                            }
    default K_Addict = 0 #how addicted she is
    default K_Addictionrate = 0 #How faster her addiciton rises
    default K_Resistance = 0 #how fast her rate falls
    default K_Inventory = []    
    default K_OCount = 0                #Orgasm counter
    default K_Loose = 0
    default K_XP = 0
    default K_Cheated = 0               #number of times you've cheated on her    
    default K_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default K_StatPoints = 0    
    default K_XPgoal = 100
    default K_Lvl = 0
    default K_Traits = []
    default K_Rep = 800
    default K_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
    default K_Shame = 0                 #The amount of shame Kitty generates with her current clothing/action
    default K_Taboo = 0                 #The taboo level of the location Kitty is at when not with you
    default K_Chat = [0,0,0,0,0,0]
    default K_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default K_Todo = []
    default K_PubeC = 0    
    default K_Like = "Like, "
    default K_like = ", like, "
#Kitty Sprite Variables
    default K_Outfit = "pink outfit"
    default K_OutfitDay = "pink outfit"
    default K_Emote = "normal"
    default K_EmoteDefault = "normal"
    default K_Arms = 0
    default K_Gloves = 0
    default K_Legs = "capris"
    default K_Over = "pink top"
    default K_Under = "pink top"
    default K_Chest = "cami"    
    default K_Pierce = 0
    default K_Panties = "green panties"
    default K_Neck = "gold necklace"
    default K_Hose = 0
    default K_Mouth = "normal"
    default K_Brows = "normal"
    default K_Eyes = "normal"
    default K_Hair = "evo"
    default K_Gag = 0    
    default K_Gagx = 0    
    default K_Blindfold = 0    
    default K_Headband = 0    
    default K_Bondage = 0    
    default K_Blush = 0
    default K_Spunk = []
    default K_Pubes = 1
    default K_Nudes = 1
    default K_Tan = 0
    default K_LegsUp = 0
    default K_HairColor = 0
    default R_HairColor = 0
    default K_Wet = 0
    default K_Water = 0
    default K_Upskirt = 0
    default K_PantiesDown = 0
    default K_Custom = [0,0,0,0,0,0,0,0,0,0]
    default K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
    default K_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]    
    default K_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]    
    default K_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]    
    default K_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]    
    default K_Gym = [2,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
    default K_Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0]
    default K_Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
    default KittyLayer = 100
    default K_SpriteLoc = StageCenter                        #Sets Kitty to default to the center
  # Sexual Encounters
    default K_History = []
    default K_RecentActions = []
    default K_DailyActions = []
    default K_Action = 3
    default K_MaxAction = 3
    default K_Caught = 0
    default K_Kissed = 0              #How many times they've kissed
    default K_Hand = 0
    default K_Foot = 0
    default K_Slap = 0
    default K_Spank = 0
    default K_Strip = 0
    default K_Tit = 0
    default K_Sex = 0
    default K_Anal = 0
    default K_Hotdog = 0
    default K_Mast = 0
    default K_Org = 0
    default K_FondleB = 0
    default K_FondleT = 0
    default K_FondleP = 0
    default K_FondleA = 0
    default K_DildoP = 0
    default K_DildoA = 0
    default K_Vib = 0
    default K_Vibrator = 0
    default K_Plug = 0
    default K_Plugged = 0
    default K_SuckB = 0
    default K_InsertP = 0
    default K_InsertA = 0
    default K_LickP = 0    
    default K_LickA = 0
    default K_Blow = 0
    default K_Swallow = 0
    default K_CreamP = 0
    default K_CreamA = 0
    default K_Les = 0  
    default K_LesWatch = 0  
    default K_SexRogue = 0
    default K_SEXP = 0
    default K_ShameLevel = 0
    default K_PlayerFav = 0                     #The player's favorite activity with her
    default K_Favorite = 0                      #her favorite activity
    default K_SeenChest = 0
    default K_SeenPanties = 0
    default K_SeenPussy = 0   
    default K_SeenPeen = 0
    default K_Sleep = 0
    default K_Personality = "normal"
    default K_Date = 0 
    default K_Forced = 0                                        #This is a toggle for if she's being coerced
    default K_ForcedCount = 0                                   #This is a counter for each time she's been coerced lately
#Emma Stats   
    default EmmaName = "Ms Frost"
    default E_Loc = "bg emma"
    default E_Love = 300
    default E_Obed = 0
    default E_Inbt = 200
    default E_Lust = 10
    default E_LikeRogue = 500
    default E_LikeKitty = 500
    default E_LikeNewGirl = {"Mystique" : 200,
                             "Laura" : 500,
                            }
    default E_Addict = 0 #how addicted she is
    default E_Addictionrate = 0 #How faster her addiciton rises
    default E_Resistance = 0 #how fast her rate falls
    default E_Inventory = []    
    default E_OCount = 0                #Orgasm counter
    default E_Loose = 2
    default E_XP = 0
    default E_Cheated = 0               #number of times you've cheated on her    
    default E_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default E_StatPoints = 0    
    default E_XPgoal = 100
    default E_Lvl = 0
    default E_Traits = []
    default E_Rep = 800
    default E_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
    default E_Shame = 0                 #The amount of shame she generates with her current clothing/action
    default E_Taboo = 0                 #The taboo level of the location she is at when not with you
    default E_Chat = [0,0,0,0,0,0]
    default E_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default E_Todo = []
    default E_PubeC = 0    
#Kitty Sprite Variables
    default E_Outfit = "pink outfit"
    default E_OutfitDay = "teacher"
    default E_Emote = "normal"
    default E_EmoteDefault = "normal"
    default Emma_Arms = 1               #her arm position
    default E_Arms = 0                  #her gloves
    default E_Legs = "pants"
    default E_Over = "jacket"
    default E_Chest = "corset"    
    default E_Pierce = 0
    default E_Panties = "white panties"
    default E_Neck = "choker"
    default E_Hose = 0
    default E_Mouth = "normal"
    default E_Brows = "normal"
    default E_Eyes = "normal"
    default E_Hair = "wavy"
    default E_HairColor = 0
    default E_Gag = 0    
    default E_Gagx = 0    
    default E_Blush = 0
    default E_Spunk = []
    default E_Pubes = 0
    default E_Wet = 0
    default E_LegsUp = 0
    default E_Water = 0
    default E_TitsUp = 1
    default E_Upskirt = 0
    default E_PantiesDown = 0
    default E_Custom = [0,0,0,0,0,0,0,0,0,0]
    default E_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
    default E_Custom4 = [0,0,0,0,0,0,0,0,0,0,0]    
    default E_Custom5 = [0,0,0,0,0,0,0,0,0,0,0]    
    default E_Custom6 = [0,0,0,0,0,0,0,0,0,0,0]    
    default E_Custom7 = [0,0,0,0,0,0,0,0,0,0,0]    
    default E_Gym = [2,0,0,"cape","NewX","corset","white panties",0,0,0,0]
    default E_Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0]
    default E_Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
    default EmmaLayer = 101
    default E_SpriteLoc = StageCenter                        #Sets Emma to default to the center
  # Sexual Encounters
    default E_History = []
    default E_RecentActions = []
    default E_DailyActions = []
    default E_Action = 3
    default E_MaxAction = 4
    default E_Caught = 0
    default E_Kissed = 0              #How many times they've kissed
    default E_Hand = 0
    default E_Foot = 0
    default E_Slap = 0
    default E_Spank = 0
    default E_Strip = 0
    default E_Tit = 0
    default E_Sex = 0
    default E_Anal = 0
    default E_Hotdog = 0
    default E_Mast = 0
    default E_Org = 0
    default E_FondleB = 0
    default E_FondleT = 0
    default E_FondleP = 0
    default E_FondleA = 0
    default E_DildoP = 0
    default E_DildoA = 0
    default E_Vib = 0
    default E_Vibrator = 0
    default E_Plug = 0
    default E_Plugged = 0
    default E_SuckB = 0
    default E_InsertP = 0
    default E_InsertA = 0
    default E_LickP = 0    
    default E_LickA = 0
    default E_Blow = 0
    default E_Swallow = 0
    default E_CreamP = 0
    default E_CreamA = 0
    default E_Les = 0    
    default E_LesWatch = 0
    default E_SexRogue = 0
    default E_SexKitty = 0
    default E_SEXP = 0
    default E_ShameLevel = 0
    default E_PlayerFav = 0                     #The player's favorite activity with her
    default E_Favorite = 0                      #her favorite activity
    default E_SeenChest = 0
    default E_SeenPanties = 0
    default E_SeenPussy = 0   
    default E_SeenPeen = 0
    default E_Sleep = 0
    default E_Personality = "normal"
    default E_Date = 0 
    default E_Forced = 0                                        #This is a toggle for if she's being coerced
    default E_ForcedCount = 0                                   #This is a counter for each time she's been coerced lately    
#Xavier Sprite Variables    
    default X_Brows = "happy"
    default X_Mouth = "happy"
    default X_Eyes = "happy"
    default X_Psychic = 0
    default X_Emote = "happy"
    default XSpriteLoc = StageCenter




label start:       
# Official game start  ////////////////////////////////////////////////////////////////////
    # if not hasattr(renpy.store,'newgirl["Mystique"].Love'):
    #     default newgirl = Girlnew("Mystique")

    $ P_CockVisible = 1
    show screen R_Status_screen    
    show screen Inventorybutton            
        
#     if config.developer:
# #        show screen roguebutton
# #        show screen statbutton
#             # Testing settings
#         $ P_Cash = 200
#         $ Cheat = 1
#         $ R_Kissed = 5
#         $ Digits.append("Rogue") 
#         $ Keys.append("Rogue") 
#         $ K_Kissed = 5      
#         $ Digits.append("Kitty")
#         $ Keys.append("Kitty")
#         $ K_History.append("met")
#         $ E_Kissed = 5      
#         $ E_Petname = "Mr. Zero"
#         $ Digits.append("Emma")
#         $ Keys.append("Emma")
#         $ E_History.append("met")
#         $ E_History.append("classcaught") 
#         $ P_Traits.append("focus")
#         $ R_Event[1] = 1 
#         $ R_Addictionrate = 10
#         #$ R_Resistance = 1 #how fast her rate falls
#         $ Day = 16
#         $ Time_Options = ["Morning", "Midday", "Evening", "Night"]
#         $ Time_Count = 4
#         $ Current_Time = "Midday"   
#         $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#         $ Weekday = 6
#         $ DayofWeek = Week[Weekday]
#         #call Wait
#         #jump Rogue_Room_Test             
        
    jump Prologue


# After loading, this runs ////////////////////////////////////////////////////////////////
label after_load: 
    # if not hasattr(renpy.StoreModule,'newgirl["Mystique"].Love'):
    #     default newgirl = Girlnew("Mystique")
label VersionNumber: 
    $ SaveVersion = 0 if "SaveVersion" not in globals().keys() else SaveVersion    
    # if SaveVersion < 978:
    # if "Jean" not in newgirl.keys():
    #     $ newgirl["Jean"] = Girlnew("Jean")
    if len(R_Custom) < 16:
        while len(R_Custom) < 16:
            $ R_Custom.append(0)
        while len(R_Custom2) < 16:
            $ R_Custom2.append(0)
        while len(R_Custom3) < 16:
            $ R_Custom3.append(0)
        while len(R_Custom3) < 16:
            $ R_Custom4.append(0)
        while len(R_Custom3) < 16:
            $ R_Custom5.append(0)
        while len(R_Custom3) < 16:
            $ R_Custom6.append(0)
        while len(R_Custom3) < 16:
            $ R_Custom7.append(0)
        while len(R_Gym) < 16:
            $ R_Gym.append(0)
        while len(R_Sleepwear) < 16:
            $ R_Sleepwear.append(0)


    if "boy" in newgirl["Laura"].Petnames:
        call Mod_Laura_Values

    if newgirl["Mystique"].XP == (0,):
        $ newgirl["Mystique"].XP = 0

    #Shit I forgot to add into the Girlnew class:
    if getattr(newgirl["Mystique"], "LooksLike", None) == None:
        $ newgirl["Mystique"].LooksLike = "Raven"
    #if getattr(newgirl["Mystique"], "Blindfold", None) == None:
        $ newgirl["Mystique"].Blindfold = 0
        $ newgirl["Mystique"].Headband = 0

    if getattr(newgirl["Mystique"], "Custom4", None) == None:
        $ newgirl["Mystique"].Custom4 = [0,0,0,0,0,0,0,0,0,0,0]
        $ newgirl["Mystique"].Custom5 = [0,0,0,0,0,0,0,0,0,0,0]
        $ newgirl["Mystique"].Custom6 = [0,0,0,0,0,0,0,0,0,0,0]
        $ newgirl["Mystique"].Custom7 = [0,0,0,0,0,0,0,0,0,0,0]

    if "metgym" not in newgirl["Mystique"].History: 
        $ newgirl["Mystique"].LooksLike = "Raven"
        $ newgirl["Mystique"].Gym = [2,0,"workout pants","workout jacket",0,"workout top","black panties",0,0,0,0]  

    if "myyyy man" in newgirl["Mystique"].Petnames:
        $ newgirl["Mystique"].Petnames.append("boy")
        $ newgirl["Mystique"].Petnames.remove("myyyy man")
        $ newgirl["Mystique"].Petname = "boy"
        
    #if not hasattr(newgirl["Mystique"], "LooksLike"):


    if SaveVersion == 975: #error correction, remove this eventually
        $ SaveVersion = 957  
        
    if SaveVersion < 978:
        if SaveVersion < 976:
                if SaveVersion < 94:
                    $ R_Love = R_Love * 10
                    $ R_Inbt = R_Inbt * 10
                    $ R_Obed = R_Obed * 10
                    $ SaveVersion = 940
                    $ R_Under = 0        
                    $ R_OutfitShame[0] = 50
                if SaveVersion < 95:
                    $ R_Event[3] = 0
                    if "hungry" in R_Traits:
                        while "hungry" in R_Traits:
                            $ R_Traits.remove("hungry")  
                        $ R_Traits.append("hungry")
                    $ SaveVersion = 950
                if SaveVersion < 955:
                    if R_Schedule[7] == 4:
                        $ R_Schedule[7] = 0
                    $ R_Schedule[8] = 4     #changes which slot is in gym clothes
                    $ SaveVersion = 955    
                if SaveVersion < 957:
                    $ R_OutfitShame[4] = 20
                    $ SaveVersion = 957    
                if SaveVersion < 960:
                    $ R_Schedule[0] = R_Schedule[1]
                    $ R_Schedule[1] = R_Schedule[2]
                    $ R_Schedule[2] = R_Schedule[3]
                    $ R_Schedule[3] = R_Schedule[4]
                    $ R_Schedule[4] = R_Schedule[5]
                    $ R_Schedule[5] = R_Schedule[6]
                    $ R_Schedule[6] = R_Schedule[7]
                    $ R_Schedule[7] = 0   
                    $ R_Hose = "stockings" if R_Hose == 1 else 0            
                    $ R_Custom[9] = "stockings" if R_Custom[9] == 1 else 0
                    $ R_Sleepwear[6] = "stockings" if R_Sleepwear[6] == 1 else 0    
                    $ TravelMode = 0 if "TravelMode" not in globals().keys() else TravelMode         
                    $ P_RecentActions = [] if "P_RecentActions" not in globals().keys() else P_RecentActions
                    $ P_DailyActions = [] if "P_DailyActions" not in globals().keys() else P_DailyActions         
                    $ R_RecentActions = [] if "R_RecentActions" not in globals().keys() else R_RecentActions
                    $ R_DailyActions = [] if "R_DailyActions" not in globals().keys() else R_DailyActions
                    $ SaveVersion = 960      
                if SaveVersion < 966:
                    $ K_History = []
                    $ K_Arms = Kitty_Arms
                    $ StageFarLeft = 150
                    $ SaveVersion = 966  
                    while len(R_OutfitShame) < 15:
                        $ R_OutfitShame.append(0)  
                if SaveVersion < 970:        
                    hide screen roguebutton
                    hide screen statbutton  
                    $ R_Sperm = []  
                    while len(Event) < 4:
                        $ Event.append(0)
                    while len(R_Chat) < 6:
                        $ R_Chat.append(0)
                    while len(R_Event) < 11:
                        $ R_Event.append(0)
                    while len(R_Custom) < 11:
                        $ R_Custom.append(0)
                    while len(R_Custom2) < 11:
                        $ R_Custom2.append(0)
                    while len(R_Custom3) < 11:
                        $ R_Custom3.append(0)
                    while len(R_Gym) < 11:
                        $ R_Gym.append(0)
                    while len(R_Sleepwear) < 7:
                        $ R_Sleepwear.append(0)
                    while len(R_Schedule) < 10:
                        $ R_Schedule.append(0)
                    while len(K_Custom) < 10:
                        $ K_Custom.append(0)  
                    $ K_Spunk = []            
                    $ K_Custom = [0,0,0,0,0,0,0,0,0,0]
                    $ K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]        
                    $ K_Gym = [0,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ K_Sleepwear = [0,0,0,0,"tank","green panties",0]
                    $ K_Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
                    $ K_Chat = [0,0,0,0,0,0]
                    $ K_Event = [0,0,0,0,0,0,0,0,0,0,0]  
                    $ K_Todo = []
                    $ SaveVersion = 970  
                if SaveVersion < 971:      
                    $ K_Gym = [1,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
                    $ K_Sleepwear = [0,"shorts",0,0,"cami","green panties",0]
                
                    $ R_Gym = [0,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ R_Sleepwear = [0,0,0,0,"tank","green panties",0] 
                    $ R_LikeKitty = 600
                    $ K_Traits = []
                    $ K_Petname = Playername[:1]    
                    $ K_Petnames = ["sweetie"]
                    $ K_Pet = "Kitty"       
                    $ K_Pets = ["Kitty"]
                    $ K_Loose = 0
                    $ K_PantiesDown = 0
                    $ K_Water = 0
                    $ K_Pierce = 0
                    $ K_ForcedCount = 0
                    $ R_ForcedCount = 0
                    $ SaveVersion = 971         
                if SaveVersion < 972:            
                    $ RogueLayer = 50
                    $ KittyLayer = 100
                                
                    if Current_Time == 'Night':
                        show NightMask onlayer nightmask      
                    if K_Over == "pink top":
                        $ K_Neck = "gold necklace"
                    else:
                        $ K_Neck = 0
                    $ R_Spunk = R_Sperm
                    if renpy.showing("setting", layer='master'):
                        scene setting onlayer backdrop
                        hide setting
                    if renpy.showing("bg_entry", layer='master'):
                        scene bg_entry onlayer backdrop
                        hide bg_entry
                    $ SaveVersion = 972 
                if SaveVersion < 973:
                    $ K_Pierce = 0 if "K_Pierce" not in globals().keys() else K_Pierce  
                    $ Trigger4 = 0                #this is the 4th sexual act performed by the second girl  
                    $ Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating 
                    $ Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
                    $ K_Sleepwear[3] = 0
                    
                    if R_Custom[1] == "collargloved":
                            $ R_Custom[1] = "gloved"
                            $ R_Custom[4] = "spiked collar"
                    elif R_Custom[1] == "collarbare":  
                            $ R_Custom[1] = 0
                            $ R_Custom[4] = "spiked collar"
                    elif R_Custom[1] == "gloved":
                            $ R_Custom[1] = "gloved"
                            $ R_Custom[4] = 0
                    else:
                            $ R_Custom[1] = 0
                            $ R_Custom[4] = 0
                            
                    if R_Custom2[1] == "collargloved":
                            $ R_Custom2[1] = "gloved"
                            $ R_Custom2[4] = "spiked collar"
                    elif R_Custom2[1] == "collarbare":  
                            $ R_Custom2[1] = 0
                            $ R_Custom2[4] = "spiked collar"
                    elif R_Custom2[1] == "gloved":
                            $ R_Custom2[1] = "gloved"
                            $ R_Custom2[4] = 0
                    else:
                            $ R_Custom2[1] = 0
                            $ R_Custom2[4] = 0
                    
                    if R_Custom3[1] == "collargloved":
                            $ R_Custom3[1] = "gloved"
                            $ R_Custom3[4] = "spiked collar"
                    elif R_Custom3[1] == "collarbare":  
                            $ R_Custom3[1] = 0
                            $ R_Custom3[4] = "spiked collar"
                    elif R_Custom3[1] == "gloved":
                            $ R_Custom3[1] = "gloved"
                            $ R_Custom3[4] = 0
                    else:
                            $ R_Custom3[1] = 0
                            $ R_Custom3[4] = 0
                            
                    if R_Gym[1] == "collargloved":
                            $ R_Gym[1] = "gloved"
                            $ R_Gym[4] = "spiked collar"
                    elif R_Gym[1] == "collarbare":  
                            $ R_Gym[1] = 0
                            $ R_Gym[4] = "spiked collar"
                    elif R_Gym[1] == "gloved":
                            $ R_Gym[1] = "gloved"
                            $ R_Gym[4] = 0
                    else:
                            $ R_Gym[1] = 0
                            $ R_Gym[4] = 0
                    
                    if R_Sleepwear[0] == "collargloved":
                            $ R_Sleepwear[0] = "gloved"
                            $ R_Sleepwear[3] = "spiked collar"
                    elif R_Sleepwear[0] == "collarbare":  
                            $ R_Sleepwear[0] = 0
                            $ R_Sleepwear[3] = "spiked collar"
                    elif R_Sleepwear[0] == "gloved":
                            $ R_Sleepwear[0] = "gloved"
                            $ R_Sleepwear[3] = 0
                    else:
                            $ R_Sleepwear[0] = 0
                            $ R_Sleepwear[3] = 0
                            
                    if R_Arms == "collargloved":
                            $ R_Arms = "gloved"
                            $ R_Neck = "spiked collar"
                    elif R_Arms == "collarbare":    
                            $ R_Arms = 0
                            $ R_Neck = "spiked collar"
                    elif R_Arms == "gloved":    
                            $ R_Arms = "gloved"
                            $ R_Neck = 0            
                    else:  
                            $ R_Arms = 0
                            $ R_Neck = 0
                    
                    $ P_Rep = 600
                    $ R_Rep = R_Rep * 10
                    $ K_Rep = K_Rep * 10
                    $ R_History = []            
                    $ R_PlayerFav = 0
                    $ R_Favorite = 0
                    $ K_PlayerFav = 0
                    $ K_Favorite = 0   
                    $ R_SeenPeen = 0   
                    $ K_SeenPeen = 0
                    $ R_Les = 0    
                    $ R_SexKitty = 0
                    $ K_Les = 0    
                    $ K_SexRogue = 0
                    $ R_SEXP += 5 if R_LickA else 0
                    $ Trigger = "fondle pussy" if Trigger == "insert pussy" else Trigger
                    $ Trigger2 = "fondle pussy" if Trigger2 == "insert pussy" else Trigger2
                    $ Trigger2 = "jackin" if Trigger2 == "masturbation" else Trigger2
                    $ R_SeenPeen = R_Sex + R_Anal + R_Hotdog + R_Blow + R_Hand + R_Tit    
                    $ K_SeenPeen = K_Sex + K_Anal + K_Hotdog + K_Blow + K_Hand + K_Tit                  
                    if "around" in R_Traits:
                        while "around" in R_Traits:
                            $ R_Traits.remove("around") 
                    if "around" in K_Traits:
                        while "around" in K_Traits:
                            $ K_Traits.remove("around") 
                    $ R_OutfitDay = R_Outfit
                    $ K_OutfitDay = K_Outfit
                    $ SaveVersion = 973 
                if SaveVersion < 974:
                    $ Adjacent = 0    
                    $ R_Resistance = 1 if R_Resistance >= 1 else 0
                    $ K_Resistance = 1 if K_Resistance >= 1 else 0
                    $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    if "All" in Keys and "Kitty" not in Keys:
                        $ Keys.append("Kitty")
                    $ Present = []
                    $ R_Date = 0 
                    $ K_Date = 0 
                    $ SaveVersion = 974 
        if SaveVersion < 976:
            if R_History == 0: 
                $ R_History = []
            if K_History == 0: 
                $ K_History = []
            if "saw with kitty" in R_Traits:
                while "saw with kitty" in R_Traits:
                        $ R_Traits.remove("saw with kitty") 
            if "saw with rogue" in K_Traits:
                while "saw with rogue" in K_Traits:
                        $ K_Traits.remove("saw with rogue") 
            $ R_Gag = 0   
            $ K_Gag = 0  
            $ SaveVersion = 976 
        if SaveVersion < 977:
            if K_Rep <= 400:
                $ P_Rep -= 100
            if R_Rep <= 400:
                $ P_Rep -= 100
            $ SaveVersion = 977 
        if SaveVersion < 978:            
            if "stockings and garterbelt" not in R_Inventory and ApprovalCheck("Rogue", 1500):
                    $ R_Inventory.append("stockings and garterbelt")
            $ E_Loose = 2
            $ SaveVersion = 978
    $ StageFarRight = 900            #these are values for location points on the screen
    $ StageRight = 715            #these are values for location points on the screen
    $ StageCenter = 550
    $ StageLeft = 350
    $ StageFarLeft = 150
    #make sure to set K_SpriteLoc etc. to new values, 
    # $ K_SpriteLoc = 200 if K_SpriteLoc = 550 else K_SpriteLoc
    # if "exhibitionist" in E_Traits:
    #     $ E_Traits.remove("exhibitionist")
    if len(R_Sleepwear) <= 9: #this should be the case on any busted-ass og versions
        $ R_Sleepwear.append(0)
        $ R_Sleepwear.append(0)
        $ R_Sleepwear.append(0)
        $ R_Sleepwear[9] = R_Sleepwear[6] #Hose 6>9
        $ R_Sleepwear[8] = "evo"            #Hair
        $ R_Sleepwear[6] = R_Sleepwear[5] #Panties 5>6
        $ R_Sleepwear[5] = R_Sleepwear[4] #Chest 4>5
        $ R_Sleepwear[4] = R_Sleepwear[3] #Neck 3>4 "choker"  
        $ R_Sleepwear[3] = R_Sleepwear[2] #Over 2>3
        $ R_Sleepwear[2] = R_Sleepwear[1] #Legs 1>2
        $ R_Sleepwear[1] = R_Sleepwear[0] #Arms 0>1
        $ R_Sleepwear[0] = 1                #new toggle
        
        $ K_Sleepwear.append(0)
        $ K_Sleepwear.append(0)
        $ K_Sleepwear.append(0)
        $ K_Sleepwear[9] = K_Sleepwear[6] #Hose 6>9
        $ K_Sleepwear[8] = "long"           #Hair
        $ K_Sleepwear[6] = K_Sleepwear[5] #Panties 5>6
        $ K_Sleepwear[5] = K_Sleepwear[4] #Chest 4>5
        $ K_Sleepwear[4] = K_Sleepwear[3] #Neck 3>4 "choker"  
        $ K_Sleepwear[3] = K_Sleepwear[2] #Over 2>3
        $ K_Sleepwear[2] = K_Sleepwear[1] #Legs 1>2
        $ K_Sleepwear[1] = K_Sleepwear[0] #Arms 0>1
        $ K_Sleepwear[0] = 1                #new toggle
        
        $ E_Sleepwear.append(0)
        $ E_Sleepwear.append(0)
        $ E_Sleepwear.append(0)
        $ E_Sleepwear[9] = E_Sleepwear[6] #Hose 6>9
        $ E_Sleepwear[8] = E_Hair          #Hair
        $ E_Sleepwear[6] = E_Sleepwear[5] #Panties 5>6
        $ E_Sleepwear[5] = E_Sleepwear[4] #Chest 4>5
        $ E_Sleepwear[4] = E_Sleepwear[3] #Neck 3>4 "choker"  
        $ E_Sleepwear[3] = E_Sleepwear[2] #Over 2>3
        $ E_Sleepwear[2] = E_Sleepwear[1] #Legs 1>2
        $ E_Sleepwear[1] = E_Sleepwear[0] #Arms 0>1
        $ E_Sleepwear[0] = 1                #new toggle
#            #end of sleepwear overhaul
            
#        call Failsafe
    return


# Event calls ////////////////////////////////////////////////////////////////////
label EventCalls:
        call Present_Check from _call_Present_Check           
        $ D20 = renpy.random.randint(1, 20)  
        #Disables events when it's too early in the game or the turn is about to end        
        if Day < 5 or Round < 10:
                    return
                
        #Activate's "Rogue like spunk" chat
        if "hungry" not in R_Traits and (R_Swallow + R_Chat[2]) >= 10 and R_Loc == bg_current:      #She's swallowed a lot
                    call Set_The_Scene from _call_Set_The_Scene            
                    call Rogue_Hungry from _call_Rogue_Hungry
                    return   
        
        #Activate's "Kitty like spunk" chat
        if "hungry" not in K_Traits and (K_Swallow + K_Chat[2]) >= 10 and K_Loc == bg_current:      #She's swallowed a lot
                    call Set_The_Scene from _call_Set_The_Scene_1            
                    call Kitty_Hungry from _call_Kitty_Hungry
                    return   
                    
        #Activates Kitty meet    
        if "traveling" in P_RecentActions and "met" not in K_History and bg_current == "bg classroom": 
                    jump KittyMeet
                    return

        #Activates Laura meet    
        if "traveling" in P_RecentActions and "met" not in newgirl["Laura"].History and bg_current == "bg dangerroom":
                if Day >= 5:
                    call LauraMeet
                    return  

        if "traveling" in P_RecentActions and bg_current == "bg classroom" and Weekday < 5:
            if "met" not in E_History:     
                    jump EmmaMeet
                    return   
            elif Current_Time == "Morning":
                if "met" not in newgirl["Mystique"].History:
                    jump MystiqueMeet
                    return  
            elif Current_Time == "Morning":
                if "met" in newgirl["Mystique"].History and newgirl["Mystique"].Loc == "bg classroom":
                    jump MystiqueMedLabStart
                    return 
            elif Current_Time == "Evening" and not Party:
                if "classcaught" not in E_History:     
                    jump Emma_Caught_Classroom
                    return     
                elif D20 <= 10:  
                    if E_Lust >= 50:
                            jump Emma_Caught_Classroom
                            return   
                    else:
                        $ E_Loc = "bg classroom"
        elif bg_current == "bg classroom" and Current_Time == "Evening" and Weekday < 5 and Round >= 70:
                #if you are in class and not travelling. . .
                if "met" in E_History:    
                        $ E_Loc = "bg classroom"

        if "traveling" in P_RecentActions and bg_current == "bg dangerroom" and Weekday < 5 and Current_Time == "Evening" and E_Loc == "bg dangerroom":
            if "metgym" not in E_History:     
                    jump EmmaMeetGym
                    return   
            #elif Current_Time == "Evening" and not Party:
            #    if "classcaught" not in E_History:     
            #        jump Emma_Caught_Classroom
            #        return     
            #    elif D20 <= 10:  
            #        if E_Lust >= 50:
            #                jump Emma_Caught_Classroom
            #                return   
            #        else:
            #            $ E_Loc = "bg classroom"
        if "traveling" in P_RecentActions and bg_current == "bg dangerroom" and Weekday < 5 and Current_Time == "Night" and newgirl["Mystique"].Loc == "bg dangerroom":
            if "metgym" not in newgirl["Mystique"].History:     
                    jump MystiqueMeetGym
                    return   
            
        if "detention" in P_Traits and bg_current == "bg classroom" and Weekday < 5 and Current_Time == "Evening" and not Party:    
                    jump Emma_Detention
                    return     
                    
        #activates if you haven't done an addiciton event today    
        if "addiction" not in R_DailyActions and R_Action >= 1:
                #Activates if she needs her fix
                if R_Resistance and R_Addict >= 60 and not R_Event[3]:
                            if (bg_current == "bg rogue" or bg_current == "bg player") and R_Loc == bg_current:
                                jump Rogue_Fix
                            elif bg_current == "bg player":
                                "Rogue pops into the room, looking a little jumpy."
                                jump Rogue_Fix
                            else:
                                call RogueFace("manic", 1) from _call_RogueFace
                                if "asked meet" in R_RecentActions:
                                    pass
                                elif "asked meet" in R_DailyActions and R_Addict >= 80:
                                    "Rogue texts you. . ."
                                    ch_r "I know I asked to meet you in your room earlier, but I'm serious, this is important."
                                    $ R_RecentActions.append("asked meet")  
                                    return
                                else:
                                    "Rogue texts and asks if you could meet her in your room later."
                                    $ R_RecentActions.append("asked meet")
                                    $ R_DailyActions.append("asked meet")  
                                    return
                #Activates if you don't need a fix but already have resistance                    
                elif R_Resistance:
                    pass
                    
                #These are the "first time addict" event chains
                elif R_Addict >= 35 and not R_Event[1]: #"I'm addicted" event
                    jump Rogue_Addicted            
                elif R_Addict >= 60 and not R_Event[2]: #"I'm super-addicted" event
                    jump Rogue_Addicted2        
                elif R_Addict >= 90:                    #"I'm crazy-addicted" event
                    jump Rogue_Addicted3               
            
        #Activates if she hasn't given you a key yet
        if not R_Event[0] and R_Sleep >= 5:               
                    if R_Loc == bg_current or "Rogue" in Party:
                        call Rogue_Key from _call_Rogue_Key
                        return  
                
        #Activates if Rogue or Kitty caught you cheating
        if "saw with kitty" in R_Traits and "dating" in R_Traits:  
                    if bg_current == "bg rogue" or bg_current == "bg player":
                        call Rogue_Cheated("Kitty") from _call_Rogue_Cheated        
                        return
                    else:
                        call AskedMeet("Rogue","angry") from _call_AskedMeet    
                    
        elif "saw with rogue" in K_Traits and "dating" in K_Traits:  
                    if bg_current == "bg kitty" or bg_current == "bg player":
                        call Kitty_Cheated("Rogue") from _call_Kitty_Cheated        
                        return
                    else:
                        call AskedMeet("Kitty","angry") from _call_AskedMeet_1  
        
        #This scene has Rogue ask Kitty if she wants to have a poly relationship with you    
        if "ask kitty" in R_Traits:                                 
                if K_Break[0]:
                        "Rogue sends you a text."
                        ch_r "She said to \"give it a rest?\""
                        ch_r "I guess we can see if she comes around on the idea."
                elif R_Loc != bg_current and K_Loc != bg_current:                 
                        $ R_Traits.remove("ask kitty")
                        if ApprovalCheck("Kitty", 2000, Bonus = int((K_LikeRogue - 500)/2)) or ApprovalCheck("Kitty", 950, "L", Bonus = int((K_LikeRogue - 500)/6)) or K_LikeRogue >= 900:
                                #applies the "dating?" tag to note that she asked Kitty about it and Kitty was ok with it. 
                                $ K_Traits.append("poly rogue")
                                $ K_Traits.append("dating?") 
                        else:                    
                                #If Kitty refuses to share you
                                "Rogue sends you a text."
                                if not ApprovalCheck("Kitty", 2000):
                                        ch_r "I talked to Kitty about sharing you, and she said she wasn't into that sort of thing,"
                                        ch_r "She's just not into you like that."
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -5)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                                else:
                                        ch_r "I talked to Kitty about sharing you, and she said she wasn't into that sort of thing,"
                                        ch_r "She doesn't really like me that much. . ."
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                $ K_Break[0] = 7 #means that she won't be available to ask again for another 7 days
                                return
        
        #Cues a dating event if Rogue is asked by Kitty to join a poly situation
        if "dating?" in R_Traits and "dating" not in R_Traits and "stop asking" not in R_Traits:
                    if bg_current == "bg rogue" or bg_current == "bg player":
                        call Rogue_BF from _call_Rogue_BF        
                        return
                    else:
                        call AskedMeet("Rogue","bemused") from _call_AskedMeet_2  
        #fix duplicate the stuff above to add kitty-centric poly situations.                    
                
        #Rogue relationship stuff        
        if "relationship" not in R_DailyActions: 
                if "boyfriend" not in R_Petnames and R_Love >= 800 and "stop asking" not in R_Traits: # R_Event[5]
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_BF
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_3   
                elif "lover" not in R_Petnames and R_Love >= 950 and K_Event[6] < 15: # R_Event[6]   
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Love
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_4   
                elif "sir" not in R_Petnames and R_Obed >= 500: # R_Event[7]
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Sub
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_5
                elif "master" not in R_Petnames and R_Obed >= 900 and R_Event[8] <2: # R_Event[8]
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Slave
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_6
                elif "daddy" not in R_Petnames and ApprovalCheck("Rogue", 750, "L") and ApprovalCheck("Rogue", 500, "O") and ApprovalCheck("Rogue", 500, "I"): # R_Event[5]
                        if bg_current == "bg rogue" or bg_current == "bg player" and R_Loc == bg_current:
                            call Rogue_Daddy from _call_Rogue_Daddy
                            return
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_7
                elif "sex friend" not in R_Petnames and R_Inbt >= 500: # R_Event[9]  Fix this one
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Sexfriend
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_8
                elif "fuck buddy" not in R_Petnames and R_Inbt >= 900: # R_Event[10]  Fix this one
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Fuckbuddy
                        else:
                            call AskedMeet("Rogue","bemused") from _call_AskedMeet_9
        #end Rogue relationship stuff
                
        #Kitty relationship stuff, not finished
        elif "relationship" not in K_DailyActions: 
                if "boyfriend" not in K_Petnames and K_Love >= 800: # K_Event[5]
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_BF from _call_Kitty_BF
                            return
                        else:
                            call AskedMeet("Kitty","bemused") from _call_AskedMeet_10 
                elif "lover" not in K_Petnames and K_Love >= 950: # K_Event[6]   
                        if K_Event[6] == 20:
                            pass
                        else:
                            call Kitty_Love from _call_Kitty_Love
                            return
                elif "sir" not in K_Petnames and K_Obed >= 500 and "sir" not in K_History: # K_Event[7]
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Sub from _call_Kitty_Sub
                            return 
                        else:
                            call AskedMeet("Kitty","bemused") from _call_AskedMeet_11
                elif "master" not in K_Petnames and K_Obed >= 800 and "sir" in K_Petnames and "master" not in K_History: # K_Event[8]
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Master from _call_Kitty_Master
                            return 
                        else:
                            call AskedMeet("Kitty","bemused") from _call_AskedMeet_12
#                elif "daddy" not in K_Petnames and ApprovalCheck("Kitty", 750, "L") and ApprovalCheck("Kitty", 500, "O") and ApprovalCheck("Kitty", 500, "I"): # K_Event[5]
#                        if bg_current == "bg kitty" or bg_current == "bg player" and K_Loc == bg_current:
#                            call Kitty_Daddy
                            return 
#                        else:
#                            call AskedMeet("Kitty","bemused")
                elif "sex friend" not in K_Petnames and K_Inbt >= 500: # K_Event[9]  Fix this one
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Sexfriend from _call_Kitty_Sexfriend
                            return 
                        else:
                            call AskedMeet("Kitty","bemused") from _call_AskedMeet_13
                           
                elif "fuck buddy" not in K_Petnames and K_Inbt >= 800 and bg_current != K_Loc: # K_Event[10]  Fix this one
                        #if she's not a fuckbuddy yet, and is not around at the time
                        call Kitty_Fuckbuddy from _call_Kitty_Fuckbuddy
                        return  
        #End Kitty relationsip stuff

        
        #Emma relationship stuff, not finished
        # if "relationship" not in E_DailyActions and "angry" not in E_DailyActions: 
        #         if "stoodup" in E_Traits: #you stood her up
        #                     call Emma_Date_Stood_Up
        #                     return                    
        #         if "boyfriend" not in E_Petnames and E_Love >= 800 and E_Event[5] != 20 and "EmmaNo" not in P_Traits: # E_Event[5]
        #                 if P_Harem and "EmmaYes" not in P_Traits:
        #                     call Poly_Start("Emma")    
        #                     return
        #                 elif bg_current == "bg emma" or bg_current == "bg player":
        #                     call Emma_BF
        #                     return
        #                 else:
        #                     call AskedMeet("Emma","bemused") 
        #         elif "lover" not in E_Petnames and E_Love >= 950 and E_Event[6] != 20: # E_Event[6]   
        #                 if bg_current == "bg emma" or bg_current == "bg player":
        #                     call Emma_Love
        #                     return
        #                 else:
        #                     call AskedMeet("Emma","bemused") 
        #         elif "sir" not in E_Petnames and E_Obed >= 500 and "sir" not in E_History: # E_Event[7]
        #                 if bg_current == "bg emma" or bg_current == "bg player":
        #                     call Emma_Sub
        #                     return 
        #                 else:
        #                     call AskedMeet("Emma","bemused")
        #         elif "master" not in E_Petnames and E_Obed >= 800 and "sir" in E_Petnames and "master" not in E_History: # E_Event[8]
        #                 if bg_current == "bg emma" or bg_current == "bg player":
        #                     call Emma_Master
        #                     return 
        #                 else:
        #                     call AskedMeet("Emma","bemused")
        #         elif "daddy" not in E_Petnames and ApprovalCheck("Emma", 750, "L") and ApprovalCheck("Emma", 500, "O") and ApprovalCheck("Emma", 500, "I"): # E_Event[5]
        #                 if bg_current == "bg emma" or bg_current == "bg player" and E_Loc == bg_current:
        #                     call Emma_Daddy
        #                     return 
        #                 else:
        #                     call AskedMeet("Emma","bemused")
        #         elif "sex friend" not in E_Petnames and E_Inbt >= 500: # E_Event[9]  Fix this one
        #                 if bg_current == "bg emma" or bg_current == "bg player":
        #                     call Emma_Sexfriend
        #                     return 
        #                 else:
        #                     call AskedMeet("Emma","bemused")
                           
        #         elif "fuck buddy" not in E_Petnames and E_Inbt >= 800 and bg_current != E_Loc: # E_Event[10]  Fix this one
        #                 #if she's not a fuckbuddy yet, and is not around at the time
        #                 call Emma_Fuckbuddy
        #                 return  
        #End Emma relationsip stuff
                            
#End primary events
        
        
                     
label QuickEvents:                                              
        #These events get checked every screen refresh

        $ del Options[:]
        call Present_Check from _call_Present_Check_1
        #If Rogue is around
        if R_Loc == bg_current:
                if R_Lust >= 90:       
                        $ R_Blush = 1
                        $ R_Wet = 2 
                elif R_Lust >= 60:        
                        $ R_Blush = 1
                        $ R_Wet = 1
                else:
                        $ R_Wet = 0
                        
                #Rogue reacts to getting horny
                if Taboo and R_Lust >= 75:
                        if R_Inbt > 800 or "exhibitionist" in R_Traits:
                                "Rogue gets a sly smile on her face and squirms a bit."
                        elif R_Inbt > 500 and R_Lust < 90:
                                "Rogue looks a bit flushed and uncomfortable."
                        elif bg_current != "bg showerroom":
                                "Rogue gets an embarrassed look on her face and suddenly leaves the room."
                                call Remove_Girl("Rogue") from _call_Remove_Girl
                                call Set_The_Scene from _call_Set_The_Scene_2        
        else:
                #if Rogue is not around
                if R_Loc == "bg showerroom" and "showered" in R_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Rogue_Schedule from _call_Rogue_Schedule
                        call RogueOutfit from _call_RogueOutfit
                        call Girls_Location from _call_Girls_Location
        #End Rogue Quick Events  
        
        if K_Loc == bg_current:
                if K_Lust >= 90:       
                        $ K_Blush = 1
                        $ K_Wet = 2 
                elif K_Lust >= 60:        
                        $ K_Blush = 1
                        $ K_Wet = 1
                else:
                        $ K_Wet = 0
                  
                #Kitty reacts to getting horny      
                if Taboo and K_Lust >= 75:
                    if K_Inbt > 800 or "exhibitionist" in K_Traits:
                            "Kitty gets a sly smile on her face and squirms a bit."
                    elif K_Inbt > 500 and K_Lust < 90:
                            "Kitty looks a bit flushed and uncomfortable."
                    elif bg_current != "bg showerroom":
                            "Kitty gets an embarrassed look on her face and suddenly phases through the floor."
                            call Remove_Girl("Kitty") from _call_Remove_Girl_1
                            call Set_The_Scene from _call_Set_The_Scene_3
        else:
                #if Kitty is not around
                if K_Loc == "bg showerroom" and "showered" in K_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Kitty_Schedule from _call_Kitty_Schedule
                        call KittyOutfit from _call_KittyOutfit
                        call Girls_Location from _call_Girls_Location_1            
        # End Kitty Quick Events
        
        if E_Loc == bg_current:
                if E_Lust >= 90:       
                        $ E_Blush = 1
                        $ E_Wet = 2 
                elif E_Lust >= 60:        
                        $ E_Blush = 1
                        $ E_Wet = 1
                else:
                        $ E_Wet = 0
                  
                #Emma reacts to getting horny      
                if Taboo and E_Lust >= 75:
                    if E_Inbt > 800 or "exhibitionist" in E_Traits:
                            "Emma gets a sly smile on her face and squirms a bit."
                    elif E_Inbt > 500 and E_Lust < 90:
                            "Emma looks a bit flushed and uncomfortable."
                    elif bg_current != "bg showerroom":
                            "Emma gets an embarrassed look on her face and suddenly phases through the floor."
                            call Remove_Girl("Emma") from _call_Remove_Girl_2
                            call Set_The_Scene from _call_Set_The_Scene_4
        else:
                #if Emma is not around
                if E_Loc == "bg showerroom" and "showered" in E_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Emma_Schedule from _call_Emma_Schedule
                        call EmmaOutfit from _call_EmmaOutfit
                        call Girls_Location from _call_Girls_Location_2   
        #end Emma Quick Events

        if newgirl["Mystique"].Loc == bg_current:
                if newgirl["Mystique"].Lust >= 90:       
                        $ newgirl["Mystique"].Blush = 1
                        $ newgirl["Mystique"].Wet = 2 
                elif newgirl["Mystique"].Lust >= 60:        
                        $ newgirl["Mystique"].Blush = 1
                        $ newgirl["Mystique"].Wet = 1
                else:
                        $ newgirl["Mystique"].Wet = 0
                  
                #Mystique reacts to getting horny      
                if Taboo and newgirl["Mystique"].Lust >= 75:
                    if newgirl["Mystique"].Inbt > 800 or "exhibitionist" in newgirl["Mystique"].Traits:
                            "Mystique gets a sly smile on her face and squirms a bit."
                    elif newgirl["Mystique"].Inbt > 500 and newgirl["Mystique"].Lust < 90:
                            "Mystique looks a bit flushed and uncomfortable."
                    elif bg_current != "bg showerroom":
                            "Mystique gets an embarrassed look on her face and suddenly phases through the floor."
                            call Remove_Girl("Mystique") from _call_Remove_Girl_3
                            call Set_The_Scene from _call_Set_The_Scene_5
        else:
                #if Mystique is not around
                if newgirl["Mystique"].Loc == "bg showerroom" and "showered" in newgirl["Mystique"].DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Mystique_Schedule from _call_Mystique_Schedule
                        call MystiqueOutfit from _call_MystiqueOutfit
                        call Girls_Location from _call_Girls_Location_3   
        #end Mystique Quick Events

        return   
#End Quick Events

label AskedMeet(Character = "Rogue", Emotion = "bemused"): # Use AskedMeet("Rogue","angry")
    #This asks the player to meet the chosen character later
    if Character == "Rogue":
            if "asked meet" not in R_DailyActions:
                    call RogueFace(Emotion) from _call_RogueFace_1
                    "Rogue asks if you could meet her in your room later."
                    $ R_DailyActions.append("asked meet") 
    elif Character == "Kitty":
            if "asked meet" not in K_DailyActions:
                    call KittyFace(Emotion) from _call_KittyFace
                    "Kitty asks if you could meet her in your room later."
                    $ K_DailyActions.append("asked meet") 
    return
    
# End Event Calls //////////////////////////////////////////////////////////////    
    
    
    
    
# Rogue's Faces //////////////////////////////////////////////
label RogueFace(Emote = R_Emote, B = R_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state
        if (R_Forced or "angry" in R_RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "angry"   
        elif R_ForcedCount and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                $ Emote = "sad"  
                
        if Emote == "normal":
                $ R_Mouth = "normal"
                $ R_Brows = "normal"
                $ R_Eyes = "normal"
        elif Emote == "angry":
                $ R_Mouth = "sad"
                $ R_Brows = "angry"
                $ R_Eyes = "sexy"
        elif Emote == "bemused":
                $ R_Mouth = "lipbite"
                $ R_Brows = "sad"
                $ R_Eyes = "squint"
        elif Emote == "closed":
                $ R_Mouth = "lipbite"
                $ R_Brows = "sad"
                $ R_Eyes = "closed"  
        elif Emote == "confused":
                $ R_Mouth = "kiss"
                $ R_Brows = "confused"
                $ R_Eyes = "surprised"
        elif Emote == "kiss":
                $ R_Mouth = "kiss"
                $ R_Brows = "normal"
                $ R_Eyes = "closed"
        elif Emote == "tongue":
                $ R_Mouth = "tongue"
                $ R_Brows = "sad"
                $ R_Eyes = "stunned"
        elif Emote == "manic":
                $ R_Mouth = "grimace"
                $ R_Brows = "sad"
                $ R_Eyes = "manic"
                $ R_Blush = 1
        elif Emote == "sad":
                $ R_Mouth = "sad"
                $ R_Brows = "sad"
                $ R_Eyes = "sexy"
        elif Emote == "sadside":
                $ R_Mouth = "sad"
                $ R_Brows = "sad"
                $ R_Eyes = "side"
        elif Emote == "sexy":
                $ R_Mouth = "lipbite"
                $ R_Brows = "normal"
                $ R_Eyes = "sexy"
        elif Emote == "smile":
                $ R_Mouth = "smile"
                $ R_Brows = "normal"
                $ R_Eyes = "normal"
        elif Emote == "sucking":
                $ R_Mouth = "sucking"
                $ R_Brows = "normal"
                $ R_Eyes = "closed"
        elif Emote == "surprised":
                $ R_Mouth = "surprised"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "oh":
                $ R_Mouth = "kiss"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "startled":
                $ R_Mouth = "grimace"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "down":
                $ R_Mouth = "surprised"
                $ R_Brows = "sad"
                $ R_Eyes = "down"  
        elif Emote == "perplexed":
                $ R_Mouth = "sad"
                $ R_Brows = "confused"
                $ R_Eyes = "normal"
        elif Emote == "sly":
                $ R_Mouth = "grimace"
                $ R_Brows = "normal"
                $ R_Eyes = "squint" 
            
        if M:
                $ R_Eyes = "manic"        
        if B > 1:
                $ R_Blush = 2
        elif B:
                $ R_Blush = 1
        else:
                $ R_Blush = 0
                
        if Mouth:
                $ R_Mouth = Mouth
        if Eyes:
                $ R_Eyes = Eyes
        if Brows:
                $ R_Brows = Brows
                
        return

label RogueFaceSpecial(Emote = R_Emote, B = R_Blush, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
        # Emote is the chosen emote, B is the lush state, and M is whether the character is in a  manic state
        if Emote == "normal":
                $ R_Mouth = "normal"
                $ R_Brows = "normal"
                $ R_Eyes = "normal"
        elif Emote == "angry":
                $ R_Mouth = "sad"
                $ R_Brows = "angry"
                $ R_Eyes = "sexy"
        elif Emote == "bemused":
                $ R_Mouth = "lipbite"
                $ R_Brows = "sad"
                $ R_Eyes = "squint"
        elif Emote == "closed":
                $ R_Mouth = "lipbite"
                $ R_Brows = "sad"
                $ R_Eyes = "closed"  
        elif Emote == "confused":
                $ R_Mouth = "kiss"
                $ R_Brows = "confused"
                $ R_Eyes = "surprised"
        elif Emote == "kiss":
                $ R_Mouth = "kiss"
                $ R_Brows = "normal"
                $ R_Eyes = "closed"
        elif Emote == "tongue":
                $ R_Mouth = "tongue"
                $ R_Brows = "sad"
                $ R_Eyes = "stunned"
        elif Emote == "manic":
                $ R_Mouth = "grimace"
                $ R_Brows = "sad"
                $ R_Eyes = "manic"
                $ R_Blush = 1
        elif Emote == "sad":
                $ R_Mouth = "sad"
                $ R_Brows = "sad"
                $ R_Eyes = "sexy"
        elif Emote == "sadside":
                $ R_Mouth = "sad"
                $ R_Brows = "sad"
                $ R_Eyes = "side"
        elif Emote == "sexy":
                $ R_Mouth = "lipbite"
                $ R_Brows = "normal"
                $ R_Eyes = "sexy"
        elif Emote == "smile":
                $ R_Mouth = "smile"
                $ R_Brows = "normal"
                $ R_Eyes = "normal"
        elif Emote == "sucking":
                $ R_Mouth = "sucking"
                $ R_Brows = "normal"
                $ R_Eyes = "closed"
        elif Emote == "surprised":
                $ R_Mouth = "surprised"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "oh":
                $ R_Mouth = "kiss"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "startled":
                $ R_Mouth = "grimace"
                $ R_Brows = "surprised"
                $ R_Eyes = "surprised"
        elif Emote == "down":
                $ R_Mouth = "surprised"
                $ R_Brows = "sad"
                $ R_Eyes = "down"  
        elif Emote == "perplexed":
                $ R_Mouth = "sad"
                $ R_Brows = "confused"
                $ R_Eyes = "normal"
        elif Emote == "sly":
                $ R_Mouth = "grimace"
                $ R_Brows = "normal"
                $ R_Eyes = "squint" 
            
        if M:
                $ R_Eyes = "manic"        
        if B > 1:
                $ R_Blush = 2
        elif B:
                $ R_Blush = 1
        else:
                $ R_Blush = 0
                
        if Mouth:
                $ R_Mouth = Mouth
        if Eyes:
                $ R_Eyes = Eyes
        if Brows:
                $ R_Brows = Brows
                
        return
        

# Rogue's Outfit //////////////////////////////////////////////
label RogueOutfit(R_OutfitTemp = R_Outfit, Spunk = 0, Undressed = 0, Changed = 0):                                                      #add transitions    
        # R_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed
        
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return

        if R_Gag:
            "She removes her gag"
            $ R_Gag = 0
        
        if R_OutfitTemp != R_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1
        if "Rogue" in Party and R_OutfitTemp == R_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ R_OutfitTemp = R_Outfit
        if R_Loc == "bg showerroom" and "Rogue" not in Party and R_OutfitTemp != "nude":
                #Automatically puts her in the towel while in the shower
                $ R_OutfitTemp = "towel" 
        elif R_Loc != "bg showerroom" and R_Loc != "bg pool":
                #Dries her off
                $ R_Water = 0
                
        if R_Spunk:
                #Removes spunk if told to do so. 
                if "painted" not in R_DailyActions or "cleaned" not in R_DailyActions:        
                    $ del R_Spunk[:]  
         
        #Resets "half-dressed" states
        $ R_Upskirt = 0
        $ R_Uptop = 0
        $ R_BodySuitOff = 0
        $ R_PantiesDown = 0
        
        if R_OutfitTemp == "evo_green":
                    if 0 in (R_Legs,R_Over,R_Chest,R_Hose):
                        $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1      
                            
                    $ R_Arms = "gloved"
                    $ R_Legs = "skirt"
                    $ R_Over = "mesh top"
                    $ R_Neck = "spiked collar"        
                    $ R_Chest = "tank"
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Panties = "black panties"
                    $ R_Boots = 0
                    if "stockings and garterbelt" in R_Inventory:
                        $ R_Hose = "stockings and garterbelt"
                    elif ApprovalCheck("Rogue", 300, "I"):                        
                        $ R_Hose = "stockings"
                    else:
                        $ R_Hose = "tights"
                    $ R_Shame = 0
        elif R_OutfitTemp == "evo_pink":
                    if 0 in (R_Legs,R_Over,R_Chest):
                            $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1                        
                        
                    $ R_Neck = 0
                    $ R_Arms = "gloved"
                    $ R_Legs = "pants"
                    $ R_Over = "pink top"
                    $ R_Neck = 0
                    $ R_Chest = "buttoned tank"
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Panties = "black panties"
                    $ R_Boots = 0
                    $ R_Hose = 0
                    $ R_Shame = 0

        elif R_OutfitTemp == "red dress":
                    if not R_Over:
                            $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1   
                    
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = "red dress"
                    $ R_Chest = 0
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Neck = 0
                    $ R_Panties = "black panties"      
                    $ R_Boots = "boots"
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "blue dress":
                    if not R_Over:
                            $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1   
                    
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = "blue dress"
                    $ R_Chest = 0
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Neck = 0
                    $ R_Panties = "black panties"      
                    $ R_Boots = 0
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "red dress pantyless":
                    if not R_Over:
                            $ Undressed = 1
                    
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = "red dress"
                    $ R_Chest = 0
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Neck = 0
                    $ R_Panties = 0      
                    $ R_Boots = "boots"
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "blue dress pantyless":
                    if not R_Over:
                            $ Undressed = 1
                    
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = "blue dress"
                    $ R_Chest = 0
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Neck = 0
                    $ R_Panties = 0      
                    $ R_Boots = 0
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "classic uniform":
                    if not R_BodySuit:
                            $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1   
                    
                    $ R_Neck = 0
                    $ R_Arms = "classic gloves"
                    $ R_Legs = 0
                    $ R_Over = "classic jacket"
                    $ R_Chest = "bra"
                    $ R_BodySuit = "classic uniform"
                    $ R_Headband = "classic headband"
                    $ R_Accessory = "classic belt"
                    $ R_Neck = 0
                    $ R_Panties = "black panties"      
                    $ R_Boots = "classic boots"
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "classic uniform commando":
                    if not R_BodySuit:
                            $ Undressed = 1
                    
                    $ R_Neck = 0
                    $ R_Arms = "classic gloves"
                    $ R_Legs = 0
                    $ R_Over = "classic jacket"
                    $ R_Chest = 0
                    $ R_BodySuit = "classic uniform"
                    $ R_Headband = "classic headband"
                    $ R_Accessory = "classic belt"
                    $ R_Neck = 0
                    $ R_Panties = 0      
                    $ R_Boots = "classic boots"
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "classic uniform damaged":
                    if not R_BodySuit:
                            $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1   
                    
                    $ R_Neck = 0
                    $ R_Arms = "classic gloves"
                    $ R_Legs = 0
                    $ R_Over = "classic jacket"
                    $ R_Chest = "bra"
                    $ R_BodySuit = "classic uniform damaged"
                    $ R_Headband = "classic headband"
                    $ R_Accessory = "classic belt"
                    $ R_Neck = 0
                    $ R_Panties = "black panties"      
                    $ R_Boots = "classic boots"
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "classic uniform damaged commando":
                    if not R_BodySuit:
                            $ Undressed = 1
                    
                    $ R_Neck = 0
                    $ R_Arms = "classic gloves"
                    $ R_Legs = 0
                    $ R_Over = "classic jacket"
                    $ R_Chest = 0
                    $ R_BodySuit = "classic uniform damaged"
                    $ R_Headband = "classic headband"
                    $ R_Accessory = "classic belt"
                    $ R_Neck = 0
                    $ R_Panties = 0      
                    $ R_Boots = "classic boots"
                    $ R_Hose = 0 
                    $ R_Shame = 0

        elif R_OutfitTemp == "swimsuit1":
                    #if 0 in (R_Legs,R_Over,R_Chest):
                    #        $ Undressed = 1
                    if R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1                        
                        
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = 0
                    $ R_Neck = 0
                    $ R_Chest = "swimsuit1"
                    $ R_BodySuit = "swimsuit1"
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Panties = "swimsuit1"
                    $ R_Boots = 0
                    $ R_Hose = 0
                    $ R_Shame = 0

        elif R_OutfitTemp == "swimsuit2":
                    #if 0 in (R_Legs,R_Over,R_Chest):
                    #        $ Undressed = 1
                    if R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1                        
                        
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = 0
                    $ R_Neck = 0
                    $ R_Chest = "swimsuit2"
                    $ R_BodySuit = "swimsuit2"
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Panties = "swimsuit2"
                    $ R_Boots = 0
                    $ R_Hose = 0
                    $ R_Shame = 0

        elif R_OutfitTemp == "nude":
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = 0
                    $ R_Neck = 0
                    $ R_Chest = 0
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Panties = 0        
                    $ R_Boots = 0
                    $ R_Hose = 0
                    $ R_Shame = 50
        elif R_OutfitTemp == "towel":
                    if R_Over == 0:
                        $ Undressed = 2
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Chest = 0
                    $ R_BodySuit = 0
                    $ R_Headband = 0
                    $ R_Accessory = 0
                    $ R_Over = "towel"
                    $ R_Panties = 0        
                    $ R_Boots = 0
                    $ R_Hose = 0        
                    $ R_Shame = 35
        elif R_OutfitTemp == "custom1":
                    if not R_Legs and R_Custom[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom[9]:          
                        $ Undressed = 1
            
                    $ R_Arms = R_Custom[1]
                    $ R_Legs = R_Custom[2]
                    $ R_Over = R_Custom[3]
                    $ R_Neck = R_Custom[4]
                    $ R_Chest = R_Custom[5]
                    $ R_BodySuit = R_Custom[13]
                    $ R_Headband = R_Custom[14]
                    $ R_Accessory = R_Custom[15]
                    $ R_Panties = R_Custom[6]
                    $ R_Boots = R_Custom[7]
                    $ R_Hair = R_Custom[8] if R_Custom[8] else "evo"
                    $ R_Hose = R_Custom[9]        
                    $ R_Shame = R_OutfitShame[3]
        elif R_OutfitTemp == "custom2":
                    if not R_Legs and R_Custom2[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom2[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom2[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom2[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom2[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom2[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom2[1]
                    $ R_Legs = R_Custom2[2]
                    $ R_Over = R_Custom2[3]
                    $ R_Neck = R_Custom2[4] 
                    $ R_Chest = R_Custom2[5]
                    $ R_BodySuit = R_Custom2[13]
                    $ R_Headband = R_Custom2[14]
                    $ R_Accessory = R_Custom2[15]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom2[6]
                    $ R_Boots = R_Custom2[7]
                    $ R_Hair = R_Custom2[8] if R_Custom2[8] else "evo"
                    $ R_Hose = R_Custom2[9]        
                    $ R_Shame = R_OutfitShame[5]
        elif R_OutfitTemp == "custom3":
                    if not R_Legs and R_Custom3[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom3[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom3[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom3[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom3[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom3[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom3[1]
                    $ R_Legs = R_Custom3[2]
                    $ R_Over = R_Custom3[3]
                    $ R_Neck = R_Custom3[4] 
                    $ R_Chest = R_Custom3[5]
                    $ R_BodySuit = R_Custom3[13]
                    $ R_Headband = R_Custom3[14]
                    $ R_Accessory = R_Custom3[15]
                    $ R_Panties = R_Custom3[6]
                    $ R_Boots = R_Custom3[7]
                    $ R_Hair = R_Custom3[8] if R_Custom3[8] else "evo"
                    $ R_Hose = R_Custom3[9]        
                    $ R_Shame = R_OutfitShame[6]
        elif R_OutfitTemp == "custom4":
                    if not R_Legs and R_Custom4[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom4[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom4[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom4[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom4[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom4[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom4[1]
                    $ R_Legs = R_Custom4[2]
                    $ R_Over = R_Custom4[3]
                    $ R_Neck = R_Custom4[4] 
                    $ R_Chest = R_Custom4[5]
                    $ R_BodySuit = R_Custom4[13]
                    $ R_Headband = R_Custom4[14]
                    $ R_Accessory = R_Custom4[15]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom4[6]
                    $ R_Boots = R_Custom4[7]
                    $ R_Hair = R_Custom4[8] if R_Custom4[8] else "evo"
                    $ R_Hose = R_Custom4[9]        
                    $ R_Shame = R_OutfitShame[11]
        elif R_OutfitTemp == "custom5":
                    if not R_Legs and R_Custom5[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom5[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom5[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom5[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom5[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom5[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom5[1]
                    $ R_Legs = R_Custom5[2]
                    $ R_Over = R_Custom5[3]
                    $ R_Neck = R_Custom5[4] 
                    $ R_Chest = R_Custom5[5]
                    $ R_BodySuit = R_Custom5[13]
                    $ R_Headband = R_Custom5[14]
                    $ R_Accessory = R_Custom5[15]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom5[6]
                    $ R_Boots = R_Custom5[7]
                    $ R_Hair = R_Custom5[8] if R_Custom5[8] else "evo"
                    $ R_Hose = R_Custom5[9]        
                    $ R_Shame = R_OutfitShame[12]
        elif R_OutfitTemp == "custom6":
                    if not R_Legs and R_Custom6[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom6[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom6[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom6[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom6[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom6[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom6[1]
                    $ R_Legs = R_Custom6[2]
                    $ R_Over = R_Custom6[3]
                    $ R_Neck = R_Custom6[4] 
                    $ R_Chest = R_Custom6[5]
                    $ R_BodySuit = R_Custom6[13]
                    $ R_Headband = R_Custom6[14]
                    $ R_Accessory = R_Custom6[15]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom6[6]
                    $ R_Boots = R_Custom6[7]
                    $ R_Hair = R_Custom6[8] if R_Custom6[8] else "evo"
                    $ R_Hose = R_Custom6[9]        
                    $ R_Shame = R_OutfitShame[13]
        elif R_OutfitTemp == "custom7":
                    if not R_Legs and R_Custom7[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom7[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Custom7[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom7[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom7[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom7[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom7[1]
                    $ R_Legs = R_Custom7[2]
                    $ R_Over = R_Custom7[3]
                    $ R_Neck = R_Custom7[4] 
                    $ R_Chest = R_Custom7[5]
                    $ R_BodySuit = R_Custom7[13]
                    $ R_Headband = R_Custom7[14]
                    $ R_Accessory = R_Custom7[15]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom7[6]
                    $ R_Boots = R_Custom7[7]
                    $ R_Hair = R_Custom7[8] if R_Custom7[8] else "evo"
                    $ R_Hose = R_Custom7[9]        
                    $ R_Shame = R_OutfitShame[14]
        elif R_OutfitTemp == "sleep":     
                    if not R_Legs and R_Sleepwear[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Sleepwear[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Sleepwear[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Sleepwear[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Sleepwear[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Sleepwear[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Sleepwear[1] #0
                    $ R_Legs = R_Sleepwear[2] #0
                    $ R_Over = R_Sleepwear[3] #0
                    $ R_Neck = R_Sleepwear[4] #0 
                    $ R_Chest = R_Sleepwear[5] #"tank"
                    $ R_BodySuit = R_Sleepwear[13]
                    $ R_Headband = R_Sleepwear[14]
                    $ R_Accessory = R_Sleepwear[15]
                    $ R_Panties = R_Sleepwear[6] #"green panties"
                    $ R_Boots = R_Sleepwear[7] #boots
                    $ R_Hair = R_Sleepwear[8] if R_Sleepwear[8] else "evo"
                    $ R_Hose = R_Sleepwear[9] #0 
                    $ R_Shame = R_OutfitShame[4]
        elif R_OutfitTemp == "gym":
                    if not R_Legs and R_Gym[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Gym[3]:          
                        $ Undressed = 1
                    elif not R_BodySuit and R_Gym[13]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Gym[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Gym[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Gym[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Gym[1]
                    $ R_Legs = R_Gym[2]
                    $ R_Over = R_Gym[3]        
                    $ R_Neck = R_Gym[4]
                    $ R_Chest = R_Gym[5]
                    $ R_BodySuit = R_Gym[13]
                    $ R_Headband = R_Gym[14]
                    $ R_Accessory = R_Gym[15]
                    $ R_Panties = R_Gym[6]
                    $ R_Boots = R_Gym[7]
                    $ R_Hair = R_Gym[8] if R_Gym[8] else "evo"
                    $ R_Hose = R_Gym[9]     
                    $ R_Shame = R_OutfitShame[7]        
                    if R_Inbt <= 300 and not R_Over:   
                        #Puts a hoodie on if she's shy
                        $ R_Over = "hoodie"  
                        $ R_Shame -= 10 if R_Shame >=10 else R_Shame
                
        if R_Panties and R_Panties != "shorts" and "pantyless" in R_DailyActions:       
                # This checks the pantyless state from flirting 
                if R_Legs == "pants" or HoseNum("Rogue") >= 10:
                    $ R_Shame -= 5    
                elif R_Legs:
                    $ R_Shame -= 10  
                elif R_Panties == "green panties":
                    $ R_Shame -= 20  
                elif R_Panties == "lace panties":
                    $ R_Shame -= 25             
                else:
                    $ R_Shame -= 23  
                
                $ R_Panties = 0        
                $ R_Shame = 0 if R_Shame < 0 else R_Shame
                
        if not Changed and R_OutfitTemp == R_Outfit and R_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "Rogue throws on a towel."
                elif Undressed:
                        "Rogue throws her clothes back on."        
        
        $ R_Outfit = R_OutfitTemp
        return
#End Rogue Outfits


#Rogue Add/Remove gloves function //////////////

label Rogue_Schedule(Clothes = 1, Location = 1, LocTemp = R_Loc):
        #Rogue's natural movements
        # If not Clothes, don't bother with her outfit in the schedule
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "Rogue" in Party and Clothes != 2: 
                #if she's in a party, never mind
                return         
        elif LocTemp == bg_current and Current_Time == "morning":
                #she slept over, so just forget this for now  
                if "sleepover" not in R_RecentActions:
                    $ R_RecentActions.append("sleepover")
                    return           
                #the second time this is called, it skips through
                
        $ D20 = renpy.random.randint(1, 20) 
                        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #In the morning, or if ordered to reschedule, pick an outfit for the day. 
                if R_Schedule[Weekday] == 1:
                        $ R_OutfitDay = "evo_green"
                elif R_Schedule[Weekday] == 2:
                        $ R_OutfitDay = "evo_pink"
                elif R_Schedule[Weekday] == 3 and R_Custom[0]:
                        $ R_OutfitDay = "custom1"
                elif R_Schedule[Weekday] == 4:
                        $ R_OutfitDay = "gym"
                elif R_Schedule[Weekday] == 5 and R_Custom2[0]:
                        $ R_OutfitDay = "custom2"
                elif R_Schedule[Weekday] == 6 and R_Custom3[0]:
                        $ R_OutfitDay = "custom3"
                else: 
                        $ Options = ["evo_pink", "evo_green"]
                        $ Options.append("custom1") if R_Custom[0] == 2 else Options
                        $ Options.append("custom2") if R_Custom2[0] == 2 else Options
                        $ Options.append("custom3") if R_Custom3[0] == 2 else Options
                        $ Options.append("custom4") if R_Custom4[0] == 2 else Options
                        $ Options.append("custom5") if R_Custom5[0] == 2 else Options
                        $ Options.append("custom6") if R_Custom6[0] == 2 else Options
                        $ Options.append("custom7") if R_Custom7[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ R_OutfitDay = Options[0]
                        $ del Options[:] 
                $ R_Outfit = R_OutfitDay
        #End clothing portion
        
        
        #Location portion
        if "Rogue" in Party or R_Loc == "hold":
                pass
        elif Weekday == 0 or Weekday == 2:            
        #Fr   
                if Current_Time == "Midday": 
                        $ R_Loc = "bg classroom"
                else:
                        $ R_Loc = "bg rogue"
        elif Weekday == 4:            
        #Fr   
                if Current_Time == "Midday": 
                        $ R_Loc = "bg classroom"
                elif Current_Time == "Evening":
                        $ R_Loc = "bg field"
                else:
                        $ R_Loc = "bg rogue"
        elif Weekday == 1 or Weekday == 3:                          
        #TuThu        
                if Current_Time == "Morning":
                        $ R_Loc = "bg classroom"
                elif Current_Time == "Midday":
                        $ R_Loc = "bg dangerroom"
                else:
                        $ R_Loc = "bg rogue"
        else:                                                       
        #Weekend                               
                if Current_Time == "Morning":
                        $ R_Loc = "bg pool"
                elif Current_Time == "Midday":
                        $ R_Loc = "bg campus"
                elif Current_Time == "Evening":
                        $ R_Loc = "bg field"
                else:
                        $ R_Loc = "bg rogue"
                                                 
        if R_Loc != LocTemp and "Rogue" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ R_RecentActions.append("leaving") 
                elif R_Loc == bg_current: #If she's showed up
                    $ R_RecentActions.append("arriving") 
                    
        return
#End Rogue's Schedule


label Rogue_Todo:
        #Actions checked each night 
        #causes her to grow her pubes out over a week   
        if "pubes" in R_Todo:               
                $ R_PubeC -= 1
                if R_PubeC >= 1:
                        pass
                else:            
                        $ R_Pubes = 1
                        $ R_Todo.remove("pubes")  
                
        #causes her to wax her pubes       
        if "shave" in R_Todo:         
                $ R_Pubes = 0
                $ R_Todo.remove("shave")
             
        #causes her to put in piercings 
        if "ring" in R_Todo:               
                $ R_Pierce = "ring"
                $ R_Todo.remove("ring")
        if "barbell" in R_Todo:
                $ R_Pierce = "barbell"
                $ R_Todo.remove("barbell")

        $ R_Spank = 0
        
        return
           

# Kitty's Outfit //////////////////////////////////////////////
label KittyOutfit(K_OutfitTemp = K_Outfit, Spunk = 0, Undressed = 0, Changed = 0):   
        # K_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return

        if K_Gag:
            "She removes her gag"
            $ K_Gag = 0
        
        if K_Blindfold:
            "She removes the blindfold"
            $ K_Blindfold = 0

        if K_OutfitTemp != K_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Kitty" in Party and K_OutfitTemp == K_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ K_OutfitTemp = K_Outfit
        if K_Loc == "bg showerroom" and "Kitty" not in Party and K_OutfitTemp != "nude":
                #Automatically puts her in the towel while in the shower
                $ K_OutfitTemp = "towel"                                  
        elif K_Loc != "bg showerroom" and K_Loc != "bg pool":
                #Dries her off
                $ K_Water = 0
                
        if K_Spunk:
                if "painted" not in K_DailyActions or "cleaned" not in K_DailyActions:        
                    $ del K_Spunk[:] 
                
        $ K_Upskirt = 0
        $ K_Uptop = 0
        $ K_PantiesDown = 0
        if K_OutfitTemp == "pink outfit":
                    if 0 in (K_Legs,K_Over,K_Chest):
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = 0
                    $ K_Legs = "capris"
                    $ K_Over = "pink top"
                    $ K_Chest = "cami"
                    $ K_Panties = "green panties"        
                    $ K_Neck = "gold necklace"
                    $ K_Hair = "evo"
                    $ K_Hose = 0    
        elif K_OutfitTemp == "red outfit":
                    if 0 in (K_Legs,K_Over,K_Chest):
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = 0
                    $ K_Legs = "black jeans"
                    $ K_Over = "red shirt"
                    $ K_Chest = "bra"
                    $ K_Panties = "green panties"      
                    $ K_Neck = 0
                    $ K_Hair = "evo"
                    $ K_Hose = 0 
        elif K_OutfitTemp == "party outfit":
                    if 0 in (K_Legs,K_Over,K_Chest):
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = "black gloves"
                    $ K_Legs = "black blue pants"
                    $ K_Over = "violet shirt scarfless"
                    $ K_Chest = "bra"
                    $ K_Panties = "green panties"      
                    $ K_Neck = "scarf"
                    $ K_Hair = "evo"
                    $ K_Hose = 0 
        elif K_OutfitTemp == "black dress":
                    if not K_Over:
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Over = "black dress"
                    $ K_Chest = 0
                    $ K_Panties = "green panties"      
                    $ K_Neck = 0
                    $ K_Hair = "long"
                    $ K_Hose = 0 

        elif K_OutfitTemp == "zipper bondage":
                    if not K_Over:
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Over = 0
                    $ K_Chest = "bustier bra"
                    $ K_Panties = "zipper panties"      
                    $ K_Neck = 0
                    $ K_Hair = K_Hair
                    $ K_Hose = 0 

        elif K_OutfitTemp == "zipper bondage open":
                    if not K_Over:
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Over = 0
                    $ K_Chest = "bustier bra open"
                    $ K_Panties = "zipper panties open"      
                    $ K_Neck = 0
                    $ K_Hair = K_Hair
                    $ K_Hose = 0 

        elif K_OutfitTemp == "swimsuit3":
                    if K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1  
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Over = 0
                    $ K_Chest = "swimsuit3"
                    $ K_Panties = "swimsuit3"      
                    $ K_Neck = 0
                    $ K_Hair = "long"
                    $ K_Hose = 0 

        elif K_OutfitTemp == "purple bikini":
                    if not K_Chest:
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Over = 0
                    $ K_Chest = "purple bikini bra"
                    $ K_Panties = "purple bikini panties"      
                    $ K_Neck = 0
                    $ K_Hair = "long"
                    $ K_Hose = 0 

        elif K_OutfitTemp == "kitty lingerie":
                    if 0 in (K_Hose,K_Chest):
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1 
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Over = 0
                    $ K_Chest = "kitty lingerie top"
                    $ K_Panties = "kitty lingerie panties"      
                    $ K_Neck = 0
                    $ K_Hair = "long"
                    $ K_Hose = "kitty lingerie socks" 
                    if K_Headband != "black" and K_Headband != "pink":
                        $ K_Headband = "black"

        elif K_OutfitTemp == "towel":
                    if K_Over == 0:
                            $ Undressed = 2
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Chest = 0
                    $ K_Over = "towel"
                    $ K_Panties = 0        
                    $ K_Hose = 0          
                    $ K_Neck = 0  
                    $ K_Hair = "long"
                    $ K_Shame = 35

        elif K_OutfitTemp == "nude":
                    $ K_Gloves = 0
                    $ K_Legs = 0
                    $ K_Chest = 0
                    $ K_Over = 0
                    $ K_Panties = 0              
                    $ K_Neck = 0
                    $ K_Hose = 0   
                    $ K_Shame = 50
        elif K_OutfitTemp == "custom1":
                    if not K_Legs and K_Custom[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom[6] and "pantyless" not in K_DailyActions:          
                            $ Undressed = 1
                    elif not K_Hose and K_Custom[9]:          
                            $ Undressed = 1
                    
                    $ K_Gloves = K_Custom[1]
                    $ K_Legs = K_Custom[2]
                    $ K_Over = K_Custom[3]    
                    $ K_Neck = K_Custom[4]
                    $ K_Chest = K_Custom[5]
                    $ K_Panties = K_Custom[6]  
                    $ K_Hose = K_Custom[9]                     
                    $ K_Hair = K_Custom[8] if K_Custom[8] else K_Hair 
                    $ K_Shame = K_OutfitShame[3]
        elif K_OutfitTemp == "custom2":
                    if not K_Legs and K_Custom2[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom2[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom2[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom2[6] and "pantyless" not in K_DailyActions:          
                            $ Undressed = 1
                    elif not K_Hose and K_Custom2[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Custom2[1]
                    $ K_Legs = K_Custom2[2]
                    $ K_Over = K_Custom2[3]   
                    $ K_Neck = K_Custom2[4]
                    $ K_Chest = K_Custom2[5]
                    $ K_Panties = K_Custom2[6] 
                    $ K_Hose = K_Custom2[9]                      
                    $ K_Hair = K_Custom2[8] if K_Custom2[8] else K_Hair
                    $ K_Shame = K_OutfitShame[5]
        elif K_OutfitTemp == "custom3":
                    if not K_Legs and K_Custom3[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom3[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom3[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom3[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_Custom3[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Custom3[1]
                    $ K_Legs = K_Custom3[2]
                    $ K_Over = K_Custom3[3]
                    $ K_Neck = K_Custom3[4]
                    $ K_Chest = K_Custom3[5]
                    $ K_Panties = K_Custom3[6]    
                    $ K_Hose = K_Custom3[9]   
                    $ K_Hair = K_Custom3[8] if K_Custom3[8] else K_Hair
                    $ K_Shame = K_OutfitShame[6]
        elif K_OutfitTemp == "custom4":
                    if not K_Legs and K_Custom4[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom4[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom4[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom4[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_Custom4[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Custom4[1]
                    $ K_Legs = K_Custom4[2]
                    $ K_Over = K_Custom4[3]
                    $ K_Neck = K_Custom4[4]
                    $ K_Chest = K_Custom4[5]
                    $ K_Panties = K_Custom4[6]    
                    $ K_Hose = K_Custom4[9]   
                    $ K_Hair = K_Custom4[8] if K_Custom4[8] else K_Hair
                    $ K_Shame = K_OutfitShame[11]
        elif K_OutfitTemp == "custom5":
                    if not K_Legs and K_Custom5[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom5[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom5[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom5[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_Custom5[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Custom5[1]
                    $ K_Legs = K_Custom5[2]
                    $ K_Over = K_Custom5[3]
                    $ K_Neck = K_Custom5[4]
                    $ K_Chest = K_Custom5[5]
                    $ K_Panties = K_Custom5[6]    
                    $ K_Hose = K_Custom5[9]   
                    $ K_Hair = K_Custom5[8] if K_Custom5[8] else K_Hair
                    $ K_Shame = K_OutfitShame[12]
        elif K_OutfitTemp == "custom6":
                    if not K_Legs and K_Custom6[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom6[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom6[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom6[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_Custom6[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Custom6[1]
                    $ K_Legs = K_Custom6[2]
                    $ K_Over = K_Custom6[3]
                    $ K_Neck = K_Custom6[4]
                    $ K_Chest = K_Custom6[5]
                    $ K_Panties = K_Custom6[6]    
                    $ K_Hose = K_Custom6[9]   
                    $ K_Hair = K_Custom6[8] if K_Custom6[8] else K_Hair
                    $ K_Shame = K_OutfitShame[13]
        elif K_OutfitTemp == "custom7":
                    if not K_Legs and K_Custom7[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom7[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom7[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom7[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_Custom7[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Custom7[1]
                    $ K_Legs = K_Custom7[2]
                    $ K_Over = K_Custom7[3]
                    $ K_Neck = K_Custom7[4]
                    $ K_Chest = K_Custom7[5]
                    $ K_Panties = K_Custom7[6]    
                    $ K_Hose = K_Custom7[9]   
                    $ K_Hair = K_Custom7[8] if K_Custom7[8] else K_Hair
                    $ K_Shame = K_OutfitShame[14]
        elif K_OutfitTemp == "sleep":  
                    if not K_Legs and K_Sleepwear[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Sleepwear[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Sleepwear[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Sleepwear[6] and "pantyless" not in K_DailyActions:        
                            $ Undressed = 1
                    elif not K_Hose and K_Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Sleepwear[1] #0
                    $ K_Legs = K_Sleepwear[2] #shorts
                    $ K_Over = K_Sleepwear[3] #0
                    $ K_Neck = K_Sleepwear[4] #0
                    $ K_Chest = K_Sleepwear[5] #"cami"
                    $ K_Panties = K_Sleepwear[6] #"green panties"
                    $ K_Hair = K_Sleepwear[8] if K_Sleepwear[8] else K_Hair
                    $ K_Hose = K_Sleepwear[9] #0  
                    
                    $ K_Hair = "long"
                    $ K_Shame = K_OutfitShame[4]
                    
        elif K_OutfitTemp == "gym":
                    if not K_Legs and K_Gym[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Gym[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Gym[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Gym[6] and "pantyless" not in K_DailyActions:        
                            $ Undressed = 1
                    elif not K_Hose and K_Gym[9]:          
                            $ Undressed = 1
                        
                    $ K_Gloves = K_Gym[1]
                    $ K_Legs = K_Gym[2]
                    $ K_Over = K_Gym[3] 
                    $ K_Neck = K_Gym[4]
                    $ K_Chest = K_Gym[5]
                    $ K_Panties = K_Gym[6]   
                    $ K_Hair = K_Gym[8] if K_Gym[8] else K_Hair 
                    $ K_Hose = K_Gym[9]     
                    $ K_Shame = K_OutfitShame[7]   
                
        if K_Panties and "pantyless" in K_DailyActions:       
                    # This checks the pantyless state from flirting 
                    if K_Legs == "pants" or HoseNum("Kitty") >= 10:
                        $ K_Shame -= 5    
                    elif K_Legs:
                        $ K_Shame -= 10  
                    elif K_Panties == "green panties":
                        $ K_Shame -= 20  
                    elif K_Panties == "lace panties":
                        $ K_Shame -= 25             
                    else:
                        $ K_Shame -= 23  
                    
                    $ K_Panties = 0        
                    $ K_Shame = 0 if K_Shame < 0 else K_Shame
                    
        if not Changed and K_OutfitTemp == K_Outfit and K_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."          

        $ K_Outfit = K_OutfitTemp
        return
#End Kitty's Outfits
      
label Kitty_Schedule(Clothes = 1, Location = 1, LocTemp = K_Loc): 
        #Kitty's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in K_History or ("Kitty" in Party and Clothes != 2): 
            #if she's in a party, never mind
            return   
        if LocTemp == bg_current and Current_Time == "morning":
                #she slept over, so just forget this for now  
                if "sleepover" not in K_RecentActions:
                    $ K_RecentActions.append("sleepover")
                    return           
                #the second time this is called, it skips through    
        
        $ D20 = renpy.random.randint(1, 20) 
        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #Pick clothes for the day
                if K_Schedule[Weekday] == 1: #Tue
                        $ K_OutfitDay = "pink outfit"
                elif K_Schedule[Weekday] == 2: #Wed
                        $ K_OutfitDay = "red outfit"
                elif K_Schedule[Weekday] == 3 and K_Custom[0]: #Thu
                        $ K_OutfitDay = "custom1"
                elif K_Schedule[Weekday] == 4: #Fri
                        $ K_OutfitDay = "gym"
                elif K_Schedule[Weekday] == 5 and K_Custom2[0]: #Sat
                        $ K_OutfitDay = "custom2"
                elif K_Schedule[Weekday] == 6 and K_Custom3[0]: #Sun
                        $ K_OutfitDay = "custom3"
                else: #Mon
                        $ Options = ["pink outfit", "red outfit"]
                        $ Options.append("custom1") if K_Custom[0] == 2 else Options
                        $ Options.append("custom2") if K_Custom2[0] == 2 else Options
                        $ Options.append("custom3") if K_Custom3[0] == 2 else Options
                        $ Options.append("custom4") if K_Custom4[0] == 2 else Options
                        $ Options.append("custom5") if K_Custom5[0] == 2 else Options
                        $ Options.append("custom6") if K_Custom6[0] == 2 else Options
                        $ Options.append("custom7") if K_Custom7[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ K_OutfitDay = Options[0]
                        $ del Options[:]  
                $ K_Outfit = K_OutfitDay 
        #End clothing portion
        
        
        #Location portion   
        if "Kitty" in Party or K_Loc == "hold":
                pass          
                
        elif Weekday == 0 or Weekday == 2:
        #MoWe   
                if Current_Time == "Morning":
                        $ K_Loc = "bg classroom"
                elif Current_Time == "Midday": 
                        $ K_Loc = "bg dangerroom"
                else:
                        $ K_Loc = "bg kitty"
        elif Weekday == 4:
        #Fr    
                if Current_Time == "Morning":
                        $ K_Loc = "bg classroom"
                elif Current_Time == "Midday": 
                        $ K_Loc = "bg dangerroom"
                elif Current_Time == "Evening": 
                        $ K_Loc = "bg field"
                else:
                        $ K_Loc = "bg kitty"
        elif Weekday == 1 or Weekday == 3:
        #TuThu        
                if Current_Time == "Morning":
                        $ K_Loc = "bg classroom"
                elif Current_Time == "Midday":
                        $ K_Loc = "bg dangerroom"
                else:
                        $ K_Loc = "bg kitty"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ K_Loc = "bg campus"
                elif Current_Time == "Midday":
                        $ K_Loc = "bg pool"
                elif Current_Time == "Evening": 
                        $ K_Loc = "bg field"
                else:
                        $ K_Loc = "bg kitty"
                        
        #If Kitty has moved from where she started this action. . .   
        if K_Loc != LocTemp and "Kitty" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ K_RecentActions.append("leaving") 
                elif K_Loc == bg_current: #If she's showed up
                    $ K_RecentActions.append("arriving") 
        return
#End Kitty's Schedule


label Kitty_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in K_Todo:
                $ K_PubeC -= 1
                if K_PubeC >= 1:
                        pass
                else:            
                        $ K_Pubes = 1
                        $ K_Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in K_Todo:               
                $ K_Pubes = 0
                $ K_Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in K_Todo:                
                $ K_Pierce = "ring"
                $ K_Todo.remove("ring")
        if "barbell" in K_Todo:
                $ K_Pierce = "barbell"
                $ K_Todo.remove("barbell")    

        $ K_Spank = 0   

        return
 

# Emma's Outfit //////////////////////////////////////////////
label EmmaOutfit(E_OutfitTemp = E_Outfit, Spunk = 0, Undressed = 0, Changed = 0):   
        # E_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return

        if E_Gag:
            "She removes her gag"
            $ E_Gag = 0
        
        if E_OutfitTemp != E_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Emma" in Party and E_OutfitTemp == E_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ E_OutfitTemp = E_Outfit
        if E_Loc == "bg showerroom" and "Emma" not in Party and E_OutfitTemp != "nude":
                #Automatically puts her in the towel while in the shower
                $ E_OutfitTemp = "towel"                                  
        elif E_Loc != "bg showerroom" and E_Loc != "bg pool":
                #Dries her off
                $ E_Water = 0
                
        if E_Spunk:
                if "painted" not in E_DailyActions or "cleaned" not in E_DailyActions:        
                    $ del E_Spunk[:] 
                
        $ E_Upskirt = 0
        $ E_Uptop = 0
        $ E_PantiesDown = 0
        if E_OutfitTemp == "teacher":
                    if 0 in (E_Legs,E_Over,E_Chest):
                            $ Undressed = 1
                    elif E_Panties == 0 and "pantyless" not in E_DailyActions:                        
                            $ Undressed = 1   
                    $ E_Arms = 0
                    $ E_Legs = "pants"
                    $ E_Over = "jacket"
                    $ E_Chest = "corset"
                    $ E_Panties = "white panties"        
                    $ E_Neck = "choker"
                    $ E_Hair = "wavy"
                    $ E_Hose = 0  
        elif E_OutfitTemp == "costume":
                    if 0 in (E_Legs,E_Chest):
                            $ Undressed = 1
                    elif E_Panties == 0 and "pantyless" not in E_DailyActions:                        
                            $ Undressed = 1   
                    $ E_Arms = "white gloves"
                    $ E_Legs = "pants"
                    $ E_Over = 0
                    $ E_Chest = "corset"
                    $ E_Panties = "white panties"        
                    $ E_Neck = "choker"
                    $ E_Hair = "wavy"
                    $ E_Hose = 0 
        elif E_OutfitTemp == "sexy costume":
                    if E_Chest == 0:
                            $ Undressed = 1
                    elif E_Panties == 0 and "pantyless" not in E_DailyActions:                        
                            $ Undressed = 1   
                    $ E_Arms = "white gloves"
                    $ E_Legs = 0
                    $ E_Over = 0
                    $ E_Chest = "corset"
                    $ E_Panties = "white panties"        
                    $ E_Neck = "choker"
                    $ E_Hair = "wavy"
                    $ E_Hose = 0 
        elif E_OutfitTemp == "bikini":
                    if E_Chest == 0:
                            $ Undressed = 1
                    elif E_Panties == 0 and "pantyless" not in E_DailyActions:                        
                            $ Undressed = 1   
                    $ E_Arms = 0
                    $ E_Legs = 0
                    $ E_Over = 0
                    $ E_Chest = "bikini"
                    $ E_Panties = "bikini"        
                    $ E_Neck = 0
                    $ E_Hair = "wavy"
                    $ E_Hose = 0     
        elif E_OutfitTemp == "towel":
                    if E_Over == 0:
                            $ Undressed = 2
                    $ E_Arms = 0
                    $ E_Legs = 0
                    $ E_Chest = 0
                    $ E_Over = "towel"
                    $ E_Panties = 0        
                    $ E_Hose = 0          
                    $ E_Neck = 0  
                    $ E_Hair = "bun" 
                    $ E_Shame = 35
        elif E_OutfitTemp == "nude":
                    $ E_Arms = 0
                    $ E_Legs = 0
                    $ E_Chest = 0
                    $ E_Over = 0
                    $ E_Panties = 0              
                    $ E_Neck = 0
                    $ E_Hose = 0   
                    $ E_Shame = 50
        elif E_OutfitTemp == "naked pool":
                    $ E_Arms = 0
                    $ E_Legs = 0
                    $ E_Over = 0
                    $ E_Chest = "naked pool"
                    $ E_Panties = "naked pool"              
                    $ E_Neck = 0
                    $ E_Hair = "wavy"
                    $ E_Hose = 0   
        elif E_OutfitTemp == "custom1":
                    if not E_Legs and E_Custom[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom[6] and "pantyless" not in E_DailyActions:          
                            $ Undressed = 1
                    elif not E_Hose and E_Custom[9]:          
                            $ Undressed = 1
                    
                    $ E_Arms = E_Custom[1]
                    $ E_Legs = E_Custom[2]
                    $ E_Over = E_Custom[3]    
                    $ E_Neck = E_Custom[4]
                    $ E_Chest = E_Custom[5]
                    $ E_Panties = E_Custom[6]  
                    $ E_Hair = E_Custom[8] if E_Custom[8] else E_Hair 
                    $ E_Hose = E_Custom[9]                     
                    $ E_Shame = E_OutfitShame[3]
        elif E_OutfitTemp == "custom2":
                    if not E_Legs and E_Custom2[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom2[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom2[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom2[6] and "pantyless" not in E_DailyActions:          
                            $ Undressed = 1
                    elif not E_Hose and E_Custom2[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom2[1]
                    $ E_Legs = E_Custom2[2]
                    $ E_Over = E_Custom2[3]   
                    $ E_Neck = E_Custom2[4]
                    $ E_Chest = E_Custom2[5]
                    $ E_Panties = E_Custom2[6] 
                    $ E_Hair = E_Custom2[8] if E_Custom2[8] else E_Hair
                    $ E_Hose = E_Custom2[9]                      
                    $ E_Shame = E_OutfitShame[5]
        elif E_OutfitTemp == "custom3":
                    if not E_Legs and E_Custom3[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom3[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom3[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom3[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_Custom3[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom3[1]
                    $ E_Legs = E_Custom3[2]
                    $ E_Over = E_Custom3[3]
                    $ E_Neck = E_Custom3[4]
                    $ E_Chest = E_Custom3[5]
                    $ E_Panties = E_Custom3[6]  
                    $ E_Hair = E_Custom3[8] if E_Custom3[8] else E_Hair  
                    $ E_Hose = E_Custom3[9]                         
                    $ E_Shame = E_OutfitShame[6]
        elif E_OutfitTemp == "custom4":
                    if not E_Legs and E_Custom4[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom4[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom4[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom4[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_Custom4[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom4[1]
                    $ E_Legs = E_Custom4[2]
                    $ E_Over = E_Custom4[3]
                    $ E_Neck = E_Custom4[4]
                    $ E_Chest = E_Custom4[5]
                    $ E_Panties = E_Custom4[6]    
                    $ E_Hose = E_Custom4[9]   
                    $ E_Hair = E_Custom4[8] if E_Custom4[8] else E_Hair
                    $ E_Shame = E_OutfitShame[11]
        elif E_OutfitTemp == "custom5":
                    if not E_Legs and E_Custom5[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom5[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom5[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom5[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_Custom5[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom5[1]
                    $ E_Legs = E_Custom5[2]
                    $ E_Over = E_Custom5[3]
                    $ E_Neck = E_Custom5[4]
                    $ E_Chest = E_Custom5[5]
                    $ E_Panties = E_Custom5[6]    
                    $ E_Hose = E_Custom5[9]   
                    $ E_Hair = E_Custom5[8] if E_Custom5[8] else E_Hair
                    $ E_Shame = E_OutfitShame[12]
        elif E_OutfitTemp == "custom6":
                    if not E_Legs and E_Custom6[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom6[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom6[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom6[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_Custom6[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom6[1]
                    $ E_Legs = E_Custom6[2]
                    $ E_Over = E_Custom6[3]
                    $ E_Neck = E_Custom6[4]
                    $ E_Chest = E_Custom6[5]
                    $ E_Panties = E_Custom6[6]    
                    $ E_Hose = E_Custom6[9]   
                    $ E_Hair = E_Custom6[8] if E_Custom6[8] else E_Hair
                    $ E_Shame = E_OutfitShame[13]
        elif E_OutfitTemp == "custom7":
                    if not E_Legs and E_Custom7[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom7[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom7[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom7[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_Custom7[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom7[1]
                    $ E_Legs = E_Custom7[2]
                    $ E_Over = E_Custom7[3]
                    $ E_Neck = E_Custom7[4]
                    $ E_Chest = E_Custom7[5]
                    $ E_Panties = E_Custom7[6]    
                    $ E_Hose = E_Custom7[9]   
                    $ E_Hair = E_Custom7[8] if E_Custom7[8] else E_Hair
                    $ E_Shame = E_OutfitShame[14]
        elif E_OutfitTemp == "sleep":  
                    if not E_Legs and E_Sleepwear[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Sleepwear[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Sleepwear[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Sleepwear[6] and "pantyless" not in E_DailyActions:        
                            $ Undressed = 1
                    elif not E_Hose and E_Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Sleepwear[1] #0
                    $ E_Legs = E_Sleepwear[2] #shorts
                    $ E_Over = E_Sleepwear[3] #0
                    $ E_Neck = E_Sleepwear[4] #0
                    $ E_Chest = E_Sleepwear[5] #"cami"
                    $ E_Panties = E_Sleepwear[6] #"green panties"
                    $ E_Hair = E_Sleepwear[8] if E_Sleepwear[8] else E_Hair 
                    $ E_Hose = E_Sleepwear[9] #0  
                    
                    $ E_Hair = "long"
                    $ E_Shame = E_OutfitShame[4]
                    
        elif E_OutfitTemp == "gym":
                    if not E_Legs and E_Gym[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Gym[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Gym[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Gym[6] and "pantyless" not in E_DailyActions:        
                            $ Undressed = 1
                    elif not E_Hose and E_Gym[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Gym[1]
                    $ E_Legs = E_Gym[2]
                    $ E_Over = E_Gym[3] 
                    $ E_Neck = E_Gym[4]
                    $ E_Chest = E_Gym[5]
                    $ E_Panties = E_Gym[6]   
                    $ E_Hair = E_Gym[8] if E_Gym[8] else E_Hair 
                    $ E_Hose = E_Gym[9]     
                    $ E_Shame = E_OutfitShame[7]   
                
        if E_Panties and "pantyless" in E_DailyActions:       
                    # This checks the pantyless state from flirting 
                    if E_Legs == "pants" or HoseNum("Emma") >= 10:
                        $ E_Shame -= 5    
                    elif E_Legs:
                        $ E_Shame -= 10  
                    elif E_Panties == "green panties":
                        $ E_Shame -= 20  
                    elif E_Panties == "lace panties":
                        $ E_Shame -= 25             
                    else:
                        $ E_Shame -= 23  
                    
                    $ E_Panties = 0        
                    $ E_Shame = 0 if E_Shame < 0 else E_Shame
                    
        if not Changed and E_OutfitTemp == E_Outfit and E_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."  
        
        $ E_Outfit = E_OutfitTemp
        call Emma_Tits_Up from _call_Emma_Tits_Up
        
        return
#End Emma's Outfits
      
label Emma_Schedule(Clothes = 1, Location = 1, LocTemp = E_Loc): 
        #Emma's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in E_History or ("Emma" in Party and Clothes != 2): 
                #if she's in a party, never mind
                return  
        if LocTemp == bg_current and Current_Time == "morning":
                #she slept over, so just forget this for now  
                if "sleepover" not in E_RecentActions:
                    $ E_RecentActions.append("sleepover")
                    return           
                #the second time this is called, it skips through    
        
        $ D20 = renpy.random.randint(1, 20) 
        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:                                                       #Pick clothes for the day
                $ Options = ["teacher"]
                $ Options.append("costume") if ApprovalCheck("Emma", 1000) else Options
                $ Options.append("custom1") if E_Custom[0] == 2 else Options
                $ Options.append("custom2") if E_Custom2[0] == 2 else Options
                $ Options.append("custom3") if E_Custom3[0] == 2 else Options
                $ Options.append("custom4") if E_Custom4[0] == 2 else Options
                $ Options.append("custom5") if E_Custom5[0] == 2 else Options
                $ Options.append("custom6") if E_Custom6[0] == 2 else Options
                $ Options.append("custom7") if E_Custom7[0] == 2 else Options
                $ renpy.random.shuffle(Options) 
                $ E_OutfitDay = Options[0]
                $ del Options[:]  
                $ E_Outfit = E_OutfitDay 
        #End clothing portion
        
        #Location portion   
        if "Emma" in Party or E_Loc == "hold":
                pass          
                
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ E_Loc = "bg emma"
                elif Current_Time == "Midday": 
                        $ E_Loc = "bg teacher"
                else:
                        $ E_Loc = "bg emma"
        elif Weekday == 1 or Weekday == 3:
        #TuThu      
                if Current_Time == "Morning":
                        $ E_Loc = "bg emma"
                elif Current_Time == "Midday":
                        $ E_Loc = "bg teacher"
                elif Current_Time == "Evening":
                        $ E_Loc = "bg dangerroom"
                else:
                        $ E_Loc = "bg emma"
        else:
        #Weekend                               
                # if Current_Time == "Morning":
                #         $ Options = ["bg pool", "bg dangerroom"]
                #         $ renpy.random.shuffle(Options)
                #         $ E_Loc = Options[0]
                #         $ del Options[:]
                # elif Current_Time == "Midday":
                #         $ Options = ["bg pool", "bg dangerroom"]
                #         $ renpy.random.shuffle(Options)
                #         $ E_Loc = Options[0]
                #         $ del Options[:]
                # else:
                #         $ E_Loc = "bg emma"

                if Current_Time == "Night":
                        $ E_Loc = "bg emma"
                else:
                        $ Options = ["bg pool", "bg dangerroom"]
                        $ renpy.random.shuffle(Options)
                        $ E_Loc = Options[0]
                        $ del Options[:]

                        
        #If Emma has moved from where she started this action. . .   
        if E_Loc != LocTemp and "Emma" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ E_RecentActions.append("leaving") 
                elif E_Loc == bg_current: #If she's showed up
                    $ E_RecentActions.append("arriving") 
        return
#End Emma's Schedule


label Emma_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in E_Todo:
                $ E_PubeC -= 1
                if E_PubeC >= 1:
                        pass
                else:            
                        $ E_Pubes = 1
                        $ E_Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in E_Todo:               
                $ E_Pubes = 0
                $ E_Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in E_Todo:                
                $ E_Pierce = "ring"
                $ E_Todo.remove("ring")
        if "barbell" in E_Todo:
                $ E_Pierce = "barbell"
                $ E_Todo.remove("barbell")            
        return
        
        

# Mystique's Outfit //////////////////////////////////////////////
label MystiqueOutfit(M_OutfitTemp = newgirl["Mystique"].Outfit, Spunk = 0, Undressed = 0, Changed = 0):   
        # M_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return

        if newgirl["Mystique"].Gag:
            "She removes her gag"
            $ newgirl["Mystique"].Gag = 0
        
        if M_OutfitTemp != newgirl["Mystique"].Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Mystique" in Party and M_OutfitTemp == newgirl["Mystique"].OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ M_OutfitTemp = newgirl["Mystique"].Outfit
        if newgirl["Mystique"].Loc == "bg teacher" or newgirl["Mystique"].Loc == "bg classroom":
                #this ignores her daily outfit if she's in the classroom
                $ M_OutfitTemp = "teacher"
        if newgirl["Mystique"].Loc == "bg showerroom" and "Mystique" not in Party and M_OutfitTemp != "nude":
                #Automatically puts her in the towel while in the shower
                $ M_OutfitTemp = "towel"                                  
        elif newgirl["Mystique"].Loc != "bg showerroom" and newgirl["Mystique"].Loc != "bg pool":
                #Dries her off
                $ newgirl["Mystique"].Water = 0
                
        if newgirl["Mystique"].Spunk:
                if "painted" not in newgirl["Mystique"].DailyActions or "cleaned" not in newgirl["Mystique"].DailyActions:        
                    $ del newgirl["Mystique"].Spunk[:] 
                
        $ newgirl["Mystique"].Upskirt = 0
        $ newgirl["Mystique"].Uptop = 0
        $ newgirl["Mystique"].PantiesDown = 0
        if M_OutfitTemp == "teacher":
                    if 0 in (newgirl["Mystique"].Legs,newgirl["Mystique"].Over,newgirl["Mystique"].Chest,newgirl["Mystique"].Hose):
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = "black skirt"
                    $ newgirl["Mystique"].Over = "red shirt"
                    $ newgirl["Mystique"].Chest = "black bra"
                    $ newgirl["Mystique"].Panties = "black panties"        
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = "stockings"  
                    $ newgirl["Mystique"].Glasses = "glasses"  
        if M_OutfitTemp == "regular":
                    if 0 in (newgirl["Mystique"].Legs,newgirl["Mystique"].Chest,newgirl["Mystique"].Hose):
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = "black skirt"
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "top"
                    $ newgirl["Mystique"].Panties = "black panties"        
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = 'stockings'  
                    $ newgirl["Mystique"].Glasses = 0  
        elif M_OutfitTemp == "costume":
                    if 0 in (newgirl["Mystique"].Legs,newgirl["Mystique"].Chest):
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = "white gloves"
                    $ newgirl["Mystique"].Legs = "pants"
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "corset"
                    $ newgirl["Mystique"].Panties = "white panties"        
                    $ newgirl["Mystique"].Neck = "choker"
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = 0 
                    $ newgirl["Mystique"].Glasses = 0  
        elif M_OutfitTemp == "bikini":
                    if newgirl["Mystique"].Chest == 0:
                            $ Undressed = 1
                    elif newgirl["Mystique"].Panties == 0 and "pantyless" not in newgirl["Mystique"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "yellow bikini"
                    $ newgirl["Mystique"].Panties = "yellow bikini"        
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "basic"
                    $ newgirl["Mystique"].Hose = 0     
                    $ newgirl["Mystique"].Glasses = 0  
        elif M_OutfitTemp == "towel":
                    if newgirl["Mystique"].Over == 0:
                            $ Undressed = 2
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Chest = 0
                    $ newgirl["Mystique"].Over = "towel"
                    $ newgirl["Mystique"].Panties = 0        
                    $ newgirl["Mystique"].Hose = 0          
                    $ newgirl["Mystique"].Neck = 0  
                    $ newgirl["Mystique"].Hair = "bun" 
                    $ newgirl["Mystique"].Shame = 35
        elif M_OutfitTemp == "nude":
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Chest = 0
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Panties = 0              
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hose = 0   
                    $ newgirl["Mystique"].Shame = 50
        elif M_OutfitTemp == "naked pool":
                    $ newgirl["Mystique"].Arms = 0
                    $ newgirl["Mystique"].Legs = 0
                    $ newgirl["Mystique"].Over = 0
                    $ newgirl["Mystique"].Chest = "naked pool"
                    $ newgirl["Mystique"].Panties = "naked pool"              
                    $ newgirl["Mystique"].Neck = 0
                    $ newgirl["Mystique"].Hair = "wavy"
                    $ newgirl["Mystique"].Hose = 0   
        elif M_OutfitTemp == "custom1":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom[6] and "pantyless" not in newgirl["Mystique"].DailyActions:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom[9]:          
                            $ Undressed = 1
                    
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom[3]    
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom[8] if newgirl["Mystique"].Custom[8] else newgirl["Mystique"].Hair 
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom[9]                     
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[3]
        elif M_OutfitTemp == "custom2":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom2[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom2[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom2[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom2[6] and "pantyless" not in newgirl["Mystique"].DailyActions:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom2[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom2[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom2[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom2[3]   
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom2[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom2[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom2[6] 
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom2[8] if newgirl["Mystique"].Custom2[8] else newgirl["Mystique"].Hair
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom2[9]                      
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[5]
        elif M_OutfitTemp == "custom3":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom3[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom3[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom3[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom3[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom3[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom3[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom3[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom3[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom3[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom3[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom3[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom3[8] if newgirl["Mystique"].Custom3[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom3[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[6]
        elif M_OutfitTemp == "custom4":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom4[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom4[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom4[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom4[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom4[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom4[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom4[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom4[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom4[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom4[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom4[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom4[8] if newgirl["Mystique"].Custom4[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom4[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[11]
        elif M_OutfitTemp == "custom5":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom5[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom5[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom5[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom5[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom5[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom5[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom5[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom5[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom5[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom5[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom5[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom5[8] if newgirl["Mystique"].Custom5[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom5[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[12]
        elif M_OutfitTemp == "custom6":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom6[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom6[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom6[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom6[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom6[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom6[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom6[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom6[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom6[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom6[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom6[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom6[8] if newgirl["Mystique"].Custom6[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom6[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[13]
        elif M_OutfitTemp == "custom7":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Custom7[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Custom7[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Custom7[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Custom7[6] and "pantyless" not in newgirl["Mystique"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Custom7[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Custom7[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Custom7[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Custom7[3]
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Custom7[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Custom7[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Custom7[6]  
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Custom7[8] if newgirl["Mystique"].Custom7[8] else newgirl["Mystique"].Hair  
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Custom7[9]                         
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[14]
        elif M_OutfitTemp == "sleep":  
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Sleepwear[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Sleepwear[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Sleepwear[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Sleepwear[6] and "pantyless" not in newgirl["Mystique"].DailyActions:        
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Sleepwear[1] #0
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Sleepwear[2] #shorts
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Sleepwear[3] #0
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Sleepwear[4] #0
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Sleepwear[5] #"cami"
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Sleepwear[6] #"green panties"
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Sleepwear[8] if newgirl["Mystique"].Sleepwear[8] else newgirl["Mystique"].Hair 
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Sleepwear[9] #0  
                    
                    $ newgirl["Mystique"].Hair = "long"
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[4]
                    
        elif M_OutfitTemp == "gym":
                    if not newgirl["Mystique"].Legs and newgirl["Mystique"].Gym[2]:            
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Over and newgirl["Mystique"].Gym[3]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Chest and newgirl["Mystique"].Gym[5]:          
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Panties and newgirl["Mystique"].Gym[6] and "pantyless" not in newgirl["Mystique"].DailyActions:        
                            $ Undressed = 1
                    elif not newgirl["Mystique"].Hose and newgirl["Mystique"].Gym[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Mystique"].Arms = newgirl["Mystique"].Gym[1]
                    $ newgirl["Mystique"].Legs = newgirl["Mystique"].Gym[2]
                    $ newgirl["Mystique"].Over = newgirl["Mystique"].Gym[3] 
                    $ newgirl["Mystique"].Neck = newgirl["Mystique"].Gym[4]
                    $ newgirl["Mystique"].Chest = newgirl["Mystique"].Gym[5]
                    $ newgirl["Mystique"].Panties = newgirl["Mystique"].Gym[6]   
                    $ newgirl["Mystique"].Hair = newgirl["Mystique"].Gym[8] if newgirl["Mystique"].Gym[8] else newgirl["Mystique"].Hair 
                    $ newgirl["Mystique"].Hose = newgirl["Mystique"].Gym[9]     
                    $ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[7]   
                
        if newgirl["Mystique"].Panties and "pantyless" in newgirl["Mystique"].DailyActions:       
                    # This checks the pantyless state from flirting 
                    if newgirl["Mystique"].Legs == "tights" or HoseNum("Mystique") >= 10:
                        $ newgirl["Mystique"].Shame -= 5    
                    elif newgirl["Mystique"].Legs:
                        $ newgirl["Mystique"].Shame -= 10  
                    elif newgirl["Mystique"].Panties == "green panties":
                        $ newgirl["Mystique"].Shame -= 20  
                    elif newgirl["Mystique"].Panties == "lace panties":
                        $ newgirl["Mystique"].Shame -= 25             
                    else:
                        $ newgirl["Mystique"].Shame -= 23  
                    
                    $ newgirl["Mystique"].Panties = 0        
                    $ newgirl["Mystique"].Shame = 0 if newgirl["Mystique"].Shame < 0 else newgirl["Mystique"].Shame
                    
        if not Changed and M_OutfitTemp == newgirl["Mystique"].Outfit and newgirl["Mystique"].Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."  
        call Mystique_Tits_Up from _call_Mystique_Tits_Up
        
        $ newgirl["Mystique"].Outfit = M_OutfitTemp

        return
#End Mystique's Outfits
      
label Mystique_Schedule(Clothes = 1, Location = 1, LocTemp = newgirl["Mystique"].Loc): 
        #Mystique's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in newgirl["Mystique"].History or ("Mystique" in Party and Clothes != 2): 
                #if she's in a party, never mind
                return  
        if LocTemp == bg_current and Current_Time == "morning":
                #she slept over, so just forget this for now  
                if "sleepover" not in newgirl["Mystique"].RecentActions:
                    $ newgirl["Mystique"].RecentActions.append("sleepover")
                    return           
                #the second time this is called, it skips through    
        
        $ D20 = renpy.random.randint(1, 20) 
        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:                                                       #Pick clothes for the day
                $ Options = ["regular", "teacher"]
                #$ Options = ["regular"]
                #$ Options.append("costume") if ApprovalCheck("Mystique", 1000) else Options
                $ Options.append("custom1") if newgirl["Mystique"].Custom[0] == 2 else Options
                $ Options.append("custom2") if newgirl["Mystique"].Custom2[0] == 2 else Options
                $ Options.append("custom3") if newgirl["Mystique"].Custom3[0] == 2 else Options
                $ Options.append("custom4") if newgirl["Mystique"].Custom4[0] == 2 else Options
                $ Options.append("custom5") if newgirl["Mystique"].Custom5[0] == 2 else Options
                $ Options.append("custom6") if newgirl["Mystique"].Custom6[0] == 2 else Options
                $ Options.append("custom7") if newgirl["Mystique"].Custom7[0] == 2 else Options
                $ renpy.random.shuffle(Options) 
                $ newgirl["Mystique"].OutfitDay = Options[0]
                $ del Options[:]  
                $ newgirl["Mystique"].Outfit = newgirl["Mystique"].OutfitDay 
        #End clothing portion
        if newgirl["Mystique"].Loc == "bg teacher" or newgirl["Mystique"].Loc == "bg classroom":
                $ newgirl["Mystique"].Outfit = "teacher" 
            
        #Location portion   
        if "Mystique" in Party or newgirl["Mystique"].Loc == "hold":
                pass          
                
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ newgirl["Mystique"].Loc = "bg teacher"
                elif Current_Time == "Midday": 
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                else:
                        $ newgirl["Mystique"].Loc = "bg Mystique"
        elif Weekday == 1 or Weekday == 3:
        #TuThu      
                if Current_Time == "Morning":
                        $ newgirl["Mystique"].Loc = "bg teacher"
                elif Current_Time == "Midday":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                elif Current_Time == "Evening":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                else:
                        $ newgirl["Mystique"].Loc = "bg dangerroom"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ Options = ["bg Mystique", "bg Mystique"]
                        $ renpy.random.shuffle(Options)
                        $ newgirl["Mystique"].Loc = Options[0]
                        $ del Options[:]
                elif Current_Time == "Midday":
                        $ Options = ["bg Mystique", "bg Mystique"]
                        $ renpy.random.shuffle(Options)
                        $ newgirl["Mystique"].Loc = Options[0]
                        $ del Options[:]
                else:
                        $ newgirl["Mystique"].Loc = "bg Mystique"

                if Current_Time == "Night":
                        $ newgirl["Mystique"].Loc = "bg Mystique"
                else:
                        $ Options = ["bg Mystique", "bg Mystique"]
                        $ renpy.random.shuffle(Options)
                        $ newgirl["Mystique"].Loc = Options[0]
                        $ del Options[:]

                        
        #If Mystique has moved from where she started this action. . .   
        if newgirl["Mystique"].Loc != LocTemp and "Mystique" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ newgirl["Mystique"].RecentActions.append("leaving") 
                elif newgirl["Mystique"].Loc == bg_current: #If she's showed up
                    $ newgirl["Mystique"].RecentActions.append("arriving") 
        return
#End Mystique's Schedule


label Mystique_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in newgirl["Mystique"].Todo:
                $ newgirl["Mystique"].PubeC -= 1
                if newgirl["Mystique"].PubeC >= 1:
                        pass
                else:            
                        $ newgirl["Mystique"].Pubes = 1
                        $ newgirl["Mystique"].Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in newgirl["Mystique"].Todo:               
                $ newgirl["Mystique"].Pubes = 0
                $ newgirl["Mystique"].Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in newgirl["Mystique"].Todo:                
                $ newgirl["Mystique"].Pierce = "ring"
                $ newgirl["Mystique"].Todo.remove("ring")
        if "barbell" in newgirl["Mystique"].Todo:
                $ newgirl["Mystique"].Pierce = "barbell"
                $ newgirl["Mystique"].Todo.remove("barbell")            
        return

# Laura's Outfit //////////////////////////////////////////////
label LauraOutfit(L_OutfitTemp = newgirl["Laura"].Outfit, Spunk = 0, Undressed = 0, Changed = 0):   
        # L_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if L_OutfitTemp == 5: #this sets it to default if using AnyOutfit
                $ L_OutfitTemp = newgirl["Laura"].Outfit
        elif L_OutfitTemp == 6: #this sets it to default if using AnyOutfit
                $ L_OutfitTemp = newgirl["Laura"].OutfitDay
                
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
                #Skips theis check if it's a sleepover
                return
        
        if L_OutfitTemp != newgirl["Laura"].Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Laura" in Party and L_OutfitTemp == newgirl["Laura"].OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ L_OutfitTemp = newgirl["Laura"].Outfit
        if newgirl["Laura"].Loc == "bg showerroom" and "Laura" not in Party and L_OutfitTemp != "nude":
                #Automatically puts her in the towel while in the shower
                $ L_OutfitTemp = "towel"                                  
        elif newgirl["Laura"].Loc != "bg showerroom":
                #Dries her off
                $ newgirl["Laura"].Water = 0
                
        if newgirl["Laura"].Spunk:
                if "painted" not in newgirl["Laura"].DailyActions or "cleaned" not in newgirl["Laura"].DailyActions:        
                    $ del newgirl["Laura"].Spunk[:] 
                
        $ newgirl["Laura"].Upskirt = 0
        $ newgirl["Laura"].Uptop = 0
        $ newgirl["Laura"].PantiesDown = 0
        if L_OutfitTemp == "mission":
                    if 0 in (newgirl["Laura"].Legs,newgirl["Laura"].Over,newgirl["Laura"].Chest):
                            $ Undressed = 1
                    elif newgirl["Laura"].Panties == 0 and "pantyless" not in newgirl["Laura"].DailyActions:                        
                            $ Undressed = 1   
                    $ newgirl["Laura"].Arms = "wrists"
                    $ newgirl["Laura"].Legs = "leather pants"
                    $ newgirl["Laura"].Over = 0
                    $ newgirl["Laura"].Chest = "leather bra"
                    $ newgirl["Laura"].Panties = "leather panties"        
                    $ newgirl["Laura"].Neck = "leash choker"                 
                    $ newgirl["Laura"].Boots = 0
                    $ newgirl["Laura"].Hair = "long"
                    $ newgirl["Laura"].Hose = 0  
                    $ newgirl["Laura"].Shame = 0
        elif L_OutfitTemp == "towel":
                    if newgirl["Laura"].Over == 0:
                            $ Undressed = 2
                    $ newgirl["Laura"].Arms = 0
                    $ newgirl["Laura"].Legs = 0
                    $ newgirl["Laura"].Chest = 0
                    $ newgirl["Laura"].Over = "towel"
                    $ newgirl["Laura"].Panties = 0        
                    $ newgirl["Laura"].Hose = 0          
                    $ newgirl["Laura"].Neck = 0                   
                    $ newgirl["Laura"].Boots = 0
                    $ newgirl["Laura"].Hair = "wet" 
                    $ newgirl["Laura"].Shame = 35
        elif L_OutfitTemp == "nude":
                    $ newgirl["Laura"].Arms = 0
                    $ newgirl["Laura"].Legs = 0
                    $ newgirl["Laura"].Chest = 0
                    $ newgirl["Laura"].Over = 0
                    $ newgirl["Laura"].Panties = 0              
                    $ newgirl["Laura"].Neck = 0                    
                    $ newgirl["Laura"].Boots = 0
                    $ newgirl["Laura"].Hose = 0   
                    $ newgirl["Laura"].Shame = 50
        elif L_OutfitTemp == "custom1":
                    if not newgirl["Laura"].Legs and newgirl["Laura"].Custom[2]:            
                            $ Undressed = 1
                    elif not newgirl["Laura"].Over and newgirl["Laura"].Custom[3]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Chest and newgirl["Laura"].Custom[5]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Panties and newgirl["Laura"].Custom[6] and "pantyless" not in newgirl["Laura"].DailyActions:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Hose and newgirl["Laura"].Custom[9]:          
                            $ Undressed = 1
                    
                    $ newgirl["Laura"].Arms = newgirl["Laura"].Custom[1]
                    $ newgirl["Laura"].Legs = newgirl["Laura"].Custom[2]
                    $ newgirl["Laura"].Over = newgirl["Laura"].Custom[3]    
                    $ newgirl["Laura"].Neck = newgirl["Laura"].Custom[4]
                    $ newgirl["Laura"].Chest = newgirl["Laura"].Custom[5]
                    $ newgirl["Laura"].Panties = newgirl["Laura"].Custom[6]  
                    $ newgirl["Laura"].Boots = newgirl["Laura"].Custom[7] 
                    $ newgirl["Laura"].Hair = newgirl["Laura"].Custom[8] if newgirl["Laura"].Custom[8] else newgirl["Laura"].Hair 
                    $ newgirl["Laura"].Hose = newgirl["Laura"].Custom[9]                     
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[3]
        elif L_OutfitTemp == "custom2":
                    if not newgirl["Laura"].Legs and newgirl["Laura"].Custom2[2]:            
                            $ Undressed = 1
                    elif not newgirl["Laura"].Over and newgirl["Laura"].Custom2[3]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Chest and newgirl["Laura"].Custom2[5]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Panties and newgirl["Laura"].Custom2[6] and "pantyless" not in newgirl["Laura"].DailyActions:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Hose and newgirl["Laura"].Custom2[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Laura"].Arms = newgirl["Laura"].Custom2[1]
                    $ newgirl["Laura"].Legs = newgirl["Laura"].Custom2[2]
                    $ newgirl["Laura"].Over = newgirl["Laura"].Custom2[3]   
                    $ newgirl["Laura"].Neck = newgirl["Laura"].Custom2[4]
                    $ newgirl["Laura"].Chest = newgirl["Laura"].Custom2[5]
                    $ newgirl["Laura"].Panties = newgirl["Laura"].Custom2[6] 
                    $ newgirl["Laura"].Boots = newgirl["Laura"].Custom2[7] 
                    $ newgirl["Laura"].Hair = newgirl["Laura"].Custom2[8] if newgirl["Laura"].Custom2[8] else newgirl["Laura"].Hair
                    $ newgirl["Laura"].Hose = newgirl["Laura"].Custom2[9]                      
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[5]
        elif L_OutfitTemp == "custom3":
                    if not newgirl["Laura"].Legs and newgirl["Laura"].Custom3[2]:            
                            $ Undressed = 1
                    elif not newgirl["Laura"].Over and newgirl["Laura"].Custom3[3]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Chest and newgirl["Laura"].Custom3[5]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Panties and newgirl["Laura"].Custom3[6] and "pantyless" not in newgirl["Laura"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Laura"].Hose and newgirl["Laura"].Custom3[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Laura"].Arms = newgirl["Laura"].Custom3[1]
                    $ newgirl["Laura"].Legs = newgirl["Laura"].Custom3[2]
                    $ newgirl["Laura"].Over = newgirl["Laura"].Custom3[3]
                    $ newgirl["Laura"].Neck = newgirl["Laura"].Custom3[4]
                    $ newgirl["Laura"].Chest = newgirl["Laura"].Custom3[5]
                    $ newgirl["Laura"].Panties = newgirl["Laura"].Custom3[6] 
                    $ newgirl["Laura"].Boots = newgirl["Laura"].Custom3[7]  
                    $ newgirl["Laura"].Hair = newgirl["Laura"].Custom3[8] if newgirl["Laura"].Custom3[8] else newgirl["Laura"].Hair  
                    $ newgirl["Laura"].Hose = newgirl["Laura"].Custom3[9]                         
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[6]
        elif L_OutfitTemp == "temporary":
                    if not newgirl["Laura"].Legs and newgirl["Laura"].TempClothes[2]:            
                            $ Undressed = 1
                    elif not newgirl["Laura"].Over and newgirl["Laura"].TempClothes[3]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Chest and newgirl["Laura"].TempClothes[5]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Panties and newgirl["Laura"].TempClothes[6] and "pantyless" not in newgirl["Laura"].DailyActions:         
                            $ Undressed = 1
                    elif not newgirl["Laura"].Hose and newgirl["Laura"].TempClothes[9]:          
                            $ Undressed = 1
                            
                    $ newgirl["Laura"].Arms = newgirl["Laura"].TempClothes[1]
                    $ newgirl["Laura"].Legs = newgirl["Laura"].TempClothes[2]
                    $ newgirl["Laura"].Over = newgirl["Laura"].TempClothes[3]
                    $ newgirl["Laura"].Neck = newgirl["Laura"].TempClothes[4]
                    $ newgirl["Laura"].Chest = newgirl["Laura"].TempClothes[5]
                    $ newgirl["Laura"].Panties = newgirl["Laura"].TempClothes[6] 
                    $ newgirl["Laura"].Boots = newgirl["Laura"].TempClothes[7]  
                    $ newgirl["Laura"].Hair = newgirl["Laura"].TempClothes[8] if newgirl["Laura"].TempClothes[8] else newgirl["Laura"].Hair  
                    $ newgirl["Laura"].Hose = newgirl["Laura"].TempClothes[9]                         
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[8]
        elif L_OutfitTemp == "sleep":  
                    if not newgirl["Laura"].Legs and newgirl["Laura"].Sleepwear[2]:            
                            $ Undressed = 1
                    elif not newgirl["Laura"].Over and newgirl["Laura"].Sleepwear[3]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Chest and newgirl["Laura"].Sleepwear[5]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Panties and newgirl["Laura"].Sleepwear[6] and "pantyless" not in newgirl["Laura"].DailyActions:        
                            $ Undressed = 1
                    elif not newgirl["Laura"].Hose and newgirl["Laura"].Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Laura"].Arms = newgirl["Laura"].Sleepwear[1] #0
                    $ newgirl["Laura"].Legs = newgirl["Laura"].Sleepwear[2] #shorts
                    $ newgirl["Laura"].Over = newgirl["Laura"].Sleepwear[3] #nighty
                    $ newgirl["Laura"].Neck = newgirl["Laura"].Sleepwear[4] #0
                    $ newgirl["Laura"].Chest = newgirl["Laura"].Sleepwear[5] #corset
                    $ newgirl["Laura"].Panties = newgirl["Laura"].Sleepwear[6] #"white panties"
                    $ newgirl["Laura"].Boots = newgirl["Laura"].Sleepwear[7] 
                    $ newgirl["Laura"].Hair = newgirl["Laura"].Sleepwear[8] if newgirl["Laura"].Sleepwear[8] else newgirl["Laura"].Hair 
                    $ newgirl["Laura"].Hose = newgirl["Laura"].Sleepwear[9] #0  
                    
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[4]                    
        elif L_OutfitTemp == "gym":
                    if not newgirl["Laura"].Legs and newgirl["Laura"].Gym[2]:            
                            $ Undressed = 1
                    elif not newgirl["Laura"].Over and newgirl["Laura"].Gym[3]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Chest and newgirl["Laura"].Gym[5]:          
                            $ Undressed = 1
                    elif not newgirl["Laura"].Panties and newgirl["Laura"].Gym[6] and "pantyless" not in newgirl["Laura"].DailyActions:        
                            $ Undressed = 1
                    elif not newgirl["Laura"].Hose and newgirl["Laura"].Gym[9]:          
                            $ Undressed = 1
                        
                    $ newgirl["Laura"].Arms = newgirl["Laura"].Gym[1]
                    $ newgirl["Laura"].Legs = newgirl["Laura"].Gym[2]
                    $ newgirl["Laura"].Over = newgirl["Laura"].Gym[3] 
                    $ newgirl["Laura"].Neck = newgirl["Laura"].Gym[4]
                    $ newgirl["Laura"].Chest = newgirl["Laura"].Gym[5]
                    $ newgirl["Laura"].Panties = newgirl["Laura"].Gym[6]  
                    $ newgirl["Laura"].Boots = newgirl["Laura"].Gym[7]  
                    $ newgirl["Laura"].Hair = newgirl["Laura"].Gym[8] if newgirl["Laura"].Gym[8] else newgirl["Laura"].Hair 
                    $ newgirl["Laura"].Hose = newgirl["Laura"].Gym[9]     
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[7]   
                
        if newgirl["Laura"].Panties and "pantyless" in newgirl["Laura"].DailyActions:       
                # This checks the pantyless state from flirting 
                if L_OutfitTemp != "sleep" and L_OutfitTemp != "gym":
                        if newgirl["Laura"].Legs == "leather pants" or HoseNum("Laura") >= 10:
                            $ newgirl["Laura"].Shame -= 5    
                        elif newgirl["Laura"].Legs:
                            $ newgirl["Laura"].Shame -= 10  
                        elif newgirl["Laura"].Panties == "leather panties":
                            $ newgirl["Laura"].Shame -= 20   
                        elif newgirl["Laura"].Panties == "lace panties":
                            $ newgirl["Laura"].Shame -= 25            
                        else:
                            $ newgirl["Laura"].Shame -= 23  
                        
                        $ newgirl["Laura"].Panties = 0        
                        $ newgirl["Laura"].Shame = 0 if newgirl["Laura"].Shame < 0 else newgirl["Laura"].Shame
                    
        if not Changed and L_OutfitTemp == newgirl["Laura"].Outfit and newgirl["Laura"].Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."  
        return
#End Laura's Outfits
      
label Laura_Schedule(Clothes = 1, Location = 1, LocTemp = newgirl["Laura"].Loc): 
        #Laura's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in newgirl["Laura"].History or ("Laura" in Party and Clothes != 2): 
                #if she's in a party, never mind
                return  
        if "sleepover" in newgirl["Laura"].Traits and Current_Time == "morning":
                #she slept over, so just forget this for now  
                return             
        
        $ D20 = renpy.random.randint(1, 20) 
        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #Pick clothes for the day
                if newgirl["Laura"].Schedule[Weekday] == 1:
                        $ newgirl["Laura"].OutfitDay = "mission"
                elif newgirl["Laura"].Schedule[Weekday] == 2:
                        $ newgirl["Laura"].OutfitDay = "mission"               # fix, make this second costume
                elif newgirl["Laura"].Schedule[Weekday] == 3 and newgirl["Laura"].Custom[0]:
                        $ newgirl["Laura"].OutfitDay = "custom1"
                elif newgirl["Laura"].Schedule[Weekday] == 4:
                        $ newgirl["Laura"].OutfitDay = "gym"
                elif newgirl["Laura"].Schedule[Weekday] == 5 and newgirl["Laura"].Custom2[0]:
                        $ newgirl["Laura"].OutfitDay = "custom2"
                elif newgirl["Laura"].Schedule[Weekday] == 6 and newgirl["Laura"].Custom3[0]: 
                        $ newgirl["Laura"].OutfitDay = "custom3"
                else: # random
                        $ Options = ["mission"]
                        $ Options.append("custom1") if newgirl["Laura"].Custom[0] == 2 else Options
                        $ Options.append("custom2") if newgirl["Laura"].Custom2[0] == 2 else Options
                        $ Options.append("custom3") if newgirl["Laura"].Custom3[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ newgirl["Laura"].OutfitDay = Options[0]
                        $ del Options[:]  
                $ newgirl["Laura"].Outfit = newgirl["Laura"].OutfitDay 
        #End clothing portion
        
        #Location portion  
        if "Laura" in Party or newgirl["Laura"].Loc == "hold" or not Location:
                pass    
        elif True:
                pass #remove this after she's fully available
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ newgirl["Laura"].Loc = "bg dangerroom"
                elif Current_Time == "Midday": 
                        $ newgirl["Laura"].Loc = "bg classroom"
                elif Current_Time == "Evening":
                        $ newgirl["Laura"].Loc = "bg dangerroom"
                else:
                        $ newgirl["Laura"].Loc = "bg laura"
        elif Weekday == 1 or Weekday == 3:
        #TuThu      
                if Current_Time == "Morning":
                        $ newgirl["Laura"].Loc = "bg dangerroom"
                elif Current_Time == "Midday":
                        $ newgirl["Laura"].Loc = "bg classroom"
                else:
                        $ newgirl["Laura"].Loc = "bg laura"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ newgirl["Laura"].Loc = "bg campus"
                elif Current_Time == "Midday":
                        $ newgirl["Laura"].Loc = "bg laura"
                elif Current_Time == "Evening":
                        $ newgirl["Laura"].Loc = "bg dangerroom"
                else:
                        $ newgirl["Laura"].Loc = "bg laura"
        
        #If Laura has moved from where she started this action. . .   
        if newgirl["Laura"].Loc != LocTemp and "Laura" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ newgirl["Laura"].RecentActions.append("leaving") 
                elif newgirl["Laura"].Loc == bg_current: #If she's showed up
                    $ newgirl["Laura"].RecentActions.append("arriving") 
        if "Laura" in Nearby:
                $ Nearby.remove("Laura")
        return
#End Laura's Schedule


label Laura_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in newgirl["Laura"].Todo:
                $ newgirl["Laura"].PubeC -= 1
                if newgirl["Laura"].PubeC >= 1:
                        pass
                else:            
                        $ newgirl["Laura"].Pubes = 1
                        $ newgirl["Laura"].Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in newgirl["Laura"].Todo:               
                $ newgirl["Laura"].Pubes = 0
                $ newgirl["Laura"].Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in newgirl["Laura"].Todo:                
                $ newgirl["Laura"].Pierce = "ring"
                $ newgirl["Laura"].Todo.remove("ring")
        if "barbell" in newgirl["Laura"].Todo:
                $ newgirl["Laura"].Pierce = "barbell"
                $ newgirl["Laura"].Todo.remove("barbell")            
        return

# Xavier Faces ///////////////////////////////

label XavierFace (Face = X_Emote):
        if Face == "psychic":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "concentrate"
                $ X_Psychic = 1
        if Face == "hypno":
                $ X_Mouth = "neutral"
                $ X_Brows = "neutral"
                $ X_Eyes = "hypno"
        if Face == "shocked":
                $ X_Mouth = "neutral"
                $ X_Brows = "shocked"
                $ X_Eyes = "shocked"
                $ X_Psychic = 0
        if Face == "happy":
                $ X_Mouth = "happy"
                $ X_Brows = "happy"
                $ X_Eyes = "happy"        
                $ X_Psychic = 0
        if Face == "angry":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "happy"
                $ X_Psychic = 0
        return
        
# Wait/Sleep Cycle //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #Wait    
    
    
    
    
    
# Wait/Sleep Cycle //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #Wait
label Wait (Outfit = 1, Lights = 1):
    # If Outfit is 1, it changes her clothes to the scheduled default, otherwise it does not. 
    # If Lights is 1, it removes the blackout screen, otherwise it does not. 
    show blackscreen onlayer black 
    $ R_Spank = 0
    $ R_Addict += R_Addictionrate 
    $ K_Addict += K_Addictionrate
    $ E_Addict += E_Addictionrate
    $ newgirl["Mystique"].Addict += newgirl["Mystique"].Addictionrate
    call Checkout(1) from _call_Checkout
    $ P_XP = 3330 if P_XP > 3330 else P_XP
    $ R_XP = 3330 if R_XP > 3330 else R_XP
    $ K_XP = 3330 if K_XP > 3330 else K_XP
    $ E_XP = 3330 if E_XP > 3330 else E_XP
    
        
    if Time_Count < 3:  #not sleep time                                          
                $ Time_Count += 1
                $ R_Action += 1  
                $ K_Action += 1 
                $ E_Action += 1 
                $ newgirl["Mystique"].Action += 1
                
    # Things that happen when you sleep   
    else:                                                          
                $ del Party[:]
                
                #Setting the time/date
                $ Time_Count = 0   
                $ Day += 1
                if Weekday < 6:
                    $ Weekday += 1
                else:
                    $ Weekday = 0
                $ DayofWeek = Week[Weekday]
                
                if PunishmentX: #Event[3]:   
                        #If you're under punishment
                        $ P_Cash += int(P_Income / 2)
                        if PunishmentX == 1:
                            "Your punishment from Xavier has expired."
                        $ PunishmentX -= 1
                else:
                        #otherwise, you make money
                        $ P_Cash += P_Income             
                
                
        # Things about you when you sleep:
                $ P_Semen = P_Semen_Max    
                $ P_Rep = 0 if P_Rep < 0 else P_Rep 
                $ P_Rep += 10 if P_Rep < 800 else 0
                $ P_Rep = 1000 if P_Rep > 1000 else P_Rep     
                
                #Clearing colognes
                if "mandrill" in P_Traits:  
                        $ P_Traits.remove("mandrill")
                if "purple" in P_Traits:
                        $ P_Traits.remove("purple")  
                if "corruption" in P_Traits:
                        $ P_Traits.remove("corruption")  
                
                call Favorite_Actions from _call_Favorite_Actions # Sets the girl's favorite activities once per day
                        
                        
        # Things about Rogue when you sleep:  
                if R_Loc == "hold":
                        $ R_Loc = "bg rogue"      
                if R_Todo:
                        call Rogue_Todo from _call_Rogue_Todo
                $ R_Addict += R_Addictionrate
                $ R_Addict -= (3*R_Resistance)
                
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ R_Addictionrate -= 2
                        $ R_Addict -= 5
                elif R_Addictionrate:
                        $ R_Addictionrate -= R_Resistance
                   
                $ R_ForcedCount -= 1 if R_ForcedCount > 0 else 0 
                $ R_Action = R_MaxAction   
                
                $ R_Rep = 0 if R_Rep < 0 else R_Rep 
                $ R_Rep += 10 if R_Rep < 800 else 0
                $ R_Rep = 1000 if R_Rep > 1000 else R_Rep 
                $ R_Lust -= 5 if R_Lust >= 50 else 0
                
                $ R_Break[0] -= 1 if R_Break[0] > 0 else 0
                
                if "painted" not in R_DailyActions or "cleaned" not in R_DailyActions:   
                        $ del R_Spunk[:]  
                    
                if "lover" in R_Petnames and R_Love > 800:
                        $ R_Love += 10
                if "master" in R_Petnames and R_Obed > 600:
                        $ R_Obed += 10
                if "fuck buddy" in R_Petnames:
                        $ R_Inbt += 10        
                    
        # Things about Kitty when you sleep:
                if K_Loc == "hold":
                        $ K_Loc = "bg kitty"  
                if K_Todo:
                        call Kitty_Todo from _call_Kitty_Todo
                
                if "addict kitty" in P_Traits:
                        $ K_Addict += K_Addictionrate
                        $ K_Addict -= (3*K_Resistance)
                else:
                        $ K_Addict = 0
                        $ K_Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ K_Addictionrate -= 2
                        $ K_Addict -= 5
                elif K_Addictionrate:
                        $ K_Addictionrate -= K_Resistance
                    
                $ K_ForcedCount -= 1 if K_ForcedCount > 0 else 0
                $ K_Action = K_MaxAction    
                
                $ K_Rep = 0 if K_Rep < 0 else K_Rep 
                $ K_Rep += 10 if K_Rep < 800 else 0
                $ K_Rep = 1000 if K_Rep > 1000 else K_Rep 
                $ K_Lust -= 5 if K_Lust >= 50 else 0
                
                if "painted" not in K_DailyActions or "cleaned" not in K_DailyActions:   
                        $ del K_Spunk[:]  
                
                if "lover" in K_Petnames and K_Love > 800:
                        $ K_Love += 10
                if "master" in K_Petnames and K_Obed > 600:
                        $ K_Obed += 10
                if "fuck buddy" in K_Petnames:
                        $ K_Inbt += 10   
                        
        # Things about Emma when you sleep:
                if E_Loc == "hold":
                        $ E_Loc = "bg emma"  
                if E_Todo:
                        call Emma_Todo from _call_Emma_Todo
                
                if "addict emma" in P_Traits:
                        $ E_Addict += E_Addictionrate
                        $ E_Addict -= (3*E_Resistance)
                else:
                        $ E_Addict = 0
                        $ E_Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ E_Addictionrate -= 2
                        $ E_Addict -= 5
                elif E_Addictionrate:
                        $ E_Addictionrate -= E_Resistance
                    
                $ E_ForcedCount -= 1 if E_ForcedCount > 0 else 0
                $ E_Action = E_MaxAction    
                
                $ E_Rep = 0 if E_Rep < 0 else E_Rep 
                $ E_Rep += 10 if E_Rep < 800 else 0
                $ E_Rep = 1000 if E_Rep > 1000 else E_Rep 
                $ E_Lust -= 5 if E_Lust >= 50 else 0
                
                if "painted" not in E_DailyActions or "cleaned" not in E_DailyActions:   
                        $ del E_Spunk[:]  
                
                if "lover" in E_Petnames and E_Love > 800:
                        $ E_Love += 10
                if "master" in E_Petnames and E_Obed > 600:
                        $ E_Obed += 10
                if "fuck buddy" in E_Petnames:
                        $ E_Inbt += 10      

        # Things about Mystique when you sleep:
                if newgirl["Mystique"].Loc == "hold":
                        $ newgirl["Mystique"].Loc = "bg Mystique"  
                if newgirl["Mystique"].Todo:
                        call Mystique_Todo from _call_Mystique_Todo
                
                if "addict mystique" in P_Traits:
                        $ newgirl["Mystique"].Addict += newgirl["Mystique"].Addictionrate
                        $ newgirl["Mystique"].Addict -= (3*newgirl["Mystique"].Resistance)
                else:
                        $ newgirl["Mystique"].Addict = 0
                        $ newgirl["Mystique"].Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ newgirl["Mystique"].Addictionrate -= 2
                        $ newgirl["Mystique"].Addict -= 5
                elif newgirl["Mystique"].Addictionrate:
                        $ newgirl["Mystique"].Addictionrate -= newgirl["Mystique"].Resistance
                    
                $ newgirl["Mystique"].ForcedCount -= 1 if newgirl["Mystique"].ForcedCount > 0 else 0
                $ newgirl["Mystique"].Action = newgirl["Mystique"].MaxAction    
                
                $ newgirl["Mystique"].Rep = 0 if newgirl["Mystique"].Rep < 0 else newgirl["Mystique"].Rep 
                $ newgirl["Mystique"].Rep += 10 if newgirl["Mystique"].Rep < 800 else 0
                $ newgirl["Mystique"].Rep = 1000 if newgirl["Mystique"].Rep > 1000 else newgirl["Mystique"].Rep 
                $ newgirl["Mystique"].Lust -= 5 if newgirl["Mystique"].Lust >= 50 else 0
                
                if "painted" not in newgirl["Mystique"].DailyActions or "cleaned" not in newgirl["Mystique"].DailyActions:   
                        $ del newgirl["Mystique"].Spunk[:]  
                
                if "lover" in newgirl["Mystique"].Petnames and newgirl["Mystique"].Love > 800:
                        $ newgirl["Mystique"].Love += 10
                if "master" in newgirl["Mystique"].Petnames and newgirl["Mystique"].Obed > 600:
                        $ newgirl["Mystique"].Obed += 10
                if "fuck buddy" in newgirl["Mystique"].Petnames:
                        $ newgirl["Mystique"].Inbt += 10          
    #End of things when you sleep
                    
        
    # Things that happen every time you wait   
                                                        
    #Things that are about you:
    $ P_Semen += 1    
    $ MultiAction = 1 
    $ P_Focus = 0    
    $ Situation = 0      
    $ Current_Time = Time_Options[(Time_Count)]    
    $ Round = 100
    $ R_OCount = 0    
    $ K_OCount = 0     
    $ E_OCount = 0    
    $ newgirl["Mystique"].OCount = 0    
    call Taboo_Level from _call_Taboo_Level  
    call GirlWaitAttract from _call_GirlWaitAttract #checks girls attraction based on who's in the room
    
    #Things that are about Rogue:      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if R_Lust >= 70 and R_Loc != bg_current:
        $ R_Lust = 25
    
    #Resets her flirt  options
    $ R_Chat[5] = 0  
    #Resets her addiction fix attempts
    if R_Event[3]:
        $ R_Event[3] -= 1               
    
    $ R_Forced = 0
    if R_Loc == "bg classroom" or R_Loc == "bg dangerroom" :
            $ R_XP += 10    
    elif R_Loc == "bg showerroom": 
            call Remove_Girl("Rogue") from _call_Remove_Girl_4
          
    #Appearance clean-up
    $ R_Blush = 0
    $ R_Water = 0
    $ R_Held = 0 
    
    #Reduced addiction
    $ R_Addictionrate -= R_Resistance if R_Addictionrate > 3 else 0 #else R_Addictionrate?
    $ R_Addictionrate = 0 if R_Addictionrate < 0 else R_Addictionrate    
        
    #Adjusts shame rate
    if R_Taboo and R_Shame:
            if R_Loc == "bg dangerroom":            
                    $ R_Shame -= 10 if R_Shame >=10 else R_Shame
            $ Count = int((R_Taboo * R_Shame) / 200)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, Count)         
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, Count) 
            $ R_Rep -= Count
        
#    call Rogue_Schedule #moved down because of scehdule/actions thing
#    call Stat_Checks    
#    call RogueOutfit 
    
    #subtracts R_Love by 5* the number of recent unsatisfieds
    $ R_Love -= 5*(Action_Check("Rogue","recent","unsatisfied")) 
    
    # Clears out recent and daily actions    
    $ del P_RecentActions[:]                            
    if Time_Count == 0: 
            $ del P_DailyActions[:]
    
    $ del R_RecentActions[:]                            
    if Time_Count == 0: 
            $ del R_DailyActions[:]
            
    call Rogue_Schedule from _call_Rogue_Schedule_1
    call Stat_Checks from _call_Stat_Checks    
    if Outfit:
            call RogueOutfit(R_OutfitDay) from _call_RogueOutfit_1
    
    #end Rogue hourly actions
        
        
    #Things that are about Kitty:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
    if K_Lust >= 70 and K_Loc != bg_current:
        $ K_Lust = 25
            
    #Resets her flirt  options
    $ K_Chat[5] = 0 
    
    #Resets her addiction fix attempts
    if K_Event[3]:
        $ K_Event[3] -= 1               
    
    $ K_Forced = 0
    if K_Loc == "bg classroom" or K_Loc == "bg dangerroom" :
            $ K_XP += 10    
    elif K_Loc == "bg showerroom":
            call Remove_Girl("Kitty") from _call_Remove_Girl_5
        
    #Appearance clean-up
    $ K_Blush = 0
    $ K_Water = 0
    $ K_Held = 0 
    
    # Reduce addiction
    $ K_Addictionrate -= K_Resistance if K_Addictionrate > 3 else 0    
    $ K_Addictionrate = 0 if K_Addictionrate < 0 else K_Addictionrate    
    
    #Adjusts shame rate
    if K_Taboo and K_Shame:
            if K_Loc == "bg dangerroom":            
                    $ K_Shame -= 10 if K_Shame >=10 else K_Shame
            $ Count = int((K_Taboo * K_Shame) / 200)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, Count)         
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, Count) 
            $ K_Rep -= Count
    
    $ K_Love -= 5*(Action_Check("Kitty","recent","unsatisfied")) #subtracts K_Love by 5* the number of recent unsatisfieds
    
    # Clears out recent and daily actions
    $ del K_RecentActions[:]                            # Clears out recent and daily actions
    if Time_Count == 0: 
        $ del K_DailyActions[:]
        
    call Kitty_Schedule from _call_Kitty_Schedule_1
    call Stat_Checks from _call_Stat_Checks_1    
    if Outfit:
            call KittyOutfit(K_OutfitDay) from _call_KittyOutfit_1
    #end Kitty hourly actions
        
    #Things that are about Emma:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
    if E_Lust >= 70 and E_Loc != bg_current:
        $ E_Lust = 25
            
    #Resets her flirt  options
    $ E_Chat[5] = 0 
    
    #Resets her addiction fix attempts
    if E_Event[3]:
        $ E_Event[3] -= 1               
    
    $ E_Forced = 0
    if E_Loc == "bg teacher" and "bg classroom" in (bg_current, R_Loc, K_Loc):
            $ E_XP += 10 
    if E_Loc == "bg classroom" or E_Loc == "bg dangerroom" :
            $ E_XP += 10    
    elif E_Loc == "bg showerroom":
            call Remove_Girl("Emma") from _call_Remove_Girl_6
        
    #Appearance clean-up
    $ E_Blush = 0
    $ E_Water = 0
    $ E_Held = 0 
    
    # Reduce addiction
    $ E_Addictionrate -= E_Resistance if E_Addictionrate > 3 else 0    
    $ E_Addictionrate = 0 if E_Addictionrate < 0 else E_Addictionrate    
    
    #Adjusts shame rate
    if E_Taboo and E_Shame:
            if E_Loc == "bg dangerroom":            
                    $ E_Shame -= 10 if E_Shame >=10 else E_Shame
            $ Count = int((E_Taboo * E_Shame) / 200)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, Count)         
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, Count) 
            $ E_Rep -= int(1.5 * Count)
    
    $ E_Love -= 5*(Action_Check("Emma","recent","unsatisfied")) #subtracts E_Love by 5* the number of recent unsatisfieds
    
    # Clears out recent and daily actions
    $ del E_RecentActions[:]                            # Clears out recent and daily actions
    if Time_Count == 0: 
        $ del E_DailyActions[:]
        
    call Emma_Schedule from _call_Emma_Schedule_1
    call Stat_Checks from _call_Stat_Checks_2
    if Outfit:
            call EmmaOutfit(E_OutfitDay) from _call_EmmaOutfit_1
    #end Emma hourly actions

    #Things that are about Mystique:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
    if newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].Loc != bg_current:
        $ newgirl["Mystique"].Lust = 25
            
    #Resets her flirt  options
    $ newgirl["Mystique"].Chat[5] = 0 
    
    #Resets her addiction fix attempts
    if newgirl["Mystique"].Event[3]:
        $ newgirl["Mystique"].Event[3] -= 1               
    
    $ newgirl["Mystique"].Forced = 0
    if newgirl["Mystique"].Loc == "bg teacher" and "bg classroom" in (bg_current, R_Loc, K_Loc):
            $ newgirl["Mystique"].XP += 10 
    if newgirl["Mystique"].Loc == "bg classroom" or newgirl["Mystique"].Loc == "bg dangerroom" :
            $ newgirl["Mystique"].XP += 10    
    elif newgirl["Mystique"].Loc == "bg showerroom":
            call Remove_Girl("Mystique") from _call_Remove_Girl_7
        
    #Appearance clean-up
    $ newgirl["Mystique"].Blush = 0
    $ newgirl["Mystique"].Water = 0
    $ newgirl["Mystique"].Held = 0 
    
    # Reduce addiction
    $ newgirl["Mystique"].Addictionrate -= newgirl["Mystique"].Resistance if newgirl["Mystique"].Addictionrate > 3 else 0    
    $ newgirl["Mystique"].Addictionrate = 0 if newgirl["Mystique"].Addictionrate < 0 else newgirl["Mystique"].Addictionrate    
    
    #Adjusts shame rate
    if newgirl["Mystique"].Taboo and newgirl["Mystique"].Shame:
            if newgirl["Mystique"].Loc == "bg dangerroom":            
                    $ newgirl["Mystique"].Shame -= 10 if newgirl["Mystique"].Shame >=10 else newgirl["Mystique"].Shame
            $ Count = int((newgirl["Mystique"].Taboo * newgirl["Mystique"].Shame) / 200)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, Count)         
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, Count) 
            $ newgirl["Mystique"].Rep -= int(1.5 * Count)
    
    $ newgirl["Mystique"].Love -= 5*(Action_Check("Mystique","recent","unsatisfied")) #subtracts newgirl["Mystique"].Love by 5* the number of recent unsatisfieds
    
    # Clears out recent and daily actions
    $ del newgirl["Mystique"].RecentActions[:]                            # Clears out recent and daily actions
    if Time_Count == 0: 
        $ del newgirl["Mystique"].DailyActions[:]
        
    call Mystique_Schedule from _call_Mystique_Schedule_1
    call Stat_Checks from _call_Stat_Checks_3    
    if Outfit:
            call MystiqueOutfit(newgirl["Mystique"].OutfitDay) from _call_MystiqueOutfit_1
    #end Mystique hourly actions
    
    #end wait items: 
    call Faces from _call_Faces #Sets girls faces based on their emotions
    call Checkout from _call_Checkout_1
    if Current_Time != "Night":        
            hide NightMask onlayer nightmask  
    if Lights:
            hide blackscreen onlayer black 
    
    return


# End Wait/Sleep Cycle ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
    
    
    
    
    
    
# //////////////////////////////////////////////////////////////////                                                            End Wait/Sleep Cycle 



label Taboo_Level:
        #Set your taboo level
        if bg_current in ("bg player", "bg rogue", "bg kitty", "bg emma"):                     
                    $ Taboo = 0
        elif bg_current == "bg classroom":
                if Current_Time == "Night":
                    $ Taboo = 0
                elif Current_Time == "Evening" or Weekday >= 5:
                    $ Taboo = 30
                    if "locked" in E_RecentActions:
                        if bg_current == R_Loc and E_LikeRogue <= 800:
                            $ E_Taboo = 20
                            $ Taboo = 20     
                        elif bg_current == K_Loc and E_LikeKitty <= 800:
                            $ E_Taboo = 20
                            $ Taboo = 20          
                        else:
                            $ Taboo = 0
                else:
                    $ Taboo = 40
        elif bg_current == "bg dangerroom":
                if Current_Time == "Night":
                    $ Taboo = 0
                else:
                    $ Taboo = 40

        elif bg_current == "bg pool":
                if Current_Time == "Night":
                    $ Taboo = 0
                else:
                    $ Taboo = 40

        elif bg_current == "bg field":
                if Current_Time == "Night":
                    $ Taboo = 0
                else:
                    $ Taboo = 40

        elif bg_current == "bg campus":
                if Current_Time == "Night":
                    $ Taboo = 20
                else:
                    $ Taboo = 40
        elif bg_current == "bg showerroom":        
                    $ Taboo = 20    
        else:
                    $ Taboo = 0
                    
        #Set Rogue's Taboo level
        if R_Loc in ("bg player", "bg rogue", "bg kitty", "bg emma"):  
                    if R_Loc == K_Loc and R_LikeKitty <= 800:
                        $ R_Taboo = 20
                        $ Taboo = 20    
                    elif R_Loc == E_Loc and R_LikeEmma <= 800:
                        $ R_Taboo = 20
                        $ Taboo = 20                       
                    else:
                        $ R_Taboo = 0
        elif R_Loc == "bg classroom":
                if Current_Time == "Night" or "locked" in E_RecentActions:
                    $ R_Taboo = 0
                elif Current_Time == "Evening" or Weekday >= 5:
                    $ R_Taboo = 30
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ R_Taboo = 0
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg pool":
                if Current_Time == "Night":
                    $ R_Taboo = 0
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg field":
                if Current_Time == "Night":
                    $ R_Taboo = 0
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg campus":
                if Current_Time == "Night":
                    $ R_Taboo = 20
                else:
                    $ R_Taboo = 40
        elif R_Loc == "bg showerroom":        
                    $ R_Taboo = 20    
        else:
                    $ R_Taboo = 0    
            
        #Set Kitty's Taboo level 
        if K_Loc in ("bg player", "bg rogue", "bg kitty", "bg emma"):  
                    if K_Loc == R_Loc and K_LikeRogue <= 800:
                        $ K_Taboo = 20
                        $ Taboo = 20  
                    elif K_Loc == E_Loc and K_LikeEmma <= 800:
                        $ K_Taboo = 20
                        $ Taboo = 20   
                    else:
                        $ K_Taboo = 0
        elif K_Loc == "bg classroom":
                if Current_Time == "Night" or "locked" in E_RecentActions:
                    $ K_Taboo = 0
                elif Current_Time == "Evening" or Weekday >= 5:
                    $ K_Taboo = 30
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ K_Taboo = 0
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg pool":
                if Current_Time == "Night":
                    $ K_Taboo = 0
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg field":
                if Current_Time == "Night":
                    $ K_Taboo = 0
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg campus":
                if Current_Time == "Night":
                    $ K_Taboo = 20
                else:
                    $ K_Taboo = 40
        elif K_Loc == "bg showerroom":        
                    $ K_Taboo = 20    
        else:
                    $ K_Taboo = 0   
                    
        #Set Emma's Taboo level 
        if E_Loc in ("bg player", "bg rogue", "bg kitty", "bg emma"):  
                    if E_Loc == R_Loc and E_LikeRogue <= 800:
                        $ E_Taboo = 20
                        $ Taboo = 20     
                    elif E_Loc == K_Loc and E_LikeKitty <= 800:
                        $ E_Taboo = 20
                        $ Taboo = 20                       
                    else:
                        $ E_Taboo = 0
        elif E_Loc == "bg classroom":
                if Current_Time == "Night" or "locked" in E_RecentActions:
                    $ E_Taboo = 0
                elif (Current_Time == "Evening" or Weekday >= 5):
                    $ E_Taboo = 30
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg dangerroom":
                if Current_Time == "Night":
                    $ E_Taboo = 0
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg pool":
                if Current_Time == "Night":
                    $ E_Taboo = 0
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg field":
                if Current_Time == "Night":
                    $ E_Taboo = 0
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg campus":
                if Current_Time == "Night":
                    $ E_Taboo = 20
                else:
                    $ E_Taboo = 40
        elif E_Loc == "bg showerroom":        
                    $ E_Taboo = 20    
        else:
                    $ E_Taboo = 0   
        return
        
        #end taboo level
            

# Overrun checking //////////////////////////////////////////////////////////////////////
label Checkout(Total = 0):    
            call VersionNumber from _call_VersionNumber
        #Rogue
            $ R_Love = 1000 if R_Love > 1000 else R_Love    
            $ R_Obed = 1000 if R_Obed > 1000 else R_Obed    
            $ R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt    
            $ R_Lust = 99 if R_Lust > 99 else R_Lust   
                
            $ R_Love = 0 if R_Love < 0 else R_Love    
            $ R_Obed = 0 if R_Obed < 0 else R_Obed    
            $ R_Inbt = 0 if R_Inbt < 0 else R_Inbt    
            $ R_Lust = 0 if R_Lust < 0 else R_Lust   
                        
            $ R_Action = R_MaxAction if R_Action > R_MaxAction else R_Action  
            $ R_Action = 0 if R_Action < 0 else R_Action  
            
            $ R_Addict = 100 if R_Addict > 100 else R_Addict  
            $ R_Addict = 0 if R_Addict < 0 else R_Addict  
            $ R_Addictionrate = 10 if R_Addictionrate > 10 else R_Addictionrate  
            $ R_Addictionrate = 0 if R_Addictionrate < 0 else R_Addictionrate 
            
            $ R_LikeKitty = 1000 if R_LikeKitty > 1000 else R_LikeKitty     
            $ R_LikeKitty = 0 if R_LikeKitty < 0 else R_LikeKitty 
            $ R_LikeEmma = 1000 if R_LikeEmma > 1000 else R_LikeEmma     
            $ R_LikeEmma = 0 if R_LikeEmma < 0 else R_LikeEmma 
            if R_Forced and R_ForcedCount < 10:
                $ R_ForcedCount += 1
            
        #Kitty
            $ K_Love = 1000 if K_Love > 1000 else K_Love    
            $ K_Obed = 1000 if K_Obed > 1000 else K_Obed    
            $ K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt    
            $ K_Lust = 99 if K_Lust > 99 else K_Lust   
                
            $ K_Love = 0 if K_Love < 0 else K_Love    
            $ K_Obed = 0 if K_Obed < 0 else K_Obed    
            $ K_Inbt = 0 if K_Inbt < 0 else K_Inbt    
            $ K_Lust = 0 if K_Lust < 0 else K_Lust   
                        
            $ K_Action = K_MaxAction if K_Action > K_MaxAction else K_Action  
            $ K_Action = 0 if K_Action < 0 else K_Action  
            
            $ K_Addict = 100 if K_Addict > 100 else K_Addict  
            $ K_Addict = 0 if K_Addict < 0 else K_Addict  
            $ K_Addictionrate = 10 if K_Addictionrate > 10 else K_Addictionrate  
            $ K_Addictionrate = 0 if K_Addictionrate < 0 else K_Addictionrate  
            
            $ K_LikeRogue = 1000 if K_LikeRogue > 1000 else K_LikeRogue     
            $ K_LikeRogue = 0 if K_LikeRogue < 0 else K_LikeRogue 
            $ K_LikeEmma = 1000 if K_LikeEmma > 1000 else K_LikeEmma     
            $ K_LikeEmma = 0 if K_LikeEmma < 0 else K_LikeEmma 
            if K_Forced and K_ForcedCount < 10:
                $ K_ForcedCount += 1

        #Emma
            $ E_Love = 1000 if E_Love > 1000 else E_Love    
            $ E_Obed = 1000 if E_Obed > 1000 else E_Obed    
            $ E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt    
            $ E_Lust = 99 if E_Lust > 99 else E_Lust   
                
            $ E_Love = 0 if E_Love < 0 else E_Love    
            $ E_Obed = 0 if E_Obed < 0 else E_Obed    
            $ E_Inbt = 0 if E_Inbt < 0 else E_Inbt    
            $ E_Lust = 0 if E_Lust < 0 else E_Lust   
                        
            $ E_Action = E_MaxAction if E_Action > E_MaxAction else E_Action  
            $ E_Action = 0 if E_Action < 0 else E_Action  
            
            $ E_Addict = 100 if E_Addict > 100 else E_Addict  
            $ E_Addict = 0 if E_Addict < 0 else E_Addict  
            $ E_Addictionrate = 10 if E_Addictionrate > 10 else E_Addictionrate  
            $ E_Addictionrate = 0 if E_Addictionrate < 0 else E_Addictionrate  
            
            $ E_LikeRogue = 1000 if E_LikeRogue > 1000 else E_LikeRogue     
            $ E_LikeRogue = 0 if E_LikeRogue < 0 else E_LikeRogue 
            $ E_LikeKitty = 1000 if E_LikeKitty > 1000 else E_LikeKitty     
            $ E_LikeKitty = 0 if E_LikeKitty < 0 else E_LikeKitty 
            if E_Forced and E_ForcedCount < 10:
                $ E_ForcedCount += 1
                
        #Player
            $ P_Focus = 99 if P_Focus > 99 else P_Focus
            $ P_Focus = 0 if P_Focus < 0 else P_Focus
            $ P_Semen = P_Semen_Max if P_Semen > P_Semen_Max else P_Semen  
            $ P_Semen = 0 if P_Semen < 0 else P_Semen   
            
            if Total:
                    call DrainWord("Player","cockout") from _call_DrainWord
                    call DrainWord("Player","nude") from _call_DrainWord_1
#                    $ LesFlag = 0
                    $ Trigger = 0        
                    $ Trigger2 = 0
                    $ Trigger3 = 0
                    $ Trigger4 = 0
                    $ Trigger5 = 0
                    $ Partner = 0 
                    $ P_FocusX = 0
            return

# end Overrun checking //////////////////////////////////////////////////////////////////////

# Scene Setting ///////////////////////////////////////////////////////////////////////

transform SpriteLoc(Loc = StageRight, LocY = 50):  #This puts the sprite at a location relative to the sent variable
        pos (Loc,LocY)
    

label Set_The_Scene(Chr = 1, Entry = 0, Dress = 1):
        # If Chr, then display the characters in the room
        # If Entry, then show the "entry" version of a room, such as a closed door, does not display characters
        # If Dress, then check whether the character is underdressed when displaying her
        
        show blackscreen onlayer black 
        
        if Entry:
            $ Chr = 0
        call Display_Background(Entry) from _call_Display_Background 
        
        if Current_Time == 'Night':
                show NightMask onlayer nightmask
        else:          
                hide NightMask onlayer nightmask  
                
        scene   #Clears content
                
        if Chr:
                call Present_Check from _call_Present_Check_2  #culls out Party to 2, sets location to bg_current, removes extra girls, sets Focus to a girl in the room   
                
                $ Grils = 0
                $ TheGirls = []
                # "Testt"
                if "Rogue" in Party: 
                    $ R_Loc = bg_current
                elif R_Loc == bg_current:       
                                $ Grils += 1
                                $ TheGirls.append("Rogue")
                if "Kitty" in Party: 
                    $ K_Loc = bg_current
                elif K_Loc == bg_current:       
                                $ Grils += 1
                                $ TheGirls.append("Kitty")
                if "Emma" in Party: 
                    $ E_Loc = bg_current
                elif E_Loc == bg_current:       
                                $ Grils += 1
                                $ TheGirls.append("Emma")

                if "Mystique" in Party: 
                    $ newgirl["Mystique"].Loc = bg_current
                elif newgirl["Mystique"].Loc == bg_current:       
                                $ Grils += 1
                                $ TheGirls.append("Mystique")

                if "Laura" in Party: 
                    $ newgirl["Laura"].Loc = bg_current
                elif newgirl["Laura"].Loc == bg_current:       
                                $ Grils += 1
                                $ TheGirls.append("Laura")
                # "[Grils]"
                # "[TheGirls] 1"

                if Ch_Focus == "Kitty" and K_Loc == bg_current: 
                        $ K_SpriteLoc = StageCenter
                        $ KittyLayer = 100
                        if "Kitty" in TheGirls:
                            $ TheGirls.remove("Kitty")

                elif Ch_Focus == "Emma" and E_Loc == bg_current:  
                        $ E_SpriteLoc = StageCenter
                        $ EmmaLayer = 100
                        if "Emma" in TheGirls:
                            $ TheGirls.remove("Emma")

                elif Ch_Focus == "Rogue" and R_Loc == bg_current:   
                        $ R_SpriteLoc = StageCenter
                        $ RogueLayer = 100
                        if "Rogue" in TheGirls:
                            $ TheGirls.remove("Rogue")
                
                elif Ch_Focus == "Mystique" and newgirl["Mystique"].Loc == bg_current: 
                        $ newgirl["Mystique"].SpriteLoc = StageCenter
                        $ newgirl["Mystique"].GirlLayer = 100 
                        if "Mystique" in TheGirls:
                            $ TheGirls.remove("Mystique")

                elif Ch_Focus == "Laura" and newgirl["Laura"].Loc == bg_current: 
                        $ newgirl["Laura"].SpriteLoc = StageCenter
                        $ newgirl["Laura"].GirlLayer = 100 
                        if "Laura" in TheGirls:
                            $ TheGirls.remove("Laura")

                # "[TheGirls] 2"

                #$ renpy.random.shuffle(TheGirls)

                # "[TheGirls] 3"
                if TheGirls:
                    # "[TheGirls]"
                    if TheGirls[0] == "Kitty" and K_Loc == bg_current:
                        $ K_SpriteLoc = StageRight
                        $ KittyLayer = 70
                    elif len(TheGirls) > 1:
                        if TheGirls[1] == "Kitty" and K_Loc == bg_current:
                            $ K_SpriteLoc = StageFarRight
                            $ KittyLayer = 50
    
                    if TheGirls[0] == "Rogue" and R_Loc == bg_current:
                        $ R_SpriteLoc = StageRight
                        $ RogueLayer = 70
                    elif len(TheGirls) > 1:
                        if TheGirls[1] == "Rogue" and R_Loc == bg_current:
                            $ R_SpriteLoc = StageFarRight
                            $ RogueLayer = 50
    
                    if TheGirls[0] == "Emma" and E_Loc == bg_current:
                        $ E_SpriteLoc = StageRight
                        $ EmmaLayer = 70
                    elif len(TheGirls) > 1:
                        if TheGirls[1] == "Emma" and E_Loc == bg_current:
                            $ E_SpriteLoc = StageFarRight
                            $ EmmaLayer = 50
    
                    if TheGirls[0] == "Mystique" and newgirl["Mystique"].Loc == bg_current:
                        $ newgirl["Mystique"].SpriteLoc = StageRight
                        $ newgirl["Mystique"].GirlLayer = 70
                    elif len(TheGirls) > 1:
                        if TheGirls[1] == "Mystique" and newgirl["Mystique"].Loc == bg_current:
                            $ newgirl["Mystique"].SpriteLoc = StageFarRight
                            $ newgirl["Mystique"].GirlLayer = 50

                    if TheGirls[0] == "Laura" and newgirl["Laura"].Loc == bg_current:
                        $ newgirl["Laura"].SpriteLoc = StageRight
                        $ newgirl["Laura"].GirlLayer = 70
                    elif len(TheGirls) > 1:
                        if TheGirls[1] == "Laura" and newgirl["Laura"].Loc == bg_current:
                            $ newgirl["Laura"].SpriteLoc = StageFarRight
                            $ newgirl["Laura"].GirlLayer = 50
    
                call Display_Laura(Dress) from _call_Display_Laura
                call Display_Mystique(Dress) from _call_Display_Mystique
                call Display_Emma(Dress) from _call_Display_Emma
                call Display_Kitty(Dress) from _call_Display_Kitty
                call Display_Rogue(Dress) from _call_Display_Rogue    

                # if Grils == 3:

                #     if Ch_Focus == "Kitty" and K_Loc == bg_current: 
                #             $ R_SpriteLoc = StageRight
                #             $ E_SpriteLoc = StageFarRight   
                #             $ newgirl["Mystique"].SpriteLoc = StageFarRight
                #             $ RogueLayer = 75
                #             $ EmmaLayer = 50
                #             $ newgirl["Mystique"].GirlLayer = 50
                #             call Display_Kitty(Dress)
                #             call Display_Rogue(Dress)
                #             call Display_Emma(Dress)
                #             call Display_Mystique(Dress)

                #     elif Ch_Focus == "Emma" and E_Loc == bg_current:  
                #             $ E_SpriteLoc = StageCenter
                #             $ R_SpriteLoc = StageRight
                #             $ K_SpriteLoc = StageFarRight  
                #             $ newgirl["Mystique"].SpriteLoc = StageFarRight
                #             $ EmmaLayer = 100
                #             $ RogueLayer = 75
                #             $ KittyLayer = 50
                #             $ newgirl["Mystique"].GirlLayer = 50
                #             call Display_Emma(Dress)
                #             call Display_Rogue(Dress)
                #             call Display_Kitty(Dress)
                #             call Display_Mystique(Dress)

                #     elif Ch_Focus == "Rogue" and R_Loc == bg_current:   
                #             $ R_SpriteLoc = StageCenter
                #             $ E_SpriteLoc = StageRight
                #             $ K_SpriteLoc = StageFarRight
                #             $ newgirl["Mystique"].SpriteLoc = StageFarRight
                #             $ RogueLayer = 100
                #             $ EmmaLayer = 75
                #             $ KittyLayer = 50
                #             $ newgirl["Mystique"].GirlLayer = 50
                #             call Display_Kitty(Dress)
                #             call Display_Emma(Dress)
                #             call Display_Rogue(Dress)
                #             call Display_Mystique(Dress)
                    
                #     elif Ch_Focus == "Mystique" and newgirl["Mystique"].Loc == bg_current:   
                #             $ newgirl["Mystique"].SpriteLoc = StageCenter
                #             $ E_SpriteLoc = StageRight
                #             $ K_SpriteLoc = StageFarRight
                #             $ R_SpriteLoc = StageFarRight
                #             $ newgirl["Mystique"].GirlLayer = 100
                #             $ EmmaLayer = 75
                #             $ KittyLayer = 50
                #             $ RogueLayer = 50
                #             call Display_Mystique(Dress)
                #             call Display_Emma(Dress)
                #             call Display_Kitty(Dress)
                #             call Display_Rogue(Dress)

                # else:

                #     if Ch_Focus == "Kitty" and K_Loc == bg_current: 
                #             $ K_SpriteLoc = StageCenter
                #             $ E_SpriteLoc = StageRight   
                #             $ R_SpriteLoc = StageRight
                #             $ newgirl["Mystique"].SpriteLoc = StageRight
                #             $ KittyLayer = 100
                #             $ EmmaLayer = 75
                #             $ RogueLayer = 75
                #             $ newgirl["Mystique"].GirlLayer = 75
                #             call Display_Kitty(Dress)
                #             call Display_Emma(Dress)
                #             call Display_Rogue(Dress)
                #             call Display_Mystique(Dress)

                #     elif Ch_Focus == "Emma" and E_Loc == bg_current:  
                #             $ E_SpriteLoc = StageCenter
                #             $ K_SpriteLoc = StageRight  
                #             $ R_SpriteLoc = StageRight
                #             $ newgirl["Mystique"].SpriteLoc = StageRight
                #             $ EmmaLayer = 100
                #             $ KittyLayer = 75
                #             $ RogueLayer = 75
                #             $ newgirl["Mystique"].GirlLayer = 75
                #             call Display_Emma(Dress)
                #             call Display_Kitty(Dress)
                #             call Display_Rogue(Dress)
                #             call Display_Mystique(Dress)

                #     elif Ch_Focus == "Rogue" and R_Loc == bg_current:   
                #             $ R_SpriteLoc = StageCenter
                #             $ K_SpriteLoc = StageRight
                #             $ E_SpriteLoc = StageRight
                #             $ newgirl["Mystique"].SpriteLoc = StageRight
                #             $ RogueLayer = 100
                #             $ KittyLayer = 75
                #             $ EmmaLayer = 75
                #             $ newgirl["Mystique"].GirlLayer = 75
                #             call Display_Rogue(Dress)
                #             call Display_Kitty(Dress)
                #             call Display_Emma(Dress)
                #             call Display_Mystique(Dress)

                #     elif Ch_Focus == "Mystique" and newgirl["Mystique"].Loc == bg_current:   
                #             $ newgirl["Mystique"].SpriteLoc = StageCenter
                #             $ E_SpriteLoc = StageRight
                #             $ K_SpriteLoc = StageRight
                #             $ R_SpriteLoc = StageRight
                #             $ newgirl["Mystique"].GirlLayer = 100
                #             $ EmmaLayer = 75
                #             $ KittyLayer = 75
                #             $ RogueLayer = 75
                #             call Display_Mystique(Dress)
                #             call Display_Emma(Dress)
                #             call Display_Kitty(Dress)
                #             call Display_Rogue(Dress)

                if bg_current == "bg study" and Current_Time != "Night":   
                        show Professor at SpriteLoc(StageLeft) zorder 25    
                if bg_current == "bg classroom" and E_Loc == "bg teacher":  
                        call EmmaOutfit(Changed=1) from _call_EmmaOutfit_2
#                        show Emma_At_Podium onlayer backdrop
        
        if not renpy.showing("Chibi_UI") and "cockout" in P_RecentActions:
                    show Chibi_UI
                    
        hide blackscreen onlayer black
        return
# End primary Display function <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<
        
        
        
label Shift_Focus(Chr = "Rogue", Second = 0):       #When used like Shift_Focus("Kitty"), changes the focus character and relative default positions
        if Chr == "Kitty":
                if K_Loc == bg_current:
                        #If Kitty is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                            if E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                            elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif E_Loc == bg_current:
                            #if Emma is there, shift her to third position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                            if newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageRight
                                $ newgirl["Mystique"].GirlLayer = 75
                        #and move Kitty to first position
                        $ K_SpriteLoc = StageCenter
                        $ KittyLayer = 100
                        
                if Ch_Focus == "Kitty": 
                    #If Kitty was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Kitty": 
                    #If Kitty was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Kitty"
        elif Chr == "Emma":
                if E_Loc == bg_current:
                        #If Emma is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                            if K_Loc == bg_current:
                                #if Kitty is there, shift her to third position
                                $ K_SpriteLoc = StageFarRight
                                $ KittyLayer = 50
                            elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                            if newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageRight
                                $ newgirl["Mystique"].GirlLayer = 75
                        #and move Emma to first position
                        $ E_SpriteLoc = StageCenter
                        $ EmmaLayer = 100
                        
                if Ch_Focus == "Emma": 
                    #If Emma was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Kitty": 
                    #If Emma was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Emma"
        elif Chr == "Rogue":
                if R_Loc == bg_current:
                        #If Rogue is where you're at. . .
                        if K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                            if E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                            elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif E_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                            if newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageRight
                                $ newgirl["Mystique"].GirlLayer = 75
                        #and move Rogue to first position
                        $ R_SpriteLoc = StageCenter
                        $ RogueLayer = 100
                        
                if Ch_Focus == "Rogue": 
                    #If Rogue was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Rogue": 
                    #If Rogue was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Rogue"
        else: #if Chr == newgirl:
                if newgirl[Chr].Loc == bg_current:
                        #If Mystique is where you're at. . .
                        if K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                            if E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                            elif R_Loc == bg_current:
                                #if Rogue is there, shift her to third position
                                $ R_SpriteLoc = StageFarRight
                                $ RogueLayer = 50
                        elif E_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                            if R_Loc == bg_current:
                                #if Rogue is there, shift her to third position
                                $ R_SpriteLoc = StageFarRight
                                $ RogueLayer = 50
                        elif R_Loc == bg_current:
                                #if Rogue is there, shift her to third position
                                $ R_SpriteLoc = StageRight
                                $ RogueLayer = 75
                        #and move Mystique to first position
                        $ newgirl[Chr].SpriteLoc = StageCenter
                        $ newgirl[Chr].GirlLayer = 100
                        
                if Ch_Focus == Chr: 
                    #If Mystique was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == Chr: 
                    #If Mystique was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = Chr
        $ renpy.restart_interaction() 
        return

label Change_Focus(Chr = "Rogue", Second = 0, Dress = 1):       #When used like Shift_Focus("Kitty"), changes the focus character and relative default positions
        if Chr == "Kitty":
                if K_Loc == bg_current:
                        #If Kitty is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                            if E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                            elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageRight
                                $ EmmaLayer = 75
                                if newgirl["Mystique"].Loc == bg_current:
                                    #if Mystique is there, shift her to third position
                                    $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                    $ newgirl["Mystique"].GirlLayer = 50
                        elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageRight
                                $ newgirl["Mystique"].GirlLayer = 75
                        #and move Kitty to first position
                        $ K_SpriteLoc = StageCenter
                        $ KittyLayer = 100
                        call Display_Emma(Dress) from _call_Display_Emma_1
                        call Display_Kitty(Dress) from _call_Display_Kitty_1
                        call Display_Rogue(Dress) from _call_Display_Rogue_1
                        call Display_Mystique(Dress) from _call_Display_Mystique_1
                        
                if Ch_Focus == "Kitty": 
                    #If Kitty was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Kitty": 
                    #If Kitty was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Kitty"
        elif Chr == "Emma":
                if E_Loc == bg_current:
                        #If Emma is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                            if K_Loc == bg_current:
                                #if Kitty is there, shift her to third position
                                $ K_SpriteLoc = StageFarRight
                                $ KittyLayer = 50
                            elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                            if newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageRight
                                $ newgirl["Mystique"].GirlLayer = 75
                        #and move Emma to first position
                        $ E_SpriteLoc = StageCenter
                        $ EmmaLayer = 100
                        call Display_Emma(Dress) from _call_Display_Emma_2
                        call Display_Kitty(Dress) from _call_Display_Kitty_2
                        call Display_Rogue(Dress) from _call_Display_Rogue_2
                        call Display_Mystique(Dress) from _call_Display_Mystique_2
                        
                if Ch_Focus == "Emma": 
                    #If Emma was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Kitty": 
                    #If Emma was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Emma"
        elif Chr == "Rogue":
                if R_Loc == bg_current:
                        #If Rogue is where you're at. . .
                        if K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                            if E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                            elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif E_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                            if newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageFarRight
                                $ newgirl["Mystique"].GirlLayer = 50
                        elif newgirl["Mystique"].Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ newgirl["Mystique"].SpriteLoc = StageRight
                                $ newgirl["Mystique"].GirlLayer = 75
                        #and move Rogue to first position
                        $ R_SpriteLoc = StageCenter
                        $ RogueLayer = 100
                        call Display_Emma(Dress) from _call_Display_Emma_3
                        call Display_Kitty(Dress) from _call_Display_Kitty_3
                        call Display_Rogue(Dress) from _call_Display_Rogue_3
                        call Display_Mystique(Dress) from _call_Display_Mystique_3
                        
                if Ch_Focus == "Rogue": 
                    #If Rogue was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Rogue": 
                    #If Rogue was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Rogue"
        elif Chr == "Mystique":
                if newgirl["Mystique"].Loc == bg_current:
                        #If Emma is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                            if K_Loc == bg_current:
                                #if Kitty is there, shift her to third position
                                $ K_SpriteLoc = StageFarRight
                                $ KittyLayer = 50
                            elif E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                        elif K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                            if E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageFarRight
                                $ EmmaLayer = 50
                        elif E_Loc == bg_current:
                                #if Emma is there, shift her to third position
                                $ E_SpriteLoc = StageRight
                                $ EmmaLayer = 75
                        #and move Emma to first position
                        $ newgirl["Mystique"].SpriteLoc = StageCenter
                        $ newgirl["Mystique"].GirlLayer = 100
                        call Display_Emma(Dress) from _call_Display_Emma_4
                        call Display_Kitty(Dress) from _call_Display_Kitty_4
                        call Display_Rogue(Dress) from _call_Display_Rogue_4
                        call Display_Mystique(Dress) from _call_Display_Mystique_4
                        
                if Ch_Focus == "Mystique": 
                    #If Mystique was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Kitty": 
                    #If Mystique was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Mystique"
        $ renpy.restart_interaction() 
        return
    
label Display_Rogue(Dress = 1, DLoc = R_SpriteLoc):
    # If Dress, then check whether the character is underdressed when displaying her
    
    if Taboo and Dress and R_Loc != "bg pool":        
            call RogueOutfit from _call_RogueOutfit_2
            #$ R_Water = 0
               
    if R_Loc != "bg showerroom" and R_Loc != "bg pool":
            $ R_Water = 0
    
    $ R_SpriteLoc = DLoc
    
    # resets triggers
    $ Trigger = 0    
    $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    
    if "Rogue" in Party or R_Loc == bg_current:         
            #displays Rogue if present, Sets her as local if in a party
            $ R_Loc = bg_current        
            
            if Taboo and Dress:              
                #If in public, check to see if clothes are too sexy, and change them if necessary
                call Rogue_OutfitShame from _call_Rogue_OutfitShame
            
            #Display Rogue
            show Rogue at SpriteLoc(DLoc) zorder RogueLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    else:       
            # If Rogue isn't there, put her away
            hide Rogue
            call Rogue_Hide from _call_Rogue_Hide
    return

label Display_Kitty(Dress = 1, DLoc = K_SpriteLoc):
   # If Dress, then check whether the character is underdressed when displaying her
    
    if Taboo and Dress and K_Loc != "bg pool": #If not in the showers, get dressed and dry off        
            call KittyOutfit from _call_KittyOutfit_2
            #$ K_Wet = 0
              
    if K_Loc != "bg showerroom" and K_Loc != "bg pool":
            $ K_Water = 0
     
    $ K_SpriteLoc = DLoc
    
    # resets triggers
    $ Trigger = 0    
    $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin" 
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    
    if "Kitty" in Party or K_Loc == bg_current:         
            #displays Kitty if present, Sets her as local if in a party
            $ K_Loc = bg_current 
            
            if Taboo and Dress:                       
                #If in public, check to see if clothes are too sexy, and change them if necessary
                call Kitty_OutfitShame from _call_Kitty_OutfitShame
                
            #Display Kitty
            show Kitty_Sprite at SpriteLoc(DLoc) zorder KittyLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # If Kitty isn't there, put her away
            hide Kitty_Sprite
            call Kitty_Hide from _call_Kitty_Hide
    return

label Display_Emma(Dress = 1, DLoc = E_SpriteLoc, Location = E_Loc):
    # If Dress, then check whether the character is underdressed when displaying her
    
    if Taboo and Dress and E_Loc != "bg pool": #If not in the showers, get dressed and dry off        
            call EmmaOutfit from _call_EmmaOutfit_3 #add when available
            #$ E_Wet = 0
              
    if E_Loc != "bg showerroom" and E_Loc != "bg pool":
            $ E_Water = 0
        
    $ E_SpriteLoc = DLoc
    
    # resets triggers
    $ Trigger = 0    
    $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    
    if "Emma" in Party or Location == bg_current:         
            #displays Emma if present, Sets her as local if in a party
            if "Emma" in Party: 
                    $ E_Loc = bg_current 
            
            if Taboo and Dress:                       #If in public, check to see if clothes are too sexy, and change them if necessary
                call Emma_OutfitShame from _call_Emma_OutfitShame #restore when working
                
            #hide podium/desk shot
            hide Emma_At_Podium onlayer backdrop
            hide Emma_At_Desk onlayer backdrop
            
            #Display Emma
            show Emma_Sprite at SpriteLoc(DLoc) zorder EmmaLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # If Emma isn't there, put her away
            hide Emma_Sprite
            call Emma_Hide from _call_Emma_Hide
    return


label Display_Mystique(Dress = 1, DLoc = newgirl["Mystique"].SpriteLoc, Location = newgirl["Mystique"].Loc):
    # If Dress, then check whether the character is underdressed when displaying her
    if Taboo and Dress and newgirl["Mystique"].Loc != "bg pool": #If not in the showers, get dressed and dry off        
            call MystiqueOutfit from _call_MystiqueOutfit_2 #add when available
            #$ newgirl["Mystique"].Wet = 0
              
    if newgirl["Mystique"].Loc != "bg showerroom" and newgirl["Mystique"].Loc != "bg pool":
            $ newgirl["Mystique"].Water = 0
        
    $ newgirl["Mystique"].SpriteLoc = DLoc
    
    # resets triggers
    $ Trigger = 0    
    $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    
    if "Mystique" in Party or Location == bg_current:         
            #displays Emma if present, Sets her as local if in a party
            if "Mystique" in Party: 
                    $ newgirl["Mystique"].Loc = bg_current 
            
            if Taboo and Dress:                       #If in public, check to see if clothes are too sexy, and change them if necessary
                call Mystique_OutfitShame from _call_Mystique_OutfitShame #restore when working
                
            #hide podium/desk shot
            #hide Emma_At_Podium onlayer backdrop
            #hide Emma_At_Desk onlayer backdrop
            
            #Display Emma
            show Mystique_Sprite at SpriteLoc(DLoc) zorder newgirl["Mystique"].GirlLayer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.5, 0.0)
    else:
            # If Emma isn't there, put her away
            hide Mystique_Sprite
            #call Mystique_Hide
    return
    

label Display_Laura(Dress = 1, TrigReset = 1, DLoc = newgirl["Laura"].SpriteLoc, YLoc=50):
   # If Dress, then check whether the character is underdressed when displaying her
    
    if "Laura" not in Party and newgirl["Laura"].Loc != bg_current:  
            # If Laura isn't there, put her away
            hide Laura_Sprite
            call Laura_Hide 
            return
            
    if Taboo and Dress: #If not in the showers, get dressed and dry off        
#            call LauraOutfit
            $ newgirl["Laura"].Wet = 0
              
    if newgirl["Laura"].Loc != "bg showerroom":
            $ newgirl["Laura"].Water = 0
    
    $ newgirl["Laura"].SpriteLoc = DLoc
    
    if TrigReset:
            # resets triggers
            $ Trigger = 0    
            $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
            $ Trigger3 = 0
            $ Trigger4 = 0
            $ Trigger5 = 0
    
    if Partner == "Laura":
        $DLoc = StageFarRight #Moves Kitty over if she's secondary
      
    call Laura_Hide         
    #displays Laura if present, Sets her as local if in a party
    $ newgirl["Laura"].Loc = bg_current 
    
#            if Dress:                       
#                #If in public, check to see if clothes are too sexy, and change them if necessary
#                call Laura_OutfitShame
    
    if bg_current == "bg movies" or bg_current == "bg restaurant":
        #shifts them downward if on a date
        $ YLoc = 250
        
    #Display Laura    
    if not renpy.showing('Laura_Sprite'):
        show Laura_Sprite at SpriteLoc(1000,YLoc) zorder newgirl["Laura"].GirlLayerLayer:
                offset (0,0)
                anchor (0.5, 0.0)  
                pos (1000,YLoc)
    show Laura_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            easeout .5 pos (DLoc,YLoc)    
    show Laura_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            pos (DLoc,YLoc)    
#    show Laura_Sprite at SpriteLoc(DLoc,YLoc) zorder newgirl["Laura"].GirlLayerLayer:
#            alpha 1
#            zoom 1
#            offset (0,0)
#            anchor (0.5, 0.0)  
#    with easeinright
            
    return
# end Scene Setting ///////////////////////////////////////////////////////////////////////



# Player Leveling
label Stat_Checks:
           
    if P_XP >= P_XPgoal and P_Lvl < 10:        
        $ P_XPgoal = int((1.15 * P_XPgoal) + 100)
        $ P_Lvl += 1
        $ P_StatPoints += 1
        if P_Lvl <5:
            $ Count = 1
        elif P_Lvl <9:
            $ Count = 2
        else:
            $ Count = 3
        $ P_Income += Count
        "You've leveled up!"
        "Xavier has noticed your achievements and raised your stipend by $[Count] per day. It is now $[P_Income]."
        if P_Lvl >= 4:
            "You've level [P_Lvl], you're now experienced enough to have better control of your powers!"
        if P_Lvl == 10:
            "You've reached max level!"
    
    if R_Loose < 2:  #checks how tight Rogue's asshole is   
        if (R_Anal + R_DildoA + R_Plug) >= 3:
            $ R_Loose = 1
        if (R_Anal + R_DildoA + R_Plug) >= 15:
            $ R_Loose = 2   
            
    if R_XP >= R_XPgoal and R_Lvl < 10:
        $ R_XPgoal = int((1.15 * R_XPgoal) + 100)
        $ R_Lvl += 1
        $ R_StatPoints += 1
        "Rogue's leveled up! I bet she has some new tricks to learn."
        if R_Lvl == 10:
            "Rogue's reached max level!"
            
            
    if K_Loose < 2:  #checks how tight Kitty's asshole is   
        if (K_Anal + K_DildoA + K_Plug) >= 3:
            $ K_Loose = 1
        if (K_Anal + K_DildoA + K_Plug) >= 15:
            $ K_Loose = 2   
            
    if K_XP >= K_XPgoal and K_Lvl < 10:
        $ K_XPgoal = int((1.15 * K_XPgoal) + 100)
        $ K_Lvl += 1
        $ K_StatPoints += 1
        "Kitty's leveled up! I bet she has some new tricks to learn."
        if K_Lvl == 10:
            "Kitty's reached max level!"
      
    if K_Loose < 2:  #checks how tight Kitty's asshole is   
        if (K_Anal + K_DildoA + K_Plug) >= 3:
            $ K_Loose = 1
        if (K_Anal + K_DildoA + K_Plug) >= 15:
            $ K_Loose = 2   
            
    if E_XP >= E_XPgoal and E_Lvl < 10:
        $ E_XPgoal = int((1.15 * E_XPgoal) + 100)
        $ E_Lvl += 1
        $ E_StatPoints += 1
        "Emma's leveled up! I bet she has some new tricks to learn."
        if E_Lvl == 10:
            "Emma's reached max level!"
            
    return

label P_Level_Up:
    menu:
        "You have [P_StatPoints] points to spend. How would you like to spend them?"
        "Increase sexual stamina. [[One point]" if "focus" not in P_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving you more time before you blow."
                "Unlock Focus.":
                    if P_StatPoints:
                        $ P_StatPoints -= 1  
                        $ P_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Increase your addictiveness. [[One point]" if "addict control" not in P_Traits and "nonaddictive" not in P_Traits and "addictive" not in P_Traits:
            menu:
                "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                "Increase addictiveness.":
                    if P_StatPoints:
                        $ P_StatPoints -= 1 
                        $ P_Traits.append("addictive") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Reduce your addictiveness. [[One point]" if "addict control" not in P_Traits and "nonaddictive" not in P_Traits and "addictive" not in P_Traits:
            menu:
                "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                "Reduce addictiveness.":
                    if P_StatPoints:
                        $ P_StatPoints -= 1 
                        $ P_Traits.append("nonaddictive") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Control your Addiction level. [[Two points]" if "addict control" not in P_Traits and ("nonaddictive" in P_Traits or "addictive" in P_Traits):
            menu:
                "This trait will allow you to freely control the amount you addict girls to your touch."
                "Gain addiction control.":
                    if P_StatPoints >= 2:
                        $ P_StatPoints -= 2 
                        $ P_Traits.append("addict control") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass       
                    
        "Increase your addictiveness. [[Free]" if "addict control" in P_Traits: #If you have Addict-control
            menu:
                "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                "Increase addictiveness, no cost.":
                    if "nonaddictive" in P_Traits:
                        $ P_Traits.remove("nonaddictive")
                        "You are now at the baseline addictiveness level."
                    elif "addictive" not in P_Traits:
                        $ P_Traits.append("addictive") 
                        "You are now at the enhanced addictiveness level."
                    else:
                        "You are already at the max addictiveness level."
                "Cancel.":
                    pass
        "Reduce your addictiveness. [[Free]" if "addict control" in P_Traits:
            menu:
                "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                "Reduce addictiveness.":
                    if "addictive" in P_Traits:
                        $ P_Traits.remove("addictive")
                        "You are now at the baseline addictiveness level."
                    elif "nonaddictive" not in P_Traits:
                        $ P_Traits.append("nonaddictive") 
                        "You are now at the reduced addictiveness level."
                    else:
                        "You are already at the minimum addictiveness level."                
                    
                    if "addictive" in P_Traits:
                        $ P_Traits.remove("addictive") 
                        $ P_Traits.append("nonaddictive") 
                        $ P_Traits.append("addict control") 
                    else:
                        $ P_Traits.append("nonaddictive") 
                "Cancel.":
                    pass
                    
        "Increase semen production. [[One point]" if P_Semen_Max < 5:            
            menu:
                "This trait will increase by 1 the number of times you can climax before needing a break."
                "Increase max semen.":                    
                    if P_StatPoints:
                        $ P_StatPoints -= 1  
                        $ P_Semen_Max += 1
                    else:
                        "You don't have enough points for that."
                    if P_Semen_Max >= 5:
                        "You're already at the max level."
                "Cancel.":
                    pass
                    
#        "Make yourself addictive to Kitty. [[One point]" if "met" in K_History and "addict kitty" not in P_Traits:
#            menu:
#                "This trait will adjust the \"flavor\" of your touch so that it is also addictive to Kitty."
#                "Increase addictiveness.":
#                    if P_StatPoints:
#                        $ P_StatPoints -= 1 
#                        $ P_Traits.append("addict kitty") 
#                    else:
#                        "You don't have enough points for that."
#                "Cancel.":
#                    pass
                    
        "Never Mind, I'll come back later.":
            return

    if P_StatPoints > 0:
        jump P_Level_Up
    return

# End Player Leveling

# Rogue Leveling
label R_Level_Up:
    menu:
        "Rogue has [R_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in R_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Rogue more time before she orgasms."
                "Unlock Focus.":
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Rogue's resistance. [[One point]]" if 0 < R_Resistance < 3:
            menu:
                "This trait will increase Rogue's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if R_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Rogue can take before needing a break."
            menu:
                "She currently has [R_MaxAction] actions."
                "Increase sex actions.":
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_MaxAction += 2
                        if R_MaxAction > 10:
                            $ R_MaxAction = 10
                            "Rogue has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Allow Rogue to touch. [[One point]" if "touch" not in R_Traits and R_Lvl >= 5:
            "This trait will allow Rogue to touch other people, not just you, without harming them."
            menu:
                "She can still borrow their abilities if they have any."
                "Unlock touch ability.":                    
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_Traits.append("touch") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Allow Rogue to permanently Steal. [[Two points]" if "touch" in R_Traits and "steal" not in R_Traits:
            "This trait will allow Rogue to permanently copy one other mutant ability at a time."            
            menu:
                "This does not harm the person she borrows from and can switch abilities with a touch."
                "Unlock steal ability.":
                    if R_StatPoints >= 2:
                        $ R_StatPoints -= 2  
                        $ R_Traits.append("steal") 
                    else:
                        "You don't have enough points for that."                    
                "Cancel.":
                    pass
        "Never Mind, I'll come back later.":
            return
    if R_StatPoints > 0:
        jump R_Level_Up
    return

# End Rogue Leveling


# Kitty Leveling
label K_Level_Up:
    menu:
        "Kitty has [K_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in K_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Kitty more time before she orgasms."
                "Unlock Focus.":
                    if K_StatPoints:
                        $ K_StatPoints -= 1  
                        $ K_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Kitty's resistance. [[One point]]" if 0 < K_Resistance < 3:
            menu:
                "This trait will increase Kitty's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if K_StatPoints:
                        $ K_StatPoints -= 1  
                        $ K_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if K_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Kitty can take before needing a break."
            menu:
                "She currently has [K_MaxAction] actions."
                "Increase sex actions.":
                    if K_StatPoints:
                        $ K_StatPoints -= 1  
                        $ K_MaxAction += 2
                        if K_MaxAction > 10:
                            $ K_MaxAction = 10
                            "Kitty has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
        "Do. . . Something else?" if K_MaxAction >= 10:
                "I don't know, what {i}should{/i} she be doing at this point?"
        "Never Mind, I'll come back later.":
            return
    if K_StatPoints > 0:
        jump K_Level_Up
    return

# End Kitty Leveling

# Emma Leveling
label E_Level_Up:
    menu:
        "Emma has [E_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in E_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Emma more time before she orgasms."
                "Unlock Focus.":
                    if E_StatPoints:
                        $ E_StatPoints -= 1  
                        $ E_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Emma's resistance. [[One point]]" if 0 < E_Resistance < 3:
            menu:
                "This trait will increase Emma's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if E_StatPoints:
                        $ E_StatPoints -= 1  
                        $ E_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if E_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Emma can take before needing a break."
            menu:
                "She currently has [E_MaxAction] actions."
                "Increase sex actions.":
                    if E_StatPoints:
                        $ E_StatPoints -= 1  
                        $ E_MaxAction += 2
                        if E_MaxAction > 10:
                            $ E_MaxAction = 10
                            "Emma has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
        "Do. . . Something else?" if E_MaxAction >= 10:
                "I don't know, what {i}should{/i} she be doing at this point?"
        "Never Mind, I'll come back later.":
            return
    if E_StatPoints > 0:
        jump E_Level_Up
    return

# End Emma Leveling

# Shop Interface //////////////////////////////////////////////////////////////////////
                                                 
label Shop:
    menu:
        "You are logged into the store. You have %(P_Cash)d dollars."       
        "Buy dildo for $20.":
            $ Count = Inventory_Check("dildo")
            if Count >= 10:
                "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
            elif P_Cash >= 20:                
                "You purchase one dildo."
                $ P_Inventory.append("dildo")
                $ P_Cash -= 20
            else:
                "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
            $ Count = Inventory_Check("vibrator")
            if Count >= 10:
                "If you bought one more vibrator, you would risk a geological event."
            elif P_Cash >= 25:
                "You purchase one vibrator."
                $ P_Inventory.append("vibrator")
                $ P_Cash -= 25
            else:
                "You don't have enough for that."   
        "Gifts for Rogue":
            menu:
                "Buy green lace nighty for $75." if "nighty" not in R_Inventory and "nighty" not in P_Inventory:            
                    if P_Cash >= 75:
                        "You purchase the nighty, this will look nice on Rogue."
                        $ P_Inventory.append("nighty")
                        $ P_Cash -= 75
                    else:
                        "You don't have enough for that."    
                "Buy black lace bra for $90." if "lace bra" not in R_Inventory and "lace bra" not in P_Inventory:            
                    if P_Cash >= 90:
                        "You purchase the lace bra, this will look nice on Rogue."
                        $ P_Inventory.append("lace bra")
                        $ P_Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "lace panties" not in R_Inventory and "lace panties" not in P_Inventory:            
                    if P_Cash >= 110:
                        "You purchase the lace panties, these will look nice on Rogue."
                        $ P_Inventory.append("lace panties")
                        $ P_Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for Kitty":
            menu:  
                "Buy white lace bra for $90." if "lace bra" not in K_Inventory and "lace bra" not in P_Inventory:            
                    if P_Cash >= 90:
                        "You purchase the lace bra, this will look nice on Kitty."
                        $ P_Inventory.append("lace bra")
                        $ P_Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in K_Inventory and "lace panties" not in P_Inventory:            
                    if P_Cash >= 110:
                        "You purchase the lace panties, these will look nice on Kitty."
                        $ P_Inventory.append("lace panties")
                        $ P_Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Never mind.":
                    pass
        "Buy books":
            menu Shop_Books:
                "Buy \"Dazzler and Longshot\" for $20.":
                    "A sappy romantic novel about two starcrossed lovers."
                    if "Dazzler and Longshot" in P_Inventory:
                        "You already have a copy, and really only need one."
                    elif P_Cash >= 20:                
                        "You purchase the book."
                        $ P_Inventory.append("Dazzler and Longshot")
                        $ P_Cash -= 20
                    else:
                        "You don't have enough for that."        
                "Buy \"256 Shades of Grey\" for $20.":
                    "A gripping sexual thriller about a stern red-headed \"goblin queen\" and her subject."
                    if "256 Shades of Grey" in P_Inventory:
                        "You already have a copy, and really only need one."
                    elif P_Cash >= 20:                
                        "You purchase the book."
                        $ P_Inventory.append("256 Shades of Grey")
                        $ P_Cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"Avengers Tower Penthouse\" for $20.":
                    "A book filled with nude pictures of various Avengers, sexy."
                    if "Avengers Tower Penthouse" in P_Inventory:
                        "You already have a copy, and really only need one."
                    elif P_Cash >= 20:                
                        "You purchase the book."
                        $ P_Inventory.append("Avengers Tower Penthouse")
                        $ P_Cash -= 20
                    else:
                        "You don't have enough for that."
                "Back":
                    jump Shop
            jump Shop_Books
        "Buy Cologne":
            if Day < 50:
                "These are currently out of stock, check back later."
                jump Shop
            menu:
                "Examine the Mandrill Cologne (\"Nothin says lovin like a shiny red butt\").":            
                    menu:
                        "This cologne is guaranteed to make women love you more [[+Love]]."
                        "Buy Mandrill Cologne for $150":
                            pass
                        "Never mind.":
                            jump Shop                 
                    if "Mandrill Cologne" in P_Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif P_Cash >= 150:                
                        "You purchase one bottle of Mandrill Cologne."
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Cash -= 150
                    else:
                        "You don't have enough for that."
                "Examine the Purple Rain Cologne (\"They can't resist your charms\").":
                    menu:
                        "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]]."
                        "Buy Purple Rain Cologne for $200":
                            pass
                        "Never mind.":
                            jump Shop   
                    if "Purple Rain Cologne" in P_Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif P_Cash >= 200:                
                        "You purchase one bottle of Purple Rain Cologne."
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Cash -= 200
                    else:
                        "You don't have enough for that."
                "Examine the Corruption Cologne (\"Let the wild out\").":
                    menu:
                        "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]]."
                        "Buy Corruption Cologne for $250":
                            pass
                        "Never mind.":
                            jump Shop   
                    if "Corruption Cologne" in P_Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif P_Cash >= 250:                
                        "You purchase one bottle of Corruption Cologne."
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Cash -= 250
                    else:
                        "You don't have enough for that."
                "Back":
                    pass                
        "Exit Store":
            return
    jump Shop
return

# end Shop Interface //////////////////////////////////////////////////////////////////////

# Inventory Interface //////////////////////////////////////////////////////////////////////


label Show_Inventory:
    menu:
        "Check Inventory":
            show screen P_Inventory_screen
            "You search your bags. . ."
            hide screen P_Inventory_screen

        "Use items.":
            if P_Inventory == []:
                "There's nothing in here."
                jump Show_Inventory
            menu:
                "View the Mandrill Cologne." if "Mandrill Cologne" in P_Inventory:
                    $ Count = Inventory_Check("Mandrill Cologne")
                    "This cologne is guaranteed to make women love you more [[+Love]]. You have [Count] doses left."
                    "Product warning, any love gained while under the effects may be lost when this wears off, if the limits are reached."
                    menu:
                        "Use it now?"
                        "Yes":
                            if "mandrill" in P_Traits:
                                "You already have this on."
                            if "purple" in P_Traits or "corruption" in P_Traits:
                                "You'll confuse the scent you already have on."
                            else:
                                $ P_Traits.append("mandrill")
                                $ P_Inventory.remove("Mandrill Cologne")   
                        "No":
                            pass
                            
                "View the Purple Rain Cologne." if "Purple Rain Cologne" in P_Inventory:
                    $ Count = Inventory_Check("Purple Rain Cologne")
                    "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]]. You have [Count] doses left."
                    "Product warning, any obedience gained whie under the effects may be lost when this wears off, if the limits are reached."
                    menu:
                        "Use it now?"
                        "Yes":
                            if "purple" in P_Traits:
                                "You already have this on."
                            if "mandrill" in P_Traits or "corruption" in P_Traits:
                                "You'll confuse the scent you already have on."
                            else:
                                $ P_Traits.append("purple")
                                $ P_Inventory.remove("Purple Rain Cologne") 
                        "No":
                            pass
                            
                "View the Corruption Cologne." if "Corruption Cologne" in P_Inventory:
                    $ Count = Inventory_Check("Corruption Cologne")
                    "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]]. You have [Count] doses left."
                    "Product warning, any Inhibition lost whie under the effects may be regained when this wears off, if the limits are reached."
                    menu:
                        "Use it now?"
                        "Yes":
                            if "corruption" in P_Traits:
                                "You already have this on."
                            if "purple" in P_Traits or "mandrill" in P_Traits:
                                "You'll confuse the scent you already have on."
                            else:
                                $ P_Traits.append("corruption")
                                $ P_Inventory.remove("Corruption Cologne")  
                                    
                        "No":
                            pass    
                
                
                "Exit":
                    return
        "Exit":
                    return
    jump Show_Inventory
# end Inventory Interface //////////////////////////////////////////////////////////////////////


return
