from utils import inputsAsList
import functools


input = inputsAsList(2)
inputs = []
for i in input:
    moin = list(map(int, i.split(" ")))
    inputs.append(moin)


def check_all_decreasing(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i] <= input_list[i + 1]:

            return False, i
    return True, -1


def check_all_increasing(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i] >= input_list[i + 1]:

            return False, i
    return True, -1


def check_second_rule(input_list):
    for i in range(len(input_list) - 1):
        if abs(input_list[i] - input_list[i + 1]) > 3:
            return False, i
    return True, -1


ctr = 0
for inputList in inputs:

    # inputListWithoutIndex = inputList[:index] + inputList[index + 1:]
    allDecreasing, index = check_all_decreasing(inputList)
    allIncreasing, hs = check_all_increasing(inputList)

    firstRule = allDecreasing or allIncreasing
    if not allDecreasing or allIncreasing:
        continue

    secondRule, hs2 = check_second_rule(inputList)

    if (firstRule and secondRule):
        ctr += 1

print(ctr)


ctr = 0

for inputList in inputs:
    # wenn nicht all decreasing oder all increasing dann eins removen und nochmal checken
    # gleiches nochmal aber das erste failende element ignorieren und nochmal checken
    # repeat bis alle regel erfüllt ist oder ende der liste erreicht
    firstRule = check_all_increasing(inputList)[0] or check_all_decreasing(
        inputList)[0]
    secondRule, hs2 = check_second_rule(inputList)

    for i in range(len(inputList)):
        listWithoutRemoveIndex = inputList[:i] + \
            inputList[i + 1:]

        allDecreasing, j = check_all_decreasing(listWithoutRemoveIndex)
        allIncreasing, hs = check_all_increasing(listWithoutRemoveIndex)

        firstRule = allDecreasing or allIncreasing

        listWithoutRemoveIndex = inputList[:i] + inputList[i + 1:]
        secondRule, hs2 = check_second_rule(listWithoutRemoveIndex)

        if firstRule and secondRule:
            ctr += 1
            break

print(ctr)
