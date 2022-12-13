import re


class day9:
    def problema1(self):
        map = self.drawer()
        print(map)

    def drawer(self):
        file = open("./day9/day9Input.txt")
        headPos = (0, 0)
        tailPos = (0, 0)
        visited = []
        for line in file.readlines():
            line = re.sub("\n", "", line)
            linha = line.split(" ")
            instruction = linha[0]
            iters = int(linha[1])
            while (iters > 0):
                if tailPos not in visited:
                    visited.append(tailPos)
                headPos = self.moveHead(headPos, instruction)
                tailPos = self.moveTail(headPos, tailPos)
                iters -= 1

        print(len(visited))
        return visited

    def moveHead(self, headPos, instruction):
        xHead, yHead = headPos
        if instruction == "R":
            return (xHead+1, yHead)
        if instruction == "L":
            return (xHead-1, yHead)
        if instruction == "U":
            return (xHead, yHead+1)
        if instruction == "D":
            return (xHead, yHead-1)

    def moveTail(self, headPos, tailPos):
        xHead, yHead = headPos
        xTail, yTail = tailPos

        if (headPos == tailPos):
            return tailPos

        if (yHead == yTail+2 and xHead == xTail+1):
            return (xTail+1, yTail+1)

        if (yHead == yTail+2 and xHead == xTail-1):
            return (xTail+1, yTail-1)

        if (yHead == yTail+1 and xHead == xTail+2):
            return (xTail+1, yTail+1)

        if (yHead == yTail-1 and xHead == xTail+2):
            return (xTail-1, yTail+1)

        if (xHead == xTail+2):
            xTail += 1

        if (xHead == xTail-2):
            xTail -= 1

        if (yHead == yTail+2):
            yTail += 1

        if (yHead == yTail-2):
            yTail -= 1

        return (xTail, yTail)


day9().problema1()
