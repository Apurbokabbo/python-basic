# =========================
# SORTING LISTS
# =========================

programming = [2, 5, 6, 1, 7, 3, 9, 0, 10, 33, 21]

# -------------------------
# sort() -> sorts list in ASCENDING order (default)
# -------------------------
programming.sort()
print("Ascending:", programming)
# Output: [0, 1, 2, 3, 5, 6, 7, 9, 10, 21, 33]


# -------------------------
# sort(reverse=True) -> DESCENDING order
# -------------------------
programming.sort(reverse=True)
print("Descending:", programming)
# Output: [33, 21, 10, 9, 7, 6, 5, 3, 2, 1, 0]



# =========================
# IMPORTANT CONCEPTS
# =========================

# 1. sort() modifies the ORIGINAL list (in-place)
# 2. It does NOT return a new list

# Wrong way
nums = [3, 1, 2]
result = nums.sort()
print(result)   # Output: None

# Correct way
nums = [3, 1, 2]
nums.sort()
print(nums)


# =========================
# sorted() FUNCTION (ALTERNATIVE)
# =========================

nums = [3, 1, 2]

new_sorted = sorted(nums)   # creates NEW list
print("Original:", nums)
print("Sorted Copy:", new_sorted)

# =========================
# CUSTOM SORTING (VERY IMPORTANT)
# =========================

# Sort based on length of string
languages = ["Python", "C", "JavaScript", "Go"]

languages.sort(key=len)
print("Sorted by length:", languages)

# =========================
# SQA ENGINEER RELATED EXAMPLES
# =========================

# Example 1: Sort response times (performance testing)
response_times = [120, 200, 150, 300, 250]

response_times.sort()
print("Fastest to Slowest:", response_times)

response_times.sort(reverse=True)
print("Slowest to Fastest:", response_times)


# Example 2: Sort test execution time
execution_time = [5.2, 1.1, 3.4, 2.0]

execution_time.sort()
print("Execution Time (Ascending):", execution_time)


# Example 3: Sort bug priorities manually (custom order)
# High > Medium > Low
bugs = ["low", "high", "medium", "high"]

priority_order = {"high": 3, "medium": 2, "low": 1}

bugs.sort(key=lambda x: priority_order[x], reverse=True)
print("Sorted Bugs:", bugs)


# Example 4: Sort test cases alphabetically
test_cases = ["TC_Login", "TC_Logout", "TC_Signup"]

test_cases.sort()
print("Sorted Test Cases:", test_cases)


# Example 5: Sort dictionary data (API response simulation)
api_data = [
    {"name": "API1", "response_time": 200},
    {"name": "API2", "response_time": 100},
    {"name": "API3", "response_time": 300}
]

# Sort by response_time
api_data.sort(key=lambda x: x["response_time"])

print("Sorted API Data:", api_data)


# =========================
# KEY DIFFERENCE
# =========================

# sort()   -> modifies original list
# sorted() -> returns new sorted list

# =========================
# KEY LEARNING POINTS
# =========================

# 1. sort() is used for ordering data
# 2. reverse=True for descending order
# 3. key= is powerful for custom sorting
# 4. sorted() is safer if you want to keep original data