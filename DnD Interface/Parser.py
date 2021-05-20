# DnD Custom File Parser
# Julia Hill, Samantha Cibere, Alex Hardjono, Gaurav Tenkila, Ryan Kaufmann

# Import statements
import numpy as np
from Constants import STATS, LANGUAGES, SKILLS, TOOLS, ARMORTYPES, WEAPONS

# Finds and returns location (indices) of blank lines given list of lines
def getBlankLines(lines):
    indices = []

    for index in range(len(lines)):
        if lines[index] == '\n':
            indices.append(index)

    return indices


# Converts a list of lines into a dictionary with the following:
# Keys- names of attributes
# Values - information pertaining to those attributes, stored as list
def convertToDictionary(lines):
    # Calls the above method to find the indices of the blank lines in the file
    indices = getBlankLines(lines)
    linesdict = {}

    # The if-elif-else statement is useful for splicing the list
    # Note also the removal of the last two characters (':' and newline)
    for index in range(len(indices) + 1):
        if index == 0:
            linesection = lines[:indices[index]]
            linesdict.update({linesection[0][:-2]: linesection[1:]})
        elif index == len(indices):
            linesection = lines[(indices[index - 1] + 1):]
            linesdict.update({linesection[0][:-2]: linesection[1:]})
        else:
            linesection = lines[(indices[index - 1] + 1):indices[index]]
            linesdict.update({linesection[0][:-2]: linesection[1:]})

    return linesdict


# Converts a String into a List when the String is written in pseudocode.
# To be converted, Strings have the format of '[1, 2, 3]\n'
def convertStringToList(string):
    list = string.split(", ")
    list[0] = list[0][1:]
    list[-1] = list[-1][:-2]

    return list


# IMPORTANT: User input method MUST be changed later to make use of GUI
# When a user has a choice between the DnD stat they can increase, this method
# is called. It queries the user with a list of possible stats and then
# increases the specified stat by a given amount. The result is added later.
def chooseStats(choicelist, increase):
    stataddition = [0, 0, 0, 0, 0, 0]

    while True:
        # Construction of the question that is asked to the user.
        query = 'Choose one of the following stats to increase by '
        query += str(increase) + ':\n'
        query += " ".join(choicelist) + '\n'

        statchoice = input(query)

        try:
            # If statchoice exists in the choicelist, add it to the Stats
            # lists with the increase parameter, break loop.
            if statchoice.upper() in choicelist:
                stataddition[STATS.index(statchoice.upper())] += increase
                break
        except ValueError:
            # In the unlikely case that a value error occurs, the following
            # message is given to the user.
            print('The input was not understood. Please choose again.')
            continue

        # If statchoice is not in choicelist, the user is notified and
        # asked again.
        print('The chosen stat was not an option. Please choose again.')
        print()

    return stataddition


# IMPORTANT: User input method MUST be changed later to make use of GUI
# When a user has a choice between languages that they can learn, this method is
# called. It queries the user with a list of possible languages and then returns
# a language that the user picks.
def chooseLanguage(alreadyknown):
    # This method takes a list of languages the user already knows and uses it
    # to construct the choices the user has.
    choices = [lang for lang in LANGUAGES if lang not in alreadyknown]

    while True:
        # Construction of the question that is asked to the user.
        query = 'Choose one of the following languages to learn:\n'
        query += ', '.join(choices) + '\n'

        langchoice = input(query)

        try:
            # If langchoice exists in the choices, add it to the return the
            # chosen language and exit the method.
            if langchoice.lower() in [choice.lower() for choice in choices]:
                return langchoice
        except ValueError:
            # In the unlikely case that a value error occurs, the following
            # message is given to the user.
            print('The input was not understood. Please choose again.')
            continue

        # If langchoice is not in choices, the user is notified and
        # asked again.
        print('The chosen language was not an option. Please choose again.')
        print()


# IMPORTANT: User input method MUST be changed later to make use of GUI
# When a user has a choice between proficiencies that they can learn, this
# method is called. It queries the user with a list of possible proficiencies
# and then returns a language that the user picks.
def chooseProfs(choicelist):
    while True:
        # Construction of the question that is asked to the user.
        query = 'Choose one of the following proficiencies to learn:\n'
        query += ', '.join(choicelist) + '\n'

        profchoice = input(query)

        try:
            # If profchoice exists in the choicelist, the value is returned.
            if profchoice.lower() in [choice.lower() for choice in choicelist]:
                return profchoice
        except ValueError:
            # In the unlikely case that a value error occurs, the following
            # message is given to the user.
            print('The input was not understood. Please choose again.')
            continue

        # If profchoice is not in choicelist, the user is notified and
        # asked again.
        print('The chosen proficiency was not an option. Please choose again.')
        print()


# Divides proficiencies into three standard sections; skills, tools, and other;
# using the SKILLS and TOOLs constants. Returns all three lists.
def splitProfs(profs):
    skillprofs, toolprofs, otherprofs = [], [], []

    for prof in profs:
        if prof in SKILLS:
            skillprofs.append(prof)
        elif prof in TOOLS:
            toolprofs.append(prof)
        else:
            otherprofs.append(prof)

    return skillprofs, toolprofs, otherprofs


# Uses the list of lines in the Stats section to create the racial bonus to
# stats that characters receive. Returns the stat increases as a list.
# Stats are [Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma].
def parseStats(statlines):
    # Compiles any definite increases to stats first, before moving to choices.
    racialstats = np.array([int(statlines[index][:-1]) for index in \
                                                     range(len(statlines) - 1)])
    choice = statlines[-1]

    # If choice is not zero, the user will have some decision to make about
    # their stat increases. If choice contains brackets, there is a reduced
    # number of stats this increase can apply to.
    if '[' in choice:
        # Uses the locations of commas in the array to find the choices the User
        # gets.
        commas = [index for index in range(len(choice)) if choice[index] == ',']
        choicelist = []

        for commalocation in commas:
            choicelist.append(choice[(commalocation - 3):commalocation])
        choicelist.append((choice[(choice.index(']') - 3):choice.index(']')]))

        # Calls upon the chooseStats method to get the user input and applies it
        # to the racial stats defined above.
        racialstats += chooseStats(choicelist, int(choice[:1]))
    elif '1' in statlines[-1]:
        # Calls upon the chooseStats method to get the user input and applies it
        # to the racial stats defined above.
        racialstats += chooseStats(np.array(STATS)[np.where(racialstats == 0)], 1)
    elif '2' in statlines[-1]:
        # Calls upon the chooseStats method twice to get the user input and
        # applies the results to the racial stats defined above.
        racialstats += chooseStats(np.array(STATS)[np.where(racialstats == 0)], 1)
        racialstats += chooseStats(np.array(STATS)[np.where(racialstats == 0)], 1)

    return racialstats


# Uses the list of lines in the Size section to determine the size the character
# is at a given level. The information is returned in a dictionary with:
# Keys - Levels
# Values - Sizes
def parseSize(sizelines):
    sizedict = {}

    for line in sizelines:
        # Uses the position of the " " character to determine where the
        # information is stored.
        firstspace = line.index(' ')
        sizedict.update({int(line[:firstspace]): line[(firstspace + 3):-1]})

    return sizedict


# Uses the list of lines in the Speed section to determine the speeds of a given
# race, stored and returned as a list. Also develops a dictionary with all the
# restrictions coming from the type of armor the character is wearing. The
# dictionary contains boolean lists with the following:
# Keys - Type of Restriction (Slowed by Heavy Armor, Negated by Heavy/Medium
#        Armor)
# Values - Boolean List with one entry per movement type
# Speeds are [Walk, Climb, Swim, Fly, Burrow].
def parseSpeed(speedlines):
    # Instantiates all lists.
    racialspeed = []
    heavyarmorslow = []
    heavyarmorrestrict = []
    mediumarmorrestrict = []

    # Each line contains information for a given speed type in the order above.
    # If a bracket ('[') is present, the given line is not slowed by heavy
    # armor. If a parenthesis ('(') is present, the given line is negated by an
    # armor type. The line also has an integer value representing the speed.
    for line in speedlines:
        if '[' in line:
            heavyarmorslow.append(False)
            heavyarmorrestrict.append(False)
            mediumarmorrestrict.append(False)
            racialspeed.append(int(line[:line.index('[')]))
        elif '(' in line:
            heavyarmorslow.append(True)

            # 'H' and 'M' are used to distinguish what armor types negate the
            # specified movement speed: 'H' for Heavy armor, 'M' for medium.
            if 'H' in line:
                heavyarmorrestrict.append(True)
            else:
                heavyarmorrestrict.append(False)

            if 'M' in line:
                mediumarmorrestrict.append(True)
            else:
                mediumarmorrestrict.append(False)

            racialspeed.append(int(line[:line.index('(')]))
        else:
            heavyarmorslow.append(True)
            heavyarmorrestrict.append(False)
            mediumarmorrestrict.append(False)
            racialspeed.append(int(line))

    # The restrictions are all compiled into a dictionary for ease.
    restricts = {'HSlow': heavyarmorslow, 'HRestrict': heavyarmorrestrict,
                 'MRestrict': mediumarmorrestrict}

    return racialspeed, restricts


# Uses the list of lines in the Vision section to determine the quality of
# vision a given race has, returned as a string. The race can have either
# regular vision (0), dark vision (1), or superior dark vision (2).
def parseVision(visionlines):
    if '0' in visionlines[0]:
        return "Your character's vision is average. It can be impaired by " + \
               "darkness or dim light."
    elif '1' in visionlines[0]:
        return "Your character has dark vision to a range of 60ft. In this" + \
               " range, you can see in darkness as if it was dim light or " + \
               "in dim light as if it bright light. You cannot discern " + \
               "color in darkness."
    elif '2' in visionlines[0]:
        return "Your character has dark vision to a range of 120ft. In this" + \
               " range, you can see in darkness as if it was dim light or " + \
               "in dim light as if it bright light. You cannot discern " + \
               "color in darkness."


# Uses the list of lines in the Language section to determine the languages that
# a character of a given race knows. Returns the languages as a list.
def parseLanguage(languagelines):
    languages = []

    # Each line is either a language that the creature knows or a number of
    # extra languages the creature can learn.
    for line in languagelines:
        try:
            # If the line is a number, it represents extra language and can be
            # chosen by the user. The languages the creature already knows is
            # passed as a list into the chooseLanguage method.
            for additional in range(int(line)):
                languages.append(chooseLanguage(languages))
        except ValueError:
            # If a value error is raised in the above, then the line is not an
            # integer and, thus, is simply a language that the creature knows.
            languages.append(line[:-1])

    return languages


# Uses the list of lines in the Profs section to determine the proficiencies
# that a certain race of characters gain. Returns three lists of proficiencies
# divided according to the splitProfs method above.
def parseProfs(proflines):
    allprofs = []

    # Each line can either be a list or an integer describing the number of
    # proficiencies that a user must pick. If the line is an integer, the
    # options that a user has is stored in the following line.
    for index in range(len(proflines)):
        try:
            # If the line is an integer, the following for-statement is valid.
            # The line is then fully converted into an integer and a list of
            # choices is generated using the convertStringToList method. The
            # list of choices are passed to the chooseProfs method for user
            # input.
            for choice in range(int(proflines[index])):
                proflines[index] = int(proflines[index])
                choices = convertStringToList(proflines[index + 1])

                allprofs.append(chooseProfs(choices))
        except ValueError:
            # If the line is instead a list, the line is checked to see if the
            # list is empty, in which nothing is done, or if the previous line
            # is an integer, in which the line must be chosen from as above.
            # Otherwise the list of proficienceis are simply concatenated onto
            # the proficiencies list.
            if proflines[index] != '[]' and type(proflines[index - 1]) != int:
                allprofs += convertStringToList(proflines[index])

    return splitProfs(allprofs)


# Uses the list of lines in the AC section to determine the Armor Class
# additions or adaptations that a race gains. Returns three values: the
# addition, if there is a flat addition; restrictions to this addition; a string
# representing a different method of calculating AC.
def parseAC(aclines):
    newcalc = False
    addition = 0
    restrictions = []
    ac = aclines[0]

    try:
        # The appears of a parenthesis ('(') indicates that there are some
        # restrictions on a flat addition to armor class. Either way, there will
        # be an addition that is recorded by converting a string to an integer.
        # The restrictions are converted to a list if necessary.
        if '(' not in ac:
            addition = int(ac)
        else:
            addition = int(ac[:ac.index('(')])
            restrictions += convertStringToList(ac[ac.index('('):])
    except ValueError:
        # If the line cannot be converted to an integer, the line must describe
        # a new method of calculating the AC. In which case, the information is
        # stored as a string and will be dealt by the object at a later point.
        newcalc = ac[:-1]

    return addition, restrictions, newcalc


# Uses the list of lines in the Abilities section to determine any extra
# abilities a character gains due to their race. The information is stored in
# two dictionaries. The first contains the information in string form with the
# following:
# Keys - Ability Names
# Values - Ability Information
# The second contains a list of tags that can identify the ability, its effects,
# its restrictions, etc. It has the following:
# Keys - Ability Names
# Values - Ability Tags
def parseAbilities(abilitylines):
    infodict, tagsdict = {}, {}

    # Abilities come in groups of three lines. The first is the name of the
    # ability. The second is the information of the ability. The third is a list
    # of the tags.
    for index in range(int(len(abilitylines) / 3)):
        nameline = abilitylines[int(index * 3)]
        infoline = abilitylines[int(index * 3) + 1]
        tagline = abilitylines[int(index * 3) + 2]

        # The first dictionary is constructed simply
        infodict.update({nameline[1:-1]: infoline[:-1]})

        # In order to gain the tags, the placements of the commas must first be
        # identified.
        commas = [index for index in range(len(tagline)) \
                        if tagline[index] == ',']

        # If there are no commas, there is only one tag and can be found easily.
        if commas == []:
            tags = [tagline[1:-1]]
        # Otherwise, a list of tags must be created by iterating through all the
        # commas.
        else:
            tags = [tagline[1:commas[0]]]
            for index in range(len(commas) - 1):
                tags.append(tagline[(commas[index] + 1):commas[index + 1]])
            tags.append(tagline[(commas[-1] + 1):-1])

        # The list of tags are then combined into the second dictionary.
        tagsdict.update({nameline[1:-1]: tags})

    return infodict, tagsdict


# Takes a given file name or file path and returns all the racial information,
# abilities, and so forth for the related file.
def parseRace(filename):
    # Checks to see if the file is a .race file.
    if '.race' not in filename:
        print('The specified file is not a race file. Please pick another.')
        return None

    # Otherwise, the file is opened and the lines are stored as a list.
    with open(filename) as file:
        lines = file.readlines()

    # The list of lines are converted to a dictionary and then each key is used
    # to generate the relevant information from the remainder of the lines list.
    linesdict = convertToDictionary(lines)
    statinfo = parseStats(linesdict['Stats'])
    sizeinfo = parseSize(linesdict['Size'])
    speedinfo, speedrestirctions = parseSpeed(linesdict['Speed'])
    ageinfo = linesdict['Age'][0][:-1]
    typeinfo = linesdict['Type'][0][:-1]
    visioninfo = parseVision(linesdict['Vision'])
    languageinfo = parseLanguage(linesdict['Language'])
    skillinfo, toolinfo, otherinfo = parseProfs(linesdict['Profs'])
    raceacmod, acrestricts, racialac = parseAC(linesdict['AC'])
    racialhp = int(linesdict['HP'][0])
    damresistinfo = convertStringToList(linesdict['Resistances'][0])
    damimmuneinfo = convertStringToList(linesdict['DamageImmune'][0])
    conresistinfo = convertStringToList(linesdict['ConditionImmune'][0])
    abilityinfo, abilitytags = parseAbilities(linesdict['Abilities'])

    # All of the information is then returned (to be made into a single object
    # at a later date).
    return statinfo, sizeinfo, speedinfo, speedrestirctions, ageinfo, typeinfo,\
           visioninfo, languageinfo, skillinfo, toolinfo, otherinfo, raceacmod,\
           acrestricts, racialac, racialhp, damresistinfo, damimmuneinfo,\
           conresistinfo, abilityinfo, abilitytags


# Returns list of Booleans, element is true if class is proficient
# in the given saving throw in stat (in order of STATS), false otherwise.
def parseSaves(saveslist):
    saveslist = [save[:-1] for save in saveslist]
    return list(np.where(np.isin(STATS, saveslist), True, False))


# For given class file, retrieves class feature data.
# Returns saves, hit die, armor, weapon, and tool proficiencies, and skills. All
# are returned as lists, except hitdie, which is a string.
def parseClass(filename):
    # Checks to see if the file is a .class file.
    if '.class' not in filename:
        print('The specified file is not a class file. Please pick another.')
        return None

    # Otherwise, the file is opened and the lines are stored as a list.
    with open(filename) as file:
        lines = file.readlines()

    # The list of lines are converted to a dictionary and then each key is used
    # to generate the relevant information from the remainder of the lines list.
    linesdict = convertToDictionary(lines)
    saves = parseSaves(linesdict['Saves'])
    hitdie = linesdict['Hit Die'][0][:-1]
    otherprofs = parseProfs(linesdict['Armor']) + \
                 parseProfs(linesdict['Weapon'])
    toolprofs = parseProfs(linesdict['Tool'])
    skillsinfo = parseProfs(LinesDict['Skills'])

    # All of the information is then returned (to be made into a single object
    # at a later date).
    return saves, hitdie, otherprofs, toolprofs, skillsinfo
