# n, m = map(int, input().split())
# for i in range(n):
#   data = map(int, input().split())
#   data[i].sort()
#   min = data[i][0]
#   data_set.append(min)

# data_set.sort()

# print(data_set[-1])


n = 3
m = 3
data = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]

data_set = []

for i in range(n):
  data[i].sort()
  min = data[i][0]
  data_set.append(min)

data_set.sort()

print(data_set[-1])