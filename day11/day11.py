import re


class day11:

    def problema1(self, rounds):
        harambe = self.listMonke()
        for i in range(rounds):
            for harambi in harambe:
                # inspectEachItem:
                operation = harambe[harambi]["Operation"]
                test = harambe[harambi]["Test"]["Test"]
                for item in harambe[harambi]["Starting Items"]:
                    harambe[harambi]["Inspections"] += 1
                    worryLevelPostOperation = self.parseOperation(
                        item, operation)
                    # monke veri bored level/3
                    worryLevelBored = worryLevelPostOperation//3
                    if self.parseTest(test, worryLevelBored):
                        monkeyToThrow = self.parseAction(
                            harambe[harambi]["Test"]["True"])
                        harambe[monkeyToThrow]["Starting Items"].append(
                            worryLevelBored)
                        harambe[harambi]["Starting Items"] = harambe[harambi]["Starting Items"][1:]
                    else:
                        monkeyToThrow = self.parseAction(
                            harambe[harambi]["Test"]["False"])
                        harambe[monkeyToThrow]["Starting Items"].append(
                            worryLevelBored)
                        harambe[harambi]["Starting Items"] = harambe[harambi]["Starting Items"][1:]

        print(self.top2Harambinos(harambe))

    def top2Harambinos(self, harambe):
        harambeMaster, subHarambeMaster = 0, 0
        for harambino in harambe:
            if (harambe[harambino]["Inspections"] > harambeMaster):
                subHarambeMaster = harambeMaster
                harambeMaster = harambe[harambino]["Inspections"]
            if (harambe[harambino]["Inspections"] < harambeMaster and harambe[harambino]["Inspections"] > subHarambeMaster):
                subHarambeMaster = harambe[harambino]["Inspections"]
        return harambeMaster*subHarambeMaster

    def parseAction(self, instruction):
        whereToThrow = re.search(r"throw to monkey (.+)", instruction)
        return int(whereToThrow.group(1))

    def parseTest(self, test, worryLevel):
        divisible = re.search(r"divisible by (.*)", test)
        return worryLevel % int(divisible.group(1)) == 0

    def parseOperation(self, item, operation):
        multOp = re.search(r".* \* (\-?[0-9]+|old|OLD)", operation)
        divOp = re.search(r".* \/ (\-?[0-9]+|old|OLD)", operation)
        addOp = re.search(r".* \+ (\-?[0-9]+|old|OLD)", operation)
        subtrOp = re.search(r".* \- (\-?[0-9]+|old|OLD)", operation)
        if multOp:
            g = multOp.group(1)
            if g.lower() == "old":
                return item*item
            return item*int(multOp.group(1))
        elif divOp:
            g = divOp.group(1)
            if g.lower() == "old":
                return item/item
            return item/int(divOp.group(1))
        elif addOp:
            g = addOp.group(1)
            if g.lower() == "old":
                return item+item
            return item+int(addOp.group(1))
        elif subtrOp:
            g = subtrOp.group(1)
            if g.lower() == "old":
                return item-item
            return item-int(subtrOp.group(1))

    def listMonke(self):
        file = open("./day11/day11Input.txt", "r")
        listOfMonkes = {}
        currMonke = 0
        for line in file.readlines():
            line = re.sub(r"[\t\n]", "", line)
            monkeDetection = re.search(r"Monkey ([0-9]+)\:", line)
            itemsDetection = re.search(r"Starting items: (.+)", line)
            operationDetected = re.search(r"Operation: (.+)", line)
            testDetected = re.search(r"Test: (.+)", line)
            trueOperationDetected = re.search(r"If true: (.+)", line)
            falseOperationDetected = re.search(r"If false: (.+)", line)
            if monkeDetection:
                currMonke = int(monkeDetection.group(1))
            else:
                if currMonke not in listOfMonkes:
                    listOfMonkes[currMonke] = {"Inspections": 0, "Starting Items": [], "Operation": "", "Test": {
                        "Test": "", "True": "", "False": ""}}
                if itemsDetection:
                    listOfItems = itemsDetection.group(1)
                    listOfItems = listOfItems.split(", ")
                    for item in listOfItems:
                        listOfMonkes[currMonke]["Starting Items"].append(
                            int(item))

                if operationDetected:
                    listOfMonkes[currMonke]["Operation"] = operationDetected.group(
                        1)
                if testDetected:
                    listOfMonkes[currMonke]["Test"]["Test"] = testDetected.group(
                        1)
                if trueOperationDetected:
                    listOfMonkes[currMonke]["Test"]["True"] = trueOperationDetected.group(
                        1)
                if falseOperationDetected:
                    listOfMonkes[currMonke]["Test"]["False"] = falseOperationDetected.group(
                        1)

        return listOfMonkes


day11().problema1(20)
