
# SPELL TEMPLATE:
# SpellID = {'NAME': 'spell name',
# 'LEVEL': 0-9,
# 'SCHOOL': "magic school",
# 'CASTTIME': 'Action',
# 'RANGE': "60 feet",
# 'COMP': [True, False, True],
# 'MATERIALS': "a leaf"
# 'RITUAL': True/False,
# 'CONC': True/False,
# 'SCHOOL': "magic school",
# 'DURATION': 'Instantaneous',
# 'DAMAGETYPE': ["Acid", "Cold"],
# 'COND': ["Blinded"],
# 'SPELLATTCK': "Ranged/Melee/Other",
# 'SAVETYPE': "STR/DEX/..."
# 'TARGETS': "Single Target", "Multiple Targets", Circle, Cone, Cube, Cylinder, Hemisphere, Line, Sphere, Square, Wall
# "TAGS": ["Utility/Telportation/Buff/Damage/Healing/Social/Control/Communication/Environment/Warding,Shapechanging/Debuff/Negation"]
# 'DESCRIPT': "stuff",
# 'HIGHERLEVEL': "more stuff"
# 'REQSIGHT': True/False}


#### ------------------------- CANTRIPS ---------------------- ####

ACIDSPLASH = {"NAME": "Acid Splash",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Acid"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You hurl a bubble of acid. Choose one creature you can see within "
            "range, or choose two creatures you can see within range that are "
            "within 5 feet of each other. A target must succeed on a Dexterity "
            "saving throw or take 1d6 acid damage. \nThis spell's damage"
            " increases by 1d6 when you reach 5th level (2d6), 11th level (3d6)"
            ", and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

BLADEWARD = {"NAME": "Blade Ward",
"LEVEL": 0,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Self",
"TAG": ["Warding", "Combat"],
"DESCRIPT": "You extend your hand and trace a sigil of warding in the air. "
            "Until the end of your next turn, you have resistance against "
            "bludgeoning, piercing, and slashing damage dealt by weapon attacks.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

BOOMINGBLADE = {"NAME": "Booming Blade",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (5-foot Radius)",
"COMP": [True, False, True],
"MATERIALS": "a melee weapon worth at least 1 sp",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": ["Thunder"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You brandish the weapon used in the spell's casting and make a "
            "melee attack with it against one creature within 5 feet of you. "
            "On a hit, the target suffers the weapon attack's normal effects "
            "and then becomes sheathed in booming energy until the start of "
            "your next turn. If the target willingly moves 5 feet or more "
            "before then, the target takes 1d8 thunder damage, and the spell ends."
            "/nThis spell's damage increases when you reach certain levels."
            " At 5th level, the melee attack deals an extra 1d8 thunder damage "
            "to the target on a hit, and the damage the target takes for moving "
            "increases to 2d8. Both damage rolls increase by 1d8 at 11th level "
            "(2d8 and 3d8) and again at 17th level (3d8 and 4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

CHILLTOUCH = {"NAME": "Chill Touch",
"LEVEL": 0,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": ["Necrotic"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "You create a ghostly, skeletal hand in the space of a creature "
            "within range. Make a ranged spell attack against the creature to "
            "assail it with the chill of the grave. On a hit, the target takes "
            "1d8 necrotic damage, and it can't regain hit points until the start"
            " of your next turn. Until then, the hand clings to the target.\n"
            "If you hit an undead target, it also has disadvantage on attack "
            "rolls against you until the end of your next turn.\nThis spell's "
            "damage increases by 1d8 when you reach 5th level (2d8), 11th level"
            " (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

CONTROLFLAMES = {"NAME": "Control Flames",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous or 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Cube",
"TAG": ["Control"],
"DESCRIPT": "You choose nonmagical flame that you can see within range and that "
            "fits within a 5-foot cube. You affect it in one of the following "
            "ways:\n-You instantaneously expand the flame 5 feet in one "
            "direction, provided that wood or other fuel is present in the new "
            "location.\n-You instantaneously extinguish the flames within the "
            "cube.\n-You double or halve the area of bright light and dim light "
            "cast by the flame, change its color, or both. The change lasts for "
            "1 hour.\n-You cause simple shapes—such as the vague form of a "
            "creature, an inanimate object, or a location—to appear within the "
            "flames and animate as you like. The shapes last for 1 hour.\n"
            "If you cast this spell multiple times, you can have up to three "
            "non-instantaneous effects created by it active at a time, and you "
            "can dismiss such an effect as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

CREATEBONFIRE = {"NAME": "Create Bonfire",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Cube",
"TAG": ["Damage", "Control"],
"DESCRIPT": "You create a bonfire on ground that you can see within range. "
            "Until the spell ends, the magic bonfire fills a 5-foot cube. Any "
            "creature in the bonfire's space when you cast the spell must "
            "succeed on a Dexterity saving throw or take 1d8 fire damage. A "
            "creature must also make the saving throw when it moves into the "
            "bonfire's space for the first time on a turn or ends its turn "
            "there.\nThe bonfire ignites flammable objects in its area that "
            "aren't being worn or carried.\nThe spell's damage increases by 1d8 "
            "when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

DANCINGLIGHTS = {"NAME": "Dancing Lights",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, True],
"MATERIALS": "a bit of phosphorus or wychwood, or a glowworm",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "You create up to four torch-sized lights within range, making them "
            "appear as torches, lanterns, or glowing orbs that hover in the air "
            "for the duration. You can also combine the four lights into one "
            "glowing vaguely humanoid form of Medium size. Whichever form you "
            "choose, each light sheds dim light in a 10-foot radius.\nAs a "
            "bonus action on your turn, you can move the lights up to 60 feet "
            "to a new spot within range. A light must be within 20 feet of "
            "another light created by this spell, and a light winks out if it "
            "exceeds the spell's range.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DRUIDCRAFT = {"NAME": "Druidcraft",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Control"],
"DESCRIPT": "Whispering to the spirits of nature, you create one of the "
            "following effects within range:\n-You create a tiny, harmless "
            "sensory effect that predicts what the weather will be at your "
            "location for the next 24 hours. The effect might manifest as a "
            "golden orb for clear skies, a cloud for rain, falling snowflakes "
            "for snow, and so on. This effect persists for 1 round.\n-You "
            "instantly make a flower blossom, a seed pod open, or a leaf bud "
            "bloom.\n-You create an instantaneous, harmless sensory effect, "
            "such as falling leaves, a puff of wind, the sound of a small "
            "animal, or the faint odor of skunk. The effect must fit in a "
            "5-foot cube.\n-You instantly light or snuff out a candle, a torch"
            ", or a small campfire.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ELDRITCHBLAST = {"NAME": "Eldritch Blast",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Force"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "A beam of crackling energy streaks toward a creature within range. "
            "Make a ranged spell attack against the target. On a hit, the "
            "target takes 1d10 force damage.\nThe spell creates more than one "
            "beam when you reach higher levels: two beams at 5th level, three "
            "beams at 11th level, and four beams at 17th level. You can direct "
            "the beams at the same target or at different ones. Make a "
            "separate attack roll for each beam.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ENCODETHOUGHTS = {"NAME": "Encode Thoughts",
"LEVEL": 0,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "Putting a finger to your head, you pull a memory, an idea, or a "
            "message from your mind and transform it into a tangible string of "
            "glowing energy called a thought strand, which persists for the "
            "duration or until you cast this spell again. The thought strand "
            "appears in an unoccupied space within 5 feet of you as a Tiny, "
            "weightless, semisolid object that can be held and carried like a "
            "ribbon. It is otherwise stationary.\nIf you cast this spell while "
            "concentrating on a spell or an ability that allows you to read or "
            "manipulate the thoughts of others (such as detect thoughts or "
            "modify memory), you can transform the thoughts or memories you "
            "read, rather than your own, into a thought strand.\nCasting this "
            "spell while holding a thought strand allows you to instantly "
            "receive whatever memory, idea, or message the thought strand "
            "contains. (Casting detect thoughts on the strand has the same effect.)",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FIREBOLT = {"NAME": "Fire Bolt",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You hurl a mote of fire at a creature or object within range. Make "
            "a ranged spell attack against the target. On a hit, the target "
            "takes 1d10 fire damage. A flammable object hit by this spell "
            "ignites if it isn't being worn or carried.\nThis spell's damage "
            "increases by 1d10 when you reach 5th level (2d10), 11th level "
            "(3d10), and 17th level (4d10).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FRIENDS = {"NAME": "Friends",
"LEVEL": 0,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [False, True, True],
"MATERIALS": "a small amount of makeup applied to the face as this spell is cast",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Social", "Buff", "Deception"],
"DESCRIPT": "For the duration, you have advantage on all Charisma checks "
            "directed at one creature of your choice that isn't hostile toward "
            "you. When the spell ends, the creature realizes that you used "
            "magic to influence its mood and becomes hostile toward you. A "
            "creature prone to violence might attack you. Another creature "
            "might seek retribution in other ways (at the DM's discretion), "
            "depending on the nature of your interaction with it.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FROSTBITE = {"NAME": "Frostbite",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Cold"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "You cause numbing frost to form on one creature that you can see "
            "within range. The target must make a Constitution saving throw. "
            "On a failed save, the target takes 1d6 cold damage, and it has "
            "disadvantage on the next weapon attack roll it makes before the "
            "end of its next turn.\nThe spell's damage increases by 1d6 when "
            "you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

GREENFLAMEBLADE = {"NAME": "Green-Flame Blade",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (5-foot radius)",
"COMP": [True, False, True],
"MATERIALS": "a melee weapon worth at least 1 sp",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Damage", "Combat"],
"DESCRIPT": "You brandish the weapon used in the spell's casting and make a "
            "melee attack with it against one creature within 5 feet of you. "
            "On a hit, the target suffers the weapon attack's normal effects, "
            "and you can cause green fire to leap from the target to a "
            "different creature of your choice that you can see within 5 feet "
            "of it. The second creature takes fire damage equal to your "
            "spellcasting ability modifier.\nThis spell's damage increases "
            "when you reach certain levels. At 5th level, the melee attack "
            "deals an extra 1d8 fire damage to the target on a hit, and the "
            "fire damage to the second creature increases to 1d8 + your "
            "spellcasting ability modifier. Both damage rolls increase by 1d8 "
            "at 11th level (2d8 and 2d8) and 17th level (3d8 and 3d8).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GUIDANCE = {"NAME": "Guidance",
"LEVEL": 0,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You touch one willing creature. Once before the spell ends, the "
            "target can roll a d4 and add the number rolled to one ability "
            "check of its choice. It can roll the die before or after making "
            "the ability check. The spell then ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GUST = {"NAME": "Gust",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Single Target",
"TAG": ["Control"],
"DESCRIPT": "You seize the air and compel it to create one of the following "
            "effects at a point you can see within range:\n-One Medium or "
            "smaller creature that you choose must succeed on a Strength saving "
            "throw or be pushed up to 5 feet away from you.\n-You create a "
            "small blast of air capable of moving one object that is neither "
            "held nor carried and that weighs no more than 5 pounds. The object "
            "is pushed up to 10 feet away from you. It isn't pushed with enough "
            "force to cause damage.\n-You create a harmless sensory effect using "
            "air, such as causing leaves to rustle, wind to slam shutters "
            "closed, or your clothing to ripple in a breeze.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

INFESTATION = {"NAME": "Infestation",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a living flea",
"COMP": "V, S, M (a living flea)",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Poison"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Damage", "Control"],
"DESCRIPT": "You cause a cloud of mites, fleas, and other parasites to appear "
            "momentarily on one creature you can see within range. The target "
            "must succeed on a Constitution saving throw, or it takes 1d6 "
            "poison damage and moves 5 feet in a random direction if it can "
            "move and its speed is at least 5 feet. Roll a d4 for the "
            "direction: 1, north; 2, south; 3, east; or 4, west. This movement "
            "doesn't provoke opportunity attacks, and if the direction rolled "
            "is blocked, the target doesn't move.\nThe spell's damage increases "
            "by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

LIGHT = {"NAME": "Light",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, False, True],
"MATERIALS": "a firefly or phosphorescent moss",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "You touch one object that is no larger than 10 feet in any "
            "dimension. Until the spell ends, the object sheds bright light in "
            "a 20-foot radius and dim light for an additional 20 feet. The "
            "light can be colored as you like. Completely covering the object "
            "with something opaque blocks the light. The spell ends if you cast "
            "it again or dismiss it as an action.\nIf you target an object "
            "held or worn by a hostile creature, that creature must succeed on "
            "a Dexterity saving throw to avoid the spell.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

LIGHTNINGLURE = {"NAME": "Lightning Lure",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (15-foot radius)",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Lightning"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Single Target",
"TAG": ["Damage", "Control"],
"DESCRIPT": "You create a lash of lightning energy that strikes at one creature "
            "of your choice that you can see within 15 feet of you. The target "
            "must succeed on a Strength saving throw or be pulled up to 10 feet "
            "in a straight line toward you and then take 1d8 lightning damage "
            "if it is within 5 feet of you.\nThis spell's damage increases by "
            "1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

MAGEHAND = {"NAME": "Mage Hand",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "A spectral, floating hand appears at a point you choose within "
            "range. The hand lasts for the duration or until you dismiss it as "
            "an action. The hand vanishes if it is ever more than 30 feet away "
            "from you or if you cast this spell again.\nYou can use your action "
            "to control the hand. You can use the hand to manipulate an object, "
            "open an unlocked door or container, stow or retrieve an item from "
            "an open container, or pour the contents out of a vial. You can "
            "move the hand up to 30 feet each time you use it.\nThe hand can't "
            "attack, activate magic items, or carry more than 10 pounds.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MAGICSTONE = {"NAME": "Magic Stone",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": ["Bludgeoning"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You touch one to three pebbles and imbue them with magic. You or "
            "someone else can make a ranged spell attack with one of the pebbles "
            "by throwing it or hurling it with a sling. If thrown, a pebble has "
            "a range of 60 feet. If someone else attacks with a pebble, that "
            "attacker adds your spellcasting ability modifier, not the "
            "attacker's, to the attack roll. On a hit, the target takes "
            "bludgeoning damage equal to 1d6 + your spellcasting ability "
            "modifier. Whether the attack hits or misses, the spell then ends "
            "on the stone.\nIf you cast this spell again, the spell ends on "
            "any pebbles still affected by your previous casting.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MENDING = {"NAME": "Mending",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Minute",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "two lodestones",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "This spell repairs a single break or tear in an object you touch, "
            "such as broken chain link, two halves of a broken key, a torn "
            "cloak, or a leaking wineskin. As long as the break or tear is no "
            "larger than 1 foot in any dimension, you mend it, leaving no "
            "trace of the former damage.\nThis spell can physically repair a "
            "magic item or construct, but the spell can't restore magic to such an object.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MESSAGE = {"NAME": "Message",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, True],
"MATERIALS": "a short piece of copper wire",
"RITUAL": False,
"CONC": False,
"DURATION": "1 round",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Communication", "Social", "Utility"],
"DESCRIPT": "You point your finger toward a creature within range and whisper "
            "a message. The target (and only the target) hears the message and "
            "can reply in a whisper that only you can hear.\nYou can cast this "
            "spell through solid objects if you are familiar with the target "
            "and know it is beyond the barrier. Magical silence, 1 foot of "
            "stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of "
            "wood blocks the spell. The spell doesn't have to follow a straight "
            "line and can travel freely around corners or through openings.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MINDSLIVER = {"NAME": "Mind Sliver",
"LEVEL": 0,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 round",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "INT",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "You drive a disorienting spike of psychic energy into the mind of "
            "one creature you can see within range. The target must succeed on "
            "an Intelligence saving throw or take 1d6 psychic damage and "
            "subtract 1d4 from the next saving throw it makes before the end "
            "of your next turn.\nThis spell's damage increases by 1d6 when you "
            "reach certain levels: 5th level (2d6), 11th level (3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

MINORILLUSION = {"NAME": "Minor Illusion",
"LEVEL": 0,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [False, True, True],
"MATERIALS": "a bit of fleece",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Control"],
"DESCRIPT": "You create a sound or an image of an object within range that "
            "lasts for the duration. The illusion also ends if you dismiss it "
            "as an action or cast this spell again.\nIf you create a sound, "
            "its volume can range from a whisper to a scream. It can be your "
            "voice, someone else's voice, a lion's roar, a beating of drums, "
            "or any other sound you choose. The sound continues unabated "
            "throughout the duration, or you can make discrete sounds at "
            "different times before the spell ends.\nIf you create an image of "
            "an object—such as a chair, muddy footprints, or a small chest—it "
            "must be no larger than a 5-foot cube. The image can't create "
            "sound, light, smell, or any other sensory effect. Physical "
            "interaction with the image reveals it to be an illusion, "
            "because things can pass through it.\nIf a creature uses its action "
            "to examine the sound or image, the creature can determine that it "
            "is an illusion with a successful Intelligence (Investigation) "
            "check against your spell save DC. If a creature discerns the "
            "illusion for what it is, the illusion becomes faint to the creature.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MOLDEARTH = {"NAME": "Mold Earth",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous or 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Cube",
"TAG": ["Control"],
"DESCRIPT": "You choose a portion of dirt or stone that you can see within "
            "range and that fits within a 5-foot cube. You manipulate it in "
            "one of the following ways:\n-If you target an area of loose earth, "
            "you can instantaneously excavate it, move it along the ground, and "
            "deposit it up to 5 feet away. This movement doesn't involve enough "
            "force to cause damage.\n-You cause shapes, colors, or both to "
            "appear on the dirt or stone, spelling out words, creating images, "
            "or shaping patterns. The changes last for 1 hour.\n-If the dirt "
            "or stone you target is on the ground, you cause it to become "
            "difficult terrain. Alternatively, you can cause the ground to "
            "become normal terrain if it is already difficult terrain. This "
            "change lasts for 1 hour.\nIf you cast this spell multiple times, "
            "you can have no more than two of its non-instantaneous effects "
            "active at a time, and you can dismiss such an effect as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

POISONSPRAY = {"NAME": "Poison Spray",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "10 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Poison"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You extend your hand toward a creature you can see within range "
            "and project a puff of noxious gas from your palm. The creature "
            "must succeed on a Constitution saving throw or take 1d12 poison "
            "damage.\nThis spell's damage increases by 1d12 when you reach 5th "
            "level (2d12), 11th level (3d12), and 17th level (4d12).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

PRESTIDIGITATION = {"NAME": "Prestidigitation",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "10 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "This spell is a minor magical trick that novice spellcasters use "
            "for practice. You create one of the following magical effects "
            "within range:\n-You create an instantaneous, harmless sensory "
            "effect, such as a shower of sparks, a puff of wind, faint musical "
            "notes, or an odd odor.\n-You instantaneously light or snuff out a "
            "candle, a torch, or a small campfire.\n-You instantaneously clean "
            "or soil an object no larger than 1 cubic foot.\n-You chill, warm, "
            "or flavor up to 1 cubic foot of nonliving material for 1 hour.\n-"
            "You make a color, a small mark, or a symbol appear on an object "
            "or a surface for 1 hour.\n-You create a nonmagical trinket or an "
            "illusory image that can fit in your hand and that lasts until the "
            "end of your next turn.\nIf you cast this spell multiple times, "
            "you can have up to three of its non-instantaneous effects active "
            "at a time, and you can dismiss such an effect as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

PRIMALSAVAGERY = {"NAME": "Primal Savagery",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Acid"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You channel primal magic to cause your teeth or fingernails to "
            "sharpen, ready to deliver a corrosive attack. Make a melee spell "
            "attack against one creature within 5 feet of you. On a hit, the "
            "target takes 1d10 acid damage. After you make the attack, your "
            "teeth or fingernails return to normal.\nThe spell's damage "
            "increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

PRODUCEFLAME = {"NAME": "Produce Flame",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "Self or 30 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "10 minutes",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Utility"],
"DESCRIPT": "A flickering flame appears in your hand. The flame remains there "
            "for the duration and harms neither you nor your equipment. The "
            "flame sheds bright light in a 10-foot radius and dim light for an "
            "additional 10 feet. The spell ends if you dismiss it as an action "
            "or if you cast it again.\nYou can also attack with the flame, "
            "although doing so ends the spell. When you cast this spell, or as "
            "an action on a later turn, you can hurl the flame at a creature "
            "within 30 feet of you. Make a ranged spell attack. On a hit, the "
            "target takes 1d8 fire damage.\nThis spell's damage increases by "
            "1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

RAYOFFROST = {"NAME": "Ray Of Frost",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Cold"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "A frigid beam of blue-white light streaks toward a creature within "
            "range. Make a ranged spell attack against the target. On a hit, it "
            "takes 1d8 cold damage, and its speed is reduced by 10 feet until "
            "the start of your next turn.\nThe spell's damage increases by 1d8 "
            "when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

RESISTANCE = {"NAME": "Resistance",
"LEVEL": 0,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a miniature cloak",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You touch one willing creature. Once before the spell ends, the "
            "target can roll a d4 and add the number rolled to one saving throw "
            "of its choice. It can roll the die before or after making the "
            "saving throw. The spell then ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SACREDFLAME = {"NAME": "Sacred Flame",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Radiant"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "Flame-like radiance descends on a creature that you can see within "
            "range. The target must succeed on a Dexterity saving throw or take "
            "1d8 radiant damage. The target gains no benefit from cover for "
            "this saving throw.\nThe spell's damage increases by 1d8 when you "
            "reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

SAPPINGSTING = {"NAME": "Sapping Sting",
"LEVEL": 0,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Necrotic"],
"COND": ["Prone"],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You sap the vitality of one creature you can see in range. The "
            "target must succeed on a Constitution saving throw or take 1d4 "
            "necrotic damage and fall prone.\nThis spell's damage increases by "
            "1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

SHAPEWATER = {"NAME": "Shape Water",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous or 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Cube",
"TAG": ["Control"],
"DESCRIPT": "You choose an area of water that you can see within range and that "
            "fits within a 5-foot cube. You manipulate it in one of the "
            "following ways:\n-You instantaneously move or otherwise change the "
            "flow of the water as you direct, up to 5 feet in any direction. "
            "This movement doesn't have enough force to cause damage.\n-You "
            "cause the water to form into simple shapes and animate at your "
            "direction. This change lasts for 1 hour.\n-You change the water's "
            "color or opacity. The water must be changed in the same way "
            "throughout. This change lasts for 1 hour.\n-You freeze the water, "
            "provided that there are no creatures in it. The water unfreezes "
            "in 1 hour.\nIf you cast this spell multiple times, you can have "
            "no more than two of its non-instantaneous effects active at a "
            "time, and you can dismiss such an effect as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

SHILLELAGH = {"NAME": "Shillelagh",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "mistletoe, a shamrock leaf, and a club or quarterstaff",
"COMP": "V, S, M (mistletoe, a shamrock leaf, and a club or quarterstaff)",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": ["Bludgeoning"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Buff"],
"DESCRIPT": "The wood of a club or quarterstaff you are holding is imbued with "
            "nature's power. For the duration, you can use your spellcasting "
            "ability instead of Strength for the attack and damage rolls of "
            "melee attacks using that weapon, and the weapon's damage die "
            "becomes a d8. The weapon also becomes magical, if it isn't "
            "already. The spell ends if you cast it again or if you let go of the weapon.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SHOCKINGGRASP = {"NAME": "Shocking Grasp",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Lightning"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "Lightning springs from your hand to deliver a shock to a creature "
            "you try to touch. Make a melee spell attack against the target. "
            "You have advantage on the attack roll if the target is wearing "
            "armor made of metal. On a hit, the target takes 1d8 lightning "
            "damage, and it can't take reactions until the start of its next "
            "turn.\nThe spell's damage increases by 1d8 when you reach 5th "
            "level (2d8), 11th level (3d8), and 17th level (4d8).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SPARETHEDYING = {"NAME": "Spare The Dying",
"LEVEL": 0,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Healing"],
"DESCRIPT": "You touch a living creature that has 0 hit points. The creature"
            "becomes stable. This spell has no effect on undead or constructs.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SWORDBURST = {"NAME": "Sword Burst",
"LEVEL": 0,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "Self (5-foot radius)",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Force"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You create a momentary circle of spectral blades that sweep around "
            "you. All other creatures within 5 feet of you must succeed on a "
            "Dexterity saving throw or take 1d6 force damage.\nThis spell's "
            "damage increases by 1d6 when you reach 5th level (2d6), 11th level "
            "(3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

THAUMATURGY = {"NAME": "Thaumaturgy",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Utility"],
"DESCRIPT": "You manifest a minor wonder, a sign of supernatural power, "
            "within range. You create one of the following magical effects "
            "within range:\n-Your voice booms up to three times as loud as "
            "normal for 1 minute.\n-You cause flames to flicker, brighten, dim, "
            "or change color for 1 minute.\n-You cause harmless tremors in the "
            "ground for 1 minute.\n-You create an instantaneous sound that "
            "originates from a point of your choice within range, such as a "
            "rumble of thunder, the cry of a raven, or ominous whispers.\n-You "
            "instantaneously cause an unlocked door or window to fly open or "
            "slam shut.\n-You alter the appearance of your eyes for 1 minute.\n"
            "If you cast this spell multiple times, you can have up to three of "
            "its 1-minute effects active at a time, and you can dismiss such an effect as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

THORNWHIP = {"NAME": "Thorn Whip",
"LEVEL": 0,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "the stem of a plant with thorns",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Piercing"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Control"],
"DESCRIPT": "You create a long, vine-like whip covered in thorns that lashes "
            "out at your command toward a creature in range. Make a melee spell "
            "attack against the target. If the attack hits, the creature takes "
            "1d6 piercing damage, and if the creature is Large or smaller, you "
            "pull the creature up to 10 feet closer to you.\nThis spell's "
            "damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

THUNDERCLAP = {"NAME": "Thunderclap",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "5 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Thunder"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You create a burst of thunderous sound that can be heard up to "
            "100 feet away. Each creature within range, other than you, must "
            "make a Constitution saving throw or take 1d6 thunder damage.\nThe "
            "spell's damage increases by 1d6 when you reach 5th level (2d6), "
            "11th level (3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

TOLLTHEDEAD = {"NAME": "Toll The Dead",
"LEVEL": 0,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Necrotic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You point at one creature you can see within range, and the sound "
            "of a dolorous bell fills the air around it for a moment. The target "
            "must succeed on a Wisdom saving throw or take 1d8 necrotic damage. "
            "If the target is missing any of its hit points, it instead takes "
            "1d12 necrotic damage.\nThe spell's damage increases by one die when "
            "you reach 5th level (2d8 or 2d12), 11th level (3d8 or 3d12), and 17th level (4d8 or 4d12).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

TRUESTRIKE = {"NAME": "True Strike",
"LEVEL": 0,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 round",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You extend your hand and point a finger at a target in range. "
            "Your magic grants you a brief insight into the target's defenses. "
            "On your next turn, you gain advantage on your first attack roll "
            "against the target, provided that this spell hasn't ended.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

VICIOUSMOCKERY = {"NAME": "Vicious Mockery",
"LEVEL": 0,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "You unleash a string of insults laced with subtle enchantments at "
            "a creature you can see within range. If the target can hear you "
            "(though it need not understand you), it must succeed on a Wisdom "
            "saving throw or take 1d4 psychic damage and have disadvantage on "
            "the next attack roll it makes before the end of its next turn.\n"
            "This spell's damage increases by 1d4 when you reach 5th level "
            "(2d4), 11th level (3d4), and 17th level (4d4).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

WORDOFRADIANCE = {"NAME": "Word Of Radiance",
"LEVEL": 0,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "5 feet",
"COMP": [True, False, True],
"MATERIALS": "a holy symbol",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Radiant"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You utter a divine word, and burning radiance erupts from you. "
            "Each creature of your choice that you can see within range must "
            "succeed on a Constitution saving throw or take 1d6 radiant damage."
            "\nThe spell's damage increases by 1d6 when you reach 5th level "
            "(2d6), 11th level (3d6), and 17th level (4d6).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}


#### ------------------------- 1ST LEVEL ---------------------- ####

ABSORBELEMENTS = {"NAME": "Absorb Elements",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 reaction, which you take when you take acid, cold, fire, lightning, or thunder damage",
"RANGE": "Self",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": ["Acid", "Cold", "Fire", "Lightning", "Thunder"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Buff"],
"DESCRIPT": "The spell captures some of the incoming energy, lessening its effect "
            "on you and storing it for your next melee attack. You have resistance "
            "to the triggering damage type until the start of your next turn. Also, "
            "the first time you hit with a melee attack on your next turn, the "
            "target takes an extra 1d6 damage of the triggering type, and the spell ends.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

ALARM = {"NAME": "Alarm",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 minute",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a tiny bell and a piece of fine silver wire",
"RITUAL": True,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "",
"TAG": ["Detection", "Utility"],
"DESCRIPT": "You set an alarm against unwanted intrusion. Choose a door, a window, "
            "or an area within range that is no larger than a 20-foot cube. "
            "Until the spell ends, an alarm alerts you whenever a Tiny or "
            "larger creature touches or enters the warded area. When you cast "
            "the spell, you can designate creatures that won't set off the alarm. "
            "You also choose whether the alarm is mental or audible.\nA mental "
            "alarm alerts you with a ping in your mind if you are within 1 mile "
            "of the warded area. This ping awakens you if you are sleeping.\n"
            "An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ANIMALFRIENDSHIP = {"NAME": "Animal Friendship",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a morsel of food",
"RITUAL": False,
"CONC": False,
"DURATION": "24 hours",
"DAMAGETYPE": [],
"COND": [Charmed],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Social"],
"DESCRIPT": "This spell lets you convince a beast that you mean it no harm. "
            "Choose a beast that you can see within range. It must see and hear "
            "you. If the beast's Intelligence is 4 or higher, the spell fails. "
            "Otherwise, the beast must succeed on a Wisdom saving throw or be "
            "charmed by you for the spell's duration. If you or one of your "
            "companions harms the target, the spell ends.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional beast for each slot level above 1st.",
"REQSIGHT": True
}

ARMOROFAGATHYS = {"NAME": "Armor Of Agathys",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a cup of water",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hours",
"DAMAGETYPE": ["Cold"],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Warding", "Buff"],
"DESCRIPT": "A protective magical force surrounds you, manifesting as a spectral "
            "frost that covers you and your gear. You gain 5 temporary hit points "
            "for the duration. If a creature hits you with a melee attack while "
            "you have these hit points, the creature takes 5 cold damage.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or "
               "higher, both the temporary hit points and the cold damage increase by 5 for each slot level above 1st.",
"REQSIGHT": False
}

ARMSOFHADAR = {"NAME": "Arms Of Hadar",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "Self(10-foot radius)",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Necrotic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Mulitple Targets",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "You invoke the power of Hadar, the Dark Hunger. Tendrils of dark "
            "energy erupt from you and batter all creatures within 10 feet of "
            "you. Each creature in that area must make a Strength saving throw. "
            "On a failed save, a target takes 2d6 necrotic damage and can't take "
            "reactions until its next turn. On a successful save, the creature "
            "takes half damage, but suffers no other effect.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

BANE = {"NAME": "Bane",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a drop of blood",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CHA",
"TARGETS": "Multiple Targets",
"TAG": ["Debuff"],
"DESCRIPT": "Up to three creatures of your choice that you can see within range "
            "must make Charisma saving throws. Whenever a target that fails this "
            "saving throw makes an attack roll or a saving throw before the "
            "spell ends, the target must roll a d4 and subtract the number "
            "rolled from the attack roll or saving throw.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.",
"REQSIGHT": True
}

BEASTBOND = {"NAME": "Beast Bond",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a bit of fur wrapped in a cloth",
"RITUAL": False,
"CONC": True,
"DURATION": "up to 10 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Communication", "Buff"],
"DESCRIPT": "You establish a telepathic link with one beast you touch that is "
            "friendly to you or charmed by you. The spell fails if the beast's "
            "Intelligence score is 4 or higher. Until the spell ends, the link "
            "is active while you and the beast are within line of sight of each "
            "other. Through the link, the beast can understand your telepathic "
            "messages to it, and it can telepathically communicate simple emotions "
            "and concepts back to you. While the link is active, the beast gains "
            "advantage on attack rolls against any creature within 5 feet of you "
            "that you can see.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

BLESS = {"NAME": "Bless",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a sprinkling of holy water",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Mulitple Targets",
"TAG": ["Buff"],
"DESCRIPT": "You bless up to three creatures of your choice within range. Whenever "
            "a target makes an attack roll or a saving throw before the spell ends, "
            "the target can roll a d4 and add the number rolled to the attack roll "
            "or saving throw.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.",
"REQSIGHT": False
}

BURNINGHANDS = {"NAME": "Burning Hands",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (15-foot cone)",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Cone",
"TAG": ["Damage"],
"DESCRIPT": "As you hold your hands with thumbs touching and fingers spread, a "
            "thin sheet of flames shoots forth from your outstretched fingertips. "
            "Each creature in a 15-foot cone must make a Dexterity saving throw. "
            "A creature takes 3d6 fire damage on a failed save, or half as much "
            "damage on a successful one.\nThe fire ignites any flammable objects "
            "in the area that aren't being worn or carried.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

CATAPULT = {"NAME": "Catapult",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Bludgeoning"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Line",
"TAG": ["Damage"],
"DESCRIPT": "Choose one object weighing 1 to 5 pounds within range that isn't "
            "being worn or carried. The object flies in a straight line up to 90 "
            "feet in a direction you choose before falling to the ground, stopping "
            "early if it impacts against a solid surface. If the object would "
            "strike a creature, that creature must make a Dexterity saving throw. "
            "On a failed save, the object strikes the target and stops moving. "
            "When the object strikes something, the object and what it strikes "
            "each take 3d8 bludgeoning damage.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the maximum weight of objects that you can target with this spell increases by 5 pounds, and the damage increases by 1d8, for each slot level above 1st.",
"REQSIGHT": False
}

CAUSEFEAR = {"NAME": "Cause Fear",
"LEVEL": 1,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": ["Frightened"],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You awaken the sense of mortality in one creature you can see within "
            "range. A construct or an undead is immune to this effect. The target "
            "must succeed on a Wisdom saving throw or become frightened of you until "
            "the spell ends. The frightened target can repeat the saving throw at "
            "the end of each of its turns, ending the effect on itself on a success.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.",
"REQSIGHT": True
}

CEREMONY = {"NAME": "Ceremony",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Hour",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "25 gp worth of powdered silver, which the spell consumes",
"RITUAL": True,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You perform a special religious ceremony that is infused with magic. "
            "When you cast the spell, choose one of the following rites, the target "
            "of which must be within 10 feet of you throughout the casting.\n"
            "Atonement. You touch one willing creature whose alignment has changed, "
            "and you make a DC 20 Wisdom (Insight) check. On a successful check, "
            "you restore the target to its original alignment.\nBless Water. You "
            "touch one vial of water and cause it to become holy water.\nComing "
            "of Age. You touch one humanoid who is a young adult. For the next 24 "
            "hours, whenever the target makes an ability check, it can roll a d4 "
            "and add the number rolled to the ability check. A creature can benefit "
            "from this rite only once.\nDedication. You touch one humanoid who "
            "wishes to be dedicated to your god's service. For the next 24 hours, "
            "whenever the target makes a saving throw, it can roll a d4 and add the "
            "number rolled to the save. A creature can benefit from this rite "
            "only once.\nFuneral Rite. You touch one corpse, and for the next 7 "
            "days, the target can't become undead by any means short of a wish "
            "spell.\nWedding. You touch adult humanoids willing to be bonded "
            "together in marriage. For the next 7 days, each target gains a +2 "
            "bonus to AC while they are within 30 feet of each other. A creature "
            "can benefit from this rite again only if widowed.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

CHAOSBOLT = {"NAME": "Chaos Bolt",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Fire", "Acid", "Cold", "Force", "Lightning", "Poison", "Psychic", "Thunder"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You hurl an undulating, warbling mass of chaotic energy at one creature "
            "in range. Make a ranged spell attack against the target. On a hit, "
            "the target takes 2d8 + 1d6 damage. Choose one of the d8s. The number "
            "rolled on that die determines the attack's damage type, as shown below."
            "\nChaos Bolt\nd8	Damage Type\n1	Acid\n2	Cold\n3	Fire\n4	Force\n"
            "5	Lightning\n6	Poison\n7	Psychic\n8	Thunder\nIf you roll the "
            "same number on both d8s, the chaotic energy leaps from the target "
            "to a different creature of your choice within 30 feet of it. Make "
            "a new attack roll against the new target, and make a new damage "
            "roll, which could cause the chaotic energy to leap again.\nA creature "
            "can be targeted only once by each casting of this spell.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, each target takes 1d6 extra damage of the type rolled for each slot level above 1st.",
"REQSIGHT": False
}

CHARMPERSON = {"NAME": "Charm Person",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": ["Charmed"],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Deception", "Social"],
"DESCRIPT": "You attempt to charm a humanoid you can see within range. It must "
            "make a Wisdom saving throw, and does so with advantage if you or "
            "your companions are fighting it. If it fails the saving throw, it is "
            "charmed by you until the spell ends or until you or your companions "
            "do anything harmful to it. The charmed creature regards you as a "
            "friendly acquaintance. When the spell ends, the creature knows it "
            "was charmed by you.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.",
"REQSIGHT": True
}

CHROMATICORB = {"NAME": "Chromatic Orb",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, True, True],
"MATERIALS": "a diamond worth at least 50 gp",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Acid", "Cold", "Fire", "Lightning", "Poison", "Thunder"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You hurl a 4-inch-diameter sphere of energy at a creature that you "
            "can see within range. You choose acid, cold, fire, lightning, poison, "
            "or thunder for the type of orb you create, and then make a ranged spell "
            "attack against the target. If the attack hits, the creature takes 3d8 "
            "damage of the type you chose.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
"REQSIGHT": True
}

COLORSPRAY = {"NAME": "Color Spray",
"LEVEL": 1,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "Self (15-foot cone)",
"COMP": [True, True, True],
"MATERIALS": "a pinch of powder or sand that is colored red, yellow, and blue",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": [],
"COND": ["Blinded"],
"SPELLATTCK": "Other",
"SAVETYPE": "",
"TARGETS": "Cone",
"TAG": ["Control", "Combat"],
"DESCRIPT": "A dazzling array of flashing, colored light springs from your hand. "
            "Roll 6d10; the total is how many hit points of creatures this spell "
            "can effect. Creatures in a 15-foot cone originating from you are "
            "affected in ascending order of their current hit points (ignoring "
            "unconscious creatures and creatures that can't see).\nStarting with "
            "the creature that has the lowest current hit points, each creature "
            "affected by this spell is blinded until the end of your next turn. "
            "Subtract each creature's hit points from the total before moving on "
            "to the creature with the next lowest hit points. A creature's hit "
            "points must be equal to or less than the remaining total for that "
            "creature to be affected.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d10 for each slot level above 1st.",
"REQSIGHT": False
}

COMMAND = {"NAME": "Command",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": [],
"COND": ["Prone"],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control"],
"DESCRIPT": "You speak a one-word command to a creature you can see within range. "
            "The target must succeed on a Wisdom saving throw or follow the command "
            "on its next turn. The spell has no effect if the target is undead, "
            "if it doesn't understand your language, or if your command is directly "
            "harmful to it.\nSome typical commands and their effects follow. You "
            "might issue a command other than one described here. If you do so, "
            "the DM determines how the target behaves. If the target can't follow "
            "your command, the spell ends.\nApproach. The target moves toward you "
            "by the shortest and most direct route, ending its turn if it moves "
            "within 5 feet of you.\nDrop. The target drops whatever it is holding "
            "and then ends its turn.\nFlee. The target spends its turn moving away "
            "from you by the fastest available means.\nGrovel. The target falls "
            "prone and then ends its turn.\nHalt. The target doesn't move and "
            "takes no actions. A flying creature stays aloft, provided that it is "
            "able to do so. If it must move to stay aloft, it flies the minimum "
            "distance needed to remain in the air.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.",
"REQSIGHT": True
}

COMPELLEDDUEL = {"NAME": "Compelled Duel",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Bonus Action",
"RANGE": "30 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Combat"],
"DESCRIPT": "You attempt to compel a creature into a duel. One creature that you "
            "can see within range must make a Wisdom saving throw. On a failed save, "
            "the creature is drawn to you, compelled by your divine demand. For "
            "the duration, it has disadvantage on attack rolls against creatures "
            "other than you, and must make a Wisdom saving throw each time it "
            "attempts to move to a space that is more than 30 feet away from you; "
            "if it succeeds on this saving throw, this spell doesn't restrict the "
            "target's movement for that turn.\nThe spell ends if you attack any "
            "other creature, if you cast a spell that targets a hostile creature "
            "other than the target, if a creature friendly to you damages the target "
            "or casts a harmful spell on it, or if you end your turn more than 30 "
            "feet away from the target.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

COMPREHENDLANGUAGES = {"NAME": "Comprehend Languagues",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a pinch of soot and salt",
"RITUAL": True,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility"],
"DESCRIPT": "For the duration, you understand the literal meaning of any spoken "
            "language that you hear. You also understand any written language "
            "that you see, but you must be touching the surface on which the words "
            "are written. It takes about 1 minute to read one page of text.\nThis "
            "spell doesn't decode secret messages in a text or a glyph, such as "
            "an arcane sigil, that isn't part of a written language.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

CREATEORDESTROYWATER = {"NAME": "Create Or Destroy Water",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a drop of water if creating water or a few grains of sand if destroying it",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility", "Environment"],
"DESCRIPT": "You either create or destroy water.\nCreate Water. You create up to "
            "10 gallons of clean water within range in an open container. "
            "Alternatively, the water falls as rain in a 30-foot cube within range, "
            "extinguishing exposed flames in the area.\nDestroy Water. You destroy "
            "up to 10 gallons of water in an open container within range. "
            "Alternatively, you destroy fog in a 30-foot cube within range.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you create or destroy 10 additional gallons of water, or the size of the cube increases by 5 feet, for each slot level above 1st.",
"REQSIGHT": False
}

CUREWOUNDS = {"NAME": "Cure Wounds",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Healing"],
"DESCRIPT": "A creature you touch regains a number of hit points equal to 1d8 + "
            "your spellcasting ability modifier. This spell has no effect on "
            "undead or constructs.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st.",
"REQSIGHT": False
}

DETECTEVILANDGOOD = {"NAME": "Detect Evil And Good",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility", "Detection"],
"DESCRIPT": "For the duration, you know if there is an aberration, celestial, "
            "elemental, fey, fiend, or undead within 30 feet of you, as well as "
            "where the creature is located. Similarly, you know if there is a "
            "place or object within 30 feet of you that has been magically "
            "consecrated or desecrated.\nThe spell can penetrate most barriers, "
            "but it is blocked by 1 foot of stone, 1 inch of common metal, a "
            "thin sheet of lead, or 3 feet of wood or dirt.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DETECTMAGIC = {"NAME": "Detect Magic",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": True,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility", Detection],
"DESCRIPT": "For the duration, you sense the presence of magic within 30 feet of "
            "you. If you sense magic in this way, you can use your action to see "
            "a faint aura around any visible creature or object in the area that "
            "bears magic, and you learn its school of magic, if any.\nThe spell "
            "can penetrate most barriers, but it is blocked by 1 foot of stone, "
            "1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DETECTPOISONANDDISEASE = {"NAME": "Detect Poison And Disease",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a yew leaf",
"RITUAL": True,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility", "Detection"],
"DESCRIPT": "For the duration, you can sense the presence and location of poisons, "
            "poisonous creatures, and diseases within 30 feet of you. You also "
            "identify the kind of poison, poisonous creature, or disease in each "
            "case.\nThe spell can penetrate most barriers, but it is blocked by "
            "1 foot of stone, 1 inch of common metal, a thin sheet of lead, or "
            "3 feet of wood or dirt.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DISGUISESELF = {"NAME": "Disguise Self",
"LEVEL": 1,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Shapechanging"],
"DESCRIPT": "You make yourself—including your clothing, armor, weapons, and other "
            "belongings on your person—look different until the spell ends or until "
            "you use your action to dismiss it. You can seem 1 foot shorter or "
            "taller and can appear thin, fat, or in between. You can't change your "
            "body type, so you must adopt a form that has the same basic arrangement "
            "of limbs. Otherwise, the extent of the illusion is up to you.\nThe "
            "changes wrought by this spell fail to hold up to physical inspection. "
            "For example, if you use this spell to add a hat to your outfit, "
            "objects pass through the hat, and anyone who touches it would feel "
            "nothing or would feel your head and hair. If you use this spell to "
            "appear thinner than you are, the hand of someone who reaches out to "
            "touch you would bump into you while it was seemingly still in midair."
            "\nTo discern that you are disguised, a creature can use its action "
            "to inspect your appearance and must succeed on an Intelligence "
            "(Investigation) check against your spell save DC.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DISSONANTWHISPERS = {"NAME": "Dissonant Whispers",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": :,"Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You whisper a discordant melody that only one creature of your choice within range can hear, wracking it with terrible pain. The target must make a Wisdom saving throw. On a failed save, it takes 3d6 psychic damage and must immediately use its reaction, if available, to move as far as its speed allows away from you. The creature doesn't move into obviously dangerous ground, such as a fire or a pit. On a successful save, the target takes half as much damage and doesn't have to move away. A deafened creature automatically succeeds on the save.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

DISTORTVALUE = {"NAME": "Distort Value",
"LEVEL": 1,
"SCHOOL": "Illusion",
"CASTTIME": "1 Minute",
"RANGE": "Touch",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Deception"],
"DESCRIPT": "Do you need to squeeze a few more gold pieces out of a merchant as you try to sell that weird octopus statue you liberated from the chaos temple? Do you need to downplay the worth of some magical assets when the tax collector stops by? Distort value has you covered. \nYou cast this spell on an object no more than 1 foot on a side, doubling the object's perceived value by adding illusory flourishes or polish to it, or reducing its perceived value by half with the help of illusory scratches, dents, and other unsightly features. Anyone examining the object can ascertain its true value with a successful Intelligence (Investigation) check against your spell save DC.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the maximum size of the object increases by 1 foot for each slot level above 1st.",
"REQSIGHT": False
}

DIVINEFAVOR = {"NAME": "Divine Favor",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Radiant"],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Damage", "Buff"],
"DESCRIPT": "Your prayer empowers you with divine radiance. Until the spell ends, your weapon attacks deal an extra 1d4 radiant damage on a hit.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

EARTHTREMOR = {"NAME": "Earth Tremor",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "10 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Bludgeoning"],
"COND": ["Prone"],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Multiple Targets",
"TAG": ["Damage", "Control"],
"DESCRIPT": "You cause a tremor in the ground within range. Each creature other than you in that area must make a Dexterity saving throw. On a failed save, a creature takes 1d6 bludgeoning damage and is knocked prone. If the ground in that area is loose earth or stone, it becomes difficult terrain until cleared, with each 5-foot-diameter portion requiring at least 1 minute to clear by hand.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

ENSNARINGSTRIKE = {"NAME": "Ensnaring Strike",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Piercing"],
"COND": ["Restrained"],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Single Target",
"TAG": ["Damage", "Control"],
"DESCRIPT": "The next time you hit a creature with a weapon attack before this spell ends, a writhing mass of thorny vines appears at the point of impact, and the target must succeed on a Strength saving throw or be restrained by the magical vines until the spell ends. A Large or larger creature has advantage on this saving throw. If the target succeeds on the save, the vines shrivel away. While restrained by this spell, the target takes 1d6 piercing damage at the start of each of its turns. A creature restrained by the vines or one that can touch the creature can use its action to make a Strength check against your spell save DC. On a success, the target is freed.",
"HIGHERLEVEL": "If you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

ENTANGLE = {"NAME": "Entangle",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": ["Restrained"],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Square",
"TAG": ["Control"],
"DESCRIPT": "Grasping weeds and vines sprout from the ground in a 20-foot square starting from a point within range. For the duration, these plants turn the ground in the area into difficult terrain. A creature in the area when you cast the spell must succeed on a Strength saving throw or be restrained by the entangling plants until the spell ends. A creature restrained by the plants can use its action to make a Strength check against your spell save DC. On a success, it frees itself. When the spell ends, the conjured plants wilt away.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

EXPEDITIOUSRETREAT = {"NAME": "Expeditious Retreat",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Movement"],
"DESCRIPT": "This spell allows you to move at an incredible pace. When you cast this spell, and then as a bonus action on each of your turns until the spell ends, you can take the Dash action.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FAERIEFIRE = {"NAME": "Faerie Fire",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Cube",
"TAG": ["Debuff"],
"DESCRIPT": "Each object in a 20-foot cube within range is outlined in blue, green, or violet light (your choice). Any creature in the area when the spell is cast is also outlined in light if it fails a Dexterity saving throw. For the duration, objects and affected creatures shed dim light in a 10-foot radius. Any attack roll against an affected creature or object has advantage if the attacker can see it, and the affected creature or object can't benefit from being invisible.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FALSELIFE = {"NAME": "False Life",
"LEVEL": 1,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a small amount of alcohol or distilled spirits",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Buff"],
"DESCRIPT": "Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 temporary hit points for the duration.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you gain 5 additional temporary hit points for each slot level above 1st.",
"REQSIGHT": False
}

FEATHERFALL = {"NAME": "Feather Fall",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 reaction, which you take when you or a creature within 60 feet of you falls",
"RANGE": "60 feet",
"COMP": [True, False, True],
"MATERIALS": "a small feather or a piece of down",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Utility"],
"DESCRIPT": "Choose up to five falling creatures within range. A falling creature's rate of descent slows to 60 feet per round until the spell ends. If the creature lands before the spell ends, it takes no falling damage and can land on its feet, and the spell ends for that creature.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FINDFAMILIAR = {"NAME": "Find Familiar",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Hour",
"RANGE": "10 feet",
"COMP": [True, True, True],
"MATERIALS": "10 gp worth of charcoal, incense, and herbs that must be consumed by fire in a brass brazier",
"RITUAL": True,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Summoning"],
"DESCRIPT": "You gain the service of a familiar, a spirit that takes an animal form you choose: bat, cat, crab, frog (toad), hawk, lizard, octopus, owl, poisonous snake, fish (quipper), rat, raven, sea horse, spider, or weasel. Appearing in an unoccupied space within range, the familiar has the statistics of the chosen form, though it is a celestial, fey, or fiend (your choice) instead of a beast. \nYour familiar acts independently of you, but it always obeys your commands. In combat, it rolls its own initiative and acts on its own turn. A familiar can't attack, but it can take other actions as normal.\nWhen the familiar drops to 0 hit points, it disappears, leaving behind no physical form. It reappears after you cast this spell again.\nWhile your familiar is within 100 feet of you, you can communicate with it telepathically. Additionally, as an action, you can see through your familiar's eyes and hear what it hears until the start of your next turn, gaining the benefits of any special senses that the familiar has. During this time, you are deaf and blind with regard to your own senses.\nAs an action, you can temporarily dismiss your familiar. It disappears into a pocket dimension where it awaits your summons. Alternatively, you can dismiss it forever. As an action while it is temporarily dismissed, you can cause it to reappear in any unoccupied space within 30 feet of you.\nYou can't have more than one familiar at a time. If you cast this spell while you already have a familiar, you instead cause it to adopt a new form. Choose one of the forms from the above list. Your familiar transforms into the chosen creature.\nFinally, when you cast a spell with a range of touch, your familiar can deliver the spell as if it had cast the spell. Your familiar must be within 100 feet of you, and it must use its reaction to deliver the spell when you cast it. If the spell requires an attack roll, you use your attack modifier for the roll.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FOGCLOUD = {"NAME": "Fog Cloud",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Sphere",
"TAG": ["Environment", "Control"],
"DESCRIPT": "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the radius of the fog increases by 20 feet for each slot level above 1st.",
"REQSIGHT": False
}

FROSTFINGERS = {"NAME": "Frost Fingers",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (15-foot cone)",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Cold"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Cone",
"TAG": ["Damage"],
"DESCRIPT": "Freezing cold blasts from your fingertips in a 15-foot cone. Each creature in that area must make a Constitution saving throw, taking 2d8 cold damage on a failed save, or half as much damage on a successful one.\nThe cold freezes nonmagical liquids in the area that aren't being worn or carried.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
"REQSIGHT": False
}

GIFTOFALACRITY = {"NAME": "Gift Of Alacrity",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Minute",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You touch a willing creature. For the duration, the target can add 1d8 to its initiative rolls.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GOODBERRY = {"NAME": "Goodberry",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a sprig of mistletoe",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Healing"],
"DESCRIPT": "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to sustain a creature for one day.\nThe berries lose their potency if they have not been consumed within 24 hours of the casting of this spell.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GREASE = {"NAME": "Grease",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a bit of pork rind or butter",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": ["Prone"],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Square",
"TAG": ["Control"],
"DESCRIPT": "Slick grease covers the ground in a 10-foot square centered on a point within range and turns it into difficult terrain for the duration.\nWhen the grease appears, each creature standing in its area must succeed on a Dexterity saving throw or fall prone. A creature that enters the area or ends its turn there must also succeed on a Dexterity saving throw or fall prone.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GUIDINGBOLT = {"NAME": "Guiding Bolt",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 round",
"DAMAGETYPE": ["Radiant"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Buff"],
"DESCRIPT": "A flash of light streaks toward a creature of your choice within range. Make a ranged spell attack against the target. On a hit, the target takes 4d6 radiant damage, and the next attack roll made against this target before the end of your next turn has advantage, thanks to the mystical dim light glittering on the target until then.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

SPELLLIST = []

ARTIFICERSPELLS = [ACIDSPLASH, BOOMINGBLADE, CREATEBONFIRE, DANCINGLIGHTS, FIREBOLT, FROSTBITE, GREENFLAMEBLADE, GUIDANCE, LIGHT, LIGHTNINGLURE, MAGEHAND, MAGICSTONE, MENDING, MESSAGE, POISONSPRAY, PRESTIDIGITATION, RAYOFFROST, RESISTANCE, SHOCKINGGRASP, SPARETHEDYING, SWORDBURST, THORNWHIP, THUNDERCLAP]
BARDSPELLS = [BLADEWARD, DANCINGLIGHTS, FRIENDS, LIGHT, MAGEHAND, MENDING, MESSAGE, MINORILLUSION, PRESTIDIGITATION, THUNDERCLAP, TRUESTRIKE, VICIOUSMOCKERY]
CLERICSPELLS = [GUIDANCE, LIGHT, MENDING, RESISTANCE, SACREDFLAME, SPARETHEDYING, THAUMATURGY, TOLLTHEDEAD, WORDOFRADIANCE]
DRUIDSPELLS = [CONTROLFLAMES, CREATEBONFIRE, DRUIDCRAFT, FROSTBITE, GUIDANCE, GUST, INFESTATION, MAGICSTONE, MENDING, MOLDEARTH, POISONSPRAY, PRIMALSAVAGERY, PRODUCEFLAME, RESISTANCE, SHAPEWATER, SHILLELAGH, THORNWHIP, THUNDERCLAP]
RANGERSPELLS = []
PALADINSPELLS = []
SORCERERSPELLS = [ACIDSPLASH, BLADEWARD, BOOMINGBLADE, CHILLTOUCH, CONTROLFLAMES, CREATEBONFIRE, DANCINGLIGHTS, FIREBOLT, FRIENDS, FROSTBITE, GREENFLAMEBLADE, GUST, INFESTATION, LIGHT, LIGHTNINGLURE, MAGEHAND, MENDING, MESSAGE, MINDSLIVER, MINORILLUSION, MOLDEARTH, POISONSPRAY, PRESTIDIGITATION, RAYOFFROST, SHAPEWATER, SHOCKINGGRASP, SWORDBURST, THUNDERCLAP, TRUESTRIKE]
WIZARDSPELLS = [ACIDSPLASH, BLADEWARD, BOOMINGBLADE, CHILLTOUCH, CONTROLFLAMES, CREATEBONFIRE, DANCINGLIGHTS, FIREBOLT, FRIENDS, FROSTBITE, GREENFLAMEBLADE, GUST, INFESTATION, LIGHT, LIGHTNINGLURE, MAGEHAND, MENDING, MESSAGE, MINDSLIVER, MINORILLUSION, MOLDEARTH, POISONSPRAY, PRESTIDIGITATION, RAYOFFROST, SHAPEWATER, SHOCKINGGRASP, SWORDBURST, THUNDERCLAP, TOLLTHEDEAD, TRUESTRIKE]
WARLOCKSPELLS = [BLADEWARD, BOOMINGBLADE, CHILLTOUCH, CREATEBONFIRE, ELDRITCHBLAST, FRIENDS, FROSTBITE, GREENFLAMEBLADE, INFESTATION, LIGHTNINGLURE, MAGEHAND, MAGICSTONE, MINDSLIVER, MINORILLUSION, POISONSPRAY, PRESTIDIGITATION, SWORDBURST, THUNDERCLAP, TOLLTHEDEAD, TRUESTRIKE]
