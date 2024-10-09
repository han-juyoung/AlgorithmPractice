n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
count = 0
result = 0
for i in range(1,m-1):
    count += 1
    result += data[0]
    if count == k:
        count = 0
        result += data[1]
print(result)