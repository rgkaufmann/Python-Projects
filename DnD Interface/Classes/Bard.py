class Bard(ClassParent):
    def __init__(self):
        ClassParent.__init__(self)

        self.hitdie = '1d8'
        self.saves[1] = 1 # DEX
        self.saves[5] = 1 # CHA

        self.toolprofs = []
        self.toolchoose = [3, ['Bagpipes', 'Drum', 'Dulcimer', 'Flute', 'Horn',
                            'Lute', 'Lyre', 'Pan Flute', 'Shawm', 'Viol']]

        self.skillsinfo = []
        self.skillschoose = [3, ['Acrobatics', 'Animal Handling', 'Arcana',
                            'Athletics', 'Deception', 'History', 'Insight',
                            'Intimidation', 'Investigation', 'Medicine',
                            'Nature', 'Perception', 'Performance',
                            'Persuasion', 'Religion', 'Sleight of Hand',
                            'Stealth', 'Survival']]

        self.otherprofs = ['Light', 'Simple', 'Hand Crossbow', 'Longsword', 
                            'Rapier', 'Shortsword']
