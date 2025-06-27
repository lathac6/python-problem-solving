def palindrome(n):
    if len(n)<=1:
        return True
    if n[0]!=n[-1]:
        return False
    return palindrome(n[1:-1])
n=input('enter:')
print(palindrome(n))
    
