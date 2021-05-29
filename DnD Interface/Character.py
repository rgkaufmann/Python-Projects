# DnD Custom Character Object
# Julia Hill, Samantha Cibere, Alex Hardjono, Gaurav Tenkila, Ryan Kaufmann

# Import statements
import numpy as np
import ClassObjects as CO

class Character:
    name = ''
    race = ''
    background = ''
    ideals = []
    bonds = []
    flaws = []
    alignment = ''
    exp = 0

    exhaustion = 0
    heropoints = 0
    piety = 0

    bardinspo = False
    dminspo = False

    classlvls = list(np.zeros(13))
    classinfo = []

    saves = [0, 0, 0, 0, 0, 0]
    stats = [10, 10, 10, 10, 10, 10]
    deathsaves = [0, 0]

    racespeed = [0, 0, 0, 0, 0]
    classspeeds = [0, 0, 0, 0, 0]
    racespeedrestrictions = {}
    classspeedrestrictions = {}

    size = {}
    age = 0
    ageinfo = ''
    type = 'Humanoid'
    vision = [0, 0, 0, 0]
    height = 0
    weight = 0
    skin = ''
    hair = ''
    eyes = ''

    racelanguages = []
    backlanguages = []
    classlanguages = []
    raceskills = []
    backskills = []
    classskills = []
    racetools = []
    backtools = []
    classtools = []
    raceothers = []
    backothers = []
    classothers = []

    racialac = ''
    racialacmod = 0
    classac = ''
    classacmod = 0
    racialacrestricts = []
    classacrestricts = []

    hp = 0
    temphp = 0
    racialhp = 0
    conditions = []

    racedamresists = []
    classdamresists = []
    damvulners = []
    damimmunes = []
    raceconimmunes = []
    classconimmunes = []

    racialabilities = {}
    racialabilitytags = {}

    inventory = []
    attunement = 0
    coins = [0, 0, 0, 0, 0]
    encumbrance = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def updateRace(self, racestats, size, racespeeds, speedrestrictions, age,\
                   type, vision, rlang, rskills, rtools, rothers, acmod, ac,\
                   acrestricts, hp, damres, damimm, conimm, abilities, atags,\
                   race):
        self.stats += racestats
        self.size = size
        self.racespeed = racespeeds
        self.racespeedrestrict = speedrestrictions
        self.ageinfo = age
        self.type = type
        self.vision[0] = vision
        self.racelanguages = rlang
        self.raceskills = rskills
        self.racetools = rtools
        self.raceothers = rothers
        self.raceacmod = acmod
        self.racialac = ac
        self.racialacrestricts = acrestricts
        self.racialhp = hp
        self.racedamresists = damres
        self.damimmunes = damimm
        self.raceconimmunes = conimm
        self.racialabilities = abilities
        self.racialabilitytags = atags
        self.race = race

    # All the get functions
    def getName(self):
        return self.name


    def getRace(self):
        return self.race


    def getBackground(self):
        return self.background


    def getIdeals(self):
        return self.ideals


    def getBonds(self):
        return self.bonds


    def getFlaws(self):
        return self.flaws


    def getAlignment(self):
        return self.alignment


    def getExp(self):
        return self.exp


    def getExhaustion(self):
        return self.exhaustion


    def getHeroPoints(self):
        return self.heropoints


    def getPiety(self):
        return self.piety


    def isBardInspo(self):
        return self.bardinspo


    def isDMInspo(self):
        return self.dminspo


    def getClassLevels(self):
        return self.classlvls


    def getClassInfo(self):
        return self.classinfo


    def getSaves(self):
        return self.saves


    def getStats(self):
        return self.stats


    def getDeathSaves(self):
        return self.deathsaves


    def getRaceSpeed(self):
        return self.racespeed


    def getClassSpeed(self):
        return self.classspeeds


    def getRaceSpeedRestrictions(self):
        return self.racespeedrestrictions


    def getClassSpeedRestrictions(self):
        return self.classspeedrestrictions


    def getSize(self):
        return self.size


    def getAge(self):
        return self.age


    def getAgeInfo(self):
        return self.ageinfo


    def getType(self):
        return self.type


    def getVision(self):
        return self.vision


    def getHeight(self):
        return self.height


    def getWeight(self):
        return self.weight


    def getSkin(self):
        return self.skin


    def getHair(self):
        return self.hair


    def getEyes(self):
        return self.eyes


    def getRaceLanguages(self):
        return self.racelanguages


    def getBackLanguages(self):
        return self.backlanguages


    def getClassLanguages(self):
        return self.classlanguages


    def getAllLanguages(self):
        return self.racelanguages + self.backlangauges + self.classlangauges


    def getRaceSkills(self):
        return self.raceskils


    def getBackSkills(self):
        return self.backskills


    def getClassSkills(self):
        return self.classskills


    def getAllSkills(self):
        return self.raceskills + self.backskills + self.classskills


    def getRaceTools(self):
        return self.racetools


    def getBackTools(self):
        return self.backtools


    def getClassTools(self):
        return self.classtools


    def getAllTools(self):
        return self.racetools + self.backtools + self.classtools


    def getRaceOthers(self):
        return self.raceothers


    def getBackOthers(self):
        return self.backothers


    def getClassOthers(self):
        return self.classothers


    def getAllOthers(self):
        return self.raceothers + self.backothers + self.classothers


    def getRacialAC(self):
        return self.racialac


    def getRacialACMod(self):
        return self.racialacmod


    def getClassAC(self):
        return self.classac


    def getClassACMod(self):
        return self.classacmod


    def getRacialACRestricts(self):
        return self.racialacrestricts


    def getClassACRestricts(self):
        return self.classacrestricts


    def getHP(self):
        return self.hp


    def getTempHP(self):
        return self.temphp


    def getRacialHP(self):
        return self.racialhp


    def getConditions(self):
        return self.conditions


    def getRaceDamResists(self):
        return self.racedamresists


    def getClassDamResists(self):
        return self.classdamresists


    def getDamVulners(self):
        return self.damvulners


    def getDamImmunes(self):
        return self.damimmunes


    def getRaceConImmunes(self):
        return self.raceconimmunes


    def getClassConImmunes(self):
        return self.classconimmunes


    def getRacialAbilityTags(self):
        return self.racialabilitytags


    def getRacialAbilities(self):
        return self.racialabilities


    def getInventory(self):
        return self.inventory


    def getAttunement(self):
        return self.attunement


    def getCoins(self):
        return self.coins


    def isEncumbrance(self):
        return self.encumbrance
