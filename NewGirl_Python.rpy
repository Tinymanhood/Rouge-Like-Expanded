init python:

    class Girlnew(object):
        
        def __init__ (self, name = "no name"):
            #self.name = name
            #self.money = money
            #self.girl = {   
            self.name = name
            self.Petname = "boy"       #What Emma calls the player
            self.Petnames = ["boy"]
            self.Pet = "Mystique"           #What you call Emma
            self.Pets = ["Mystique"]
            self.Rules = 1
            self.GirlName = "Raven"
            self.Loc = "bg Mystique"
            self.Love = 300
            self.Obed = 0
            self.Inbt = 200
            self.Lust = 10
            self.LikeRogue = 500
            self.LikeEmma = 500
            self.LikeKitty = 500
            self.LikeOtherGirl = {}
            self.Addict = 0 #how addicted she is
            self.Addictionrate = 0 #How faster her addiciton rises
            self.Resistance = 0 #how fast her rate falls
            self.Inventory = []    
            self.OCount = 0                #Orgasm counter
            self.Loose = 2
            self.XP = 0
            self.Cheated = 0               #number of times you've cheated on her    
            self.Break = [0,0]                 #minimum time between break-ups/number of total break-ups
            self.StatPoints = 0    
            self.XPgoal = 100
            self.Lvl = 0
            self.Traits = []
            self.Rep = 800
            self.OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
            self.Shame = 0                 #The amount of shame she generates with her current clothing/action
            self.Taboo = 0                 #The taboo level of the location she is at when not with you
            self.Chat = [0,0,0,0,0,0]
            self.Event = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Todo = []
            self.PubeC = 0    
            # #Sprite Variables
            self.Outfit = "regular"
            self.OutfitDay = "regular"
            self.Emote = "normal"
            self.EmoteDefault = "normal"
            self.Girl_Arms = 1               #her arm position
            self.Arms = 0                  #her gloves
            self.Legs = "skirt"
            self.Over = 0
            self.Chest = "top"    
            self.Pierce = 0
            self.Panties = "black panties"
            self.Neck = 0
            self.Hose = 0
            self.Mouth = "normal"
            self.Brows = "normal"
            self.Eyes = "normal"
            self.Hair = "basic"
            self.HairColor = 0
            self.Gag = 0    
            self.Gagx = 0    
            self.Blush = 0
            self.Spunk = []
            self.Pubes = 0
            self.Wet = 0
            self.LegsUp = 0
            self.Water = 0
            self.TitsUp = 1
            self.Upskirt = 0
            self.PantiesDown = 0
            self.Custom = [0,0,0,0,0,0,0,0,0,0]
            self.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
            self.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Custom4 = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Custom5 = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Custom6 = [0,0,0,0,0,0,0,0,0,0,0]    
            self.Custom7 = [0,0,0,0,0,0,0,0,0,0,0]    
            self.Gym = [2,0,0,0,"tights","top","black panties",0,0,0,0] #arms position, 0, 0, over, legs, chest, panties, 
            self.Sleepwear = [0,0,0,0,0,"short top","black panties",0,0,0]
            self.Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
            self.GirlLayer = 101
            self.SpriteLoc = 550                        #Sets Emma to default to the center
            # # Sexual Encounters
            self.History = []
            self.RecentActions = []
            self.DailyActions = []
            self.Action = 3
            self.MaxAction = 4
            self.Caught = 0
            self.Kissed = 0              #How many times they've kissed
            self.Hand = 0
            self.Foot = 0
            self.Slap = 0
            self.Spank = 0
            self.Strip = 0
            self.Tit = 0
            self.Sex = 0
            self.Anal = 0
            self.Hotdog = 0
            self.Mast = 0
            self.Org = 0
            self.FondleB = 0
            self.FondleT = 0
            self.FondleP = 0
            self.FondleA = 0
            self.DildoP = 0
            self.DildoA = 0
            self.Vib = 0
            self.Vibrator = 0
            self.Plug = 0
            self.Plugged = 0
            self.SuckB = 0
            self.InsertP = 0
            self.InsertA = 0
            self.LickP = 0    
            self.LickA = 0
            self.Blow = 0
            self.Swallow = 0
            self.CreamP = 0
            self.CreamA = 0
            self.Les = 0    
            self.LesWatch = 0
            self.SexRogue = 0
            self.SexKitty = 0
            self.SexEmma = 0
            self.SexOtherGirl = {}
            self.SEXP = 0
            self.ShameLevel = 0
            self.PlayerFav = 0                     #The player's favorite activity with her
            self.Favorite = 0                      #her favorite activity
            self.SeenChest = 0
            self.SeenPanties = 0
            self.SeenPussy = 0   
            self.SeenPeen = 0
            self.Sleep = 0
            self.Personality = "normal"
            self.Date = 0 
            self.Forced = 0                                        #This is a toggle for if she's being coerced
            self.ForcedCount = 0 
            self.Glasses = 0 
            self.HeadBand = 0 
            self.Swimsuit = 0 
            self.OnePiece = 0 
            self.Held = 0
            self.Accessory1 = 0 
            self.Accessory2 = 0 
            self.Accessory3 = 0 
            self.Extra = {} 
            self.LooksLike = "Raven" 
            self.Blindfold = 0 
            self.Headband = 0 
            #}

         

        
    class FieldValue2(BarValue, FieldEquality):
    # """
    #  :doc: value
    #  A bar value that allows the user to adjust the value of a field
    #  on an object.
    #  `object`
    #      The object.
    #  `field`
    #      The field, a string.
    #  `range`
    #      The range to adjust over.
    #  `max_is_zero`
    #      If True, then when the field is zero, the value of the
    #      bar will be range, and all other values will be shifted
    #      down by 1. This works both ways - when the bar is set to
    #      the maximum, the field is set to 0.
    #      This is used internally, for some preferences.
    #  `style`
    #      The styles of the bar created.
    #  `offset`
    #      An offset to add to the value.
    #  `step`
    #      The amount to change the bar by. If None, defaults to 1/10th of
    #      the bar.
    #  """
        offset = 0

        identity_fields = [ 'object' ]
        equality_fields = [ 'range', 'max_is_zero', 'style', 'offset', 'step']

        def __init__(self, object, field, girl, range, max_is_zero=False, style="bar", offset=0, step=None):
            self.object = object
            #self.field = field
            self.variable = field
            self.girl = girl
            self.range = range
            self.max_is_zero = max_is_zero
            self.style = style
            self.offset = offset

            if step is None:
                if isinstance(range, float):
                    step = range / 10.0
                else:
                    step = max(range / 10, 1)

            self.step = step

        def changed(self, value):

            if self.max_is_zero:
                if value == self.range:
                    value = 0
                else:
                    value = value + 1

            value += self.offset

            setattr(newgirl[self.girl], self.variable, value)
            #newgirl["Mystique"].Love = value
            renpy.restart_interaction()

        def get_adjustment(self):

            #value = newgirl["Mystique"].Love
            #getattr(self.object, self.field)
            value = getattr(newgirl[self.girl], self.variable)

            value -= self.offset

            if self.max_is_zero:
                if value == 0:
                    value = self.range
                else:
                    value = value - 1

            return ui.adjustment(
                range=self.range,
                value=value,
                changed=self.changed,
                step=self.step)

        def get_style(self):
            return self.style, "v" + self.style

    def VariableValue2(variable, girl, range, max_is_zero=False, style="bar", offset=0, step=None):
        # """
        #  :doc: value

        #  A bar value that allows the user to adjust the value of a variable
        #  in the default store.

        #  `variable`
        #      A string giving the name of the variable to adjust.
        #  `range`
        #      The range to adjust over.
        #  `max_is_zero`
        #      If True, then when the field is zero, the value of the
        #      bar will be range, and all other values will be shifted
        #      down by 1. This works both ways - when the bar is set to
        #      the maximum, the field is set to 0.

        #      This is used internally, for some preferences.
        #  `style`
        #      The styles of the bar created.
        #  `offset`
        #      An offset to add to the value.
        #  `step`
        #      The amount to change the bar by. If None, defaults to 1/10th of
        #      the bar.
        # """

        return FieldValue2(store, variable, girl, range, max_is_zero=max_is_zero, style=style, offset=offset, step=step)    


    def Girls_Around():
        GirlsAround = []
        if R_Loc == bg_current:
            GirlsAround.append("Rogue")
        if K_Loc == bg_current:
            GirlsAround.append("Kitty")
        if E_Loc == bg_current:
            GirlsAround.append("Emma")
        for xkk in ModdedGirls:
            if newgirl[xkk].Loc == bg_current:
                GirlsAround.append(xkk)
        return GirlsAround

    def OtherGirls_Around(Girl_ = "Rogue"):
        OtherGirlsAround = []
        if R_Loc == bg_current and Girl_ != "Rogue":
            OtherGirlsAround.append("Rogue")
        if K_Loc == bg_current and Girl_ != "Kitty":
            OtherGirlsAround.append("Kitty")
        if E_Loc == bg_current and Girl_ != "Emma":
            OtherGirlsAround.append("Emma")
        for xkk in ModdedGirls:
            if newgirl[xkk].Loc == bg_current and Girl_ != xkk:
                OtherGirlsAround.append(xkk)
        return OtherGirlsAround
    