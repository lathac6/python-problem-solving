def is_buzz(n:int)->bool:
    return  n%7==0 or n%10==7

def display(n:int,m:int)->int:
    for i in range(n,m):
        if is_buzz(i):
            print(i,end=" ")
n=int(input('enter:'))
m=int(input('enter:'))
display(n,m)
