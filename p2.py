from collections import deque

n, m = 5, 6
array = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 0:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))
    return array[n-1][m-1]

print(bfs(0,0))

# def bfs(x,y):
#     queue = deque([x, y])
#     visited[x][y] = True
#     while queue:
#         cx, cy = queue.popleft()
#         for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#             nx, ny = cx+dx, cy+dy
#             if not visited[nx][ny]:
#                 queue.append((nx, ny))
#                 visited[nx][ny] = True