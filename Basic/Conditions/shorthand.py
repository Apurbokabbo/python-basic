# =========================================================
# TERNARY OPERATOR - ADVANCED PRACTICE
# =========================================================


# =========================
# Example 1: Login Status Check
# =========================

is_logged_in = True
status = "Login Successful" if is_logged_in else "Login Failed"
print(status)


# =========================
# Example 2: Pass / Fail Result
# =========================

marks = 45
result = "Pass" if marks >= 50 else "Fail"
print("Exam Result:", result)


# =========================
# Example 3: Age Category
# =========================

age = 17
category = "Adult" if age >= 18 else "Minor"
print("Age Category:", category)


# =========================
# Example 4: Discount System
# =========================

amount = 6000
discount = "20%" if amount > 5000 else "10%" if amount > 2000 else "5%"
print("Discount Applied:", discount)


# =========================
# Example 5: API Status Check (SQA USE CASE)
# =========================

status_code = 404
api_result = "PASS" if status_code == 200 else "FAIL"
print("API Test Result:", api_result)


# =========================
# Example 6: Even or Odd
# =========================

num = 11
type_result = "Even" if num % 2 == 0 else "Odd"
print("Number Type:", type_result)


# =========================
# Example 7: Temperature Status
# =========================

temp = 35
weather = "Hot" if temp > 30 else "Cold"
print("Weather:", weather)


# =========================
# Example 8: Largest Number
# =========================

a = 10
b = 20

largest = a if a > b else b
print("Largest Number:", largest)


# =========================
# Example 9: Login Role Access
# =========================

role = "admin"
access = "Full Access" if role == "admin" else "Limited Access"
print("User Access:", access)


# =========================
# IMPORTANT LEARNING NOTES
# =========================

# 1. Ternary = short if-else
# 2. Best for simple decisions
# 3. Nested ternary = multiple conditions (use carefully)
# 4. Used in automation for quick validations
# 5. Not recommended for complex business logic


# =========================
# SQA REAL AUTOMATION USE CASES
# =========================

# Example: API validation
code = 201
test_status = "PASS" if code in [200, 201] else "FAIL"
print("Test Status:", test_status)


# Example: Browser test result
browser = "Chrome"
result = "Supported" if browser in ["Chrome", "Firefox", "Edge"] else "Not Supported"
print("Browser Check:", result)