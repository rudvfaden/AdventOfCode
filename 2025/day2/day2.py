with open("2025/day2/input.txt", 'r') as file:
    for line in file:
        ranges = line.split(',')



# rranges = [num.split('-') for num in ranges]
# r = [list(map(int, sublist)) for sublist in rranges]

# for i in range(r[0][0], r[0][1]+1):
#         if has_repeated_digits(i):
#             print(i)

print(has_repeated_digits(1188511885))