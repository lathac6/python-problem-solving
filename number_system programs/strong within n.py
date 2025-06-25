def is_factorail(n:int)->int:
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
def is_strong(n:int)->int:
    sum=0
    temp=n
    while n!=0:
        d=n%10
        sum=sum+is_factorail(d)
        n=n//10
    return sum==temp
def display(n:int)->int:
    for i in range(1,n+1):
        if is_strong(i):
            print(i,end=" ")
n=int(input('enter :'))
display(n)
