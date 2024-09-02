class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks

    def get_avg(self):
        sum=0
        for value in self.marks:
            sum +=value
        print(self.name,"the average of your marks are",sum/3)

s1 = Student("Srija",[99,100,100])
s1.get_avg()

class Accounts:
    def __init__(self,bal,acc):
        self.balance =bal
        self.accountNumber=acc

    def debit(self,amount):
        self.balance -= amount

    def credit(self,amount):
        self.balance += amount
        

Account1=Accounts(10000000,980701)
print(Account1.balance)
Account1.debit(500)
print(Account1.balance)
Account1.credit(500)
print(Account1.balance)

