import re


class day4:
    def problema1(self):
        sectionsAssigned = self.sectioning()
        print(len(self.overWrittenElves(sectionsAssigned)))

    def overWrittenElves(self, sectionsAssigned):
        elvesToLayOff = []
        lastElve = len(sectionsAssigned)

        for elve in range(1, lastElve, 2):
            nextElve = elve+1
            begOfSectionFstElve = sectionsAssigned[elve][0]
            endOfSectionFstElve = sectionsAssigned[elve][-1]
            begOfSectionSndElve = sectionsAssigned[nextElve][0]
            endOfSectionSndElve = sectionsAssigned[nextElve][-1]
            if (begOfSectionFstElve <= begOfSectionSndElve and endOfSectionFstElve >= endOfSectionSndElve):
                elvesToLayOff.append(nextElve)

            elif (begOfSectionFstElve >= begOfSectionSndElve and endOfSectionFstElve <= endOfSectionSndElve):
                elvesToLayOff.append(elve)

        return elvesToLayOff

    def problema2(self):
        sectionsAssigned = self.sectioning()
        print(len(self.overWrittenElves2(sectionsAssigned)))

    def overWrittenElves2(self, sectionsAssigned):
        elvesToLayOff = []
        lastElve = len(sectionsAssigned)

        for elve in range(1, lastElve, 2):
            nextElve = elve+1
            begOfSectionFstElve = sectionsAssigned[elve][0]
            endOfSectionFstElve = sectionsAssigned[elve][-1]
            begOfSectionSndElve = sectionsAssigned[nextElve][0]
            endOfSectionSndElve = sectionsAssigned[nextElve][-1]
            if (begOfSectionFstElve <= begOfSectionSndElve and endOfSectionFstElve >= endOfSectionSndElve):
                elvesToLayOff.append(elve)

            elif (begOfSectionFstElve >= begOfSectionSndElve and endOfSectionFstElve <= endOfSectionSndElve):
                elvesToLayOff.append(elve)

            elif (begOfSectionSndElve >= begOfSectionFstElve and begOfSectionSndElve <= endOfSectionFstElve):
                elvesToLayOff.append(elve)

            elif (endOfSectionSndElve <= endOfSectionFstElve and endOfSectionSndElve >= begOfSectionFstElve):
                elvesToLayOff.append(elve)
        return elvesToLayOff

    def sectioning(self):
        sectionsAssigned = {}
        file = open("./day4/day4Input.txt", "r")
        elve = 1
        for line in file.readlines():
            sections = re.sub("\n", "", line)
            sections = sections.split(",")
            for section in sections:
                splitted = section.split("-")
                begOfSection = int(splitted[0])
                endOfSection = int(splitted[1])
                if elve not in sectionsAssigned:
                    sectionsAssigned[elve] = []
                sectionsAssigned[elve].append(begOfSection)
                sectionsAssigned[elve].append(endOfSection)
                elve += 1
        return sectionsAssigned


day4().problema2()
