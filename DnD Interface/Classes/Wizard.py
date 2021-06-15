class Warlock(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d6'
        self.saves[4] = 1 # WIS
        self.saves[3] = 1 # INT

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [2, ['Arcana', 'Insight', 'History',
                                 'Medicine', 'Investigation', 'Religion']]

        self.otherprofs = ['Light Crossbow', 'Dagger', 'Dart', 'Sling', 'Quarterstaff']
