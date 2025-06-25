n=int(input('enter:'))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(k,end=" ")
        k+=1
    print()
#-------------------------
n=int(input('enter:'))
k=1
for i in range(1,n+1):
   for j in range(1,n+1):
       print(f'{k:{2}}',end=" ")
       k+=1
   print()

#---------------------------
n=int(input('enter:'))
k=1
w=len(str(n*n))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f'{k:>{w}}',end=" ")
        k+=1
    print()
