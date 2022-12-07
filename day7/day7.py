import re


class day7:

    def problema1(self):
        file = open("./day7/day7Input.txt", "r")
        inputBuffer = []
        for line in file.readlines():
            inputBuffer.append(re.sub("\n", "", line))

        dirHierarchy = self.dirHierarchy(inputBuffer)
        dirTree = self.dirTree(inputBuffer)
        print(self.atMost100000(dirHierarchy, dirTree))
        print(dirHierarchy)
        # print(dirTree)

    def atMost100000(self, dirHierarchy, dirTree):
        sizeAtMost100000 = 0

        # pastas com subpastas e subpastas
        for dir in dirHierarchy:
            subDirs = dirHierarchy[dir]
            tempSize = 0
            subDirsSize = 0
            for subDir in subDirs:
                tempSize += dirTree[subDir]
                if dirTree[subDir] <= 100000:
                    subDirsSize += dirTree[subDir]

            tempSize += dirTree[dir]
            sizeAtMost100000 += subDirsSize
            if (tempSize <= 100000):
                sizeAtMost100000 += tempSize
        return sizeAtMost100000

    def dirHierarchy(self, inputBuffer):
        dirHierarchy = {}
        currParentDir = ""
        pos = 0
        while (pos < len(inputBuffer)):
            line = inputBuffer[pos]
            changeDirRegex = re.search(r".* cd (.*)", line)
            dirInfoRegex = re.search(r"dir (.*)", line)
            if (changeDirRegex):
                newDir = changeDirRegex.group(1)
                if newDir != "/" and newDir != "..":
                    if newDir not in dirHierarchy:
                        flag = 1
                        for key in dirHierarchy:
                            if currParentDir in dirHierarchy[key]:
                                flag = 0
                        if flag == 1:
                            currParentDir = newDir
                            dirHierarchy[currParentDir] = []
            if dirInfoRegex and currParentDir != "":
                dirHierarchy[currParentDir].append(dirInfoRegex.group(1))

            pos += 1
        return dirHierarchy

    def dirTree(self, inputBuffer):
        pos = 0
        currDirSize = 0
        currDir = ""
        dirs = {}
        while (pos < len(inputBuffer)):
            line = inputBuffer[pos]
            commandRegex = re.search(r"$", line)
            fileInfoRegex = re.search(r"([0-9]+) [a-zA-Z0-9]+", line)
            if fileInfoRegex:
                currDirSize += int(fileInfoRegex.group(1))
            if commandRegex:
                changeDirRegex = re.search(r".* cd (.*)", line)
                if changeDirRegex and changeDirRegex.group(1) != "..":
                    if currDir != "":
                        dirs[currDir] = currDirSize
                    currDirSize = 0
                    currDir = changeDirRegex.group(1)
            pos += 1
        dirs[currDir] = currDirSize
        return dirs


day7().problema1()
