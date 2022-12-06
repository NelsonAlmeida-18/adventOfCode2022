

class day3:
    def problema1(self):
        priority = {}
        file = open("./day3/day3Input.txt", "r")
        for line in file.readlines():
            tamanho = len(line)
            itemSize = int(tamanho/2)
            fstItem = line[:itemSize]
            sndItem = line[itemSize:]
            for i in fstItem:
                if i in sndItem:
                    if (i not in priority):
                        priority[i] = 0
                    priority[i] += self.priorityValue(i)
                    break
        print(sum(priority[x] for x in priority))

    def priorityValue(self, i):
        if (i.isupper()):
            return ord(i)-65+27
        if (i.islower()):
            return ord(i)-97+1

    def problema2(self):
        priority = {}
        file = open("./day3/day3Input.txt", "r")
        q = {}
        tempq = []
        pos = 0
        for line in file.readlines():
            tempq.append(line)
            pos += 1
            if (pos % 3 == 0):
                q[int(pos/3)] = tempq
                tempq = []

        for elveGroup in q:
            elve1 = q[elveGroup][0]
            elve2 = q[elveGroup][1]
            elve3 = q[elveGroup][2]
            for i in elve1:
                if (i in elve2 and i in elve3 and i != "\n"):
                    if i not in priority:
                        priority[i] = 0
                    priority[i] += self.priorityValue(i)
                    break
        print(sum(priority[x] for x in priority))


day3().problema2()
