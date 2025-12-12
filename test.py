n = int(input())

li = []

for i in range(n):
    li.append(int(input()))

li.sort(reverse=True)

print(" ".join(map(  str,li)))