class Fighter(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d10'
        self.saves[0] = 1 # STR
        self.saves[2] = 1 # CON

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['Acrobatics', 'Animal Handling', 'Athletics',
                        'History', 'Insight', 'Intimidation', 'Perception',
                        'Survival']]

        self.otherprofs = ['Light', 'Medium', 'Heavy', 'Shields', 'Simple',
                        'Martial']
