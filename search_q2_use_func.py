def binary_search(array, target, start, end):
    # start = array[0]
    # end = array[-1] 필요X
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            # return 틀림
            return mid
        # elif mid < target:
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return None

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    # binary_search(n_list, i, 0, m)
    # result = binary_search(n_list, i, 0, m) 틀림
    result = binary_search(n_list, i, 0, n-1) # n 안에 해당 부품이 존재하는지 확인해야함
    # if i: 틀림
    if result != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')         
