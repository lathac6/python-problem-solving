n=int(input('enter:'))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(i+64),end=" ")
    print()
