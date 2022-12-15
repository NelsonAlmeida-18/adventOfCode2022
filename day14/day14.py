import re


class day14:

    def problema1(self):
        waterfall = self.drawer()

    def drawer(self):
        file = open("./day14/day14Input.txt", "r")
        file = file.readlines()
        (minx, maxx), (miny, maxy), tabuleiro = self.tabuleiro(file)
        # self.imprimeTabuleiro(tabuleiro)
        self.adicionaRochas(tabuleiro, minx, file)
        pos = 0
        while (True):
            try:
                self.ballDropping(tabuleiro, minx)
                pos += 1
            except:
                print(pos)
                return

    def ballDropping(self, tabuleiro, minx):
        ballDropx, ballDropy = 500-minx, 0
        possibleToMove = True
        while (possibleToMove):
            if tabuleiro[ballDropy+1][ballDropx] == ".":
                ballDropy += 1
            # encontrou sand ou brick
            elif tabuleiro[ballDropy+1][ballDropx] == "#" or tabuleiro[ballDropy+1][ballDropx] == "o":
                # verificar esquerda
                if tabuleiro[ballDropy+1][ballDropx-1] == ".":
                    ballDropx -= 1
                    ballDropy += 1
                elif tabuleiro[ballDropy+1][ballDropx+1] == ".":
                    ballDropx += 1
                    ballDropy += 1

                else:
                    possibleToMove = False
                # verificar direita
            else:
                possibleToMove = False

        tabuleiro[ballDropy][ballDropx] = "o"
        self.imprimeTabuleiro(tabuleiro)

    def adicionaRochas(self, tabuleiro, minx, file):
        for line in file:
            line = re.sub("\n", "", line)
            line = line.split(" -> ")
            pos = 0
            while (pos < len(line)-1):
                srcx, srcy = line[pos].split(",")
                destx, desty = line[pos+1].split(",")
                srcx, srcy, destx, desty = int(srcx), int(
                    srcy), int(destx), int(desty)
                # desenha linha vertical
                if srcx == destx:
                    if srcy > desty:
                        while (srcy >= desty):
                            tabuleiro[desty][srcx-minx] = "#"
                            desty += 1
                    elif srcy < desty:
                        while (srcy <= desty):
                            tabuleiro[srcy][srcx-minx] = "#"
                            srcy += 1

                # desenha linha horizontal
                if srcy == desty:
                    if srcx > destx:
                        while (srcx >= destx):
                            tabuleiro[desty][destx-minx] = "#"
                            destx += 1
                    elif srcx < destx:
                        while (srcx <= destx):
                            tabuleiro[srcy][srcx-minx] = "#"
                            srcx += 1
                pos += 1
            # print(line)
            # self.imprimeTabuleiro(tabuleiro)
            # print("\n")

    def tabuleiro(self, file):
        minx, maxx = 0, 0
        miny, maxy = 0, 0
        for line in file:
            line = re.sub("\n", "", line)
            line = line.split(" -> ")
            for i in line:
                i = i.split(",")
                x = int(i[0])
                y = int(i[1])
                if x < minx or minx == 0:
                    minx = x
                if x > maxx or maxx == 0:
                    maxx = x
                if y < miny or miny == 0:
                    miny = y
                if y > maxy or maxy == 0:
                    maxy = y

        tabuleiro = []
        drawingMaxx = maxx-minx
        drawingMaxy = maxy
        for i in range(drawingMaxy+1):
            tabuleiro.append(["." for j in range(drawingMaxx+1)])

        return (minx, maxx), (miny, maxy), tabuleiro

    def imprimeTabuleiro(self, tabuleiro):
        pos = 0
        for i in tabuleiro:
            if pos < 10:
                print(f"0{pos}: {''.join(i)}")
            else:
                print(f"{pos}: {''.join(i)}")
            pos += 1

    def problema2(self):
        file = open("./day14/day14Input.txt", "r")
        file = file.readlines()
        (minx, maxx), (miny, maxy), tabuleiro = self.tabuleiro(file)
        self.adicionaRochas(tabuleiro, minx, file)
        piso1 = ["." for i in range(maxx-minx+1)]
        piso0 = ["#" for i in range(maxx-minx+1)]
        tabuleiro.append(piso1)
        tabuleiro.append(piso0)
        self.imprimeTabuleiro(tabuleiro)
        pos = 0
        while (tabuleiro[0][500-minx] != "o"):
            try:
                tabuleiro, minx, adicionado = self.ballDropping2(
                    tabuleiro, minx)
                if not adicionado:
                    pos += 1
            except:
                print(pos)
                return
        print(pos)

    def ballDropping2(self, tabuleiro, minx):
        ballDropx, ballDropy = 500-minx, 0
        possibleToMove = True
        while (possibleToMove):

            if ballDropx-1 == 0:
                tabuleiro = self.adicionaEsquerda(tabuleiro)
                minx -= 1
                return tabuleiro, minx, True

            elif ballDropx+1 == len(tabuleiro[0]):
                tabuleiro = self.adicionaDireita(tabuleiro)
                return tabuleiro, minx, True

            elif tabuleiro[ballDropy+1][ballDropx] == ".":
                ballDropy += 1
            # encontrou sand ou brick
            elif tabuleiro[ballDropy+1][ballDropx] == "#" or tabuleiro[ballDropy+1][ballDropx] == "o":
                # verificar esquerda
                if tabuleiro[ballDropy+1][ballDropx-1] == ".":
                    ballDropx -= 1
                    ballDropy += 1
                elif tabuleiro[ballDropy+1][ballDropx+1] == ".":
                    ballDropx += 1
                    ballDropy += 1

                else:
                    possibleToMove = False
                # verificar direita
            else:
                possibleToMove = False

        tabuleiro[ballDropy][ballDropx] = "o"
        return tabuleiro, minx, False

    def adicionaEsquerda(self, tabuleiro):
        newTabuleiro = []
        for i in range(len(tabuleiro)):
            newTabuleiro.append(["."]+tabuleiro[i])
        newTabuleiro[-1] = ["#"]+newTabuleiro[-1][1:]

        # self.imprimeTabuleiro(newTabuleiro)
        return newTabuleiro

    def adicionaDireita(self, tabuleiro):
        newTabuleiro = []
        for i in range(len(tabuleiro)):
            newTabuleiro.append(tabuleiro[i]+["."])
        newTabuleiro[-1] = newTabuleiro[-1][:-1]+["#"]
        # self.imprimeTabuleiro(newTabuleiro)
        return newTabuleiro


print()
day14().problema2()
