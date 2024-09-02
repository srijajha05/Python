marks =[95.4 ,96.4,100]
print(marks)
print(marks[0:2])
marks.append(101);
print(marks)
marks.sort(reverse=True)
print(marks)
marks.sort()
print(marks)
marks.insert(2,1000)
print(marks)
marks.remove(1000)
marks.pop(3)
print(marks)

print("Enter your 3 favourite movies")
movies =[]
movies.append ( input("Enter 1st movie "))
movies.append(input("Enter 2nd movie "))
movies.append (input("Enter 3rd movie "))
print(movies)

list =[1,2,3,2,1]
list2 =list.copy()
list.reverse()
if(list==list2):
    print("The list is a palindrome")