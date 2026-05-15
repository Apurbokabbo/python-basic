class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f" Name: {self.name} is {self.age} years old"

class Employee:
    def __init__(self, position,dept,salary):
        self.position = position
        self.dept = dept
        self.salary = salary

    def work(self):
        return f" Position : {self.position} Department: {self.dept} Salary: {self.salary}"

class Manager(Person, Employee):
    def __init__(self,name,age,position,dept,salary,experience):
        Person.__init__(self,name,age)
        Employee.__init__(self,position,dept,salary)
        self.experience = experience


manager = Manager("Apurbo Kabbo" ,27 , "Sr SQA" , "SQA", "10k",5)
print(manager.introduce())
print(manager.work())

