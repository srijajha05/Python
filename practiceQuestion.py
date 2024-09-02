with open("practiceQuestion.txt","w") as f:
    f.write("hello everyone\nWe are learning File I/O\nusing java\nI like programming in java")

with open("practiceQuestion.txt","r") as f:
    data=f.read()


newData = data.replace("java","python")
print(newData)

with open("practiceQuestion.txt","w") as f:
    f.write(newData)

if newData.find("learning"):
    print("found")
else:
    print("not found")

word ="learning"
if newData.find(word) !=-1:
    print("found")
else:
    print("not found")

def find_line():
    word="learning"
    data =True
    line_no =1
    with open("practiceQuestion.txt","r") as f:
        while data :
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1

find_line()

with open("myFile.txt","r") as f:
    data = f.read()
    print(data)

    num=''
    for i in range(len(data)):
        if (data[i]==","):
            print(int(num))
            num=""
        else:
            num +=data[i]

count =0
with open("myFile.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)
    for val in nums:
        if int(val)%2==0:
            count +=1

print(count)




