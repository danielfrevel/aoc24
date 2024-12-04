
from utils import inputsAsList

rawInput = inputsAsList(4)

inputMatrix = list(map(lambda i: list(i),  rawInput))

order = ["M", "A", "S"]


def checkRight(row, col):
    if col + 3 >= len(inputMatrix[0]):
        return False
    for i in range(0, 3):
        if not inputMatrix[row][col + i + 1] == order[i]:
            return False
    return True


def checkLeft(row, col):
    if col - 3 < 0:
        return False
    for i in range(0, 3):
        if not inputMatrix[row][col - i - 1] == order[i]:
            return False
    return True


def checkTop(row, col):
    if row - 3 < 0:
        return False
    for i in range(0, 3):
        if not inputMatrix[row - i - 1][col] == order[i]:
            return False
    return True


def checkBottom(row, col):
    if row + 3 >= len(inputMatrix):
        return False
    for i in range(0, 3):
        if not inputMatrix[row + i + 1][col] == order[i]:
            return False
    return True


def checkTopRight(row, col):
    if row - 3 < 0 or col + 3 >= len(inputMatrix[0]):
        return False
    for i in range(0, 3):
        if not inputMatrix[row - i - 1][col + i + 1] == order[i]:
            return False
    return True


def checkTopLeft(row, col):
    if row - 3 < 0 or col - 3 < 0:
        return False
    for i in range(0, 3):
        if not inputMatrix[row - i - 1][col - i - 1] == order[i]:
            return False
    return True


def checkBottomRight(row, col):
    if row + 3 >= len(inputMatrix) or col + 3 >= len(inputMatrix[0]):
        return False
    for i in range(0, 3):
        if not inputMatrix[row + i + 1][col + i + 1] == order[i]:
            return False
    return True


def checkBottomLeft(row, col):
    if row + 3 >= len(inputMatrix) or col - 3 < 0:
        return False
    for i in range(0, 3):
        if not inputMatrix[row + i + 1][col - i - 1] == order[i]:
            return False
    return True


def first(inputMatrix):
    count = 0
    for rowIndex, rows in enumerate(inputMatrix):
        for colIndex, letter in enumerate(rows):
            if letter == "X":
                count += [
                    checkRight(rowIndex, colIndex),
                    checkLeft(rowIndex, colIndex),
                    checkTop(rowIndex, colIndex),
                    checkBottom(rowIndex, colIndex),
                    checkTopRight(rowIndex, colIndex),
                    checkTopLeft(rowIndex, colIndex),
                    checkBottomRight(rowIndex, colIndex),
                    checkBottomLeft(rowIndex, colIndex)
                ].count(True)

    print(count)


# first(inputMatrix)

count = 0
for rowIndex, rows in enumerate(inputMatrix):
    for colIndex, letter in enumerate(rows):

        def check(row, col):
            if row - 1 < 0 or row + 1 >= len(inputMatrix) or col - 1 < 0 or col + 1 >= len(inputMatrix[0]):
                return False

            topLeft = inputMatrix[row - 1][col - 1]
            bottomRight = inputMatrix[row + 1][col + 1]
            topRight = inputMatrix[row - 1][col + 1]
            bottomLeft = inputMatrix[row + 1][col - 1]

            ms = [topLeft, bottomRight, topRight, bottomLeft].count("M") == 2
            ss = [topLeft, bottomRight, topRight, bottomLeft].count("S") == 2

            if not (ms and ss):
                return False

            if topLeft == "M" and bottomRight == "S" and topRight == "S" and bottomLeft == "M":
                return True

            if topLeft == "S" and bottomRight == "M" and topRight == "M" and bottomLeft == "S":
                return True

            if bottomRight == "S" and topRight == "M" and topRight == "M" and bottomLeft == "S":
                return True

            if bottomRight == "M" and topRight == "S" and topRight == "S" and bottomLeft == "M":
                return True

            return False

        if letter == 'A' and check(rowIndex, colIndex):
            count += 1


print(count)
