a=list(map(int,input("enter array").split()))
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
median=0
if len(a)%2==0:
    median=(a[(len(a)//2)]+a[(len(a)//2)-1])/2
else:
    median=a[len(a)//2]
print(median)