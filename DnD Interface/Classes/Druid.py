class Druid(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[3] = 1 # WIS
        self.saves[4] = 1 # INT

        self.toolprofs = ['Herbalism Kit']

        self.skillsinfo = []
        self.skillschoose = [2, ['Arcana', 'Animal Handling', 'Insight',
                        'Medicine', 'Nature', 'Perception', 'Religion',
                        'Survival']]

        self.otherprofs = ['Light', 'Medium', 'Club', 'Dagger', 'Dart',
                        'Javelin', 'Mace', 'Quarterstaff', 'Scimitar', 'Sickle',
                        'Sling', 'Spear']
