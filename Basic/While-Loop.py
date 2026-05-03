# =========================
# Variable Examples
# =========================

# -------- Different Data Types in Variables --------
username = "ebrahim123"   # string
age = 30                  # integer
height = 5.8              # float
is_logged_in = False      # boolean

print(username, age, height, is_logged_in)


# -------- Dynamic Typing (Python feature) --------
# Same variable can hold different types over time
data = 100
print("Before:", data, type(data))

data = "Now I'm a string"
print("After:", data, type(data))


# -------- Using Variables in Expressions --------
a = 10
b = 5

sum_result = a + b
mul_result = a * b

print("Sum:", sum_result)
print("Multiplication:", mul_result)


# -------- Combining (Concatenation) --------
first_name = "Ebrahim"
last_name = "Hossain"

# Combine strings using +
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Better way using f-string
print(f"My name is {first_name} {last_name}")


# -------- Updating Variable Value --------
count = 0
print("Initial count:", count)

# Incrementing value
count = count + 1   # or count += 1
print("Updated count:", count)


# -------- Input from User --------
# input() always returns string
user_input = input("Enter a number: ")

print("You entered:", user_input)
print("Type:", type(user_input))

# Convert input to integer
user_number = int(user_input)
print("Converted to int:", user_number)


# -------- Checking Variable Type --------
value = 25.5

print("Is integer?", isinstance(value, int))    # False
print("Is float?", isinstance(value, float))    # True


# -------- Constants (by convention) --------
# Python doesn't have true constants, but we use uppercase
PI = 3.1416
MAX_LIMIT = 100

print("PI value:", PI)


# -------- Deleting a Variable --------
temp = "temporary data"
print(temp)

# Delete variable using del
del temp

# print(temp)  # ❌ This will cause error (variable no longer exists)


# -------- Unpacking with List --------
numbers = [1, 2, 3]

# Assign list values to variables
a, b, c = numbers

print("Unpacked:", a, b, c)


# -------- Ignoring Values While Unpacking --------
data = ("Ebrahim", 30, "Dhaka")

name, _, city = data   # '_' is used to ignore value

print("Name:", name)
print("City:", city)


# -------- Using Variables Inside Lists & Dictionaries --------
name = "Ebrahim"
age = 30

user = {
    "name": name,
    "age": age
}

print("User Dictionary:", user)