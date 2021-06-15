class Warlock(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[4] = 1 # WIS
        self.saves[5] = 1 # CHA

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['Arcana', 'Deception', 'History',
                                 'Intimidation', 'Investigation', 'Nature', 'Religion']]

        self.otherprofs = ['Light', 'Simple']
