def pali(n:int)->None:
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    if rev==temp:
        return 'palindrome'
    else:
        return 'not a palindrome'

n=int(input('enter n value:'))
print(pali(n))
