import re


class day12:

    def grafo(self, NV):
        grafo = {}
        for i in range(NV):
            grafo[i] = {}
        return grafo

    def problema1(self):
        self.createGraph()

    def createGraph(self):
        file = open("./day12/day12Input.txt", "r")
        matriz = []
        for line in file.readlines():
            matriz.append(re.sub("\n", "", line))
        print(matriz)


day12().problema1()
