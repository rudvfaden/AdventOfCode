# part1 

l1=[]
l2=[]

with open('2024/day1/input.txt','r') as file:
    for line in file:
        n1, n2 = map(int,line.strip().split())
        l1.append(n1)
        l2.append(n2)
    
l1.sort()
l2.sort()
result=sum([abs(a-b) for a,b in zip(l1,l2)])

print(result)

# part 2
similarity_score=0
for list in l1:
    similarity_score+=l2.count(list)*list
    
print(similarity_score)