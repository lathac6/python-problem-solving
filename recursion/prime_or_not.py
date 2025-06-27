def prime(n,div=None):
    if n==0 or n==1:
        return False
    if  div is None:
        div=n//2
    if div==1:
        return True
    if n%div==0:
        return False
    return prime(n,div-1)
n=int(input('enter:'))
print(prime(n))
