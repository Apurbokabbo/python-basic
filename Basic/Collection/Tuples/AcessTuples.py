# =========================================================
# TUPLE - ACCESSING DATA (SQA AUTOMATION CONTEXT)
# =========================================================

# Tuple is similar to a list but:
# ✔ Immutable (cannot be changed after creation)
# ✔ Ordered (supports indexing)
# ✔ Faster than list (useful in automation)

programming = ("Python", "Java", "C#", "C++", "Javascript")


# ---------------------------------------------------------
# INDEX ACCESS
# ---------------------------------------------------------
# Index starts from 0

print(programming[2])
# Output: C#
# (3rd element in tuple)


# ---------------------------------------------------------
# NEGATIVE INDEXING
# ---------------------------------------------------------
# -1 = last element
# -2 = second last element

print(programming[-2])
# Output: C++


# ---------------------------------------------------------
# SLICING
# ---------------------------------------------------------
# tuple[start : end] → end index is excluded

print(programming[2:5])
# Output: ('C#', 'C++', 'Javascript')



# =========================================================
# LEAD SQA REAL-WORLD USE CASES
# =========================================================

# Example 1: API response structure (IMMUTABLE DATA)
api_response = ("200", "Success", "User Created")

print("Status Code:", api_response[0])
print("Message:", api_response[1])


# Example 2: Fixed configuration values
browser_config = ("Chrome", "120.0", "Windows")

print("Browser:", browser_config[0])
print("Version:", browser_config[1])


# Example 3: Test case metadata (unchangeable record)
test_case = ("TC_Login", "High", "Regression")

print("Test Case:", test_case[0])
print("Priority:", test_case[1])


# Example 4: Partial data extraction (slicing)
logs = ("Step1", "Step2", "Step3", "Step4", "Step5")

print("Execution Steps:", logs[1:4])



# =========================================================
# LEAD SQA KEY TAKEAWAYS
# =========================================================

# ✔ Tuple is used when data should NOT change
# ✔ Supports:
#    - indexing
#    - negative indexing
#    - slicing

# ✔ Best for:
#    - API responses (fixed structure)
#    - configuration data
#    - test metadata
#    - constants in automation frameworks

# ✔ Why QA prefers tuple in some cases:
#    - safer (immutable → no accidental change)
#    - faster performance
#    - better data integrity