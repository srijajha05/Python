# def findLen(a):
#     return len(a)

# a=[1,2,3,45,6,78,9]
# print(findLen(a))

# def printarray(array):
#     for i in range(0,len(array),1):
#         print(array[i] ,end=' ')

# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     print(f)

# printarray(a)
# factorial(5)

def findINR(usd):
    return usd*83

print(findINR(2))

def check(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

check(7)