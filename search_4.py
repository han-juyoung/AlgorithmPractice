# n = 5
# shop = [8, 3, 7, 9, 2]

# m = 3
# cus = [5, 7, 9]

# for i in range(m):
#     if cus[i] in shop:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = input(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
