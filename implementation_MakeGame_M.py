# 입력예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

row, col = map(int, input().split())
nx, ny, direction = map(int, input().split())
for i in range(row):
    data = list(map(int, input().split()))
north = 0
east = 1
south = 2
west = 3

