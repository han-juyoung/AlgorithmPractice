# x = [0] * 30001
# num = int(input())
# sum = 0

# while num != 1:
#     if num % 5 == 0:
#         num = num // 5
#         x[num] = 1
#     elif num % 3 == 0:
#         num = num // 3
#         x[num] = 1
#     elif num % 2 == 0:
#         num = num // 2
#         x[num] = 1
#     else:
#         num = num - 1

# for i in x:
#     sum += i
# print(sum)

x = int(input())
d = [0] * 30001

for i in range(2, x+1): 
    d[i] = d[i-1] + 1
    if i%5 == 0: # 모든경우 탐색 if if if 써야함.
        d[i] = min(d[i], d[i//5] + 1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
print(d[x])