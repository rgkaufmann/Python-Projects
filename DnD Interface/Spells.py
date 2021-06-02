
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

HAILOFTHORNS = {"NAME": "Hail Of Thorns",
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
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "The next time you hit a creature with a ranged weapon attack before the spell ends, this spell creates a rain of thorns that sprouts from your ranged weapon or ammunition. In addition to the normal effect of the attack, the target of the attack and each creature within 5 feet of it must make a Dexterity saving throw. A creature takes 1d10 piercing damage on a failed save, or half as much damage on a successful one.",
"HIGHERLEVEL": "If you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st (to a maximum of 6d10).",
"REQSIGHT": False
}

HEALINGWORD = {"NAME": "Healing Word",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
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
"DESCRIPT": "A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d4 for each slot level above 1st.",
"REQSIGHT": True
}

HELLISHREBUKE = {"NAME": "Hellish Rebuke",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Reaction, which you take in response to being damaged by a creature within 60 feet of you that you can see",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st.",
"REQSIGHT": True
}

HEROISM = {"NAME": "Heroism",
"LEVEL": 1,
"SCHOOL": "Enchantment",
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
"DESCRIPT": "A willing creature you touch is imbued with bravery. Until the spell ends, the creature is immune to being frightened and gains temporary hit points equal to your spellcasting ability modifier at the start of each of its turns. When the spell ends, the target loses any remaining temporary hit points from this spell.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.",
"REQSIGHT": False
}

HEX = {"NAME": "Hex",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Bonus Action",
"RANGE": "90 feet",
"COMP": [True, True, True],
"MATERIALS": "the petrified eye of a newt",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": ["Necrotic"],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "You place a curse on a creature that you can see within range. Until the spell ends, you deal an extra 1d6 necrotic damage to the target whenever you hit it with an attack. Also, choose one ability when you cast the spell. The target has disadvantage on ability checks made with the chosen ability.\nIf the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to curse a new creature.\nA remove curse cast on the target ends this spell early.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd or 4th level, you can maintain your concentration on the spell for up to 8 hours. When you use a spell slot of 5th level or higher, you can maintain your concentration on the spell for up to 24 hours.",
"REQSIGHT": True
}

HUNTERSMARK = {"NAME": "Hunter's Mark",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Bonus Action",
"RANGE": "90 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Detection"],
"DESCRIPT": "You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, and you have advantage on any Wisdom (Perception) or Wisdom (Survival) check you make to find it. If the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to mark a new creature.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd or 4th level, you can maintain your concentration on the spell for up to 8 hours. When you use a spell slot of 5th level or higher, you can maintain your concentration on the spell for up to 24 hours.",
"REQSIGHT": False
}

ICEKNIFE = {"NAME": "Ice Knife",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, True],
"MATERIALS": "a drop of water or piece of ice",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Piercing", "Cold"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "DEX",
"TARGETS": "Mulitple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You create a shard of ice and fling it at one creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 piercing damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 cold damage.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the cold damage increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

IDENTIFY = {"NAME": "Identify",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Minute",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a pearl worth at least 100 gp and an owl feather",
"RITUAL": True,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Detection"],
"DESCRIPT": "You choose one object that you must touch throughout the casting of the spell. If it is a magic item or some other magic-imbued object, you learn its properties and how to use them, whether it requires attunement to use, and how many charges it has, if any. You learn whether any spells are affecting the item and what they are. If the item was created by a spell, you learn which spell created it.\nIf you instead touch a creature throughout the casting, you learn what spells, if any, are currently affecting it.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ILLUSORYSCRIPT = {"NAME": "Illusory Script",
"LEVEL": 1,
"SCHOOL": "Illusion",
"CASTTIME": "1 Minute",
"RANGE": "Touch",
"COMP": [False, True, True],
"MATERIALS": "a lead-based ink worth at least 10 gp, which the spell consumes",
"RITUAL": True,
"CONC": False,
"DURATION": "10 days",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Communication", "Deception"],
"DESCRIPT": "You write on parchment, paper, or some other suitable writing material and imbue it with a potent illusion that lasts for the duration.\nTo you and any creatures you designate when you cast the spell, the writing appears normal, written in your hand, and conveys whatever meaning you intended when you wrote the text. To all others, the writing appears as if it were written in an unknown or magical script that is unintelligible. Alternatively, you can cause the writing to appear to be an entirely different message, written in a different hand and language, though the language must be one you know.\nShould the spell be dispelled, the original script and the illusion both disappear.\nA creature with truesight can read the hidden message.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

INFLICTWOUNDS = {"NAME": "Inflict Wounds",
"LEVEL": 1,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Necrotic"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "Make a melee spell attack against a creature you can reach. On a hit, the target takes 3d10 necrotic damage.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st.",
"REQSIGHT": False
}

JIMSMAGICMISSILE = {"NAME": "Jim's Magic Missile",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, True],
"MATERIALS": "1 gp (Royalty Component)",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Force"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "Any apprentice wizard can cast a boring old magic missile. Sure, it always strikes its target. Yawn. Do away with the drudgery of your grandfather's magic with this improved version of the spell, as used by Jim Darkmagic!\nYou create three twisting, whistling, hypoallergenic, gluten-free darts of magical force. Each dart targets a creature of your choice that you can see within range. Make a ranged spell attack for each missile. On a hit, a missile deals 2d4 force damage to its target.\nIf the attack roll scores a critical hit, the target of that missile takes 5d4 force damage instead of you rolling damage twice for a critical hit. If the attack roll for any missile is a 1, all missiles miss their targets and blow up in your face, dealing 1 force damage per missile to you.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart, and the royalty component increases by 1 gp, for each slot level above 1st.",
"REQSIGHT": False
}

JUMP = {"NAME": "Jump",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a grasshopper's hind leg",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Movement"],
"DESCRIPT": "You touch a creature. The creature's jump distance is tripled until the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

LONGSTRIDER = {"NAME": "Longstrider",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a pinch of dirt",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Movement"],
"DESCRIPT": "You touch a creature. The target's speed increases by 10 feet until the spell ends.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.",
"REQSIGHT": False
}

MAGEARMOR = {"NAME": "Mage Armor",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a piece of cured leather",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff", "Warding"],
"DESCRIPT": "You touch a willing creature who isn't wearing armor, and a protective magical force surrounds it until the spell ends. The target's base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or if you dismiss the spell as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MAGICMISSILE = {"NAME": "Magic Missile",
"LEVEL": 1,
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
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot level above 1st.",
"REQSIGHT": True
}

MAGNIFYGRAVITY = {"NAME": "Magnify Gravity",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 round",
"DAMAGETYPE": ["Force"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Sphere",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "The gravity in a 10-foot-radius sphere centered on a point you can see within range increases for a moment. Each creature in the sphere on the turn when you cast the spell must make a Constitution saving throw. On a failed save, a creature takes 2d8 force damage, and its speed is halved until the end of its next turn. On a successful save, a creature takes half as much damage and suffers no reduction to its speed.\nUntil the start of your next turn, any object that isn't being worn or carried in the sphere requires a successful Strength check against your spell save DC to pick up or move.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
"REQSIGHT": True
}

PROTECTIONFROMEVILANDGOOD = {"NAME": "Protection From Evil And Good",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "holy water or powdered silver and iron, which the spell consumes",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff", "Debuff", "Warding"],
"DESCRIPT": "Until the spell ends, one willing creature you touch is protected against certain types of creatures: aberrations, celestials, elementals, fey, fiends, and undead.\nThe protection grants several benefits. Creatures of those types have disadvantage on attack rolls against the target. The target also can't be charmed, frightened, or possessed by them. If the target is already charmed, frightened, or possessed by such a creature, the target has advantage on any new saving throw against the relevant effect.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

PURIFYFOODANDDRINK = {"NAME": "Purify Food And Drink",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "10 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": True,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Sphere",
"TAG": ["Utility"],
"DESCRIPT": "All nonmagical food and drink within a 5-foot-radius sphere centered on a point of your choice within range is purified and rendered free of poison and disease.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

RAYOFSICKNESS = {"NAME": "Ray Of Sickness",
"LEVEL": 1,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Poison"],
"COND": ["Poisoned"],
"SPELLATTCK": "Ranged",
"SAVETYPE": "CON",
"TARGETS": "Single TArget",
"TAG": ["Damage", "Debuff"],
"DESCRIPT": "A ray of sickening greenish energy lashes out toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 2d8 poison damage and must make a Constitution saving throw. On a failed save, it is also poisoned until the end of your next turn.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
"REQSIGHT": False
}

SANCTUARY = {"NAME": "Sanctuary",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Bonus Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a small silver mirror",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Warding"],
"DESCRIPT": "You ward a creature within range against attack. Until the spell ends, any creature who targets the warded creature with an attack or a harmful spell must first make a Wisdom saving throw. On a failed save, the creature must choose a new target or lose the attack or spell. This spell doesn't protect the warded creature from area effects, such as the explosion of a fireball.\nIf the warded creature makes an attack, casts a spell that affects an enemy, or deals damage to another creature, this spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SEARINGSMITE = {"NAME": "Searing Smite",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "The next time you hit a creature with a melee weapon attack during the spell's duration, your weapon flares with white-hot intensity, and the attack deals an extra 1d6 fire damage to the target and causes the target to ignite in flames. At the start of each of its turns until the spell ends, the target must make a Constitution saving throw. On a failed save, it takes 1d6 fire damage. On a successful save, the spell ends. If the target or a creature within 5 feet of it uses an action to put out the flames, or if some other effect douses the flames (such as the target being submerged in water), the spell ends.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the initial extra damage dealt by the attack increases by 1d6 for each slot level above 1st.",
"REQSIGHT": False
}

SHIELD = {"NAME": "Shield",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 reaction, which you take when you are hit by an attack or targeted by the magic missile spell",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 round",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Warding"],
"DESCRIPT": "An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SHIELDOFFAITH = {"NAME": "Shield Of Faith",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Bonus Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a small parchment with a bit of holy text written on it",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Warding"],
"DESCRIPT": "A shimmering field appears and surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SILENTIMAGE = {"NAME": "Silent Image",
"LEVEL": 1,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a bit of fleece",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Cube",
"TAG": ["Deception", "Utility"],
"DESCRIPT": "You create the image of an object, a creature, or some other visible phenomenon that is no larger than a 15-foot cube. The image appears at a spot within range and lasts for the duration. The image is purely visual; it isn't accompanied by sound, smell, or other sensory effects.\nYou can use your action to cause the image to move to any spot within range. As the image changes location, you can alter its appearance so that its movements appear natural for the image. For example, if you create an image of a creature and move it, you can alter the image so that it appears to be walking.\nPhysical interaction with the image reveals it to be an illusion, because things can pass through it. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the creature can see through the image.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SLEEP = {"NAME": "Sleep",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, True, True],
"MATERIALS": "a pinch of fine sand, rose petals, or a cricket",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": ["Unconscious"],
"SPELLATTCK": "Other",
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Control"],
"DESCRIPT": "This spell sends creatures into a magical slumber. Roll 5d8; the total is how many hit points of creatures this spell can affect. Creatures within 20 feet of a point you choose within range are affected in ascending order of their current hit points (ignoring unconscious creatures).\nStarting with the creature that has the lowest current hit points, each creature affected by this spell falls unconscious until the spell ends, the sleeper takes damage, or someone uses an action to shake or slap the sleeper awake. Subtract each creature's hit points from the total before moving on to the creature with the next lowest hit points. A creature's hit points must be equal to or less than the remaining total for that creature to be affected.\nUndead and creatures immune to being charmed aren't affected by this spell.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d8 for each slot level above 1st.",
"REQSIGHT": False
}

SNARE = {"NAME": "Snare",
"LEVEL": 1,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Minute",
"RANGE": "Touch",
"COMP": [False, True, True],
"MATERIALS": "25 feet of rope, which the spell consumes",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": ["Restrained"],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Single Target",
"TAG": ["Control"],
"DESCRIPT": "As you cast this spell, you use the rope to create a circle with a 5-foot radius on the ground or the floor. When you finish casting, the rope disappears and the circle becomes a magic trap.\nThis trap is nearly invisible, requiring a successful Intelligence (Investigation) check against your spell save DC to be discerned.\nThe trap triggers when a Small, Medium, or Large creature moves onto the ground or the floor in the spell's radius. That creature must succeed on a Dexterity saving throw or be magically hoisted into the air, leaving it hanging upside down 3 feet above the ground or the floor. The creature is restrained there until the spell ends.\nA restrained creature can make a Dexterity saving throw at the end of each of its turns, ending the effect on itself on a success. Alternatively, the creature or someone else who can reach it can use an action to make an Intelligence (Arcana) check against your spell save DC. On a success, the restrained effect ends.\nAfter the trap is triggered, the spell ends when no creature is restrained by it.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SPEAKWITHANIMALS = {"NAME": "Speak With Animals",
"LEVEL": 1,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Communication", "Social"],
"DESCRIPT": "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts is limited by their intelligence, but at minimum, beasts can give you information about nearby locations and monsters, including whatever they can perceive or have perceived within the past day. You might be able to persuade a beast to perform a small favor for you, at the DM's discretion.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

TASHASCAUSTICBREW = {"NAME": "Tasha's Caustic Brew",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (30-foot line)",
"COMP": [True, True, True],
"MATERIALS": "a bit of rotten food",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Acid"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Line",
"TAG": ["Damage"],
"DESCRIPT": "A stream of acid emanates from you in a line 30 feet long and 5 feet wide in a direction you choose. Each creature in the line must succeed on a Dexterity saving throw or be covered in acid for the spell's duration or until a creature uses its action to scrape or wash the acid off itself or another creature. A creature covered in the acid takes 2d4 acid damage at start of each of its turns.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 2d4 for each slot level above 1st.",
"REQSIGHT": False
}

TASHASHIDEOUSLAUGHTER = {"NAME": "Tasha's Hideous Laughter",
"LEVEL": 1,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "tiny tarts and a feather that is waved in the air",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": ["Prone", "Incapacitated"],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Debuff"],
"DESCRIPT": "A creature of your choice that you can see within range perceives everything as hilariously funny and falls into fits of laughter if this spell affects it. The target must succeed on a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand up for the duration. A creature with an Intelligence score of 4 or less isn't affected.\nAt the end of each of its turns, and each time it takes damage, the target can make another Wisdom saving throw. The target has advantage on the saving throw if it's triggered by damage. On a success, the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

TENSORSFLOATINGDISK = {"NAME": "Tensor's Floating Disk",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a drop of mercury",
"RITUAL": True,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Movement", "Utility"],
"DESCRIPT": "This spell creates a circular, horizontal plane of force, 3 feet in diameter and 1 inch thick, that floats 3 feet above the ground in an unoccupied space of your choice that you can see within range. The disk remains for the duration, and can hold up to 500 pounds. If more weight is placed on it, the spell ends, and everything on the disk falls to the ground.\nThe disk is immobile while you are within 20 feet of it. If you move more than 20 feet away from it, the disk follows you so that it remains within 20 feet of you. It can move across uneven terrain, up or down stairs, slopes and the like, but it can't cross an elevation change of 10 feet or more. For example, the disk can't move across a 10-foot-deep pit, nor could it leave such a pit if it was created at the bottom.\nIf you move more than 100 feet from the disk (typically because it can't move around an obstacle to follow you), the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

THUNDEROUSSMITE = {"NAME": "Thunderous Smite",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Thunder"],
"COND": ["Prone"],
"SPELLATTCK": "Melee",
"SAVETYPE": "STR",
"TARGETS": "Single Target",
"TAG": ["Control", "Damage"],
"DESCRIPT": "The first time you hit with a melee weapon attack during this spell's duration, your weapon rings with thunder that is audible within 300 feet of you, and the attack deals an extra 2d6 thunder damage to the target. Additionally, if the target is a creature, it must succeed on a Strength saving throw or be pushed 10 feet away from you and knocked prone.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

THUNDERWAVE = {"NAME": "Thunderwave",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (15-foot cube)",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Thunder"],
"COND": ["Restrained"],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Cube",
"TAG": ["Damage", "Control"],
"DESCRIPT": "A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. On a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn't pushed.\nIn addition, unsecured objects that are completely within the area of effect are automatically pushed 10 feet away from you by the spell's effect, and the spell emits a thunderous boom audible out to 300 feet.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.",
"REQSIGHT": False
}

UNSEENSERVANT = {"NAME": "Unseen Servant",
"LEVEL": 1,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a piece of string and a bit of wood",
"RITUAL": True,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Control", "Utility", "Summoning"],
"DESCRIPT": "This spell creates an invisible, mindless, shapeless, Medium force that performs simple tasks at your command until the spell ends. The servant springs into existence in an unoccupied space on the ground within range. It has AC 10, 1 hit point, and a Strength of 2, and it can't attack. If it drops to 0 hit points, the spell ends.\nOnce on each of your turns as a bonus action, you can mentally command the servant to move up to 15 feet and interact with an object. The servant can perform simple tasks that a human servant could do, such as fetching things, cleaning, mending, folding clothes, lighting fires, serving food, and pouring wine. Once you give the command, the servant performs the task to the best of its ability until it completes the task, then waits for your next command.\nIf you command the servant to perform a task that would move it more than 60 feet away from you, the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

WITCHBOLT = {"NAME": "Witch Bolt",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a twig from a tree that has been struck by lightning",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Lightning"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "A beam of crackling, blue energy lances out toward a creature within range, forming a sustained arc of lightning between you and the target. Make a ranged spell attack against that creature. On a hit, the target takes 1d12 lightning damage, and on each of your turns for the duration, you can use your action to deal 1d12 lightning damage to the target automatically. The spell ends if you use your action to do anything else. The spell also ends if the target is ever outside the spell's range or if it has total cover from you.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 2nd level or higher, the initial damage increases by 1d12 for each slot level above 1st.",
"REQSIGHT": False
}

WRATHFULSMITE = {"NAME": "Wrathful Smite",
"LEVEL": 1,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Psychic"],
"COND": ["Frightened"],
"SPELLATTCK": "Melee",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Damage"],
"DESCRIPT": "The next time you hit with a melee weapon attack during this spell's duration, your attack deals an extra 1d6 psychic damage. Additionally, if the target is a creature, it must make a Wisdom saving throw or be frightened of you until the spell ends. As an action, the creature can make a Wisdom check against your spell save DC to steel its resolve and end this spell.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ZEPHYRSTRIKE = {"NAME": "Zephyr Strike",
"LEVEL": 1,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Force"],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Movement", "Buff", "Damage", "Combat"],
"DESCRIPT": "You move like the wind. Until the spell ends, your movement doesn't provoke opportunity attacks.\nOnce before the spell ends, you can give yourself advantage on one weapon attack roll on your turn. That attack deals an extra 1d8 force damage on a hit. Whether you hit or miss, your walking speed increases by 30 feet until the end of that turn.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}


#### ------------------------- 2ND LEVEL ---------------------- ####

AGANAZZARSSCORCHER = {"NAME": "Aganazzar's Scorcher",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a red dragon's scale",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Line",
"TAG": ["Damage"],
"DESCRIPT": "A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose. Each creature in the line must make a Dexterity saving throw. A creature takes 3d8 fire damage on a failed save, or half as much damage on a successful one.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.",
"REQSIGHT": False
}

AID = {"NAME": "Aid",
"LEVEL": 2,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a tiny strip of white cloth",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Mulitple Targets",
"TAG": ["Buff"],
"DESCRIPT": "Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range. Each target's hit point maximum and current hit points increase by 5 for the duration.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, a target's hit points increase by an additional 5 for each slot level above 2nd.",
"REQSIGHT": False
}

ALTERSELF = {"NAME": "Alter Self",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Deception", "Utility", "Movement"],
"DESCRIPT": "You assume a different form. When you cast the spell, choose one of the following options, the effects of which last for the duration of the spell. While the spell lasts, you can end one option as an action to gain the benefits of a different one.\nAquatic Adaptation. You adapt your body to an aquatic environment, sprouting gills and growing webbing between your fingers. You can breathe underwater and gain a swimming speed equal to your walking speed.\nChange Appearance. You transform your appearance. You decide what you look like, including your height, weight, facial features, sound of your voice, hair length, coloration, and distinguishing characteristics, if any. You can make yourself appear as a member of another race, though none of your statistics change. You also can't appear as a creature of a different size than you, and your basic shape stays the same; if you're bipedal, you can't use this spell to become quadrupedal, for instance. At any time for the duration of the spell, you can use your action to change your appearance in this way again.\nNatural Weapons. You grow claws, fangs, spines, horns, or a different natural weapon of your choice. Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing damage, as appropriate to the natural weapon you chose, and you are proficient with your unarmed strikes. Finally, the natural weapon is magic and you have a +1 bonus to the attack and damage rolls you make using it.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ANIMALMESSENGER = {"NAME": "Animal Messenger",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a morsel of food",
"RITUAL": True,
"CONC": False,
"DURATION": "24 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Communication"],
"DESCRIPT": "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as "a man or woman dressed in the uniform of the town guard" or "a red-haired dwarf wearing a pointed hat." You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.\nWhen the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell.",
"HIGHERLEVEL": "If you cast this spell using a spell slot of 3rd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd.",
"REQSIGHT": True
}

ARCANELOCK = {"NAME": "Arcane Lock",
"LEVEL": 2,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "gold dust worth at least 25 gp, which the spell consumes",
"RITUAL": False,
"CONC": False,
"DURATION": "Until dispelled",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Warding", "Utility"],
"DESCRIPT": "You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting knock on the object suppresses arcane lock for 10 minutes.\nWhile affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

AUGURY = {"NAME": "Augury",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Minute",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "specially marked sticks, bones, or similar tokens worth at least 25 gp",
"RITUAL": True,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Foreknowledge"],
"DESCRIPT": "By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, or employing some other divining tool, you receive an omen from an otherworldly entity about the results of a specific course of action that you plan to take within the next 30 minutes. The DM chooses from the following possible omens:\n -Weal, for good results\n -Woe, for bad results\n -Weal and woe, for both good and bad results\n -Nothing, for results that aren't especially good or bad\n-The spell doesn't take into account any possible circumstances that might change the outcome, such as the casting of additional spells or the loss or gain of a companion.\nIf you cast the spell two or more times before completing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get a random reading. The DM makes this roll in secret.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

BARKSKIN = {"NAME": "Barkskin",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a handful of oak bark",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff", "Warding"],
"DESCRIPT": "You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance, and the target's AC can't be less than 16, regardless of what kind of armor it is wearing.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

BEASTSENSE = {"NAME": "Beast Sense",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": True,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Utility"],
"DESCRIPT": "You touch a willing beast. For the duration of the spell, you can use your action to see through the beast's eyes and hear what it hears, and continue to do so until you use your action to return to your normal senses. While perceiving through the beast's senses, you gain the benefits of any special senses possessed by that creature, though you are blinded and deafened to your own surroundings.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

BLINDNESSDEAFNESS = {"NAME": "Blindness/Deafness",
"LEVEL": 2,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": ["Blinded", "Deafened"],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Control"],
"DESCRIPT": "You can blind or deafen a foe. Choose one creature that you can see within range to make a Constitution saving throw. If it fails, the target is either blinded or deafened (your choice) for the duration. At the end of each of its turns, the target can make a Constitution saving throw. On a success, the spell ends.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.",
"REQSIGHT": True
}

BLUR = {"NAME": "Blur",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Warding", "Debuff"],
"DESCRIPT": "Your body becomes blurred, shifting and wavering to all who can see you. For the duration, any creature has disadvantage on attack rolls against you. An attacker is immune to this effect if it doesn't rely on sight, as with blindsight, or can see through illusions, as with truesight.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

BRANDINGSMITE = {"NAME": "Branding Smite",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Radiant"],
"COND": [],
"SPELLATTCK": "Other",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage", "Control"],
"DESCRIPT": "The next time you hit a creature with a weapon attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it's invisible, and the target sheds dim light in a 5-foot radius and can't become invisible until the spell ends.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the extra damage increases by 1d6 for each slot level above 2nd.",
"REQSIGHT": False
}

CALMEMOTIONS = {"NAME": "Calm Emotions",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CHA",
"TARGETS": "Sphere",
"TAG": ["Debuff", "Social", "Control"],
"DESCRIPT": "You attempt to suppress strong emotions in a group of people. Each humanoid in a 20-foot-radius sphere centered on a point you choose within range must make a Charisma saving throw; a creature can choose to fail this saving throw if it wishes. If a creature fails its saving throw, choose one of the following two effects.\nYou can suppress any effect causing a target to be charmed or frightened. When this spell ends, any suppressed effect resumes, provided that its duration has not expired in the meantime.\nAlternatively, you can make a target indifferent about creatures of your choice that it is hostile toward. This indifference ends if the target is attacked or harmed by a spell or if it witnesses any of its friends being harmed. When the spell ends, the creature becomes hostile again, unless the DM rules otherwise.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

CLOUDOFDAGGERS = {"NAME": "Cloud Of Daggers",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a sliver of glass",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Slashing"],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Cube",
"TAG": ["Damage"],
"DESCRIPT": "You fill the air with spinning daggers in a cube 5 feet on each side, centered on a point you choose within range. A creature takes 4d4 slashing damage when it enters the spell's area for the first time on a turn or starts its turn there.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 2d4 for each slot level above 2nd.",
"REQSIGHT": False
}

CONTINUALFLAME = {"NAME": "Continual Flame",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "ruby dust worth 50 gp, which the spell consumes",
"RITUAL": False,
"CONC": False,
"DURATION": "Until dispelled",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility"],
"DESCRIPT": "A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn't use oxygen. A continual flame can be covered or hidden but not smothered or quenched.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

CORDONOFARROWS = {"NAME": "Cordon Of Arrows",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "5 feet",
"COMP": [True, True, True],
"MATERIALS": "four or more arrows or bolts",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": ["Piercing"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Circle",
"TAG": ["Damage", "Warding"],
"DESCRIPT": "You plant four pieces of nonmagical ammunition—arrows or crossbow bolts—in the ground within range and lay magic upon them to protect an area. Until the spell ends, whenever a creature other than you comes within 30 feet of the ammunition for the first time on a turn or ends its turn there, one piece of ammunition flies up to strike it. The creature must succeed on a Dexterity saving throw or take 1d6 piercing damage. The piece of ammunition is then destroyed. The spell ends when no ammunition remains.\nWhen you cast this spell, you can designate any creatures you choose, and the spell ignores them.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the amount of ammunition that can be affected increases by two for each slot level above 2nd.",
"REQSIGHT": False
}

CROWNOFMADNESS = {"NAME": "Crown Of Madness",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": ["Charmed"],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Combat"],
"DESCRIPT": "One humanoid of your choice that you can see within range must succeed on a Wisdom saving throw or become charmed by you for the duration. While the target is charmed in this way, a twisted crown of jagged iron appears on its head, and a madness glows in its eyes.\nThe charmed target must use its action before moving on each of its turns to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no creature or if none are within its reach.\nOn your subsequent turns, you must use your action to maintain control over the target, or the spell ends. Also, the target can make a Wisdom saving throw at the end of each of its turns. On a success, the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

DARKNESS = {"NAME": "Darkness",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, True],
"MATERIALS": "bat fur and a drop of pitch or piece of coal",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Sphere",
"TAG": ["Control"],
"DESCRIPT": "Magical darkness spreads from a point you choose within range to fill a 15-foot-radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it.\nIf the point you choose is on an object you are holding or one that isn't being worn or carried, the darkness emanates from the object and moves with it. Completely covering the source of the darkness with an opaque object, such as a bowl or a helm, blocks the darkness.\nIf any of this spell's area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DARKVISION = {"NAME": "Darkvision",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "either a pinch of dried carrot or an agate",
"RITUAL": False,
"CONC": False,
"DURATION": "8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

DETECTTHOUGHTS = {"NAME": "Detect Thoughts",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a copper piece",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Social", "Detection"],
"DESCRIPT": "For the duration, you can read the thoughts of certain creatures. When you cast the spell and as your action on each turn until the spell ends, you can focus your mind on any one creature that you can see within 30 feet of you. If the creature you choose has an Intelligence of 3 or lower or doesn't speak any language, the creature is unaffected.\nYou initially learn the surface thoughts of the creature—what is most on its mind in that moment. As an action, you can either shift your attention to another creature's thoughts or attempt to probe deeper into the same creature's mind. If you probe deeper, the target must make a Wisdom saving throw. If it fails, you gain insight into its reasoning (if any), its emotional state, and something that looms large in its mind (such as something it worries over, loves, or hates). If it succeeds, the spell ends. Either way, the target knows that you are probing into its mind, and unless you shift your attention to another creature's thoughts, the creature can use its action on its turn to make an Intelligence check contested by your Intelligence check; if it succeeds, the spell ends.\nQuestions verbally directed at the target creature naturally shape the course of its thoughts, so this spell is particularly effective as part of an interrogation.\nYou can also use this spell to detect the presence of thinking creatures you can't see. When you cast the spell or as your action during the duration, you can search for thoughts within 30 feet of you. The spell can penetrate barriers, but 2 feet of rock, 2 inches of any metal other than lead, or a thin sheet of lead blocks you. You can't detect a creature with an Intelligence of 3 or lower or one that doesn't speak any language.\nOnce you detect the presence of a creature in this way, you can read its thoughts for the rest of the duration as described above, even if you can't see it, but it must still be within range.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

DRAGONSBREATH = {"NAME": "Dragon's Breath",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a hot pepper",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Acid", "Cold", "Fire", "Lightning", "Poison"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Cone",
"TAG": ["Damage"],
"DESCRIPT": "You touch one willing creature and imbue it with the power to spew magical energy from its mouth, provided it has one. Choose acid, cold, fire, lightning, or poison. Until the spell ends, the creature can use an action to exhale energy of the chosen type in a 15-foot cone. Each creature in that area must make a Dexterity saving throw, taking 3d6 damage of the chosen type on a failed save, or half as much damage on a successful one.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.",
"REQSIGHT": False
}

DUSTDEVIL = {"NAME": "Dust Devil",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a pinch of dust",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Bludgeoning"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Cube",
"TAG": ["Control", "Damage"],
"DESCRIPT": "Choose an unoccupied 5-foot cube of air that you can see within range. An elemental force that resembles a dust devil appears in the cube and lasts for the spell's duration.\nAny creature that ends its turn within 5 feet of the dust devil must make a Strength saving throw. On a failed save, the creature takes 1d8 bludgeoning damage and is pushed 10 feet away from the dust devil. On a successful save, the creature takes half as much damage and isn't pushed.\nAs a bonus action, you can move the dust devil up to 30 feet in any direction. If the dust devil moves over sand, dust, loose dirt, or light gravel, it sucks up the material and forms a 10-foot-radius cloud of debris around itself that lasts until the start of your next turn. The cloud heavily obscures its area",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.",
"REQSIGHT": True
}

EARTHBIND = {"NAME": "Earthbind",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "300 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Single Target",
"TAG": ["Control", "Debuff"],
"DESCRIPT": "Choose one creature you can see within range. Yellow strips of magical energy loop around the creature. The target must succeed on a Strength saving throw, or its flying speed (if any) is reduced to 0 feet for the spell's duration. An airborne creature affected by this spell safely descends at 60 feet per round until it reaches the ground or the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

ENHANCEABILITY = {"NAME": "Enhance Ability",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "fur or a feather from a beast",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You touch a creature and bestow upon it a magical enhancement. Choose one of the following effects; the target gains that effect until the spell ends.\nBear's Endurance. The target has advantage on Constitution checks. It also gains 2d6 temporary hit points, which are lost when the spell ends.\nBull's Strength. The target has advantage on Strength checks, and his or her carrying capacity doubles.\nCat's Grace. The target has advantage on Dexterity checks. It also doesn't take damage from falling 20 feet or less if it isn't incapacitated.\nEagle's Splendor. The target has advantage on Charisma checks.\nFox's Cunning. The target has advantage on Intelligence checks.\nOwl's Wisdom. The target has advantage on Wisdom checks.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.",
"REQSIGHT": False
}

ENLARGEREDUCE = {"NAME": "Enlarge/Reduce",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a pinch of powdered iron",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Control", "Buff", "Debuff"],
"DESCRIPT": "You cause a creature or an object you can see within range to grow larger or smaller for the duration. Choose either a creature or an object that is neither worn nor carried. If the target is unwilling, it can make a Constitution saving throw. On a success, the spell has no effect.\nIf the target is a creature, everything it is wearing and carrying changes size with it. Any item dropped by an affected creature returns to normal size at once.\nEnlarge. The target's size doubles in all dimensions, and its weight is multiplied by eight. This growth increases its size by one category—from Medium to Large, for example. If there isn't enough room for the target to double its size, the creature or object attains the maximum possible size in the space available. Until the spell ends, the target also has advantage on Strength checks and Strength saving throws. The target's weapons also grow to match its new size. While these weapons are enlarged, the target's attacks with them deal 1d4 extra damage.\nReduce. The target's size is halved in all dimensions, and its weight is reduced to one-eighth of normal. This reduction decreases its size by one category—from Medium to Small, for example. Until the spell ends, the target also has disadvantage on Strength checks and Strength saving throws. The target's weapons also shrink to match its new size. While these weapons are reduced, the target's attacks with them deal 1d4 less damage (this can't reduce the damage below 1).",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

ENTHRALL = {"NAME": "Enthrall",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Multiple Targets",
"TAG": ["Control"],
"DESCRIPT": "You weave a distracting string of words, causing creatures of your choice that you can see within range and that can hear you to make a Wisdom saving throw. Any creature that can't be charmed succeeds on this saving throw automatically, and if you or your companions are fighting a creature, it has advantage on the save. On a failed save, the target has disadvantage on Wisdom (Perception) checks made to perceive any creature other than you until the spell ends or until the target can no longer hear you. The spell ends if you are incapacitated or can no longer speak.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

FINDSTEED = {"NAME": "Find Steed",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "10 minutes",
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
"TARGETS": None,
"TAG": ["Movement", "Summoning", "Utility"],
"DESCRIPT": "You summon a spirit that assumes the form of an unusually intelligent, strong, and loyal steed, creating a long-lasting bond with it. Appearing in an unoccupied space within range, the steed takes on a form that you choose: a warhorse, a pony, a camel, an elk, or a mastiff. (Your DM might allow other animals to be summoned as steeds.) The steed has the statistics of the chosen form, though it is a celestial, fey, or fiend (your choice) instead of its normal type. Additionally, if your steed has an Intelligence of 5 or less, its Intelligence becomes 6, and it gains the ability to understand one language of your choice that you speak.\nYour steed serves you as a mount, both in combat and out, and you have an instinctive bond with it that allows you to fight as a seamless unit. While mounted on your steed, you can make any spell you cast that targets only you also target your steed.\nWhen the steed drops to 0 hit points, it disappears, leaving behind no physical form. You can also dismiss your steed at any time as an action, causing it to disappear. In either case, casting this spell again summons the same steed, restored to its hit point maximum.\nWhile your steed is within 1 mile of you, you can communicate with each other telepathically.\nYou can't have more than one steed bonded by this spell at a time. As an action, you can release the steed from its bond at any time, causing it to disappear.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FINDTRAPS = {"NAME": "Find Traps",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Detection"],
"DESCRIPT": "You sense the presence of any trap within range that is within line of sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator. Thus, the spell would sense an area affected by the alarm spell, a glyph of warding, or a mechanical pit trap, but it would not reveal a natural weakness in the floor, an unstable ceiling, or a hidden sinkhole.\nThis spell merely reveals that a trap is present. You don't learn the location of each trap, but you do learn the general nature of the danger posed by a trap you sense.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

FLAMEBLADE = {"NAME": "Flame Blade",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "leaf of sumac",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. If you let go of the blade, it disappears, but you can evoke the blade again as a bonus action.\nYou can use your action to make a melee spell attack with the fiery blade. On a hit, the target takes 3d6 fire damage.\nThe flaming blade sheds bright light in a 10-foot radius and dim light for an additional 10 feet.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for every two slot levels above 2nd.",
"REQSIGHT": False
}

FLAMINGSPHERE = {"NAME": "Flaming Sphere",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a bit of tallow, a pinch of brimstone, and a dusting of powdered iron",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Sphere",
"TAG": ["Damage"],
"DESCRIPT": "A 5-foot-diameter sphere of fire appears in an unoccupied space of your choice within range and lasts for the duration. Any creature that ends its turn within 5 feet of the sphere must make a Dexterity saving throw. The creature takes 2d6 fire damage on a failed save, or half as much damage on a successful one.\nAs a bonus action, you can move the sphere up to 30 feet. If you ram the sphere into a creature, that creature must make the saving throw against the sphere's damage, and the sphere stops moving this turn.\nWhen you move the sphere, you can direct it over barriers up to 5 feet tall and jump it across pits up to 10 feet wide. The sphere ignites flammable objects not being worn or carried, and it sheds bright light in a 20-foot radius and dim light for an additional 20 feet.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.",
"REQSIGHT": False
}

FORTUNESFAVOR = {"NAME": "Fortune's Favor",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Minute",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a white pearl worth at least 100 gp, which the spell consumes",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "You impart latent luck to yourself or one willing creature you can see within range. When the chosen creature makes an attack roll, an ability check, or a saving throw before the spell ends, it can dismiss this spell on itself to roll an additional d20 and choose which of the d20s to use. Alternatively, when an attack roll is made against the chosen creature, it can dismiss this spell on itself to roll a d20 and choose which of the d20s to use, the one it rolled or the one the attacker rolled.\nIf the original d20 roll has advantage or disadvantage, the creature rolls the additional d20 after advantage or disadvantage has been applied to the original roll.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.",
"REQSIGHT": True
}

GENTLEREPOSE = {"NAME": "Gentle Repose",
"LEVEL": 2,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a pinch of salt and one copper piece placed on each of the corpse's eyes, which must remain there for the duration",
"RITUAL": True,
"CONC": False,
"DURATION": "10 days",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Warding"],
"DESCRIPT": "You touch a corpse or other remains. For the duration, the target is protected from decay and can't become undead.\nThe spell also effectively extends the time limit on raising the target from the dead, since days spent under the influence of this spell don't count against the time limit of spells such as raise dead.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GIFTOFGAB = {"NAME": "Gift Of Gab",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 reaction, which you take when you speak to another creature",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "2 gp (Royalty Component)",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Deception", "Social"],
"DESCRIPT": "Jim Darkmagic is said to have invented this spell, originally calling it I said what?! Have you ever been talking to the local monarch and accidentally mentioned how their son looks like your favorite hog from when you were growing up on the family farm? We've all been there! But rather than being beheaded for an honest slip of the tongue, you can pretend it never happened—by ensuring that no one knows it happened.\nWhen you cast this spell, you skillfully reshape the memories of listeners in your immediate area, so that each creature of your choice within 5 feet of you forgets everything you said within the last 6 seconds. Those creatures then remember that you actually said the words you speak as the verbal component of the spell.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

GUSTOFWIND = {"NAME": "Gust Of Wind",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self (60-foot line)",
"COMP": [True, True, True],
"MATERIALS": "a legume seed",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Line",
"TAG": ["Control"],
"DESCRIPT": "A line of strong wind 60 feet long and 10 feet wide blasts from you in a direction you choose for the spell's duration. Each creature that starts its turn in the line must succeed on a Strength saving throw or be pushed 15 feet away from you in a direction following the line.\nAny creature in the line must spend 2 feet of movement for every 1 foot it moves when moving closer to you.\nThe gust disperses gas or vapor, and it extinguishes candles, torches, and similar unprotected flames in the area. It causes protected flames, such as those of lanterns, to dance wildly and has a 50 percent chance to extinguish them.\nAs a bonus action on each of your turns before the spell ends, you can change the direction in which the line blasts from you.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

HEALINGSPIRIT = {"NAME": "Healing Spirit",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Bonus Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Cube",
"TAG": ["Healing"],
"DESCRIPT": "You call forth a nature spirit to soothe the wounded. The intangible spirit appears in a space that is a 5-foot cube you can see within range. The spirit looks like a transparent beast or fey (your choice).\nUntil the spell ends, whenever you or a creature you can see moves into the spirit's space for the first time on a turn or starts its turn there, you can cause the spirit to restore 1d6 hit points to that creature (no action required). The spirit can't heal constructs or undead. The spirit can heal a number of times equal to 1 + your spellcasting ability modifier (minimum of twice). After healing that number of times, the spirit disappears.\nAs a bonus action on your turn, you can move the spirit up to 30 feet to a space you can see.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the healing increases by 1d6 for each slot level above 2nd.",
"REQSIGHT": True
}

HEATMETAL = {"NAME": "Heat Metal",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a piece of iron and a flame",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Fire"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Damage", "Debuff", "Control", "Utility"],
"DESCRIPT": "Choose a manufactured metal object, such as a metal weapon or a suit of heavy or medium metal armor, that you can see within range. You cause the object to glow red-hot. Any creature in physical contact with the object takes 2d8 fire damage when you cast the spell. Until the spell ends, you can use a bonus action on each of your subsequent turns to cause this damage again.\nIf a creature is holding or wearing the object and takes the damage from it, the creature must succeed on a Constitution saving throw or drop the object if it can. If it doesn't drop the object, it has disadvantage on attack rolls and ability checks until the start of your next turn.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.",
"REQSIGHT": True
}

HOLDPERSON = {"NAME": "Hold Person",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a small, straight piece of iron",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": ["Paralyzed"],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control"],
"DESCRIPT": "Choose a humanoid that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration. At the end of each of its turns, the target can make another Wisdom saving throw. On a success, the spell ends on the target.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you can target one additional humanoid for each slot level above 2nd. The humanoids must be within 30 feet of each other when you target them.",
"REQSIGHT": True
}

IMMOVABLEOBJECT = {"NAME": "Immovable Object",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "gold dust worth at least 25 gp, which the spell consumes",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility"],
"DESCRIPT": "You touch an object that weighs no more than 10 pounds and cause it to become magically fixed in place. You and the creatures you designate when you cast this spell can move the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute.\nIf the object is fixed in the air, it can hold up to 4,000 pounds of weight. More weight causes the object to fall. Otherwise, a creature can use an action to make a Strength check against your spell save DC. On a success, the creature can move the object up to 10 feet.",
"HIGHERLEVEL": "If you cast this spell using a spell slot of 4th or 5th level, the DC to move the object increases by 5, it can carry up to 8,000 pounds of weight, and the duration increases to 24 hours. If you cast this spell using a spell slot of 6th level or higher, the DC to move the object increases by 10, it can carry up to 20,000 pounds of weight, and the effect is permanent until dispelled.",
"REQSIGHT": False
}

INVISIBILITY = {"NAME": "Invisibility",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "an eyelash encased in gum arabic",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff"],
"DESCRIPT": "A creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target's person. The spell ends for a target that attacks or casts a spell.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd.",
"REQSIGHT": False
}

JIMSGLOWINGCOIN = {"NAME": "Jim's Glowing Coin",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [False, True, True],
"MATERIALS": "a coin and 2 gp (Royalty Component)",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Sphere",
"TAG": ["Control", "Debuff"],
"DESCRIPT": "Of the many tactics employed by master magician and renowned adventurer Jim Darkmagic, the old glowing coin trick is a time-honored classic. When you cast the spell, you hurl the coin that is the spell's material component to any spot within range. The coin lights up as if under the effect of a light spell. Each creature of your choice that you can see within 30 feet of the coin must succeed on a Wisdom saving throw or be distracted for the duration. While distracted, a creature has disadvantage on Wisdom (Perception) checks and initiative rolls.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

KNOCK = {"NAME": "Knock",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility"],
"DESCRIPT": "Choose an object that you can see within range. The object can be a door, a box, a chest, a set of manacles, a padlock, or another object that contains a mundane or magical means that prevents access.\nA target that is held shut by a mundane lock or that is stuck or barred becomes unlocked, unstuck, or unbarred. If the object has multiple locks, only one of them is unlocked.\nIf you choose a target that is held shut with arcane lock, that spell is suppressed for 10 minutes, during which time the target can be opened and shut normally.\nWhen you cast the spell, a loud knock, audible from as far away as 300 feet, emanates from the target object",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

LESSERRESTORATION = {"NAME": "Lesser Restoration",
"LEVEL": 2,
"SCHOOL": "Abjuration",
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
"DESCRIPT": "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

LEVITATE = {"NAME": "Levitate",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Control", "Movement"],
"DESCRIPT": "One creature or loose object of your choice that you can see within range rises vertically, up to 20 feet, and remains suspended there for the duration. The spell can levitate a target that weighs up to 500 pounds. An unwilling creature that succeeds on a Constitution saving throw is unaffected.\nThe target can move only by pushing or pulling against a fixed object or surface within reach (such as a wall or a ceiling), which allows it to move as if it were climbing. You can change the target's altitude by up to 20 feet in either direction on your turn. If you are the target, you can move up or down as part of your move. Otherwise, you can use your action to move the target, which must remain within the spell's range.\nWhen the spell ends, the target floats gently to the ground if it is still aloft.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

LOCATEANIMALSORPLANTS = {"NAME": "Locate Animals Or Plants",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a bit of fur from a bloodhound",
"RITUAL": True,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Detection"],
"DESCRIPT": "Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

LOCATEOBJECT = {"NAME": "Locate Object",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a forked twig",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Detection"],
"DESCRIPT": "Describe or name an object that is familiar to you. You sense the direction to the object's location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.\nThe spell can locate a specific object known to you, as long as you have seen it up close—within 30 feet—at least once. Alternatively, the spell can locate the nearest object of a particular kind, such as a certain kind of apparel, jewelry, furniture, tool, or weapon.\nThis spell can't locate an object if any thickness of lead, even a thin sheet, blocks a direct path between you and the object.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MAGICMOUTH = {"NAME": "Magic Mouth",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Minute",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a small bit of honeycomb and jade dust worth at least 10 gp, which the spell consumes",
"RITUAL": True,
"CONC": False,
"DURATION": "Until dispelled",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility", "Communication"],
"DESCRIPT": "You implant a message within an object in range, a message that is uttered when a trigger condition is met. Choose an object that you can see and that isn't being worn or carried by another creature. Then speak the message, which must be 25 words or less, though it can be delivered over as long as 10 minutes. Finally, determine the circumstance that will trigger the spell to deliver your message.\nWhen that circumstance occurs, a magical mouth appears on the object and recites the message in your voice and at the same volume you spoke. If the object you chose has a mouth or something that looks like a mouth (for example, the mouth of a statue), the magical mouth appears there so that the words appear to come from the object's mouth. When you cast this spell, you can have the spell end after it delivers its message, or it can remain and repeat its message whenever the trigger occurs.\nThe triggering circumstance can be as general or as detailed as you like, though it must be based on visual or audible conditions that occur within 30 feet of the object. For example, you could instruct the mouth to speak when any creature moves within 30 feet of the object or when a silver bell rings within 30 feet of it.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MAGICWEAPON = {"NAME": "Magic Weapon",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Bonus Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Buff"],
"DESCRIPT": "You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +1 bonus to attack rolls and damage rolls.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 4th level or higher, the bonus increases to +2. When you use a spell slot of 6th level or higher, the bonus increases to +3.",
"REQSIGHT": False
}

MAXIMILLIANSEARTHENGRASP = {"NAME": "Maximillian's Earthen Grasp",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, True, True],
"MATERIALS": "a miniature hand sculpted from clay",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Bludgeoning"],
"COND": ["Restrained"],
"SPELLATTCK": "Save",
"SAVETYPE": "STR",
"TARGETS": "Single Target",
"TAG": ["Control", "Damage"],
"DESCRIPT": "You choose a 5-foot-square unoccupied space on the ground that you can see within range. A Medium hand made from compacted soil rises there and reaches for one creature you can see within 5 feet of it. The target must make a Strength saving throw. On a failed save, the target takes 2d6 bludgeoning damage and is restrained for the spell's duration.\nAs an action, you can cause the hand to crush the restrained target, which must make a Strength saving throw. The target takes 2d6 bludgeoning damage on a failed save, or half as much damage on a successful one.\nTo break out, the restrained target can use its action to make a Strength check against your spell save DC. On a success, the target escapes and is no longer restrained by the hand.\nAs an action, you can cause the hand to reach for a different creature or to move to a different unoccupied space within range. The hand releases a restrained target if you do either.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

MELFSACIDARROW = {"NAME": "Melf's Acid Arrow",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, True, True],
"MATERIALS": "powdered rhubarb leaf and an adder's stomach",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Acid"],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage (both initial and later) increases by 1d4 for each slot level above 2nd.",
"REQSIGHT": False
}

MINDSPIKE = {"NAME": "Mind Spike",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Detection", "Damage"],
"DESCRIPT": "You reach into the mind of one creature you can see within range. The target must make a Wisdom saving throw, taking 3d8 psychic damage on a failed save, or half as much damage on a successful one. On a failed save, you also always know the target's location until the spell ends, but only while the two of you are on the same plane of existence. While you have this knowledge, the target can't become hidden from you, and if it's invisible, it gains no benefit from that condition against you.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.",
"REQSIGHT": True
}

MIRRORIMAGE = {"NAME": "Mirror Image",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Warding", "Combat"],
"DESCRIPT": "Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic your actions, shifting position so it's impossible to track which image is real. You can use your action to dismiss the illusory duplicates.\nEach time a creature targets you with an attack during the spell's duration, roll a d20 to determine whether the attack instead targets one of your duplicates.\nIf you have three duplicates, you must roll a 6 or higher to change the attack's target to a duplicate. With two duplicates, you must roll an 8 or higher. With one duplicate, you must roll an 11 or higher.\nA duplicate's AC equals 10 + your Dexterity modifier. If an attack hits a duplicate, the duplicate is destroyed. A duplicate can be destroyed only by an attack that hits it. It ignores all other damage and effects. The spell ends when all three duplicates are destroyed.\nA creature is unaffected by this spell if it can't see, if it relies on senses other than sight, such as blindsight, or if it can perceive illusions as false, as with truesight.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

MISTYSTEP = {"NAME": "Misty Step",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Teleportation"],
"DESCRIPT": "Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

MOONBEAM = {"NAME": "Entangle",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, True],
"MATERIALS": "several seeds of any moonseed plant and a piece of opalescent feldspar",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Radiant"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Cylinder",
"TAG": ["Damage"],
"DESCRIPT": "A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high cylinder centered on a point within range. Until the spell ends, dim light fills the cylinder.\nWhen a creature enters the spell's area for the first time on a turn or starts its turn there, it is engulfed in ghostly flames that cause searing pain, and it must make a Constitution saving throw. It takes 2d10 radiant damage on a failed save, or half as much damage on a successful one.\nA shapechanger makes its saving throw with disadvantage. If it fails, it also instantly reverts to its original form and can't assume a different form until it leaves the spell's light.\nOn each of your turns after you cast this spell, you can use an action to move the beam up to 60 feet in any direction.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d10 for each slot level above 2nd.",
"REQSIGHT": False
}

NYSTULSMAGICAURA = {"NAME": "Nystul's Magic Aura",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a small square of silk",
"RITUAL": False,
"CONC": False,
"DURATION": "24 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Deception"],
"DESCRIPT": "You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn't being carried or worn by another creature.\nWhen you cast the spell, choose one or both of the following effects. The effect lasts for the duration. If you cast this spell on the same creature or object every day for 30 days, placing the same effect on it each time, the illusion lasts until it is dispelled.\nFalse Aura. You change the way the target appears to spells and magical effects, such as detect magic, that detect magical auras. You can make a nonmagical object appear magical, a magical object appear nonmagical, or change the object's magical aura so that it appears to belong to a specific school of magic that you choose. When you use this effect on an object, you can make the false magic apparent to any creature that handles the item.\nMask. You change the way the target appears to spells and magical effects that detect creature types, such as a paladin's Divine Sense or the trigger of a symbol spell. You choose a creature type and other spells and magical effects treat the target as if it were a creature of that type or of that alignment.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

PASSWITHOUTTRACE = {"NAME": "Pass Without Trace",
"LEVEL": 2,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "ashes from a burned leaf of mistletoe and a sprig of spruce",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Circle",
"TAG": ["Buff", "Exploration"],
"DESCRIPT": "A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and can't be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

PHANTASMALFORCE = {"NAME": "Phantasmal Force",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a bit of fleece",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "INT",
"TARGETS": "Single Target",
"TAG": ["Control", "Damage"],
"DESCRIPT": "You craft an illusion that takes root in the mind of a creature that you can see within range. The target must make an Intelligence saving throw. On a failed save, you create a phantasmal object, creature, or other visible phenomenon of your choice that is no larger than a 10-foot cube and that is perceivable only to the target for the duration. This spell has no effect on undead or constructs.\nThe phantasm includes sound, temperature, and other stimuli, also evident only to the creature.\nThe target can use its action to examine the phantasm with an Intelligence (Investigation) check against your spell save DC. If the check succeeds, the target realizes that the phantasm is an illusion, and the spell ends.\nWhile a target is affected by the spell, the target treats the phantasm as if it were real. The target rationalizes any illogical outcomes from interacting with the phantasm. For example, a target attempting to walk across a phantasmal bridge that spans a chasm falls once it steps onto the bridge. If the target survives the fall, it still believes that the bridge exists and comes up with some other explanation for its fall—it was pushed, it slipped, or a strong wind might have knocked it off.\nAn affected target is so convinced of the phantasm's reality that it can even take damage from the illusion. A phantasm created to appear as a creature can attack the target. Similarly, a phantasm created to appear as fire, a pool of acid, or lava can burn the target. Each round on your turn, the phantasm can deal 1d6 psychic damage to the target if it is in the phantasm's area or within 5 feet of the phantasm, provided that the illusion is of a creature or hazard that could logically deal damage, such as by attacking. The target perceives the damage as a type appropriate to the illusion.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

PRAYEROFHEALING = {"NAME": "Prayer Of Healing",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "10 Minutes",
"RANGE": "30 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Multiple Targets",
"TAG": ["Healing"],
"DESCRIPT": "Up to six creatures of your choice that you can see within range each regain hit points equal to 2d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the healing increases by 1d8 for each slot level above 2nd.",
"REQSIGHT": True
}

PROTECTIONFROMPOISON = {"NAME": "Protection From Poison",
"LEVEL": 2,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff", "Warding"],
"DESCRIPT": "You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.\nFor the duration, the target has advantage on saving throws against being poisoned, and it has resistance to poison damage.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

PYROTECHNICS = {"NAME": "Pyrotechnics",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": [],
"COND": ["Blinded"],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Multiple Targets",
"TAG": ["Control"],
"DESCRIPT": "Choose an area of nonmagical flame that you can see and that fits within a 5-foot cube within range. You can extinguish the fire in that area, and you create either fireworks or smoke when you do so.\nFireworks. The target explodes with a dazzling display of colors. Each creature within 10 feet of the target must succeed on a Constitution saving throw or become blinded until the end of your next turn.\nSmoke. Thick black smoke spreads out from the target in a 20-foot radius, moving around corners. The area of the smoke is heavily obscured. The smoke persists for 1 minute or until a strong wind disperses it.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

RAYOFENFEEBLEMENT = {"NAME": "Ray Of Enfeeblement",
"LEVEL": 2,
"SCHOOL": "Necromancy",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Ranged",
"SAVETYPE": "CON",
"TARGETS": "Single Target",
"TAG": ["Debuff", "Combat"],
"DESCRIPT": "A black beam of enervating energy springs from your finger toward a creature within range. Make a ranged spell attack against the target. On a hit, the target deals only half damage with weapon attacks that use Strength until the spell ends.\nAt the end of each of the target's turns, it can make a Constitution saving throw against the spell. On a success, the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ROPETRICK = {"NAME": "Rope Trick",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "powdered corn extract and a twisted loop of parchment",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility"],
"DESCRIPT": "You touch a length of rope that is up to 60 feet long. One end of the rope then rises into the air until the whole rope hangs perpendicular to the ground. At the upper end of the rope, an invisible entrance opens to an extradimensional space that lasts until the spell ends.\nThe extradimensional space can be reached by climbing to the top of the rope. The space can hold as many as eight Medium or smaller creatures. The rope can be pulled into the space, making the rope disappear from view outside the space.\nAttacks and spells can't cross through the entrance into or out of the extradimensional space, but those inside can see out of it as if through a 3-foot-by-5-foot window centered on the rope.\nAnything inside the extradimensional space drops out when the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SCORCHINGRAY = {"NAME": "Scorching Ray",
"LEVEL": 2,
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
"TARGETS": "Multiple Targets",
"TAG": ["Damage"],
"DESCRIPT": "You create three rays of fire and hurl them at targets within range. You can hurl them at one target or several.\nMake a ranged spell attack for each ray. On a hit, the target takes 2d6 fire damage..",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you create one additional ray for each slot level above 2nd.",
"REQSIGHT": False
}

SEEINVISIBILITY = {"NAME": "See Invisibility",
"LEVEL": 2,
"SCHOOL": "Divination",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, True, True],
"MATERIALS": "a pinch of Talc and a small sprinkling of powdered silver",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Detection"],
"DESCRIPT": "For the duration, you see invisible creatures and objects as if they were visible, and you can see into the Ethereal Plane. Ethereal creatures and objects appear ghostly and translucent.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SHADOWBLADE = {"NAME": "Shadow Blade",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Bonus Action",
"RANGE": "Self",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 minute",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You weave together threads of shadow to create a sword of solidified gloom in your hand. This magic sword lasts until the spell ends. It counts as a simple melee weapon with which you are proficient. It deals 2d8 psychic damage on a hit and has the finesse, light, and thrown properties (range 20/60). In addition, when you use the sword to attack a target that is in dim light or darkness, you make the attack roll with advantage.\nIf you drop the weapon or throw it, it dissipates at the end of the turn. Thereafter, while the spell persists, you can use a bonus action to cause the sword to reappear in your hand.",
"HIGHERLEVEL": "When you cast this spell using a 3rd- or 4th-level spell slot, the damage increases to 3d8. When you cast it using a 5th- or 6th-level spell slot, the damage increases to 4d8. When you cast it using a spell slot of 7th level or higher, the damage increases to 5d8.",
"REQSIGHT": False
}

SHATTER = {"NAME": "Shatter",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a chip of mica",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Thunder"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CON",
"TARGETS": "Sphere",
"TAG": ["Damage"],
"DESCRIPT": "A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range. Each creature in a 10-foot-radius sphere centered on that point must make a Constitution saving throw. A creature takes 3d8 thunder damage on a failed save, or half as much damage on a successful one. A creature made of inorganic material such as stone, crystal, or metal has disadvantage on this saving throw.\nA nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.",
"REQSIGHT": False
}

SILENCE = {"NAME": "Silence",
"LEVEL": 2,
"SCHOOL": "Illusion",
"CASTTIME": "1 Action",
"RANGE": "120 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": True,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": ["Deafened"],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Sphere",
"TAG": ["Control", "Buff", "Debuff"],
"DESCRIPT": "For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it. Casting a spell that includes a verbal component is impossible there.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SKYWRITE = {"NAME": "Skywrite",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Sight",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": True,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Communication", "Utility", "Environment"],
"DESCRIPT": "You cause up to ten words to form in a part of the sky you can see. The words appear to be made of cloud and remain in place for the spell's duration. The words dissipate when the spell ends. A strong wind can disperse the clouds and end the spell early.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

SNILLOCSSNOWBALLSWARM = {"NAME": "Snilloc's Snowball Swarm",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, True, True],
"MATERIALS": "a piece of ice or a small white rock chip",
"RITUAL": False,
"CONC": False,
"DURATION": "Instantaneous",
"DAMAGETYPE": ["Cold"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Sphere",
"TAG": ["Damage"],
"DESCRIPT": "A flurry of magic snowballs erupts from a point you choose within range. Each creature in a 5-foot-radius sphere centered on that point must make a Dexterity saving throw. A creature takes 3d6 cold damage on a failed save, or half as much damage on a successful one.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.",
"REQSIGHT": False
}

SPIDERCLIMB = {"NAME": "Spider Climb",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a drop of bitumen and a spider",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Movement"],
"DESCRIPT": "Until the spell ends, one willing creature you touch gains the ability to move up, down, and across vertical surfaces and upside down along ceilings, while leaving its hands free. The target also gains a climbing speed equal to its walking speed.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SPIKEGROWTH = {"NAME": "Spike Growth",
"LEVEL": 2,
"SCHOOL": "Transmutation",
"CASTTIME": "1 Action",
"RANGE": "150 feet",
"COMP": [True, True, True],
"MATERIALS": "seven sharp thorns or seven small twigs, each sharpened to a point",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": ["Piercing"],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Circle",
"TAG": ["Control", "Damage"],
"DESCRIPT": "The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.\nThe transformation of the ground is camouflaged to look natural. Any creature that can't see the area at the time the spell is cast must make a Wisdom (Perception) check against your spell save DC to recognize the terrain as hazardous before entering it.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

SPIRITUALWEAPON = {"NAME": "Spiritual Weapon",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Bonus Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 minute",
"DAMAGETYPE": ["Force"],
"COND": [],
"SPELLATTCK": "Melee",
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Damage"],
"DESCRIPT": "You create a floating, spectral weapon within range that lasts for the duration or until you cast this spell again. When you cast the spell, you can make a melee spell attack against a creature within 5 feet of the weapon. On a hit, the target takes force damage equal to 1d8 + your spellcasting ability modifier.\nAs a bonus action on your turn, you can move the weapon up to 20 feet and repeat the attack against a creature within 5 feet of it.\nThe weapon can take whatever form you choose. Clerics of deities who are associated with a particular weapon (as St. Cuthbert is known for his mace and Thor for his hammer) make this spell's effect resemble that weapon.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for every two slot levels above 2nd.",
"REQSIGHT": False
}

SUGGESTION = {"NAME": "Suggestion",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "30 feet",
"COMP": [True, False, True],
"MATERIALS": "a snake's tongue and either a bit of honeycomb or a drop of sweet oil",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 8 hours",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "WIS",
"TARGETS": "Single Target",
"TAG": ["Control", "Social"],
"DESCRIPT": "You suggest a course of activity (limited to a sentence or two) and magically influence a creature you can see within range that can hear and understand you. Creatures that can't be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act ends the spell.\nThe target must make a Wisdom saving throw. On a failed save, it pursues the course of action you described to the best of its ability. The suggested course of action can continue for the entire duration. If the suggested activity can be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.\nYou can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that a knight give her warhorse to the first beggar she meets. If the condition isn't met before the spell expires, the activity isn't performed.\nIf you or any of your companions damage the target, the spell ends.",
"HIGHERLEVEL": "",
"REQSIGHT": True
}

SUMMONBEAST = {"NAME": "Summon Beast",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, True, True],
"MATERIALS": "a feather, tuft of fur, and fish tail inside a gilded acorn worth at least 200 gp",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Summoning"],
"DESCRIPT": "You call forth a bestial spirit. It manifests in an unoccupied space that you can see within range. This corporeal form uses the Bestial Spirit stat block. When you cast the spell, choose an environment: Air, Land, or Water. The creature resembles an animal of your choice that is native to the chosen environment, which determines certain traits in its stat block. The creature disappears when it drops to 0 hit points or when the spell ends.\nThe creature is an ally to you and your companions. In combat, the creature shares your initiative count, but it takes its turn immediately after yours. It obeys your verbal commands (no action required by you). If you don't issue any, it takes the Dodge action and uses its move to avoid danger.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, use the higher level wherever the spell's level appears in the stat block.",
"REQSIGHT": True
}

TASHASMINDWHIP = {"NAME": "Tasha's Mind Whip",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "90 feet",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "1 Round",
"DAMAGETYPE": ["Psychic"],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "INT",
"TARGETS": "Single Target",
"TAG": ["Control", "Debuff", "Damage"],
"DESCRIPT": "You psychically lash out at one creature you can see within range. The target must make an Intelligence saving throw. On a failed save, the target takes 3d6 psychic damage, and it can't take a reaction until the end of its next turn. Moreover, on its next turn, it must choose whether it gets a move, an action, or a bonus action; it gets only one of the three. On a successful save, the target takes half as much damage and suffers none of the spell's other effects.",
"HIGHERLEVEL": "When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd. The creatures must be within 30 feet of each other when you target them.",
"REQSIGHT": True
}

WARDINGBOND = {"NAME": "Warding Bond",
"LEVEL": 2,
"SCHOOL": "Abjuration",
"CASTTIME": "1 Action",
"RANGE": "Touch",
"COMP": [True, True, True],
"MATERIALS": "a pair of platinum rings worth at least 50 gp each, which you and the target must wear for the duration",
"RITUAL": False,
"CONC": False,
"DURATION": "1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Single Target",
"TAG": ["Buff", "Warding"],
"DESCRIPT": "This spell wards a willing creature you touch and creates a mystic connection between you and the target until the spell ends. While the target is within 60 feet of you, it gains a +1 bonus to AC and saving throws, and it has resistance to all damage. Also, each time it takes damage, you take the same amount of damage.\nThe spell ends if you drop to 0 hit points or if you and the target become separated by more than 60 feet. It also ends if the spell is cast again on either of the connected creatures. You can also dismiss the spell as an action.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

WARDINGWIND = {"NAME": "Warding Wind",
"LEVEL": 2,
"SCHOOL": "Evocation",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [True, False, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 10 minutes",
"DAMAGETYPE": [],
"COND": ["Deafened"],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": "Sphere",
"TAG": ["Control", "Debuff", "Environment"],
"DESCRIPT": "A strong wind (20 miles per hour) blows around you in a 10-foot radius and moves with you, remaining centered on you. The wind lasts for the spell's duration.\nThe wind has the following effects:\n-It deafens you and other creatures in its area.\n-It extinguishes unprotected flames in its area that are torch-sized or smaller.\n-It hedges out vapor, gas, and fog that can be dispersed by strong wind.\n-The area is difficult terrain for creatures other than you.\n-The attack rolls of ranged weapon attacks have disadvantage if the attacks pass in or out of the wind.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

WEB = {"NAME": "Web",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, True],
"MATERIALS": "a bit of spiderweb",
"RITUAL": False,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": ["Fire"],
"COND": ["Restrained"],
"SPELLATTCK": "Save",
"SAVETYPE": "DEX",
"TARGETS": "Cube",
"TAG": ["Control", "Environment"],
"DESCRIPT": "You conjure a mass of thick, sticky webbing at a point of your choice within range. The webs fill a 20-foot cube from that point for the duration. The webs are difficult terrain and lightly obscure their area.\nIf the webs aren't anchored between two solid masses (such as walls or trees) or layered across a floor, wall, or ceiling, the conjured web collapses on itself, and the spell ends at the start of your next turn. Webs layered over a flat surface have a depth of 5 feet.\nEach creature that starts its turn in the webs or that enters them during its turn must make a Dexterity saving throw. On a failed save, the creature is restrained as long as it remains in the webs or until it breaks free.\nA creature restrained by the webs can use its action to make a Strength check against your spell save DC. If it succeeds, it is no longer restrained.\nThe webs are flammable. Any 5-foot cube of webs exposed to fire burns away in 1 round, dealing 2d4 fire damage to any creature that starts its turn in the fire.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

WRISTPOCKET = {"NAME": "Wristpocket",
"LEVEL": 2,
"SCHOOL": "Conjuration",
"CASTTIME": "1 Action",
"RANGE": "Self",
"COMP": [False, True, False],
"MATERIALS": "",
"RITUAL": True,
"CONC": True,
"DURATION": "Up to 1 hour",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": None,
"SAVETYPE": "",
"TARGETS": None,
"TAG": ["Utility"],
"DESCRIPT": "You flick your wrist, causing one object in your hand to vanish. The object, which only you can be holding and can weigh no more than 5 pounds, is transported to an extradimensional space, where it remains for the duration.\nUntil the spell ends, you can use your action to summon the object to your free hand, and you can use your action to return the object to the extradimensional space. An object still in the pocket plane when the spell ends appears in your space, at your feet.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}

ZONEOFTRUTH = {"NAME": "Zone Of Truth",
"LEVEL": 2,
"SCHOOL": "Enchantment",
"CASTTIME": "1 Action",
"RANGE": "60 feet",
"COMP": [True, True, False],
"MATERIALS": "",
"RITUAL": False,
"CONC": False,
"DURATION": "10 minutes",
"DAMAGETYPE": [],
"COND": [],
"SPELLATTCK": "Save",
"SAVETYPE": "CHA",
"TARGETS": "Sphere",
"TAG": ["Control", "Social"],
"DESCRIPT": "You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range. Until the spell ends, a creature that enters the spell's area for the first time on a turn or starts its turn there must make a Charisma saving throw. On a failed save, a creature can't speak a deliberate lie while in the radius. You know whether each creature succeeds or fails on its saving throw.\nAn affected creature is aware of the spell and can thus avoid answering questions to which it would normally respond with a lie. Such creatures can be evasive in its answers as long as it remains within the boundaries of the truth.",
"HIGHERLEVEL": "",
"REQSIGHT": False
}


#### ------------------------- 3RD LEVEL ---------------------- ####

ENTANGLE = {"NAME": "Entangle",
"LEVEL": 3,
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


# --------------------- CLASS SPELL LISTS -------------------------------- #

SPELLLIST = []

# ARTIFICER
ARTIFICERSPELLS = [ACIDSPLASH, BOOMINGBLADE, CREATEBONFIRE, DANCINGLIGHTS, FIREBOLT, FROSTBITE, GREENFLAMEBLADE, GUIDANCE, LIGHT, LIGHTNINGLURE, MAGEHAND, MAGICSTONE, MENDING, MESSAGE, POISONSPRAY, PRESTIDIGITATION, RAYOFFROST, RESISTANCE, SHOCKINGGRASP, SPARETHEDYING, SWORDBURST, THORNWHIP, THUNDERCLAP, ABSORBELEMENTS, ALARM, CATAPULT, CUREWOUNDS, DETECTMAGIC, DISGUISESELF, EXPEDITIOUSRETREAT, FAERIEFIRE, FALSELIFE, FEATHERFALL, GREASE, IDENTIFY, JUMP, LONGSTRIDER, PURIFYFOODANDDRINK, SANCTUARY, SNARE, TASHASCAUSTICBREW, AID, ALTERSELF, ARCANELOCK, BLUR, CONTINUALFLAME, DARKVISION, ENHANCEABILITY, ENLARGEREDUCE, HEATMETAL, INVISIBILITY, LESSERRESTORATION, LEVITATE, MAGICMOUTH, MAGICWEAPON, PROTECTIONFROMPOISON, PYROTECHNICS, ROPETRICK, SEEINVISIBILITY, SKYWRITE, SPIDERCLIMB, WEB]

# BARD
BARDSPELLS = [BLADEWARD, DANCINGLIGHTS, FRIENDS, LIGHT, MAGEHAND, MENDING, MESSAGE, MINORILLUSION, PRESTIDIGITATION, THUNDERCLAP, TRUESTRIKE, VICIOUSMOCKERY, ANIMALFRIENDSHIP, BANE, CHARMPERSON, COLORSPRAY, COMMAND, COMPREHENDLANGUAGES, CUREWOUNDS, DETECTMAGIC, DISGUISESELF, DISSONANTWHISPERS, DISTORTVALUE, EARTHTREMOR, FAERIEFIRE, FEATHERFALL, HEALINGWORD, HEROISM, IDENTIFY, ILLUSORYSCRIPT, LONGSTRIDER, SILENTIMAGE, SLEEP, SPEAKWITHANIMALS, TASHASHIDEOUSLAUGHTER, THUNDERWAVE, UNSEENSERVANT, AID, ANIMALMESSENGER, BLINDNESSDEAFNESS, CALMEMOTIONS, CLOUDOFDAGGERS, CROWNOFMADNESS, DETECTTHOUGHTS, ENHANCEABILITY, ENLARGEREDUCE, ENTHRALL, GIFTOFGAB, HEATMETAL, HOLDPERSON, INVISIBILITY, KNOCK, LESSERRESTORATION, LOCATEANIMALSORPLANTS, LOCATEOBJECT, MAGICMOUTH, MIRRORIMAGE, PHANTASMALFORCE, PYROTECHNICS, SEEINVISIBILITY, SHATTER, SILENCE, SKYWRITE, SUGGESTION, WARDINGWIND, ZONEOFTRUTH]

# CLERIC
CLERICSPELLS = [GUIDANCE, LIGHT, MENDING, RESISTANCE, SACREDFLAME, SPARETHEDYING, THAUMATURGY, TOLLTHEDEAD, WORDOFRADIANCE, BANE, BLESS, CEREMONY, COMMAND, CREATEORDESTROYWATER, CUREWOUNDS, DETECTEVILANDGOOD, DETECTMAGIC, DETECTPOISONANDDISEASE, GUIDINGBOLT, HEALINGWORD, INFLICTWOUNDS, PROTECTIONFROMEVILANDGOOD, PURIFYFOODANDDRINK, SANCTUARY, SHIELDOFFAITH, AID, AUGURY, BLINDNESSDEAFNESS, CALMEMOTIONS, CONTINUALFLAME, ENHANCEABILITY, FINDTRAPS, GENTLEREPOSE, HOLDPERSON, LESSERRESTORATION, LOCATEOBJECT, PRAYEROFHEALING, PROTECTIONFROMPOISON, SILENCE, SPIRITUALWEAPON, WARDINGBOND, ZONEOFTRUTH]

# DRUID
DRUIDSPELLS = [CONTROLFLAMES, CREATEBONFIRE, DRUIDCRAFT, FROSTBITE, GUIDANCE, GUST, INFESTATION, MAGICSTONE, MENDING, MOLDEARTH, POISONSPRAY, PRIMALSAVAGERY, PRODUCEFLAME, RESISTANCE, SHAPEWATER, SHILLELAGH, THORNWHIP, THUNDERCLAP, ABSORBELEMENTS, ANIMALFRIENDSHIP, BEASTBOND, CHARMPERSON, CREATEORDESTROYWATER, CUREWOUNDS, DETECTMAGIC, DETECTPOISONANDDISEASE, EARTHTREMOR, ENTANGLE, FAERIEFIRE, FOGCLOUD, GOODBERRY, HEALINGWORD, ICEKNIFE, JUMP, LONGSTRIDER, PROTECTIONFROMEVILANDGOOD, PURIFYFOODANDDRINK, SNARE, SPEAKWITHANIMALS, THUNDERWAVE, ANIMALMESSENGER, AUGURY, BARKSKIN, BEASTSENSE, CONTINUALFLAME, DARKVISION, DUSTDEVIL, EARTHBIND, ENHANCEABILITY, ENLARGEREDUCE, FINDTRAPS, FLAMEBLADE, FLAMINGSPHERE, GUSTOFWIND, HEALINGSPIRIT, HEATMETAL, HOLDPERSON, LESSERRESTORATION, LOCATEANIMALSORPLANTS, LOCATEOBJECT, MOONBEAM, PASSWITHOUTTRACE, PROTECTIONFROMPOISON, SKYWRITE, SPIKEGROWTH, SUMMONBEAST, WARDINGWIND]

# RANGER
RANGERSPELLS = [ABSORBELEMENTS, ALARM, ANIMALFRIENDSHIP, BEASTBOND, CUREWOUNDS, DETECTMAGIC, DETECTPOISONANDDISEASE, ENSNARINGSTRIKE, ENTANGLE, FOGCLOUD, GOODBERRY, HAILOFTHORNS, HUNTERSMARK, JUMP, LONGSTRIDER, SEARINGSMITE, SNARE, SPEAKWITHANIMALS, ZEPHYRSTRIKE, AID, ANIMALMESSENGER, BARKSKIN, BEASTSENSE, CORDONOFARROWS, DARKVISION, ENHANCEABILITY, FINDTRAPS, GUSTOFWIND, HEALINGSPIRIT, LESSERRESTORATION, LOCATEANIMALSORPLANTS, LOCATEOBJECT, MAGICWEAPON, PASSWITHOUTTRACE, PROTECTIONFROMPOISON, SILENCE, SPIKEGROWTH, SUMMONBEAST]

# PALADIN
PALADINSPELLS = [BLESS, CEREMONY, COMMAND, COMPELLEDDUEL, CUREWOUNDS, DETECTEVILANDGOOD, DETECTMAGIC, DETECTPOISONANDDISEASE, DIVINEFAVOR, HEROISM, PROTECTIONFROMEVILANDGOOD, PURIFYFOODANDDRINK, SEARINGSMITE, SHIELDOFFAITH, THUNDEROUSSMITE, WRATHFULSMITE, AID, BRANDINGSMITE, FINDSTEED, GENTLEREPOSE, LESSERRESTORATION, LOCATEOBJECT, MAGICWEAPON, PRAYEROFHEALING, PROTECTIONFROMPOISON, WARDINGBOND, ZONEOFTRUTH]

# SORCERER
SORCERERSPELLS = [ACIDSPLASH, BLADEWARD, BOOMINGBLADE, CHILLTOUCH, CONTROLFLAMES, CREATEBONFIRE, DANCINGLIGHTS, FIREBOLT, FRIENDS, FROSTBITE, GREENFLAMEBLADE, GUST, INFESTATION, LIGHT, LIGHTNINGLURE, MAGEHAND, MENDING, MESSAGE, MINDSLIVER, MINORILLUSION, MOLDEARTH, POISONSPRAY, PRESTIDIGITATION, RAYOFFROST, SHAPEWATER, SHOCKINGGRASP, SWORDBURST, THUNDERCLAP, TRUESTRIKE, ABSORBELEMENTS, BURNINGHANDS, CATAPULT, CHAOSBOLT, CHARMPERSON, CHROMATICORB, COLORSPRAY, COMPREHENDLANGUAGES, DETECTMAGIC, DISGUISESELF, DISTORTVALUE, EARTHTREMOR, EXPEDITIOUSRETREAT, FALSELIFE, FEATHERFALL, FOGCLOUD, GREASE, ICEKNIFE, JUMP, MAGEARMOR, MAGICMISSILE, RAYOFSICKNESS, SHIELD, SILENTIMAGE, SLEEP, TASHASCAUSTICBREW, THUNDERWAVE, WITCHBOLT, AGANAZZARSSCORCHER, ALTERSELF, BLINDNESSDEAFNESS, BLUR, CLOUDOFDAGGERS, CROWNOFMADNESS, DARKNESS, DARKVISION, DETECTTHOUGHTS, DRAGONSBREATH, DUSTDEVIL, EARTHBIND, ENHANCEABILITY, ENLARGEREDUCE, FLAMEBLADE, FLAMINGSPHERE, GUSTOFWIND, HOLDPERSON, INVISIBILITY, KNOCK, LEVITATE, MAGICWEAPON, MAXIMILLIANSEARTHENGRASP, MINDSPIKE, MIRRORIMAGE, MISTYSTEP, PHANTASMALFORCE, PYROTECHNICS, SCORCHINGRAY, SEEINVISIBILITY, SHADOWBLADE, SHATTER, SNILLOCSSNOWBALLSWARM, SPIDERCLIMB, SUGGESTION, TASHASMINDWHIP, WARDINGWIND, WEB]

# WIZARD
WIZARDSPELLS = [ACIDSPLASH, BLADEWARD, BOOMINGBLADE, CHILLTOUCH, CONTROLFLAMES, CREATEBONFIRE, DANCINGLIGHTS, FIREBOLT, FRIENDS, FROSTBITE, GREENFLAMEBLADE, GUST, INFESTATION, LIGHT, LIGHTNINGLURE, MAGEHAND, MENDING, MESSAGE, MINDSLIVER, MINORILLUSION, MOLDEARTH, POISONSPRAY, PRESTIDIGITATION, RAYOFFROST, SHAPEWATER, SHOCKINGGRASP, SWORDBURST, THUNDERCLAP, TOLLTHEDEAD, TRUESTRIKE, ABSORBELEMENTS, ALARM, BURNINGHANDS, CATAPULT, CAUSEFEAR, CHARMPERSON, CHROMATICORB, COLORSPRAY, COMPREHENDLANGUAGES, DETECTMAGIC, DISGUISESELF, DISTORTVALUE, EARTHTREMOR, EXPEDITIOUSRETREAT, FALSELIFE, FEATHERFALL, FINDFAMILIAR, FOGCLOUD, FROSTFINGERS, GREASE, ICEKNIFE, IDENTIFY, ILLUSORYSCRIPT, JIMSMAGICMISSILE, JUMP, LONGSTRIDER, MAGEARMOR, MAGICMISSILE, PROTECTIONFROMEVILANDGOOD, RAYOFSICKNESS, SHIELD, SILENTIMAGE, SLEEP, SNARE, TASHASCAUSTICBREW, TASHASHIDEOUSLAUGHTER, TENSORSFLOATINGDISK, THUNDERWAVE, UNSEENSERVANT, WITCHBOLT, GIFTOFALACRITY, MAGNIFYGRAVITY, AGANAZZARSSCORCHER, ALTERSELF, ARCANELOCK, AUGURY, BLINDNESSDEAFNESS, BLUR, CLOUDOFDAGGERS, CONTINUALFLAME, CROWNOFMADNESS, DARKNESS, DARKVISION, DETECTTHOUGHTS, DRAGONSBREATH, DUSTDEVIL, EARTHBIND, ENHANCEABILITY, ENLARGEREDUCE, FLAMINGSPHERE, GENTLEREPOSE, GIFTOFGAB, GUSTOFWIND, HOLDPERSON, INVISIBILITY, JIMSGLOWINGCOIN, KNOCK, LEVITATE, LOCATEOBJECT, MAGICMOUTH, MAGICWEAPON, MAXIMILLIANSEARTHENGRASP, MELFSACIDARROW, MINDSPIKE, MIRRORIMAGE, MISTYSTEP, NYSTULSMAGICAURA, PHANTASMALFORCE, PYROTECHNICS, RAYOFENFEEBLEMENT, ROPETRICK, SCORCHINGRAY, SEEINVISIBILITY, SHADOWBLADE, SHATTER, SKYWRITE, SNILLOCSSNOWBALLSWARM, SPIDERCLIMB, SUGGESTION, TASHASMINDWHIP, WARDINGWIND, WEB, FORTUNESFAVOR, IMMOVABLEOBJECT, WRISTPOCKET, SAPPINGSTING]

# WARLOCK
WARLOCKSPELLS = [BLADEWARD, BOOMINGBLADE, CHILLTOUCH, CREATEBONFIRE, ELDRITCHBLAST, FRIENDS, FROSTBITE, GREENFLAMEBLADE, INFESTATION, LIGHTNINGLURE, MAGEHAND, MAGICSTONE, MINDSLIVER, MINORILLUSION, POISONSPRAY, PRESTIDIGITATION, SWORDBURST, THUNDERCLAP, TOLLTHEDEAD, TRUESTRIKE, ARMOROFAGATHYS, ARMSOFHADAR, CAUSEFEAR, CHARMPERSON, COMPREHENDLANGUAGES, DISTORTVALUE, EXPEDITIOUSRETREAT, HELLISHREBUKE, HEX, ILLUSORYSCRIPT, PROTECTIONFROMEVILANDGOOD, UNSEENSERVANT, WITCHBOLT, CLOUDOFDAGGERS, CROWNOFMADNESS, DARKNESS, EARTHBIND, ENTHRALL, HOLDPERSON, INVISIBILITY, MINDSPIKE, MIRRORIMAGE, MISTYSTEP, RAYOFENFEEBLEMENT, SHADOWBLADE, SHATTER, SPIDERCLIMB, SUGGESTION]
