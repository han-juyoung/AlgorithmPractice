n, m = 4, 5
array = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if array[x][y] == 0:
        array[x][y] = 1
        
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)



# def dfs(x, y):
#     if visited[x][y]:
#         return
#     visited[x][y] = True
#     for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#         dfs(x+dx, y+dy)
