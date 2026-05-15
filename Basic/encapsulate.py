#private
class Bank:
    def __init__(self):
        #pass
        self.__maximum_salary = 100000

    def get_salary(self):
        self.__maximum_salary +=900
        print("Salary :", self.__maximum_salary)

    def set_maximum_salary(self, maximum_salary):
        self.__maximum_salary += maximum_salary


bank = Bank()
bank.get_salary()

bank.set_maximum_salary(1000)
bank.get_salary()