import re

data = [l.strip() for l in open("2023/data/1.in")]

digits = re.compile("\d+")
symbol = re.compile("[^a-z0-9\.]+")


partnumber = []
j = 0
for x in data:
    partnumbers = re.finditer(digits, x)
    for part in partnumbers:
        start = part.start()
        end = part.end()
        partno = part.group()
        for i in range(start-1, end+1):
            for q in range(-1, 1):
                if j+q >= 0 and j+q <= 10:
                    print(j+q, i, start, end)
                    if re.finditer(symbol, data[j+q][i]):
                        partnumber.append(data[j][start:end])
                        # print(data[j+q][i])
    j += 1
    print(partnumber)
