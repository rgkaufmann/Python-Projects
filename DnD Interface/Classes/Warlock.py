import numpy as np

class Warlock(ClassParent):
    def __init__(self, mc, stats):
        ClassParent.__init__(self, mc)

        self.hitdie = '1d8'
        self.multiclassing = [0, 0, 0, 0, 0, 1]
        self.subclass = ''
        self.abilities = {1: {'Pact Magic': "Your arcane research and the magic bestowed on you by your patron have given you facility with spells. See chapter 10 for the general rules of spellcasting and chapter 11 for the warlock spell list.",
                              'Cantrips': "You know two cantrips of your choice from the warlock spell list. You learn additional warlock cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Warlock table.",
                              'Spell Slots': "The Warlock table shows how many spell slots you have to cast your warlock spells of 1st through 5th level. The table also shows what the level of those slots is; all of your spell slots are the same level. To cast one of your warlock spells of 1st level or higher, you must expend a spell slot. You regain all expended spell slots when you finish a short or long rest.\nFor example, when you are 5th level, you have two 3rd-level spell slots. To cast the 1st-level spell witch bolt, you must spend one of those slots, and you cast it as a 3rd-level spell.",
                              'Spellcasting Ability': "Charisma is your spellcasting ability for your warlock spells, so you use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one.\nSpell save DC = 8 + your proficiency bonus + your Charisma modifier\nSpell attack modifier = your proficiency bonus + your Charisma modifier", 'Spellcasting Focus': "You can use an arcane focus as a spellcasting focus for your warlock spells.",
                              'Spells Known of 1st Level and Higher': "At 1st level, you know two 1st-level spells of your choice from the warlock spell list.\nThe Spells Known column of the Warlock table shows when you learn more warlock spells of your choice of 1st level and higher. A spell you choose must be of a level no higher than what's shown in the table's Slot Level column for your level. When you reach 6th level, for example, you learn a new warlock spell, which can be 1st, 2nd, or 3rd level.\nAdditionally, when you gain a level in this class, you can choose one of the warlock spells you know and replace it with another spell from the warlock spell list, which also must be of a level for which you have spell slots.",
                              'Otherwordly Patron': "At 1st level, you have struck a bargain with an otherworldly being chosen from the list of available patrons. Your choice grants you features at 1st level and again at 6th, 10th, and 14th level."},
                          2: {'Eldritch Invocations': "In your study of occult lore, you have unearthed eldritch invocations, fragments of forbidden knowledge that imbue you with an abiding magical ability.\nAt 2nd level, you gain two eldritch invocations of your choice. A list of the available options can be found on the Optional Features page. When you gain certain warlock levels, you gain additional invocations of your choice, as shown in the Invocations Known column of the Warlock         table.\nAdditionally, when you gain a level in this class, you can choose one of the invocations you know and replace it with another invocation that you could learn at that level.\nIf an eldritch invocation has prerequisites, you must meet them to learn it. You can learn the invocation at the same time that you meet its prerequisites. A level prerequisite refers to your level in this class."},
                          3: {'Pact Boon': "At 3rd level, your otherworldly patron bestows a gift upon you for your loyal service. "},
                          4: {'Ability Score Improvement': "When you reach 4th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          8: {'Ability Score Improvement': "When you reach 8th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          11: {'Mystic Arcanum': "At 11th level, your patron bestows upon you a magical secret called an arcanum. Choose one 6th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nAt higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest."},
                          12: {'Ability Score Improvement': "When you reach 12th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          13: {'Mystic Arcanum': "At 13th level, your patron bestows upon you a magical secret called an arcanum. Choose one 7th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again."},
                          15: {'Mystic Arcanum': "At 15th level, your patron bestows upon you a magical secret called an arcanum. Choose one 8th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again."},
                          16: {'Ability Score Improvement': "When you reach 16th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          17: {'Mystic Arcanum': "At 17th level, your patron bestows upon you a magical secret called an arcanum. Choose one 9th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again."},
                          19: {'Ability Score Improvement': "When you reach 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          20: {'Eldritch Master': "At 20th level, you can draw on your inner reserve of mystical power while entreating your patron to regain expended spell slots. You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature. Once you regain spell slots with this feature, you must finish a long rest before you can do so again."}}

        if not mc:
            self.saves[4] = 1 # WIS
            self.saves[5] = 1 # CHA

            self.toolprofs = []

            self.skillsinfo = []
            self.skillschoose = [2, ['Arcana', 'Deception', 'History',
                                 'Intimidation', 'Investigation', 'Nature', 'Religion']]

            self.otherprofs = ['Light', 'Simple']

            return True
        elif mc and np.and(stats > (multiclassing * 13)):
            self.otherprofs = ['Light', 'Simple']

            return True

        else:
            return False
