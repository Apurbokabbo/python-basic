class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f'Hi, My name is {self.first_name} {self.last_name}')

class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def work(self):
        print(f"Working as {self.position} and earning  {self.salary}")

class Manager(Person, Employee):
    def __init__(self, first_name, last_name, position, salary):
        Person.__init__(self, first_name, last_name)
        Employee.__init__(self, position, salary)

manager = Manager("Ebrahim", "Hossain", "SQA", 50000)
manager.introduce()
manager.work()