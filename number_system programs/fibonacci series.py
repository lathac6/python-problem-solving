def fibonacci(n:int)->int:
    n1=0
    n2=1
    n3=0
    count=n
    while count>0:
        count-=1
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
n=int(input('enter n value:'))
fibonacci(n)
        
        
