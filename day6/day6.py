import re


class day6:
    def problema1(self):
        buffer = ""
        file = open("./day6/day6Input.txt", "r")
        for line in file.readlines():
            buffer += (re.sub("\n", "", line))
        print(self.janelaFlutuante(buffer))

    def janelaFlutuante(self, dataStream):
        pos = 0
        for i in range(len(dataStream)):
            if (self.janelaChecker(dataStream[i:i+14])):
                return i+14

    def janelaChecker(self, input):
        for i in input:
            if input.count(i) > 1:
                return False
        return True


day6().problema1()
