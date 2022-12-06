

class day1:
    def problema1(self):
        elvesList = {}
        file = open("./day1/day1Input.txt", "r")
        elve = 0
        for line in file.readlines():
            if line != "\n":
                if elve not in elvesList:
                    elvesList[elve] = 0
                elvesList[elve] += int(line)
            else:
                elve += 1

        print(max(elvesList.values()))

    def problema2(self):
        elvesList = {}
        file = open("./day1/day1Input.txt", "r")
        elve = 0
        for line in file.readlines():
            if line != "\n":
                if elve not in elvesList:
                    elvesList[elve] = 0
                elvesList[elve] += int(line)
            else:
                elve += 1

        top3 = self.top3(elvesList)
        print(sum(top3))

    def top3(self, elvesList):
        dic_sorted = sorted(
            elvesList.items(), key=lambda item: item[1], reverse=True)
        return dic_sorted[0][1], dic_sorted[1][1], dic_sorted[2][1]


day1().problema1()
