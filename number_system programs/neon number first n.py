def neon(n:int)->None:
    sum=0
    s=n**2
    while s>0:
        digit=s%10
        sum+=digit 
        s//=10
    return sum==n
def display(n:int):
    count=n
    i=1
    while count>0:
        if neon(i):
           print(i,end=" ")
           count+=1
        i+=1
           
n=int(input('enter n value:'))
print(display(n))

