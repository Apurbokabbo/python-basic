# syntax
# if condition:
#   execute
#else:
#    block
from Basic import Print

salary =20000

if salary < 20000:
    print("Salary is less than 20000 and Junior")

else:
    print("Salary is greater than 20000 and Mid")

#if condition
#    block
#elif:
#   block
#elif:
#   block
#else
#   block


result =84

if result >90:
    print("result is greater than 90 A+")
elif result>80:
    print("result is greater than 80 A")
elif result>70:
    print("result is greater than 70 B")
elif result <=33:
    print("result is greater than 33 F")
else:
    print("result is invalid")


age =18
city= "Dhaka"
area= ""

if city=="Dhaka":
    if age>=18:
        print("Dhaka valid voter and age is 18 or above")
    else:
        print("Dhaka valid voter age is under 18")
else:
    print("Not in Dhaka ")


# =========================
# Example 3: Even or Odd Number
# =========================

num = int(input("Enter a number: "))
if num%2==0:
    print("The given number is even")
else:
    print("The given number is odd")

# =========================
# Example 5: Login System
# =========================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Welcome Admin")
else:
    print("Wrong Credentials")

# =========================
# Example 6: Age Category
# =========================

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age >= 13 and age < 18:
    print("Teenager")

elif age >= 18 and age <60:
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
# Example 10: Nested If (Real Case)
# =========================

marks = int(input("Enter marks: "))

if marks > 50:
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