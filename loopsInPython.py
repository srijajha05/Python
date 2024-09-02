count = 1
while count<=100:
    print(count)
    count +=1

count = 100
while count>=1:
    print(count)
    count -=1

n=int(input("Enter a number "))
a=1
while a<=10:
    print(n,"*",a,"=",n*a)
    a +=1

counting = 1
while counting<=10:
    print(counting*counting)
    counting +=1

tuple=(1,4,9,16,25,36,49,64,81,100)
index = 0
x=4
while index<len(tuple):
    if (tuple[index]==x):
        print(index)
    index +=1

index=0
for i in tuple:
    if x==i:
        print(index)
        break
    index +=1

seq = range(5)
for i in seq:
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(11,100,11):
    print(i)
sum =0
n=10
while n>=0:
    sum += n
    n-=1
print(sum)
value = 5
factorial =1
for i in range(1,value+1):
    factorial *= i
print(factorial)