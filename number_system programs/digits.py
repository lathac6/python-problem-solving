def display(n:str)->None:
    x=len(n)-1
    for i in range(x,-1,-1):
        print(n[i])
n=input('enter:')
display(n)
