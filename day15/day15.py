import re
import math


class day15:
    def problema1(self):
        board, sensorsAndBeacons, minx = self.drawer()
        for sensor in sensorsAndBeacons:
            self.povoaTabuleiro(board, sensorsAndBeacons[sensor][0], minx)

        for sensor in sensorsAndBeacons:
            self.desenhaRaios(
                board, sensorsAndBeacons[sensor][0], sensorsAndBeacons[sensor][1], minx)

           # self.imprimeTabuleiro(board)

    def desenhaRaios(self, tabuleiro, sensorAndBeacon, distance, minx):
        width, height = distance
        sensor, beacon = sensorAndBeacon
        xSensor, ySensor = sensor
        xBeacon, yBeacon = beacon
        xSensor += abs(minx)
        xBeacon += abs(minx)
        escreve = 1
        espacos = int((width+height)/2)
        for y1 in range(espacos):
            for x1 in range(escreve):
                tabuleiro[y1][espacos+x1] = "#"
            espacos -= 1
            escreve += 2

        escreve = width+height-1
        espacos = 1
        for y1 in range(4):
            for x1 in range(escreve):
                tabuleiro[4+y1][espacos+x1] = "#"
            espacos += 1
            escreve -= 2

        self.imprimeTabuleiro(tabuleiro)

    def povoaTabuleiro(self, tabuleiro, sensorAndBeacon, minx):
        sensor, beacon = sensorAndBeacon
        xSensor, ySensor = sensor
        xBeacon, yBeacon = beacon
        xSensor += abs(minx)
        xBeacon += abs(minx)
        tabuleiro[ySensor][xSensor] = "S"
        tabuleiro[yBeacon][xBeacon] = "B"

    def radius(self, coords):
        sensor, beacon = coords
        xSensor, ySensor = sensor
        xBeacon, yBeacon = beacon
        width = abs(xSensor-xBeacon)
        height = abs(ySensor-yBeacon)
        return (width, height)

    # steps:
    # criar mapa
    # funcao de radius com distancia ate ao beacon mais proximo
    def drawer(self):
        file = open("./day15/day15Input.txt", "r")
        file = file.readlines()
        minx, maxx, miny, maxy, pos = 0, 0, 0, 0, 0
        sensorsAndBeacons = {}
        for line in file:
            regex = re.search(
                r"Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)", line)
            if regex:
                sensorx, sensory, beaconx, beacony = int(regex.group(
                    1)), int(regex.group(2)), int(regex.group(3)), int(regex.group(4))
                sensorsAndBeacons[pos] = (
                    ((sensorx, sensory), (beaconx, beacony)), self.radius(((sensorx, sensory), (beaconx, beacony))))
                maxxLine = max(beaconx, sensorx)
                minxLine = min(beaconx, sensorx)
                maxyLine = max(beacony, sensory)
                minyLine = min(beacony, sensory)
                if maxxLine > maxx:
                    maxx = maxxLine
                if minxLine < minx:
                    minx = minxLine
                if maxyLine > maxy:
                    maxy = maxyLine
                if minyLine < miny:
                    miny = minyLine

                pos += 1

        board = []
        for i in range(miny, maxy+1):
            board.append(["." for i in range(abs(maxx)+abs(minx)+1)])

        return board, sensorsAndBeacons, minx

    def imprimeTabuleiro(self, tabuleiro):
        pos = 0
        for i in tabuleiro:
            if pos < 10:
                print(f"0{pos}: {''.join(i)}")
            else:
                print(f"{pos}: {''.join(i)}")
            pos += 1


day15().problema1()
