def fac(n:int)->int:
    f=1
    i=1
    while i<=n:
        f=f*i
        i+=1
    return f
def strong(n:int)->bool:
    sum=0
    temp=n
    for i in range(1,n+1):
        while n>0:
            d=n%10
            sum+=fac(d)
            n//=10
    return temp==sum
n=int(input('enter:'))
print(strong(n))
