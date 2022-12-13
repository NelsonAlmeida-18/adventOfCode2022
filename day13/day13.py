import re


class day13:
    def problema1(self):
        pairs = self.pairMaker()
        for pair in pairs:
            print(pairs[pair][0], pairs[pair][1])

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
                pairs[pairPos].append(self.pairInner(line))
        return pairs

    def pairInner(self, line):
        line = re.sub("\n", "", line)
        pair = []
        openBrackets = re.search(r"\[(.*)\]$", line)
        if openBrackets:
            line = openBrackets.group(1)
            test = re.split(r"(.*\])\,", line)
            for i in test:
                openBrackets = re.search(r"\[(.+)\]$", i)
                if openBrackets:
                    pair.append(self.pairInner(i))
                else:
                    items = i.split(",")
                    for item in items:
                        if item != "" and item != "[]":
                            pair.append(int(item))
                        if item == "[]":
                            pair.append([])
        return pair


day13().problema1()
