# import os
# os.remove("sample.txt")

# f=open("demo.txt","r")
# data =f.read(5)
# print(data)
# line1 =f.readline()
# print(line1)
# data2 = f.read()
# print(data2)
# f.close()

# f=open("demo.txt","w")
# f.write("This is a line")
# f.close()

# f=open("demo.txt","a")
# f.write("\n append a line")
# f.close()

# f=open("sample.txt","w")

# f.close()

# f=open("demo.txt","r+")
# f.write("abc")
# data =f.read(5)
# f.close()

with open("demo.txt","r") as f:
    data = f.read()
    print(data)
newData = data.replace("My","A")
print(newData)

with open("demo.txt","w") as f:
    f.write(newData)






