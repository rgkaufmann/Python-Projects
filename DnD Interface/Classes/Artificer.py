import numpy as np

class Artificer(ClassParent):
    def __init__(self, mc, stats):
        ClassParent.__init__(self, mc)

        self.hitdie = '1d8'
        self.multiclassing = [0, 0, 0, 0, 1, 0]
        self.subclass = ''
        self.abilities = {}

        if not mc:
            self.saves[2] = 1 # CON
            self.saves[4] = 1 # INT

            self.toolprofs = ['Thieves Tools']
            self.toolchoose = [2, ["Alchemist's Supplies", "Brewer's Supplies",
                                   "Calligrapher's Supplies", "Carpenter's Tools",
                                   "Cartographer's Tools", "Cobbler's Tools",
                                   "Cook's Utensils", "Glassblower's Tools",
                                   "Jeweler's Tools", "Leatherworker's Tools",
                                   "Mason's Tools", "Painter's Supplies",
                                   "Potter's Tools", "Smith's Tools", "Tinker's Tools",
                                   "Weaver's Tools", "Woodcarver's Tools",
                                   "Disguise kit", "Forgery Kit", "Herbalism Kit",
                                   "Bagpipes", "Drum", "Dulcimer", "Flute", "Lute",
                                   "Lyre", "Horn", "Pan Flute", "Shawm", "Viol",
                                   "Navigator's Tools", "Poisoner's Kit",
                                   "Thieves' Tools"]]

            self.skillsinfo = []
            self.skillschoose = [3, ['Arcana', 'Deception', 'History',
                                     'Investigation', 'Medicine', 'Nature', 'Religion',
                                     'Sleight of Hand']]

            self.otherprofs = ['Light', 'Medium', 'Simple', 'Hand Crossbow',
                               'Heavy Crossbow']

            return True
        elif mc and np.and(stats > (multiclassing * 13)):
            sdflk;ja;lkkadflk;fad

            return True
        else:
            return False
