class Barbarian(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d12'
        self.saves[2] = 1 # CON
        self.saves[0] = 1 # STR

        self.skillsinfo = []
        self.skillschoose = [2, ['Animal Handling', 'Athletics', 'Intimidation',
                            'Nature', 'Perception', 'Survival']]

        self.otherprofs = ['Light', 'Medium', 'Shields', 'Simple', 'Martial']
