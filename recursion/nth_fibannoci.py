def fibanocci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibanocci(n-1)+fibanocci(n-2)
n=int(input('enter:'))
print(fibanocci(n))
