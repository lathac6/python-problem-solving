def pow(n:int)->int:
    count=0
    while n>0:
        count+=1
        n//=10
    return count
def is_armstrong(n:int)->int:
    sum=0
    temp=n
    count=pow(n)
    while n!=0:
        d=n%10
        sum+=d**count
        n//=10
    return sum==temp
def display(n:int)->int:
    i=1
    while n>0:
        if is_armstrong(i):
            print(i,end=" ")
            n-=1
        i+=1
n=int(input('enter:'))
display(n)
            
