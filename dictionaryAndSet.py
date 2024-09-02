dictionary ={
    "name" : "Srija",
    "age" : 21
}
set={2,3,4,5}
print(set.pop())
print(set.pop())
print(set)
set.clear()
print(set)

set1={1,2,3,4,5,6,7,8,9}
set2={1,3,5,7,9}
print(set1.union(set2))
print(set1.intersection(set2))

myDictionary={
    "table":["a peice of furniture","lists of facts and figures"],
    "cat":"a small animal"
}
print(myDictionary)

set={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(set))

subjectDictionary ={}

subject1 =int(input("Enter subject 1 marks "))
subject2 = int(input("Enter subject 2 marks "))
subject3 = int(input("Enter subject 3 marks "))

subjectDictionary.update({"Subject 1":subject1})
subjectDictionary.update({"Subject 2":subject2})
subjectDictionary.update({"Subject 3":subject3})

print(subjectDictionary)


set={9, '9.0'}
print(set)
set={("int",9),("float",9.0)}
print(set)
