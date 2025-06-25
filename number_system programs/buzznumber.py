def is_buzz(n:int)->bool:
    return  n%7==0 or n%10==7

n=int(input('enter:'))
print(is_buzz(n))
