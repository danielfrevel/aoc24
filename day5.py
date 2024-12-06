def ordern(update, rules):
    count = 0
    for i in range(len(update)):
        if i + 1 < len(update) and f"{update[i]}|{update[i+1]}" in rules:
            count += 1
    if count == len(update) - 1:
        return True
    return False


def fixne(update, rules):
    n = len(update)
    while not ordern(update, rules):
        for i in range(n - 1):
            if f"{update[i]}|{update[i+1]}" not in rules:
                update[i], update[i+1] = update[i+1], update[i]
        fixne(update, rules)
    return update


def eins(rules, updates) -> int:
    sum = 0
    for update in updates:
        if ordern(update, rules):
            sum += int(update[len(update)//2])
    return sum


def zwo(rules: list, updates: list) -> int:
    sum = 0
    for update in updates:
        if not ordern(update, rules):
            update2 = fixne(update, rules)
            sum += int(update2[len(update)//2])
    return sum


rules = []
updates = []
with open("./inputs/day5.txt", "r") as file:
    rules, updates = file.read().split('\n\n')

rules = rules.strip().split()
updates = [update.split(',') for update in updates.strip().split()]

rules, updates = input()
print(eins(rules, updates))
print(zwo(rules, updates))
