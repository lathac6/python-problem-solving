def is_buzz(n:int)->bool:
    return  n%7==0 or n%10==7

def display(n:int)->int:
    for i in range(n):
        if is_buzz(i):
            print(i,end=" ")
n=int(input('enter:'))
display(n)
