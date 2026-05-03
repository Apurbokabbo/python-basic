# =========================
# BASIC FUNCTION EXAMPLES
# =========================

# Function declaration (no parameters)
# This function simply prints "Hello"
def hello():
    print("Hello")

# Function call (executing the function)
hello()   # Output: Hello


# Function with a parameter
# 'name' is a parameter (input)
def welcome(name):
    print("Welcome:", name)

# Calling function and passing argument
welcome("GTA")   # Output: Welcome: GTA


# Function with return value
# This function takes two numbers and returns their sum
def add(x, y):
    return x + y   # return sends value back to caller

# Storing returned value in a variable
result = add(1, 2)
print("Addition:", result)   # Output: Addition: 3


# Function returning formatted string
def welcome1(name):
    return f'Welcome {name}!'

# Printing returned value directly
print(welcome1("GTA"))   # Output: Welcome GTA!



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Test Case Status Checker
# This function checks if a test case passed or failed
def check_test_status(status):
    if status == "pass":
        return "Test Case Passed ✅"
    else:
        return "Test Case Failed ❌"

print(check_test_status("pass"))
print(check_test_status("fail"))


# Example 2: Bug Severity Classifier
# Helps QA engineers categorize bugs
def bug_severity(priority):
    if priority == "high":
        return "Critical Bug 🚨"
    elif priority == "medium":
        return "Major Bug ⚠️"
    else:
        return "Minor Bug ℹ️"

print(bug_severity("high"))
print(bug_severity("low"))


# Example 3: API Response Validation
# Simulates checking API response status code
def validate_response(status_code):
    if status_code == 200:
        return "API Working Fine 👍"
    else:
        return "API Issue Found ❌"

print(validate_response(200))
print(validate_response(500))


# Example 4: Login Test Function
# Simulates login test validation
def login_test(username, password):
    # Assume correct credentials
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login Test Passed ✅"
    else:
        return "Login Test Failed ❌"

print(login_test("admin", "1234"))
print(login_test("user", "wrong"))


# Example 5: Count Passed Test Cases
# Helps in reporting
def count_passed_tests(results):
    count = 0
    for result in results:
        if result == "pass":
            count += 1
    return count

test_results = ["pass", "fail", "pass", "pass"]
print("Total Passed Tests:", count_passed_tests(test_results))