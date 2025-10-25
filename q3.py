# s = '0001100'
# count = 0
# for i in range(0,7):
#     if s[i-2] == s[i-1]:
#         continue
#     else:
#         if s[i-1] == s[i]:
#             count += 1
#         else:
#             count += 2

# print(count)

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 +=1

# 0001100

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
        
print(min(count0, count1))