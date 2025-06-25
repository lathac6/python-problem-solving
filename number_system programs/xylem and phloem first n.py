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
    count=n
    i=1
    while count>0:
        if is_xylem(i):
            print(i,end=" ")
            count-=1
        i+=1
            
n=int(input('enter:'))
dis(n)
