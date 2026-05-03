# =========================
# LIST MODIFICATION METHODS
# =========================

# Initial list
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# append() -> adds item at the END of the list
programming.append("Python")
# Note: duplicates are allowed in lists

print("After append:", programming)
# Output: ['Python', 'Java', 'C#', 'C++', 'Javascript', 'Python']

# insert() -> adds item at a specific index
programming.insert(2, "HTML")
# "HTML" will be placed at index 2, shifting others to the right

print("After insert:", programming)

# extend() -> adds multiple items from another list
newlist = ["PHP", "NodeJS", "Ruby"]

programming.extend(newlist)
# This will merge both lists

print("After extend:", programming)

# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Add new test case dynamically
test_cases = ["TC_Login", "TC_Logout"]

test_cases.append("TC_Signup")   # adding new test case
print("Test Cases:", test_cases)


# Example 2: Insert high priority test at top
test_cases.insert(0, "TC_Critical_Payment")
print("Priority Test Cases:", test_cases)


# Example 3: Merge regression + smoke test suites
smoke_tests = ["TC_Home", "TC_Search"]
regression_tests = ["TC_Profile", "TC_Settings"]

smoke_tests.extend(regression_tests)
print("Merged Suite:", smoke_tests)


# Example 4: Avoid duplicate test cases (important in SQA)
test_cases.append("TC_Login")  # duplicate added

# Remove duplicates using set()
unique_tests = list(set(test_cases))
print("Unique Test Cases:", unique_tests)


# Example 5: Add multiple failed tests for re-run
failed_tests = ["TC_Login", "TC_Payment"]

rerun_list = []
rerun_list.extend(failed_tests)
print("Re-run List:", rerun_list)