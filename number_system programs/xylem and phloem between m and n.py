def is_xylem(n:int)->bool:
    es=0
    ms=0
    temp=n
    while n>0:
        d=n%10
        if temp==n or d==n:
            es+=d
        else:
            ms+=d
        n//=10
    return es==ms

def display(n:int,m:int)->int:
    for i in range(n,m+1):
        if is_xylem(i):
            print(i,end=" ")
n=int(input('enter:'))
m=int(input('enter:'))
display(n,m)
