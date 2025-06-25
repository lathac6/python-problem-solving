n=int(input('enterr:'))
k=79
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
        if k==91:
            k=65
    print()
