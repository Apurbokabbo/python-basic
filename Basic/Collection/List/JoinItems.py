# =========================
# MERGING LISTS USING LOOP
# =========================

list1 = ["Python", "Java", "C#", "C++", "Javascript"]
list2 = ["PHP", "NodeJS", "Ruby"]

# Loop through list2 and add each item to list1
for x in list2:
    list1.append(x)   # append each element one by one

print("Merged List:", list1)
# Output: ['Python', 'Java', 'C#', 'C++', 'Javascript', 'PHP', 'NodeJS', 'Ruby']


# =========================
# COPY LIST
# =========================

# copy() -> creates a new list with same values
mylist = list1.copy()
print("Copied List:", mylist)

# Important: modifying one will NOT affect the other
mylist.append("Go")
print("Original List:", list1)
print("Modified Copy:", mylist)

# =========================
# BETTER WAY (ALTERNATIVE)
# =========================

# You can also merge lists using extend() (cleaner)
list1 = ["Python", "Java"]
list2 = ["PHP", "Ruby"]
list1.extend(list2)
print("Using extend:", list1)

# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Merge test suites (Smoke + Regression)
smoke_tests = ["TC_Login", "TC_Logout"]
regression_tests = ["TC_Profile", "TC_Settings"]

# Using loop (like your example)
for tc in regression_tests:
    smoke_tests.append(tc)
print("Merged Test Suite:", smoke_tests)


# Example 2: Copy test cases before modification
original_tests = ["TC_Login", "TC_Payment"]
# Create backup copy
backup_tests = original_tests.copy()
# Modify new list
original_tests.append("TC_Logout")
print("Original:", original_tests)
print("Backup:", backup_tests)   # remains unchanged

# Example 3: Prepare re-run test list
failed_tests = ["TC_Login", "TC_Payment"]
rerun_tests = []

# Add failed tests for re-execution
for tc in failed_tests:
    rerun_tests.append(tc)
print("Re-run Tests:", rerun_tests)


# Example 4: Avoid modifying original data
api_response = ["pass", "fail", "pass"]

# Work on copy instead of original
temp_data = api_response.copy()
temp_data.append("fail")
print("Original Response:", api_response)
print("Modified Copy:", temp_data)

# Example 5: Combine multiple environments test data
dev_tests = ["TC_Login", "TC_Search"]
prod_tests = ["TC_Payment"]

all_tests = dev_tests.copy()
all_tests.extend(prod_tests)
print("All Environment Tests:", all_tests)