import re


class day2:
    def __init__(self):
        self.problema2()

    def game(self):
        score = 0
        file = open("./day2/day2Input.txt", "r")
        for line in file.readlines():
            hint = line.split(" ")
            player1Play = hint[0]
            player2Play = hint[1]

            score += self.play(player2Play, player1Play)
        print(score)

    def play(self, player1Play, player2Play):
        player1Play = re.sub("\n", "", player1Play)
        bonusScore = {"X": 1, "Y": 2, "Z": 3}
        score = bonusScore[player1Play]

        if (player2Play == "A" and player1Play == "X"):
            score += 3
        if (player2Play == "A" and player1Play == "Y"):
            score += 6
        if (player2Play == "A" and player1Play == "Z"):
            score += 0

        if (player2Play == "B" and player1Play == "X"):
            score += 0
        if (player2Play == "B" and player1Play == "Y"):
            score += 3
        if (player2Play == "B" and player1Play == "Z"):
            score += 6

        if (player2Play == "C" and player1Play == "X"):
            score += 6
        if (player2Play == "C" and player1Play == "Y"):
            score += 0
        if (player2Play == "C" and player1Play == "Z"):
            score += 3

        return score

    def problema2(self):
        file = open("./day2/day2Input.txt", "r")
        score = 0
        for line in file.readlines():
            hint = line.split(" ")
            oponentPlay = hint[0]
            result = hint[1]
            result = re.sub("\n", "", result)
            score += self.chooseYourCharacter(oponentPlay, result)
        print(score)

    def chooseYourCharacter(self, oponentPlay, result):
        score = 0
        rock = "A"
        paper = "B"
        scissor = "C"
        lose = "X"
        draw = "Y"
        win = "Z"
        myPlay = ""
        values = {"X": 1, "Y": 2, "Z": 3}
        if (win == result):
            score += 6
            if (oponentPlay == rock):
                myPlay = "Y"
            if (oponentPlay == paper):
                myPlay = "Z"
            if (oponentPlay == scissor):
                myPlay = "X"
        if (lose == result):
            score += 0
            if (oponentPlay == rock):
                myPlay = "Z"
            if (oponentPlay == scissor):
                myPlay = "Y"
            if (oponentPlay == paper):
                myPlay = "X"

        if (draw == result):
            score += 3
            if (oponentPlay == rock):
                myPlay = "X"
            if (oponentPlay == paper):
                myPlay = "Y"
            if (oponentPlay == scissor):
                myPlay = "Z"

        score += values[myPlay]
        return score


day2()
