
rules = []
updates = []
with open("2024/day5/input.txt") as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            item = list(map(int, line.strip().split("|")))
            rules.append(item)
        else:
            item = list(map(int, line.strip().split(",")))
            updates.append(item)


def find_mid_index(input_list):
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return input_list[int(middle - 0.5)]
    else:
        return (input_list[int(middle)], input_list[int(middle - 1)])


incorrect = []
count = 0
correct = []
for update in updates:
    valid = True
    for rule in rules:
        if (
            rule[0] in update
            and rule[1] in update
            and update.index(rule[0]) > update.index(rule[1])
        ):
            valid = False
    if valid:
        count += find_mid_index(update)
    else:
        incorrect.append(update)

print(count)


count_incor = 0
new_insrts = []
for it in incorrect:
    for i in range(0, len(it)):
        for j in range(i + 1, len(it)):
            if [it[j], it[i]] in rules:
                err_flag = False
                it[j], it[i] = it[i], it[j]
    count_incor += find_mid_index(it)

print(count_incor)
