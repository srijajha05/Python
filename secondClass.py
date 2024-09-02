name =input("Enter you name ")
print("your name has ",len(name)," characters")

marks=int(input("Enter your marks "))
if(marks>=90):
    print("Very Good")
elif(marks>75):
    print("Good")
else:
    print("Keep Practicing")

numberEntered = int(input("Enter a number "))
if(numberEntered & 1)==0:
    print("Even number")
else:
    print("Odd number")