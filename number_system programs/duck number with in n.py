def duck(n:int)->bool:
    return not n.startswith('0') and '0' in n
def display(n:int)->int:
    for i in range(n):
        if duck(str(i)):
             print(i,end=" ")
n=int(input('enter:'))
print(display(n))
        
