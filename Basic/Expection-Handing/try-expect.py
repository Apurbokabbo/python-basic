try:
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    result = x/y
    print(result)
except Exception as e:
    print("You can't divide by zero. Error: ", e)