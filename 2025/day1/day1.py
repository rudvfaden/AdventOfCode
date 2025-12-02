dail = tuple(range(0, 100))

combination = []
with open("2025/day1/input.txt") as f:
    for line in f:
        combination.append(line.strip())

turn = 50
number_zero = 0
number_crossed_zero = 0


for comb in combination:
    if comb.startswith("L"):
        move = -int(comb[1:])
    elif comb.startswith("R"):
        move = int(comb[1:])
    else:
        continue

    # Tæl hvor mange gange vi krydser 0
    if move < 0:  # Drej moed ventre
        # tjek om vi krydser 0 mellem turn og (turn - move)
        steps = abs(move)
        for i in range(1, steps + 1):
            pos = (turn - i) % len(dail)
            if pos == 0:
                number_crossed_zero += 1
    else:  # drej mod højre
        # tjek om vi krydser 0 mellem turn og (turn + move)
        steps = move
        for i in range(1, steps + 1):
            pos = (turn + i) % len(dail)
            if pos == 0:
                number_crossed_zero += 1

    pos = (turn + move) % len(dail)
    turn = dail[pos]
    if turn == 0:
        number_zero += 1

print(number_zero, number_crossed_zero)
