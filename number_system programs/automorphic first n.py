def automorphic(n:int)->None:
    s=n**2
    while n>0:
       digit1=s%10
       digit2=n%10
       if digit1!=digit2:
            return False
       n=n//10
       s=s//10
    return True
def display(n:int)->int:
   count=n
   i=1
   while count>0:
       if automorphic(i):
            print(i,end=" ")
            count-=1
       i+=1

n=int(input('enter n value:'))
display(n)
            
