

from utils import inputAsString

input = inputAsString(1)


def split_data(data_string):
    lines = data_string.strip().split('\n')

    left_side = []
    right_side = []

    for line in lines:
        left, right = map(int, line.split())
        left_side.append(left)
        right_side.append(right)

    return left_side, right_side


l, r = split_data(input)

l.sort()
r.sort()

ctr = 0
for i in range(len(l)):
    ctr += abs(l[i] - r[i])

print(ctr)

lctr = {}
for num in r:
    lctr[num] = lctr.get(num, 0) + 1

nuck = 0
for num in l:
    occurrences = lctr.get(num, 0)

    nuck += num * occurrences

print(nuck)
