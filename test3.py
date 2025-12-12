n,k = map(int,input().split())

a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))

a.sort()
b.sort(reverse=True)

sum=0
for i in range(n):
    if(i<k):
        sum=sum+b[i]
    else:
        sum=sum+a[i]
print(sum)