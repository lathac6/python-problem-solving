n=int(input('enter:'))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(k+64),end=" ")
        k+=1
    print()
#--------------------------------
n=int(input('enter:'))
k=65
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(k),end=" ")
        k+=1
    print()
#-------------------------------------
n=int(input('enter:'))
k=65
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(k),end=" ")
        k+=1
        if k==91:
            k=65
    print()
#-------------------------------------------
n=int(input('enter:'))
k=0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(k%26+65),end=" ")
        k+=1
    print()
