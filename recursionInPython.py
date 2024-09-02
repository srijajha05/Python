def show(n):
    if(n==0):
        return
    
    show(n-1)
    print(n)

show(5)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

print(factorial(5))

def calculateSum(n):
    if(n==0):
        return 0
    return n +calculateSum(n-1)

print(calculateSum(5))

myList =[2,3,5,6,7,8]

def printList(list,index):
    if index==len(list):
        return
    print(list[index]) 
    printList(list,index+1)
   
printList(myList,0)