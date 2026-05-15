

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))


try :
    results = num_1 / num_2

except Exception as e:
    print("Division by zero" ,e)