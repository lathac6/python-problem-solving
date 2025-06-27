def count_of_digits(n):
    if n==0:
        return 0
    return 1+count_of_digits(n//10)
n=int(input('enter:'))
print(count_of_digits(n))
#or
def count_of_digits(n):
    if n<10:
        return 1
     return 1+count_of_digits(n//10)
#or
def count_of_digits(n):
    n=abs(n)
     if n<10:
        return 1
     return 1+count_of_digits(n//10)
