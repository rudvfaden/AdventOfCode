def order(numbers: list) -> bool:
    if len(numbers) < 2:
        return True

    # Determine if the sequence is increasing or decreasing
    increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    return increasing or decreasing

def distinance(numbers: list) -> bool:
    dist=True
    for i in range(1, len(numbers)):
        if not(0 < abs(numbers[i] - numbers[i-1]) < 4):
            dist=False
    return dist

def dampner(numbers):
    for i in range(len(numbers)):
        dampened_numbers = numbers[:i] + numbers[i + 1:]
        result = is_safe(dampened_numbers)
        if result is True:
            return True
    return False

def is_safe(numbers: list) -> bool:
    return order(numbers) and distinance(numbers)
    
safe = 0
dampend_safe=0
with open('2024/day2/input.txt', 'r') as file:
    for line in file:
        l = list(map(int, line.split()))
        if is_safe(l):
            safe += 1
        elif dampner(l):
            dampend_safe+=1
            

print(safe,dampend_safe, safe+dampend_safe)
    
