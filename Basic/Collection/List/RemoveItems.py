# =========================
# REMOVING ITEMS FROM LIST
# =========================

programming = ["Python", "Java", "C#", "C++", "Javascript"]

# -------------------------
# remove() -> removes specific VALUE
# -------------------------
programming.remove("Python")
# Removes the first occurrence of "Python"

print("After remove:", programming)
# Output: ['Java', 'C#', 'C++', 'Javascript']


# -------------------------
# pop() -> removes by INDEX (default: last item)
# -------------------------
programming.pop()
# No index → removes last item ("Javascript")

print("After pop:", programming)
# Output: ['Java', 'C#', 'C++']

# pop() also returns the removed value
removed_item = programming.pop(1)
print("Removed item:", removed_item)
print("After pop with index:", programming)


# -------------------------
# del -> deletes item or entire list
# -------------------------
del programming[1]
# Deletes item at index 1
print("After del:", programming)


# -------------------------
# clear() -> removes ALL items (empties list)
# -------------------------
programming.clear()

print("After clear:", programming)
# Output: []


# =========================
# IMPORTANT DIFFERENCES
# =========================

# remove("value") -> removes by VALUE
# pop(index)      -> removes by INDEX and returns value
# del             -> deletes item or whole list
# clear()         -> empties list

# ⚠️ Common Errors:
# remove("X") -> error if value not found
# pop(index)  -> error if index out of range


# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Remove executed test case
test_cases = ["TC_Login", "TC_Logout", "TC_Signup"]
test_cases.remove("TC_Login")
print("Remaining Tests:", test_cases)


# Example 2: Remove last executed test (stack behavior)
test_cases = ["TC1", "TC2", "TC3"]
last_test = test_cases.pop()
print("Last Executed:", last_test)
print("Remaining:", test_cases)


# Example 3: Remove test by index (failed test)
test_cases = ["TC_Login", "TC_Logout", "TC_Signup"]
del test_cases[1]   # remove "TC_Logout"
print("After Deletion:", test_cases)


# Example 4: Clear test results before new run
results = ["pass", "fail", "pass"]
results.clear()
print("Cleared Results:", results)


# Example 5: Safe remove (avoid crash if item not found)
test_cases = ["TC_Login", "TC_Logout"]

if "TC_Signup" in test_cases:
    test_cases.remove("TC_Signup")
else:
    print("Test case not found, skipping remove")


# Example 6: Process and remove all failed tests
results = ["pass", "fail", "fail", "pass"]
while "fail" in results:
    results.remove("fail")
print("After removing failures:", results)


# =========================
# BONUS (BEST PRACTICE)
# =========================

# Avoid modifying list while looping directly ❌
# Instead use a copy or list comprehension

results = ["pass", "fail", "pass", "fail"]
# Correct way:
results = [r for r in results if r != "fail"]
print("Filtered Results:", results)


# =========================
# KEY LEARNING POINTS
# =========================

# 1. remove() -> by value
# 2. pop() -> by index (and returns value)
# 3. del -> delete by index or entire list
# 4. clear() -> empty list