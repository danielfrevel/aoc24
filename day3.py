from utils import inputAsString
import re


def part1():
    input = inputAsString(3)

    input = input.replace(" ", "").replace("\n", "").replace("\t", "")

    regex = "mul\(\d+,\d+\)"

    res = re.findall(regex, input)

    resres = 0
    for i in res:
        i = i.replace("mul", "")
        i = i.replace("(", "").replace(")", "")
        x, y = i.split(",")
        resres += int(x) * int(y)

    print(resres)


def part2():
    input = inputAsString(3)

    input = input.replace(" ", "").replace("\n", "").replace("\t", "")

    regex = "mul\(\d+,\d+\)|do\(\)|don't\(\)"

    res = re.findall(regex, input)

    doit = True
    resres = 0
    for i in res:
        if i == "do()":
            doit = True

        elif i == "don't()":
            doit = False

        else:
            if doit:
                i = i.replace("mul", "")
                i = i.replace("(", "").replace(")", "")
                x, y = i.split(",")
                resres += int(x) * int(y)

    print(resres)


part1()
part2()
