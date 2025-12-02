with open("2025/day2/input.txt", 'r') as file:
    for line in file:
        ranges = line.split(',')

def find_middle(lst):
    mid_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return lst[mid_index - 1:mid_index + 1]
    else:
        return lst[mid_index]
    
def repated_number(n):
    s = str(n)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
        if left == right:
            return int(s)    
        
def repated_number_general(n):
    s = str(n)
    for k in range(2, find_middle(s)+1):
        substr = s[:k]
        mid = substr // 2
        left = substr[:-mid]
        right = substr[mid:]
        if left == right:
            return int(s[-k:])


total = 0
rranges = [num.split('-') for num in ranges]
r = [list(map(int, sublist)) for sublist in rranges]

for rr in rranges:
    for i in range(int(rr[0]), int(rr[1])+1):
            if repated_number(i):
                total += repated_number(i)

print(total)