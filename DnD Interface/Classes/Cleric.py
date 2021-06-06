class Cleric(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[3] = 1 # WIS
        self.saves[5] = 1 # CHAR

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['History', 'Insight', 'Medicine', 'Persuasion',
                            'Religion']]

        self.otherprofs = ['Light', 'Medium', 'Shields', 'Simple']
