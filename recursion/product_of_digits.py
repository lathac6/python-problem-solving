def product_of_digits(n):
    if n==0:
        return 1
    return (n%10)*product_of_digits(n//10)
n=int(input('enter:'))
print(product_of_digits(n))
