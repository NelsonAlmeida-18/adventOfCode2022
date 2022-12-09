import re


class day9:
    def problema1(self):
        file = open("./day9/day9Input.txt")
        mapp = []
        tempBuffer = []
        for line in file.readlines():
            line = re.sub("\n", "", line)
            linha = line.split(" ")
            instruction = linha[0]
            iters = linha[1]


day9().problema1()
