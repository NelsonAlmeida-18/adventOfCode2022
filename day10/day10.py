import re


class day10:
    def problema1(self):
        file = open("./day10/day10Input.txt", "r")
        interesting = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
        X = 1
        numOfCycles = 0
        # addx v faz dois ciclos e x+=v
        # noop faz um ciclo mas sem efeitos
        for line in file:
            line = re.sub("\n", "", line)
            if line == "noop":
                numOfCycles += 1
                if numOfCycles in interesting:
                    print(numOfCycles, X)
                    interesting[numOfCycles] = numOfCycles*X
                if numOfCycles-1 in interesting:
                    print(numOfCycles-1, X)
                    interesting[numOfCycles-1] = (numOfCycles-1)*X
            else:
                numOfCycles += 2
                if numOfCycles in interesting:
                    print(numOfCycles, X)
                    interesting[numOfCycles] = numOfCycles*X
                if numOfCycles-1 in interesting:
                    print(numOfCycles-1, X)
                    interesting[numOfCycles-1] = (numOfCycles-1)*X
                increments = line.split(" ")[1]
                X += int(increments)

        x = 0
        for i in interesting:
            x += interesting[i]
        print(x)

    def problema2(self):
        crt = self.crtMaker()

        spritePostition = "".join(["." for i in range(40)])
        spritePostition[0] = "#"
        spritePostition[1] = "#"
        spritePostition[2] = "#"

        crtPosition = 0

        file = open("./day10/day10Input.txt")
        for line in file.readlines():
            line = re.sub("\n", "", line)

            if line == "noop":

            else:
                increments = line.split(" ")[1]
                X += int(increments)

    def crtMaker(self):
        width = 40
        height = 6
        crt = ["".join(["." for i in range(width)]) for i in range(height)]
        return crt


day10().problema2()
