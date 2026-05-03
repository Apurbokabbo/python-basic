# =========================
# LIST BASICS
# =========================

# Declare a list (stores multiple values in one variable)
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# Print the entire list
print(programming)
# Output: ['Python', 'Java', 'C#', 'C++', 'Javascript']


# =========================
# ACCESSING ELEMENTS
# =========================

# Access a specific item using index (starts from 0)
print(programming[2])
# Output: C#

# Negative index (starts from end, -1 = last item)
print(programming[-2])
# Output: C++


# =========================
# SLICING (RANGE)
# =========================

# Get items from index 2 to 3 (end index is excluded)
print(programming[2:4])
# Output: ['C#', 'C++']


# =========================
# CHECK IF ITEM EXISTS
# =========================

# Check if "Python" exists in the list
if "Python" in programming:
    print("Python is awesome")

# =========================
# MORE USEFUL LIST EXAMPLES
# =========================

# Add new item
programming.append("Go")
print("After Append:", programming)

# Insert at specific position
programming.insert(1, "Ruby")
print("After Insert:", programming)

# Remove item
programming.remove("Java")
print("After Remove:", programming)

# Length of list
print("Total Languages:", len(programming))

# Loop through list
for lang in programming:
    print("Language:", lang)



# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Test Case List
test_cases = ["TC_Login", "TC_Logout", "TC_Signup"]

# Access specific test case
print("Run:", test_cases[0])   # First test case

# Example 2: Get last test case (useful in execution order)
print("Last Test Case:", test_cases[-1])

# Example 3: Run a subset of test cases
print("Regression Tests:", test_cases[1:3])


# Example 4: Check if a test case exists
if "TC_Login" in test_cases:
    print("Login test is available")


# Example 5: Add new test case dynamically
test_cases.append("TC_Profile_Update")
print("Updated Test Cases:", test_cases)


# Example 6: Remove failed test case (for rerun logic)
test_cases.remove("TC_Logout")
print("After Removal:", test_cases)


# Example 7: Loop through test cases (automation style)
for tc in test_cases:
    print("Executing:", tc)


# Example 8: Store test results
results = ["pass", "fail", "pass"]

# Count failures
fail_count = results.count("fail")
print("Failed Tests:", fail_count)


# Example 9: Pair test cases with results
report = list(zip(test_cases, results))
print("Test Execution Report:", report)