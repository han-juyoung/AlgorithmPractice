n = int(input())

li =[]

for i in range(n):
    name, grade = input().split(" ")
    li.append((name,int(grade)))

li.sort(key= lambda x : x[1])

print(" ".join([x[0] for x in li]))