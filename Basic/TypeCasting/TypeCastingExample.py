# =========================
# More Type Conversion Examples
# =========================

# -------- Float to String --------
# Converting a float number to string
price = 99.99
price_str = str(price)

# Now it's text, not a number
print("Float to String:", price_str, "| Type:", type(price_str))


# -------- Int to String --------
# Converting integer to string
num = 50
num_str = str(num)

print("Int to String:", num_str, "| Type:", type(num_str))


# -------- String to Float --------
# String must contain a valid decimal number
float_str = "45.67"
float_num = float(float_str)

print("String to Float:", float_num, "| Type:", type(float_num))


# -------- Boolean to Int --------
# True = 1, False = 0 in Python
is_active = True
bool_to_int = int(is_active)

print("Boolean to Int:", bool_to_int)


# -------- Int to Boolean --------
# 0 = False, any non-zero = True
num1 = 0
num2 = 5

print("0 to Boolean:", bool(num1))   # False
print("5 to Boolean:", bool(num2))   # True


# -------- List to String (using join) --------
# join() works only with list of strings
words = ["Python", "is", "easy"]

# Combine list items into a single string
sentence = " ".join(words)

print("List to String:", sentence)


# -------- String to List --------
# split() converts string into list
text = "Python is powerful"

word_list = text.split(" ")

print("String to List:", word_list)


# -------- Error Example (Important) --------
# This will cause an error because "abc" is not a number
# Uncomment to test

# invalid = int("abc")   # ❌ ValueError
# print(invalid)


# -------- Float Rounding vs Int Conversion --------
value = 9.8

# int() truncates (removes decimal)
print("Using int():", int(value))   # 9

# round() rounds to nearest value
print("Using round():", round(value))  # 10


# -------- Nested Conversion --------
# Convert string → float → int
num_str = "25.9"

converted = int(float(num_str))  # First float, then int
print("Nested Conversion:", converted)  # 25