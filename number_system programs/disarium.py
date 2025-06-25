def is_count(n:int)->int:
    count=0
    while n!=0:
        count+=1
        n//=10
    return count
def is_sum(n:int)->int:
    sum=0
    count=is_count(n)
    temp=n
    while n>0:
        d=n%10
        sum+=d**count
        count-=1
        n//=10
    return sum==temp
n=int(input('enter:'))
print(is_sum(n))

    
        
