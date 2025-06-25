def neon(n:int)->None:
    sum=0
    s=n**2
    while s>0:
        digit=s%10
        sum+=digit 
        s//=10
    return sum==n
n=int(input('enter n value:'))
print(neon(n))

