def pow(n:int)->int:
    count=0
    while n>0:
        count+=1
        n//=10
    return count
def is_armstrong(n:int)->int:
    sum=0
    temp=n
    l=pow(n)
    while n!=0:
        d=n%10
        sum+=d**l
        n//=10
    return sum==temp
def display(n:int)->int:
    for i in range(1,n+1):
        if is_armstrong(i):
            print(i,end=" ")
n=int(input('enter n value:'))
display(n)
