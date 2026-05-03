class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f'Hi, My name is {self.first_name} {self.last_name}')

class Employee(Person):
    def __init__(self, first_name, last_name, position, salary):
        super().__init__(first_name, last_name)
        self.position = position
        self.salary = salary

    def work(self):
        print(f"Working as {self.position} and earning  {self.salary}")

class Manager(Employee):
    def __init__(self, first_name, last_name, position, salary, department):
        super().__init__(first_name, last_name, position, salary)
        self.department = department

    def department_work(self):
        print(f'Department {self.department}')

manager = Manager("Ebrahim", "Hossain", "SQA", 50000, "IT")
manager.introduce()
manager.work()
manager.department_work()