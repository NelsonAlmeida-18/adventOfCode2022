import re


class day13:
    def problema1(self):
        pairs = self.pairMaker()
        for pair in pairs:
            self.pairInner(pairs[pair])

    def pairMaker(self):
        file = open("./day13/day13Input.txt", "r")
        pairs = {}
        pairPos = 0
        for line in file:
            if pairPos not in pairs:
                pairs[pairPos] = []
            if line == "\n":
                pairPos += 1
            else:
                pairs[pairPos].append(re.sub("\n", "", line))
        return pairs

    def pairInner(self, pair):
        pair1 = pair[0]
        pair2 = pair[1]
        self.pairParser(pair1)

    def pairParser(self, pair):
        pairParsed = []
        pair = re.search(r"\[(.*)\]$", pair).group(1)
        if "[" in pair:
            pairSplitted = []
            buffer = ""
            numOfAbreParen = 0

            print(pairSplitted)
        else:
            pair = pair.split(",")
            for i in pair:
                pairParsed.append(i)


day13().problema1()
