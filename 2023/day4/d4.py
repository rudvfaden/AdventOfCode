with open("2023/day4/input.txt", "r") as input:
	data = input.readlines()


data1=[r.strip().split(':')[1].split('|') for r in data]

wins=[set(a[0].split()) for a in data1]
mywins=[set(a[1].split()) for a in data1]

totPoint=0
for n, val in enumerate(wins):
	test=wins[n].intersection(mywins[n])
	if len(test)>0:
		totPoint+=2**(len(test)-1)

print(totPoint)