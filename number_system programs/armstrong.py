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
n=int(input('enter:'))
print(is_armstrong(n))
        
