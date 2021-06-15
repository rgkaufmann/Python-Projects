class ClassParent:

    saves = [0, 0, 0, 0, 0, 0, 0]
    hitdie = ''
    toolprofs = []      # tool proficiencies
    toolchoose = [0]    # 0th el is number of tools one can choose from,
                        # 1st el is list of the choices
    skillsinfo = []     # skill proficiencies
    skillschoose = [0]  # 0th el is number of skills one can choose from,
                        # 1st el is list of the choices
    otherprofs = []     # weapon and armor proficiencies

    def __init__(self):
        return 0

    def getSaves(self):
        return self.saves

    def getHitDie(self):
        return self.hitdie

    def getToolProfs(self):
        return self.toolprofs

    def getToolChoose(self):
        return self.toolchoose

    def getSkillInfo(self):
        return self.skillinfo

    def getSkillsChoose(self):
        return self.skillschoose

    def getOtherProfs(self):
        return self.otherprofs

    def setSaves(self, newsaves):
        self.saves = newsaves

    def setHitDie(self, newhitdie):
        self.hitdie = newhitdie

    def setToolProfs(self, newtools):
        self.toolprofs = newtools

    def setToolChoose(self, newtoolschoose):
        self.toolchoose = newtoolschoose

    def setSkillInfo(self, newskillinfo):
        self.skillinfo = newskillinfo

    def setSkillsChoose(self, newskillschoose):
        self.skillschoose = newskillschoose

    def setOtherProfs(self, newother):
        self.otherprofs = newother
