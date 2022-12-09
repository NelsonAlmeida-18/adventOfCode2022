import re


class day8:
    def problema1(self):
        garden = self.gardenMaker()
        # since all trees from the border can be seen we start as pos 1,1
        sizeOfGarden, numOfTrees = len(garden), len(garden[0])
        visibleTrees = 0
        for row in range(1, sizeOfGarden-1):
            for pos in range(1, numOfTrees-1):
                if self.visible(garden, sizeOfGarden, numOfTrees, (row, pos)):
                    visibleTrees += 1

        print(visibleTrees+sizeOfGarden*2+numOfTrees*2-4)

    def gardenMaker(self):
        file = open("./day8/day8Input.txt", "r")
        garden = []
        rowOfTrees = []
        for line in file:
            line = re.sub("\n", "", line)
            for i in line:
                rowOfTrees.append(int(i))
            garden.append(rowOfTrees)
            rowOfTrees = []
        return garden

    def visible(self, garden, sizeOfGarden, numOfTrees, pos):
        x, y = pos
        hightOfTree = garden[x][y]
        # check if visible from left
        visible = True
        for x1 in range(0, x):
            if garden[x1][y] >= hightOfTree:
                visible = False

        if visible:
            return True

        # check if visible from right
        visible = True
        for x1 in range(x+1, numOfTrees):
            if garden[x1][y] >= hightOfTree:
                visible = False

        if visible:
            return True

        # check if visible from top
        visible = True
        for y1 in range(0, y):
            if garden[x][y1] >= hightOfTree:
                visible = False

        if visible:
            return True

        # check if visible from bottom
        visible = True
        for y1 in range(y+1, sizeOfGarden):
            if garden[x][y1] >= hightOfTree:
                visible = False

        if visible:
            return True

        return False

    def problema2(self):
        garden = self.gardenMaker()
        sizeOfGarden, numOfTrees = len(garden), len(garden[0])
        scenicScore = 0
        for linha in range(1, numOfTrees-1):
            for coluna in range(1, sizeOfGarden-1):
                tempScenicScore = self.scenicScore(
                    garden, sizeOfGarden, numOfTrees, (linha, coluna))
                if tempScenicScore > scenicScore:
                    scenicScore = tempScenicScore

        print(scenicScore)

    def scenicScore(self, garden, sizeOfGarden, numOfTrees, pos):
        linha, coluna = pos
        tamanhoArvore = garden[linha][coluna]
        arvoresAcima = [garden[i][coluna] for i in range(linha-1, -1, -1)]
        arvoresAbaixo = [garden[i][coluna]
                         for i in range(linha+1, numOfTrees)]
        arvoresEsquerda = [garden[linha][i] for i in range(coluna-1, -1, -1)]
        arvoresDireita = [garden[linha][i]
                          for i in range(coluna+1, sizeOfGarden)]
        arvoresVisiveisAcima = self.visible(tamanhoArvore, arvoresAcima)
        arvoresVisiveisAbaixo = self.visible(tamanhoArvore, arvoresAbaixo)
        arvoresVisiveisEsquerda = self.visible(tamanhoArvore, arvoresEsquerda)
        arvoresVisiveisDireita = self.visible(tamanhoArvore, arvoresDireita)
        return arvoresVisiveisAcima*arvoresVisiveisAbaixo*arvoresVisiveisDireita*arvoresVisiveisEsquerda

    def visible(self, treeSize, treesNextTo):
        visibleTrees = 0
        for i in treesNextTo:
            if i < treeSize:
                visibleTrees += 1
            else:
                visibleTrees += 1
                break
        return visibleTrees


day8().problema2()
