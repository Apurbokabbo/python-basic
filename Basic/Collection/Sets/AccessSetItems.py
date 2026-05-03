# =========================================================
# SET DATA STRUCTURE - SQA AUTOMATION USE CASE (LEAD LEVEL)
# =========================================================

# In automation testing, we often use SETS when:
# - We need to ensure uniqueness of test cases or data
# - We want fast lookup (O(1) average time complexity)
# - We are comparing expected vs actual results (API/UI validation)

programming = {"Python", "Java", "C#", "C++", "Javascript"}

# ---------------------------------------------------------
# IMPORTANT CHARACTERISTICS OF SET (VERY IMPORTANT IN QA)
# ---------------------------------------------------------
# 1. Unordered collection → No index support
# 2. No duplicates allowed → Automatically removes duplicate data
# 3. Cannot use:
#    - indexing (programming[0])
#    - slicing (programming[1:3])
# 4. Best suited for:
#    - validation
#    - comparison
#    - deduplication


# ---------------------------------------------------------
# ITERATING THROUGH SET
# ---------------------------------------------------------
# Used in automation when validating dynamic datasets

for item in programming:
    print(item)


# ---------------------------------------------------------
# MEMBERSHIP VALIDATION (VERY COMMON IN API TESTING)
# ---------------------------------------------------------
# Example: Check if a feature exists in response payload

if "Go" in programming:
    print("Go is supported")
else:
    print("Go is NOT supported in system")


# =========================================================
# SET OPERATIONS IN REAL SQA AUTOMATION SCENARIOS
# =========================================================

# ---------------------------------------------------------
# ADD / REMOVE OPERATIONS
# ---------------------------------------------------------
programming.add("Go")  # Add new feature validation
programming.remove("Java")  # Remove deprecated feature

# discard() is safer in automation (no exception if missing)
programming.discard("C#")


# ---------------------------------------------------------
# REAL-WORLD SQA EXAMPLE 1: UNIQUE TEST CASE EXECUTION
# ---------------------------------------------------------
# Duplicate test cases are automatically removed

test_cases = {"TC_Login", "TC_Logout", "TC_Signup", "TC_Login"}

print("Unique Test Cases:", test_cases)


# ---------------------------------------------------------
# REAL-WORLD SQA EXAMPLE 2: API RESPONSE VALIDATION
# ---------------------------------------------------------
# Comparing expected vs actual API fields

expected_fields = {"id", "name", "email", "status"}
actual_fields = {"id", "name", "email"}

missing_fields = expected_fields - actual_fields

print("Missing API Fields:", missing_fields)


# ---------------------------------------------------------
# REAL-WORLD SQA EXAMPLE 3: COMMON TEST COVERAGE
# ---------------------------------------------------------
# Finding overlapping test coverage between smoke and regression

smoke_tests = {"TC1", "TC2", "TC3"}
regression_tests = {"TC2", "TC4", "TC5"}

common_tests = smoke_tests & regression_tests

print("Common Test Coverage:", common_tests)


# ---------------------------------------------------------
# REAL-WORLD SQA EXAMPLE 4: MERGING TEST SUITES
# ---------------------------------------------------------
# Union operation ensures no duplicates

all_tests = smoke_tests | regression_tests

print("Combined Test Suite:", all_tests)


# =========================================================
# LEAD SQA KEY TAKEAWAYS
# =========================================================

# ✔ Use SET when:
#    - uniqueness is required
#    - fast lookup is needed
#    - comparing datasets (API/UI/DB)

# ✔ Avoid SET when:
#    - order matters
#    - index-based access is required

# ✔ In automation frameworks (PyTest / Selenium / API):
#    - SET is used for validation layers
#    - ensures clean test data
#    - helps in diff-based testing (expected vs actual)