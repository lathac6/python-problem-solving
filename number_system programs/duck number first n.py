def duck(n:int)->bool:
    return not n.startswith('0') and '0' in n
def display(n:int)->int:
    count=n
    i=1
    while count>0:
        if duck(str(i)):
             print(i,end=" ")
             count-=1
        i+=1
n=int(input('enter:'))
display(n)
        
