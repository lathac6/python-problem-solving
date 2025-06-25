def is_buzz(n:int)->bool:
    return  n%7==0 or n%10==7

def display(n:int)->int:
    count=n
    i=1
    while count>0:
        if is_buzz(i):
            print(i,end=" ")
            count-=1
        i+=1
n=int(input('enter:'))
display(n)
