def duck(n:int)->bool:
    return not n.startswith('0') and '0' in n
def display(n:int,m:int)->int:
     for i in range(n,m):
        if duck(str(i)):
            print(i,end=" ")
n=int(input('enter:'))
m=int(input('enter:'))
display(n,m)
        
