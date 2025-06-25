def is_fibb(n:int)->int:
    f1=0
    f2=1
    count=0
    while count<n:
        count+=1
        f3=f1+f2
        f1=f2
        f2=f3
    print(f1)
n=int(input('enter:'))
is_fibb(n)
