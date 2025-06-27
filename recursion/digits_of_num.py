def digits_of_num(n):
    if n==0:
        return
    print(n%10)
    digits_of_num(n//10)
n=int(input('entere:'))
digits_of_num(n)
