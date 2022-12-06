import re


class day5:
    def problema1(self):
        stack, instructions = self.stackMaker()
        stack = self.mover(stack, instructions)
        solution = self.solver(stack)
        print(solution)

    def solver(self, stacks):
        topOfEachStack = ""
        for stack in stacks:
            topOfEachStack += stacks[stack][-1]
        return topOfEachStack

    def mover(self, stack, instructions):
        for instruction in instructions:
            groups = re.findall(r"([0-9]+)", instruction)
            nmbrContainers = int(groups[0])
            srcStack = int(groups[1])-1
            destStack = int(groups[2])-1
            for i in range(1, nmbrContainers+1):
                stack[destStack].append(stack[srcStack][-1])
                stack[srcStack] = stack[srcStack][:len(stack[srcStack])-1]
        return stack

    def stackMaker(self):
        stacks = {}
        file = open("./day5/day5Input.txt")
        instructions = []
        for line in file.readlines():
            if "[" in line or "]" in line:
                stack = 1
                line = re.sub(r"\n", "", line)
                inputSize = 9
                for i in range(inputSize):
                    if i not in stacks:
                        stacks[i] = []
                    if line[stack] != " ":
                        stacks[i].insert(0, line[stack])
                    stack += 4
            if "move" in line:
                instructions.append(line)

        return stacks, instructions

    def mover9001(self, stack, instructions):
        for instruction in instructions:
            groups = re.findall(r"([0-9]+)", instruction)
            nmbrContainers = int(groups[0])
            srcStack = int(groups[1])-1
            destStack = int(groups[2])-1
            cratesToMove = stack[srcStack][len(
                stack[srcStack])-nmbrContainers:]
            stack[destStack] += cratesToMove
            stack[srcStack] = stack[srcStack][:len(
                stack[srcStack])-nmbrContainers]
        return stack

    def problema2(self):
        stack, instructions = self.stackMaker()
        stack = self.mover9001(stack, instructions)
        print(self.solver(stack))


day5().problema2()
