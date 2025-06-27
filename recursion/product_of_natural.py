def product_of_natural(n):
    if n==0:
        return 1
    return n*product_of_natural(n-1)
n=int(input('enter:'))
print(product_of_natural(n))
