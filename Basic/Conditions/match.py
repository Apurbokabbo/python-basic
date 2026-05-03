# =========================================================
# MATCH-CASE STATEMENT
# =========================================================


# =========================
# Example 1: HTTP Status Codes
# =========================

def http_status_code(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "INTERNAL SERVER ERROR"
        case _:
            return "UNKNOWN STATUS"

print(http_status_code(200))
print(http_status_code(404))
print(http_status_code(500))
print(http_status_code(50))


# =========================
# Example 2: Day of Week
# =========================

def day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid Day"

print(day_name(3))
print(day_name(7))
print(day_name(10))


# =========================
# Example 3: User Role System
# =========================

def user_role(role):
    match role:
        case "admin":
            return "Full Access"
        case "tester":
            return "Test Access"
        case "developer":
            return "Code Access"
        case _:
            return "No Access"

print(user_role("admin"))
print(user_role("tester"))
print(user_role("guest"))


# =========================
# Example 4: Calculator Operations
# =========================

def calculator(op, a, b):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else "Cannot divide by zero"
        case _:
            return "Invalid Operator"

print(calculator("+", 10, 5))
print(calculator("*", 3, 4))
print(calculator("/", 10, 0))


# =========================
# Example 5: API Test Result Mapping (SQA Use Case)
# =========================

def api_test_result(status_code):
    match status_code:
        case 200:
            return "Test Passed"
        case 201:
            return "Created Successfully"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Response"

print(api_test_result(200))
print(api_test_result(401))
print(api_test_result(999))


# =========================
# Example 6: Browser Selection
# =========================

def browser_launcher(browser):
    match browser.lower():
        case "chrome":
            return "Launching Chrome Browser"
        case "firefox":
            return "Launching Firefox Browser"
        case "edge":
            return "Launching Edge Browser"
        case _:
            return "Browser Not Supported"

print(browser_launcher("Chrome"))
print(browser_launcher("Firefox"))
print(browser_launcher("Safari"))


# =========================
# Example 7: Simple Menu System
# =========================

def menu(option):
    match option:
        case 1:
            return "Create User"
        case 2:
            return "Update User"
        case 3:
            return "Delete User"
        case 4:
            return "View Users"
        case _:
            return "Invalid Option"

print(menu(1))
print(menu(4))
print(menu(10))


# =========================
# LEARNING NOTES
# =========================

# 1. match-case = cleaner alternative to if-elif
# 2. case _ = default (like else)
# 3. Best for fixed values (status codes, menus, roles)
# 4. Makes code more readable in automation testing
# 5. Available in Python 3.10+