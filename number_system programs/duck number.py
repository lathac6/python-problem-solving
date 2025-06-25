def duck(n:int)->bool:
    return not n.startswith('0') and '0' in n
n=input('enter:')
print(duck(n))
        
