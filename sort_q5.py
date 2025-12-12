num = int(input())
list = []
for i in range(num):
    list.append(int(input()))

array = sorted(list, reverse=True)

for i in array:
    print(i, end=' ')
