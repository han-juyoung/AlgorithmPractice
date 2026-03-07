n = int(input())
k_list = list(map(int, input().split()))

sum_a = 0
sum_b = 0

for i in range(len(k_list)):
    if i%2 == 0:
        sum_a += k_list[i]
    elif i%2 == 1:
        sum_b += k_list[i]

print(max(sum_a, sum_b))