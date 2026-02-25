n = int(input())
n_set = set(map(int, input().split())) #  2 3 7 8 9

m = int(input())
m_list = list(map(int, input().split())) # 5 7 9

for i in m_list:
    print("yes" if i in n_set else "no")
    # if i in n_set:
    #     print("yes")
    # else:
    #     print("no")


 