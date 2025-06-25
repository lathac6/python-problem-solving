n=int(input('enter:'))
for i in range(1,n+1):
    for j in range(i,n+1):
        if i%2==0:
            print(chr(97),end=" ")
        else :
            print(chr(65),end=" ")
    print()
