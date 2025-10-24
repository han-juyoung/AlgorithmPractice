n = int(input())
array = []
for i in range(n):
    array.append(input().split())

def setting(item):
    return item[1] 

result = sorted(array, key=setting)

name = []
for i in result:
    name.append(i[0])

for i in name:
    print(i, end=' ')