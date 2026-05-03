# =========================
# LOOPING THROUGH A LIST
# =========================

programming = ["Python", "Java", "C#", "C++", "Javascript"]

# -------------------------
# Method 1: Direct loop (BEST & MOST READABLE)
# -------------------------
for item in programming:
    print(item)
# Output:
# Python
# Java
# C#
# C++
# Javascript


# -------------------------
# Method 2: Using index (range + len)
# -------------------------
# Useful when you need index position
for i in range(len(programming)):
    print(f'Index {i}: {programming[i]}')
# Output:
# Index 0: Python
# Index 1: Java
# ...


# -------------------------
# Method 3: List comprehension (NOT recommended for print)
# -------------------------
# This works, but it's not good practice for printing
# because list comprehension is meant for creating lists
[print(item) for item in programming]


# =========================
# BETTER ALTERNATIVE (IMPORTANT)
# =========================

# Use enumerate() when you need both index + value
for index, item in enumerate(programming):
    print(f'Index {index}: {item}')



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Execute test cases
test_cases = ["TC_Login", "TC_Logout", "TC_Signup"]

for tc in test_cases:
    print("Executing:", tc)


# Example 2: Show test case index (useful in logs)
for i, tc in enumerate(test_cases, start=1):
    print(f"Step {i}: Running {tc}")


# Example 3: Loop with condition (only run specific tests)
for tc in test_cases:
    if "Login" in tc:
        print("Running only login-related test:", tc)


# Example 4: Loop through test results
results = ["pass", "fail", "pass"]
for i, result in enumerate(results):
    print(f"Test {i} result: {result}")


# Example 5: Stop execution if failure found (important in automation)
for result in results:
    if result == "fail":
        print("Test failed! Stopping execution ❌")
        break


# Example 6: Skip passed tests and only print failed ones
for result in results:
    if result == "pass":
        continue
    print("Failed test found:", result)


# Example 7: Validate all test cases executed
executed = []
for tc in test_cases:
    executed.append(tc)
print("Executed Test Cases:", executed)