def reverse_string(n):
    if len(n)==0:
        return n
    return reverse_string(n[1:])+n[0]
n=input('enter:')
print(reverse_string(n))
