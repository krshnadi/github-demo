
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_info(self):
        return f"{self.make} {self.model} {self.year}"
car1 = car('Toyota', 'Innova', 2020)
print(car1) #We get object reference. Using class we can create an object.
print(car1.car_info())
# print(car1.make)
# print(car1.model)
# print(car1.year)

# class car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def car_info(self):
#         print("Car Information:")
#         print(f"make: {self.make}")
#         print(f"model: {self.model}")
#         print(f"year: {self.year}")
#         print('-' * 20)
# car1 = car('Toyota', 'Innova', 2020)
# car2 = car('Hyundai', 'Elantra', 2005)
# #print(car1)
# car1.car_info()
# car2.car_info()
"""
Till now we have created only one Method inside a class. As we know we can create multiple mentods inside 
a single class. We are going to see that below."""

# class BankAccount:
#     def __init__(self, account_name, balance):
#         self.account_name = account_name
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount} and new balance is {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn amount is {amount} and remaining balance is {self.balance}")
#         else:
#             print("Insufficient balance.")
# account1 = BankAccount('Aditya', 10000)
# account1.withdraw(2500)
# account1.deposit(1500)
# account1.withdraw(1000)

#Task: Create a class with Student name.

# """ Encapsulation: This restricts direct access to class variables and allows data modification only 
# through methods."""

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#eg:
class Student:
    def __init__(self):
        self.name = 'Aditya'
        self.age = 35
        self.city = 'Hyderabad'
    def data(self):
        print("My name is : ", self.name)
        print("My age is : ", self.age)
        print(self.name, "currently lives in :", self.city)
        return f"End of execution."

"""We have written class i.e. we have defined the attributes and actions, but this is not sufficient 
just to define a class. We have to use the class. To use the class we need to define instances or objects.
Instance creation or object creation represents alloting memory necessary to store the actual data of the
variables i.e. name, age, city.
To create an instance the below syntax is used:
    syntax:
        instancename = ClassName()"""
s1 = Student()
"""Once instance is created, PVM understands that a class object is created and then starts to allocate
memory in the PVM. Now how much memory to be allocated depends on the attributes and methods inside 
the class."""
print(s1)
s1.data()
#print(s1.data())#we can get the action by object instantiation in the class.
# print(s1.name) #we can directly access the attributes of class using constructor function(__init__).
# print(s1.age)
# print(s1.city)
"""
The following steps occur internally:
1. A block of memory is allocated on Heap. How much memory is to be allocated is decide from the 
attributes and methods available in the Student class.
2. After allocating the memory block, the special method by name '__init__(self)' is called internally.
This method stores the initial data into the variables. Since this method is useful to construct the 
instance, it is called as Constructor.
3. Finally, the allocated memory location address of the instance is returned into 's1' variable. To
see this memory location in decimal number format, we can use id() function as id(s1).
Now s1 refers to the instance of Student class. Hence, any variables or methods in the instance can be 
referred by 's1' using dot operator.
The dot operator takes the instance name at its left and the member of the instance at right hand
side.
"""