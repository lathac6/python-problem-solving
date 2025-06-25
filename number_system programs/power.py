def is_power(base:int,power:int)->int:
    res=1
    for i in range(power+1):
        res=res*base
    return res    
        
base=int(input('enter:'))
power=int(input('enter:'))
print(is_power(base,power))

#by using while
def is_power(b:int,p:int)->int:
    res=1
    while p>0:
        res*=b
        p-=1
    return res
b=int(input('enter b value:'))
p=int(input('enter p value:'))
print(is_power(b,p))
