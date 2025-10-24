n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# n = 5
# k = 3
# a = [1, 2, 5, 4, 3]
# b = [5, 5, 6, 6, 5]
a = sorted(a)
b = sorted(b, reverse=True)
# a = [1, 2, 3, 4, 5]
# b = [5, 5, 5, 6, 6]

# for i in range(k):
#     for j in range(n):
#         if a[j] < b[j]:
#             a[j] = b[j]
#         else:
#             continue
# sum = 0
# for i in range(n):
#     sum += a[i]
# print(sum)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))