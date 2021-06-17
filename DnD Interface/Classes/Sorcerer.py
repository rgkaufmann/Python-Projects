import numpy as np

class Sorcerer(ClassParent):
    def __init__(self, mc, stats):
        ClassParent.__init__(self, mc)

        self.hitdie = '1d6'
        self.multiclassing = [0, 0, 0, 0, 0, 1]
        self.subclass = ''
        self.abilities = {1: {'Spellcasting': "An event in your past, or in the life of a parent or ancestor, left an indelible mark on you, infusing you with arcane magic. This font of magic, whatever its origin, fuels your spells. See chapter 10 for the general rules of spellcasting and chapter 11 for the sorcerer spell list.",
                              'Cantrips': "At 1st level, you know four cantrips of your choice from the sorcerer spell list. You learn an additional sorcerer cantrip of your choice at 4th level and another at 10th level.",
                              'Spell Slots': "The Sorcerer table shows how many spell slots you have to cast your sorcerer spells of 1st level and higher. To cast one of these sorcerer spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.\nFor example, if you know the 1st-level spell burning hands and have a 1st-level and a 2nd-level spell slot available, you can cast burning hands using either slot.",
                              'Spellcasting Ability': "Charisma is your spellcasting ability for your sorcerer spells, since the power of your magic relies on your ability to project your will into the world. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a sorcerer spell you cast and when making an attack roll with one.\nSpell save DC = 8 + your proficiency bonus + your Charisma modifier\nSpell attack modifier = your proficiency bonus + your Charisma modifier",
                              'Spellcasting Focus': "You can use an arcane focus as a spellcasting focus for your sorcerer spells.",
                              'Spells Known of 1st Level and Higher': "You know two 1st-level spells of your choice from the sorcerer spell list.\nYou learn an additional sorcerer spell of your choice at each level except 12th, 14th, 16th, 18th, 19th, and 20th. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level.\nAdditionally, when you gain a level in this class, you can choose one of the sorcerer spells you know and replace it with another spell from the sorcerer spell list, which also must be of a level for which you have spell slots.",
                              'Sorcerous Origin': "Choose a sorcerous origin, which describes the source of your innate magical power, from the list of available origins.\nYour choice grants you features when you choose it at 1st level and again at 6th, 14th, and 18th level."},
                          2: {'Font of Magic': "At 2nd level, you tap into a deep wellspring of magic within yourself. This wellspring is represented by sorcery points, which allow you to create a variety of magical effects.",
                              'Sorcery Points': "You have 2 sorcery points, and you gain one additional point every time you level up, to a maximum of 20 at level 20. You can never have more sorcery points than shown on the table for your level. You regain all spent sorcery points when you finish a long rest.",
                              'Flexible Casting': "You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels.\nCreating Spell Slots. You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The created spell slots vanish at the end of a long rest. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th.\nCreating Spell Slots\nSpell Slot Level	Sorcery Point Cost\n1st	2\n2nd	3\n3rd	5\n4th	6\n5th	7\nConverting a Spell Slot to Sorcery Points. As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level."},
                          3: {'Metamagic': "At 3rd level, you gain the ability to twist your spells to suit your needs. You gain two of the following Metamagic options of your choice. You gain another one at 10th and 17th level.\nYou can use only one Metamagic option on a spell when you cast it, unless otherwise noted."},
                          4: {'Ability Score Improvement': "When you reach 4th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          8: {'Ability Score Improvement': "When you reach 8th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          10: {'Metamagic': "At 10th level, you learn an additional metamagic option."},
                          12: {'Ability Score Improvement': "When you reach 12th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          16: {'Ability Score Improvement': "When you reach 16th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          17: {'Metamagic': "At 17th level, you learn an additional metamagic option."},
                          19: {'Ability Score Improvement': "When you reach 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          20: {'Sorcerous Restoration': "At 20th level, you regain 4 expended sorcery points whenever you finish a short rest"}}

        if not mc:
            self.saves[2] = 1 # CON
            self.saves[5] = 1 # CHA

            self.toolprofs = []

            self.skillsinfo = []
            self.skillschoose = [3, ['Arcana', 'Deception', 'Insight',
                                 'Intimidation', 'Persuasion', 'Religion']]

            self.otherprofs = ['Dagger', 'Light Crossbow', 'Dart', 'Sling', 'Quarterstaff']
            return True

        elif mc and np.and(stats > (multiclassing * 13)):

            return True

        else:
            return False
