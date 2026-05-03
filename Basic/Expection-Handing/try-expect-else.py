try:
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    result = x/y
except Exception as e:
    print("You can't divide by zero. Error: ", e)
else:
    print("The result is: ", result)
finally:
    print("The program is done.")