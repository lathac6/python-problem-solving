def is_prime(n:int)->int:
    if n==0 or n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return n
def display(n:int)->int:
    for i in range(1,n+1):
        if is_prime(i):
             print(i,end=" ")
n=int(input('enter n value:'))
display(n)
