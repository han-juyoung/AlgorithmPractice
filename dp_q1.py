cal = [0] * 4

n = int(input())

while n != 1:
    if n % 5 == 0:
        cal[0] += 1
        n = n // 5
    elif n % 3 == 0:
        cal[1] += 1
        n = n // 3
    elif n % 2 == 0:
        cal[2] += 1
        n = n // 2
    else:
        cal[3] += 1
        n -= 1

print(sum(cal))
    
