class Rogue(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[3] = 1 # INT
        self.saves[1] = 1 # DEX

        self.toolprofs = ["Thieves' Tools"]

        self.skillsinfo = []
        self.skillschoose = [3, ['Acrobatics', 'Athletics', 'Deception',
                                 'Insight', 'Intimidation', 'Investigation'
                                 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']]

        self.otherprofs = ['Simple', 'Hand Crossbow', 'Light', 'Longsword', 'Shortsword', 'Rapier']
