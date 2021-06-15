class Mystic(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[3] = 1 # WIS
        self.saves[4] = 1 # INT

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['Arcana', 'History', 'Insight', 'Medicine',
                                 'Nature', 'Perception', 'Religion']]

        self.otherprofs = ['Simple', 'Light']
