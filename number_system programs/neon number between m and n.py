def neon(n:int)->None:
    sum=0
    s=n**2
    while s>0:
        digit=s%10
        sum+=digit 
        s//=10
    return sum==n
def display(n:int,m:int):
    for i in range(n,m):
        if neon(i):
           print(i,end=" ")
           count-=1
n=int(input('enter n value:'))
m=int(input('enter m vlaue:'))
print(display(n,m))

