# =========================
# UPDATING LIST ITEMS
# =========================

# Initial list
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# Update a single item using index
# Index 1 = second element ("Java")
programming[1] = "Go"

print("After single update:", programming)
# Output: ['Python', 'Go', 'C#', 'C++', 'Javascript']


# =========================
# UPDATE MULTIPLE ITEMS (SLICING)
# =========================

# Replace items from index 2 to 3 (end index is excluded)
# So it replaces "C#" and "C++"
programming[2:4] = ["PHP", "HTML"]

print("After slice update:", programming)
# Output: ['Python', 'Go', 'PHP', 'HTML', 'Javascript']


# Example: Replace 2 items with 3 items
nums = [1, 2, 3, 4]
nums[1:3] = [10, 20, 30]
print("More items:", nums)
# Output: [1, 10, 20, 30, 4]

# Example: Replace 2 items with 1 item
nums = [1, 2, 3, 4]
nums[1:3] = [99]
print("Fewer items:", nums)
# Output: [1, 99, 4]

# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Update test case name
test_cases = ["TC_Login", "TC_Logout", "TC_Signup"]

# Fix incorrect test case name
test_cases[1] = "TC_Logout_Fix"
print("Updated Test Cases:", test_cases)


# Example 2: Replace test cases for regression suite
test_cases = ["TC_Login", "TC_Old_Feature1", "TC_Old_Feature2", "TC_Signup"]

# Replace outdated test cases
test_cases[1:3] = ["TC_New_Feature1", "TC_New_Feature2"]

print("Updated Regression Suite:", test_cases)


# Example 3: Update test results
results = ["pass", "fail", "fail"]

# Fix result after bug resolved
results[1] = "pass"

print("Updated Results:", results)


# Example 4: Bulk update test statuses
results = ["fail", "fail", "pass", "fail"]

# Mark multiple tests as passed after fix
results[0:2] = ["pass", "pass"]
print("Bulk Updated Results:", results)

# Example 5: Replace environment configs
environments = ["dev", "staging", "old_prod"]

# Replace old environment
environments[2] = "prod"
print("Updated Environments:", environments)