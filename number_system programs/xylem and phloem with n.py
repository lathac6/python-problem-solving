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
def dis(n:int)->int:
    for i in range(n):
        if is_xylem(i):
            print(i,end=" ")
            
n=int(input('enter:'))
dis(n)
