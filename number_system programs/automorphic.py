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
n=int(input('enter n value:'))
print(automorphic(n))
            
