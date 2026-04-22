# =========================================================
# FOR LOOP - COMPLETE PRACTICE (BEGINNER TO INTERMEDIATE)
# =========================================================
from operator import index

# =========================
# Example 1: Basic range loop
# =========================

for i in range(5):
    print(i)

# =========================
# Example 2: Range with start and end
# =========================

for i in range(2,8):
    print(f"Number : {i}")

# =========================
# Example 3: Range with step
# =========================
for i in range(0, 20, 2):
    print("Step Value:", i)

# Counting backwards
for i in range(10, 0, -1):
    print("Countdown:", i)

# =========================
# Example 5: Loop through list
# =========================

fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print("Fruit Name",fruit)

# =========================
# Example 6: Loop with index (enumerate)
# =========================

students = ["Tamal", "Apurbo", "Sheikh"]
for name in enumerate(students):
    print(index, "=>", name)

# =========================
# Example 7: BREAK statement
# =========================

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num == 4:
        break  # stop loop when 4 is found
    print("Break Example:", num)

# =========================
# Example 8: CONTINUE statement
# =========================

for num in numbers:
    if num == 3:
        continue  # skip number 3
    print("Continue Example:", num)


# =========================
# Example 9: Loop through string
# =========================

name = "Ebrahim"

for char in name:
    print("Character:", char)


# Example 10: Nested Loop
# =========================

# Outer loop
for i in range(1, 4):
    # Inner loop
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# =========================
# Example 11: Multiplication Table
# =========================

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# =========================
# Example 12: Sum of numbers
# =========================

total = 0

for i in range(1, 11):
    total += i
    print(f"{i}  = {total}")

print("Total Sum:", total)

# =========================
# Example 13: Search in list (SQA concept)
# =========================

users = ["admin", "tester", "developer"]

for user in users:
    if user == "tester":
        print("User Found:", user)
        break

# =========================
# Example 14: Skip invalid data
# =========================

data = [10, 0, 20, 0, 30]

for value in data:
    if value == 0:
        print("Skipping invalid value")
        continue
    print("Valid value:", value)

# =========================
# REAL SQA AUTOMATION EXAMPLES
# =========================


# Example 15: API response validation
responses = [200, 200, 404, 200]

for code in responses:
    if code != 200:
        print("Test Failed! Error Code:", code)
        break
    print("API Passed:", code)


# Example 16: Running test cases
test_cases = ["Login", "Signup", "Payment", "Logout"]

for test in test_cases:
    print("Executing Test Case:", test)


# =========================
# KEY LEARNING POINTS
# =========================

# 1. for loop → used for repeated execution
# 2. range() → generates numbers
# 3. enumerate() → gives index + value
# 4. break → stops loop completely
# 5. continue → skips current iteration
# 6. nested loop → loop inside loop
# 7. widely used in automation testing