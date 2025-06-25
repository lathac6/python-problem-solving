# def perfect(n:int)->bool:
#     sum=0
#     for i in range(1,n//2+1):
#          if n%i==0:
#             sum+=i
#     return sum==n
# n=int(input('enter n value:'))
# print(perfect(n))
# #approch
def perfect(n:int)->bool:
    sum=0
    i=1
    while n>0:
        if n%i==0:
            sum+=i
            i+=1
    return sum ==n
n=int(input('enter n value:'))
print(perfect(n))
