class Sorcerer(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d6'
        self.saves[2] = 1 # CON
        self.saves[5] = 1 # CHA

        self.toolprofs = []

        self.skillsinfo = []
        self.skillschoose = [3, ['Arcana', 'Deception', 'Insight',
                                 'Intimidation', 'Persuasion', 'Religion']]

        self.otherprofs = ['Dagger', 'Light Crossbow', 'Dart', 'Sling', 'Quarterstaff']
