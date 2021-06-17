import numpy as np

class Rogue(ClassParent):
    def __init__(self, mc, stats):
        ClassParent.__init__(self, mc)

        self.hitdie = '1d8'
        self.multiclassing = [0, 1, 0, 0, 0, 0]
        self.subclass = ''
        self.abilities = {1: {'Expertise': "At 1st level, choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.\nAt 6th level, you can choose two more of your proficiencies (in skills or with thieves' tools) to gain this benefit.",
                              'Sneak Attack': "Beginning at 1st level, you know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.\nYou don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.\nThe amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table.",
                              "Thieves' Cant": "During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.\nIn addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run."},
                          2: {'Cunning Action': "Starting at 2nd level, your quick thinking and agility allow you to move and act quickly. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action."},
                          3: {'Roguish Archetype': "At 3rd level, you choose an archetype that you emulate in the exercise of your rogue abilities from the list of available archetypes. Your archetype choice grants you features at 3rd level and then again at 9th, 13th, and 17th level."},
                          4: {'Ability Score Improvement': "When you reach 4th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          5: {'Uncanny Dodge': "Starting at 5th level, when an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you."},
                          6: {'Expertise': "At 6th level, you can choose two more of your proficiencies (in skills or with thieves' tools) to gain the benefit of Expertise."},
                          7: {'Evasion': "Beginning at 7th level, you can nimbly dodge out of the way of certain area effects, such as a red dragon's fiery breath or an ice storm spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail."},
                          8: {'Ability Score Improvement': "When you reach 8th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          10: {'Ability Score Improvement': "When you reach 8th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          11: {'Reliable Talent': "By 11th level, you have refined your chosen skills until they approach perfection. Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10."},
                          12: {'Ability Score Improvement': "When you reach 10th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          14: {'Blindsense': "Starting at 14th level, if you are able to hear, you are aware of the location of any hidden or invisible creature within 10 feet of you."},
                          15: {'Slippery Mind': "By 15th level, you have acquired greater mental strength. You gain proficiency in Wisdom saving throws."},
                          16: {'Ability Score Improvement': "When you reach 16th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          18: {'Elusive': "Beginning at 18th level, you are so evasive that attackers rarely gain the upper hand against you. No attack roll has advantage against you while you aren't incapacitated."},
                          19: {'Ability Score Improvement': "When you reach 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat."},
                          20: {'Stroke of Luck': "At 20th level, you have an uncanny knack for succeeding when you need to. If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20.\nOnce you use this feature, you can't use it again until you finish a short or long rest."}}

        if not mc:
            self.saves[3] = 1 # INT
            self.saves[1] = 1 # DEX

            self.toolprofs = ["Thieves' Tools"]

            self.skillsinfo = []
            self.skillschoose = [3, ['Acrobatics', 'Athletics', 'Deception',
                                 'Insight', 'Intimidation', 'Investigation'
                                 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']]

            self.otherprofs = ['Simple', 'Hand Crossbow', 'Light', 'Longsword', 'Shortsword', 'Rapier']
            return True

        elif mc and np.and(stats > (multiclassing * 13)):
            self.toolprofs = ["Thieves' Tools"]

            self.skillschoose = [1, ['Acrobatics', 'Athletics', 'Deception',
                                 'Insight', 'Intimidation', 'Investigation'
                                 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']]

            self.otherprofs = ['Light']

            return True

        else:
            return False
