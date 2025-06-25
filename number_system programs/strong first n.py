def is_fact(n:int)->int:
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def is_strong(n:int)->int:
    temp=n
    sum=0
    while n!=0:
        d=n%10
        sum+=is_fact(d)
        n//=10   
    return sum==temp
def display(n:int)->int:
    count=0
    i=1
    while count<n:
        if is_strong(i):
            print(i,end=" ")
            count+=1
        i+=1
    
n=int(input('enter n value:'))
display(n)
    
