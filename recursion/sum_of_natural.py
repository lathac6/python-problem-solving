def sum_of_digits(n):
    if n==0:
        return 0
    return n+sum_of_digits(n-1)
n=int(input('enter:'))
print(sum_of_digits(n))
