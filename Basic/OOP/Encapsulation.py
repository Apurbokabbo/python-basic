class Bank:
    def __init__(self):
        self.__max_salary = 100000  # Private

    def getSalary(self):
        self.__max_salary = self.__max_salary + 1000
        print("Salary: ", self.__max_salary)

    def setMaxSalary(self, new_max_salary):
        self.__max_salary = new_max_salary

bank = Bank()
bank.getSalary()

bank.setMaxSalary(100)
bank.getSalary()