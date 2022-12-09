import re


class day7:

    def problema1(self):
        file = open("./day7/day7Input.txt", "r")
        inputBuffer = []
        for line in file.readlines():
            inputBuffer.append(re.sub("\n", "", line))

        dirHierarchy = self.dirHierarchy(inputBuffer)
        dirTree = self.dirTree(inputBuffer)
        print(dirHierarchy)

    def dirHierarchy(self, inputBuffer):
        dirHierarchy = {}
        currParentDir = "/"
        dirBuffer = []
        pos = 0
        while (pos < len(inputBuffer)):
            line = inputBuffer[pos]
            changeDirRegex = re.search(r".* cd (.*)", line)
            dirInfoRegex = re.search(r"dir (.*)", line)
            fileInfoRegex = re.search(r"^[0-9]+ [a-zA-Z0-9]+", line)
            listDirRegex = re.search(r".* ls", line)
            if (changeDirRegex):
                nextDir = changeDirRegex.group(1)
                if (nextDir == ".."):
                    dirBuffer = dirBuffer[:len(dirBuffer)-1]
                else:
                    currParentDir = nextDir
                    dirHierarchy[currParentDir] = []
                    dirBuffer.append(nextDir)
            if (listDirRegex):
                pos += 1
                line = inputBuffer[pos]
                dirInfoRegex = re.search(r"dir (.*)", line)
                fileInfoRegex = re.search(r"^[0-9]+ [a-zA-Z0-9]+", line)
                while (pos < len(inputBuffer)-1 and (dirInfoRegex or fileInfoRegex)):
                    if (dirInfoRegex and dirInfoRegex.group(1) not in dirHierarchy[currParentDir]):
                        dirHierarchy[currParentDir].append(
                            dirInfoRegex.group(1))
                    pos += 1
                    line = inputBuffer[pos]
                    dirInfoRegex = re.search(r"dir (.*)", line)
                    fileInfoRegex = re.search(r"^[0-9]+ [a-zA-Z0-9]+", line)

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
