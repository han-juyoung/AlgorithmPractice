# 완전 탐색 유형(가능한 경우의 수를 모두 검사)
# 전체 데이터 수가 100만개 이하일 때 사용하는 것이 적절함

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

