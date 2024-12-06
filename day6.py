from utils import inputsAsList


def findGuardIndex(inputMatrix):
    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            if inputMatrix[i][j] in ['^', 'v', '<', '>']:
                return i, j


def part1(inputMatrix):
    inputMatrix = [list(row) for row in inputMatrix]
    guardRow, guardCol = findGuardIndex(inputMatrix)
    nextBlock = inputMatrix[guardRow-1][guardCol]
    direction = '^'

    while True:
        if nextBlock == '#':
            if direction == '^':
                direction = '>'
            elif direction == '>':
                direction = 'v'
            elif direction == 'v':
                direction = '<'
            elif direction == '<':
                direction = '^'
        else:
            if direction == '^':
                guardRow -= 1
            elif direction == 'v':
                guardRow += 1
            elif direction == '<':
                guardCol -= 1
            elif direction == '>':
                guardCol += 1

        inputMatrix[guardRow][guardCol] = "X"

        if direction == '^':
            if guardRow - 1 < 0:
                break
            nextBlock = inputMatrix[guardRow - 1][guardCol]
        elif direction == 'v':
            if guardRow + 1 >= len(inputMatrix):
                break
            nextBlock = inputMatrix[guardRow + 1][guardCol]
        elif direction == '<':
            if guardCol - 1 < 0:
                break
            nextBlock = inputMatrix[guardRow][guardCol - 1]
        elif direction == '>':
            if guardCol + 1 >= len(inputMatrix[0]):
                break
            nextBlock = inputMatrix[guardRow][guardCol + 1]

    moveCount = 0

    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            if inputMatrix[i][j] == 'X':
                moveCount += 1

    print(moveCount + 1)  # +1 weil startPosition nicht mitgezählt wird


part1(inputsAsList(6))


def findLoop(startRow, startCol, nextRow, nextCol, grid):
    rowCount = len(grid)
    colCount = len(grid[0])
    currRow, currCol = startRow, startCol
    visited = set()

    while True:
        visited.add((currRow, currCol, nextRow, nextCol))

        if currRow + nextRow < 0 or currRow + nextRow >= rowCount or currCol + nextCol < 0 or currCol + nextCol >= colCount:
            break

        nextBlock = grid[currRow + nextRow][currCol + nextCol]
        if nextBlock == "#":
            nextRow, nextCol = nextCol, -nextRow
        else:
            currRow += nextRow
            currCol += nextCol

        if (currRow, currCol, nextRow, nextCol) in visited:
            return True


def partTwo(dataInput):
    total = 0
    grid = [list(row) for row in dataInput]

    startRow, startCol = findGuardIndex(grid)

    nextRow, nextCol = -1, 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                continue
            grid[row][col] = "#"
            if findLoop(startRow, startCol, nextRow, nextCol, grid):
                total += 1
            grid[row][col] = "."

    return total


print(partTwo(inputsAsList(6)))
