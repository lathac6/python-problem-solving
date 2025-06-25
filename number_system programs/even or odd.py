def isdigit(v:int)->None:
    n1=n//2
    if n1*2==n:
        print(f'{v} is even')
    else:
        print(f'{v}is odd')
n=int(input('enter n value:'))
isdigit(n)