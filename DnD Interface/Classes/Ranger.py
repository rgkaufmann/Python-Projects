class Ranger(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d10'
        self.saves[0] = 1 # STR
        self.saves[1] = 1 # DEX

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['Animal Handling', 'Athletics', 'Insight',
                                 'Investigation', 'Nature', 'Perception'
                                 'Stealth', 'Survival']]

        self.otherprofs = ['Simple', 'Martial', 'Light', 'Medium', 'Shields']
