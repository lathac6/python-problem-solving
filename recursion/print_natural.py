def natural(n):
    if n>1:
        natural(n-1)
    print(n)
n=int(input('enter:'))
natural(n)
