def reverse(n:int)->int:
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev
n=int(input('enter n value:'))
print(reverse(n))


#str......
def reverse(n:str)->str:
    return n[::-1]
n=int(input('enter:'))
print(reverse(n))
