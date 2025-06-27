def get_gcd(a,b):
    if b==0:
        return a
    return get_gcd(b,a%b)
a=int(input('enter:'))
b=int(input('enter:'))
if a>b:
    print(get_gcd(a,b))
else:
    print(get_gcd(b,a))
