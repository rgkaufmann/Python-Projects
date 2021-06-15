class Paladin(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d10'
        self.saves[3] = 1 # WIS
        self.saves[5] = 1 # CHA

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['Athletics', 'Insight', 'Intimidation', 'Medicine',
                                 'Persuasion', 'Religion']]

        self.otherprofs = ['Simple', 'Martial', 'Light', 'Medium', 'Heavy', 'Shields']
