def perfect(n:int)->bool:
    sum=0
    for i in range(1,n//2+1):
         if n%i==0:
            sum+=i
    return sum==n
def display(n:int)->None:
    for i in range(1,n+1):
        if perfect(i):
            print(i,end=" ")
n=int(input('enter:'))
display(n)
