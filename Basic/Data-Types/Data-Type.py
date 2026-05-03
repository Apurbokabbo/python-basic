# Assigning a string value to a variable named 'name'
name = "Walid"

# Printing the value stored in 'name'
print(name)

# Printing the data type of 'name'
# Expected output: <class 'str'> (because it's a string/text)
print(type(name))


# Assigning a very large integer value to 'age'
age = 201132

# Printing the data type of 'age'
# Expected output: <class 'int'> (Python supports large integers)
print(type(age))


# Assigning a decimal (floating-point) number to 'price'
price = 15.59

# Printing the data type of 'price'
# Expected output: <class 'float'>
print(type(price))


# Assigning a number inside quotes → this makes it a string, NOT a number
price1 = '15.25'

# Printing the data type of 'price1'
# Expected output: <class 'str'>
print(type(price1))


# Assigning a boolean value (True/False)
is_active = True

# Printing the data type of 'is_active'
# Expected output: <class 'bool'>
print(type(is_active))


# Creating a list (ordered collection) of integers
numbers = [1, 2, 3]

# Printing the data type of 'numbers'
# Expected output: <class 'list'>
print(type(numbers))


# Creating a list with mixed data types (int, string, float, boolean)
mixed_list = [1, "Test", 3.14, True]

# Printing the data type of 'mixed_list'
# Expected output: <class 'list'>
print(type(mixed_list))


# Creating a dictionary (key-value pair structure)
student = {
    "name": "Walid",   # key: 'name', value: string
    "age": 25,         # key: 'age', value: integer
    "height": 22.5,    # key: 'height', value: float
    "weight": 22.5     # key: 'weight', value: float
}

# Printing the data type of 'student'
# Expected output: <class 'dict'>
print(type(student))