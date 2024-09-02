class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
    
c1=Circle(21)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self,role,dept,salary):
        self.role =role
        self.dept =dept
        self.salary = salary
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

e1=Employee("a","abc",1000000)
e1.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
        return self.price>order2.price
    
order1 =Order("chips",20)
order2 = Order("avacado",50)

print(order1>order2)