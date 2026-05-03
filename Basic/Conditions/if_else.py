# =========================================================
# IF - ELIF - ELSE
# =========================================================


# =========================
# Example 1: Salary Level Check
# =========================

salary = 15000

if salary < 20000:
    print("Level: Junior")
elif salary < 50000:
    print("Level: Mid")
else:
    print("Level: Senior")


# =========================
# Example 2: Grading System
# =========================

marks = 85

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# =========================
# Example 3: Even or Odd Number
# =========================

num = 12

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# =========================
# Example 4: Positive, Negative, or Zero
# =========================

value = -10

if value > 0:
    print("Positive Number")
elif value < 0:
    print("Negative Number")
else:
    print("Zero")


# =========================
# Example 5: Login System
# =========================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# =========================
# Example 6: Age Category
# =========================

age = 17

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


# =========================
# Example 7: Temperature Check
# =========================

temperature = 35

if temperature > 40:
    print("Very Hot")
elif temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
else:
    print("Cold")


# =========================
# Example 8: Traffic Light System
# =========================

signal = "red"

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


# =========================
# Example 9: Multiple Conditions (AND / OR)
# =========================

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")


# =========================
# Example 10: Nested If (Real Case)
# =========================

marks = 75

if marks >= 50:
    print("Pass")

    if marks >= 80:
        print("Distinction")
    else:
        print("No Distinction")
else:
    print("Fail")


# =========================
# IMPORTANT LEARNING POINTS
# =========================

# 1. Conditions run TOP to BOTTOM
# 2. First TRUE condition executes only
# 3. '==' checks equality
# 4. '=' is assignment (not comparison)
# 5. AND → both conditions must be True
# 6. OR → any one condition can be True
# 7. Nested if = if inside another if


# =========================
# BONUS REAL SQA IDEA
# =========================

# You can use if-else in automation testing like:
# - API response validation
# - Status code check
# - Login verification
# - Data validation

status_code = 200

if status_code == 200:
    print("Test Passed: API Working")
else:
    print("Test Failed: API Issue")