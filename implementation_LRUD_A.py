n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 벗어나면 무시
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            # 이동
            x, y = nx, ny

print(x, y)















