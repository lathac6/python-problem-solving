def is_prime(n:int)->int:
    if n==0 or n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def is_rev(n:int)->int:
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n//=10
    return rev
def is_emirp(n:int)->bool:
    return is_prime(n) and is_prime( is_rev(n))
n=int(input('enter:'))
print(is_emirp(n))
