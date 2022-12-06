

class day1:
    def problema1(self):
        elvesList = {}
        file = open("./day1/day1Input.txt", "r")
        elve = 0
        maxCals = [(0, 0), (0, 0), (0, 0)]
        for line in file.readlines():
            if line != "\n":
                if elve not in elvesList:
                    elvesList[elve] = 0
                elvesList[elve] += int(line)
            else:
                calsElve = elvesList[elve]
                if calsElve > maxCals[0][0]:
                    maxCals[0] = (calsElve, elve)
                if calsElve < maxCals[0][0] and calsElve > maxCals[1][0]:
                    maxCals[1] = (calsElve, elve)
                if calsElve < maxCals[0][0] and calsElve < maxCals[1][0] and calsElve > maxCals[2][0]:
                    maxCals[2] = (calsElve, elve)
                elve += 1
        print(maxCals)


day1().problema1()
