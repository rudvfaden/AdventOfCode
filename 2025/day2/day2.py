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
            return True  
        
def is_repeated_pattern(s):
    n = len(s)
    for pattern_len in range(1, n // 2 + 1):
        pattern = s[:pattern_len]
        if pattern * (n // pattern_len) == s:
            return True
    return False


total = 0
total2 = 0
rranges = [num.split('-') for num in ranges]
r = [list(map(int, sublist)) for sublist in rranges]


for rr in rranges:
    for i in range(int(rr[0]), int(rr[1])+1):
            if repated_number(i):
                total += i
            if is_repeated_pattern(str(i)):
                total2 += i
            #print(i,is_repeated_pattern(str(i)))

print(total, total2)