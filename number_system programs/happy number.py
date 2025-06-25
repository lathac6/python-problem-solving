def is_sum(n:int)->int:
    sum=0
    while n!=0:
        d=n%10
        sum+=d**2
        n//=10
    return sum
def is_happy(n:int)->bool:
    while  n>9:
        n=is_sum(n)
    return  n==1 or n==7
n=int(input('enter:'))
print(is_happy(n))
        
