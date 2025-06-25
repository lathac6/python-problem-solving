def is_xylem(n:int)->bool:
    es=0
    ms=0
    temp=n
    while n>0:
        d=n%10
        if temp==n or n<10:
            es+=d
        else:
            ms+=d
        n//=10
    return es==ms
n=int(input('enter:'))

print(is_xylem(n))
