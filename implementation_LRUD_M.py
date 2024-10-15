# size = input(int())

# plan = map(str, input().split())

size = 5
plan = ['R', 'R', 'R', 'U', 'D', 'D']

x, y = 1, 1

direction = ['L', 'R', 'U', 'D']
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

for i in range(len(plan)):
    if plan[i] == direction[0]:
        x += row[0]
        y += col[0]
    if plan[i] == direction[1]:
        x += row[1]
        y += col[1]
    if plan[i] == direction[2]:
        x += row[2]
        y += col[2]
    if plan[i] == direction[3]:
        x += row[3]
        y += col[3]
print(x, y)

# 공간 밖에 대한 처리 필요함