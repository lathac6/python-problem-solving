n=int(input('enter:'))
k=65
for i in range(n):
    for j in range(n,i,-1):
        print(chr(k),end=" ")
        k+=1
    print()
