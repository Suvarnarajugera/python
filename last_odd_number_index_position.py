n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    if a[i]%2==1:
        b.append(i)
print(max(b))