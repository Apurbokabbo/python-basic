# =========================================================
# WHILE LOOP - COMPLETE PRACTICE (BEGINNER + SQA LEVEL)
# =========================================================


# =========================
# Example 1: Basic While Loop
# =========================

i = 1
# Loop runs until condition becomes False
while i <= 10:
    print("Value:", i)
    i += 1   # increment to avoid infinite loop


# =========================
# Example 2: While + Else
# =========================

i = 1
while i <= 5:
    print("Counting:", i)
    i += 1
else:
    # runs when while condition becomes False
    print("Loop completed successfully")


# =========================
# Example 3: Continue Statement
# =========================

i = 0
while i < 10:
    i += 1
    # skip number 4
    if i == 4:
        continue
    print("Continue Example:", i)


# =========================
# Example 4: Break Statement
# =========================

i = 1
while i <= 10:
    if i == 6:
        break  # stop loop completely
    print("Break Example:", i)
    i += 1


# =========================
# Example 5: Input Validation Loop
# =========================

while True:
    user_input = int(input("Enter a positive number: "))

    if user_input > 0:
        print(f"{user_input} is valid")
        break
    else:
        print(f"Invalid input: {user_input}")


# =========================
# Example 6: Login System (SQA REAL CASE)
# =========================

while True:
    user_email = input("Enter email: ")
    user_password = input("Enter password: ")
    if user_email == "admin@gmail.com" and user_password == "admin123":
        print("Login Successful: Admin Access Granted")
        break
    else:
        print("Invalid credentials, try again")


# =========================
# Example 7: Retry Mechanism (Automation Concept)
# =========================

attempt = 1
while attempt <= 3:
    print(f"API Request Attempt: {attempt}")
    # Simulated failure condition
    if attempt == 3:
        print("API Success on retry")
        break
    attempt += 1


# =========================
# Example 8: Sum using While Loop
# =========================

i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Total Sum:", total)


# =========================
# Example 9: Factorial Calculation
# =========================

n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("Factorial:", factorial)


# =========================
# Example 10: Menu System (Real Application Style)
# =========================

while True:
    print("\n1. Create User")
    print("2. Update User")
    print("3. Delete User")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("User Created")
    elif choice == 2:
        print("User Updated")
    elif choice == 3:
        print("User Deleted")
    elif choice == 4:
        print("Exiting system")
        break
    else:
        print("Invalid option")


# =========================
# IMPORTANT LEARNING NOTES
# =========================

# 1. while loop runs until condition becomes False
# 2. always update variable inside loop (avoid infinite loop)
# 3. break → stops loop completely
# 4. continue → skips current iteration
# 5. while True → used for infinite loops (login, API retry, menu systems)
# 6. widely used in automation testing (retry, polling, validation)


# =========================
# SQA AUTOMATION USE CASES
# =========================

# - Login retry system
# - API retry mechanism
# - Waiting for UI element
# - Polling for response status
# - Menu-driven automation tools