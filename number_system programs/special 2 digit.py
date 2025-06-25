def special2(n:int)->bool:
    if 9<n<100:
        l=n%10
        f=n//10
        print 
        res=(l*f)+(l+f)
        return res==n
    else:
        return False
n=int(input('enter:'))
print(special2(n))
