def perfect(n:int)->int:
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    return sum==n
def display(count:int)->None:
    i=1
    while count>0:
        if perfect(i):
            print(i,end=" ")
            count-=1
        i+=1
count=int(input('enter n value:'))
display(count)
    
