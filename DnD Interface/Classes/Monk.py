class Monk(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[0] = 1 # STR
        self.saves[1] = 1 # DEX

        self.toolprofs = [1, ["Alchemist's Supplies", "Brewer's Supplies",
                              "Calligrapher's Supplies", "Carpenter's Tools",
                              "Cartographer's Tools", "Cobbler's Tools",
                              "Cook's Utensils", "Glassblower's Tools",
                              "Jeweler's Tools", "Leatherworker's Tools",
                              "Mason's Tools", "Painter's Supplies",
                              "Potter's Tools", "Smith's Tools", "Tinker's Tools",
                              "Weaver's Tools", "Woodcarver's Tools",'Bagpipes',
                              'Drum', 'Dulcimer', 'Flute', 'Horn', 'Lute', 'Lyre',
                              'Pan Flute', 'Shawm', 'Viol']]

        self.skillsinfo = []
        self.skillschoose = [2, ['Acrobatics', 'Athletics', 'History', 'Insight',
                                 'Religion', 'Stealth']]

        self.otherprofs = ['Simple', 'Shortsword']
