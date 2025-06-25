n=int(input('enter:'))
for i in range(1,n+1):
    for  j in range(1,n+1):
        if i%2==0:
            print(chr(i+96),end=" ")
        else:
            print(chr(i+64),end=" ")
    print()
